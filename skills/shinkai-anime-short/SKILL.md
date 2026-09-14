---
name: shinkai-anime-short
display_name: 新海诚动画短片
description: 制作新海诚风格动画短片。当用户要求生成新海诚风格动画视频、日系动画短片、青春情感动画电影风视频时触发。覆盖从故事分析、分镜设计、元素图生成到视频合成与配音的完整管线，产出电影级动画短片。
tools: ["sandbox_generate_image", "render_video", "sandbox_generate_video", "sandbox_process_video"]
---

# 新海诚动画短片

## 核心原则

不做"像动画的风景视频"，要做"天气驱动的情感叙事片"——新海诚的本质是让自然现象（天气/光线/时间）成为叙事主角，而非装饰背景。

持久引擎（因果链）：

**用户故事输入 → 角色与情绪提取 → 天气/场景/时间匹配 → 色彩系统锁定 → 分镜与镜头语言设计 → 元素图（角色/场景/道具） → 关键帧融合 → 逐 shot 视频生成 → 旁白 + BGM → 最终合成**

每一步的产出都是下一步的风格锚点：色彩系统约束分镜，分镜约束元素图的 prompt，元素图约束视频生成的首帧参考。

### 质量测试（可证伪）

如果移除天气系统（黄昏/雨/云海/星空等），故事的转折和情绪变化就无法成立——则风格成立。天气不是"好看背景"，而是"情绪的因果机制"：黄昏对应离别，雨对应思念，星空对应重逢。每个镜头必须有天气理由。

## 输入诊断

生产前，识别或合理假设以下维度：

- 故事核心：用户提供的故事文本/创意描述
- 主角设定：名字、年龄（14–25 岁）、身份、外观、性格
- 情绪曲线：关键情绪节点（如 相遇 → 陪伴 → 分离 → 重逢）
- 天气系统等级：S 级（黄昏/流星/云海/星空/雨后放晴）、A 级（暴雨/晚霞/雪景/晨曦）、B 级（阴天/晴天/微风）——优先选 S/A
- 色彩系统：晴空系 / 黄昏系 / 雨天系 / 夜景系（随情绪曲线切换）
- 场景类型：城市场景 / 校园场景 / 自然场景 / 雨景场景 / 黄昏场景 / 夜景场景
- 画幅比：默认 16:9 电影横屏
- 总时长：根据故事规模确定
- 视觉风格关键词：Makoto Shinkai, Japanese Animation, Beautiful Sky, Cinematic Anime, Weather Driven Atmosphere, Volumetric Light, Ultra Detailed Background, 4K
- 旁白风格：第一人称 / 青春文学 / 克制表达 / 轻微伤感
- BGM 方向：钢琴独奏 / 钢琴+环境音 / 钢琴+弦乐 / 钢琴+电子 / 钢琴+吟唱
- 合规敏感点：角色未成年则禁止暧昧/亲密画面；不出现真实品牌/商标；不生成暴力/血腥内容

若用户输入较少，做合理假设并继续。仅当故事核心完全空白时才发问。

## 路由表

| 输入特征 | 选用路线 | 必读 reference |
|---|---|---|
| 故事含明确角色与场景 | 标准管线 | `references/industries/shinkai-style.md` + `references/formats/storyboard-spec.md` |
| 故事仅有情绪/氛围描述 | 先补角色再走标准管线 | 同上 |
| 需要写视频 prompt | 必读 prompt 文法 | `references/formats/prompt-writing.md` |
| 需要旁白/BGM | 必读音频规范 | `references/formats/audio-voiceover.md` |
| 进入最终合成 | 必读合成规范 | `references/formats/assembly-spec.md` |

## 强制加载 reference

落 prompt 前，**必须**按路由结果加载对应 references，并把相关词汇/句式写进本技能的实际产出。

必读：
1. `references/industries/shinkai-style.md`（风格核心与角色设计）
2. `references/formats/storyboard-spec.md`（分镜设计规范：色彩/天气/场景/光影/镜头语言）
3. `references/formats/prompt-writing.md`（元素图与视频 prompt 文法）

条件读取：
- 涉及旁白或 BGM 时读 `references/formats/audio-voiceover.md`
- 进入合成阶段时读 `references/formats/assembly-spec.md`

硬规则：若最终产出包含视频生成 prompt，则本回合必须已读过 `references/formats/prompt-writing.md`。

## 工作流（步骤）

### 步骤 1：故事分析

读取用户故事输入，提取：
- 角色信息（名字、年龄、身份、外观、性格）
- 场景信息（地点、时间、天气、情绪）
- 关键物件（如雨伞、手机、信件、电车票、项链）
- 情绪曲线（如 相遇 → 陪伴 → 分离 → 重逢）

读取 `references/industries/shinkai-style.md` 中的新海诚风格核心主题与视觉关键词，校准提取结果。

### 步骤 2：全局参数锁定

建立全局参数文档，锁定：
- 画幅比（默认 16:9）
- 总时长
- 视觉风格关键词
- 色彩系统选型
- 输出语言

**暂停，请用户确认全局参数后再继续。**

### 步骤 3：分镜设计

读取 `references/formats/storyboard-spec.md`，生成 Storyboard：
- 每镜包含：场景、人物、动作、运镜、天气、光线、情绪、时长（默认 5–8 秒）
- 天气优先选 S/A 级
- 每个镜头必须声明主光源 + 次光源 + 环境光
- 镜头语言从 M01–M09 中选用

**暂停，请用户确认分镜后再继续。**

### 步骤 4：素材绑定

扫描当前上下文中用户已提供或已生成的素材，将匹配的资源绑定到 Storyboard 对应 slots。

### 步骤 5：元素图生成

读取 `references/formats/prompt-writing.md`，逐一生成：
- **角色图**：全身、电影静帧、动画电影风格、非三视图
- **场景图**：高精度背景、动画电影级美术、写实环境
- **道具图**：高细节、情绪物件、电影级质感

每张图必须携带新海诚统一风格关键词。生成后注册并绑定到 Storyboard 对应 key_element。

### 步骤 6：关键帧融合

将同一镜头的角色图 + 场景图 + 道具图融合为关键帧参考图，供视频生成使用。

**暂停，请用户确认关键帧后再继续。**

### 步骤 7：逐 shot 视频生成

读取 `references/formats/prompt-writing.md`，按 Storyboard 顺序逐 shot 生成视频。

每个 shot 的参考输入：
1. 该镜头涉及的所有元素图（角色图、场景图、道具图）
2. 关键帧融合图（如有）
3. 可选：上一 shot 的视频（仅前后镜头连续性极高时使用）

prompt 统一附加风格关键词：Makoto Shinkai Animated Film, Beautiful Sky, Volumetric Light, Cinematic Anime Lighting, Emotional Atmosphere, Ultra Detailed Background, Masterpiece

时长 ≤15s 的单 shot 用一次视频生成即可拿到完整片段；超过 15s 的 shot 拆成若干 ≤15s 片段分别生成再拼接。

### 步骤 8：旁白生成

读取 `references/formats/audio-voiceover.md`，按分镜生成旁白。
风格：第一人称、青春文学、克制表达、轻微伤感。

### 步骤 9：BGM 生成

读取 `references/formats/audio-voiceover.md`，根据故事风格选择 BGM 方向：
- 秒速五厘米风格：钢琴独奏
- 言叶之庭风格：钢琴 + 环境音
- 你的名字风格：钢琴 + 弦乐
- 天气之子风格：钢琴 + 电子
- 铃芽之旅风格：钢琴 + 吟唱

步骤 8 与 9 可在步骤 7 完成后并行执行。

### 步骤 10：最终合成

读取 `references/formats/assembly-spec.md`，执行合成：
- 轨道 1：视频
- 轨道 2：旁白
- 轨道 3：BGM
- 默认直切，章节间淡入淡出
- 禁止：字幕烧录、夸张转场、3D 特效、过度滤镜

最终输出：电影级新海诚动画短片。

## 输出契约

每 shot 的视频 prompt 结构：

```
[镜头语言 M0x] [运镜] [天气等级] [色彩系] [主光源 + 次光源 + 环境光] [画面描述] [角色动作/情绪] [统一风格关键词]
```

元素图 prompt 结构：

```
[主体类型] [画面描述] [情绪/氛围] [新海诚统一风格关键词] [分辨率 2K]
```

Storyboard 每镜字段：

| 字段 | 说明 |
|---|---|
| shot_id | 镜头编号 |
| scene | 场景（含地点/时间/天气） |
| characters | 出场角色 |
| action | 动作描述 |
| camera | 运镜（M01–M09） |
| weather | 天气等级（S/A/B） |
| light | 光源声明（主/次/环境） |
| color_system | 色彩系（晴空/黄昏/雨天/夜景） |
| emotion | 情绪 |
| duration | 时长（秒） |
| key_elements | 绑定的角色/场景/道具图 |

## 静默自检

交付前内部执行，重写弱项。不暴露给用户。

- 因果链是否每一环都成立？（天气 → 情绪 → 镜头 → 光色 是否对齐）
- 质量测试是否通过？（天气是否为情绪的因果机制而非装饰）
- 每个镜头是否声明了三种光源？
- 天气等级是否优先 S/A？
- 镜头语言是否从 M01–M09 选用且与情绪匹配？
- 色彩系统是否随情绪曲线正确切换？
- 元素图 prompt 是否包含统一风格关键词？
- 视频生成 prompt 是否以运镜起手、正向措辞？
- 旁白是否第一人称、克制表达？
- 合成是否遵守禁止项（无字幕烧录/夸张转场/3D特效/过度滤镜）？
- 角色年龄在 14–25 岁范围内，无不当画面？
- 全文语言是否中文、无中英混杂？