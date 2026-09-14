# 图像资产生成提示词规范

> 这些是可适配的模式与句式，按场景改写，不要逐字照搬。

## 目录

1. 图像生成全局规范
2. 角色全身三视图提示词
3. 场景四宫格参考图提示词
4. 战车设定图提示词
5. 一致性微调控制
6. 参考图资产校验规范

## 1. 图像生成全局规范

- 画幅统一 16:9，分辨率 2K。
- 所有图像必须呈现米勒式实拍废土视觉：真实重型机械、粗粝手工拼装材质、极端沙漠日光、赭橙色地表与深青蓝天空形成清晰分离。
- 画面保持高对比和高可读性，但人物肤色、铁锈、火焰与沙尘不得被统一覆盖青橙滤镜。
- 绝不出现赛博霓虹、塑料质感CG、数字故障或电子游戏式视觉。

## 2. 角色全身三视图提示词

强制加入以下关键词确保三视图质量：

```
character sheet, full-body multi-angle view showing front, side, and back profiles of the same character, full-body model sheet, consistent details, standing pose
```

要求：
- 正面、侧面、背面均为直立全身，严禁生成任何半身照。
- 特征高度连贯，同一角色的服装、妆容、装备在三个角度保持一致。
- 若角色有废土朋克视觉特质（如不均匀分布的磨损皮革、拼接金属扣件、特定部落妆容涂装、图腾和专属特征），须在提示词中明确描述。

## 3. 场景四宫格参考图提示词

强制加入以下排版关键词：

```
quad-split, 2x2 grid collage, multi-angle scene reference, no people, no characters
```

四格内容依次为：
- **左上——全景定场（Establishing Shot）**：展示宏大的荒原整体地貌、地平线与整体据点形态。
- **右上——陈设特写（Props & Close-up）**：展示废旧钢铁、铆钉、锈蚀铁刺或拼凑机械等标志性细节。
- **左下——纵深透视（Depth & Perspective）**：展示据点廊道、重叠废墟等具有强烈透视和纵深空间的布局。
- **右下——气氛光效（Atmospheric Lighting）**：展示青橙对比、沙尘弥漫或逆光剪影等强烈的情感与色彩基调。依据分镜背景灵活调整（如硬日光、沙暴、钴蓝夜景或室内蒸汽光），而非固定黄昏。

## 4. 战车设定图提示词

生成展现狂暴机械、火焰喷射和生锈铆钉的重型战车参考大样。

按载具用途选择核心词库：

### 重载/开路型（如重装卡车）
强调高耸体量与庞大轮廓：
```
colossal vertical triangle front silhouette, towering high-clearance heavy chassis, massive armor-plated war rig cab, heavy industrial scrap-metal welding, giant multi-axle knobby tire tread setup, massive steel bumpers, heavily caked in rust and soot
```

### 中型/追击型（如肌肉车/中型越野）
强调宽扁低趴与速度轮廓：
```
wide low-slung wedge-shaped front silhouette, medium-sized rugged armored muscle car body, exposed custom front-bumper steel bull bar, wide off-road sport wheels and massive rubber tires
```

### 轻型/侦察型
强调低矮长条与敏捷轮廓：
```
low and narrow elongated silhouette, lightweight stripped-down chassis, minimal armor plating, exposed roll cage, knobby off-road motorcycle tires
```

每辆车仅保留 2-3 个核心识别特征进行高辨识度分流。严禁千车一面地均等堆砌钢刺、排气管或骷髅装饰。

## 5. 一致性微调控制

后续衍生图像制作（如更换场景、变更微小姿态）统一采用以图生图路径，以前序确立且锁定的风格化元素图像（无论是用户直接提供还是系统风格重绘/生成的版本，含四宫格场景图）作为主参考源，保持核心视觉特征与细节完全对齐。

## 6. 参考图资产校验规范

### 角色全身三视图合规校验
评估用户上传的角色参考图是否为标准的、无遮挡的直立全身三视图：
- 正面、侧面、背面均必须是全身立姿。
- 若为半身照、缺少任一核心角度、或存在遮挡，均判定为不合规。提取其服装风格、配色及五官特征，输出"需重绘为包含正面、侧面、背面全身直立角度的三视图"的重塑指引。
- 若完全合规，评估其是否包含废土朋克视觉特质，提炼特征输出。

### 场景参考图合规校验
评估用户上传的场景参考图是否为无人物、多角度、且以 2x2 四宫格形式排版的拼图：
- 若图像中出现人物、非废土风格的未来霓虹、或仅为单一视角的宽幅图片，均判定为格式不合规。
- 检查四宫格拼图的四个象限是否对齐标准内容分配（全景定场/陈设特写/纵深透视/气氛光效）。
- 若格式与风格合规，提炼结构比例、废土材质特征与光影质感。若不合规，评估原图中的可用轮廓与据点大体布局，输出"需重塑为标准无人物废土四宫格"的重绘指引。

### 参考视频与动态资产解析
当用户上传参考视频片段时，深度提取：
- 主体运动轨迹
- 平均切镜频率（节奏）
- 镜头运动模式（如快速横移、颠簸晃动、急推等）
- 色彩饱和度、光影青橙比
- 特定物理特征（如漫天飞砂密度、车尾拉烟浓度等）

将其转化为高密度的文字特征信号，用于精化动态故事板设计和视频运动提示词微调。
