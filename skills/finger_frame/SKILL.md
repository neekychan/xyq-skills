---
name: finger_frame
display_name: 手指取景框
description: "手指取景框特效视频：用户上传双手比取景框手势的视频，取景框内呈现 AI 重绘的漫画风平行世界——框内人物变身为蒙面英雄/黑帮老大等反差形象，随手势合拢-张开完成变身，框外保留原视频。适用于用户提到手指取景框、手势框、取景框特效、finger frame、框内变身/换风格等意图。需要用户提供包含双手取景框手势的视频素材。"
tools: ["sandbox_generate_video"]
---

# 手指取景框特效视频

用户上传一段"双手拇指+食指围成取景框"的手势视频，产出平行世界特效成片：取景框内是 AI 重绘的漫画风异世界（全片单一画风，随"合拢再张开"手势从日常装扮变身为反差酷形象），框外保持原视频；"手指交叉"手势可将内外反转（框外变异世界）。框沿霓虹流光描边，异世界区域带间歇的信号干扰特效。

本 Skill 的参考文件路径：`/workspace/.skills/finger_frame/references/`

```
references/
├── finger_frame-prompt.md   # 重绘 Prompt 骨架 + 对齐后缀 + 禁写清单 + 画风库/变身形象库（步骤四前必读）
└── scripts/
    ├── setup_finger_frame.sh  # 环境引导（步骤〇）
    ├── detect_frame.py        # 手指四边形检测 → template.json（步骤二）
    ├── composite.py           # 合成（步骤五）
    └── models/                # 手部关键点模型（随包分发，勿改动）
```

## 〇、环境引导（进入 skill 后立即执行，幂等）

```bash
bash /workspace/.skills/finger_frame/references/scripts/setup_finger_frame.sh
```

- 输出 `SETUP_OK` → 继续。
- 输出 `SETUP_FAIL` → 重试一次；仍失败则如实告知用户特效环境不可用，停止流程，不要自行改装环境或跳过检测直接生成。

## 一、素材确认

- 用户已上传视频 → 直接使用。未上传 → 请用户上传"双手比取景框手势"的视频后再继续，并提示拍摄要点：双手拇指与食指张开围成矩形、手保持在画面内、想触发变身时把双手合拢再重新张开。
- 视频时长 > {{.max_video_duration}} 秒 → 记入待确认项（见步骤三问卷）。

## 二、取景框检测（先告知用户"检测处理中，预计需要几分钟"）

```bash
python3 /workspace/.skills/finger_frame/references/scripts/detect_frame.py upload/用户视频.mp4 --job main
```

> `sandbox_bash` 必须传 `Timeout: 600000`（CPU 逐帧推理，30 秒视频约需 2~5 分钟）。

脚本 stdout 即产物凭证：末行 `wrote <template路径> frames=N coverage=P% segments=K inversions=M duration=Ss` 出现即成功，**禁止**再用 `ffprobe`/`ls`/`cat` 校验。按 stdout 事实分流：

| 事实 | 动作 |
|------|------|
| coverage < 30% | 告知用户视频中取景框手势过少、效果无法保证，建议重拍（给出步骤一的拍摄要点），**停止流程不进生成** |
| segments = 1 | 单段模式：告知用户未检测到"合拢再张开"的切换手势，全片直接呈现变身后形象（无日常→变身的递进） |
| segments ≥ 2 | 变身模式：阶段一为所选画风下的日常装扮，手势切换后变身为反差形象；**至多 2 个阶段、变身一次**（segments 更多时相邻段合并，见 prompt 文件第一节） |
| inversions ≥ 1 | 告知用户检测到 M 次"手指交叉"手势：交叉后画面**内外反转**——框外变为异世界、框内保留现实，直到再次交叉恢复。反转由合成脚本按模板自动完成，**不进入重绘 Prompt** |

检测通过后，立即生成**手势追踪预览**发给用户（重绘参数传 `none` = 只叠加霓虹框不换画面）：

```bash
python3 /workspace/.skills/finger_frame/references/scripts/composite.py \
  upload/用户视频.mp4 none /tmp/finger_frame/main/template.json output/gesture_preview.mp4
```

随后 `present_sandbox_file(filepath="output/gesture_preview.mp4", interrupt=false)`（不中断，紧接问卷一并等待用户反馈）。预览让用户在消耗生成额度前确认追踪效果；用户若反馈框不准，引导重拍，不进入重绘。

## 三、关键确认（dynamic_questionnaire，一次合并，已明确项跳过）

出问卷前先读取 `references/finger_frame-prompt.md` 第四节：**画风库与变身形象库是问卷选项的唯一来源，禁止自创或改名**（如"水彩绘本风""赛博偶像"这类库外选项）。

- **画风**（必问，除非用户已指明具体画风或经济模式）：从画风库 4 选 1（全片统一，AI 重绘推荐项放首位标注推荐），**并固定追加最后一个选项"经济滤镜特效（无需积分）"**（描述注明：本地滤镜逐段轮换如热成像/点阵像素，**无需消耗积分**、几分钟出片，但只做画面处理、无换装变身）。经济模式的存在只靠这个选项让用户感知，**不单独设"制作模式"问题，该选项任何情况下不得省略，"无需积分"必须出现在选项标题**。用户选经济滤镜 → 走步骤三·五，变身形象答案忽略。
- **变身形象**（与画风同一问卷）：按形象库排序优先、**只挑与原视频人物性别匹配**（"适用"列）的 3-4 个作为选项让用户选 1 个（选项描述点出具体装扮，如"蒙面英雄——全脸面罩+荧光线条战衣"）；用户输入中已指明则跳过。
- **滤镜选择**（仅用户输入已直接指明经济模式时单独问）：从 gray/duotone/pixel/negative/posterize/thermal 中选 K 种（中文名展示：黑白胶片/青橙单色/点阵像素/负片反转/色阶海报/热成像），多段时逐段轮换。经问卷选中"经济滤镜特效"的场景不再补问，直接按段数自动轮换（用户点名了滤镜则用指定的）。
- **超长处理**（仅 AI 模式且时长 > {{.max_video_duration}} 秒时问）：裁剪到前 {{.max_video_duration}} 秒（推荐，效果最稳）/ 切段逐段重绘再拼接（完整保留，耗时更长）。经济模式无时长限制，不问。
- 不要问段落结构、生成次数等技术分流维度；segments 数量以检测结果为准，不作为问卷选项。

## 三·五、经济特效模式（用户选择后走此分支，跳过步骤四）

无需调用生成工具，直接合成（滤镜名逗号拼接，数量与 segments 对应）：

```bash
python3 /workspace/.skills/finger_frame/references/scripts/composite.py \
  upload/用户视频.mp4 "filter:thermal,pixel" /tmp/finger_frame/main/template.json output/final.mp4
```

> 传 `Timeout: 600000`。完成后直接进入步骤五的交付（present）。

## 四、全量重绘（读取 `references/finger_frame-prompt.md` 后构造 Prompt）

调用 `sandbox_generate_video`，按 prompt 文件的骨架、对齐后缀、检查清单执行：

- 常规：单次调用，`VideoList`=[原视频]，`Duration`=视频时长，Prompt 按检测 stdout 的 segment 区间逐阶段写（"阶段N（X秒到Y秒）+ 该阶段手部动作 + 手势切换因果句 + 画风/装扮/场景三要素"三重锚定，时间照抄不推算；单段=全片变身后形象，多段=日常装扮→变身）。
- 裁剪模式：先 `ffmpeg -y -i upload/用户视频.mp4 -t {{.max_video_duration}} -c:v libx264 -crf 18 -c:a aac output/clip.mp4`，对裁剪后视频重跑步骤二检测，再单次生成。
- 切段模式：按 prompt 文件第六节切段，画风与变身状态跨段连续，逐段调用。

工具返回产物路径即成功；仅工具明确报错时可重试，同参数至多一次。

## 五、合成与交付

```bash
python3 /workspace/.skills/finger_frame/references/scripts/composite.py \
  <原视频> <重绘视频> /tmp/finger_frame/main/template.json output/final.mp4
```

> 同样传 `Timeout: 600000`。切段模式先 `ffmpeg concat` 拼接各段重绘视频再合成。

stdout 末行 `wrote output/final.mp4` 出现即成功。随后：

```
present_sandbox_file(filepath="output/final.mp4", interrupt=true)
```

## Ref 加载总表

| 文件 | 内容 | 加载时机 |
|------|------|---------|
| `finger_frame-prompt.md` | Prompt 骨架/对齐后缀/禁写清单/画风库与变身形象库/切段规则 | 步骤四构造 Prompt 前 |

## 红线

1. 未见 `SETUP_OK` 不进入后续步骤。
2. 脚本与生成工具的 stdout/返回即事实：禁止 `ffprobe`/`ls`/`cat` 二次校验产物，禁止探测性 bash（`which`/`pip list` 等）。
3. 中间产物（template.json、切段素材、模型缓存）一律在 `/tmp/finger_frame/`，不落 workspace；交付物只有 `output/gesture_preview.mp4`（手势预览）与 `output/final.mp4`（成片）。
4. coverage < 30% 必须止损，不得带病进入生成消耗额度。
5. 交付必须以 `present_sandbox_file(interrupt=true)` 收尾，不可省略。
6. 单次 `sandbox_generate_video` 的 `Duration` 不得超过 {{.max_video_duration}} 秒；切段模式失败不得回退为超限的单次生成。
7. 合成阶段（composite.py）报错或提示"重绘视频不可读/已降级"时，**这是终态不是故障**：禁止重新调用 `sandbox_generate_video`（换风格/换参数/切段重试都不行），禁止用 ffprobe/ffmpeg 检查或修复该文件，禁止重跑合成——生成额度已消耗且重跑结果相同。唯一正确动作：交付本次合成产物并向用户如实说明。
8. 重绘 Prompt 的每个阶段必须包含人物改造（服装/发型/妆造）与场景改造描述，且画风必须为**非写实的漫画/动画类**（人脸与双手也重绘成漫画质感，全画面不残留写实区域）、全片统一——本 skill 卖的是"平行世界变身"，只调色不换装、或保持写实人脸/写实手只换装扮的 Prompt 禁止提交。Prompt 描述的是**整个画面**的重绘，禁止出现"框内/框外/蒙版/反转"等后期合成概念（窗口效果由合成脚本按模板完成）。
