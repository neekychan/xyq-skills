---
name: fpv
display_name: 穿越飞行
description: 根据用户上传的参考图片或视频，生成 FPV 穿越飞行风格视频。自动识别主体类型、空间结构与障碍物，规划可物理成立的飞行轨迹，生成主体连续、穿越合理、环境有动态反馈的 FPV 视频。触发场景：用户提及 FPV、穿越飞行、第一人称飞行、无人机穿越、flythrough、无人机视角、飞鸟视角、车辆追飞，或上传图片/视频并要求生成飞行穿越效果的视频时使用。支持低空贴地、高空俯冲、螺旋环绕、急速穿梭、飞鸟掠过、车辆追飞等预设，单段 ≤15s 一次生成，超时可拆分拼接。
tools: ["render_video", "sandbox_generate_video", "sandbox_process_video"]
---

# 穿越飞行

## 1. 核心原则

FPV 视频的本质是“穿越空间叙事”。镜头必须沿着可物理成立的路径穿过空间，让观众感知前景、中景、远景之间的视差、遮挡、速度和高度变化。

持久引擎：

**参考素材 → 主体识别 → 空间占用图 → 动态物理层 → 风格预设 → 可飞行轨迹 → 分镜序列 → 主体连续性约束 → FPV 视频**

各环节因果关系：

- 主体识别决定默认风格、镜头距离、追踪对象和不能丢失的视觉锚点。
- 空间占用图标记可穿越结构、不可穿越障碍、遮挡物和安全飞行通道。
- 动态物理层规定每一个主动运动 beat 都必须绑定可见的环境响应 beat，镜头不能只自己动、环境不动。
- 风格预设决定速度、角速度、高度变化、镜头倾斜和节奏。
- 可飞行轨迹把风格映射为不会穿模、不会撞击主体的连续路径。
- 分镜序列将路径拆解为时间轴 beat，同一段 ≤15s 可一次生成。
- 主体连续性约束保证人物、车辆、动物、建筑核心形态在时序上不丢失、不变形、不凭空出现。

## 2. 质量测试

飞行轨迹必须穿越多个空间层次，且穿越动作、视差变化、环境反馈和主体连续性同时成立。画面要有高级大片质感、明确速度张力和真实空间阻力。

可证伪判据：

- 如果去掉飞行穿越动作后，画面只剩匀速平移，创意不成立。
- 如果镜头路径穿过树干、人体、车辆、墙体、柱子等不可穿越物，创意不成立。
- 如果高速低空掠过草地、水面、尘土、树叶、人群边缘，但环境完全静止，创意不成立。
- 如果主动运动只发生在镜头本身，而周围可受影响物体没有同步产生可见变化，创意不成立。
- 如果飞鸟穿越草丛时，草叶只是静态背景，没有被镜头气流拨开、压弯、扫过镜头边缘并回弹，创意不成立。
- 如果车辆、人物、动物等关键主体中途消失、数量变化、外观突变，创意不成立。

具体检验点：

- 至少穿越 1 个可穿越结构，例如门洞、拱桥、建筑缝隙、树丛间隙、峡谷缝隙、车辆之间的安全空隙。
- 穿越前后必须存在高度变化或方向变化。
- 近景与远景之间的视差清晰，近景运动更快，远景运动更慢。
- 草丛、稻田、麦田场景中，前 3 秒必须出现近景草叶的主动运动，例如向两侧分开、被压低、形成波浪、擦过镜头边缘、镜头过后回弹。
- 每个主动运动 beat 必须至少绑定 1 个环境响应：俯冲带起气流，贴地卷起尘土，掠水产生涟漪，穿廊带动窗帘或纸张，追车带出轮胎运动和路面尘雾。
- 节奏有加速、减速或停顿蓄力，不是全程匀速。
- 不可穿越物必须被绕开、掠过、从旁边擦过或被自然遮挡，不能直接穿透。
- 关键主体全程保持可追踪状态；如被遮挡，必须在合理时间内从遮挡后重新出现。

## 3. 输入诊断

生成前必须识别或合理假设以下维度：

- 参考素材类型：单张图片、多张图片、参考视频、图片+视频组合。
- 主体类型：人物、建筑、风景、车辆、室内空间、自然隧道、飞鸟/动物视角、混合主体。
- 核心主体：画面中必须保持连续的主体，例如一辆红色跑车、一个穿白衣的人、一栋塔楼、一只飞鸟。
- 主体数量：车辆、人物、动物等可数对象必须登记数量，生成中不得凭空增减。
- 空间纵深：前景、中景、远景层次，以及可穿越结构。
- 空间占用图：不可穿越物、可穿越间隙、近景遮挡物、危险穿模区域。
- 动态物理层：草、树叶、尘土、水面、衣物、头发、旗帜、车灯、烟雾等会对气流或高速运动产生反馈的元素。
- 光源方向：顺光、逆光、侧光、顶光，用于规划飞行方向和遮挡后的曝光变化。
- 风格预设：低空贴地、高空俯冲、螺旋环绕、急速穿梭、飞鸟掠过、车辆追飞、未指定自动匹配。
- 难度档位：简单、标准、高难度，未指定默认标准。
- 画幅比例：16:9 横屏或 9:16 竖屏。
- 目标时长：≤15s 一次生成，>15s 拆分后拼接。
- 目标平台：抖音、TikTok、Reels、YouTube、其他。
- 运镜速度偏好：慢速沉浸、中速叙事、高速刺激。
- 光线时段：日出、白天、黄昏、夜晚。
- 素材间冲突：多张图的主体、光线、时段、数量冲突时，暂停询问用户以哪张为准。

## 4. 物理与连续性硬规则

这些规则优先级高于风格表现。任何分镜或 prompt 不能为了刺激感牺牲物理合理性。

### 4.1 空间占用图规则

生成分镜前，必须把画面元素分成三类：

| 类型 | 定义 | 运镜处理 |
|---|---|---|
| 可穿越结构 | 门洞、拱桥、树枝间隙、峡谷缝、车辆间安全空隙 | 可以穿越，但要留出安全边距 |
| 不可穿越障碍 | 人体、树干、墙体、柱子、车辆实体、山体、家具实体 | 只能绕开、掠过、抬升越过或侧飞避开 |
| 动态反馈物 | 稻草、草叶、树叶、水面、尘土、衣物、烟雾 | 镜头高速靠近时必须被风压、尾流或运动扰动影响 |

若素材中没有可穿越结构，不能硬造穿模路径。应改为“掠过、绕行、拉升、俯冲、贴近遮挡物边缘飞过”的路线。

### 4.2 避障与防穿模规则

- 镜头不得穿过人体、树干、墙面、车身、柱子、家具、动物身体。
- 高速穿越必须发生在“明确空隙”中，例如两棵树之间、车与车之间、门洞中央、拱桥下方。
- 近距离擦过障碍物时，要描述“沿边缘掠过”“侧向避开”“贴着外侧飞过”“从上方越过”，避免“穿过树、人、车身”。
- 遮挡物可以短暂挡住主体，但遮挡前后主体的位置、方向和速度要连续。
- 当人物站在树旁或车旁时，路径必须从人物外侧或树枝间隙绕过，不能从人物和树干实体中穿过。

### 4.3 动态环境反应规则

低空、高速、贴近物体飞行时，环境不能静止。草丛、稻田、麦田、灌木不是背景装饰，而是必须参与运动的前景动作层。根据场景添加合理反馈：

| 场景 | 必须加入的动态反馈 |
|---|---|
| 稻田、草地、麦田 | 前景草叶被镜头气流向两侧拨开，草尖压低成波浪，近景草叶擦过镜头边缘，镜头飞过后草叶回弹 |
| 高草丛穿越 | 镜头从草缝中钻入，草叶先遮挡画面两侧，再被气流分开；叶片有明显弯曲、抖动、回弹，不得保持静止 |
| 树林、灌木 | 近景叶片被气流推开并抖动，枝叶掠过镜头边缘，树干被避开 |
| 沙地、土路 | 尘土被卷起，近地面有颗粒拖尾 |
| 水面、溪流 | 水面产生涟漪或反光拉伸，低空掠过时水花轻微扰动 |
| 人物近景 | 头发、衣角、裙摆或周围轻物体轻微摆动，人物实体不能被穿过 |
| 车辆追飞 | 车灯、反光、轮胎运动、路面光影和车身相对位置保持连续 |

草丛、稻田、麦田场景的 prompt 必须把“草叶运动”写成镜头时间轴上的动作，而不是只写成画面质感。推荐句式：

- “0-3s：镜头贴着草尖钻入，高草叶先遮住画面两侧，随后被气流向外拨开。”
- “3-7s：前景草叶连续压弯成波浪，叶尖快速擦过镜头边缘，远处背景慢速后移形成视差。”
- “7-10s：镜头拉升离开草丛，被压弯的草叶在身后回弹，尾流波纹向后扩散。”

禁止只写“grass moves slightly”“草叶轻微摆动”这类弱描述。应使用“拨开、压弯、扫过镜头、回弹、尾流波纹”等可见动作词。

### 4.4 主动运动与环境响应绑定

凡是分镜中出现主动运动，都必须绑定一个同步发生的环境响应。主动运动包括前飞、俯冲、拉升、侧飞、螺旋、急停、加速、贴地掠过、穿越空隙、追车、飞鸟掠过、室内穿门。环境响应必须写成可见动作，不能只写“真实物理”“有风感”“自然反馈”。

| 主动运动 | 必须绑定的环境响应 |
|---|---|
| 低空前飞 | 近景草叶、树叶、尘土、衣物或水面产生方向一致的尾流变化 |
| 高速贴地 | 地面尘土、碎叶、草尖或水面反光被拉出运动轨迹 |
| 俯冲 | 前景物体快速放大，草叶或树叶向镜头两侧分开，尘土或水面出现压迫感 |
| 拉升 | 被压弯或扰动的近景物体在镜头后方回弹，远景逐渐展开 |
| 侧飞擦边 | 障碍物边缘的叶片、布料、纸张或尘雾沿镜头运动方向扫过画面边缘 |
| 螺旋环绕 | 主体周围的衣物、头发、叶片、烟雾或光影出现环向变化 |
| 急速穿门穿廊 | 门帘、窗帘、纸张、灰尘、灯影随气流或速度变化晃动 |
| 车辆追飞 | 轮胎持续转动，车身反光连续变化，路面尘雾、落叶或水花被车辆和镜头共同带动 |
| 飞鸟穿草丛 | 草叶遮挡镜头边缘、被气流拨开、压弯成波浪、扫过镜头、离开后回弹 |

每个分镜 beat 必须写成“镜头动作 → 环境响应”的结构。例如：“0-3s：镜头贴地前飞 → 草尖向两侧倒伏，尘土沿镜头后方拖出尾流”。如果某个 beat 没有可见环境响应，应降低镜头速度、改变飞行高度，或补充可响应物体；不能让镜头单独运动。

### 4.5 主体追踪锁规则

对人物、车辆、动物等主体建立 identity lock：

- 记录主体数量、颜色、外观、运动方向、相对位置。
- 同一段视频内主体不得消失、变形、换色、换车、凭空增加或减少。
- 多车场景必须标注“所有车辆持续存在，短暂遮挡后重新出现，数量保持不变”。
- 追车镜头中，主车始终是视觉锚点，除非分镜明确设计为“短暂遮挡 0.5-1s 后重现”。
- 遮挡后重现必须符合运动方向和速度，不得从错误位置跳出。

### 4.6 车辆连续性规则

车辆飞行是高风险场景，必须额外约束：

- 每辆车使用清晰标签描述，例如“红色主车”“黑色副车”“白色远处车”。
- 若镜头超车或侧飞，必须说明被超车辆继续在画面后方或侧后方可见。
- 若一辆车被桥柱、树影、前车短暂遮挡，必须说明遮挡后它沿原车道重现。
- 车辆数量在整段中保持一致，不能中途少一辆或多一辆。
- 镜头不得穿过车身，只能从车旁、车上方、车间空隙或车道外侧穿过。

### 4.7 飞鸟视角规则

当用户提到飞鸟飞行、鸟瞰穿越、飞鸟视角、鸟类主体或类似表达时，使用“飞鸟掠过”规则：

- 镜头可以模仿鸟类低空掠过、贴近草尖、上扬越树、俯冲穿林间空隙。
- 不表现僵硬无人机匀速移动，要有轻微自然起伏和翼感节奏。
- 贴近稻草、草地、树叶时，近景植物必须作为画面主动作出现：草叶先遮挡镜头边缘，再被气流拨开、压弯、扫过镜头边缘，并在镜头离开后回弹。
- 飞鸟穿越草丛时，prompt 的前半段必须先描述“草叶如何运动”，再描述远景和氛围；不能只在末尾追加“草随风摆动”。
- 若草叶运动不是视频中的可见动作，必须判定该片段失败并重生成。
- 镜头不能穿过树干、人物、动物身体；遇到树、人、房屋时必须侧向绕开或拉升越过。
- 若画面中有人物，人物保持实体存在，可被树叶或草丛短暂遮挡，但不能被镜头穿透。

## 5. 路由表

| 输入特征 | 选用路线 | 必读 reference |
|---|---|---|
| 人物主体 | 螺旋环绕为主，可搭配安全穿越 | references/trajectories/person.md |
| 建筑主体 | 高空俯冲为主，穿插穿门、穿拱、穿缝 | references/trajectories/building.md |
| 风景主体 | 低空贴地为主，沿地形起伏 | references/trajectories/landscape.md |
| 车辆主体 | 急速穿梭或车辆追飞，强制主体追踪锁 | references/trajectories/vehicle.md |
| 室内空间 | 穿门穿廊为主，走廊、房间、出口连续 | references/trajectories/interior.md |
| 自然隧道 | 窄缝穿越为主，贴壁贴树但不穿透实体 | references/trajectories/nature-tunnel.md |
| 飞鸟视角 | 飞鸟掠过，强调自然起伏、气流反馈、避开实体 | references/trajectories/bird-flight.md |
| 竖屏模式 | 竖屏运镜规则叠加 | references/formats/vertical-rules.md |
| 写最终视频 prompt | FPV 专用 prompt 文法 | references/formats/fpv-prompt-grammar.md |
| 画幅/平台适配 | 平台规则 | references/formats/platforms-markets.md |

只读匹配项，不全部加载。

## 6. 强制加载 reference

落 prompt 前，必须按路由结果加载对应 references，并把相关词汇、句式、约束写进实际产出。不得跳过，不得凭记忆生成。

必读：

1. `references/formats/fpv-prompt-grammar.md`

条件读取：

- 按主体类型读取 `references/trajectories/<类型>.md`。
- 飞鸟视角读取 `references/trajectories/bird-flight.md`；若不存在，则使用本文件 4.7 的飞鸟视角规则。
- 竖屏模式读取 `references/formats/vertical-rules.md`。
- 平台影响画幅或节奏时读取 `references/formats/platforms-markets.md`。

硬规则：

- 若最终输出包含视频生成 prompt，本回合必须已读过 `references/formats/fpv-prompt-grammar.md`。
- 若主体为车辆，prompt 必须包含“车辆数量保持一致、主车持续可追踪、短暂遮挡后按原方向重现”。
- 若主体为飞鸟视角、稻田、草地、草丛、麦田、树林，prompt 必须把“草叶/稻草/树叶的前景运动”写在时间轴前半段，并包含“遮挡镜头边缘、被气流拨开、压弯成波浪、擦过镜头、镜头离开后回弹”中的至少 3 个动作词。
- 每个主动运动 beat 必须写出“镜头动作 → 环境响应”的对应关系；如果找不到可响应物体，必须降低速度、改变高度或补充可响应环境元素。

## 7. 工作流

### 步骤 1：分析参考素材

1. 读取用户上传的参考图片或视频。
2. 识别主体类型和核心主体。
3. 登记主体数量、外观、颜色、位置和运动方向。
4. 分析空间纵深：前景、中景、远景层次，以及门洞、拱桥、建筑缝隙、峡谷、树丛、车间空隙等可穿越结构。
5. 建立空间占用图：标记可穿越结构、不可穿越障碍、动态反馈物和危险穿模区域。
6. 判断光源方向，用于规划飞行方向、曝光变化和遮挡后的明暗连续。
7. 多张图片时，判断主图、环境图、多角度参考；若光线、时段、主体数量冲突，暂停询问用户以哪张为准。
8. 参考视频时，提取运镜风格、速度节奏、高度变化和主体连续方式。
9. 图片+视频同时上传时，图片提供主体与环境外观锚点，视频提供运镜风格信号。

异常处理：

- 图片主体模糊无法识别：告知用户“请上传主体更清晰的图片”。
- 图片缺乏空间纵深：建议用户“更换含背景/环境的图片，或选择风景、建筑、室内、道路类场景”。
- 画面中障碍过密且无可穿越空隙：改为绕行、贴边掠过、拉升越过，不强行穿越。
- 多车辆数量无法确认：先询问用户需要追踪哪辆车，避免生成中车辆丢失。

### 步骤 2：风险诊断

在设计分镜前，先输出内部风险判断，随后把关键风险转化为 prompt 约束。

常见风险与修正：

| 风险 | 原因 | 修正方式 |
|---|---|---|
| 稻草、草叶、树叶不动 | prompt 把植物当背景，只写“轻微摆动”或写在末尾，模型优先生成镜头运动 | 把植物升级为前景运动层，写入 0-3s 时间轴：草叶遮挡镜头边缘、被气流拨开、压弯成波浪、扫过镜头、离开后回弹 |
| 镜头主动运动但环境不动 | 分镜只写了前飞、俯冲、拉升、穿越，没有给每个动作绑定环境响应 | 每个 beat 使用“镜头动作 → 环境响应”结构，例如“贴地加速 → 尘土被卷起并向后拖尾” |
| 人物穿树或穿人 | 未区分可穿越空隙和实体障碍 | 建立空间占用图，明确绕开树干、人物、车身 |
| 车辆中途消失 | 未登记车辆数量与 identity lock | 标注主车/副车，要求数量不变，遮挡后重现 |
| 遮挡后主体跳位 | 缺少运动连续描述 | 指定主体沿原方向、原车道或原路径重现 |
| FPV 变成平移 | 缺少高度、方向、速度变化 | 每段加入俯冲、拉升、侧飞、滚转或穿越点 |
| 穿越点不成立 | 场景缺少真实空隙 | 改为掠过边缘、绕柱、越树、沿缝隙外侧飞行 |

### 步骤 3：规划轨迹分镜

1. 根据主体类型读取对应轨迹规则。
2. 根据用户指定或自动匹配的风格预设确定运镜语言。
3. 根据难度档位调整轨迹复杂度。
4. 设计连续飞行路径，标注：
   - 起点、穿越点、转向点、终点。
   - 高度变化、方向变化、速度变化。
   - 可穿越结构与不可穿越障碍。
   - 主体追踪锁和遮挡后重现方式。
   - 前景运动层：草叶、稻草、树叶、尘土、水面等在每个时间段如何运动。
   - 主动运动绑定：每个镜头动作对应哪个环境响应。
5. 每段分镜不超过 15 秒。若总时长 ≤15s，分镜中的多个 beat 写入同一条 prompt 一次生成；不要拆成多次生成。
6. 若总时长 >15s，拆为若干 ≤15s 片段，并确保段间速度、方向、光线和主体位置连续。

风格自动匹配规则：

| 主体类型 | 默认风格 |
|---|---|
| 人物 | 螺旋环绕 |
| 建筑 | 高空俯冲 |
| 风景 | 低空贴地 |
| 车辆 | 车辆追飞 / 急速穿梭 |
| 室内空间 | 低空贴地 |
| 自然隧道 | 低空贴地 |
| 飞鸟视角 | 飞鸟掠过 |

竖屏模式检测：

若用户提及“竖屏”“抖音”“Reels”“TikTok”“9:16”“短视频平台”，或参考图高于宽，画幅锁定 9:16，并读取 `references/formats/vertical-rules.md`。未明确说明时默认 16:9 横屏。

### 步骤 4：暂停确认

分镜设计完成后，向用户展示飞行轨迹概要，等待用户确认或微调后再生成。

必须展示：

- 整体路径：起点 → 关键穿越点 → 终点。
- 高度变化：例如低空贴地 → 拉升越树 → 俯冲入门洞。
- 关键动作：穿门、绕柱、俯冲、拉升、侧飞、螺旋、擦边掠过。
- 速度节奏：何处加速，何处减速，何处短暂停顿。
- 光线方向：顺光、逆光、侧光，以及遮挡后的曝光变化。
- 物理避障：说明哪些实体会绕开，哪些结构会穿越。
- 前景运动层：草叶、稻草、尘土、水面、衣物、树叶等在 0-3s、3-7s、7s 之后分别如何运动。
- 主动运动绑定：每个关键动作对应的环境变化，例如俯冲对应草叶分开，贴地对应尘土拖尾，穿廊对应窗帘晃动。
- 主体连续性：车辆、人物或动物如何保持全程存在；遮挡后如何重现。
- 预计总时长与分段情况。

### 步骤 5：生成视频素材

1. 以参考图或视频为视觉基础，按确认后的分镜生成 FPV 视频。
2. 时长 ≤15s 的成片使用一次视频生成，分镜 beat 是同一条 prompt 内的时间轴。
3. 总时长 >15s 时，拆成若干 ≤15s 片段分别生成。
4. 每段 prompt 都必须包含：
   - FPV 第一人称镜头动作。
   - 空间结构与可穿越点。
   - 不可穿越障碍的绕行方式。
   - 前景运动层，且草丛、稻田、麦田场景必须放在 prompt 前半段描述。
   - 主动运动绑定，用“镜头动作 → 环境响应”的句式写入 prompt 时间轴。
   - 主体追踪锁。
   - 光线方向与电影质感。
5. 生成后检查关键主体是否消失、数量是否变化、是否穿模、环境是否静止；若任一主动运动 beat 没有对应环境响应，判定失败并重生成；若飞鸟穿草丛但草叶没有明显拨开、压弯、擦镜头或回弹，判定失败并重生成。

### 步骤 6：合成输出

1. 若分段生成，按轨迹顺序无缝拼接。
2. 段间要保持方向、速度、光线、主体位置和主体数量连续。
3. 若发现车辆消失、人物穿树、草叶静止、主体跳位，应优先重生成问题片段，而不是直接拼接。
4. 最终交付成片。

## 8. 输出契约

### 分镜输出格式

```markdown
【FPV 飞行轨迹方案】

主体类型：[人物/建筑/风景/车辆/室内空间/自然隧道/飞鸟视角]
核心主体：[必须连续保持的主体，如红色主车/白衣人物/塔楼/飞鸟视角]
主体数量：[人物/车辆/动物数量；不可数场景写无]
风格预设：[低空贴地/高空俯冲/螺旋环绕/急速穿梭/飞鸟掠过/车辆追飞]
难度档位：[简单/标准/高难度]
画幅：[16:9 / 9:16]
总时长：[Xs]

空间占用图：
- 可穿越结构：[门洞/树丛间隙/建筑缝隙/车间空隙等]
- 不可穿越障碍：[人物/树干/车身/墙体/柱子等]
- 前景运动层：[稻草/草叶/树叶/尘土/水面/衣物等，写清楚 0-3s、3-7s、7s 之后的运动]

连续性约束：
- 主体追踪锁：[主体外观、数量、方向、遮挡后重现规则]
- 避障规则：[哪些实体绕开、从哪侧通过、是否拉升越过]
- 主动运动绑定：[镜头动作 → 环境响应，例如贴地加速 → 草叶倒伏与尘土拖尾]

--- 分镜 1 (0-Xs) ---
高度：[起始高度 → 结束高度]
关键动作：[描述]
穿越结构：[有/无，具体描述]
避障方式：[绕开/越过/侧飞掠过/从空隙穿过]
前景运动层：[草叶遮挡镜头边缘、被气流拨开、压弯成波浪、擦过镜头、离开后回弹等]
主动运动绑定：[镜头动作 → 环境响应]
主体连续性：[主体保持可见或短暂遮挡后重现]
速度：[慢速/中速/高速/加速/减速]
光线：[顺光/逆光/侧光/顶光]
prompt: [FPV 专用 prompt]
```

### 视频 prompt 格式

按 `references/formats/fpv-prompt-grammar.md` 输出，并补足以下约束：

- 相机：FPV 第一人称视角，明确前飞、侧飞、拉升、俯冲、螺旋、穿越、绕行。
- 画面：空间结构、主体、环境、前景遮挡与远景纵深。
- 物理路径：明确穿过可穿越空隙，绕开树干、人物、车身、墙体等实体。
- 前景运动层：近景植物、尘土、水面、衣物等必须作为可见动作参与镜头时间轴；草丛、稻田、麦田场景中，先写草叶运动，再写远景和氛围。
- 主动运动绑定：每个主动镜头动作必须绑定一个周围环境变化，用“镜头动作 → 环境响应”组织时间轴。
- 主体锁定：人物、车辆、动物数量和外观保持一致；遮挡后按原方向重现。
- 速度节奏：具体加速、减速、停顿、拉升、俯冲节点。
- 光线：方向、时段、遮挡后的曝光变化。
- 氛围：大片质感、电影调性、真实运动模糊和清晰空间视差。

## 9. 高风险场景 prompt 模板

### 9.1 飞鸟掠过稻田或树林

```text
FPV first-person bird-flight perspective through a rice field and trees. 0-3s: the camera dives into the rice tips at blade height; tall rice stalks first cover both edges of the frame, then visibly bend outward and get pushed aside by the airflow, with leaf tips brushing across the lens edge. 3-7s: the camera skims forward through a narrow open channel, foreground rice stalks are pressed down into a rolling wave and rebound behind the camera, while the distant field moves slowly to create strong parallax. 7-10s: the camera rises to avoid a solid tree trunk and passes only through a visible open gap between branches; nearby leaves flutter and part from the airflow. A person near the tree remains a solid physical subject, the camera arcs around the person and tree instead of passing through them. Side sunlight, cinematic natural color, realistic motion blur, visible plant motion, physically plausible obstacle avoidance, continuous spatial depth.
```

### 9.2 飞鸟穿越高草丛

```text
FPV first-person bird-flight perspective inside a dense high-grass corridor, with grass motion as the main foreground action. 0-3s: the camera enters at grass-tip height, tall grass blades partially block the left and right edges of the frame, then the airflow from the fast pass pushes the blades outward, bending them away from the lens. 3-6s: the camera threads through a visible narrow gap; grass blades whip past the lens edge, some blades flatten into a wave under the flight path, and the wake travels backward through the grass. 6-9s: the camera makes a slight natural bird-like rise and bank, the pressed grass behind springs back upright, while new foreground blades bend before the camera reaches them. 9-12s: the camera exits the grass into a brighter open field, with the last blades brushing past the frame edge and rebounding. The grass must never stay still; its bending, parting, brushing, wave motion, and rebound are clearly visible throughout the shot. No tree trunk, person, animal body, or solid obstacle is crossed; the camera only uses open gaps. Cinematic natural light, strong foreground parallax, realistic motion blur, physical airflow interaction.
```

### 9.3 车辆追飞与超车

```text
FPV chase-flight perspective following the red lead car and the black secondary car on the same road. Both cars remain present and visually consistent throughout the shot; the red lead car is the main tracking anchor, the black car may be briefly hidden by road dust or a passing foreground pole for less than one second, then reappears in the same lane and direction. The camera dives from above, flies through the safe open space between the cars without touching either vehicle, then rises over the red car and banks to the side. Car count stays unchanged, no vehicle disappears, no car body is crossed by the camera. Road reflections, wheel motion, dust trails and sunlight flicker remain continuous, fast cinematic FPV movement with clear parallax and physically plausible spacing.
```

### 9.4 人物与树木同框

```text
FPV first-person camera rushes through a visible open path beside the tree, then curves around the person at a safe distance. The person and tree trunk are solid obstacles; the camera never passes through the body, face, limbs, or trunk. Leaves near the lens flutter from the airflow, clothing edges and hair move subtly as the camera passes. The motion begins with a low forward glide, slows near the person, rotates around the outer side, then accelerates into the open background. Warm side light, cinematic depth, realistic occlusion, continuous subject identity, no physical intersection.
```

### 9.5 室内穿门穿廊

```text
FPV first-person camera glides low through an open doorway, follows the corridor centerline, banks around a table without intersecting furniture, then exits through a bright open door. Curtains and small papers move subtly from the airflow as the camera passes. Walls, door frames, furniture and people are solid obstacles, only open doorways and clear gaps are used for flythrough. Speed increases after each doorway and slows before tight turns, realistic indoor lighting, strong foreground-to-background parallax, cinematic stable exposure.
```

## 10. 静默自检

定稿前内部检查，不向用户输出，除非用户要求点评。

- 主体类型、空间结构、风格预设、轨迹、分镜、视频之间的因果链是否成立。
- 是否建立空间占用图，并区分可穿越结构、不可穿越障碍和动态反馈物。
- 是否逐个检查每个主动运动 beat，并确认其都有“镜头动作 → 环境响应”的对应关系。
- 是否存在镜头高速前飞、俯冲、拉升、侧飞、穿越、追车、穿廊时，周围环境仍完全静止的片段；若存在，必须判定失败并重生成。
- 是否至少穿越 1 个真实空隙或结构；若没有真实空隙，是否改为绕行或掠过。
- 是否避免穿过树干、人体、车身、墙体、柱子、家具等实体。
- 低空高速经过草丛、稻田、麦田时，是否把草叶运动写成前景主动作，而不是背景形容词。
- 飞鸟穿草丛的前 3 秒是否能看到草叶遮挡镜头边缘、被拨开、压弯或擦过镜头。
- 镜头离开草丛后，是否能看到被压弯的草叶回弹或尾流波纹扩散。
- 车辆、人物、动物是否建立主体追踪锁；数量、颜色、外观、方向是否保持一致。
- 车辆场景是否明确“车辆数量保持不变、短暂遮挡后按原车道重现”。
- 飞鸟视角是否有自然起伏、气流反馈和实体避障，而不是僵硬平移。
- 穿越前后是否有高度变化或方向变化。
- 首 3 秒是否出现明确飞行动作和空间纵深提示。
- 速度是否有加速、减速或蓄力变化。
- 光线方向是否与飞行方向协调，避免无意逆光盲飞。
- ≤15s 成片是否一次生成；>15s 是否拆分为若干 ≤15s 片段。
- prompt 是否以正向描述为主，避免只堆否定式约束。
- 参考素材主体是否清晰，空间纵深是否足够。
- 全文语言是否与目标市场一致。
