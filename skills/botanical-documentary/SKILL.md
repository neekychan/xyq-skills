---
name: botanical-documentary
display_name: 植物博物纪录片
description: >
  制作45秒植物博物学纪录片全片。生成18世纪科学植物图鉴风格解析图、2×3六格导演分镜板图、逐组15秒组级视频，合成旁白VO与管弦BGM，最终拼接为三段式完整成片。
  触发场景：用户希望制作植物科学纪录片、博物学解说视频、植物科普短片、或要求"植物+纪录片+解析图+分镜+旁白"组合创作流程时使用。
  覆盖全流程：植物参考材料分析、Botany_Spec规格编写、植物解析图生成、三组六格分镜板设计与逐字旁白撰写、组级视频生成、BGM与VO合成、全片色彩弧光审计与组装导出。
tools: ["sandbox_generate_image", "render_video", "sandbox_generate_video", "sandbox_process_video"]
---

# 植物博物纪录片 / Botanical Documentary

## 核心原则

不要只做"植物图片的堆叠"，而要做一条有因果叙事弧的植物博物学纪录片——从科学解构到生命历程到人文应用，三段递进，每一段的视觉基调与旁白情绪都不可互换。

持久引擎（因果链）：

**植物参考材料 → Botany_Spec 规格锁定 → 植物解析图（全片视觉锚点） → 解析图结构化分析 → 三组六格分镜板（含逐字旁白VO） → 逐组15秒视频 → BGM + VO 合成 → 全片色彩弧光审计 → 45秒成片导出**

### 质量测试（可证伪）

全片成立的硬标准：**如果没有植物解析图（Plant_Asset_01）作为视觉锚点，三组视频的植物形态（叶形/花色/茎秆/根系）就无法保持跨组一致性，全片就退化为三段互不关联的素材拼接。**

验证方法：在每组视频生成后，对照 Plant_Asset_01 检查叶形、花色、茎秆形态的视觉连续性；相邻镜头视觉重心偏差控制在 20% 以内。

## 输入诊断

生产前，识别或合理假设以下维度：

- **植物种类**：用户是否指定了植物？若未指定，向用户推荐 3–5 种代表性植物（如姜黄 Curcuma longa、藏红花 Crocus sativus、水稻 Oryza sativa、薰衣草 Lavandula angustifolia、人参 Panax ginseng），询问感兴趣的植物及重点呈现内容
- **参考材料**：用户是否上传了植物文本或图像？若有则提取解剖学特征、色彩弧光、HSL 参数区间、地理与时代背景
- **旁白输出语言**：默认中文；若用户指定其他语言则在规格中锁定
- **画幅与分辨率**：默认 16:9 横版，组级视频 720p，解析图与分镜板图 2K
- **总时长与结构**：默认 45 秒（3 组 × 15 秒），每组 6 个内容节拍（每格约 2.5 秒）
- **视觉风格**：写实科学纪录片 / 国家地理美学
- **色彩弧光**：A 组清爽白底信息图 → B 组写实自然绿棕 → C 组生活中性明亮
- **旁白风格**：深沉磁性的纪录片解说腔——语速平稳、信息密度高、情感克制有力量感
- **合规敏感点**：若涉及药用功效声称（如人参、藏红花），旁白须以"传统用途"措辞表述，不做医疗效果断言

若用户给的上下文很少，做合理假设并继续。仅当植物种类完全无法确定时才暂停询问。

## 路由表

| 任务阶段 | 选用路线 | 必读 reference |
|---|---|---|
| 生成植物解析图 | TextToImage，18 世纪博物学风格 | `references/industries/botanical-illustration.md` |
| 编写三组六格分镜板 | 三组主题（信息展示 / 种植过程 / 功效应用） | `references/formats/storyboard-structure.md` |
| 撰写视频 prompt | 六格分镜驱动的视频生成提示词 | `references/formats/video-prompt-grammar.md` |
| 撰写解析图与分镜板图 prompt | 文生图提示词模板 | `references/formats/image-prompt-grammar.md` |
| 音频层规划（VO + BGM） | 旁白逐字稿与管弦乐规格 | `references/formats/audio-layer-spec.md` |
| 色彩弧光与视觉焦点轴线 | 跨组色调审计与动量守恒 | `references/craft/color-arc-eye-tracing.md` |
| 运镜与景别语言 | 纪录片级镜头规范 | `references/craft/cinematography.md` |
| 组装与导出 | 时间轴拼接与 L-Cut/J-Cut | `references/formats/assembly-spec.md` |

## 强制加载 reference

落任何产出前，先按路由结果加载对应 references，把相关词汇与句式写进实际产出。

**必读：**
1. `references/formats/storyboard-structure.md` — 三组六格分镜结构是全片骨架
2. `references/formats/image-prompt-grammar.md` — 解析图与分镜板图提示词文法
3. `references/formats/video-prompt-grammar.md` — 视频提示词文法

**条件读取：**
- 涉及植物科学解析图时读 `references/industries/botanical-illustration.md`
- 涉及音频层（VO/BGM）时读 `references/formats/audio-layer-spec.md`
- 涉及最终组装导出时读 `references/formats/assembly-spec.md`
- 涉及色彩弧光审计与视觉焦点轴线时读 `references/craft/color-arc-eye-tracing.md`
- 涉及运镜与景别设计时读 `references/craft/cinematography.md`

**硬规则：** 若最终产出包含视频生成提示词，则本回合必须已读过 `references/formats/video-prompt-grammar.md`；若产出包含植物解析图提示词，则必须已读过 `references/industries/botanical-illustration.md`。

## 工作流（步骤）

### 全片阶段逻辑与依赖关系

依赖链：2→1；3→2；4→3；5→4；6→5（逐组）；7→6；8→6,7

---

### Step 1：建立全局规格文件

创建 `Final_Video_Spec.md`，锁定以下参数：
- 画幅：16:9 横版
- 总时长：45 秒（3 组 × 15 秒）
- 视觉风格：写实科学纪录片 / 国家地理美学
- 旁白输出语言（默认中文，可配置）
- 色彩弧光：A 组清爽白底 → B 组自然绿棕 → C 组生活中性明亮
- 分辨率：组级视频 720p，解析图与分镜板图 2K

**暂停确认节点①**：规格文件锁定后，等待用户确认。

---

### Step 2：分析植物参考材料

**分支 A — 用户上传了参考材料：**
对用户上传的植物文本或图像进行结构化分析，提取：
- 解剖学特征（叶形、花序/花色、茎秆/块茎形态、根系、果实）
- 色彩弧光（Color Arc）与 HSL 参数区间
- 地理与时代背景
将分析结果写入 `Botany_Spec.md`。

**分支 B — 用户未上传任何参考材料：**
向用户推荐 3–5 种代表性植物：
- 姜黄 Curcuma longa — 药用与香料双重身份，根茎截面色彩鲜明
- 藏红花 Crocus sativus — 极高经济价值，红色柱头与紫色花朵对比强烈
- 水稻 Oryza sativa — 文明粮食作物，生命周期完整且具人文深度
- 薰衣草 Lavandula angustifolia — 芳香与观赏，紫色花海视觉冲击力强
- 人参 Panax ginseng — 传统药用，根系形态独特且文化底蕴深厚

询问用户感兴趣的植物及希望重点呈现的内容。用户确认后，基于植物名称直接编写 `Botany_Spec.md`，内容覆盖：学名、科属、核心识别特征、产地分布、生长条件、核心成分、生命周期节点、功效与应用线索。

**暂停确认节点②**：`Botany_Spec.md` 确认后继续。

---

### Step 3：生成植物科学解析图（Plant_Asset_01）

`Botany_Spec.md` 确认后，立即生成一张竖版（3:4）植物博物学解析图。

**生成规格：**
- 方式：文生图
- 分辨率：2K
- 比例：3:4 竖版
- 风格：复古羊皮纸纹理，18 世纪博物学水墨水彩风格

**解析图必须涵盖：**
- 整体形态大图（居中）
- 放大镜框截面细节
- 叶形与花序解剖图
- 产地小地图
- 分子结构示意
- 底部生命周期序列图
- 中文书法标注（学名、科属、产地、成分）

**提示词编写规范：** 参见 `references/industries/botanical-illustration.md`，按其中的模板结构起草。

生成后绑定至 Plant_Asset_01，作为全片视觉形态约束锚点。

**暂停确认节点③**：植物解析图确认后方可继续。

---

### Step 4：解析图分析 + 故事脚本编写 + 分镜板转化

**4a. 对 Plant_Asset_01 执行结构化分析：**

分析 Plant_Asset_01，输出以下信息供剧本编排使用：
- **形态要素清单**：叶形、花序/花色、茎秆/块茎形态、根系、果实——为 Section A 每格画面提供视觉主体
- **科学标注内容**：学名、科属、产地信息、分子结构关键词、生命周期阶段标注——作为 Section A 信息卡片文案素材
- **色彩与质感基调**：主导色（如赭石暖褐、哑光草绿）与纸张/背景质感——作为 Section B/C 视频调色参考底色
- **生长周期线索**：从生命周期图提炼 Section B 应覆盖的关键阶段节点（播种 → 萌发 → 茎叶生长 → 开花 → 结果/成熟）
- **功效与应用线索**：提炼为 Section C 核心信息点

分析结果写入 `Botany_Spec.md` 补充章节。

**4b. 编写三组六格分镜板与逐字旁白VO：**

依据解析图信息与三大分镜组主题，为每组规划 6 个内容节拍鲜明的分镜画面（全片共 18 格）。同步为三组逐字撰写完整 Narration VO 台词。

**三大分镜组结构详见：** `references/formats/storyboard-structure.md`

**旁白台词规范：**
- 语言风格：深沉磁性的纪录片解说腔——语速平稳、信息密度高、情感克制有力量感；避免口语化和广告腔
- 台词与 Grid 编号严格绑定（每格对应约 2.5 秒台词量）
- 三组台词在叙事逻辑上首尾相连，形成完整的植物人文叙事弧

**暂停确认节点④**：故事脚本与旁白台词确认后，转化为结构化分镜板（含 2×3 六格画面内容、运镜标注）及跨组音频层（BGM、Narration VO，含完整逐字稿）规划。

---

### Step 5：逐组生成 2×3 六格导演分镜板图

以确认后的脚本为依据，为每组生成一张六格矩阵分镜图。

**生成规格：**
- 方式：纯文生图，无需参考图输入
- 分辨率：2K
- 比例：16:9 横版
- 排版：2×3（2 横排 × 3 纵列）六格规整矩阵，每格独立黑色边框，角落标注镜头编号与运镜说明

**提示词编写规范：** 参见 `references/formats/image-prompt-grammar.md`，Section A 与 B/C 有不同风格要求。

**逐组暂停确认**（核心拦截点⑤）：每组分镜板图生成后暂停，等待用户确认后方可继续下一组。

---

### Step 6：逐组生成 15 秒组级视频

每组以已确认的六格分镜图作为参考图驱动生成，一次生成 15 秒完整片段，覆盖 6 个叙事节点。

**生成规格：**
- 方式：参考图生视频
- 分辨率：720p
- 时长：15 秒/组
- 参考图：该组已确认的六格分镜板图

**提示词编写规范：** 参见 `references/formats/video-prompt-grammar.md`，Section A 与 B/C 有不同风格与负向词要求。

**视频提示词结构：**
1. 以六格分镜参考图开头
2. 15 秒时长
3. 按故事顺序逐格描述 6 个动态节拍（运镜方式、主体动作、光线演变、景深变化）
4. 标注每格切换时视觉中心动量连续
5. Section B/C 写实段落嵌入 Foley 音效标签

每组视频完成后同步合成对应 Narration VO。

**暂停确认节点⑥**：3 组视频全部完成后继续。

**视频时长说明：** 每组 15 秒视频用一次生成即可拿到完整成片；6 个 beat（每格约 2.5 秒）是同一条 prompt 内的时间轴描述，不是分段多次生成。全片 45 秒由 3 组各自独立生成的 15 秒片段拼接而成。

---

### Step 7：生成全片 BGM

3 组视频全部确认后，生成 45 秒深沉管弦乐背景音轨。

**生成规格：**
- 风格：深沉管弦乐，纪录片配乐质感
- 时长：45 秒

---

### Step 8：组装与导出

**8a. 时间轴组装：**
将 3 组视频按 A（植物信息展示）→ B（生长周期）→ C（功效应用）顺序拼接至时间轴，总时长 45 秒。

**转场逻辑：** 组内镜头及组际转场全面应用 L-Cut / J-Cut 逻辑——泥土破裂声、古法粗加工碰撞音等 Foley 音效提前约 0.5 秒跨越剪辑点切入，增强视听沉浸感。

**音轨层级：** BGM 与 Narration VO 分别置于独立音轨，音量层级：Narration VO > Foley > BGM。

**8b. 色彩弧光与视觉连续性审计：**

对照 `Botany_Spec.md` 核验全片色调演变是否契合设定弧光：
- A 组：清爽白底信息图
- B 组：写实自然绿棕
- C 组：生活中性明亮

核验 18 个分镜中植物叶形与花色的视觉连续性；相邻镜头视觉重心偏差控制在 20% 以内。

色彩弧光审计规范详见 `references/craft/color-arc-eye-tracing.md`。

审计通过后执行高清导出。

**暂停确认节点⑦**：最终组装完成后，向用户呈现全片。

## 暂停确认节点汇总

| 节点 | 触发时机 | 确认内容 |
|---|---|---|
| ① | Step 1 完成后 | 全局规格文件 Final_Video_Spec.md |
| ② | Step 2 完成后 | Botany_Spec.md 植物规格 |
| ③ | Step 3 完成后 | 植物解析图 Plant_Asset_01（核心视觉锚点） |
| ④ | Step 4 完成后 | 故事脚本与逐字旁白 VO 台词 |
| ⑤ | Step 5 每组完成后 | 六格分镜板图（逐组确认，核心拦截点） |
| ⑥ | Step 6 三组全部完成后 | 3 段 15 秒组级视频 |
| ⑦ | Step 8 完成后 | 最终 45 秒成片 |

## 输出契约

### 植物解析图提示词模板

```
Chinese botanical illustration of [植物学名]（[中文名]）,
retro vintage parchment paper texture, scientific botanical chart,
detailed ink and watercolor sketch, multipanel layout.
Central large [主要器官描述],
detailed cross-section under a magnifying glass,
anatomical diagrams of leaves and flowers,
small regional map, molecular structure diagrams,
step-by-step life cycle diagram at the bottom.
Elegant Chinese calligraphy headers and labels.
Highly detailed, accurate botanical drawing,
18th-century naturalist style, sepia tones, muted colors, aesthetic composition.
no watermarks, no modern UI, no neon colors.
```

### 分镜板图提示词模板

```
[植物主题] director storyboard, 2×3 grid matrix layout,
6 panels with black borders, camera movement arrows,
shot type labels (Wide/MCU/ECU/Time-lapse),
[Section A: clean white background, minimal infographic style / Section B,C: realistic documentary aesthetic],
bottom Chinese handwritten director notes.
[Section A追加: clean white background, minimal infographic style, no realistic scenery, no watermarks]
[Section B/C追加: no watermarks, no stylization, no fantasy lighting]
```

### 视频提示词模板

```
Based on storyboard reference <<<image_1>>>:
15 seconds, 6 narrative beats in sequence.
Beat 1 (0-2.5s): [运镜] [主体动作] [光线] [景深]
Beat 2 (2.5-5s): ...
Beat 3 (5-7.5s): ...
Beat 4 (7.5-10s): ...
Beat 5 (10-12.5s): ...
Beat 6 (12.5-15s): ...
Visual momentum continuity at each cut.
[Foley tags for B/C: <Foley描述>]
no split frames, no arrows, no watermarks, no subtitles, no music.
[Section A追加: no realistic background, no nature scenery, no handheld shake]
[Section B/C追加: no floating text, no annotation labels]
```

### 旁白 VO 台词模板

```
Section A (0–15s):
Grid 1 (0–2.5s): "[台词]"
Grid 2 (2.5–5s): "[台词]"
Grid 3 (5–7.5s): "[台词]"
Grid 4 (7.5–10s): "[台词]"
Grid 5 (10–12.5s): "[台词]"
Grid 6 (12.5–15s): "[台词]"

Section B (15–30s): [同上结构]
Section C (30–45s): [同上结构]
```

### 全片时间轴

```
0–15s:   Section A — 植物信息展示（白底信息图风格）
15–30s:  Section B — 植物种植过程（写实自然绿棕）
30–45s:  Section C — 植物功效与使用场景（生活中性明亮）
```

## 静默自检

交付前内部跑清单并重写弱项，不暴露给用户。

- [ ] Plant_Asset_01 是否涵盖整体形态、截面、解剖、地图、分子、生命周期六大面板？
- [ ] 三组分镜板的植物形态（叶形/花色/茎秆）是否与 Plant_Asset_01 一致？
- [ ] 每组 6 格画面是否节拍鲜明、无重复？
- [ ] 旁白 VO 台词是否与 Grid 编号严格绑定，每格约 2.5 秒台词量？
- [ ] 三组旁白是否首尾相连形成完整叙事弧？
- [ ] 每组视频是否为一次生成的 15 秒完整片段（非分段拼接）？
- [ ] Section A 视频是否保持白底信息图风格，无写实场景？
- [ ] Section B/C 视频是否为写实纪录片美学，无浮动文字与标注？
- [ ] 相邻镜头视觉重心偏差是否 ≤20%？
- [ ] 色彩弧光是否契合 A→B→C 演变？
- [ ] 音轨层级是否为 VO > Foley > BGM？
- [ ] 转场是否应用 L-Cut / J-Cut（Foley 提前 0.5 秒切入）？
- [ ] 药用功效声称是否以"传统用途"措辞表述，无医疗效果断言？
- [ ] 全文语言是否与旁白输出语言设定一致？
