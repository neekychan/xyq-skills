# 视频生成提示词文法

> 可适配的模式与句式，按场景改写，不要逐字照搬。

## 目录
1. 语系优先与主导风格写作规范
2. 场景四宫格防分屏融合指令
3. 五行特效画风质感标签
4. 不同场景色彩比例提示词控制
5. 写意碎落粒子与焦墨烟尘高级渲染标签
6. 视频生成制式规范
7. 参考绑定与唇形同步机制

## 1. 语系优先与主导风格写作规范

当用户使用中文交互或系统加载中文 UI 时，提示词本体必须使用中文撰写，但关键艺术术语、风格标签、五行特效标签采取中英双语对照或括号标注（例如 traditional Chinese ink wash painting (水墨写意)）。涉及对白台词、旁白等配音文本时，严格遵循全局规格文档所规定的输出语言。

## 2. 场景四宫格防分屏融合指令

视频生成提示词中必须强行加入对四宫格参考图每个格具体分配内容的精准说明，作为视频生成引擎的参考输入，并配合防分屏/防拼贴指令强制融合四格特征为单一连续画面：

```
Reference: 4-grid scene design sheet. Grid 1 provides the panoramic establishing layout; Grid 2 provides furnishing close-up texture details; Grid 3 provides deep perspective depth lines; Grid 4 provides atmospheric lighting and color tone. DO NOT generate a split-screen or 4-panel layout. Fuse all four grids into a single continuous cinematic shot that incorporates the landscape, textures, depth, and lighting from the reference.
```

## 3. 五行特效画风质感标签

详见 `references/formats/image-prompt-grammar.md` 第 6 节"五行特效画风质感标签"。视频提示词中根据角色属性选择对应标签，爆发态追加标签须包含色彩配比百分比。

### 打斗招式具体呈现形式
- **金行**：招式伴随金属质感的锋刃、漫天洒金碎屑、亮白光轨，动作大开大合，展现无坚不摧的锋芒。
- **木行**：招式呈现为如狂草笔触的藤蔓缠绕、飞叶如刀、翠绿生机能量流，配合灵动敏捷的闪避与体术。
- **水行**：招式结合流体力学的水流、冰锥凝结与水墨晕染，水势与冰刃交替，攻守兼备，行云流水。
- **火行**：招式包裹着熊熊烈焰，火焰边缘带有明显的焦墨毛笔顿挫质感，火光爆发伴随爆裂、极速位移打击。
- **土行**：招式显现为崩裂的巨石、飞扬的沙尘、拔地而起的岩壁，岩石轮廓带有厚重的枯笔飞白线条。

## 4. 不同场景色彩比例提示词控制

### 意境空镜/文戏场景
```
35% refined fine-line gongbi ink wash painting, elegant delicate outlines (工笔细描), smooth wet-on-wet ink gradients, highly detailed characters and costumes with clean and neat lines.
40% extensive negative space (意境留白), ethereal misty clouds and soft smoke, blank paper texture, breathing space, high atmospheric depth.
25% classical Chinese landscape splashed colors (写意泼彩), subtle accents of pale azurite (淡石青), light malachite (淡石绿), and mineral pale gold (矿物淡金), soft low-contrast lighting, peaceful and quiet atmosphere.
```

### 常规对打/过渡场景
```
50% dark charcoal ink wash base, 50% vibrant mineral pigments, dynamic lighting with bright sunbeams breaking through heavy ink clouds, rich textures, stark light-dark contrast
```

### 决战/招式冲撞场景
```
70% explosive cinnabar red (朱砂) and rich gold splashed colors, 30% stark pitch-black heavy charcoal outlines (焦墨压阵), extreme high-contrast dramatic backlight, electric gold sparks, dynamic ink splatters, blinding white flash
```

## 5. 写意碎落粒子与焦墨烟尘高级渲染标签

详见 `references/formats/image-prompt-grammar.md` 第 7 节"写意碎落粒子与焦墨烟尘渲染标签"。核心原则：
- 严禁使用任何 CGI、魔法粒子或日漫光效词汇
- 粒子必须从物理介质的写意破碎感出发（矿物碎彩、金属碎屑、书法笔痕）
- 烟尘必须被赋予炭黑与枯笔摩擦的有机粗粝质感，严禁使用平滑的 3D 立体烟雾词汇

## 6. 视频生成制式规范

- 输出视频分辨率严格控制为 720p（适配 16:9 画幅）
- 单镜时长严格控制在 4s-12s 之间，严禁生成低于 4s 的视频镜头
- 时长严格读取故事板中该分镜设定的 duration 属性，严禁全量套用 5s 等默认时长
- 时长 ≤15s 的单镜视频用一次生成即可拿到完整片段；多镜成片需逐镜生成后通过后处理拼接

## 7. 参考绑定与唇形同步机制

### 角色一致性
生成单镜视频时，必须将对应的角色三视图作为参考输入，确保面部五官及笔触质感保持高度一致。

### 场景一致性（绝对防跳画铁律）
必须严密解析镜头对应的 scene_id，拉取该场景唯一绑定的四宫格参考图。若相邻镜头或全片指向同一场景 ID，必须绑定完全相同的场景参考资产，严禁动态重复生成不同批次的场景图。提示词中加入四宫格精准说明 + 防分屏融合指令（见第 2 节）。

### 声音与唇形高精度对齐
若该镜头中角色有台词对白，必须将该角色的声音凭证作为音频参考传入。提示词中的台词文本与声音特征通过声学-视觉特征交叉注意力机制驱动角色嘴唇、舌头、面部咬肌和下颌骨进行语音轮廓契合。生成的视频画面中，角色发音口型、吞吐节奏与声音凭证的音色频率必须达到完美同步。

### 跨镜连续性（可选）
若当前镜头与前一镜头在动作或空间上具有极强连续性，可将前一镜视频作为动态参考传入，保障画面过渡流畅性与色彩/笔触一致性。

## 落 prompt 前自检

- 提示词是否使用中文撰写，关键术语是否中英双语标注？
- 四宫格防分屏融合指令是否写入视频提示词？
- 五行特效标签是否与角色属性对应？爆发态是否含配比百分比？
- 色彩比例是否与场景类型正确匹配？
- 粒子是否使用物理介质描述而非 CGI 词汇？
- 烟尘是否使用焦墨/炭黑质感而非 3D 立体烟雾词汇？
- 视频分辨率是否为 720p？时长是否在 4s-12s？
- 角色三视图、场景四宫格、声音凭证是否全部绑定？
- 场景参考资产是否与 story_id 严格对应、未重复生成？
