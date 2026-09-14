# Gargantuan Cinema Video Assembler

> 本文件定义视频片段生成、声音设计、配乐、字幕、调色、巨物感强化与最终输出的完整规则。所有视频必须来源于 Storyboard.md, Prompt_Bible.md, Visual_Assets.md。不得重新解释剧本，不得修改巨物外观，不得改变尺度比例。

## 目录
1. 镜头生成
2. 视频Prompt最终格式
3. 镜头运动限制
4. 镜头转场
5. 环境音设计
6. 巨物音效设计
7. 配乐设计
8. 巨物感剪辑规则（核心）
9. 字幕
10. 调色
11. 最终检查
12. 最终输出

---

## 1. 镜头生成

**生成顺序：** Chapter 01 → Chapter 02 → Chapter 03。

每一个镜头输出：
```
Shot ID: C01-S001
Duration: 10s
Image Prompt: [来自Prompt_Bible.md]
Video Prompt: [来自Prompt_Bible.md]
Negative Prompt: [来自Prompt_Bible.md]
Camera Motion: G-01 Slow Dolly Back
Transition: Cut
Audio Layer: [环境音+巨物音效描述]
Reference Images: [绑定的元素图片列表]
```

镜头编号如 C01-S001, C01-S002, C01-S003 … 保持全片唯一编号。

## 2. 视频Prompt最终格式

统一格式：
Scene → Gargantuan Subject → Scale Reference → Action → Environment → Camera Motion → Lighting → Atmosphere → Film Style → Quality → Negative Prompt

**示例：**
```
Massive mecha and kaiju charging toward each other on stormy sea, seawater just below calf level, V-shaped wave walls blasting outward, low-angle worship shot, 14mm ultra-wide, slow dolly back revealing both subjects, lightning flashing, Pacific Rim cinema, 8K, cinematic realism, --ar 16:9
```

禁止增加剧情，禁止新增巨物。

## 3. 镜头运动限制

**允许：** Static Low-Angle, Slow Dolly Back, Slow Dolly Forward, Slow Pan, Tracking (with wobble), Crane Rise, Reveal Shot, Impact Shake

**禁止：** FPV, Handheld Shaky Cam (除非灾难混乱场景), Fast Zoom, Crash Zoom, Hyperlapse, Whip Pan, Drone Racing, Selfie Angle

镜头必须具有真实摄影机重量感。

## 4. 镜头转场

默认采用 Cut（硬切）。

**允许：**
- Fade In / Fade Out（章节之间）
- Cross Dissolve（时间流逝）
- Fade To Black（结局）
- Match Cut（巨物动作匹配、光线匹配）

**禁止：** 现代MG动画、炫酷转场、闪光转场、像素化转场。

## 5. 环境音设计

环境音独立生成，分层叠加：

| 层次 | 内容 | 出现条件 |
|---|---|---|
| 底层 | 风声、海浪、暴雨、雷电、远处低频轰鸣（巨物心跳感） | 始终存在 |
| 中层 | 机甲液压声、钢缆绷紧声、焊接火花声、怪兽脚步震动、海水拍击、雾中低频回响 | 随场景出现 |
| 顶层 | 碰撞冲击波、金属扭曲、玻璃破碎、建筑倒塌、海啸轰鸣 | 冲击时刻 |

**每镜头至少一层环境底噪，冲击镜头必须有三层叠加。**

## 6. 巨物音效设计

**机甲音效资产：**
- 液压关节运转（低频嗡鸣）
- 重型足部踩地（次低音炮击感）
- 钢缆绷断（金属撕裂高频+低频回响）
- 眼窗通电（电流声+光芒爆发音效）
- 工厂维修（焊接、敲击、金属碰撞）

**怪兽音效资产：**
- 脚步震动（次低音，地面传导感）
- 嘶吼/咆哮（低频+中频，不等于狮子吼）
- 荧光脉络脉动（有机生物低频）
- 皮肤摩擦（岩石摩擦声）
- 血液滴落（液体在海中扩散声）

**禁止：** 电子游戏枪声、科幻激光声、卡通音效。

## 7. 配乐设计

巨物科幻配乐原则：**低频压倒一切，旋律让位于尺度感。**

| 章节 | 配乐设计 |
|---|---|
| 预兆（Presage） | 极低频 drone + 远处雷声 + 微弱钢琴单音 |
| 降临（Arrival） | 弦乐渐进 + 定音鼓 + 铜管乐爆发 |
| 冲击（Impact） | 全管弦乐 + 打击乐 + 次低音声波设计 |
| 余波（Aftermath） | 钢琴 + 弦乐渐弱 + 风声回归 |

**禁止：** 电子音乐、EDM、Trap、Synthwave、流行歌曲。

## 8. 巨物感剪辑规则（核心）

### 规则1：镜头时长与巨物感正相关
史诗远景/揭示镜头 ≥ 8秒，让观众"感受尺度"。禁止3秒切镜。

### 规则2：冲击镜头用慢动作延长
碰撞/拍击/碎片飞溅，采用慢动作（50%速度），让破坏感持续。

### 规则3：声音先于画面
巨物出场前0.5–1秒，先有低频轰鸣/地面震动感，再出现画面。

### 规则4：静止镜头制造压抑感
终极压迫时刻（巨物俯视/对视），镜头完全静止3–5秒，张力来自"不动"。

### 规则5：尺度跳跃用一镜到底
从人类尺度（工厂维修）→ 巨物尺度（机甲全貌），用单个后拉镜头完成，禁止切镜。

## 9. 字幕

默认不开启。开启后采用：
- **字体：** 无衬线工业字体
- **颜色：** Desaturated White / Cold Blue
- **位置：** 画面下三分之一
- 禁止彩色字幕、动画字幕

## 10. 调色

巨物科幻调色目标：**真实胶片感 + 灾难暗调**。

| 调整项 | 方向 |
|---|---|
| 冷色调 | 提高 |
| 深蓝 | 提高 |
| 墨绿 | 提高 |
| 锈铁色 | 提高 |
| 荧光蓝绿 | 提高 |
| 暖色 | 降低 |
| 绿色 | 降低 |
| 紫色 | 降低 |
| 荧光色 | 降低 |
| 胶片颗粒 | 轻微35mm颗粒感 |
| 黑位 | 略抬（保留暗部细节，巨物纹理必须可见） |
| 高光 | 自然，荧光脉络可做局部高光溢出 |

**禁止：** HDR过度、高饱和糖果色、赛博朋克色彩、明亮商业广告色。

## 11. 最终检查

输出前自动检查：
- 巨物外观一致
- 配色一致
- 发光元素一致
- 战损状态与剧情阶段匹配
- 天气一致
- 光线方向一致
- 海面波浪方向一致
- 参照物比例一致
- 镜头编号一致
- Prompt一致
- 音效与画面同步
- 配乐情绪匹配

若存在冲突，返回对应阶段重新生成。

## 12. 最终输出

**输出文件清单：**

| 文件 | 内容 |
|---|---|
| Final_Video_Spec.md | 最终视频规格说明 |
| Storyboard.md | 全部分镜设计 |
| Prompt_Bible.md | 全部Prompt |
| Visual_Assets.md | 全部视觉资产 |
| Sound_Design.md | 声音设计 |
| Music_Design.md | 配乐设计 |
| Color_Script.md | 调色方案 |
| Final_Render.md | 最终渲染参数与输出 |

输出格式：Markdown, UTF-8，保持全部可编辑。

生成完成，等待用户确认。

---

## 落 prompt 前自检

- [ ] 每镜头是否输出全部必填字段（Shot ID/Duration/Prompt/Camera/Transition/Audio）
- [ ] 镜头运动是否在允许列表内
- [ ] 转场是否在允许列表内
- [ ] 环境音是否分层（底层/中层/顶层）
- [ ] 冲击镜头是否三层叠加
- [ ] 配乐是否匹配章节情绪
- [ ] 剪辑是否遵循5条巨物感规则
- [ ] 调色是否遵循灾难暗调目标
- [ ] 字幕是否默认关闭
- [ ] 最终检查是否通过（12项一致性检查）
- [ ] 全部8个输出文件是否齐全
