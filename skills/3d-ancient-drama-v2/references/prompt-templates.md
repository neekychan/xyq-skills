# 提示词模板与撰写规范

## 目录
1. [全局提示词撰写原则](#全局提示词撰写原则)
2. [角色设定图提示词](#角色设定图提示词)
3. [场景四视图提示词](#场景四视图提示词)
4. [关键道具资产图提示词](#关键道具资产图提示词)
5. [同一角色多套妆造提示词](#同一角色多套妆造提示词)
6. [用户上传非3D资产图风格转化提示词](#用户上传非3d资产图风格转化提示词)
7. [内切镜时长估算](#内切镜时长估算)
8. [视频提示词撰写前空间校验](#视频提示词撰写前空间校验)
9. [单shot视频提示词](#单shot视频提示词)
10. [音频生成](#音频生成)

---

## 全局提示词撰写原则

### 风格关键词强制写入（所有提示词类型）
无论是视频提示词、角色图提示词、场景图提示词还是道具图提示词，都必须写入关键词组：

```
半写实3D国漫风格, stylized anime-doll beauty, youthful androgynous pretty face, narrow oval V-shaped face, soft jawline, slightly enlarged almond eyes, delicate straight nose, soft thin lips, smooth poreless porcelain skin, clean stylized skin shader, soft cinematic close-up lighting
```

不得用"按项目风格填写""与全片风格一致"等模糊措辞替代——必须逐字写入关键词，确保模型每次生成都落在统一的3D古风渲染风格上。

**例外（场景四视图提示词）：** 场景四视图设定图不渲染光影，将风格关键词组中的 `soft cinematic close-up lighting` 替换为 `flat even lighting, no shadows, no cast shadows, no dramatic light direction`——但色调关键词（bright and clear tone, medium-high lightness, low to medium saturation, fresh harmonious color palette）仍然适用于场景设定图，确保场景图的色彩明度与饱和度与视频画面保持同一基调。场景设定图仅不呈现方向性光源或阴影效果，色彩调性须与全局色调一致。

### 禁用真人摄影/解剖学词汇（强制）
角色外貌描述须使用3D角色造型语言（如sculpted、stylized、3D character face），禁止使用真人摄影/解剖学词汇（如weathered、deep-set、heavy brow ridge、prominent cheekbones、photographic、ultra-realistic等）——这些词汇在训练数据中几乎只与真人摄影关联，会将输出拉向写实方向。面部特征用3D雕塑化语言描述，如"sculpted jaw"、"stylized brow"、"3D rendered cheekbones"。

### 禁止抽象表述，全部具体化
提示词中不得出现"优美的""有氛围感的""戏剧性的"等抽象形容词，每一项描述都必须落到可被模型直接渲染的具体视觉元素——写明具体颜色、材质、光位、角度、距离、动作幅度、表情肌肉状态等。

示例：
- 不写"优雅的姿态"，而写"右手轻提裙摆至腰侧，左肩微向后展，下颌微抬15°"
- 不写"昏暗的光线"，而写"右侧高处窗光，暖黄色3200K，投射角约45°"

### 禁用比喻性/情绪化外观词（强制）
禁止使用中文中带有物理外观副作用的比喻性情绪词或成语——模型会将这些词中的颜色、损伤、形变描述**按字面渲染**，而非理解为情绪比喻。

| 禁用词 | 模型误渲染效果 | 正确替代写法 |
|---|---|---|
| 面目狰狞 | 添加伤疤、疤痕、面部扭曲 | 眉头猛然拧紧，鼻翼扩张，上唇掀起露出牙齿，下颌前突 |
| 面色惨白/面无血色/面如死灰 | 整张脸渲染为纯白/灰白色 | 瞳孔骤缩，嘴唇微张，面部肌肉僵硬（肤色由key_element图像锁定） |
| 血盆大口 | 渲染出带血的嘴部 | 嘴巴大张，露出牙齿 |
| 青面獠牙 | 绿色皮肤和尖牙 | 面色铁青（描述表情肌肉状态而非肤色） |
| 面如桃花/面若桃花 | 面部渲染为粉色/桃花色色块 | 脸颊微红（描述表情而非色块） |

替代写法核心原则：将情绪**拆解为面部肌肉层面的具体微表情**。肤色由key_element图像锁定，提示词不干预肤色。

### 仅描述物理可见内容（强制）
提示词只描述画面中实际可见的元素——可见的动作、表情、姿态、光影和空间关系。不要描述画面外的元素，不要向模型解释角色动机、内心活动或情感背景；只写镜头能拍到的物理事实，让模型通过可见的肢体语言和面部表情自行呈现情绪。

### 人物站位关系一致性（强制）
在为Storyboard shot、参考图片撰写提示词时，人物之间的相对站位关系（左右顺序、前后景层级、彼此距离）必须与该shot的空间锚点卡完全一致，不得在不同提示词中对同一场景的人物站位给出矛盾描述。同一场景内多个shot之间，若人物未发生位移，站位关系须逐字保持一致；若发生位移，须在提示词中明确写出从何处移动到何处。

### 空间关系描述方式（强制——镜头相对描述）
描述角色与场景的空间关系时，禁止使用"角色面向某物"的角色相对朝向写法（如"角色面向龙椅"），必须改为镜头相对描述——直接写从镜头视角看，角色背后/左侧/右侧可见什么背景元素，以及哪些关键场景元素位于画面外或景深处不可见。这样无需模型做空间推理，直接指定该渲染什么、不该渲染什么。

---

## 角色设定图提示词

使用文生图，分辨率2K，画幅默认16:9横版（如用户要求其它比例则以用户为准）。

```
角色：[角色名]，[年龄段]，[性别/体态]，[身份/职业]。
外貌：[脸型、五官、眉眼、鼻梁、唇形、发型、肤色、年龄感、核心气质、标志性识别点]。

风格：半写实3D国漫风格，stylized anime-doll beauty, youthful androgynous pretty face, narrow oval V-shaped face, soft jawline, slightly enlarged almond eyes, delicate straight nose, soft thin lips, smooth poreless porcelain skin, clean stylized skin shader, soft cinematic close-up lighting. 所有角色（含配角）的肤色必须统一为warm porcelain-white skin with soft golden undertone。

服装：[必须严格贴合中国古代/古风服饰体系——主角偏华丽精致、层次丰富：内搭、中衣、外袍、披帛、腰带等多层叠穿，面料写明（丝绸、织锦、纱罗、锦缎等），配以刺绣纹样与玉佩、金簪等饰物，体现身份品阶；配角可适当简化但风格统一。逐一列明：内搭、外袍、下装、鞋、首饰、关键道具、材质、颜色、纹样、新旧程度]。

表情与气质：[常用表情须具体到面部肌肉层面（如"眉尾微挑、唇角轻抿、眼底含笑但不达眼底"），标注情绪强度；标志性微表情（如习惯性抿唇/假笑时眼角不动等）作为跨镜识别锚点；情绪底色、人物状态]。3D渲染角色表情需要比真人更鲜明、更具戏剧张力的描述。

画面排列：左侧1/3区域为超大高清面部特写，右侧2/3区域整齐排布角色三张全身三视图，包含角色的正面、侧面及背面三个维度的全身站姿视图。纯白背景，干净极简，无阴影，高清，精致细节；角色长相和服装细节一致。

背景：白色背景，柔和均匀灯光，无场景道具，无复杂背景。

限制：必须是同一个角色；脸型、发型、服装、鞋子、配饰完全一致；不要生成多个不同人物；不要换装；不要改变发色；不要随机文字；不要水印；不要logo。
```

---

## 场景四视图提示词

使用文生图，分辨率2K。

```
A location reference sheet of [场景描述，含空间结构/材质/标志物/纹样工艺细节].

Lighting: Flat, even, shadowless illumination—uniform ambient light only, no cast shadows, no dramatic light sources, no directional light, no ambient occlusion shadows, no light rays or god rays. The scene reference sheet should read like a clean 半写实3D国漫风格, 3D model viewport render with flat ambient lighting, not a cinematically lit shot.

Show four directional views of the same location in one composite image (2×2 grid). Each view is a full spatial angle—no isolated prop close-ups. Key furnishings and fixed landmarks naturally appear within whichever angle they are visible from:
Top-left: View from end A looking toward end B (forward depth—what is visible looking into the space from one end)
Top-right: View from end B looking toward end A (reverse depth—what is visible looking back from the opposite end)
Bottom-left: Left-side lateral view (camera positioned at the left side of the space, looking across horizontally)
Bottom-right: Right-side lateral view (camera positioned at the right side of the space, looking across horizontally)

Identical flat even lighting (no shadows, no dramatic light direction), color palette, and props across all four panels.

[Style]: Richly detailed ancient Chinese interior/exterior environment—carved wooden furniture with intricate grain patterns, painted beams with traditional motifs (cloud dragons, floral scrolls, geometric fretwork), lattice windows with openwork designs, inlaid mother-of-pearl surfaces, silk curtains with embroidered borders, bronze incense burners, jade ornaments. Color palette follows classical Chinese aesthetics—warm wood tones, muted indigo, elegant ochre, subtle moon-white, harmonious and layered.

[人群条件]：若为群像场景（上朝、集市、宴会等），将末尾的 "No people in frame." 替换为以下人群描述：
Populate the scene with background crowd NPCs in period-appropriate ancient Chinese attire—[人群规模/服饰风格/站位分布/活动状态，如 "court officials standing in formal rows", "market vendors and pedestrians browsing and haggling"]. Crowd figures should be slightly lower in detail than the main environment, serving as atmospheric background without dominating the frame.
若为非群像场景则保留：No people in frame.

No text, no labels, no watermark, no cast shadows, no dramatic lighting.
```

---

## 关键道具资产图提示词

使用文生图，分辨率2K，纯白背景、干净极简、无阴影、高清；画幅默认16:9（如用户要求其它比例则以用户为准）。

```
[道具名]
尺寸：[具体尺寸]
材质：[具体材质]
颜色：[具体颜色]
新旧程度：[描述]
正反面：[如有差异需在同一张图中同时展示正反两面]
当前状态：[描述]

风格关键词：3D CGI rendering, ancient Chinese aesthetic, PBR materials, stylized 3D CGI

限制：只生成该道具本身，不要出现人物或场景；不要随机文字、水印、logo。
```

---

## 同一角色多套妆造提示词

使用图生图，将首套造型图作为参考图上传。

在前述角色图模板基础上做以下调整：
- **外貌字段**：与首套完全一致，不得修改脸型、五官、肤色、身高比例、核心识别特征——这些由垫图保证，提示词中重复写明以强化锁定。
- **服装字段**：替换为本套造型的具体服装/发型/妆容/配饰描述，同样遵循古风服饰体系与主角华丽精致要求。
- **画面排列、背景、风格**：与首套保持一致，确保输出格式统一。
- 在提示词中显式注明：`Reference image: <<<image_1>>> is the same character's first look—keep identical face, facial features, skin tone, body proportions; only change costume/hairstyle/makeup/accessories.`

---

## 用户上传非3D资产图风格转化提示词

使用图生图，以原图为参考图。

- 提取原图中的角色身份特征（脸型、五官、发型、肤色、服装款式、配饰等），在提示词中逐项写明，要求转化后保持一致。
- 注入3D古风风格关键词：`半写实3D国漫风格, stylized anime-doll beauty, youthful androgynous pretty face, narrow oval V-shaped face, soft jawline, slightly enlarged almond eyes, delicate straight nose, soft thin lips, smooth poreless porcelain skin, clean stylized skin shader, soft cinematic close-up lighting`
- 在提示词中显式注明：`Reference image: <<<image_1>>> is the same character/scene/prop—keep identical identity features (face shape, facial features, hairstyle, costume structure, proportions); only convert the rendering style to 3D ancient Chinese CGI. Do not alter the character's identity.`
- 服装/道具若含现代元素，在转化提示词中一并替换为符合古风世界观的对应物品。
- 限制：保持原图角色身份不变；不要改变脸型/五官/肤色/身高比例；不要随机文字、水印、logo。

---

## 内切镜时长估算

若Storyboard shot未标注各内切镜时长，按以下经验值估算，确保单shot合计 ≤ 15s且 ≥ 10s：

| 镜头类型 | 建议时长 |
|---|---|
| 大特写/手部脚部特写 | 2–3.5s |
| 面部特写（含台词） | 3–5s |
| 近景胸像（含台词） | 3.5–5s |
| 中景/中全景 | 4–6s |
| 运镜推进/拉远/环绕 | 基础景别时长 +1s |
| 台词落点后停留 | +1s（强制，每句台词末尾须留余韵） |
| 动作落点后停留 | +1s（强制，每个主要动作完成后须保持收势姿态停留） |

**台词时长估算（强制）：** 每句台词须按字数估算说话时长（中文约2.5字/秒——古风戏剧化念白带情绪停顿与气息，实际语速低于日常对话，不得用3字/秒的高估值），加上台词落点后1s停留，作为该台词对应内切镜的最低时长。若台词+停留时间超过该景别建议时长上限，以台词+停留时间为准。

**动作完成度校验（强制）：** 每个内切镜的时长须覆盖该镜内所有动作的完整起势→执行→收势过程**加上动作落点后1s停留**——若动作链条+停留需要5s但景别建议时长只有3s，以动作完成+停留所需时长为准，不得压缩动作使其仓促。

超过15s必须拆分为独立shot。

---

## 视频提示词撰写前空间校验

撰写每个shot的视频提示词前，执行一次空间校验：

1. 对照该shot的空间锚点卡，逐角色确认提示词中描述的背景元素是否正确——根据空间锚点卡中角色的镜头相对背景描述，确认每个角色背后/左侧/右侧可见的背景元素在提示词中描述正确。
2. 确认画面外不可见的场景元素已在提示词中排除，未被误写为可见。
3. 确认提示词与空间锚点卡的空间描述完全一致。

### 参考帧分工说明
空间一致性参考帧已通过四层过滤（背景内容匹配→角色过滤→方向过滤→景别兼容性）选出，本阶段不重复执行选帧过滤，仅做提示词写作层面的一致性校验：背景匹配确认、景别兼容性确认、背景元素逐项对照。

### 参考帧背景内容匹配校验（从第二个shot起强制）
若本shot纳入了从任意前序shot中挑选的空间一致性参考帧，须执行以下校验序列（任一步不通过则排除该参考帧）：

1. **背景内容匹配检查（强制·第一优先级）：** 检查该帧在截帧时生成的视觉内容分析标签中的"可见背景元素清单"，将其与当前shot空间锚点卡中各角色背后/左侧/右侧可见背景元素逐项比对。若帧的背景元素与空间锚点卡不一致，该参考帧必须排除。若帧没有视觉内容分析标签，须先补做视觉内容分析再比对。
2. **景别兼容性检查：** 确认参考帧景别在本shot最宽内切镜景别对应的兼容区间内。
3. **背景元素逐项对照：** 通过前两步后，确认提示词中描述的每个可见背景元素在参考帧中确实可见且一致。若参考帧中拍到了某背景元素但提示词未提及，须补入；若提示词描述了某背景元素但参考帧中看不到，须回溯修正空间锚点卡和提示词。

校验通过后，在提示词 [空间] 段中以 `<<<image_reference_frame>>>` 占位符显式引用参考帧，并写明 `background elements must match reference frame <<<image_reference_frame>>>—[列出需保持一致的具体背景元素]`。

若校验发现不一致，须先修正提示词中的场景元素描述（或回溯修正shot描述/空间锚点卡），修正后再进入视频生成，不得带错生成。

### 重新生成时的提示词锁定（强制）
须复用上次已确认的视频提示词原稿，仅改用户指定部分。

---

## 单shot视频提示词

使用视频生成，分辨率720p，时长 ≤ 15s。

**失败处理（强制）：** 若视频生成失败，可尝试重新生成；若多次失败，停止任务并向用户说明，不得擅自切换到其他工具路径。

每个shot输出一段提示词，影像风格行作为整体基调先行，其后严格按 **摄影机→主体→空间→音频** 四段顺序撰写：

### [影像风格]
```
半写实3D国漫风格, stylized 3D CGI rendering, ancient Chinese aesthetic,
bright and clear tone, medium-high lightness, soft global illumination, soft shadows with preserved detail in dark areas, no harsh light rays, no god rays, silk painting color palette, low to medium saturation, fresh harmonious color palette, stylized depth of field, 24fps.
```

### [摄影机]
按内切镜顺序逐镜写明：景别 + 机位角度 + 运镜方式 + 切镜变化。多镜时每镜换行；同一shot内各镜景别/机位/运镜须有变化，避免重复堆叠。

**固定镜头时长上限（强制）：** 任何标注为fixed/lock-off的内切镜不得超过4s——超过4s必须改为带运镜的镜头或拆成多个有切镜变化的短镜。对话场景禁止长段固定机位。

**台词-镜头动势联动（强制）：** 每句台词对应的内切镜描述中必须包含至少一个镜头动势词——运镜变化（push-in/pull-out/orbit/pan/tilt/crane/dolly/whip-pan等）、景别切换（cut to close-up/cut to extreme close-up/cut to reaction/cut to detail/cut to over-shoulder等）或机位变化（switch to low angle/switch to side profile等）。禁止 "static camera, character speaks" 式的零动势描述；同一shot内多句台词的动势词须有变化。

**示例1（单镜，≤4s固定）:**
```
Medium waist shot, fixed camera, eye-level, 3s
```

**示例2（多镜含反应镜头与细节特写）:**
```
1. Medium two-shot, slow dolly-in, eye-level—A and B facing each other
2. Close-up on A, slow push-in—A delivers line with suppressed fury
3. Close-up on B, fixed, 2s—B's reaction: eyes widen, jaw tightens (reaction shot)
4. Extreme close-up on A's eyes, rapid push-in—A speaks key line, eyes narrow with cold rage
5. Extreme close-up on A's clenched fist, fixed, 2s—knuckles white, veins bulging (detail cutaway)
6. Close-up on A, push-in tighter—A continues, voice drops
```

**示例3（含过肩镜头）:**
```
1. Medium two-shot, eye-level—A and B facing each other across the desk
2. Over Character B's shoulder, looking at Character A, slow push-in—A speaks with suppressed fury (foreground: B's shoulder/back silhouette; background: A's face)
3. Over Character A's shoulder, looking at Character B, fixed, 3s—B's reaction: lips press tight, gaze drops (foreground: A's shoulder; background: B's face)
```

**过肩镜头写法（强制）：** 过肩镜头必须同时点名两个不同角色——写明 `over [前景角色]'s shoulder, looking at [背景角色]`，前景角色只有肩/背出现在画面前景，背景角色是画面主体。禁止将同一角色同时写在前景和背景。

**反应镜头写法：** 对话段落中，在说话者的镜头之间插入听者反应特写，用 `reaction shot` 标注并写明听者面部微表情；切回说话者时可收紧景别强化情绪。

**重点台词推进写法：** 关键台词处用 `rapid push-in to extreme close-up` 或 `slow push-in from close-up to extreme close-up on eyes/lips` 标注推进路径，速度词与情绪强度匹配。

**身体部位细节特写写法：** 需要非面部细节特写时，用 `extreme close-up on [身体部位] (detail cutaway)` 标注，紧跟情绪词描述局部状态，与面部镜头交替出现，同一shot内不超过两个细节特写。

**对话镜头动势池（强制泛化）：** 对话段落中镜头不得停留在单一景别+固定机位上，须主动从以下动势池中选取组合：
- **运镜类**：slow push-in / rapid push-in / pull-out / orbit / arc shot / whip-pan / dolly / tracking / crane up-down / tilt / pan
- **景别切换类**：cut to extreme close-up on eyes/lips/brow / cut to close-up on hands/fist/fingers / cut to over-shoulder / cut to two-shot / cut to medium-full（禁止拉至全景/大全景）
- **反应与细节类**：cut to reaction shot / cut to detail cutaway / cut to insert
- **机位变化类**：switch to low angle / switch to high angle / switch to side profile

组合原则：同一对话段落内连续的内切镜应交替使用不同类别的动势（如push-in→reaction→detail cutaway→orbit），避免连续多镜都属同一类别。

### [主体]
```
<<<image_角色>>>—[当前服装/状态，与设定图一致]；[人物动作分解，按叙事顺序推进，主要动作→次要动作]
```

每个关键节拍须附带具体面部微表情描述（如 `brows snap together, jaw tightens, eyes narrow with suppressed fury`），标注情绪强度词；3D CGI角色情绪需比真人更夸张才能被模型呈现。

**每句台词必须搭配一个明确的肢体动作**（gesture/body shift/head turn/gaze shift），动作与台词情绪合理匹配，禁止static standing dialogue。

**动作幅度词库（强制）：** 每个关键动作必须附带一个标准化幅度词，从以下词库选取：`large / sweeping / sharp / explosive / sudden / violent / forceful / dramatic / swift / wide`。示例：`sweeps sleeve wide`, `snaps head around`, `stumbles half a step back`, `slams fist onto the table`。**禁止**使用 subtle/slight/gentle/mild/soft/faint 等弱幅度词描述主要动作。

**情绪-动作联动（强制）：** 动作幅度必须与情绪强度挂钩——高情绪强度必须配大幅度肢体动作，用 large/explosive/violent/sudden 等词描述；低情绪强度才允许小幅度动作，用 measured/restrained 等词描述。禁止出现"情绪激烈但身体不动"的割裂写法。

**情绪动态与放大（强制）：** 每个shot须有明确的情绪起伏，关键节拍处情绪强度必须显式升级（如 suppressed anger→explosive fury, calm composure→visible shock），标注情绪变化路径。

**眼神互动（强制）：** 每句台词至少附带一个具体的眼神动作描述（gaze locked on / eyes dart to / avoids eye contact / glares at / glances sideways at / looks up to meet / drops gaze 等），眼神方向与目标须明确写出；对话场景中须设计角色间的眼神互动。禁止空洞注视或无指向目光。

避免写绝对秒数，用 slow/quick/lingering 描述节奏。

**台词落点后须描述至少1s的情绪延续动作**（如 `holds gaze, expression lingers, slight exhale`），禁止台词说完即切。

**动作落点后停留（强制）：** 每个主要动作完成后须描述至少1s的姿态延续与余势（如 `holds final pose, body lingers, slight exhale before next movement`），禁止动作刚做完即切。

**动作完整性（强制）：** 每个动作节拍须写明完整的起势→执行→收势三段，不得只写"角色A转身"而省略转身的过程。

**武打shot动作描写：** 按Storyboard武打设计的四段式结构（起手→接触→命中→结果）逐段写明动作分解；打击动作用 sharp/explosive/impact 等力度词描述，命中处可标注 slow-motion（仅决胜一击）；闪避、格挡、落空、反制动作须与命中动作交替出现，不得全部命中；镜头晃动仅标注在命中瞬间。

**动作完整链条（强制）：** 每个交手节拍必须写清六要素——①谁先动→②谁防守→③接触点→④交锋结果→⑤受力结果→⑥段末状态。禁止用"二人激烈打斗"等笼统概括。

### [空间]
```
<<<image_场景>>>—[逐字继承该场景element scene的固定光影基调（光源 + 色温 + 氛围词），不得自行改写或换措辞]；[镜头相对空间描述：从镜头视角写明画内可见的背景元素、各角色相对位置，以及哪些关键场景元素位于画面外或景深处不可见]
```

**参考帧引用（从第二个shot起强制）：** 若本shot纳入了空间一致性参考帧，须在空间段末尾追加：
```
<<<image_reference_frame>>>—Reference frame from a prior shot. IMPORTANT: This reference frame is for background layout and scene backdrop consistency ONLY. The camera angle, shot scale, framing, perspective, and camera movement described in the [摄影机] section above MUST take full precedence—do NOT replicate, copy, or imitate the reference frame's camera perspective, shot composition, lens height, or framing. The reference frame defines what background elements exist and where they are positioned in the scene; it does NOT define how the camera shoots them. Background elements and spatial layout behind/left/right of each character MUST match this frame. Specifically: [逐元素列出需保持一致的背景元素]. Do not change or relocate these background elements; the scene backdrop must remain identical to the reference frame. However, the camera angle, shot scale, framing, and composition must follow the [摄影机] section instructions exclusively.
```

### [音频]
```
[台词] [角色]: {台词原文} (with [情绪词] tone)
[内心OS] [角色]: {(OS)OS原文} (with [情绪词] tone, no lip movement—inner voice only, character's mouth stays closed; facial expression must shift in sync with OS emotional arc—write specific micro-expression beats in [主体] section)
[音效] <音效描述，紧贴对应动作>
无音乐——BGM在audio_layer独立生成、后期混音，视频生成时须内嵌no background music
```

### [禁止]
```
No subtitles, no background music, no text overlay, no watermark, no modern elements (modern clothing, electronic devices, plastic, modern architecture, etc.)—strictly ancient Chinese setting.
```

### [时长]
```
Approximately [X]s
```

### 固定尾部规则

- 所有视频提示词末尾必须包含 No subtitles, no background music, no text overlay, no modern elements——BGM在audio_layer独立生成，后期混音；台词/音效/内心OS可内嵌。
- 使用内嵌格式：音乐 (...)、音效 <...>、台词 {...}、内心OS {(OS)...}（括号内只写原文，不加情绪标注）、片内字幕 【...】。角色名写在花括号外，格式为 `[角色]: {台词原文}`、`[角色]: {(OS)OS原文}`。
- 内心OS须标注 `(OS)` 前缀以区分开口台词，并在对应内切镜的[主体]描述中注明角色嘴唇不动（no lip movement, mouth stays closed），同时为OS时段设计具体的面部表情变化路径。
- 不依赖绝对时间戳（如 "0–3s"）描述动作节奏，改用速度形容词。

---

## 音频生成

### BGM
使用音乐生成，按audio_layer中的BGM设计生成。视频生成时视频本身不内嵌BGM，BGM在audio_layer独立生成后于组装阶段混音。

### 第三人称旁白（VO）
使用语音合成，按narration_speaker_profile生成。

### 角色内心OS
内心OS不作为独立旁白轨单独生成——须内嵌在视频生成中（写入视频提示词 [音频] 段，与台词同级），通过该角色的key_element_audio绑定保持音色一致。OS时间计入shot总时长，按说话时长估算。OS期间角色嘴唇不动，须为OS时段设计具体的面部表情变化路径并写入视频提示词主体段。

### 角色台词与内心OS音色一致性
视频生成时通过character的key_element_audio绑定保持台词与内心OS跨镜音色一致。
