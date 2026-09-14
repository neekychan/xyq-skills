# 音频层规范 / Audio Layer Specification

> 可适配的模式与句式，按场景改写，不要逐字照搬。

## 三层音频架构

全片包含三条独立音轨，层级关系如下：

| 音轨 | 类型 | 音量层级 | 说明 |
|---|---|---|---|
| Track 1 | Narration VO | 最高 | 逐字旁白，与分镜 Grid 编号绑定 |
| Track 2 | Foley | 中 | 环境音效与拟音，仅 Section B/C 写实段落 |
| Track 3 | BGM | 最低 | 深沉管弦乐背景音轨，全片铺底 |

---

## Narration VO 规范

### 台词要求

- **语言风格**：深沉磁性的纪录片解说腔——语速平稳、信息密度高、情感克制有力量感；避免口语化和广告腔
- **绑定规则**：台词与 Grid 编号严格绑定，每格对应约 2.5 秒台词量
- **叙事弧**：三组台词首尾相连形成完整的植物人文叙事弧
  - Section A：报出学名与别称 → 描述核心形态特征与产地 → 点明生长习性与主要成分 → 简要预告生命旅程
  - Section B：描述种植条件 → 呈现生长过程关键节点 → 点明人工干预的意义
  - Section C：列举核心功效与用途 → 串联加工到应用的转化链 → 升华植物与人类文明的关系

### 台词录入格式

将完整逐字台词录入对应的 audio_layer，含每格时间锚点：

```
Section A — Narration VO
audio_layer:
  type: narration
  segments:
    - grid: A1
      time: 0–2.5s
      text: "[逐字台词]"
    - grid: A2
      time: 2.5–5s
      text: "[逐字台词]"
    - grid: A3
      time: 5–7.5s
      text: "[逐字台词]"
    - grid: A4
      time: 7.5–10s
      text: "[逐字台词]"
    - grid: A5
      time: 10–12.5s
      text: "[逐字台词]"
    - grid: A6
      time: 12.5–15s
      text: "[逐字台词]"

Section B — Narration VO
[同上结构，grid: B1–B6, time: 0–15s 偏移至 15–30s]

Section C — Narration VO
[同上结构，grid: C1–C6, time: 0–15s 偏移至 30–45s]
```

### 合规约束

涉及药用功效声称时（如人参、藏红花），旁白须以"传统用途""民间常用于"等措辞表述，不做医疗效果断言。

---

## BGM 规范

### 生成规格

- 风格：深沉管弦乐，纪录片配乐质感
- 时长：45 秒
- 触发时机：3 组视频全部确认后生成

### 使用规范

- BGM 置于独立音轨，音量为最低层
- 全片铺底，不与 Narration VO 抢频
- 色调与全片色彩弧光匹配：A 段克制理性 → B 段生机舒展 → C 段温暖升华

---

## Foley 音效规范

### 使用范围

仅 Section B/C 写实段落使用 Foley 标签，Section A 白底信息图段落不使用。

### Foley 标签格式

在视频提示词中嵌入 `<Foley描述>` 标签：

```
Beat 1: ... <soil crumbling, seeds hitting damp earth>
Beat 4: ... <water mist spraying, droplets hitting leaves>
```

### 常用 Foley 音效

| 场景 | Foley 描述 |
|---|---|
| 播种入土 | soil crumbling, seeds hitting damp earth |
| 破土萌发 | gentle crack, soil shifting |
| 水雾喷洒 | water mist spraying, droplets on leaves |
| 剪刀修剪 | snip, shearing, branch snapping |
| 收获穗头 | rustling, weight settling |
| 古法采摘 | hands tearing, stems snapping |
| 石磨研磨 | grinding, crushing, fiber tearing |
| 细胞破裂 | wet pop, liquid splashing |
| 日常应用 | ambient warmth, soft conversation |

### 转场 Foley

组际转场应用 L-Cut / J-Cut 逻辑：泥土破裂声、古法粗加工碰撞音等 Foley 音效提前约 0.5 秒跨越剪辑点切入，增强视听沉浸感。

详细组装规范见 `references/formats/assembly-spec.md`。

## 落 prompt 前自检

- [ ] 旁白台词是否逐字撰写并与 Grid 编号绑定？
- [ ] 每格台词量是否约 2.5 秒？
- [ ] 三组旁白是否首尾相连形成叙事弧？
- [ ] BGM 是否为 45 秒深沉管弦乐？
- [ ] Foley 标签是否仅用于 Section B/C？
- [ ] 药用功效声称是否以"传统用途"措辞表述？
- [ ] 音轨层级是否为 VO > Foley > BGM？
