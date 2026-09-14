# 视频提示词文法 / Video Prompt Grammar

> 可适配的模式与句式，按场景改写，不要逐字照搬。

## 生成规格

- 方式：参考图生视频（以六格分镜板图作为参考图驱动）
- 分辨率：720p
- 时长：15 秒/组
- 参考图：该组已确认的六格分镜板图

## 视频时长说明

每组 15 秒视频用一次生成即可拿到完整成片。6 个 beat（每格约 2.5 秒）是同一条 prompt 内的时间轴描述，不是分段多次生成。全片 45 秒由 3 组各自独立生成的 15 秒片段拼接而成。

## 提示词结构

```
Based on storyboard reference <<<image_1>>>:
15 seconds, 6 narrative beats in sequence.

Beat 1 (0-2.5s): [运镜方式] [主体动作] [光线演变] [景深变化]
Beat 2 (2.5-5s): [运镜方式] [主体动作] [光线演变] [景深变化]
Beat 3 (5-7.5s): [运镜方式] [主体动作] [光线演变] [景深变化]
Beat 4 (7.5-10s): [运镜方式] [主体动作] [光线演变] [景深变化]
Beat 5 (10-12.5s): [运镜方式] [主体动作] [光线演变] [景深变化]
Beat 6 (12.5-15s): [运镜方式] [主体动作] [光线演变] [景深变化]

Visual momentum continuity at each cut.
[Foley tags for B/C: <Foley描述>]

no split frames, no arrows, no watermarks, no subtitles, no music.
```

## 编写要点

1. **参考图开头**：以六格分镜参考图 <<<image_1>>> 作为提示词起点
2. **逐格描述**：按故事顺序逐格描述 6 个动态节拍
3. **每格四要素**：运镜方式 + 主体动作 + 光线演变 + 景深变化
4. **动量连续**：标注每格切换时视觉中心动量连续
5. **Foley 音效**：Section B/C 写实段落使用 Foley 标签 `<Foley描述>`
6. **固定尾缀**：no split frames, no arrows, no watermarks, no subtitles, no music

## Section A 视频提示词 — 额外要求

```
[通用结构] +
纯白背景, 植物主体居中,
信息标签与浮动文字以动态渐显方式出现,
镜头以缓慢推进或 lock-off 为主, 避免写实场景运镜 (如摇镜、航拍),
整体风格参考科学纪录片片头信息展示段落.
追加负向词: no realistic background, no nature scenery, no handheld shake.
```

- 纯白背景，植物主体居中
- 信息标签与浮动文字以动态渐显方式出现
- 镜头以缓慢推进或 lock-off 为主，避免写实场景运镜
- 整体风格参考科学纪录片片头信息展示段落

## Section B/C 视频提示词 — 额外要求

```
[通用结构] +
写实科学纪录片风格, 电影级镜头语言,
Foley 音效标签按需嵌入.
追加负向词: no floating text, no annotation labels.
```

- 写实科学纪录片风格
- 电影级镜头语言
- Foley 音效标签按需嵌入

## 运镜与景别词汇

详细运镜与景别规范见 `references/craft/cinematography.md`。

常用运镜词汇：
- lock-off（锁定）
- slow push-in（缓慢推进）
- slow pull-out（缓慢拉远）
- tracking shot（推轨）
- handheld（手持纪实）
- rapid zoom（急速推拉变焦）
- slow dolly（慢速推轨）
- orbital retreat（轨道退行）

常用景别词汇：
- ECU（极度特写）
- CU（特写）
- MCU（中近景）
- MS（中景）
- WS（宽景）
- Time-lapse（微时差）

## 落 prompt 前自检

- [ ] 是否以参考图 <<<image_1>>> 开头？
- [ ] 是否标注 15 秒、6 个 beat？
- [ ] 每个 beat 是否包含运镜、动作、光线、景深四要素？
- [ ] 是否标注视觉中心动量连续？
- [ ] Section B/C 是否嵌入 Foley 标签？
- [ ] 固定尾缀是否完整？
- [ ] Section A 是否追加 no realistic background, no nature scenery, no handheld shake？
- [ ] Section B/C 是否追加 no floating text, no annotation labels？
