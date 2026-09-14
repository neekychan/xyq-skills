# LEGO Minifigure 角色与场景设计词库

> 本文件提供 LEGO Minifigure 风格的角色与场景设计专业用词，确保生成结果符合官方 LEGO 美学标准。

## 一、角色设计用词

### Minifigure 比例关键词

固定使用以下描述锁定 Minifigure 比例：

- `LEGO Minifigure` / `official LEGO style`
- `ABS plastic material` — 塑料材质
- `minifigure proportions` — 标准比例（头大身小，约 1:1.5 头身比）
- `C-clip hands` — C 型夹手
- `printed facial features` — 印刷面部细节
- `stud on top of head` — 头顶凸粒
- `movie quality` — 电影级品质

### 发型词汇

| 类型 | 用词示例 |
|---|---|
| 短发 | short black hair, slicked back hair, spiky hair |
| 长发 | long flowing hair, ponytail, braided hair |
| 特殊造型 | messy hair, afro, bald with printed stubble |
| 头饰 | space helmet, knight helmet, explorer hat, construction hard hat |

### 服装配色与图案

- 使用具体色名：`bright red`, `dark blue`, `yellow`, `white`, `dark gray`, `lime green`
- 图案描述：`printed logo on chest`, `utility belt with pouches`, `racing stripes`
- 职业标识：`scientist lab coat`, `police uniform with badge`, `knight armor with crest`

### 配件词汇

| 类型 | 用词示例 |
|---|---|
| 手持物品 | coffee cup, wrench, sword, flashlight, laptop, magnifying glass |
| 佩戴物品 | cape, backpack, glasses, scarf, tool belt |
| 特殊配件 | jetpack, wings, robotic arm, diving tank |

### 面部印刷细节

- 表情：`standard smile`, `determined expression`, `surprised face`, `serious brow`
- 特殊面部：`eyepatch`, `beard print`, `scar print`, `cybernetic eye`

### Turnaround Sheet 构图要求

```
角色参考图必须为横版拼排，包含：
- 正面视图（front view）
- 侧面视图（side view）
- 背面视图（back view）
- 表情图（expression sheet）：至少 3 种表情
```

### 角色描述句式模板

```
LEGO Minifigure, official LEGO style, ABS plastic material, movie quality,
character turnaround sheet, front view / side view / back view / expression sheet,
studio lighting, high detail,
[发型颜色与款式], [服装配色与图案], [配件], [面部印刷细节]
```

## 二、场景设计用词

### 积木搭建逻辑关键词

固定使用以下描述锁定场景的积木风格：

- `LEGO environment` / `brick-built architecture`
- `stud-visible surfaces` — 表面可见凸粒
- `plate and brick construction` — 板砖搭建结构
- `geometric shapes` — 几何造型
- `no organic curves` — 无有机曲线
- `snapped-together modules` — 拼接模块
- `official LEGO style`

### 建筑元素词汇

| 类型 | 用词示例 |
|---|---|
| 墙体 | brick wall with visible studs, stacked plates, window frame with panes |
| 屋顶 | sloped brick roof, flat tile roof, dome made of curved slopes |
| 门 | hinged door panel, archway made of curved bricks, garage door |
| 地面 | baseplate with road pattern, tiled floor, grass stud surface |

### 家具与道具词汇

| 类型 | 用词示例 |
|---|---|
| 桌椅 | brick-built table, chair with backrest, stool |
| 电子设备 | computer monitor on stand, control panel with buttons, screen display |
| 储物 | shelf with stacked items, treasure chest, tool rack |
| 交通工具 | car chassis with wheels, spaceship cockpit, motorcycle |

### 自然元素词汇

所有自然元素必须用积木方式表达：

| 类型 | 用词示例 |
|---|---|
| 树木 | brick-built tree with leaf clusters, cylindrical trunk with foliage pieces |
| 水体 | trans-blue plate water surface, wave bricks, transparent blue tiles |
| 地形 | rock formations made of angular bricks, mountain with stepped slopes |
| 植物 | flower stem pieces, bush clusters made of leaf elements |

### 时段光照词汇

| 时段 | 用词示例 |
|---|---|
| 白天 | bright daylight, clear sky, natural sunlight on stud surfaces |
| 夜晚 | night scene, streetlamp glow, window light, moonlight, blue-toned shadows |
| 黄昏 | golden hour, warm orange light on bricks, long shadows across baseplate |

### 场景描述句式模板

```
LEGO environment, brick-built architecture, cinematic lighting, movie quality,
high detail, official LEGO style,
[景别], [时段: daytime / night / golden hour],
[场景构成描述: 建筑布局、道路、关键道具位置]
```

## 三、场景变体设计指引

每个场景根据剧情需要生成以下版本：

- **白天版（daytime）**：自然光，色彩鲜明，适合建立镜头。
- **夜晚版（night）**：人造光源，蓝调阴影，适合紧张/悬疑段落。
- **关键动作版（action variant）**：在场景中加入动作所需的可动元素或破坏痕迹（如倒塌的积木墙、散落的道具），适合高潮段落。

## 落 prompt 前自检

- [ ] 角色 prompt 是否包含 `LEGO Minifigure` + `official LEGO style` + `ABS plastic material`？
- [ ] 角色 turnaround sheet 是否包含正面/侧面/背面/表情图四个视图？
- [ ] 发型、服装、配件、面部印刷是否全部具体描述？
- [ ] 场景 prompt 是否包含 `LEGO environment` + `brick-built architecture`？
- [ ] 场景元素是否全部使用积木几何造型？有无有机曲线？
- [ ] 自然元素（树、水、岩石）是否用积木方式表达？
- [ ] 时段光照是否明确标注？
- [ ] 描述是否限于镜头可见内容？有无心理状态或叙事意图类词汇？
