---
name: story_short_film
display_name: 剧情短片制作
description: "当用户要求根据剧本做短片、剧情短片、微电影、微剧片段、故事短片、角色剧情演绎等叙事剧情类视频创作时使用本 skill；支持将用户上传剧本或一句话创意制作成完整剧情短片。流程为：统一项目制作单 → 元素资产生成 → 故事板 → 镜头视频生成 → 音频层生成 → 最终剪辑。统一项目制作单合并剧本提取、内容分析和制作规格；旁白与画面角色分离；用户修改后仅更新受影响环节及下游产物。"
tools: ["sandbox_generate_image", "sandbox_generate_video", "sandbox_generate_audio", "render_video"]
---

# 剧情短片制作 Skill

本 Skill 负责剧情短片的完整制作管线，并严格执行“关键阶段暂停确认”原则。

本 Skill 的参考文件路径：`/workspace/.skills/story_short_film/references/`

```text
references/
├── shortfilm-rules.md                  # 确认规则、依赖、用户变更影响分析与生成红线
├── shortfilm-project-brief.md          # 合并剧本提取、内容分析和制作规格，输出 Project_Brief.md
├── shortfilm-content-analysis-rules.md # Project Brief 内部使用的内容类型分析规则
├── shortfilm-assets.md                 # 元素资产、角色/旁白分离、element_id 与音色锚定
├── shortfilm-storyboard.md             # 故事板、画面角色/音频实体分离与内部剪辑
├── shortfilm-prompt.md                 # 图像、关键元素、关键帧和视频 Prompt 规范
├── shortfilm-audio.md                  # 对白、旁白、BGM、音效与音频层确认
└── shortfilm-editing.md                # 最终剪辑、视频合成与交付
```

## 一、任务边界

本 Skill 默认交付一个完整剧情短片项目。必须在统一项目制作单、元素资产、故事板、镜头视频、音频层和最终交付等关键阶段停下来，收到用户明确确认后才进入下一阶段。

适用：根据剧本做短片、剧情短片、短片、微电影、微剧片段、故事短片、角色剧情演绎、故事类短视频。

排除：
1. 动物主角且重点为萌宠表达 → 优先 `pet_video`。
2. 核心为单段武打动作高光 → 优先 `fight_scene`。

## 二、执行流程（多阶段暂停确认）

### 阶段 1：统一项目制作单确认

读取 `shortfilm-project-brief.md`，并按需使用 `shortfilm-content-analysis-rules.md` 完成内部内容判断。

用户已上传剧本则忠实解析；用户未上传剧本则分两轮卡片收集核心需求和风格约束并起草完整剧本。在同一份 `Project_Brief.md` 中依次完成：剧本提取、内容分析、剧情短片灵感参考和制作规格。

`Project_Brief.md` 必须包含故事结构、实体表、场景、准确台词、动作节点、内容定位、参考手法、交付参数、视觉与摄影、角色与场景规格、声音、约束、验收标准和待确认项。

旁白必须标记为独立声音实体。除非剧本明确其真实出镜，否则设置为 `entity_type=narrator`、`visual_presence=off_screen`，不得作为画面角色。

- **文件确认门**：展示 `Project_Brief.md` 的核心确认摘要和待确认项。收到明确确认前，不得进入元素资产阶段。

### 阶段 2：元素资产生成确认

读取 `shortfilm-assets.md`。

如果用户已经上传元素资源，直接绑定为相应 key_elements 的资产；否则，为已确认的画面角色、关键地点/场景和关键道具生成图像。为有对话台词的画面角色建立 `key_element_audio`。画外旁白只建立声音参考，不生成角色图、不进入 ImageList。

- **暂停并确认**：展示所有元素资产和音色方案，等待用户确认。确认前不得进入故事板设计。

### 阶段 3：故事板确认

读取 `shortfilm-storyboard.md`。

基于已确认的 `Project_Brief.md` 和元素资产生成故事板，包括关键元素、镜头列表和 audio_layers。每个镜头必须分开记录 `visible_entities` 与 `audio_entities`；画外旁白只进入 narration/audio_layers，不进入 `visible_entities`。

- **暂停并确认**：输出故事板列表，等待用户确认。确认前不得进入镜头视频生成。

### 阶段 4：镜头视频生成确认

读取 `shortfilm-prompt.md`。

为每个镜头生成最终视频；ImageList 只包含当前镜头物理可见的角色、场景和道具。AudioList 只传入当前镜头实际需要口型或角色声音一致性的说话角色音频；画外旁白不作为视觉或口型条件传入。

- **暂停并确认**：展示镜头视频结果，等待用户确认。确认前不得进入音频层生成。

### 阶段 5：音频层生成确认

读取 `shortfilm-audio.md`。

基于故事板生成所有 audio_layers，包括独立旁白、BGM、音效和必要的角色语音。画外旁白作为后期 narration 混入，不要求画面角色口型。

- **暂停并确认**：展示音频层结果，等待用户确认。确认前不得进入最终剪辑。

### 阶段 6：最终剪辑与交付

读取 `shortfilm-editing.md`。

当所有资源就绪后，按分镜和时间轴顺序组装所有镜头、旁白音轨和 BGM，进行最终剪辑合成。

- **最终交付**：推送 `output.mp4`。最终交付后停止自动推进，等待用户反馈。

## 三、用户变更处理

用户修改任何信息后，先定位唯一权威产物，再执行最小影响更新：

1. 剧情、角色、旁白、场景、台词、参考手法或制作规格 → 更新 `Project_Brief.md`。
2. 角色图、场景图、道具、音色资产 → 更新元素资产记录。
3. 镜头、动作、元素引用或音频规划 → 更新 `storyboard.md`。
4. 已生成镜头、音频或最终剪辑 → 只更新直接受影响的媒体和时间线。
5. 向用户展示“已更新、不受影响、需重新确认、需重生成”四项清单。

下游文件不得静默覆盖上游事实；发现冲突时必须先回到对应权威产物。禁止因局部修改而盲目全量重做。

## 四、Ref 加载总表

| Ref | 内容 | 加载时机 |
|-----|------|----------|
| `shortfilm-rules.md` | 确认规则、依赖、变更影响与红线 | Skill 启动后 |
| `shortfilm-project-brief.md` | 剧本提取、内容分析、灵感参考、制作规格 | 阶段 1 |
| `shortfilm-content-analysis-rules.md` | Project Brief 内部内容类型判断 | 阶段 1 |
| `shortfilm-assets.md` | 元素资产、旁白分离、音色锚定 | 阶段 2 |
| `shortfilm-storyboard.md` | 故事板、内部剪辑和实体分离 | 阶段 3 |
| `shortfilm-prompt.md` | 图像/视频 Prompt 规范 | 阶段 4 |
| `shortfilm-audio.md` | 声音标签、旁白分离和音色一致性 | 阶段 5 |
| `shortfilm-editing.md` | 最终组装与交付 | 阶段 6 |
