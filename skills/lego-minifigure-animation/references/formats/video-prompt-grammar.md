# 图像与视频 Prompt 文法

> 本文件提供 LEGO Minifigure 动画的图像与视频 prompt 编写规范、模板和句式。

## 一、图像提示词

### 角色参考图（Turnaround Sheet）模板

```
LEGO Minifigure, official LEGO style, ABS plastic material, movie quality,
character turnaround sheet, front view / side view / back view / expression sheet,
studio lighting, high detail,
[角色外观: 发型颜色与款式、服装配色与图案、配件、面部印刷细节]
```

**示例：**

```
LEGO Minifigure, official LEGO style, ABS plastic material, movie quality,
character turnaround sheet, front view / side view / back view / expression sheet,
studio lighting, high detail,
short spiky black hair, dark blue jacket with silver zipper print, 
black pants, holding a flashlight, determined expression with raised eyebrows
```

### 场景参考图模板

```
LEGO environment, brick-built architecture, cinematic lighting, movie quality,
high detail, official LEGO style,
[景别], [时段: daytime / night / golden hour],
[场景构成描述: 建筑布局、道路、关键道具位置]
```

**示例：**

```
LEGO environment, brick-built architecture, cinematic lighting, movie quality,
high detail, official LEGO style,
wide shot, nighttime,
urban street scene with brick-built buildings on both sides, 
road made of dark gray baseplate with yellow lane markings,
streetlamp with warm glow, a brick-built car parked on the right side,
a collapsed wall section with scattered bricks in the center
```

### 图像 prompt 规则

- 所有描述限于镜头可见内容。
- 禁止心理状态或叙事意图类词汇（如"看起来很悲伤"、"陷入回忆"）。
- 角色图优先锁定跨镜头一致的外观细节（发型、服装颜色、配件）。
- 避免画面内出现无关文字。
- 分辨率 2K。

## 二、视频提示词

### Prompt 结构

```
主体描述 → 动作节拍（叙事顺序）→ 场景与环境 → 景别 + 运镜 → 光效 → LEGO 风格锚定
```

### 各部分说明

**1. 主体描述：**
- 使用占位符绑定角色与场景参考图：`<<<image_1>>>`, `<<<image_2>>>`, …
- 说明各图对应角色/场景。

**2. 动作节拍（叙事顺序）：**
- 动作描述具体到肢体部位与幅度。
- 按叙事时序列出多个动作节拍。
- 不使用"0–3s / 3–6s"等绝对时间分割。
- 仅可视化动作（如"右手拿起桌上的咖啡杯，举到嘴边"）。

**3. 场景与环境：**
- 简述场景特征与氛围。
- 引用场景参考图占位符。

**4. 景别 + 运镜：**
- 景别：ECU / CU / MCU / MS / MLS / LS / ELS
- 运镜：Static / Push In / Pull Out / Pan / Tilt / Tracking / Orbit / Handheld

**5. 光效：**
- 描述光源方向、色温、阴影特征。
- LEGO 材质的光泽反射效果。

**6. LEGO 风格锚定：**
- 固定结尾：`LEGO Minifigure style, ABS plastic material, brick-built environment, official LEGO aesthetic`

### 对白与音效标记

- 对白使用 `{台词原文}` 标记。
- 音效使用 `<音效描述>` 标记。

### Negative 标注

- 固定 negative：`no subtitles`
- 若该 Shot 有独立旁白轨，加：`no music`

### 视频 Prompt 模板

```
<<<image_1>>> (角色A参考图), <<<image_2>>> (场景B参考图),

角色A [外观简述] 在 [场景简述] 中。
[动作节拍1]; [动作节拍2]; [动作节拍3]。
{角色A: "台词原文"}
<音效: 环境音/动作音描述>

[景别], [运镜],
[光效描述],
LEGO Minifigure style, ABS plastic material, brick-built environment, official LEGO aesthetic
```

### 视频 Prompt 示例

```
<<<image_1>>> (探险家角色参考图), <<<image_2>>> (古庙场景-夜晚版),

LEGO Minifigure explorer in a brick-built ancient temple at night.
Explorer walks forward three steps, right hand raises the flashlight to eye level, 
beam of light sweeps across the wall revealing a hidden brick doorway;
left hand pushes the door panel, bricks scatter as the door swings open.
{Explorer: "Here it is... the lost chamber."}
<音效: 积木脚步声, 手电筒开关声, 积木门铰链吱嘎声, 散落积木碰撞声>

Medium Shot, Push In,
warm flashlight beam cuts through cool blue ambient darkness, 
plastic surface highlights catch the light, deep shadows between brick studs,
LEGO Minifigure style, ABS plastic material, brick-built environment, official LEGO aesthetic
```

### 视频 Prompt 规则

- 单次生成时长不超过 15 秒。≤15 秒的 Shot 用一次生成完成；>15 秒的 Shot Group 拆分为多个 ≤15 秒片段。
- 分辨率 720p。
- 参考输入必须包含该镜头涉及的所有角色与场景参考图。
- 前一 Shot 视频作为参考视频仅在与前镜头连续性极强时使用，通常跳过。
- 动作描述按叙事时序排列，不使用绝对时间分割。
- 禁止画面内字幕或浮现文字。

## 三、音频 Prompt 指引

### 对白 / 旁白

- 旁白需匹配 narration speaker profile（如"[沉稳男声，叙述语气]"）。
- 若有角色音频绑定，用于保持角色音色一致。

### BGM

- prompt 中避免出现知名艺术家名字。
- 描述音乐风格、情绪、节奏（BPM）、配器。
- 示例：`Upbeat adventure orchestral, brave and determined mood, 120 BPM, strings and brass with light percussion, no vocals`

## 落 prompt 前自检

- [ ] 图像 prompt 是否包含 LEGO 风格锚定词？
- [ ] 视频 prompt 是否按六段结构（主体→动作→场景→景别运镜→光效→LEGO 锚定）编写？
- [ ] 占位符 `<<<image_N>>>` 是否正确绑定到对应参考图？
- [ ] 动作描述是否全部可视化？有无不可视化描述？
- [ ] 对白是否用 `{台词原文}` 标记？音效是否用 `<描述>` 标记？
- [ ] negative 是否包含 `no subtitles`？有独立旁白轨时是否加了 `no music`？
- [ ] 单次生成是否 ≤15 秒？
- [ ] BGM prompt 中是否出现了知名艺术家名字？
