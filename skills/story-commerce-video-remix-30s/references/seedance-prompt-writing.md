# Seedance Prompt Writing

## Seedance 2.0 Prompt Writing

After finalizing ONE genre direction, convert the story into a Seedance 2.0-ready prompt. Focus on executable video instructions, not strategy notes. The final prompt should be pasteable into Seedance with minimal rewriting.

### Default Deliverable

- Default output is one `video_generation_prompt`, not a loose brief.
- Use a continuous production-ready paragraph or a timestamped 5-6 shot block for 30-second prompts.
- The prompt must include: task type, duration, aspect ratio, subject binding, scene, camera movement, character actions, spoken lines, product placement, visible proof, sound/dialogue, and ending conversion line.
- The prompt must make a character or voiceover say the product name at least once. Product-name exposure in package text, product binding, or visual fields is not enough.
- For Chinese prompts, start with `时长：30秒，比例：9:16。`; for English prompts, use `Duration: 30 seconds. Aspect ratio: 9:16.`
- Do not use `--` in the final prompt.

### Example Hygiene

All examples, fragments, and templates in this file are structural references only. Never copy their concrete products, character traits, dialogue, visual references, scene settings, props, or conversion lines into the final answer unless the user supplied the same details.

Before finalizing a `video_generation_prompt`, replace every bracketed placeholder and every sample-like detail with task-specific content derived from the user's product, target audience, chosen genre, and category reference. If a detail is not grounded in the current task, omit it or create a new relevant detail instead of reusing an example.

Do not output any of these as final content:

- literal placeholder text such as `[known visual reference]`, `[shot size + angle...]`, or `[商品名]`
- sample-only products, outfits, body details, accessories, scenes, or plot lines
- sample-only visual reference names, unless the selected genre truly requires that exact reference
- generic sample dialogue such as `{狗血误判台词}` or `{包含商品名的转化句}`

### Seedance 2.0 Base Formula

Use this writing order:

**task type -> duration/aspect ratio -> subject and product binding -> visual style -> beat-by-beat camera/action/dialogue -> product proof -> final line -> stability constraints**

Seedance follows natural language well, but it needs clear object references and dynamic order. Each beat should answer:

1. What is the camera doing?
2. What is the character doing with their body, hands, and face?
3. Where is the product, and how is it used or revealed?
4. What is said or heard at this moment?
5. What visual proof appears before the payoff?

### Task Type Routing

When no media reference is provided, write a generation task:

```text
时长：30秒，比例：9:16。生成一条竖屏短剧剧情带货视频...
```

When references are provided, choose the correct Seedance task type:

- **Reference generation**: use `参考图片1中的产品外观，生成...` or `参考视频1中的运镜，生成...`
- **Video edit**: use `严格编辑视频1，将其中的...修改为...，其余内容保持不变。`
- **Video extension**: use `向后延长视频1，保持人物、产品、场景、画面风格和台词语气一致，继续生成...`
- **Video stitching / track completion**: use `视频1，过渡画面描述，接视频2...`

For edit and extension tasks, say `视频1`, not `参考视频1`. For reference-only tasks, say exactly what is being referenced: product look, character identity, action, camera movement, special effect, scene, composition, or audio tone.

### Subject And Product Binding

At the beginning of the prompt, bind every important subject with stable descriptions:

- Define the product with 2-3 visual anchors: color, shape, package, texture, pattern, logo position, screen state, or wearing position.
- Define each character with stable age range, face shape, hairstyle silhouette, outfit, posture, expression habit, and relationship role.
- Give every recurring person one memorable visual anchor that can persist across shots. Create a fresh anchor that fits the current category and scene, such as a visible facial mark, hair silhouette, accessory, outfit color/material, carried object, posture habit, or expression habit.
- Separate `主体1` and `反派1` through contrasting silhouettes and styling logic, not just dialogue. Define the contrast from the story relationship: restrained vs performative, prepared vs careless, understated vs flashy, professional vs chaotic, or another contrast that fits the current concept.
- Define scene references separately from character/product references.
- Reuse exact labels such as `主体1`, `产品1`, `反派1`, `图片1`, `视频1`; do not switch to vague pronouns when precision matters.
- If using multiple images, say `图片1`, `图片2`, etc. and explain what each one controls.
- For ancient / Qinggong / rebirth modern-product routes, bind the modern artifacts with higher weight than the generic costume world: name the phone/app/page/package/courier/delivery bag/order state and require at least one 古今同框 proof shot where the ancient scene and modern product are visible together.

#### Subject Character Design

Do not describe people only as `年轻女生`, `帅气男生`, `黑长发`, `白衬衫`, or `同龄女性`. These descriptions collapse into same-face generations. Design each subject as a character with stable, visible differences.

Use this compact character recipe:

`role + age range + face shape / facial anchor + hairstyle silhouette + outfit color/material + posture/movement habit + expression habit + relationship function`

Use this structure, replacing every slot with task-specific details:

- `主体1是[年龄段+目标人群角色]，[脸型/面部锚点]，[发型轮廓]，穿[符合场景的服装材质颜色]，[姿态/动作习惯]，[表情习惯]，[关系功能]。`
- `反派1是[与主体1形成对比的压力角色]，[不同脸型/发型/服装/配饰]，[压迫性动作习惯]，[表情/语气习惯]，[制造误判或冲突的关系功能]。`

Avoid character descriptions that only state age/gender and generic hair/clothing. They do not create stable visual separation.

When there are multiple supporting characters, keep them simpler but still distinct:

- `[见证者A]是[与主角/反派不同的发型或服装锚点]，[负责起哄/沉默/拍摄/质疑/确认结果]。`
- `[场景角色]是[年龄段/职业/服装锚点]，站在[与场景有关的位置]，负责[推动证明或见证反转]。`

Rules:

- Use 2-4 stable visual anchors per main character; too many anchors can distract from product proof.
- Do not assign the same hair, outfit color, glasses, or accessory to multiple characters unless the plot requires uniforms.
- Character anchors must be visible in normal shots, not hidden details the model cannot render.
- For beauty and skincare products, avoid making the protagonist visually humiliated through exaggerated flaws. Use lighting, posture, makeup texture, social pressure, and reaction shots instead.
- Keep character design consistent with the genre: 霸总 can use sharper tailoring and cold posture; 重生 can use mirrored past/present styling; 宫斗 can use rank-coded costume and accessories; campus/social scenes should remain everyday and believable.

Reference-binding structure:

```text
将图片1中的[产品类型、颜色、形状、材质、图案、Logo位置或穿戴位置]定义为产品1。主体1是[当前产品TA对应的人物设计]，在[符合商品使用场景的状态]中使用/穿戴/展示产品1。反派1是[制造压力的人物设计]，通过[与产品证明相关的动作]制造误判。全片产品1的[2-3个关键视觉锚点]保持一致。
```

### Beat Writing Order

Each shot or time beat should be written in this order:

1. **Camera / framing**: close-up, medium shot, over-the-shoulder, phone handheld, mirror shot, push-in, pan, tracking shot.
2. **Action / expression**: hand movement, product operation, body posture, facial reaction, eye line.
3. **Space / staging**: office corridor, family dining room, poolside, bedroom mirror, live room table, checkout page.
4. **Audio / dialogue**: natural dialogue, low background music, impact sound, object sound.

Avoid action descriptions that only say the product is shown or the protagonist feels confident.

Use this stronger structure: `镜头从[压力方/见证者]的[位置]推近到[产品证明位置]，主体1用[手/身体/工具/屏幕动作]完成[产品相关动作]，抬头看向[反派/镜头/见证者]，表情从[压力状态]变成[反击状态]。反派1低声说{与当前产品误判直接相关的台词}`

### High-Control Cinematic Prompt Pattern

For complex cinematic prompts, especially when using reference images, write in two layers:

1. **Global setup layer**: lock the reusable world, subject identity, product identity, scene identity, style, lighting, lens, sound rule, and continuity constraints.
2. **Shot layer**: describe only what changes in each shot: framing, composition, action, motion, character expression, product proof, and sound.

This is useful when the concept has a strong visual universe, such as retro-futurism, apocalypse, luxury melodrama, CEO office fantasy, courtroom confrontation, family banquet, poolside comparison, or live-room chaos.

Global setup should include:

- **Reference binding**: `参考图片1的场景构图`, `参考图片2的人物外观`, `参考图片3的表情状态`; explain what each reference controls.
- **Title / concept name**: when useful, start with a short title such as `《入侵》` or `《宫门补货》` to lock the tone.
- **Subject identity**: body type, clothing, face/display feature, role relationship, and one memorable visual anchor.
- **Product / prop identity**: exact color, shape, material, position, logo/screen/pattern, and whether it is worn, held, opened, displayed, or used.
- **Scene state**: time of day, weather, light direction, aftermath objects, crowd state, room layout, or social setting.
- **Style stack**: era, genre, realism level, image style, lens/camera feel, color palette, grain, contrast, and whether it should feel like live-action rather than game/CG.
- **Known visual reference**: a recognizable film, TV series, director-era, advertising style, art movement, or platform-native aesthetic. State which part is being referenced: color palette, lens language, architecture, costume, pacing, lighting, mood, production design, or genre atmosphere.
- **Lighting / exposure rule**: exposure level, contrast, practical light source, rim light, haze, reflections, highlights, and whether shadows should keep detail.
- **Camera / lens rule**: camera type, handheld/fixed style, lens reference, depth of field, motion blur, camera shake, and whether the image should avoid game/CG gloss.
- **Sound rule**: music, no music, live sound only, object sound, crowd reaction, phone shutter, impact sound, or dialogue.
- **Key elements**: list the protagonist, product/weapon/tool, antagonist/witnesses, and scene references before the beat list when there are multiple visual references.

Shot layer should be concise and physical:

- Define **shot size**: close-up, medium shot, low-angle ground-level shot, over-the-shoulder, wide shot.
- Define **camera position and angle**: front/side/back, high/low/eye-level angle, 45-degree side angle, foreground obstruction, or over-the-shoulder relation.
- Define **composition**: who is left/right/center, foreground/background, product position, witness position.
- Define **camera behavior**: fixed camera, handheld follow, slow push-in, pan, tracking, orbit, rack focus.
- Define **action chain**: one clear action at a time, with body part and force when relevant.
- Define **motion result**: object flies out of frame, product opens, screen changes, hair moves, character turns, crowd freezes.
- Define **payoff reaction**: antagonist stunned, protagonist calm, bystander whispers, phone camera clicks, family goes silent.

Do not mix too many unrelated actions in one beat. If the shot contains a physical gag, combat move, dance move, product reveal, or proof moment, describe the spatial path and endpoint clearly.

For Seedance, dense style language is acceptable only when it clarifies the image. The prompt still needs concrete camera/action instructions. A beautiful style stack cannot replace the action chain.

For high-control cinematic scripts, prefer this global order before the beat list:

`标题 -> 视觉基调 -> 画面风格 -> 主题与情绪 -> 色彩与色调 -> 光影设计 -> 拍摄设备/镜头语言 -> 声音 -> 关键元素 -> 场景 -> 分镜`

This structure is especially useful for sci-fi, palace drama, crime scenes, action, luxury melodrama, and any prompt using multiple image references.

### Known Visual Reference Rule

It is often useful to anchor the visual baseline with a known film, TV series, aesthetic movement, commercial style, or platform-native look. This gives Seedance a stronger visual target than generic words like `cinematic`, `premium`, or `高级`.

Use reference structures like this. Choose a fresh reference that fits the selected genre and product; do not reuse the structures below as final content:

- `视觉基调参考[影视/综艺/平台原生内容/广告类型]的[色彩与光线维度]、[镜头语言维度]和[场景/服装/节奏维度]`
- `视觉基调参考[目标受众熟悉的内容形态]的[构图]、[人物调度]和[情绪节奏]`

Always specify what part of the reference should be used:

- **Color / light**: warm orange, sea-salt blue, neon magenta, low-key contrast, harsh noon sunlight.
- **Production design**: 1960s atom-punk villa, luxury CEO office, crowded family banquet, old apartment corridor.
- **Lens / camera**: anamorphic widescreen, handheld phone video, slow push-in, fixed low-angle shot, orbit follow shot.
- **Costume / styling**: western retro, quiet luxury, beach vacation, office uniform, family banquet formalwear.
- **Mood / genre**: absurd apocalypse, melodramatic betrayal, cold CEO romance, family oppression, comedy misunderstanding.

Do not rely on the reference name alone. Write `参考X的[具体视觉维度]` rather than only `参考X风格`. If the reference conflicts with the story-commerce goal, keep the product proof and action chain higher priority than the style reference.

### Required Visual Reference In Prompt

Every `video_generation_prompt` must include a visual reference anchor in the first setup paragraph, unless the user explicitly asks for a plain no-reference prompt.

The reference can be a known film, drama, variety-show format, platform-native video style, visual genre, art direction movement, camera language, or lighting reference. Always name the borrowed dimensions:

- **Color / lighting**
- **Lens / camera language**
- **Costume / styling**
- **Production design**
- **Pacing**
- **Mood / genre atmosphere**
- **Composition**

Avoid empty style labels:

- `电影感`
- `高级感`
- `短剧感`
- `真实自然`
- `古装风`

Use concrete anchors created for the current task:

- `视觉基调参考[具体内容形态]的[权力关系构图/反应切镜/手持真实感/强对比侧光/屏幕回放结构等具体维度]`
- `视觉基调参考[平台原生视频类型]的[拍摄设备感/节奏/真实互动/环境声]`

Tie the visual reference to the selected creative container. The prompt should make the viewer understand the genre world before the product proof appears.

### Dialogue And Symbol Rules

- Use `{}` around spoken dialogue. The dialogue must be freshly written for the current product and conflict, for example `主体1说{[当前产品名或产品结果相关台词]}`.
- Use `（）` for music, for example `（背景有低音量紧张短剧音乐）`
- Use `<>` for sound effects, for example `<手机快门声>` or `<人群安静一秒>`
- Include the exact product name in spoken dialogue or voiceover at least once, usually in the final conversion line: `主体1说{[用户给出的商品名或短商品名]，[符合平台和场景的转化动作]。}`. If the full listing name is too long, say the user-facing short product name plus the core product type.
- Do not count package text, brand logo, on-screen product binding, or `产品1` labels as dialogue exposure. The audience must hear or read a spoken line that names the product.
- Keep dialogue language unified. Avoid mixing Chinese and English unless the product or market requires it.
- Use common, easy-to-pronounce words. Avoid rare characters, dense brand jargon, and overly technical claims.
- If subtitles are required, explicitly say where and when they appear. Otherwise, default to no subtitles for cleaner generation.

### Story-Commerce Specific Prompt Rules

- The first beat must show the dog-blood conflict visually: accusation, public comparison, family pressure, love-rival provocation, boss humiliation, betrayal hint, or absurd misunderstanding.
- Product explanation should not arrive before pressure is clear.
- The product must appear as action, not static packshot: worn, opened, handed over, applied, clicked, compared, revealed, or used to produce the proof.
- The product proof must be visible, not just spoken: reaction shot, before/after, photo result, finished deliverable, clean surface, fit change, saved time, social recognition, or family relief.
- The product name must also be spoken at least once after the story pressure is established, so the name lands as the winning choice rather than as an early hard ad.
- The antagonist or witness should be visible during the payoff so the reversal lands.
- If the product is fashion/beauty/lifestyle, use close-up plus body/scene context; do not rely only on abstract words like `高级`, `显瘦`, `自信`.
- If the product is software/app, show human pressure first, then a tight screen/action proof, then a human reaction.

### Prompt Density Rules

Quality Seedance prompts are specific, but not randomly overloaded. Use detail to control ambiguity:

- Repeat the **global setting** once at the top; do not restate the entire world in every shot.
- Repeat the **key subject labels** in every shot where they appear, such as `主体1`, `反派1`, `产品1`.
- Repeat only the most important character anchors when needed for continuity, such as `主体1的[发型/配饰/服装锚点]`, `反派1的[对比性配饰/服装锚点]`; do not restate the full character biography in every beat.
- Repeat **critical product visual anchors** when the product is the proof, especially color, pattern, package, screen state, or wearing position.
- Keep each shot focused on one main event: humiliation, escalation, hidden choice, product reveal, proof, or reaction.
- Put lens/camera/lighting detail where it changes the shot. If it stays the same, place it in global setup.
- Use "live-action realism" constraints when the visual style risks becoming game-like, cartoon-like, glossy CGI, or brand showroom.
- Sound should support the beat: no music / live sound only / tense short-drama music / impact hit / phone shutter / crowd silence.

Avoid:

- Empty adjective piles without spatial action.
- Multiple camera moves that contradict each other in the same beat.
- Vague references like `像图片那样` without saying what the image controls.
- Product proof that is only described as an emotion.
- Repeating a long basic setup before every shot.

### Required Beat Structure For Video Generation Prompts

When writing `video_generation_prompt`, each time beat must include these fixed fields in this order. This is mandatory for Seedance prompts because it forces the model to know how to shoot the image before it receives the story action.

- **拍法**: write this first. Specify shot size, angle, composition, camera position, camera movement, and lens feel. Use structural wording such as `[角度]+[景别]+[构图关系]+[前景/背景]+[镜头运动或固定机位]`; create the actual camera description for the current shot.
- In `拍法`, do not stop at `近景` or `大全景`. Always add how it is shot: side/front/back angle, high/low/eye-level camera, handheld/fixed/tracking/push-in/pull-back, foreground/background relationship, and whether the camera follows the subject.
- **画面内容**: then describe what happens inside this shot: character body, hand, face, expression, eye-line, relationship pressure, story action, and the visible proof or payoff that must appear by the end of the shot.
- **商品露出**: optional field. Write it only when the product is actually visible, used, handed over, worn, opened, clicked, or otherwise present in this exact beat. Describe how the product is seen or used: front package, logo side, screen state, hand action, wearing position, texture, or result anchor.
- **声音**: dialogue, voice tone, narration, music, ambient sound, and sound effects. Put spoken lines in `{}`, music in `（）`, and sound effects in `<>`.

Omit anything not visible in the current beat. Do not write `商品露出` for absent, hidden, upcoming, off-screen, or only implied products. Do not say `产品1暂不出现`, `隐藏在包里`, `作为后续伏笔`, or describe any object that the viewer cannot see in this shot.

Do not add a separate `画面结果` field. Put the final visible result directly at the end of `画面内容`. Avoid abstract endings such as `女主很自信` or `产品很好用`; write the visible image inside the shot, such as `反派1看着合照沉默`, `产品1包装和古装宫宴同框`, or `杯沿保持干净`.

Use this beat template for 30-second prompts. Output 5-6 timestamped shots by default. The preferred pacing is still front-loaded, but the new model should receive more story continuity and proof expansion: 0-3 seconds creates the abnormal hook and relationship pressure, 3-8 seconds escalates the pressure and locks the stakes, 8-14 seconds shows the protagonist's hidden choice and product/ability activation, 14-22 seconds carries the main visible proof escalation, 22-27 seconds lands the genre payoff plus witness reaction, and 27-30 seconds gives the product-name conversion line plus product/image high-light close-up. If the story is extremely simple, use 5 shots by combining payoff and conversion; otherwise keep all 6 shots.

```text
0-3秒：
拍法：[shot size + angle + composition + camera position + camera movement]。
画面内容：[one instantly legible abnormal hook or high-pressure visual action; show the relationship pressure and end with the wrong judgment or abnormal state visible as a concrete image]。
声音：[dialogue/voice tone/music/sfx]。

3-8秒：
拍法：
画面内容：
声音：

8-14秒：
拍法：
画面内容：
声音：

14-22秒：
拍法：
画面内容：
声音：

22-27秒：
拍法：
画面内容：
声音：

27-30秒：
拍法：
画面内容：
声音：
```

Insert `商品露出` only into beats where the product is visible or used. Do not leave empty `商品露出` placeholders.

### Prompt Template

This is a slot template, not an example prompt. Replace every bracketed slot and generic phrase before output. Do not preserve placeholder labels, generic conflict names, or sample tone words in the final prompt.

```text
video_generation_prompt:
时长：30秒，比例：9:16。生成一条竖屏短剧剧情带货视频。视觉基调参考[known visual reference]的[具体参考维度：灯光/镜头/服装/布景/节奏/氛围/构图]，镜头以中近景、表情特写、手部特写和反应镜头为主，节奏紧凑但叙事完整。

将[参考素材/产品描述]定义为产品1，产品1的[关键视觉特征]全片保持一致。主体1是[主角稳定人物设计：年龄段、脸型/面部锚点、发型轮廓、服装材质颜色、姿态习惯、表情习惯、关系角色]。反派1是[反派稳定人物设计：与主体1明显不同的脸型/发型/服装/配饰/姿态/表情和压力角色]。场景是[具体场景]。

0-3秒：
拍法：[shot size + angle + composition + camera position + camera movement]。
画面内容：[用一个异常动作、压迫关系、公开误判或结果先行画面立刻抓住注意力；这一镜同时交代谁在压迫主体1、主体1会失去什么，最后要在画面上看到压力、误判或异常状态成立]。
声音：[反派1用符合人物设定的音色说{当前冲突里的具体误判台词}]，（与当前类型匹配的音乐起），<关键环境音或冲击音>。

3-8秒：
拍法：[camera/framing/movement, with shot size, angle, composition, camera position, and camera movement]。
画面内容：[反派1继续施压或误判升级，见证者反应加重，主体1被锁进必须回应的局面；这一镜最后要看见主体1的视线、表情或手部动作发生变化，暗示隐藏选择开始]。
声音：[dialogue/music/sfx]。

8-14秒：
拍法：[camera/framing/movement, with shot size, angle, composition, camera position, and camera movement]。
画面内容：[主体1做出隐藏选择或启动反击；产品操作、能力启动、订单完成、涂抹/穿戴/打开/点击/递出等关键动作被清楚拍到；这一镜最后要看见产品1开始产生可见证明，而不是静态摆拍]。
商品露出：[产品1以行动方式出现，正面、屏幕、包装、使用方式或结果锚点清楚]。
声音：[dialogue/music/sfx]。

14-22秒：
拍法：[main proof shot and witness reaction, with shot size, angle, composition, camera position, and camera movement]。
画面内容：[产品结果持续扩大成现场反转，至少给出两个连续可见证明或一个证明加一个对比反应；反派1、见证者或客户的表情变化被拍到，反派误判被产品结果当场推翻]。
声音：[reaction/dialogue/sfx]。

22-27秒：
拍法：[payoff shot with protagonist, antagonist, witness, and proof object relation, with shot size, angle, composition, camera position, and camera movement]。
画面内容：[genre payoff 落地：反派1失语、道歉、被打脸、关系修复或公开认可；主体1完成一个有爽感的收尾动作，产品证明仍然在画面中可见]。
声音：[payoff dialogue/reaction/music lift/sfx]。

27-30秒：
拍法：[closing composition with product and protagonist, with shot size, angle, composition, camera position, and camera movement]。
画面内容：[主体1看向镜头或见证者，说出自然转化句；产品和主体1在同一画面中被清楚看见，最后用产品/商品图片高光特写收束]。
商品露出：[产品1保持可识别，避免变成静态硬广 packshot]。
声音：主体1说{当前商品名 + 当前场景里自然成立的转化句}，（音乐抬升或干净收束）。

全片保持人物、产品、场景连续一致；不要生成无关同类产品；不要出现多人同脸；不生成字幕、logo、水印。
```

### Seedance Quality Check

Before finalizing, check:

- Does the prompt start with duration and aspect ratio?
- Is the task type clear: generate, reference, edit, extend, or stitch?
- Are product, protagonist, antagonist, and scene bound with stable labels?
- Are protagonist and antagonist visually distinct enough to avoid same-face generation, with concrete face, hair, outfit, posture, expression, and accessory anchors?
- If using a known visual reference, does it specify which visual dimension is borrowed, such as color, lighting, lens, costume, production design, pacing, or mood?
- Does each beat start with `拍法`, before the story content?
- Does each `拍法` specify shot angle, shot size, composition, camera position, and camera movement, or explicitly say fixed camera?
- Does each beat include `画面内容` and `声音` after `拍法`?
- Does it include `商品露出` only in beats where the product is actually visible or used, and omit that line when the product is not in the shot?
- Does each `画面内容` end with a visible proof, motion result, or payoff image rather than an abstract judgment?
- Does each beat specify voice tone, music, ambient sound, or sound effect?
- Does the product appear before the proof moment and remain recognizable?
- Is the proof visual enough for Seedance to render?
- Does at least one spoken line or voiceover explicitly include the product name, not only the package text or product label?
- For ancient / Qinggong / rebirth modern-product routes, is the modern product the main reversal evidence, and is there at least one strong 古今同框 shot rather than only a costume-drama atmosphere?
- Are spoken lines inside `{}` and sound/music cues formatted clearly?
- For cinematic prompts, is the global setup separated from shot-specific action so the prompt is detailed but not repetitive?
- Does each shot have one clear physical action chain and a visible endpoint?
- Does the prompt avoid `--`, vague pronouns, rare characters, and contradictory instructions?
- Does it include continuity constraints for character/product/scene?
- Has every example-derived detail been replaced with current-task content, with no copied sample products, sample characters, sample dialogue, sample visual references, or bracketed placeholders left in the final prompt?
