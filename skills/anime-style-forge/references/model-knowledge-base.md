# 二次元风格生成策略知识库

> 本文档为 anime-style-forge Skill 的生成策略参考。
> 针对不同画风在二次元风格生成中的表现、最优 prompt 写法、适用场景和已知问题进行记录。
> **本文档应随实测结果持续更新。**
> **本文档仅供内部决策参考，不向用户展示任何模型/引擎名称。**

---

## 生成能力总览

平台生图能力在不同画风方向上各有强弱。以下按**能力维度**而非模型名称组织，供 prompt 策略路由使用。

### 能力维度定义

| 能力维度 | 含义 | 影响画风的维度 |
|------|-------------|---------|
| **2D 平涂精度** | 干净描边 + 均匀色块 + 二分阴影的还原能力 | 赛璐璃、Webtoon、轻小说 |
| **水彩/手绘质感** | 纸张纹理、晕染边缘、柔和笔触的模拟能力 | 吉卜力、水墨、韩系水彩 |
| **厚涂精致度** | 多层光影、服装细节、面部精度的渲染能力 | 手游立绘、韩系厚涂 |
| **3D/CG 渲染感** | 体积光、物理材质、次表面散射的模拟能力 | 玄幻3D、新海诚风 |
| **中文语义理解** | 中文 prompt 对画风/场景/角色的理解准确度 | 国漫全系、武侠、水墨 |
| **复古质感模拟** | 胶片颗粒、VHS、旧赛璐璃片的质感还原能力 | 90年代复古、像素风 |
| **指令遵循度** | 对"不要什么""只改什么"等约束的执行率 | 分镜/多帧、表情差分、风格转换 |
| **参考图传递** | 传入参考图后角色/构图的一致性保持能力 | 风格转换、多帧连续、三视图 |

### 能力维度 → 画风适配矩阵

| 画风 | 核心能力需求 | 平台能力评估 | 备注 |
|------|------------|------------|------|
| jp_cel 赛璐璃 | 2D平涂精度 | ⭐⭐⭐ | 能画但可能偏"AI味"，线条不够干净，需强化平涂关键词 |
| jp_ghibli 吉卜力 | 水彩/手绘质感 | ⭐⭐⭐⭐ | 水彩感不错 |
| jp_90s 90年代 | 复古质感模拟 | ⭐⭐⭐ | 需要强化 VHS/grain 关键词 |
| jp_gacha 厚涂立绘 | 厚涂精致度 | ⭐⭐⭐⭐⭐ | 强项，服装和光效细节好 |
| jp_ln 轻小说 | 2D平涂精度 + 水彩质感 | ⭐⭐⭐⭐ | 清新感好 |
| jp_shinkai 新海诚 | 3D/CG渲染感 + 厚涂精致度 | ⭐⭐⭐⭐ | 背景光影好，但人物可能偏甜 |
| cn_xuan3d 玄幻3D | 3D/CG渲染感 + 中文语义理解 | ⭐⭐⭐⭐ | 中式审美好，3D质感能出来 |
| cn_ink 水墨 | 水彩/手绘质感 + 中文语义理解 | ⭐⭐⭐⭐ | 中文 prompt "水墨风" 效果不错 |
| cn_wuxia 武侠 | 厚涂精致度 + 中文语义理解 | ⭐⭐⭐⭐ | 理解"武侠"语义 |
| kr_watercolor 韩系水彩 | 水彩/手绘质感 + 厚涂精致度 | ⭐⭐⭐⭐ | 精致面部和低饱和处理好 |
| kr_webtoon 条漫 | 2D平涂精度 + 指令遵循度 | ⭐⭐⭐⭐ | 干净线条 |
| kr_paint 韩系厚涂 | 厚涂精致度 | ⭐⭐⭐⭐⭐ | 面部精度可能是最高 |
| us_comic 欧美漫画 | 2D平涂精度 + 厚涂精致度 | ⭐⭐⭐ | 有但需强化漫画关键词 |
| chibi Q版 | 指令遵循度 | ⭐⭐⭐ | 比例控制不稳定，需强调头身比 |
| il_pixel 像素 | 复古质感模拟 + 指令遵循度 | ⭐⭐ | 不擅长，需额外提示和简化 |

---

## 1. 日系动漫方向（jp_cel / jp_ghibli / jp_90s / jp_gacha / jp_ln / jp_shinkai）

### 定位
日系是二次元生图的核心方向。平台在厚涂立绘类表现最强，水彩/手绘感次之，纯平涂赛璐璃需要额外 prompt 强化。

### Prompt 写法

**核心策略**：标签堆叠 + 自然语言混合

```
格式：[画风标签], [角色描述], [动作/姿势], [场景], [光影/氛围], [画质词]
```

**风格锚点词**：
- 赛璐璃：`anime screencap, cel shading, flat color, studio anime`
- 厚涂立绘：`game splash art, detailed illustration, painted`
- 吉卜力：`studio ghibli, watercolor, hand-drawn, warm tones`
- 90年代：`1990s anime, retro, bold outlines, VHS aesthetic`
- 轻小说：`light novel illustration, soft pastel, delicate`
- 新海诚：`Makoto Shinkai style, photorealistic background, golden hour lighting`
- Q版：`chibi, super deformed, 2-head-tall, kawaii`

### 已知问题与应对
1. **赛璐璃平涂不够"干净"**：倾向于加渐变和柔和处理，失去平涂的硬朗感 → 加强 `flat color fill, hard shadow, bold outlines` + 负向 `gradient, soft, watercolor`
2. **面部偏模板化**：大量美少女脸谱化 → 需要具体描述面部差异
3. **背景可能过于精致**：Q版/简约风格时背景容易抢戏 → 明确 `simple background`
4. **90年代复古风不理想**：VHS/胶片颗粒感模拟弱 → 强化 `VHS film grain, analog texture, nostalgic`
5. **中文 prompt 支持弱**：日系风格建议全英文 prompt

### 最佳使用场景
✅ 日系全品类（赛璐璃/吉卜力/厚涂/轻小说/Q版）
✅ 角色立绘和头像
✅ 新海诚风（背景光影强项）
❌ 国漫3D、写实向（走中文语义方向）

---

## 2. 国漫方向（cn_xuan3d / cn_ink / cn_wuxia）

### 定位
国漫方向的核心优势是**中文语义理解**——中文 prompt 对"玄幻""武侠""水墨"等概念的把握准确，远优于英文 prompt。

### Prompt 写法

**核心优势：中文 prompt 效果好**

```
中文写法（推荐国漫/武侠/水墨）：
"一个身穿青色道袍的白发老者，仙气飘飘，站在云海之上，国风仙侠风格，水墨画质感，大气留白"

英文写法（玄幻3D也可用英文）：
"Chinese fantasy 3D CGI animation, {content}, Unreal Engine 5 render quality, 
cinematic volumetric lighting, flowing silk robes with embroidery, 
ethereal spirit energy effects, dramatic cloud sea background"
```

**关键发现**：
- 中文语义理解优于英文，**国漫/武侠/水墨风格建议全中文 prompt**
- `高品质, 精细, 8K` 等中文画质词有效
- 玄幻3D 方向可用英文 + `Unreal Engine, CGI, volumetric lighting` 等渲染关键词
- 武侠/水墨方向全中文 prompt 效果最好

### 已知问题与应对
1. **玄幻3D 的 3D 感有时不够强**：需强化 `3D CGI, Unreal Engine, subsurface scattering, volumetric lighting`
2. **水墨的墨韵不够**：需强化 `ink wash, sumi-e, rice paper texture, calligraphic brush strokes`
3. **武侠可能偏日系化**：需强化 `Chinese wuxia, semi-realistic donghua, dark elegant color palette`

### 最佳使用场景
✅ 国漫系列首选（玄幻3D / 武侠 / 水墨）— 中文 prompt
✅ 需要中文语义理解的场景
❌ 纯平涂赛璐璃（走日系方向）
❌ 像素风/复古风

---

## 3. 韩系方向（kr_watercolor / kr_webtoon / kr_paint）

### 定位
韩系方向的核心优势是**面部精致度**。厚涂类的面部渲染和眼睛细节是全风格中精度最高的。

### Prompt 写法

```
韩系水彩：
"Korean manhwa watercolor style, {content}, soft pastel watercolor wash, 
delicate facial features with long eyelashes, dreamy bokeh background, 
flower petals floating, romantic ethereal atmosphere"

韩系厚涂：
"Korean digital painting portrait, {content}, extremely detailed face and eyes, 
multiple light reflections in iris, luminous translucent skin, 
rich color depth and subtle gradients, semi-realistic beautiful features"

Webtoon 条漫：
"Korean webtoon art style, {content}, clean digital black lineart, 
flat bright coloring, simple or gradient background, expressive character face"
```

### 已知问题与应对
1. **水彩的柔和感可能被破坏**：避免使用 `high contrast, bold outlines, hard shadow` 等硬朗词
2. **Webtoon 背景容易过度复杂**：明确 `simple background, clean composition`
3. **厚涂面部是灵魂**：面部和眼睛的描述要极其详细

### 最佳使用场景
✅ 韩系厚涂/精致面部（强项）
✅ 韩系水彩/朦胧言情
✅ Webtoon 条漫风格
❌ 3D 渲染类（走国漫方向）

---

## 4. 其他风格（us_comic / chibi / il_pixel）

### 定位
这些风格需要特殊 prompt 策略，平台原生支持度较低，需要额外强化关键词。

### Prompt 写法与应对

**欧美漫画**：
- 需要主动加 `American comic book art, bold black ink outlines, halftone dot texture`
- 强调 `chiaroscuro shading, muscular proportions, dynamic foreshortened`

**Q版/Chibi**：
- 必须强调 `2-head-tall, super deformed, big round head tiny body`
- 比例控制不稳定 → 加强 `chibi, SD, kawaii, simplified` 并用负向词排斥正常比例
- 若仍偏正常比例 → 降级用中文 prompt + `NORMAL ADULT HUMAN PROPORTIONS` 反向控制（当需要从Q版转正常时）

**像素风**：
- 不擅长 → 需强化 `pixel art, 16-bit, limited color palette, no anti-aliasing, crisp visible pixels`
- 建议小尺寸生成后用 ffmpeg 最近邻放大

---

## 5. 风格转换与多帧一致性方向

### 定位
当任务核心需求是**一致性 / 指令遵循 / 参考图传递**时，生成路径的选择优先于画风路由。

### 参考图锚定路径（分镜/多帧/表情差分/三视图）

**核心能力**：支持传入参考图锁定角色外貌和构图。

**多帧锚定写法（分镜）**：
```
[第N帧] 传入第N-1帧作为参考图，写明"same character same composition"
+ 本帧差异描述（仅改光线方向 / 仅改表情）
```

**构图锁定写法**：
```
"Same exact composition as reference image. Only change: [具体变量]. Keep all else identical."
```

**表情差分写法**：
```
传入角色立绘作为参考图 + "same character, same outfit, only change facial expression to [目标表情]"
```

### 风格转换路径

**跨风格转换（首选 ⭐）**：文生图路径
- 读取参考图 → 提取角色所有特征（发型/发色/眼睛/服装/姿势/表情/配件）
- 用目标风格的 prompt 模板 + 精细角色描述重新生成
- 画质和风格深度最高

**细微编辑**：图生图路径
- 传入原图 + 编辑指令（改发色/改服装颜色/加配饰）
- 仅适用于不改变整体风格的局部修改
- ⚠️ 画质低于文生图路径，有"滤镜感"而非"重绘感"

---

## 画风→生成策略推荐速查表

> 按画风 id 查首选/备选 prompt 策略，再用 SKILL.md 中「任务类型维度决策三问」覆盖校验。

| 画风 | 首选策略 | 备选策略 | 避免使用 |
|------|---------|---------|---------|
| jp_cel 赛璐璃 | 日系英文标签路线，强化平涂词 | 中文 prompt | 复古质感路线 |
| jp_ghibli 吉卜力 | 日系英文标签路线，强化水彩词 | 中文 prompt | 平涂路线 |
| jp_90s 90年代 | 日系英文标签路线，强化复古词 | — | 中文 prompt |
| jp_gacha 厚涂立绘 | 日系英文标签路线，强化厚涂词 | 中文 prompt | 平涂路线 |
| jp_ln 轻小说 | 日系英文标签路线，强化柔淡词 | 中文 prompt | 厚涂路线 |
| jp_shinkai 新海诚 | 日系英文标签路线，强化光影背景词 | — | 平涂路线 |
| cn_xuan3d 玄幻3D | 中文 prompt + 渲染关键词 | 英文 + CGI 关键词 | 纯平涂路线 |
| cn_ink 水墨 | 中文 prompt + 水墨关键词 | 英文 + ink wash | 厚涂路线 |
| cn_wuxia 武侠 | 中文 prompt + 武侠关键词 | 英文 + wuxia | 日系平涂路线 |
| kr_watercolor 韩系水彩 | 英文 + 水彩言情词 | 中文 prompt | 3D 渲染路线 |
| kr_webtoon 条漫 | 英文 + 干净勾线词 | 中文 prompt | 厚涂路线 |
| kr_paint 韩系厚涂 | 英文 + 精致面部词 | 中文 prompt | 平涂路线 |
| us_comic 欧美漫画 | 英文 + 漫画关键词 | — | 水彩路线 |
| chibi Q版 | 英文 + Q版关键词，强化头身比 | 中文 prompt | 写实路线 |
| il_pixel 像素 | 英文 + 像素关键词，小尺寸生成 | — | 3D 渲染路线 |
| 风格转换（跨风格） | 文生图路径（提取特征+目标风格重建） | 图生图（仅限细微编辑） | — |
| 比例变换（Q版↔正常） | 中文 prompt + 比例控制词 | 英文 + 比例关键词 | — |

---

## 任务类型 → 生成路径速查（优先于画风路由）

> 以下任务类型的生成路径选择由**一致性/指令遵循/参考图传递**驱动，不由风格决定。

| 任务类型 | 首选路径 | 原因 |
|---------|---------|------|
| 分镜/多帧（同角色/同场景 N≥2） | 参考图锚定路径 | 传前帧锁角色和构图 |
| 构图固定只改光影/季节 | 参考图锚定路径 | 传上一帧锁构图 |
| 表情差分（同角色多表情） | 参考图锚定路径 | 传角色图锁面部 |
| 三视图 / 多角度立绘 | 参考图锚定路径 | 传正面图锁角色 |
| 单张独立立绘/头像 | 按画风路由表 | 无跨图一致性需求，风格优先 |
| 风格转换（跨风格重建） | 文生图路径 | 提取特征 + 目标风格重建 |

---

## Prompt 语言策略速查

| 画风方向 | 推荐语言 | Prompt 风格 | 长度建议 |
|------|------|-----------|---------|
| 日系全品类 | 英文 | 标签堆叠 + 自然语言 | 中等（50-100词）|
| 国漫全系 | 中文 | 自然语言 | 长（可堆细节）|
| 韩系全品类 | 英文（中文也可） | 自然语言 | 中长 |
| 欧美漫画 | 英文 | 自然语言 | 中等 |
| Q版 | 英文 | 标签堆叠 | 中等 |
| 像素 | 英文 | 标签堆叠 | 短 |

---

## 更新日志

| 日期 | 更新内容 |
|------|---------|
| 2026-04-28 | 初版，基于已有认知整理。待实测校准。 |
| 2026-05-06 | 新增任务类型维度框架；分镜/多帧/表情差分/三视图类任务改推参考图锚定路径 |
| 2026-04-28 | Benchmark v1 实测校准：风格转换改推文生图路径；比例变换策略确认 |

---

> ⚠️ **重要**：以上评分已通过 Benchmark v1（35题/7维度）实测校准。
> Benchmark 总分 104.5/122.5（85.3%），核心发现已写入各方向"已知问题"和速查表。
