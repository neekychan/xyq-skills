---
name: hyperframes
description: 使用 HyperFrames 按用户 prompt 直接编写代码生成视频。语音使用 edge-tts 生成；幂等创建 hyperframes-project，并返回最终 MP4。
---

# HyperFrames Code To Video

## 用户输入

- `创意需求`: 必填。用户的创意需求，包括视频时长、目标、受众、风格、市场、语言等。
- `图片素材`: 选填。图片素材，可用于产品展示、品牌画面、截图说明或视觉参考。

## Agent loop 预算（硬约束）

全程上限 **50 轮**，按阶段分配，超出即收敛：

| 阶段 | 预算 |
|---|---|
| 1. 初始化（归一化 + 建项目 + 抓取） | ≤ 5 轮 |
| 2. 策划（PLAN.md + narration.txt） | ≤ 12 轮 |
| 3. 制作（旁白 + index.html） | ≤ 18 轮 |
| 4. 验证与交付 | ≤ 10 轮 |

阶段合计 45 轮，剩余 5 轮作为机动和最终汇报预留。

- 有 loop 状态就先读：`current_loop` / `loop_limit` / `remaining_loops`；没有状态也按 50 轮自行计数。
- 只路由一次；同一阶段内能合并的读写放同一轮批量执行，不拆成多轮。
- 任一命令失败：定位根因修一次、重跑一次；仍失败就停止重试，带路径/日志交 blocker。render-debug 全程最多 2 轮。
- 第 **40** 轮起停止加料（不开新 workflow、不再联网检索），收敛产物，跑最小验证。
- 第 **45** 轮起只修阻断问题；保留最后 2 轮做校验汇报和最终回复。

## 路由

先判断创意需求是否命中专用hyperframe下 workflow skill。命中则直接加载执行该 skill，**停止本文档后续流程**。这些 `/xxx` 是 agent workflow skill，不是 `hyperframes` CLI 子命令；语音若没有，仍用 edge-tts。

| Skill | 方向 | 典型输入 |
|---|---|---|
| `/product-launch-video` | 产品发布 / SaaS 宣传 / 功能亮相视频 | 产品 URL、营销 brief、产品脚本 |
| `/website-to-video` | 把真实网站截图和品牌资产做成网站导览 / showcase | 普通网站 URL |
| `/faceless-explainer` | 无真人讲解视频，视觉全靠文字、图形、图表、抽象画面生成 | 一个主题、文章、笔记、brief |
| `/pr-to-video` | 把 PR diff / commit 讲成代码变更解说视频 | GitHub PR URL 或 repo PR |
| `/embedded-captions` | 给已有 talking-head 视频加字幕/特效字幕 | 已有口播视频 |
| `/graphic-overlays` | 给已有视频加标题卡、lower-third、数据卡、引用卡、侧栏等包装层 | 已有采访/播客/口播视频 |
| `/motion-graphics` | 短、无旁白、运动本身是重点的动效片段 | 数字动效、logo sting、tweet 动画，通常 10s 左右 |
| `/slideshow` | HyperFrames 交互式幻灯片/演示 deck | pitch deck、presentation；默认产物不是 MP4 |
| `/general-video` | 兜底通用视频创作 | 自定义长短视频、montage、title card、loop |

命中 `/general-video` 或没有精确匹配时，按下面 4 步通用流程执行。

## 执行步骤

### 1. 初始化：归一化输入 + 幂等建项目 + 可选抓取（单轮批量执行）

```bash
INPUT_URL="<input_url>"
USER_PROMPT="<user_prompt>"

NORMALIZED_URL=""
if [ -n "$INPUT_URL" ]; then
  case "$INPUT_URL" in
    http://*|https://*) NORMALIZED_URL="$INPUT_URL" ;;
    *) NORMALIZED_URL="https://$INPUT_URL" ;;
  esac
fi

if [ ! -f hyperframes-project/index.html ]; then
  hyperframes init hyperframes-project \
    --non-interactive \
    --skip-skills \
    --example blank \
    --resolution landscape
fi

cd hyperframes-project
rm -rf capture capture.json
if [ -n "$NORMALIZED_URL" ]; then
  hyperframes capture "$NORMALIZED_URL" -o capture --json > capture.json
  test -s capture.json
fi
```

要求：

- `USER_PROMPT` 是主输入；URL 只作为素材来源，不覆盖用户创意需求。
- `--skip-skills` 在部分 HyperFrames 版本中可能仍会触发 skill 检查，不要当成离线保证。
- 素材只选与创意需求、脚本、分镜直接相关的；不用模糊、重复、无关广告、cookie banner、页脚素材。
- capture 失败不重试第二次、不伪造网页信息：在 `PLAN.md` 标注失败原因，继续用用户 prompt 做通用表达。

### 2. 策划：写 PLAN.md 和 narration.txt

在 `hyperframes-project` 内写入两个文件：

- `PLAN.md`: 按序包含四节——**素材与事实**（用户 prompt、可用素材、可确认/不可确认信息、来源链接）、**Brief**（目标、受众、市场、风格、语言、时长、画幅、核心诉求）、**音频策略**（是否生成旁白、是否加入背景音乐、背景音乐风格、音量、选择原因）、**旁白脚本**、**分镜**（画面元素、字幕、动效、时间轴）。
- `narration.txt`: 从旁白脚本提取的纯旁白文本。
- 有声视频必须先设计开场音画同步：如果旁白从 0s 或接近 0s 开始，0s-0.5s 内必须已经出现标题、主体图形、字幕、关键符号或明确运动线索；禁止前 4 秒只有背景色、渐变、纹理、水印或播放器控件。

要求：

- 用户没给 URL/图片且主题公开时，可联网查参考材料，但只查与需求直接相关的公开信息；用户要求"只基于我给的素材/URL"时禁止联网补充。
- 不编造数字、案例、引用、时间线或产品承诺；搜不到可靠来源就按用户 prompt 做通用信息图表达，并在 `PLAN.md` 标注素材不足。
- 缺少画幅时默认 16:9 横屏；每个场景只表达一个重点；旁白短句口播，顺序与画面主题一致。

### 3. 制作：旁白音频 + index.html

**旁白（默认生成；用户明确要求"无声 / 静音 / 不要旁白 / no voice"时跳过）：**

- 默认不加速，不设置 `--rate`；默认音色 `zh-CN-XiaoxiaoNeural`。
- 用户指定音色时就近选择：女声温和 `zh-CN-XiaoxiaoNeural`、女声活泼 `zh-CN-XiaoyiNeural`、男声清晰 `zh-CN-YunxiNeural`、男声稳重 `zh-CN-YunjianNeural`；指定其它音色/地区/语言时先 `edge-tts --list-voices` 再就近选。

```bash
cd hyperframes-project

VOICE="${VOICE:-zh-CN-XiaoxiaoNeural}"

if [ "${RENDER_AUDIO:-true}" = "true" ]; then
  EDGE_TTS=edge-tts
  if ! command -v edge-tts >/dev/null 2>&1; then
    python3 -m venv /tmp/hyperframes-edge-tts-venv
    /tmp/hyperframes-edge-tts-venv/bin/python -m pip install edge-tts
    EDGE_TTS=/tmp/hyperframes-edge-tts-venv/bin/edge-tts
  fi

  "$EDGE_TTS" \
    --voice "$VOICE" \
    --text "$(cat narration.txt)" \
    --write-media narration.mp3

  test -s narration.mp3
  ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 narration.mp3
fi
```

**index.html：**

- HTML 是最终视频的 source of truth；时间轴、字幕、画面元素与 `PLAN.md` 分镜对齐。
- 有声视频引用 `narration.mp3`；无声视频不生成 `narration.mp3`、不写 `<audio>`，时长以 `PLAN.md` 目标时长为准。
- 第一场景必须从 `data-start="0"` 开始，并且在 0s-0.5s 内出现有效主体：标题、关键词、图形、关系图、字幕、图标、线条动画或其它用户可理解的内容。
- 如果旁白 0s 起播，首帧不能只显示背景；如果需要淡入，主体淡入延迟不得超过 0.3s，淡入时长不得超过 0.6s。
- 避免不确定的远程字体、远程脚本或不可控资源；动画出场/退场在场景边界清理，避免元素残留。

**音画一致性硬约束：**

- 旁白、字幕、画面主体必须讲同一件事：当前旁白讲到的概念、步骤、关系或结论，画面中必须同步出现对应标题、关键词、图形、标注或动效。
- 禁止出现“旁白讲 A，画面还停在 B”超过 1 秒；跨场景转场时也必须保留当前旁白对应的字幕或关键词，避免音频已经进入下一句但画面仍是上一段。
- 每个分镜必须在 `PLAN.md` 里写清楚：时间段、旁白句子、画面主体、字幕关键词；写 `index.html` 时按这个表对齐 `data-start` / `data-duration` / 动画时间。
- render 后抽帧检查时，不只看是否黑屏，还要核对截图时间点是否和该时间点旁白内容一致；发现音画错位，优先调整场景 `data-start` / `data-duration`、字幕时间和主体入场时间。

**背景音乐（按 PLAN.md 决策，可选）：**

- 用户明确要求优先：不要音乐、静音、使用指定音乐、指定音乐风格，都按用户要求执行。
- 用户没有说明时按场景判断：产品宣传、发布、showcase、通用解说、幻灯片、montage、情绪节奏明显的视频，可以加入低音量背景音乐；PR/代码讲解、技术教程、数据密集旁白、已有口播视频加字幕、或任何会影响语音清晰度的场景，默认不加背景音乐。
- 若加入背景音乐，只使用本地化/已冻结素材，命名为 `bgm.*`；音量必须弱于旁白，通常 `data-volume="0.08"` 到 `0.18`，有旁白时优先 `0.06` 到 `0.12`。
- BGM 需要覆盖完整视频时长，可循环、裁剪或淡入淡出；不要靠远程音频链接，不要让音乐抢对白或遮盖关键信息。
- 不加背景音乐时，不生成 `bgm.*`，不写对应 `<audio>`。

**黑屏防护硬约束：**

- composition root 只负责尺寸和裁剪，不承载背景色/背景图；所有全屏背景必须放到 root 内第一个 full-bleed 子节点上：`position:absolute; inset:0; width:100%; height:100%`，避免 render 阶段丢 root background 导致黑屏。
- 所有可见 timed clip、`<video>`、`<audio>` 必须是 composition root 的直接子节点；不要把 clip/media 包在 wrapper 或 sub-composition template 里。需要动画 wrapper 时，把 wrapper 放进 clip 内部。
- 禁止动画 `display` / `visibility`，禁止对未来场景 clip 做 `gsap.set()`；场景显隐由 `data-start` / `data-duration` 管，转场只动画内部 wrapper 的 `opacity` / `x` / `y` / `scale` / `rotation`。
- 所有 DOM `id` 必须全局唯一，尤其是 `<img>` / `<video>` / `<audio>`；多场景统一加 scene 前缀。
- 渲染关键资源必须本地化，禁止依赖远程图片、字体、脚本、`fetch`、`Date.now()`、`Math.random()`、`requestAnimationFrame` 驱动画面；动画必须由同步创建的 paused timeline 驱动，并注册到 `window.__timelines[compositionId]`。
- 黑屏不只等于纯黑。只有背景色、渐变、纹理、水印或播放器控件，但没有主体内容，也算空画面失败。
- 有声视频的任何旁白时间段都不能出现空画面；尤其检查 0s、0.5s、1s、2s、3s、4s。若这些帧只有背景，必须回到 `index.html` 修首场景内容和入场时间，不能交付。

### 4. 验证与交付（单轮批量执行）

```bash
cd hyperframes-project

hyperframes lint .
hyperframes render --output hyperframes-output.mp4 --quality standard
ffprobe -v error -show_streams hyperframes-output.mp4
hyperframes snapshot . --at 0,0.5,1,2,3,4 --no-end
hyperframes snapshot . --frames 30
```

完成标准：

- lint 无 error；render 成功；`hyperframes-output.mp4` 存在且非空。
- 有声视频时长与 `narration.mp3` 基本一致；无声视频与 `PLAN.md` 目标时长基本一致。
- render 后必须做开场专项 snapshot：`hyperframes snapshot . --at 0,0.5,1,2,3,4 --no-end`，只要旁白已开始，画面必须有标题、字幕、图形、主体元素或明确动效；不能只有背景色、渐变、纹理、水印或播放器控件。
- 全片抽帧使用 `hyperframes snapshot . --frames 30`；任意一张出现纯黑、空白、只有背景、只有音频无画面，都视为失败。

最终回复包含：最终回复包含：最终 MP4 路径；是否使用 URL / 图片素材；是否生成旁白；是否加入背景音乐及原因；lint / render / ffprobe 校验结果；如有失败或素材不足，明确说明 blocker 或降级方式。

## 产物

全部在 `hyperframes-project/`：

- `PLAN.md`
- `narration.txt`
- `narration.mp3`，仅有声视频
- `index.html`
- `hyperframes-output.mp4`
- `capture/` 与 `capture.json`，仅有 URL 时

## 失败处理

均遵守 loop 预算的"修一次、重跑一次"上限：

- URL 抓取失败：记录到 `PLAN.md`，继续基于用户 prompt 生成，不编造网页事实。
- TTS 失败：重试一次；仍失败时在最终回复标注 blocker，或询问是否接受无声版。
- lint 失败：修 `index.html`，不要跳过 lint。
- render 失败：看错误日志和 `hyperframes doctor`，定位 Chrome、ffmpeg、资源路径或 HTML runtime 问题；最多 2 轮 render-debug。
- 时长不匹配：缩短旁白或调整分镜时间轴，不要靠加空白尾帧凑时长。
