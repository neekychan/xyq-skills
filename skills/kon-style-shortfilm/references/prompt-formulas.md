# 今敏导演风格多模态提示词撰写指南

> 可适配的模式与句式，按场景改写，不要逐字照搬。

## 目录

1. 图像生成提示词公式
2. 视频生成提示词与画面物理动作死锁公式
3. 四宫格场景子区域锁定句式
4. 今敏式无缝转场画面物理动作死锁句式

---

## 1. 图像生成提示词公式

### 1.1 角色全身三视图人设图（TextToImage / ImageToImage）

**公式**：

`[角色核心人设描述] + character sheet, full body model sheet, 3 view rendering showing front view, side view, and back view simultaneously side-by-side, clean white background, 武藏野美大 90s hand-drawn cel anime style, visible hand-drawn charcoal pencil outlines, organic cel-paint texture, tactile paper grain, high-precision hand-inked cel-shading without digital gradients, desaturated 90s retro film color wash, highly realistic facial proportions, extremely detailed anime key art --ar 16:9`

**注意**：绝对禁止加入任何网格分割线或不连贯背景，确保在一幅画布中无缝并排放置，锁定纯手绘有机笔触，锁定角色核心视觉一致性锚点。

### 1.2 多角度无人物四宫格场景图（TextToImage / ImageToImage）

**公式**：

`pure scenery with no characters, 4-panel split grid reference sheet, panel 1 (wide-angle establishing shot of [场景名], asymmetric framing with dramatic negative space, split-level vertical layering, organic watercolor wash), panel 2 (macro close-up of domestic furnishings and props, shallow depth-of-field, dusty paper grain texture, tactile cel-paint layering), panel 3 (deep receding linear perspective corridor, off-center lens alignment, cold metallic industrial tones clashing with warm-tinted pools of light, visible ink outlines), panel 4 (dramatic cinematic lighting with high-contrast desaturated shadows and extreme temperature clash, muted retro film color palette with a 90s vintage warm-tinted wash, 85% teal and 15% amber ratio), Tokyo urban realism, Satoshi Kon anime style, visible hand-drawn outlines, organic paper texture overlay, highly detailed cel animation environment --ar 4:3`

**注意**：强行在公式头部锁死"无人物"指令，并在提示词中通过排版构图与质感修饰词（如 asymmetric framing, watercolor wash, paper grain, desaturated shadows）清晰划分各网格的物理美学。

---

## 2. 视频生成提示词与画面物理动作死锁公式

### 2.1 角色生理与口型物理同步机制（核心）

当镜头包含对白台词、省略号或生理语气词（如喘息、干咽、大笑、哭腔）时，视频提示词中**必须用英文精确描摹相应的面部肌肉、下颌、嘴唇及体腔呼吸动作**，实现声音与视觉画面的像素级物理拟真对齐：

**对白喘息与气声（Gasping & Whispering）**：
`lips slightly parted in a quiet breathless gasp, chest rising and falling rapidly in sync with heavy breathing, eyes trembling, delicate mouth-sync motion representing shaky speaking`

**吞咽与干咽（Swallowing / Hesitation）**：
`throat muscles visibly contracting in a hard swallow, trembling lower lip, mouth opening and closing hesitantly as if struggling to find words`

**哭腔、抽泣与悲泣面部动作（Weeping, Sobbing & Tearful Facial Movements）**：
`lips trembling violently, mouth gasping slightly as if choked by tears, subtle sniffle causing the nostrils to flare briefly, chest heaving unevenly, tearful glint in the wide eyes, throat muscles contracting rapidly to swallow a sob, capturing a raw emotional breakdown and painful weeping sync`

**神经质笑意（Manic Laughter / Disorientation）**：
`eyes widening in psychological panic, a subtle manic and nervous twitching grin forming, mouth opening in hysterical laughter, facial muscles showing sudden tension and madness`

**瞳孔微缩与微颤（Pupil Constriction & Eye Trembling - 极端窥视与惊恐反应）**：
- 瞬间惊惧微缩：`extreme close-up of a single eye, the pupil constricting suddenly to a tiny pinprick, the iris trembling with psychological shock, rapid micro-saccades, subtle twitching of the lower eyelid, veins slightly visible in the sclera, capturing the raw terror of sudden realization`
- 虚实破裂微缩：`sudden dramatic contraction of the pupil, constricting rapidly into a small black dot, reflecting a flickering light, eyelids twitching in silent terror, capturing an intense moment of psychological realization`

**心理惊恐与面部肌肉死锁（Psychological Panic & Facial Muscle Lock）**：
- 窒息式惊恐死锁：`facial muscles locking in sudden rigid terror, eyebrows drawing tightly together and upward, vertical lines forming between the brows, the jaw freezing slightly open, subtle twitching around the corners of the mouth, pale skin with beads of cold sweat forming along the hairline, capturing an expression of profound existential dread`
- 绝望麻痹死锁：`a paralyzed facial expression of sheer panic, muscles around the eyes and mouth tightening into a rigid frozen state, cold sweat glistening on the forehead, the corners of the mouth twitching downward, expressing a trapped and helpless psychological breakdown`

---

## 3. 四宫格场景子区域锁定句式

用于在视频生成时锁定四宫格场景参考图中的特定子区域，防止背景跳画：

**走廊/深空间**：
`specifically expand and lock onto the deep perspective from the bottom-left panel of <<<image_2>>> as the background space of this unified shot, keeping the background extremely consistent with the previous shot.`

**书桌/陈设特写**：
`specifically implement and lock onto the desk and furnishings details from the top-right panel of <<<image_2>>> as the background space of this unified shot, ensuring zero scene displacement from the previous shot.`

---

## 4. 今敏式无缝转场画面物理动作死锁句式（核心）

### 4.1 瞳孔穿梭推镜头转场（Pupil Zoom-In/Push Transition）

**转场前镜（A镜：吸入）提示词物理描述**：
`extreme close-up of a single eye, camera rapidly zooms in along an exponential speed curve, pushing deep into the pupil's center with extreme radial motion blur, the pitch-black pupil expanding exponentially at 2.0x velocity to consume 100% of the screen, shifting focal depth directly into the iris, sub-pixel centered axis alignment, transforming the entire frame into a deep black void in the final frame, smooth seamless transition`

**转场后镜（B镜：展开）提示词物理描述**：
`camera starts inside a complete pitch-black void, then smoothly pulls back along an inverse-exponential curve (deceleration) with 3D spatial alignment, revealing [next scene space] expanding outward from the sub-pixel exact center of the screen, shifting from a narrow pinhole depth-of-field to deep-focus composition, seamless wormhole transition`

### 4.2 运动关联转场（Motion Match Cut）

**转场前镜（A镜：现实奔跑）提示词物理描述**：
`medium side profile shot of character running frantically to the right through rain-soaked urban street, motion blur on the character's limbs, rain streaks matching the running rhythm, composition centered at frame-right 60% position, camera tracking at matching speed`

**转场后镜（B镜：梦境奔跑）提示词物理描述**：
`medium side profile shot of character running frantically to the right through surreal dreamstage, maintaining identical composition at frame-right 60% position, identical running cadence and limb motion blur, seamless transition from rain-soaked street to neon-lit dreamstage, background transforming from gray urban to saturated crimson-gold`

### 4.3 形体关联转场（Shape Match Cut）

**转场前镜（A镜：旋转物体特写）提示词物理描述**：
`extreme close-up of rotating circular object filling the frame center, rhythmic circular motion, specific angular velocity and motion blur pattern, composition locked at frame center`

**转场后镜（B镜：旋转空间全景）提示词物理描述**：
`wide shot of circular/rotational space environment, matching the exact angular velocity and motion blur pattern of the previous shot, identical composition at frame center, seamless morph from close-up object to wide environment, the rotational rhythm continuing without interruption`
