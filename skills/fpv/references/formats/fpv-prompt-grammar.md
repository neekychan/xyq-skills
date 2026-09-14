# FPV 视频 prompt 文法

> 可适配的模式与句式，按场景改写，不要逐字照搬。

## 目录
1. prompt 结构
2. 相机与运镜要素
3. 速度与节奏描述
4. 空间结构描述
5. 光线与氛围
6. 实体标签规范
7. 完整示例
8. 落 prompt 前自检

## 1. prompt 结构

每条 FPV 视频 prompt 按以下顺序组织：

```
[相机/视角] + [飞行动作] + [空间结构] + [主体/环境] + [速度节奏] + [光线氛围]
```

优先使用正向措辞，不堆否定式约束（否定式留给内部自检）。

## 2. 相机与运镜要素

### 视角
- `FPV first-person view` —— 第一人称穿越视角（默认）
- `FPV drone perspective, slightly elevated` —— 略高于人眼的无人机视角
- `FPV low-angle, ground level` —— 贴地低角度

### 飞行动作（按风格）
- 前飞：`FPV forward flight`
- 俯冲：`FPV steep dive / nosedive`
- 拉升：`FPV rapid ascend / pull-up`
- 螺旋：`FPV spiral around [Subject], clockwise/counterclockwise`
- 侧飞：`FPV lateral flight / strafing`
- 穿越结构：`FPV fly through [Structure]`
- 急转：`FPV sharp turn / banked turn`
- 倒飞：`FPV reverse flight / flying backward`
- 翻滚：`FPV roll / flip`

### 复合动作
- 俯冲穿门：`FPV dive through [Structure] entrance`
- 螺旋拉升：`FPV spiral ascend from [Subject]`
- 贴壁急转：`FPV close wall flight followed by sharp turn`
- 低空穿缝：`FPV low-altitude fly through narrow gap`

## 3. 速度与节奏描述

避免笼统的"fast/slow"，使用具体节奏描述：

| 节奏 | 描述 |
|---|---|
| 匀速 | `steady speed, constant velocity` |
| 加速 | `accelerating, gaining speed` |
| 减速 | `decelerating, slowing down` |
| 急加 | `rapid acceleration, burst of speed` |
| 急停 | `sudden stop, hovering briefly` |
| 变速 | `dynamic speed changes, alternating fast and slow` |
| 全程高速 | `high speed throughout, adrenaline pace` |

### 节奏叙事
- 压迫→释放：`starts tight and confined, then bursts into open space`
- 沉浸→冲击：`begins with slow immersive flight, then sudden acceleration`
- 线性→螺旋：`straight forward flight transitions into spiral around [Subject]`

## 4. 空间结构描述

### 穿越结构类型
- 门/拱门：`archway / doorway / gate`
- 窗户：`open window / French window`
- 缝隙：`narrow gap / crevice / slit between structures`
- 桥洞：`bridge underpass / tunnel`
- 树丛：`tree canopy gap / forest opening`
- 峡谷：`canyon passage / gorge narrows`
- 走廊：`corridor / hallway`

### 空间纵深线索
- 近景遮挡：`foreground objects blur past` / `nearby structures rushing by`
- 远景展开：`distant vista unfolds` / `expansive view revealed beyond`
- 纵深隧道：`tunnel-like perspective, walls closing in then opening`

## 5. 光线与氛围

### 光线方向
- 顺光：`front-lit, well-illuminated scene`
- 逆光：`backlit, silhouette against bright background`
- 侧光：`side-lit, dramatic shadow play`
- 顶光：`overhead lighting, minimal shadows`
- 穿光：`burst of light when exiting structure`

### 时段与氛围
- 黄金时刻：`golden hour, warm cinematic light`
- 蓝调时刻：`blue hour, cool twilight atmosphere`
- 正午：`midday harsh light, high contrast`
- 夜景：`night scene, artificial lights, moody atmosphere`
- 雾天：`misty/foggy, ethereal depth layers`
- 电影质感：`cinematic quality, film grain, rich color grading`

## 6. 实体标签规范

使用稳定标签绑定复现实体，确保 prompt 中同一实体前后一致：

- 主体：`Subject1`（人物）、`Building1`（建筑）、`Landscape1`（风景）、`Vehicle1`（车辆）、`Interior1`（室内）、`Canyon1`（自然隧道）
- 穿越结构：`Archway1`、`Doorway1`、`Tunnel1`、`Gap1`
- 环境：`Sky1`、`Water1`、`Forest1`、`Road1`

## 7. 完整示例

### 人物 + 螺旋环绕 + 标准
```
FPV first-person view. Fly through Archway1 at moderate speed, Subject1 standing in courtyard beyond. FPV spiral around Subject1 clockwise, radius narrowing from 5m to 2m. Cinematic golden hour light from the left, warm tones. Subject1's hair and clothes gently moving in the wind created by FPV proximity. Slow deceleration as spiral completes.
```

### 建筑 + 高空俯冲 + 高难度
```
FPV drone perspective. Steep nosedive from 3x Building1 height, rapid acceleration. Close wall flight alongside Building1 glass facade, sharp banked turn left. FPV squeeze through narrow Gap1 between Building1 and Building2, decelerating. Re-enter open space, another sharp turn, FPV fly through Building1 entrance archway. Interior briefly dark then bright exit. High speed throughout, adrenaline pace. Overcast sky, cool cinematic grading.
```

### 风景 + 低空贴地 + 标准
```
FPV low-angle, ground level. Fly low over Landscape1 terrain at 0.5m altitude, following ground contour. FPV fly through Forest1 canopy gap, branches rushing past foreground. Skim over Water1 surface, reflection visible. FPV gradual ascend revealing Landscape1 mountain panorama. Starts tight and confined in forest, then bursts into open lakeside. Golden hour, warm side-light.
```

### 车辆 + 急速穿梭 + 标准
```
FPV first-person view. Chase Vehicle1 from behind, accelerating to match speed. FPV overtake Vehicle1, passing close alongside driver side. Continue forward, FPV fly through Tunnel1 underpass, Vehicle1 visible behind. Exit tunnel into open road, decelerating. Daylight, harsh midday sun, high contrast on Vehicle1 metallic surface.
```

## 8. 落 prompt 前自检

- 是否以"FPV + 视角"起手？
- 是否包含至少一个具体飞行动作（不仅是"fly"）？
- 是否描述了穿越结构（门/缝/桥洞等）？
- 速度节奏是否有变化（非全程匀速）？
- 光线方向是否与飞行方向协调？
- 实体标签是否一致（同一对象用同一标签）？
- 是否使用正向措辞（无"no/not/avoid"堆砌）？
- 氛围描述是否足够具体到可生成？
