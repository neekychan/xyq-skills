# 文生图提示词文法 / Image Prompt Grammar

> 可适配的模式与句式，按场景改写，不要逐字照搬。

本文档覆盖两类文生图产出的提示词编写规范：植物解析图与六格分镜板图。

---

## 一、植物科学解析图提示词

### 提示词结构

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

### 编写要点

1. **植物学名与中文俗名**：使用拉丁学名 + 中文名，置于提示词开头
2. **核心识别特征**：在 "Central large" 后描述植物最具辨识度的器官
3. **风格锚定**：复古羊皮纸纹理 + 18 世纪博物学水墨水彩
4. **多面板布局**：六面板逐一描述（整体形态、放大截面、叶花解剖、地图、分子结构、生命周期）
5. **标注要求**：中文书法标题与科学标注
6. **色调约束**：赭石暖褐与哑光草绿为主（占比 ≥ 90%），沉稳克制
7. **固定尾缀**：no watermarks, no modern UI, no neon colors, highly detailed, accurate botanical drawing

详细工艺规范见 `references/industries/botanical-illustration.md`

---

## 二、分镜板图提示词

### 通用结构

```
[植物主题] director storyboard,
2×3 grid matrix layout (2 rows × 3 columns),
6 panels with black borders,
camera movement arrows and shot type labels (Wide/MCU/ECU/Time-lapse),
bottom Chinese handwritten director notes (镜头类型、运动方式、光线方向).
```

### Section A 分镜板图 — 额外要求

```
[通用结构] +
clean white background, minimal infographic style,
植物主体居中, floating text areas and indicator arrows,
色调清爽明快, no realistic scenery texture.
追加: clean white background, minimal infographic style, no realistic scenery, no watermarks.
```

- 每格背景为纯白或极浅灰
- 主体居中，风格为简洁科学信息图（infographic）
- 标注浮动文字区域和指示箭头位置
- 色调清爽明快，无写实场景纹理

### Section B/C 分镜板图 — 额外要求

```
[通用结构] +
写实科学纪录片美学, natural field tones,
自然绿与泥土暖棕为主色 (占比 ≥ 90%),
植物主体清晰、背景虚化, 强透视与景深节奏.
追加: no watermarks, no stylization, no fantasy lighting.
```

---

## 全局提示词规则

1. **提示词主体用中文撰写**；旁白台词语言遵循 Final_Video_Spec.md 中的输出语言设定
2. 分镜板图为**纯文生图，无需参考图输入**
3. 分辨率 2K，横版 16:9 比例
4. 三组分别生成，逐组暂停确认
5. 正向措辞为主，否定式约束以追加词形式放在末尾

## 落 prompt 前自检

- [ ] 植物学名与中文名是否准确？
- [ ] 六面板是否在解析图提示词中逐一描述？
- [ ] 分镜板图是否标注 2×3 矩阵、黑色边框、镜头编号？
- [ ] Section A 是否追加 clean white background, minimal infographic style？
- [ ] Section B/C 是否追加 no stylization, no fantasy lighting？
- [ ] 负向词是否包含 no watermarks？
