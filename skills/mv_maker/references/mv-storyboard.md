# MV 分镜脚本 (storyboard.md) 格式规范与用户确认门禁 (mv-storyboard.md)

本文件定义 MV Maker 在 Phase 3 规划完成后输出的 `storyboard.md` 格式规范（参考 `nest_video` 标准分镜格式）、落盘路径、推送与用户确认门禁（Confirmation Gate）以及 Phase 4 的执行消费规则。

---

## 一、定位与落盘路径 (Storyboarding Contract)

`./assets/storyboard.md` 是连接 **Phase 3（分镜规划与剧本设计）** 与 **Phase 4（视频生成）** 的唯一核心工程交付物与事实源。

1. **落盘路径**：必须写入 `/workspace/assets/storyboard.md`（或 `./assets/storyboard.md`）；
2. **单一事实源**：Phase 4 视频生成阶段，Agent 直接根据 `storyboard.md` 中记录的 `shot_NN` 小节、素材列表与 Prompt 逐段调用 `sandbox_generate_video`，不得在生成阶段临时臆造或大幅篡改已确认的分镜内容；
3. **用户确认硬门禁 (Confirmation Gate)**：`storyboard.md` 落盘后，必须先通过 `present_sandbox_file` 推送并触发 `dynamic_questionnaire` 向用户征求确认。**未收到用户确认前，绝对严禁调用 `sandbox_generate_video`**！

---

## 二、storyboard.md 格式规范模板（严格参考标准分镜格式）

```markdown
# storyboard.md

视频比例：16:9
最大分镜时长：{{.max_video_duration}} 秒

## 总览

| Shot | 场次/乐段 | Duration | 衔接 | 景别 | 核心情绪/声学事件 |
|------|----------|----------|------|------|-----------------|
| shot_01 | Intro / 0-15s | 15 | — | 中景/特写 | 蓄势爆发 / Snare Drop |
| shot_02 | Verse 1 / 15-30s | 15 | — | 俯瞰/全景 | 极速推进 / 节奏齐舞 |
| shot_03 | Chorus / 30-45s | 15 | — | 特写/全景 | 高潮爆发 / 标志性 Killing Part |
| shot_04 | Outro / 45-60s | 15 | — | 远景/背影 | 余韵回味 / 渐隐定格 |

总时长：60s

## 通用尾注

{全片每段逐字相同的技术约束与负向词，视频生成时由主 Agent 原样拼接到每段 Prompt 末尾。包含：画质与片基兜底、角色人设与服装稳定不变形、全片不要在同一画面中复制相同主角人物、不要生成水印/logo、保持无字幕（普通字幕由后期统一添加）、严格以 @视频1 为全片唯一背景音乐与口型对齐基准、严禁生成任何与 @视频1 无关的其他BGM或杂乱音轨。}

## shot_01

- ImageList:
  - assets/character_member1.png
  - assets/character_member2.png
  - assets/character_member3.png
  - assets/character_member4.png
- VideoList:
  - assets/seg_01_audio.mp4
- AudioList: []
- Prompt: |
  @图片1 为Member 1 C位主唱，@图片2 为Member 2 领舞，@图片3 为Member 3 Rap担当，@图片4 为Member 4 副主唱，锁定各成员五官、发型与胶囊系列服装款式。@视频1 提供全段唯一背景音乐与节拍时间轴，不提供画面。画面动作与节奏必须严格跟随 @视频1 的音频作为 BGM，不擅自编曲，严禁生成任何其他无关背景音乐或杂乱音轨。
  High-Fashion 顶级先锋时尚大片质感，24mm广角大透视镜头，直闪摄影 (Direct Flash) 与强反差黑白水泥建筑光影，1/500s 高速快门冷酷定格。
  镜头1 (0-2s 全景微仰拍)：四位成员背对镜头站在极简纯黑水泥长廊中央，头顶两排冷白光束瞬间暴闪，光线在肩膀勾勒出强烈冷白轮廓光 (Rim Light)，背光面沉入深黑漫反射阴影。
  镜头2 (2-5s 硬切领舞近景)：领舞在重音落下瞬间单手向画外凶猛挥砍撕裂空间，伴随 1 帧黑白反相冲击帧 (1-Frame Invert Flash)，画面微震 2 像素强化打击感。
  镜头3 (5-8s 特写主唱咬字)：主唱眼神锐利直视镜头，全程在唱，精准咬字口型：{歌词第一句}。
  镜头4 (8-11s 中景齐舞爆发)：四人整齐划一划出利落手部波浪，动作在底鼓重击瞬间做一次 10% 数字变焦 (Digital Punch Zoom) 瞬间放大并弹回强化卡点。
  镜头5 (11-15s 大字切割转场)：紧凑实心无衬线粗体字【OVERFLOW】横扫全屏呈现前后夹心视差，全员在尾拍瞬间利落定格。

## shot_02

- ImageList:
  - assets/character_member1.png
  - assets/character_member2.png
  - assets/character_member3.png
  - assets/character_member4.png
- VideoList:
  - assets/seg_02_audio.mp4
- AudioList: []
- Prompt: |
  {完整视频 Prompt，格式同上}
```

---

## 三、格式要点与编写铁律

1. **总览表规范**：
   - 表头固定为：`| Shot | 场次/乐段 | Duration | 衔接 | 景别 | 核心情绪/声学事件 |`；
   - `Duration` 列：必须为**纯整数秒**（如 15、30、12 等），严禁出现 13.7s、24.2s 浮点数；
   - `衔接` 列：MV 各乐段（Verse/Chorus等）属于独立换景换盒大跳切，默认填 `—`；
   - 表格下方必须附带 `总时长：XXs` 汇总行。
2. **通用尾注规范 (General Suffix)**：
   - `## 通用尾注` 紧跟总览表，只写一次；
   - 收录全片每段完全相同的质量与技术约束（画质、防水印、禁BGM、保持无字幕、防变形克隆人等）；
   - **段内 Prompt 不重复通用尾注**：在 Phase 4 实际调用 `sandbox_generate_video` 时，由 Agent 自动把通用尾注内容追加到每个 `shot_NN` 的 Prompt 末尾。
3. **分段 `shot_NN` 规范与四大质检验收**：
   - 每个 `shot_NN` 对应一次 `sandbox_generate_video` 调用；
   - 包含四个字段：`ImageList`（纯人物参考图列表，严禁场景图）、`VideoList`（对应黑屏音频切片）、`AudioList`（通常为 `[]`）、`Prompt: |`（多行缩进 Prompt）；
   - `Prompt` 内部必须按四层结构编写（素材职务声明 + 全局概述 + 秒数镜头序号推进 + 口型咬字），且必须严格过四大质检门禁：
     - ① **歌词画外音与精准唱演门禁 (Lyrics Voice-Over & Targeted Lip-Sync)**：绝大多数微镜头（空镜/手部特写/背影/远景/剧情演戏）Prompt 中严禁出现任何歌词文本，严禁出现“精准咬字口型”或口型字样；微镜头标题统一采用 `(秒数区间 + 景别动作)` 格式（如 `镜头1 (0-2s 全景微仰拍)`、`镜头2 (2-5s 硬切领舞近景)`），**严禁在标题括号内堆砌歌词文本与唱演标签（如严禁写 唱演：歌词文本）**；仅在极少数正面特写确需开口时在句末自然标注 `{歌词}`；
     - ② **实体空间与零白底 (Zero-White-Void)**：严禁写 `纯白底`、`极简白底`、`冷白通道`，第二层全局概述定调世界观，微镜头轻量聚焦运镜动作，不逐镜死板堆砌三层；
     - ③ **特写叙事因果链 (Action-Causality)**：严禁商品目录式无因果部位陈列（严禁单纯堆砌眼/手/鞋三屏），每个特写必须遵循 [察觉/动机 $\rightarrow$ 动作执行 $\rightarrow$ 物理反馈]；
     - ④ **破风动能与多机位冲刺 (Dynamic Locomotion)**：严禁单一机位背追/正面原地跑步机，冲刺必须在 2~3 秒内串联贴地飞驰、侧面广角超车与急刹滑行多机位跳切。

---

## 四、推送展示与用户确认流程 (Confirmation Gate Workflow)

在 Phase 3 完成分镜规划并使用 `sandbox_write` 写入 `./assets/storyboard.md` 后，必须严格执行以下三步确认门禁：

```text
       ┌────────────────────────────────────────────────────────┐
       │   1. sandbox_write 写入 ./assets/storyboard.md          │
       └──────────────────────────┬─────────────────────────────┘
                                  │
                                  ▼
       ┌────────────────────────────────────────────────────────┐
       │   2. present_sandbox_file 推送分镜文档 (interrupt=false) │
       │      - filepath: "./assets/storyboard.md"              │
       │      - 展示分镜方案给用户细看，不中断后续问卷发送            │
       └──────────────────────────┬─────────────────────────────┘
                                  │
                                  ▼
       ┌────────────────────────────────────────────────────────┐
       │   3. dynamic_questionnaire 发送分镜确认问卷 (硬停等待)   │
       │      - 选项 A: 满意，开始生成视频 (推荐)                    │
       │      - 选项 B: 需要调整分镜与画面                          │
       └──────────────────────────┬─────────────────────────────┘
                                  │
                  ┌───────────────┴───────────────┐
                  ▼                               ▼
        【用户确认：满意开始】            【用户要求修改】
                  │                               │
                  ▼                               ▼
       进入 Phase 4 逐段生成视频           根据修改意见调整 storyboard.md
                                          再次推送并确认
```

### 问卷调用参数示例：
```json
{
  "title": "MV 分镜方案确认",
  "questions": [
    {
      "id": "confirm_storyboard",
      "title": "MV 分镜脚本已规划完毕（共 N 个分段，总时长 Xs），请确认是否开始生成视频？",
      "type": "radio",
      "options": [
        {
          "label": "满意，开始生成视频 (推荐)",
          "description": "立即进入视频生成阶段，按分镜方案并行生成各分段并合成交付成片"
        },
        {
          "label": "需要调整分镜与画面",
          "description": "提出具体调整意见（如调整某段景别、动作、文字特效或场景风格）"
        }
      ]
    }
  ]
}
```

---

## 五、Phase 4 消费与生成规则

收到用户确认（`满意，开始生成视频`）后，Agent 进入 Phase 4：
1. 逐段读取 `storyboard.md` 中的 `shot_NN` 小节；
2. 提取每段的 `ImageList`、`VideoList`、`Duration`；
3. 将 `## 通用尾注` 中的质量与技术约束文字拼接到每段 `Prompt` 末尾；
4. 调用 `sandbox_generate_video` 并行或顺序生成各分段；
5. 所有分段生成完成后，进入 Phase 5 装配成片。
