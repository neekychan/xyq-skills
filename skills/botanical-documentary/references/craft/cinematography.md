# 运镜与景别语言 / Cinematography

> 可适配的模式与句式，按场景改写，不要逐字照搬。

## 一、运镜词汇库

### 固定机位

| 运镜 | 英文 | 适用场景 | 说明 |
|---|---|---|---|
| 锁定 | lock-off | ECU 特写、信息图 | 完全静止，画面无运动，强调细节与精准 |
| 缓慢推进 | slow push-in | 登场、信息揭示 | 机位缓慢向主体靠近，制造专注感 |
| 缓慢拉远 | slow pull-out | 收束、全景揭示 | 从主体缓慢退远，展示环境关系 |
| 慢速推轨 | slow dolly | 收获、产品呈现 | 轨道平稳推进，电影感节奏 |
| 轨道退行 | orbital retreat | 结尾收束 | 极平稳的退行，景深虚化，情绪定格 |

### 运动机位

| 运镜 | 英文 | 适用场景 | 说明 |
|---|---|---|---|
| 手持纪实 | handheld | 采摘、灌溉、田间 | 自然晃动，纪实感强，增强临场感 |
| 急速推拉变焦 | rapid zoom push-pull | 灌溉、水珠特写 | 快速推拉，捕捉瞬态动作 |
| 低角度仰拍 | low angle | 破土萌发 | 从地面仰视，强调生长力量 |
| 微时差 | Time-lapse | 生长过程 | 压缩时间，呈现植物生长动态 |

---

## 二、景别词汇库

| 景别 | 缩写 | 说明 | 适用 Grid |
|---|---|---|---|
| 极度特写 | ECU | 微观级细节，如种子入土、细胞破裂 | B1, C3 |
| 特写 | CU | 单一主体的近距离呈现 | B6, C2 |
| 中近景 | MCU | 主体局部与部分环境 | A2 |
| 中景 | MS | 主体全貌与环境关系 | B3, B5, C1, C4 |
| 宽景 | WS | 广阔环境，人文场景 | C5 |
| 微时差 | Time-lapse | 时间压缩呈现 | B2, B3 |

---

## 三、Section 差异化运镜规则

### Section A — 白底信息图

**允许运镜**：slow push-in, lock-off
**禁止运镜**：handheld, 摇镜, 航拍, 急速推拉
**整体节奏**：缓慢、克制、理性
**光线**：均匀柔光，无方向性阴影

### Section B — 写实种植过程

**允许运镜**：lock-off (ECU), Time-lapse, handheld, rapid zoom, low angle, slow dolly
**禁止运镜**：航拍（除非有明确需要）
**整体节奏**：从微观静止 → 时间压缩 → 纪实动感 → 收束稳定
**光线**：自然天光，快速位移的光影变化（Time-lapse 段落）

### Section C — 功效与使用场景

**允许运镜**：handheld (纪实), stable CU, ECU, MS, WS, orbital retreat
**整体节奏**：纪实动感 → 微观震撼 → 生活温暖 → 极稳收束
**光线**：自然柔和光 → 温暖天光

---

## 四、视频提示词中的运镜描述格式

每个 beat 的运镜描述应包含四个要素：

```
Beat N (时间): [运镜方式] [主体动作描述] [光线演变] [景深变化]
```

### 示例

```
Beat 1 (0-2.5s): lock-off ECU, seed falling into damp loose soil particles,
soft diffused light from upper left, shallow depth of field with bokeh background.
<soil crumbling, seeds hitting damp earth>

Beat 2 (2.5-5s): low angle Time-lapse, seed coat cracking and roots pushing downward,
rapid shadow movement across frame, deep focus transitioning to shallow.
<gentle crack, soil shifting>
```

---

## 五、景深与透视规范

### Section A
- 景深：全画面清晰，无虚化（信息图风格）
- 透视：平面化，无强透视

### Section B
- 景深：强透视与景深节奏交替（ECU 浅景深 → Time-lapse 深景深 → MS 中等景深）
- 透视：低角度仰拍强调生长力量

### Section C
- 景深：从 ECU 浅景深渐变至 WS 深景深
- 透视：收束段落（C6）使用极平稳轨道退行，景深虚化

## 落 prompt 前自检

- [ ] 每个 beat 是否包含运镜、动作、光线、景深四要素？
- [ ] Section A 是否仅使用 slow push-in 和 lock-off？
- [ ] Section B 的 Time-lapse 是否标注光影快速位移？
- [ ] Section C 收束段落是否使用 orbital retreat + 景深虚化？
- [ ] Foley 标签是否仅用于 Section B/C？
