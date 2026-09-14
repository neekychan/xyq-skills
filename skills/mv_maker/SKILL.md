---
name: mv_maker
display_name: MV Maker
description: "制作、修改和合成以音乐为核心驱动的高品质音乐视频（MV Maker / 音乐视频 / 歌词PV / 舞台唱演 / 舞蹈卡点 / 剧情微电影）。支持舞台唱演、电影叙事、编舞/K-pop、电子赛博粒子、二次元虚拟偶像、唯美情绪蒙太奇、动感歌词排版、概念动态漫/极简赛博排版等 8 大流派。支持上传音频/视频音轨/用户素材/AI自主作词作曲生成音乐/纯文生，具备音频总监子 Agent 歌词识别与多模态乐理感知、3D实体化文字特效与跨段姿态连续性交接。当用户意图涉及'做MV/音乐视频/歌曲视频/歌词视频/唱演短片/音乐卡点/写歌做MV/配乐'时加载。"
tools: ["sandbox_generate_video", "sandbox_generate_image", "sandbox_generate_audio", "extract_lyrics", "task"]
---

# MV Maker (音乐视频制作) Skill

本 Skill 的参考文件路径：`/workspace/.skills/mv_maker/`

```text
agents/
└── audio-director.md            # 音频总监子 Agent Profile：歌词识别 + 多模态听感感知 + BPM/乐段声学分析，产出 beats 事实源
references/
├── mv-rules.md                  # 核心红线：无歌红线、单段时长上限、素材职务声明、唱演/文字分轨、禁用词清单
├── mv-storyboard.md             # 分镜脚本规范与确认门：storyboard.md 标准格式、总览表与通用尾注、用户确认门禁
├── mv-prompt.md                 # Prompt 引擎：Film DNA 架构、四层标准结构、秒数连续阶段化、8大运镜积木、自检清单
├── mv-audio-performance.md      # 视听张力与表演：乐理张力映射表、色彩脚本(Color Arc)、视觉母题、景别呼吸律、5大物理转场
├── mv-visual-lock.md            # 视觉资产锁定：纯人物定妆照、四维五官防撞脸、胶囊打歌服、画风二元分流（严禁场景图）
├── mv-render.md                 # 工程执行与合成：音频 25MB 预检、黑屏 MP4 桥接、原生直拼与 beats.md 字幕烧录
├── mv-type-stage.md             # 流派01: 舞台唱演 (Stage Performance) 积木与范例
├── mv-type-narrative.md         # 流派02: 电影叙事 (Cinematic Narrative) 积木与范例
├── mv-type-kpop.md              # 流派03: 编舞 / K-pop (Choreography Dance) 积木与范例
├── mv-type-cyber.md             # 流派04: 电子 / 赛博 / 粒子 (Cyber & Electronic) 积木与范例
├── mv-type-anime.md             # 流派05: 二次元 / 虚拟偶像 (Anime PV) 积木与范例
├── mv-type-vibe.md              # 流派06: 唯美情绪蒙太奇 (Impressionist Vibe) 积木与范例
├── mv-type-typography.md        # 流派07: 动感歌词排版 (Kinetic Typography) 积木与范例
└── mv-type-graphic-anime.md     # 流派08: 概念动态漫 / 极简赛博排版 (Graphic Anime MV) 积木与范例
```

## 〇、品类定位（先于一切创作决策）

**MV Maker** 是专注于以音乐为灵魂的工业级视频创作引擎。
**铁律：音乐先于一切视觉决策。绝不在未听懂音乐前盲目发问或臆测流派。必须由音频总监子 Agent 先听懂歌曲（歌词 ASR + 多模态听感感知 + 歌手性别/阵容 + 乐理结构），再由主 Agent 根据真实曲风给出针对性方案与智能问卷。**

爆款核心公式：
> **[音频总监子 Agent 听觉与歌词事实（曲风/歌手性别/时间轴）] → [真实曲风智能路由 + 深度定制问卷] → [纯人物资产锁定 + Film DNA 摄影体系] → [分秒连续推进 + 5 大物理转场 + 动作闭环] → 极致视听震撼**

---

!IMPORTANT:**当用户上传音频（分支 A）时，extract_lyrics 是 MV 流程中必须执行的版权预检步骤。如果工具返回"音频权限预检未通过，禁止继续生产。请更换有权限的音频后重试；在预检通过前不得继续调用视频生成、分镜或渲染工具。"，请明确告知用户该音乐无版权不可以使用，禁止开展后续流程；而对于 AI 自主生成音乐（分支 B），属于全新原创资产，无需经过该版权卡点，可直接进入后续制作流程。**

## 一、输入模式判定与核心执行流程

```text
               ┌──────────────────────────────────────────────┐
               │              用户输入与素材判定               │
               └──────────────────────┬───────────────────────┘
                                      │
     ┌────────────────────────────────┼────────────────────────────────┐
     ▼                                ▼                                ▼
【分支 A: 上传目标音频】       【分支 B: AI 生成音乐再做 MV (推荐)】    【分支 C: 纯画面无声版】
     │                                │                                │
 1. 启动 audio-director        1. 词曲与声学设计 (Music Ideation)         1. 问卷确认纯画面无声
    - extract_lyrics 提取歌词     - 带唱歌曲：精算歌词行数与结构标签         2. 纯画面叙事与分镜
    - 听懂曲风/歌手阵容/Drop      - 纯音乐 BGM：英文时间轴+结构标签         3. 交付无声成片
    - ffprobe 测 BPM 与时长    2. 调用 sandbox_generate_audio(Type="music")
 2. 产出 beats.md                产出高质量音频 assets/audio/generated_song.mp3
 3. 进入视觉与分镜制作         3. 自动将生成音频作为输入，启动 audio-director
                               4. 产出 beats.md，无缝进入 MV 制作管线！
```

---

## 一-1、分支 B: AI 自主创作音乐 ➔ 制作 MV 规范（用户无音频时）

当用户无上传音频但希望“制作完整 MV / 包含歌曲的音乐视频”时，系统依托工业级 AI 音乐模型（`sandbox_generate_audio`）先作词作曲并演唱生成母带级音频，再全自动接力进入 MV 制作流程：

### 1. 音乐创意设计与 Producer Brief 提示词构建
- **核心原则**：以专业音乐制作人创作简报 (Producer Brief) 的英文长句书写，涵盖 6 层骨架：
  `A [能量/情绪] [精确 BPM] [核心流派] song/piece. [人声/器乐核心]. [叙事画面与声学场景]. [配器编曲与演奏细节]. [声学质感 Production Tokens (如 wide stereo imaging, punchy transients)]. [动态起伏弧线].`
- **流派配方参考**：
  - **流行舞曲 / K-pop (120-128 BPM)**：`tight sidechain compression pump, modern polished vocal chop risers, punchy compressed transients`
  - **都市抒情情歌 (68-82 BPM)**：`warm studio acoustic recording, intimate vocal mic placement, lush orchestral string swell in chorus`
  - **现代说唱 (135-150 BPM)**：`sub-bass saturation, half-time groove switch, dry centered vocal presence`
  - **二次元 / 燃系摇滚 (140-165 BPM)**：`driving electric guitar power chords, energetic anime lead synth, soaring emotional vocals`

### 2. 歌词编排与时长精算
- **带唱歌曲 (Vocal Song)**：
  - 必须包含标准结构标签（`[Intro]`, `[Verse]`, `[Chorus]`, `[Outro]`），标签独占一行；
  - **歌词行数字数精算表**：
    - **30 秒**：`[Verse]` + `[Chorus]`，4~8 行，45~75 字；
    - **60 秒**：`[Intro]` + `[Verse]` + `[Chorus]` + `[Outro]`，8~14 行，90~140 字；
    - **120 秒**：双段式结构，16~24 行，180~260 字；
  - **展示给用户**：若用户未提供歌词，AI 撰写完成后**必须在正文完整贴出歌词展示给用户**。
- **纯音乐 BGM (Instrumental)**：
  - `Prompt` 显式注入英文时间轴事件（如 `"0:00-0:15: ... 0:15-0:30: ..."`）；
  - `Lyrics` 仅填入纯器乐结构标签占位（`[Intro]\n[Inst]\n[Build Up]\n[Climax]\n[Outro]`）。

### 3. 调用工具生成母带音频
调用 `sandbox_generate_audio`：
```json
{
  "Type": "music",
  "Prompt": "A dynamic 124 BPM K-pop dance pop song featuring energetic and crystal-clear female vocals, driving 4/4 electronic beats, lush supersaw chords, wide stereo imaging and punchy compressed transients.",
  "Lyrics": "[Intro]\n（前奏强劲鼓点起）\n[Verse]\n霓虹闪烁 照亮黑夜的舞台\n节拍跳动 唤醒沉睡的期待\n[Chorus]\n倒数三秒 属于我们的光芒\n冲破引力 飞向最高的远方\n[Outro]\n这就是我们的时刻",
  "DurationSec": 30,
  "OutputPath": "assets/audio/generated_song.mp3"
}
```

### 4. 无缝接力进入 MV 管线
音频生成完成后，**自动将 `assets/audio/generated_song.mp3` 传入 Phase 1**，调用 `task` 启动 `audio-director` 提取歌词、听懂声学细节并生成 `beats.md`，随后完全复用 Phase 2（人物定妆）➔ Phase 3（分镜确认）➔ Phase 4（视频生成）➔ Phase 5（FFmpeg 直拼 + ASS 动态字幕）全流程！

---

## 二、基于 beats.md 的曲风智能路由与专属 Ref

拿到 `audio-director` 产出的 `beats.md` 后，主 Agent 根据曲风精准匹配专属流派 Ref，**在 Phase 3 规划分镜时仅读取对应流派的 Ref 文件，严禁跨流派全量加载造成上下文污染**：

| 识别曲风与声学特征 | 智能匹配流派 | 定制视听策略与表演规范 | 专属加载 Ref 文件 |
|---|---|---|---|
| **韩系女团/男团、K-pop、动感舞曲、高BPM齐舞** | **03 编舞 / K-pop (Choreography)** | **多 Concept Box 换盒 + 高能齐舞 + 标志性 Killing Part**，全景齐舞40% + 成员特写60%，数字变焦 (Punch Zoom) 卡拍 | `references/mv-type-kpop.md` |
| **流行唱将、摇滚乐队、Live 现场、燃系单曲** | **01 舞台唱演 (Stage Performance)** | **40~50% MCU 歌手高光唱演 + 50~60% 舞台光效/冷焰火**，精准口型对嘴，展现歌手面部魅力 | `references/mv-type-stage.md` |
| **民谣、抒情情歌、电影原声 (OST)、叙事曲** | **02 电影叙事 (Cinematic Narrative)** | **35mm 胶片微电影故事弧 + 情绪特写**，变焦 (Rack Focus) 与空间反转，少量唱演 + 大量剧情蒙太奇 | `references/mv-type-narrative.md` |
| **EDM、Future Bass、Trap、赛博朋克电音** | **04 电子 / 赛博 / 粒子 (Cyber & Electronic)** | **Drop 极速爆发 + 光流粒子 + FPV 穿梭**，空间折叠与几何建筑，纯视觉爆发不对嘴 | `references/mv-type-cyber.md` |
| **动感说唱 (Rap)、J-Pop 概念曲、高密度词作** | **07 动感歌词排版 (Kinetic Typography)** | **3D 实体文字穿插 + 掌心生长 + 视差排版**，严格执行**唱演与文字分轨**（唱演镜不写字，排版镜不加口型） | `references/mv-type-typography.md` |
| **二次元、ACG、Vocaloid、虚拟主播曲** | **05 二次元 / 虚拟偶像 (Anime PV)** | **日漫赛璐珞平涂 + 速度线 + 跳切 (Jump Cut)**，高饱和撞色与夸张透视 | `references/mv-type-anime.md` |
| **Hyperpop、Glitchcore、电音说唱、动感动态漫/AMV** | **08 概念动态漫 / 极简赛博排版 (Graphic Anime MV)** | **赛博国潮/赛璐珞高精原画 + 文字蒙版切割 + 文字透镜 + 重复文字墙**，默认 0% 唱演不对嘴，一拍一剪高频卡点轰炸 | `references/mv-type-graphic-anime.md` |
| **纯器乐、Ambient、治愈系氛围、轻音乐 (无人声)** | **06 唯美情绪蒙太奇 (Impressionist Vibe)** | **微距材质 (水滴/光斑) + 逆光尘埃 + 慢快门动态模糊**，**自动跳过所有口型相关询问与设置**，纯视觉意境 | `references/mv-type-vibe.md` |

---

## 三、关键确认（听懂音乐后、创作前）

**铁律：问卷必须在拿到 `beats.md` 事实源后触发（纯文生除外）。问卷前先向用户汇报听感结论，且仅针对未明确的必要维度提问，严禁询问已由曲风决定的默认常识。**

| 维度 | 何时问 | 选项要点（带后果说明） |
|------|-------|---------------------|
| **1. 音乐来源** | **仅在用户未上传音频时问** | **AI 自主创作音乐并制作完整 MV (推荐)**（AI 自动作词编曲并生成高质量母带音乐，再全自动制作 MV，声画完美卡点）/ **纯画面无声版**（生成高品质画面视频，成片无声，提示用户后期自行贴入音乐）/ **等待用户上传音频**（需用户在输入框提供音频附件） |
| **2. 画幅比例** | 用户输入未明确指定比例 | **16:9 横屏 (推荐)**（经典宽银幕电影与舞台大片画幅）/ **9:16 竖屏**（适配抖音/TikTok 全屏短视频） |
| **3. 时长模式** | 用户未明确指定总时长 | **单段精剪（约 {{.max_video_duration}} 秒，推荐）**（最快交付，单段内包含 2~4 个连贯镜头）/ **多段全曲 MV**（按乐段规划多段拼接） |
| **4. 视觉方案微调** | 用户对流派有特殊定制诉求时 | 提供 2~3 个与**已识别曲风高度匹配**的创意分支供选（例如针对 K-pop：`极简先锋冷白光盒风` vs `未来黑金浅水舞台风`） |

---

## 四、单段 / 多段分流逻辑

| 判定条件 | 创作路径 | 核心执行逻辑 |
|---|---|---|
| **总时长 ≤ {{.max_video_duration}} 秒**<br>（或问卷确认单段精剪） | **单段创作流程（§五）** | 一次调用 `sandbox_generate_video` 完成，单段内通过镜头序号组织 2~4 个连贯镜头，直接交付 |
| **总时长 > {{.max_video_duration}} 秒**<br>（或问卷确认多段全曲） | **多段制作流程（§六）** | 主 Agent 将 `{{.max_video_duration}}` 上限传入音频总监子 Agent 产出 `beats.md`；主 Agent 规划分镜时**遵循纯整数秒切片与大块乐段贪心合并原则，尽量用满 `{{.max_video_duration}}`（如 15s 模型规划纯整数 15s，30s 模型规划纯整数 30s），生成最少数量的片段**。每个 Seg 均为纯整数秒（Duration 必须为整数，最后一段尾巴向上取整 $\ge 4$ 秒生成，末尾多一两秒定格留白完全合规），多段并行生成后由 FFmpeg 脚本直接拼接 |

---

## 五、单段创作流程（5 阶段渐进式执行）

```text
【Phase 1: 音频感知】 ──▶ 【Phase 2: 视觉资产】 ──▶ 【Phase 3: 分镜规划】 ──▶ 【Phase 4: 视频生成】 ──▶ 【Phase 5: 成片装配】
 (audio-director.md)   (mv-visual-lock.md)   (audio-perf + archetypes)  (rules + prompt.md)     (mv-render.md)
```

1. **Phase 1: 音频感知与曲风判定**
   * 若有上传音频，**第一步立即调用 `task` 工具启动音频总监（`agents/audio-director.md`）**：
     - 若用户输入中包含「参考歌词文本」，**必须在 prompt 中完整传入用户歌词，并显式指令子 Agent 以用户原词校准 ASR 识别结果**；
     - `extract_lyrics` 提取歌词时间轴；
     - `sandbox_file_read` 听懂曲风、歌手性别与演唱阵容（女/男/对唱/女团/乐队）、情绪、主奏乐器与核心爆发点；
     - `sandbox_bash` (`ffprobe`) 测量 BPM 与时长；
     - 产出 `beats.md` 并将音频制成黑屏 MP4 传入 `VideoList`；
   * 若无上传音频，问卷确认纯画面无声版；
   * 自动根据 `beats.md` 匹配 8 大流派与歌手性别，若有缺失维度调用 `dynamic_questionnaire` 确认。
2. **Phase 2: 视觉资产锁定与生图（纯人物锁图，画风二元分流）**
   * **按需读取 `references/mv-visual-lock.md`**；
   * **【歌手性别与阵容驱动】严格根据 `beats.md` 识别出的歌手性别与阵容（如女声单人、男声摇滚、4人女团）规划角色画像**；
   * **【画风二元路由】根据曲风流派选择生图分支**：
     - 若为 **05 二次元 / 08 概念动态漫**：必须使用**分支 B 动漫模板（赛璐珞平涂、黑色勾线、边缘行者风）**，**绝对严禁出现 85mm镜头、真实皮肤毛孔等真人词汇**；
     - 若为 **01 舞台 / 02 电影 / 03 K-pop**：使用分支 A 写实真人模板（85mm、真实皮肤质感）；
   * 调用 `sandbox_generate_image` 生成主角单人定妆照（纯白无缝背景、四维五官精准、胶囊系列服装）；
   * **【红线禁令】严禁生成任何场景参考图**！场景空间、光影系统与超现实符号 100% 交由生视频 Prompt 纯文字驱动，避免生图模型拉低视频审美上限。
3. **Phase 3: 视听张力、分镜规划与输出 storyboard.md（用户确认硬门禁）**
   * **按需并行读取 `references/mv-audio-performance.md` + 专属流派文件 `references/mv-type-{selected_type}.md`（如 `mv-type-kpop.md`）+ `references/mv-storyboard.md`**；
   * 检索对应流派正交积木库，规划全片色彩脚本 (Color Script)、视觉母题 (Visual Motif)、景别呼吸律与动作四阶力学；
   * **【输出 storyboard.md】**：调用 `sandbox_write` 将完整分镜方案写入 `./assets/storyboard.md`（严格遵循 `mv-storyboard.md` 格式规范，包含总览表、通用尾注与 shot_01 分镜）；
   * **【推送与用户确认门禁】**：
     - 调用 `present_sandbox_file(filepath="./assets/storyboard.md", interrupt=false)` 向用户展示分镜方案；
     - 立即触发 `dynamic_questionnaire` 发起确认问卷（`满意，开始生成视频 (推荐)` / `需要调整分镜与画面`）；
     - **【硬门禁】未获得用户确认前，绝对严禁调用 `sandbox_generate_video`**。
4. **Phase 4: 消费 storyboard.md 与生成视频（实体空间/因果特写/动能位移）**
   * **按需读取 `references/mv-rules.md` + `references/mv-prompt.md`**；
   * **【三大生成铁律】**：
     - ① **实体空间与零白底**：每镜构建三层实体世界（镜面水泊/电路网格/赛博建筑/代码瀑布），严禁使用“纯白底/冷白通道”；
     - ② **特写叙事因果链**：局部特写严格遵循 [察觉/动机 $\rightarrow$ 动作执行 $\rightarrow$ 物理反馈]，严禁商品目录式无因果部位陈列；
     - ③ **破风动能与多机位冲刺**：严禁单一机位原地跑步机，冲刺必须在 2~3 秒内串联贴地抓地、广角超车与急刹滑行多机位跳切；
   * 从 `storyboard.md` 提取 `shot_01` 的 Prompt，并将 `## 通用尾注` 拼接到末尾，调用 `sandbox_generate_video`：
     - `Prompt`: 组装完成的分秒阶段化提示词（包含通用尾注）
     - `ImageList`: 全量传入所有主角单人参考图（严禁传场景图）
     - `VideoList`: 传入生成的黑屏 MP4 路径
     - `Duration`: 填入 `{{.max_video_duration}}` 或确认秒数
     - `Resolution`: `1080p`
5. **Phase 5: FFmpeg 混流与成片交付**
   * **按需读取 `references/mv-render.md`**；
   * 原生视频直接混入原曲母带音频轨，严禁二次硬裁切（以视频为准）；
   * **【左对齐动感 ASS 字幕全量烧录】**：根据 `beats.md` 歌词时间轴生成 `/workspace/assets/lyrics.ass` 并由 FFmpeg 烧录左对齐动感字幕（若为有歌词人声歌曲，默认全量烧录字幕；纯音乐除外）；
   * 执行 `present_sandbox_file(filepath="/workspace/output/final_mv.mp4", interrupt=true)` 交付成片。

---

## 六、多段制作流程（5 阶段渐进式执行）

1. **Phase 1: 音频总监事实源感知与曲风判定**
   * 主 Agent 立即调用 `task` 工具，**在 prompt 中明确注入 `{{.max_video_duration}}` 秒上限与用户参考歌词（如有）**：
     ```json
     {
       "description": "调用音频总监子 Agent 执行歌词提取、多模态听感感知（含歌手性别/阵容）与乐理节拍分析",
       "prompt": "请对音频 /workspace/upload/... 执行 extract_lyrics 提取歌词时间轴、多模态听感感知（必须细致辨析歌手性别、演唱阵容与音色质感）与乐理结构分析。当前模型单段视频生成时长上限严格为 {{.max_video_duration}} 秒（{{.max_video_duration}}000ms）。【重要：用户提供的参考歌词为：{user_lyrics}。请在 extract_lyrics 识别后，务必以用户提供的歌词文本为准校准 ASR 识别结果，将用户原版歌词精准对齐到时间戳上】。请确保输出的 beats.md 乐段结构表中，遵循【纯整数秒切片与尽量用满时长上限】原则：每个分段起止时间必须为整千毫秒纯整数秒，相邻短乐段贪心合并，严禁出现浮点小数切分；单行时长严格控制在 4000ms ~ {{.max_video_duration}}000ms 之间，严禁任何一行超过 {{.max_video_duration}} 秒，将事实源输出到 ./assets/beats.md",
       "system_prompt_file": "/workspace/.skills/mv_maker/agents/audio-director.md"
     }
     ```
   * 读取子 Agent 产出的 `beats.md`，向用户简报曲风与歌手性别识别结论，通过 `dynamic_questionnaire` 确认必要维度。
2. **Phase 2: 视觉资产准备（纯白底单人定妆照，画风二元分流）**
   * **按需读取 `references/mv-visual-lock.md`**；
   * **【歌手性别与阵容驱动】严格根据 `beats.md` 识别出的歌手性别与阵容（女/男/对唱/女团/乐队）规划角色画像**；
   * **【画风二元路由】根据曲风流派选择生图分支**：
     - 若为 **05 二次元 / 08 概念动态漫**：必须使用**分支 B 动漫模板（赛璐珞平涂、黑色勾线、边缘行者风）**，**绝对严禁出现 85mm镜头、真实皮肤毛孔等真人词汇**；
     - 若为 **01 舞台 / 02 电影 / 03 K-pop**：使用分支 A 写实真人模板（85mm、真实皮肤质感）；
   * 根据歌手性别与人设，按「胶囊系列打歌服法则 (同色系同材质、版型差异化)」调用 `sandbox_generate_image` 生成单人定妆照（纯白底、四维五官精准）；
   * **【红线禁令】严禁生成场景参考图**！场景空间完全由生视频 Prompt 纯文字驱动，释放视频模型的高动态审美。
3. **Phase 3: 视听张力、分镜规划与输出 storyboard.md（纯整数秒 + 尾段容错 + 确认门）**
   * **按需并行读取 `references/mv-audio-performance.md` + 专属流派文件 `references/mv-type-{selected_type}.md`（如 `mv-type-kpop.md`）+ `references/mv-storyboard.md`**；
   * **【纯整数秒切片与尾段容错门禁】**：生视频模型 Duration 仅支持纯整数秒：
     - 前置各 Seg 时长必须按纯整数秒（如 15s 或 30s）对齐规划；
     - **【单段时长绝对上限门禁】无论 `beats.md` 给出何种乐段划分，每个 `shot_NN` 的 Duration 绝对严禁超过 `{{.max_video_duration}}` 秒（通常为 30 秒）！若某一乐理大段（如 0-42s）超过上限，主 Agent 在 Phase 3 必须强制将其拆分为两个合规的 shot（如 `shot_01: 24s`，`shot_02: 18s`），严禁出现任何 Duration > {{.max_video_duration}} 的分镜！**
     - 最后一小段尾巴（如原曲余下 2.4s）由于模型最低时长限制（$\ge 4$ 秒），**直接向上取整规划为 4 秒或 5 秒纯整数**，末尾多出一两秒画面定格/回味空镜完全合规，不影响母带对齐；
   * 规划全片色彩脚本 (Color Script)、视觉母题 (Visual Motif)、景别呼吸律与跨段动作匹配 (Match Cut)；
   * **【输出 storyboard.md】**：调用 `sandbox_write` 将全片分镜方案写入 `./assets/storyboard.md`（严格遵循 `mv-storyboard.md` 格式规范，包含总览表、通用尾注、各段 `shot_NN` 小节及完整 Prompt）；
   * **【推送与用户确认门禁】**：
     - 调用 `present_sandbox_file(filepath="./assets/storyboard.md", interrupt=false)` 向用户展示完整分镜方案；
     - 立即触发 `dynamic_questionnaire` 发送分镜确认问卷（`满意，开始生成视频 (推荐)` / `需要调整分镜与画面`）；
     - **【硬门禁】未收到用户确认前，绝对严禁调用 `sandbox_generate_video`**；若用户提出修改意见，调整 `storyboard.md` 后重新确认。
4. **Phase 4: 消费 storyboard.md 与分段并行生成（实体空间/因果特写/动能位移）**
   * **按需读取 `references/mv-rules.md` + `references/mv-prompt.md`**；
   * **【三大生成铁律】**：
     - ① **实体空间与零白底**：每镜构建三层实体世界（镜面水泊/电路网格/赛博建筑/代码瀑布），严禁使用“纯白底/冷白通道”；
     - ② **特写叙事因果链**：局部特写严格遵循 [察觉/动机 $\rightarrow$ 动作执行 $\rightarrow$ 物理反馈]，严禁商品目录式无因果部位陈列；
     - ③ **破风动能与多机位冲刺**：严禁单一机位原地跑步机，冲刺必须在 2~3 秒内串联贴地抓地、广角超车与急刹滑行多机位跳切；
   * **【MV 无串行依赖铁律】MV 乐段之间（Verse / Pre / Chorus / Bridge / Outro）天然属于换盒换景大跳切 (Jump Cut / Box Cut)，各分段 (Seg) 彼此完全独立，可直接并行调用 `sandbox_generate_video`**；
   * **严禁将上一段生成的视频或尾帧传入下一段（彻底避免画质二次压缩劣化、动作残留与光影污染）**；
   * 每一个分段均独立全量传入纯角色参考图（`ImageList: [member1..4]`），并传入该分段精准裁切的黑屏音频（`VideoList: [seg_audio.mp4]`，`AudioList: []`）；
   * 逐段从 `storyboard.md` 提取 `shot_NN`，将 `## 通用尾注` 拼接到每段 Prompt 末尾，调用 `sandbox_generate_video`（`Resolution: 1080p`）。
5. **Phase 5: 原生直拼、歌词字幕与成片交付**
   * **按需读取 `references/mv-render.md`**；
   * **【原生直拼不剪辑】严禁使用 FFmpeg 做二次 `-t` 硬裁切或重新编码；若末端有轻微 gap，统一以视频为准**；
   * 使用 `sandbox_bash` 执行 FFmpeg `concat` 脚本，将所有原生视频片段（`seg_01.mp4` ~ `seg_04.mp4`）无损串联，并合入原曲母带音频轨；
   * **【左对齐动感 ASS 字幕全量烧录】**：根据 `beats.md` 歌词时间轴生成 `/workspace/assets/lyrics.ass` 并由 FFmpeg 烧录左对齐动感字幕（若为有歌词人声歌曲，默认全量烧录字幕；纯音乐除外）；
   * 调用 `present_sandbox_file(filepath="/workspace/output/final_mv.mp4", interrupt=true)` 交付成片。

---

## 七、Ref 渐进式加载总表

| 执行阶段 (Phase) | 专属加载文件 | 核心内容与职责 | 加载触发时机 |
|---|---|---|---|
| **Phase 1: 音频感知** | `agents/audio-director.md` | 歌词 ASR + 多模态听感感知（含歌手性别/阵容） + BPM/乐段声学分析 | 有音频时第一步通过 task 工具调用 |
| **Phase 2: 视觉资产准备** | `references/mv-visual-lock.md` | 单人纯白底、四维防撞脸五官、胶囊系列服装、画风二元分流（严禁场景图） | 准备角色素材时读取 |
| **Phase 3: 分镜规划与确认** | `references/mv-audio-performance.md`<br>+ 专属流派 `references/mv-type-*.md`<br>+ `references/mv-storyboard.md` | 乐理张力映射、色彩脚本、视觉母题、景别呼吸律、storyboard.md 格式规范与用户确认门禁 | 规划分镜、输出 storyboard.md 与发起确认问卷时并行读取 |
| **Phase 4: Prompt 构造与生成** | `references/mv-rules.md`<br>`references/mv-prompt.md` | 核心红线、四层结构、秒数连续阶段化、8大运镜积木与自检清单 | 构造视频 Prompt 与生视频时并行读取 |
| **Phase 5: 合成与成片交付** | `references/mv-render.md` | 音频 25MB 预检、黑屏 MP4 桥接、FFmpeg 原生直拼与 beats.md 字幕烧录 | 涉及音频切片与最终拼接时读取 |
