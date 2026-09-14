# Prompt 词库与固定短语

这些是可适配的模式与句式，按场景改写，不要逐字照搬。但视觉风格固定短语的核心语义不可删减，固定负向词不可遗漏。

## 目录

1. 语言优先级规则
2. 视觉风格固定短语（每条 image/video prompt 均须包含）
3. 场景专属环境短语
4. 图像 prompt 结构
5. 视频 prompt 结构与运动描述栈
6. 摄影机运动词库
7. 斯皮尔伯格镜头语言词汇
8. 固定负向词
9. 禁止使用词汇清单

---

## 1. 语言优先级规则

**最高优先级（全局）：** 用户使用中文交互时，prompt 正文以中文书写；片中对白/旁白台词须遵循 Final_Video_Spec 指定的输出语言。视觉风格固定短语保留英文以确保模型执行。

---

## 2. 视觉风格固定短语

**每条 image/video prompt 均须包含以下短语，可微调措辞但不可删减核心语义：**

> 35mm film grain, 1993 Hollywood realism, 16:9 aspect ratio, desaturated vintage green tones, natural physical lighting, warm heavy film grain, soft vintage cinematic color grading, 8K film restoration quality, low saturation, practical light sources, Spielberg cinematography

---

## 3. 场景专属环境短语

### 热带丛林场景

凡涉及岛屿热带丛林或户外丛林场景的 image/video prompt，从以下词组中按需选取融入，不可与视觉风格固定短语冲突：

> outdoor tropical rainforest, diffused overcast sky light, Tyndall light beams through jungle canopy, dappled light filtering through leaf gaps, humid rainforest haze and water vapor, wet foliage specular highlights, moist earth and moss-covered ground, ancient towering trees with buttress roots, primeval jungle terrain, tropical island natural landscape

### 访客中心场景

凡涉及访客中心或室内建筑场景的 image/video prompt，从以下词组中按需选取融入，不可与视觉风格固定短语冲突：

> indoor atrium with skylight diffused natural light, warm tungsten practical light fill, dinosaur skeleton spotlight casting sharp bone shadows, large glass curtain wall reflections, high vaulted ceiling interior, warm mixed light from skylights and tungsten lamps, 1990s commercial building interior lighting, stone floor with soft reflected light, tropical foliage inside lobby, deep shadow contrast under display spotlights

---

## 4. 图像 prompt 结构

**结构顺序：** 主体 + 动作/姿态 → 环境/背景 → 光线条件 → 视觉风格固定短语 → 构图/镜别

要点：
- key_element 图像：锁定外观、服装、材质状态；避免画面内出现无关文字。
- 角色图：生成横向拼合参考图——左侧头肩特写（面部特征锚定）、右侧全身（服装/体型）。
- 恐龙类 prompt 须遵守 `references/elements-dinosaurs.md` 第2节的专属规范。
- 禁止使用现代电影风格词汇（如 "cinematic HDR"、"neon color"、"hyper-sharp 4K"）。

---

## 5. 视频 prompt 结构与运动描述栈

### 参考图绑定

使用占位符 <<<image_1>>>、<<<image_2>>> …，每个角色/场景独立标注。

### 运动描述栈（按此顺序组织视频 prompt）

**摄影机**（运动类型/速度）→ **主体**（动作节拍/面部反应）→ **空间**（环境变化/遮挡关系）→ **音效提示**（环境音/SFX；若无独立 VO 轨则在此注明）

### 音效标记格式

- SFX 标记：`SFX <...>`
- 对白标记：`{...}`（非项目语言时在括号前标注语言）
- 片名/字幕标记：`【...】`

---

## 6. 摄影机运动词库

设计 shot 时按需引用，标注具体运动参数：

| 运动类型 | 典型用途 |
|---|---|
| 稳定轨道缓慢推进（steady dolly push） | 积累张力；人物发现生物前的漫长等待 |
| 低空贴地跟拍（low-level ground tracking） | 强调恐龙腿部冲击力与地面震动感 |
| 航拍海岛远景（aerial establishing shot） | 开场或转场，交代岛屿地貌宏观格局 |
| 快速手持晃动（fast handheld shake） | 追逐/惊吓段落，快速提升紧张感 |
| 恐龙头部极近特写（ECU dinosaur head） | 强调眼神、鼻孔张合、皮肤纹理细节 |
| 俯瞰整片雨林（overhead aerial jungle canopy） | 展示热带丛林规模；营造空旷与未知感 |
| 长焦远景全景（telephoto wide shot） | 压缩纵深，使背景恐龙显得更近、更巨大 |
| 缓慢平移长镜头（slow lateral pan, long take） | 跟随角色行进或扫描场景全貌 |
| 升格慢镜头（overcrank slow motion） | 强调关键动作细节（恐龙冲刺/跌落/撞击）；保留胶片颗粒感 |

---

## 7. 斯皮尔伯格镜头语言词汇

按需在视频 prompt 中使用：

- slow dolly push
- low angle upshot
- foreground obstruction
- rack focus
- wide establishing then cut to reaction
- handheld slight shake for tension
- low-level ground tracking shot
- aerial establishing wide shot
- fast handheld shake
- ECU (extreme close-up) dinosaur head
- overhead aerial jungle canopy shot
- telephoto wide shot
- slow lateral pan long take
- overcrank slow motion

---

## 8. 固定负向词

每条视频 prompt 须包含以下负向词：

- **no subtitles** —— 字幕在装配阶段处理
- **no music** —— BGM 在独立音频层处理
- 若有独立 VO 轨：**no voiceover in video** —— VO 在独立音频层处理

---

## 9. 禁止使用词汇清单

以下词汇偏离1993年原版视觉，禁止出现在任何 prompt 中：

**现代电影风格词：**
- cinematic HDR
- neon color
- hyper-sharp 4K
- modern CGI look

**恐龙类禁止词（详见 `references/elements-dinosaurs.md`）：**
- feathered（含任何羽毛/原羽/绒毛描述）
- sleek smooth skin
- vibrant saturated scales
- 任何《侏罗纪世界》改版视觉描述（蓝灰金属光泽、疤痕纹路等）
