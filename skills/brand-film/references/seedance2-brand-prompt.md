# Seedance 2.0 Brand Film Prompt Writing

Use this reference when writing Seedance 2.0 prompts for brand films, TVCs, hero films, campaign films, and brand-story visuals within 15 seconds. The goal is not only to describe plot, but to lock the brand world's scene style, atmosphere, texture, lens behavior, lighting, and product-symbol treatment.

## Core Rule

Seedance 2.0 prompts for brand films must translate "brand feel" into visible production decisions:

**brand position -> style reference -> style keywords -> scene world -> material texture -> atmosphere -> lens and camera grammar -> product symbol -> emotional movement -> final brand memory**

Avoid abstract phrases such as `高级感`, `大片感`, `现代感`, `科技感`, `品牌感`, or `电影感` unless each is immediately grounded in concrete visual choices.

For every style-related phrase, concretize it through four craft layers: **镜头语言**, **视觉风格 / 美术规则**, **色调与材质系统**, and **音效 / 声音记忆点**. This applies to `风格与视觉参考`, `场景`, `拍法`, `画面内容`, and `声音`. The prompt should make the model see how the style is shot, what the image world contains, how color and material behave, and what the viewer hears.

## Two-Layer Output

For brand-film tasks, work in two layers:

1. `Brand Film Spec`: internal planning and user-facing rationale.
2. `Video Prompt`: the final Seedance 2.0 prompt.

Do not paste every spec field into the final prompt. However, the final prompt must keep style and camera references explicit. The generation model needs these details to create brand-film texture.

When the main skill uses compact spec output, keep the long Brand Film Spec in a standalone markdown file and keep the conversation concise. This must not reduce the final Seedance 2.0 prompt: the chat still needs a full paste-ready `video_generation_prompt` with the required visual reference, scene, subject, camera grammar, lighting, sound, product/brand proof, and final lockup.

Match the user's primary input language in the final chat response and in the prompt unless the user explicitly requests another target language or market. For Chinese requests, use Chinese field labels such as `风格与视觉参考`, `场景`, `主体`, `各个分镜的具体内容`, `拍法`, `画面内容`, `品牌/产品露出`, and `声音`; keep only brand names, product names, platform names, model names, and widely recognized style references in their original language.

## Prompt Structure

Use this compact final-prompt order:

```text
时长：15秒以内，比例：16:9。任务：生成品牌TVC/品牌大片。

标题：
风格与视觉参考：
场景：
主体：
各个分镜的具体内容：
```

Default to `时长：15秒以内，比例：16:9。` for brand films, TVCs, campaign hero films, luxury/fashion/fragrance image films, and cinematic routes. Use `9:16` when the user explicitly asks for vertical, mobile-first, TikTok/Reels/Shorts, social-first, or phone-native delivery. Keep 3-4 beats for 15-second videos unless the user changes the duration.

Horizontal and vertical prompts must be designed differently. Do not only change `16:9` to `9:16`. Horizontal prompts should emphasize spatial depth, lateral movement, architecture/landscape, ensemble blocking, wide negative space, and breathable logo/product lockup. Vertical prompts should emphasize stacked depth, central subject axis, closer hand/face/product proximity, safe caption zones, phone-readable product exposure, and faster top-to-bottom visual hierarchy.

The compact prompt should still carry strong visual direction:

- `风格与视觉参考` names the reference mode and 4-8 keywords; state what to borrow visually, including the full-film lighting rule, composition tendency, camera behavior, edit rhythm, and sound direction.
- `风格与视觉参考` must translate every style label into camera language, visual/art-direction rule, color/material system, lighting behavior, editing rhythm, and sound motif. Do not leave style as a reference name or mood word.
- `场景` covers location, time, props, spatial depth, light source, material texture, atmosphere, brand world, and where the brand/product sits in the space.
- `主体` covers only the visible human / product / object subject details that will actually appear in the shots, including posture, clothing parts, body parts, styling anchors, expression, motion habit, or product surface.
- `各个分镜的具体内容` contains timed beats with `拍法 / 画面内容 / 品牌或产品露出 / 声音`; `拍法` must include lens behavior, camera movement, composition, pacing, and shot grammar; `画面内容` should include shot-specific lighting when light is central to the brand texture.

Do not create a standalone `镜头参考` section in the final prompt. Lens behavior, camera movement, composition, pacing, and shot grammar belong inside `风格与视觉参考` and each beat's `拍法` / `画面内容`.

## Style Reference Planning

Before writing the shot list, choose one primary reference style according to the brand task. Choose it because it supports the category tension, audience, brand stage, and product role.

Use `references/style-reference-routing.md` when selecting a style direction.

For Seedance 2.0, treat the style reference as a generation trigger. Do not write flat style labels such as `高级感`, `电影感`, `都市感`, `温暖治愈`, `轻奢`, `自然纪实`, or `黑色电影` by themselves. Use a strong, recognizable film / advertising style anchor plus production details:

```text
风格参考：neo-noir rain city / Wong Kar-wai-style rainy neon romance / David Fincher-style cold corporate thriller / luxury fragrance myth film / 1980s VHS night-drive / Wes Anderson-style symmetrical tableau / A24-style surreal suburbia / Denis Villeneuve-style monumental sci-fi / high-fashion flash photography campaign / shounen anime opening
风格关键词：4-8个能改变画面的词
打光规则：光源 + 方向 + 对比 + 色温 + 反射 + 暗部 + 产品/人物高光
参考维度：镜头语言 + 色彩 + 美术 + 质感 + 运动规则 + 声音
```

The final prompt should make Seedance see a specific production world immediately. A strong style reference should answer:

- What camera behavior repeats: locked symmetry, slow axial push, handheld breathing, low-angle wide lens, long-lens compression, orbit, whip pan, macro slider, surveillance overhead.
- What lighting system repeats: neon reflection, practical lamp pools, dashboard glow, direct flash, gold skin light, hard top light, smoke shafts, cold window light, backlit rain, sodium-vapor streetlight.
- What color/material world repeats: red-green neon, amber/teal low key, pastel blocks, chrome/glass, wet asphalt, concrete/steel/wood, silk/metal/water, VHS color bleed.
- What visual/art-direction rule repeats: public-institution framing, backstage clutter, ritualized dressing, clean lab geometry, lived-in kitchen, warped office order, hero product table, street tribe code, or surreal everyday prop logic.
- What motion rule repeats: controlled slow push, lateral dollhouse movement, fragmented jump cuts, rhythmic match cuts, handheld micro-shake, speed-line impacts, one clean proof frame.
- What sound motif repeats: rain on glass, shutter clicks, synth pulse, sub-bass drone, ticking percussion, muffled radio, close-mic Foley, sudden silence.

The primary reference can be:

- a classic film or TV series used as a visual reference
- a director-like visual school
- an advertising lineage, such as luxury myth, sports manifesto, music-video fashion, documentary testimony, or food occasion warmth
- a genre world such as quiet life cinema, family naturalism, post-apocalyptic, atomic punk, noir, retro-futurism, new western, cold-war thriller, surreal suburbia, cyberpunk, or documentary realism

Use the reference to borrow production dimensions only:

- lighting logic
- color palette
- lens and camera movement
- production design
- costume/material language
- atmosphere and weather
- pacing and sound
- world rules

Do not copy protected characters, exact plots, dialogue, iconic scenes, logos, or named fictional worlds.

For Seedance 2.0, avoid naming multiple full style systems in one prompt. Mixed labels such as "documentary realism + music group ad + Japanese life cinema + surreal everyday" create competing instructions. If a secondary influence is useful, convert it into a production dimension instead of a second style name, such as "rhythmic match cuts driven by object sounds" or "warm environmental sound under a documentary camera".

Each prompt must include:

```text
风格参考：
风格关键词：
打光规则：
参考维度：
```

`风格关键词` should contain 4-8 concrete keywords created from the brief itself. Do not treat the examples below as a fixed menu. First infer the category tension, audience, product role, commercial type, and brand world, then create keywords that describe camera behavior, light, material, rhythm, world texture, and sound.

Possible keyword patterns:

- `日式生活电影`, `自然光`, `低声对话`, `空气感`, `生活褶皱`, `克制情绪`
- `欧洲艺术片`, `留白构图`, `长镜头`, `低饱和`, `人物疏离`, `环境声`
- `indie film 碎片氛围`, `自然杂光`, `胶片颗粒`, `局部身体`, `环境噪声`, `不完整动作`
- `岩井俊二式青春记忆`, `低饱和`, `白色过曝`, `淡蓝白绿色调`, `柔软逆光`, `浅景深`, `手持漂浮`, `局部身体构图`, `白光溶接`, `钢琴环境声`
- `奢侈品香氛神话`, `金色侧逆光`, `手部仪式动作`, `产品边缘高光`, `丝绸/水面/金属反射`, `暗部留白`, `低频歌剧呼吸`
- `Mugler式先锋时装身体`, `身体建筑`, `束腰轮廓`, `锐利肩线`, `黑色高光材质`, `直视镜头`, `低频秀场节拍`
- `aesthetic-core亚文化世界`, `服装编码`, `场景身份`, `平台原生姿态`, `色彩纪律`, `道具标识`, `社群声音`
- `音乐舞蹈片`, `群像调度`, `节拍剪辑`, `可模仿动作`, `强色块`, `身体记忆`
- `A24式轻微异样`, `普通生活场景`, `超现实小偏差`, `安静不安`, `固定镜头`, `冷幽默`
- `neo-noir rain city`, `湿地霓虹`, `长焦压缩`, `车灯眩光`, `低调光`, `雨刷节奏`
- `David Fincher式冷峻惊悚`, `绿灰暗部`, `对称办公室`, `屏幕冷光`, `精确慢推`, `机械低噪`
- `Wong Kar-wai式雨夜霓虹`, `红绿光污染`, `玻璃反射`, `慢动作碎片`, `前景遮挡`, `孤独近景`
- `Denis Villeneuve式纪念碑科幻`, `巨构墙面`, `沙尘侧光`, `轴向慢推`, `产品作为唯一发光点`, `小人物大尺度`, `低频无人声氛围`
- `1980s VHS夜行`, `磁带噪点`, `仪表盘光`, `钠灯街道`, `色彩溢出`, `手持乘客视角`
- `高定闪光灯大片`, `direct flash`, `硬阴影`, `切脸构图`, `后台白墙`, `快门声`, `侵略性姿态`
- `Wes Anderson式对称童话`, `锁定居中`, `粉彩分区`, `横向平移`, `微缩布景`, `冷面表演`
- `末日废土`, `沙尘硬光`, `低饱和暖黄`, `修补金属`, `功能性服装`, `手持追踪`, `风声与工具声`
- `原子朋克`, `冷战实验室`, `奶油色控制台`, `圆角金属仪器`, `模拟仪表指针`, `对称构图`, `硬边顶光`, `合成器低鸣`
- `黑色电影雨夜`, `湿地反光`, `百叶窗阴影`, `低调光`, `烟雾层次`, `慢速推轨`
- `复古未来主义`, `太空时代家具`, `柔和塑料材质`, `粉蓝撞色`, `宽角静帧`, `合成器氛围`
- `手持纪实`, `自然光`, `拥挤后台`, `呼吸感镜头`, `真实皮肤纹理`, `环境杂音`

These examples are inspiration only, not a style menu. Keep the keyword list coherent under the one primary style. A brand film can be quiet, warm, elegant, funny, observational, romantic, surreal, epic, or highly genre-driven. The keyword set must make the brand more legible, not overpower it.

Treat broad labels such as `奢侈品神话`, `史诗尺度`, `末日`, `原子朋克`, `复古未来主义`, `纪念碑科幻`, `未来感`, and `霓虹赛博` as unfinished placeholders. Before finalizing, either translate the label into brand-specific human-scale proof, material texture, camera behavior, lighting behavior, and sound motif, or replace it with a more precise style anchor created for the brief.

## Narrative And Shot Logic

Every timed beat must be a shootable narrative step, not only a story summary. Seedance 2.0 needs camera, sound, and atmosphere to understand how the beat should be filmed.

For each beat, specify:

- narrative function: entering the world, creating pressure, revealing desire, triggering action, proving change, or resolving the brand idea
- transition bridge: match cut, repeated gesture, screen glow, object movement, music cue, environment sound, eye-line, or camera direction
- camera grammar: shot size, angle, camera position, movement, composition, and foreground/background relationship
- lighting grammar: light source, direction, contrast, softness, color temperature, reflection, shadow density, skin/product/logo highlight, and how light changes from the previous beat
- sound logic: environment sound, human voice, breath, silence, music, phone tone, machine sound, crowd reaction, or object sound
- scene atmosphere: light, air, texture, crowd density, rhythm, and physical details
- tone consistency: every beat belongs to the same narrative argument and chosen style world

Before finalizing, every beat should answer: why this shot now, what changed from the previous shot, how the light is designed in this exact frame, and how sound or atmosphere helps Seedance 2.0 shoot the scene.

## Motion Spine And Continuity

Before writing timed beats, define the prompt's motion spine in one sentence: what action, object, sound, light, gaze, spatial path, or material change carries the viewer from the hook to the lockup.

Good motion spines are concrete and sequential:

- `hand closes latch -> motor starts -> road vibration -> dashboard glow -> headlights reveal destination`
- `shutter click -> flash reflection -> body turn -> fabric snap -> logo lockup`
- `ice clink -> phone tap -> rain on delivery bag -> bottle hits table -> liquid enters glass -> cheers`

Use the motion spine to make the film feel continuous:

- Each beat should receive a visible or audible cue from the previous beat.
- Each beat should leave a cue for the next beat.
- Each beat should contain a real action, material change, reaction, or spatial movement.
- Product or brand appearance should change the movement rhythm, light state, sound pattern, posture, relationship, or world logic.
- The final lockup should close or transform the opening cue into a brand memory.

Do not add a separate `motion spine` field to the final compact prompt unless the user asks for development notes. Instead, embed the continuity inside `拍法`, `画面内容`, and `声音` so the video model receives it as production direction.

## Lighting Design

For brand films, lighting is a production rule, not a finishing adjective. Define lighting at two levels:

- In `风格与视觉参考`, write a full-film `打光规则`: key source, direction, contrast, softness, color temperature, reflection strategy, shadow density, and the emotional movement of light across the film.
- In every important `画面内容`, state how the light lands in that shot: what hits the face, hands, product, logo, packaging, fabric, car body, screen, table, architecture, or background; what remains in shadow; what rim light, catchlight, reflection, or highlight makes the image feel like a brand film.

Use light to make brand texture visible:

- tension: hard noon sun, glare, cold screen glow, narrow practical light, deep shadow, low-key contrast, flicker, or backlit haze
- release: softened bounce, open shade, warm side light, water reflection, cleaner fill, lower contrast, moving tree shadow, or skin catchlight
- product proof: product edge light, glass refraction, metal glint, screen glow, condensation sparkle, logo catchlight, readable pack silhouette, or reflection on a branded surface
- final lockup: designed product/logo light such as gold logo reflection on black, soft shadow under white packaging, neon rim on a device edge, warm table light on a ritual object, or headlight edge on a vehicle line

Concrete lighting phrases are better than broad style claims:

- `正午硬顶光制造热感压迫`
- `白墙反射出柔和侧光`
- `水面反光落在脸侧和手腕`
- `侧逆光照亮喷雾边缘`
- `产品玻璃边缘出现清晰轮廓光`
- `低调暗部托住金色logo`
- `柔化窗光保留真实皮肤纹理`
- `冷屏幕光和暖台灯形成责任压力`

## Brand Scene Style

Define the scene as a brand world, not a generic location.

Weak:

```text
高级办公室，科技感，年轻人在使用产品。
```

Better:

```text
清晨6点的玻璃幕墙创意工作室，室内只开一排冷白桌面灯，窗外城市还未完全亮起，桌面有样机、草图、咖啡杯和半透明便签，空间安静、克制、像一次重要提案前的最后准备。
```

Write scene style through:

- time of day
- weather or air quality
- architecture and spatial depth
- props that imply the role and category
- cleanliness or lived-in texture
- brand-coded color accents
- foreground/midground/background composition

## Atmosphere and Texture

Atmosphere should be physical:

- mist, rain reflection, dust in light, condensation, fabric movement, screen glow, glass reflection, metal edge light, skin texture, paper grain, food steam, leather crease, road spray, stage haze.

Texture should fit the category:

- tech: glass, brushed metal, screen glow, translucent UI reflection, cable discipline, silent workspace.
- beauty: skin texture, water sheen, soft fabric, mirror reflection, bathroom steam, natural pores, hand ritual.
- auto: wet asphalt, headlight beams, cabin leather, dashboard glow, road vibration, tunnel light rhythm.
- fashion: denim weave, satin fold, wool texture, body movement, backstage mirror bulbs, dance-floor scuff marks.
- food/beverage: steam, condensation, table scratches, warm tungsten light, glass bubbles, wrapper crinkle.
- B2B: paper stacks, meeting-room glass, notification light, control-room screens, marker residue, late-night desk clutter.

## Lens and Camera Grammar

Do not stop at "close-up" or "wide shot". Each beat should specify:

- shot size: extreme wide, wide, medium, close-up, macro.
- angle: eye-level, low angle, top-down, over-shoulder, side profile, windshield POV, product POV.
- camera support: locked-off, slow dolly-in, tracking, handheld controlled, crane down, orbit, macro slider.
- motion speed: slow, precise, nervous, floating, rhythmic, sudden.
- composition: subject centered, negative space, foreground occlusion, reflection layer, split-depth, silhouette.

Example:

```text
拍法：低机位广角跟拍，镜头贴近湿润地面向前滑行，前景是车灯在积水里的长条反光，中景车身从画面右侧压过，背景城市高架形成冷色纵深。
```

## Brand and Product Symbols

In brand film prompts, product appearance should feel intentional.

Use `品牌/产品露出` only when visible in that beat:

- logo, product body, packaging, UI, app screen, vehicle, store sign, pattern, brand color, sonic logo, character, tagline, historic symbol.

Good exposure forms:

- product as tool in action
- product as light source
- product as POV/camera
- logo revealed through reflection
- package entering a ritual moment
- brand color appearing before the logo
- repeated shape motif that prepares the final packshot

Avoid:

- product floating without context
- logo slapped on the last frame only
- unreadable packaging text as the only brand exposure

## Beat Format

Every beat must use:

```text
0-3秒
拍法：
画面内容：
品牌/产品露出：（only if visible）
声音：
```

The first beat should create either a world entrance or a tension entrance. The final beat should resolve with a brand sentence, logo/product lockup, or memorable product-symbol image.

In each beat:

- `拍法` should explain how the shot is motivated by the previous cue, such as a match cut, sound bridge, object movement, gaze direction, light spill, or camera movement through space.
- `画面内容` should describe what actively happens in the frame, not only what is present. Include the physical change, human action, material behavior, or product consequence that moves the film forward.
- `声音` should carry rhythm, continuity, and emotional movement. A sound can continue, transform, drop out, or be answered by the next beat.

If the timed beats can be reduced to isolated labels such as `empty room`, `user taps`, `product arrives`, `logo appears`, rewrite them around the motion spine before finalizing.

## Positive Production Direction

Final brand-film prompts should express control through positive direction, not negative instructions. Omit standalone `限制` / `Restrictions` sections and omit wording such as `不要...`, `不生成...`, `避免...`, or equivalent "what not to do" phrasing.

Convert generation-control needs into affirmative setup, scene, or beat language:

- Claim safety -> describe only visible, substantiated outcomes and emotional response.
- UI uncertainty -> describe the UI at the level of readable, simple product action: app name, input text, generated cards, preview thumbnails, completion state.
- Beauty realism -> specify natural skin texture, visible pores, real fabric, water sheen, and practical light.
- Auto distinctiveness -> specify the vehicle's story role, cabin perspective, sensor POV, passenger relationship, or control-system proof.
- Handwritten or screen text -> specify short, readable text only when it is story-critical.
- AI / tech imagery -> specify the product's real visual language: phone screen glow, simple generation cards, clean preview grid, progress state, or result playback.
- Continuity -> write one affirmative final sentence such as: `全片保持人物、品牌/产品、场景连续一致，画面干净，只保留品牌锁定画面中指定的标识与字幕。`

## Compact Template

```text
时长：15秒以内，比例：16:9。任务：生成品牌TVC。

标题：
风格与视觉参考：

场景：

主体：

各个分镜的具体内容：
0-3秒
拍法：
画面内容：
声音：

3-7秒
拍法：
画面内容：
品牌/产品露出：
声音：

7-12秒
拍法：
画面内容：
声音：

12-15秒
拍法：
画面内容：
品牌/产品露出：
声音：
```
