# 图像提示词写法（TextToImage / ImageToImage, GPT Image 2）

> 可适配的模式与句式，按场景改写，不要逐字照搬。

## 目录

1. 核心风格锚定词
2. 角色三视图提示词
3. 场景参考图提示词
4. 生物与道具参考图提示词
5. 布光与材质规范
6. 风格禁忌

---

## 1. 核心风格锚定词

融入所有图像描述中的风格锚定词：

```
cinematic 3D CGI animation, semi-realistic anime style, post-apocalyptic sci-fi,
high-fidelity rendering, subsurface scattering skin, pore-level detail,
dirty realism aesthetic, cinematic lighting, volumetric light rays with dust particles,
muted color palette with selective vivid accents
```

## 2. 角色三视图提示词

**生成方式：** TextToImage（首版）/ ImageToImage（多造型，参考前序生成保持一致性）
**画幅：** 强制 16:9
**分辨率：** 2K
**格式要求：** 全身三视图（正面全身 | 侧面全身 | 背面全身）横向排列，统一光源与比例。

### 提示词结构

```
[核心风格锚定词], character reference sheet, full body turnaround sheet,
three views arranged horizontally: front view | side profile view | back view,
uniform lighting and proportions across all three views,

[角色面部描述]: semi-realistic anime face, slightly stylized but grounded,
pore-level skin detail, subsurface scattering, sweat stains, grime,
realistic hair physics with weight and movement,

[角色服装与装备描述]:
(猎荒者) tactical military functional gear, tight dark combat suit,
modular tactical vest, mechanical exoskeleton frame, HUD visor helmet,
high-top tactical boots, scratches patches dust and bloodstains on equipment;
(灯塔上层人员) white/light-gray sterile uniform, clean orderly appearance,

[造型变体描述]: 多造型时逐一描述 (Variant 1: ...; Variant 2: ...),

character sheet layout, white background, full body visible from head to toe,
no cropping, no half-body, 16:9 aspect ratio
```

### 禁止

- 半身图、头像图、单角度图
- 日系二次元大眼夸张、平涂赛璐璐
- 干净全新无磨损的服装

## 3. 场景参考图提示词

**生成方式：** TextToImage
**画幅：** 强制 4:3
**分辨率：** 2K
**格式要求：** 多角度无人物四宫格（2×2 网格）。

### 提示词结构

```
[核心风格锚定词], environment reference sheet, four-panel grid layout (2x2),
no characters, multiple angle views of the same location,

[按场景类型描述]:

(地表废土) ruined city skeleton frames, rusted vehicles half-buried in sand,
cracked highways, yellow dust or spore-laden grey sky,
distant colossal silhouette on horizon, Tyndall light beams piercing through clouds,
earth tones: dusty yellow, rust red, grey-brown;

(灯塔内部) cold blue-white LED lighting, sterile metal corridors,
dense control panels with glowing screens, tiered residential zones,
surveillance dystopian atmosphere, harsh artificial lighting,
industrial cold grey and deep blue palette;

(玛娜生态核心区) fleshy flower-like structures with visible veins and bioluminescence,
vines covering ruins, black organic soil ground with breathing undulation,
spore fog, Lovecraftian biological horror aesthetic,
dark red bioluminescent blue deep purple, wet viscous and chitinous textures;

(龙骨村) neo-Chinese sci-fi style, terraced farming fields,
traditional village mixed with high-tech elements,
warm yellow bonfire light, cave-like redemptive atmosphere,
warm amber and soft gold tones,

four-panel grid, no people, 4:3 aspect ratio
```

### 禁止

- 有人物出现在场景图中
- 非四宫格的单角度图
- 明亮高饱和色彩

## 4. 生物与道具参考图提示词

**生成方式：** TextToImage（首版）/ ImageToImage（多形态）
**画幅：** 4:3
**分辨率：** 2K

### 生物提示词结构

```
[核心风格锚定词], creature reference sheet, neutral background, multiple angles,

(噬极兽) grey-brown/dark-red tightly stretched skin, pathological growth plaques,
reverse-jointed six limbs, serrated bone dorsal fin,
retractable fleshy tentacles on neck, fangs dripping corrosive viscous saliva,
some with multiple eyes or degenerated eye sockets,
full body visible showing complete morphology and biomechanical detail;

(脊蛊) spinal column segments articulated together, multiple legs for rapid movement,
full body visible;

(玛娜之花) massive fleshy flower/organ structure, visible veins,
bioluminescence, pulsing rhythm, full structure visible,

horror realism, biomechanical plausibility, 4:3 aspect ratio
```

### 道具提示词结构

```
[核心风格锚定词], prop reference sheet, neutral background, multiple angles,
[道具描述]: [具体道具名称与外观], worn and weathered condition,
functional military-industrial design, 4:3 aspect ratio
```

### 禁止

- 卡通化或 Q 版怪物
- 生物体型不完整
- 华丽魔法特效风格

## 5. 布光与材质规范

### 布光

须体现强烈明暗对比（Chiaroscuro）与丁达尔效应——体积光穿透废墟/云层，光束中悬浮尘埃与孢子。

### 材质

须体现：
- 金属划痕锈蚀油污
- 皮革布料磨损褶皱
- 皮肤次表面散射
- 岩石风化苔藓

**脏旧美学（Dirty Realism）是核心。**

## 6. 风格禁忌（提示词层面）

避免以下词汇与描述：
- 日系二次元 / 平涂赛璐璐
- 明亮高饱和
- "干净全新"措辞
- 卡通 / Q版怪物
- 魔法特效
- 霓虹泛滥赛博朋克
