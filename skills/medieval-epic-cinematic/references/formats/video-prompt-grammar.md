# 视频提示词文法规范

> 可适配的模式与句式，按场景改写，不要逐字照搬。

## 目录

1. 全局最高优先级
2. 参考图声明格式（必须）
3. 版权隔离规则
4. 提示词示例
5. 智能参考模式整合优先级

## 1. 全局最高优先级

- 提示词正文与代码块等所有生成内容一律强制使用纯英文呈现。
- 禁止出现任何中文字符。
- 台词（dialogue）无论用户以何种语言输入，写入提示词时均须翻译为英文后嵌入 `{...}` 语法块中。
- 禁止在 `{...}` 内使用中文或其他非英文字符。

## 2. 参考图声明格式（必须）

在每条视频提示词的最顶部，紧接图片占位符之后，输出一行纯英文参考声明，列明每张参考图的身份：

```
<<<image_1>>> is the storyboard panel set, <<<image_2>>> is [Character Name] character reference, <<<image_3>>> is the scene reference.
```

- 参考图数量与顺序须与实际传入的参考图列表完全一致，不得虚构未传入的编号。
- 角色名称使用当前项目的原创角色名（非 IP 角色专名）。
- 若某类参考不存在（如无第二角色），则跳过该项，不留空占位。
- 该声明行与下方正文之间空一行。

## 3. 版权隔离规则

提示词中严禁出现以下任何形式的版权标识符：

- **作品名称**：禁止出现任何 IP 名称及其缩写。
- **角色专名**：禁止出现任何原著/剧集中的具体角色姓名。
- **替代策略**：以视觉外形描述替代角色身份（如 "a red-haired noblewoman in heavy wool robes"），以地理美学描述替代地名（如 "a cold northern stone great hall with low candlelight"），以风格描述替代 IP 标识（如 "medieval epic cinematic aesthetic"）。

## 4. 提示词示例

### 示例一：场景人物核心概念图提示词

```
<<<image_1>>> is the visual style reference, <<<image_2>>> is {Protagonist} character reference, <<<image_3>>> is the scene reference.

Cinematic full shot, a masterpiece historical scene from medieval epic fantasy cinematic aesthetic. Shot on ARRI ALEXA LF camera with Cooke S4/i prime lenses, capturing the signature warm oil-painting-styled "Cooke Look". High dynamic range with thick film-like texture and rich shadows. The variable protagonist {Protagonist} is framed within the bleak, low-light medieval stone great hall in the cold north [Regional_Stage: North & the Wall]. Low-key lighting strictly driven by natural source compliance, utilizing single-direction fire torch glow, leaving massive unlit negative space and deep shadows. The color science features the regional palette of "Winter Teal and Ice Blue", with heavy desaturation and high contrast on skin textures. The character wears distressed heavy textured armor with deep 3D bone-carved embroidery and raw unpolished fur. Real grit and charcoal on sweat-glistening skin roughness at 0.4. Perfect architectural symmetry composition with extreme depth-of-field isolation, photorealistic texture detailing, no text, no watermarks, landscape 16:9 ratio.
```

### 示例二：角色设定卡提示词

```
<<<image_1>>> is the visual style reference.

High-definition, clean, and professional 3D character turnaround schematic on a pure solid white background. Medieval epic fantasy cinematic aesthetic, ARRI ALEXA XT rendering fidelity, Cooke S4/i premium optics quality. [Left Side - Main Full-Body Area]: Displays a full-body 3-view turnaround of the exact same character (front, left side, back view) under high-contrast dramatic backlight. The character wears custom medieval tactical garments crafted from heavy distressed leather, tight metal knittings, and asymmetrical rigid 3D wolf-bone embroidery. Hairstyle is complex, tactical hand-braided braids adhering to tribal winner tradition. The face, clothing weathering, and height proportions must be 100% identical. [Right Side - Simplified Detail Grid]: A neat 2x3 grid combining headshots and macro textures matching the character profile: 1. De-stage gritty portrait face with real mud texture under fingernails, fingernails and face mixed with sweat and carbon ash, 2. Back view showing complex braided hair parting lines, 3. Close-up of the rough heavy leather and unpolished fur textures, 4. Close-up of heavy iron metal buckles and geometric stitches, 5. Close-up of realistic physical prosthetics skin texture replicating grey-scale disease or scaly latex layers, 6. Close-up of mud-covered heavy boots. Landscape composition, pure white background, no text, no save buttons.
```

### 示例三：九宫格分镜提示词（武戏流 9 格）

```
<<<image_1>>> is the storyboard panel template, <<<image_2>>> is {Protagonist} character reference, <<<image_3>>> is the scene reference.

Professional cinematic multi-panel director's display sheet, 3x3 grid panel alignment system. Absolute visual DNA lock: all active panels are strictly rendered with ARRI ALEXA LF sensor characteristics and Angenieux Optimo zoom lens physics, executing cold, ruthless camera movement. Color palette strictly follows the regional color grading of [Regional_Stage: Southern Court & Golden Coast] with "Dragon Gold and Warm Yellow" amber highlights dominating the high-contrast lighting shadows. Centered at Grid [2,2], it displays a precise 3D top-down blueprint view of the grand royal throne hall, sketching brutal Technocrane paths and soldier square formations. Surrounding the center, 8 active panels display an intensive long-take handheld combat montage: Grid [1,1]: Voyeuristic long lens view hidden behind stone columns. The protagonist {Protagonist} unsheathes a broadsword, light fracturing off blood-stained metal. Grid [1,2]: Framing within a frame. Looking through a narrow arrow slit window, weapon kinetic movement cutting across natural window lighting. Grid [1,3]: Low-angle shot. The character lunges forward aggressively, sweat and soot flaring off the skin, high handheld camera shake and realistic blur. Grid [2,1]: Macro tracking close-up. Crimson blood splattering violently onto fine silk and gold-threaded 3D lion embroidery fabric. Grid [2,3]: Absolute symmetrical wide shot. An army of disciplined elite legion soldiers thrusting spears simultaneously, ruthless rigid authority framing. Grid [3,1]: Narrative cutaway shot. A crown forged of raw iron falls into blood-mixed mud on the battlefield, ultra-shallow depth of field. Grid [3,2]: Extreme kinetic view. Technocrane sweeping downward tracking a shield cracking under heavy blunt force impact, air particles and ash flying. Grid [3,3]: Isolating close-up. The character stands alone in a shadowed corner, back lit contour, face completely hidden, background fully blurred, capturing political isolation. Photorealistic film grain, pure solid borders partitioning the grids, no watermarks, no generic digital smoothness, landscape 16:9 ratio.
```

## 5. 智能参考模式整合优先级

每条镜头视频生成时，按以下优先级整合全部可用参考输入：

1. **分镜组参考** — 将已确认的九宫格分镜大图对应格位截图作为参考图，锚定构图方向与镜头节奏。
2. **角色参考** — 绑定该镜头所有涉及的角色设定卡作为参考图。
3. **场景参考** — 绑定该镜头所属场景概念图作为参考图。
4. **音色参考** — 若该镜头含台词角色，绑定对应音色样本，保证跨镜头口音与音色一致。
5. **提示词 + 台词** — 整合镜头运动、动作描述与以 `{...}` 嵌入的英文台词。
6. **连续性视频参考**（可选，低频使用）— 仅当当前镜头与前一镜头存在**极强动作连续性**时，追加前一镜头的视频作为参考；其余情况不使用。

## 落 prompt 前自检

- 提示词是否为纯英文，零中文字符？
- 是否以参考图声明行开头，且数量与顺序与实际传入一致？
- 台词是否用 `{...}` 嵌入且为英文？
- 是否零版权标识符（IP 名称、角色专名、地名）？
- 是否以视觉外形描述替代角色身份？
- 参考图整合是否覆盖了分镜/角色/场景三类？
