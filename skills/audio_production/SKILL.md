---
name: audio_production
display_name: 音频制作
description: "工业级音频生产全流程 Skill。覆盖 AI 音乐创作（纯音乐 BGM、带人声歌曲创作与编曲、歌词定制）、高保真 TTS 语音合成（商业旁白、影视级配音、播客对话、口播朗读）、以及智能多轨混音工程（智能侧链压制 Sidechain Ducking、响度标准化与防爆音限制）。当用户意图为生成音乐、制作背景音乐(BGM)、写歌演唱、文本转语音、播客配音、有声书录制、或将人声与配乐混音成完整音频时加载。本 Skill 专注纯音频工程交付，不生成视频画面。"
tools: ["sandbox_generate_audio"]
---

# 音频制作 (Audio Production) Skill

工业级音频创作与声学母带工程工作台。生产三类音频产物：**AI 音乐**（纯音乐 BGM / 带人声流行歌曲）、**TTS 语音**（商业旁白 / 影视配音 / 多角色对白 / 口播）、以及两者的**智能混音成品**（动态侧链避让 Ducking + 响度标准化）。

本 Skill 的参考文件路径：`/workspace/.skills/audio_production/references/`

```text
references/
├── music-prompt.md   # 音乐工程：Prompt 英文叙事骨架、声学质感词表、8大核心流派配方、歌词结构与时长精确校准表、长纯音乐时间轴技术
├── tts-voice.md      # 语音工程：标点停顿声学映射、8大声线 VoiceDesc 矩阵、多角色对白与声线锚定
└── audio-mix.md      # 混音工程：FFmpeg 动态侧链闪避 (Sidechain Ducking) 滤镜链、降级回退模板、EBU R128 响度与防削波限幅、无缝循环
```

---

## 〇、不可逾越的声学铁律 (Ironclad Rules)

1. **统一生成引擎铁律**：所有音乐与 TTS 语音资产必须通过 `sandbox_generate_audio` 生成。严禁用 `sandbox_bash` 编写 Python/numpy/scipy/wave 等玩具合成脚本；严禁通过生视频模型抽帧提取音轨来"绕出"音频。
2. **异步轮询与防重复提交**：底层音乐生成为异步任务，工具内部自带轮询（常态 30~90 秒，长曲可达数分钟）。调用后耐心等待工具返回，严禁因等待而在未完成前重复发起同一调用。
3. **严格串行化探索**：下游生音频模型并发配额有限，多候选曲目（Candidate A/B/C）与多轨资产（旁白 + BGM）必须**逐首/逐段完全串行生成**，杜绝并发抢占引发的失败。
4. **强制终端交付协议与防偷懒铁律 (Mandatory Delivery Contract)**：
   - **自检通过后，必须立即调用 `present_sandbox_file(filepath=..., interrupt=false)` 推送！**
   - ⚠️ **严禁“嘴替式”假交付**：绝对禁止在未实际调用 `present_sandbox_file` 工具的情况下，在文本中虚构“已推送至上方播放卡片”、“请点击上方试听”！
   - ⚠️ **Todo 状态顺序铁律**：严禁在未调用 `present_sandbox_file` 之前提前将交付 Todo 标记为 `completed`！必须在实际调用 `present_sandbox_file` 的当轮（或之后）才允许打钩完成。未实际触发 `present_sandbox_file` 视为未交付。
5. **规范化目录命名空间**：所有产物统一收敛至 `assets/audio/` 目录下：
   - 纯音乐 / 歌曲：`assets/audio/music/<项目名>_<描述>.mp3`
   - TTS 人声 / 旁白：`assets/audio/voice/<角色>_<序号>.mp3`
   - 混音最终成片：`assets/audio/mix/<项目名>_master.mp3`
6. **交付前声学检测门禁**：成片在调用 `present_sandbox_file` 之前，必须执行 `ffprobe` 验证文件真实存在、时长符合预期；多轨混音需通过限幅器（alimiter）杜绝数字削波 (Clipping)。

---

## 一、输入意图判定与路由分流

```text
               ┌──────────────────────────────────────────────┐
               │              用户音频创作意图判定              │
               └──────────────────────┬───────────────────────┘
                                      │
     ┌──────────────────┬─────────────┴──────┬───────────────────┐
     ▼                  ▼                    ▼                   ▼
【路径 A: 纯音乐 BGM】  【路径 B: 带唱歌曲】   【路径 C: TTS 配音】   【路径 D: 综合混音】
  - 纯器乐 / 伴奏       - 写歌 / 词曲演唱      - 旁白 / 口播 / 对白   - 旁白 + BGM 混音
  - 无词、不传Lyrics    - 先出词给用户确认     - 设计精准 VoiceDesc   - 分轨串行生成
  - 加载 music-prompt   - 加载 music-prompt   - 加载 tts-voice       - 加载全部 references
```

| 业务分类 | 用户典型意图 | 工具调用 Type | 歌词处理 | 专属加载 Ref |
|---|---|---|---|---|
| **A. 纯音乐 BGM** | 背景音乐、宣传片配乐、卡点伴奏、冥想轻音乐、游戏配乐 | `music` | **不传 Lyrics**（模型按纯器乐生成） | `references/music-prompt.md` |
| **B. 人声歌曲创作** | 做一首歌、写词并唱出来、情歌/古风/说唱单曲创作 | `music` | **必须传 Lyrics**；未提供歌词时必须先写好歌词贴在对话中展示给用户 | `references/music-prompt.md` |
| **C. TTS 语音旁白** | 文本转语音、广告旁白、纪录片解说、短剧角色对白、情感电台朗读 | `tts` | 纯文本填入 `Text`，利用标点控制断句与呼吸 | `references/tts-voice.md` |
| **D. 旁白+配乐混音** | 播客片头、有声书成片、带 BGM 的广告配音、诗朗诵配乐 | `tts` ➔ `music` ➔ ffmpeg 混音 | 语音与 BGM 分轨串行生成后，通过侧链闪避滤镜合成母带 | 按需全量加载三份 ref |

> **只读当前任务需要的参考文件**，严禁一次性无脑全读造成上下文污染。

---

## 二、关键确认与问卷门禁 (dynamic_questionnaire)

**铁律：已从用户输入中明确的维度（如流派、角色声线、明确给出的歌词文本、时长要求）直接锁定，严禁重复发问！** 仅在关键维度缺失、可能导致输出方向严重偏离用户预期时，触发 `dynamic_questionnaire` 一次性聚合确认。

### 1. 纯音乐 / 歌曲意图问卷（仅在输入高度模糊如“帮我做首歌/配乐”时触发）
- **Q1 音乐形态**：【带人声演唱歌曲 (推荐)】（AI 自动作词编曲并演唱） / 【纯音乐 / 伴奏 BGM】（纯器乐演奏，无任何歌词人声）
- **Q2 音乐流派与情绪**：给出 3 个贴近用户场景的选项（如：【流行抒情 (温馨治愈)】 / 【动感流行/电子 (元气活力)】 / 【新国风/民谣 (诗意悠扬)】）
- **Q3 目标时长倾向**：【短视频卡点版 (约 30 秒)】 / 【叙事完整版 (约 60 秒)】 / 【全曲广播版 (120 秒以上)】

### 2. TTS 旁白意图问卷（仅在未指定声线风格时触发）
- **Q1 播报声线调性**：【成熟沉稳商务风 (男声/低沉磁性)】 / 【温暖治愈倾诉风 (女声/轻柔自然)】 / 【活力元气口播风 (年轻明亮/快节奏)】 / 【权威新闻纪录风 (标准端庄/字正腔圆)】

---

## 三、任务看板初始化 (todo_write)

在需求确认后，必须使用 `todo_write` 建立全流程任务看板，并在各阶段流转状态（`pending` ➔ `in_progress` ➔ `completed`）：

```json
[
  {"content": "1. 需求意图解析与创意设计（流派/声线/歌词/时长对齐）", "status": "in_progress"},
  {"content": "2. 音频资产串行生成（调用 sandbox_generate_audio）", "status": "pending"},
  {"content": "3. 多轨混音与声学母带处理（仅混音工程需执行侧链避让与限幅）", "status": "pending"},
  {"content": "4. 声学指标自检（ffprobe 真实时长、采样率与削波检测）", "status": "pending"},
  {"content": "5. 终端播放器推送与交付审计报告（present_sandbox_file）", "status": "pending"}
]
```

---

## 四、核心生产步骤与工具调用规范

### 步骤 1：创意设计与歌词编排
- 若为带唱歌曲：
  - **前奏起唱控制（时间紧凑 Case ≤90s）**：严禁空裸 `[Intro]`！必须在 `[Intro]` 标签下方**直接写入第一句歌词**（顺应模型开场乐段先验，开篇 5~10s 内唱响首句，杜绝 24s 漫长空转）；若需要长器乐 Solo 铺垫，必须将 `DurationSec` 相应放宽至 120s~130s。
  - **歌词容量精准对齐**：必须按目标时长精算字数（见 `music-prompt.md` §4），以 80~90 BPM 慢歌为例，**90s 黄金字数为 115~125 字（11~13行）**，字数太少（<90字）会导致 60s 提前收尾，字数太多（>150字）会导致末尾截断。
  - **Prompt 语言与主副声音量平衡**：`MusicPrompt` 默认采用连贯地道的中文音乐制作简报书写，必须包含“人声清晰靠前，主歌与副歌音量平稳均衡无耳语”的声压平衡描述，杜绝主歌过小、副歌突大的断层。
  - 必须使用官方标准结构标签（`[Intro]`, `[Verse]`, `[Chorus]`, `[Outro]` 等），标签独占一行。
  - **在发起生成前，将设计好的歌词完整展示给用户阅读。**
- 若为纯音乐：
  - ≤30s：直接指定 `DurationSec`。
  - >30s：采用中文时间轴分段刻度描述 + `Lyrics` 纯器乐标签占位（见 `music-prompt.md` §4）。

### 步骤 2：音频资产串行生成
调用 `sandbox_generate_audio`：

```json
// 音乐生成示例 (中文 MusicPrompt)
{
  "Type": "music",
  "MusicPrompt": "一首充满未来感的 124 BPM 律动流行电子歌曲。人声清晰靠前透亮，主歌与副歌音量平稳均衡。核心配器：华丽厚实的 Supersaw 合成器和弦层、紧实有力的侧链次低频低音、晶莹清脆的电吉他琶音。宽广立体声场，现代高光律动 Drop 爆发，动态起伏饱满。",
  "Lyrics": "[Verse]\n夜色渐晚 街灯点亮孤单\n微风吹拂 吹散昨日遗憾\n[Chorus]\n奔跑在属于未来的光芒里\n每一秒心跳 都是存在的意义",
  "DurationSec": 30,
  "OutputPath": "assets/audio/music/future_anthem.mp3"
}

// TTS 旁白示例
{
  "Type": "tts",
  "Text": "夜幕降临，城市归于宁静。——这间亮着微光的深夜食堂，正等待着每一位晚归的旅人。",
  "VoiceDesc": "温柔醇厚的中年男声，近距离语感，语速偏慢，尾音带有自然呼吸感与治愈叙述感",
  "Lang": "zh",
  "OutputPath": "assets/audio/voice/narration_01.mp3"
}
```

### 步骤 3：多轨混音组装（仅混音工程执行）
使用 `sandbox_bash` 执行 ffmpeg 动态侧链压制命令（详见 `references/audio-mix.md`）：
- 优先采用 **单 pass 动态侧链压缩滤镜链**（人声出现时 BGM 自动下压 10~14dB，人声停歇后平滑呼吸回弹）。
- 末端串接 `alimiter=limit=0.95` 彻底消除数字削波。
- 产物输出至 `assets/audio/mix/<project>_master.mp3`。

### 步骤 4：声学参数自检
在向用户交付前，必须使用 `sandbox_bash` 运行 `ffprobe` 获取声学元信息：
```bash
ffprobe -v error -show_entries format=duration,bit_rate:stream=sample_rate,channels -of json <产物路径>
```
核验指标：
- 文件是否成功生成且体积正常（>0 字节）；
- 实际时长与用户诉求是否高度吻合（时长偏差若超过 20%，必须在交付报告中说明实际听感原因）；
- 采样率与声道正常。

⚠️ **自检通过后的强约束执行动作**：
自检确认文件正常后，**下一步必须发起 `present_sandbox_file` 的实际工具调用！严禁只调用 `todo_write` 却漏掉 `present_sandbox_file`！** 交付 Todo 项只有在伴随 `present_sandbox_file` 调用时才允许标记为 `completed`。

### 步骤 5：终端交付推送与审计报告（核心）

**制作完成之后，必须立即调用 `present_sandbox_file` 推送给用户！** 绝对禁止只在回复文本中打字“已推送至上方卡片”而漏调工具！

#### 1. 工具调用契约
```json
{
  "filepath": "assets/audio/mix/podcast_master.mp3",
  "interrupt": false
}
```
> **注意**：
> - `interrupt` 固定传 `false`（不用 `interrupt=true` 中断挂起），前端唤起播放卡片的同时，AI 继续在当轮输出完整的声学交付审计报告。
> - 若用户要求制作多首不同风格候选供比选（A/B 探索），每生成完一首即调用一次 `present_sandbox_file(filepath=..., interrupt=false)` 依次推送展示卡片，随后集中汇总各候选的差异化特点。

#### 2. 用户交付审计报告标准模板
在调用 `present_sandbox_file` 交付的同时，必须向用户输出专业规范的制作审计报告：

```markdown
### 🎵 音频工程交付报告

已为您完成高品质音频的创作与声学母带工程处理，音频播放器已推送至上方卡片，您可以直接点击试听。

#### 📋 声学与工程参数
- **文件路径**：`assets/audio/music/city_pop_30s.mp3`
- **声学规格**：44.1 kHz / 立体声双声道 (MP3 320 kbps)
- **实际时长**：`00:30.5` (与目标 30 秒精准对齐)
- **动态电平**：True Peak < -0.5 dBFS，无任何爆音削波

#### 🎼 编曲与声场设计
- **核心风格**：City Pop (都市流行 / 律动 115 BPM)
- **器乐配置**：复古合成器铺底、Funky 清脆电吉他切音、丰满低潜 Bassline、温暖的女声声线
- **结构编排**：
  - `[00:00 - 00:08]` [Intro] 律动吉他切入与霓虹氛围铺底
  - `[00:08 - 00:18]` [Verse] 温暖叙事主歌，近麦人声
  - `[00:18 - 00:30]` [Chorus] 情绪饱满副歌，明亮合成器展开并自然淡出收束

如果您希望调整人声音色、微调 BGM 节奏或尝试不同流派，请随时告诉我！
```
