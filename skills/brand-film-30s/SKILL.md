---
name: brand-film-30s
description: Create Seedance 2.5-ready 30-second brand films, TVCs, campaign hero films, brand story films, and cinematic product films. Use when the active route is 30s, when the user asks for 品牌大片30s, 30秒品牌片, Seedance 2.5 brand film, TVC 30s, 品牌故事片30s, or a longer brand-image route with category tension, visual style, product/brand proof, and final brand mnemonic.
---

# Brand Film

## Seedance 2.5 Override

This is the 30-second Seedance 2.5 version of the brand-film skill. Follow the user's explicit duration first; if no duration is specified, default to `30秒` for this skill.

For final video prompts, read `/workspace/.skills/brand-film-30s/references/seedance25-brand-prompt.md` before writing the prompt. The 30-second Seedance 2.5 prompt contract is authoritative for this skill.

Default 30-second brand-film rhythm:

- `0-3秒`: directed hook / brand world entrance.
- `3-8秒`: category tension or audience pressure.
- `8-14秒`: protagonist, subject, or brand world expands.
- `14-21秒`: product or brand mechanism becomes visible proof.
- `21-27秒`: emotional, social, or visual resolution.
- `27-30秒`: brand mnemonic lockup with product/brand asset, readable line, and sonic cue.

## Core Principle

Do not start from "premium visuals", slow motion, abstract slogans, or product features. Start from the category's real tension: what the audience wants, fears, resents, misses, or wants to prove inside this category. Then turn that tension into a film genre, a clear visual idea, and a brand-specific resolution.

The durable engine is:

**category -> audience pressure -> cultural timing -> brand asset -> film genre -> visual idea -> protagonist/world -> product role in the film -> brand evidence -> memorable brand line**

A strong brand film passes this test:

**Without this brand or product, the film cannot resolve the tension in this exact way; but the audience should feel they watched a film first, not a feature presentation.**

## Default Workflow

Use this skill as a routing hub. Keep the core reasoning in `SKILL.md`; load only the references needed for the current brand, category, and requested output.

Reference files are addressed as `/workspace/.skills/brand-film-30s/references/xxx.md`; when a reference is needed, read it with the `sandbox_read` tool.

Reference loading should be selective but real. Do not answer concrete brand-film, TVC, product-promotion, storyboard-prompt, or Seedance/video-generation tasks from `SKILL.md` alone.

For most concrete outputs, read these references with `sandbox_read` before finalizing:
- `/workspace/.skills/brand-film-30s/references/tvc-type-routing.md`
- `/workspace/.skills/brand-film-30s/references/style-reference-routing.md`
- `/workspace/.skills/brand-film-30s/references/compact-spec-output.md` unless the user explicitly asks for a fast prompt, chat-only answer, no file creation, or strategy-only guidance.
- `/workspace/.skills/brand-film-30s/references/seedance25-brand-prompt.md` when writing a final video prompt.

Read only the additional references that the task triggers:
- category reference when the product/category is concrete.
- `/workspace/.skills/brand-film-30s/references/current-trend-signals.md` when expression form, trend fit, AI/CGI, mixed-media, creator-style realism, or modular campaign judgment matters.
- `/workspace/.skills/brand-film-30s/references/vfx-expression-routing.md` when using VFX, CGI, motion graphics, animation, mixed media, virtual production, surreal transformation, impossible scale, product mechanism visualization, or generated-video spectacle.
- specialized craft references only when that craft layer is central or weak in the draft.

Use references silently; do not report the loading process to the user unless asked.

For concrete brand-film, TVC, campaign film, product-promotion, storyboard-prompt, or Seedance/video-generation tasks:

1. Diagnose category, audience pressure, cultural timing, brand asset, product truth, and delivery channel.
2. Read the matching category reference only when the category is concrete.
3. Read `/workspace/.skills/brand-film-30s/references/current-trend-signals.md` for expression-form judgment.
4. Read `/workspace/.skills/brand-film-30s/references/tvc-type-routing.md` unless the user already specified the exact commercial type.
5. Read `/workspace/.skills/brand-film-30s/references/vfx-expression-routing.md` when the route may use CGI/VFX, motion graphics, animation, mixed media, virtual production, surreal transformation, product mechanism visualization, impossible scale, or generated-video spectacle.
6. Read `/workspace/.skills/brand-film-30s/references/style-reference-routing.md` before choosing the visual style.
7. Read `/workspace/.skills/brand-film-30s/references/seedance25-brand-prompt.md` before writing a final Seedance 2.5 prompt.
8. Read `/workspace/.skills/brand-film-30s/references/compact-spec-output.md` when creating the default standalone creative plan file.
9. Read specialized craft references only when needed:
   - `/workspace/.skills/brand-film-30s/references/shot-logic-and-continuity.md` for filmable evidence, narrative beats, and motion spine.
   - `/workspace/.skills/brand-film-30s/references/lighting-design.md` for lighting rules and shot-level lighting language.
   - `/workspace/.skills/brand-film-30s/references/sound-and-music.md` for BGM density, sound motif, silence, and sonic lockup.
   - `/workspace/.skills/brand-film-30s/references/originality-checks.md` for anti-generic checks and failure modes.

If context is missing, proceed with labeled assumptions. Ask questions only when category, brand, or audience is unknowable.

## Always Apply

- Default to one fully developed, production-ready route unless the user explicitly asks for multiple concepts, alternatives, routes, or comparisons.
- When output is likely to become generated video, include a paste-ready 30-second Seedance 2.5 prompt even if the user did not explicitly say "prompt".
- Default to `时长：30秒，比例：16:9。` for brand films, TVCs, campaign hero films, luxury/fashion/fragrance image films, and cinematic routes. Use `9:16` only when the user asks for vertical, mobile-first, TikTok/Reels/Shorts, social-first, or phone-native delivery.
- Use 5-6 beats for 30-second brand films unless the user changes the duration.
- Match the user's primary language for the chat response, spec, and final prompt unless the target market requires another language or the user requests another language.
- Use one primary style reference or one coherent style family. If another influence is useful, translate it into a production dimension instead of naming a second full style.
- The brand or product must play a structural role: tool, evidence, ritual object, connector, turning point, protection mechanism, memory carrier, status signal, witness, lens, or proof mechanism.
- The first 2-3 seconds need a directed hook tied to category tension, product mechanism, or brand world.
- The final beat should usually create a brand mnemonic: visible product or brand asset, readable logo, brand name or product name when appropriate, brand line or slogan when appropriate, and a short sonic cue.
- Final `Video Prompt` text should use positive guidance only. Do not add standalone `限制` / `Restrictions` sections or negative instructions such as `不要`, `不生成`, or `避免`.

## Input Diagnosis

Before writing routes, identify:

- **Category**: sport, beauty, personal care, consumer tech, auto, fashion, food and beverage, alcohol, travel, finance, platform/service, B2B, or another category.
- **Brand stage**: challenger, legacy brand renewal, premiumization, launch, product-line push, reputation repair, youth refresh, or cultural leadership.
- **Audience**: who needs to feel seen, upgraded, reassured, provoked, entertained, or invited.
- **Category tension**: the lived pressure in the category, not the brand's slogan.
- **Cultural timing**: why this story should exist now.
- **Brand asset**: long-term symbol, tagline, sound, character, product shape, ritual, celebrity, founder story, design code, or historic campaign.
- **Product truth**: the smallest concrete ability, object, or ritual the product can make visible.
- **Film genre**: manifesto, documentary, horror, thriller, comedy, musical, dance, sports anthem, road film, family drama, workplace comedy, sci-fi, fashion film, product demonstration, or another genre.
- **Expression form**: live-action, CGI/VFX, motion graphics, mixed media, stylized animation, documentary fragments, screen format, or hybrid.
- **Commercial type**: product beauty / sensory product film, spectacle / VFX-led commercial, narrative lifestyle film, mood film, brand manifesto / anthem film, product demonstration / stunt spot, or format-based commercial / parody spot.
- **Style reference**: classic film, TV series, director-like visual school, advertising lineage, or genre world used as production reference.
- **Style keywords**: 4-8 concrete keywords created from the brand task itself, not chosen from a fixed menu.
- **Lighting logic**: source, direction, contrast, softness, color temperature, reflection, rim light, product edge light, skin highlights, shadow density, and emotional shift.
- **Motion spine**: the action, object, sound, light, gaze, space, or material change that connects the film.
- **Product narrative function**: resolver, witness, tool, lens, ritual object, social connector, memory keeper, status signal, safety system, or proof mechanism.
- **Brand line**: one sentence the audience can remember after the film.

## Category Routing

For a concrete category, read only the matching category reference before producing final routes. Do not load every category file unless the user asks for cross-category comparison.

- **Sport** -> `/workspace/.skills/brand-film-30s/references/categories/sport.md`
- **Beauty / personal care** -> `/workspace/.skills/brand-film-30s/references/categories/beauty-personal-care.md`
- **Consumer tech / AI** -> `/workspace/.skills/brand-film-30s/references/categories/consumer-tech-ai.md`
- **Auto / mobility** -> `/workspace/.skills/brand-film-30s/references/categories/auto-mobility.md`
- **Fashion / lifestyle** -> `/workspace/.skills/brand-film-30s/references/categories/fashion-lifestyle.md`
- **Food / beverage / alcohol** -> `/workspace/.skills/brand-film-30s/references/categories/food-beverage-alcohol.md`
- **Service / platform / travel / marketplace** -> `/workspace/.skills/brand-film-30s/references/categories/service-platform-travel.md`
- **B2B / productivity** -> `/workspace/.skills/brand-film-30s/references/categories/b2b-productivity.md`
- **Finance / insurance / health-adjacent** -> `/workspace/.skills/brand-film-30s/references/categories/finance-insurance-health.md`

Fast selector:

- **Sport** -> external doubt, identity pressure, body/action proof, manifesto or athlete montage.
- **Beauty / personal care** -> who defines beauty, self-worth, body confidence, documentary or human story.
- **Consumer tech / AI** -> invisible capability or risk, clear visual idea, genre film.
- **Auto / mobility** -> vehicle as space, sensor, camera, companion, or control system; avoid generic road beauty.
- **Fashion / lifestyle** -> identity, body language, music, cultural participation, luxury mythology, or subculture code.
- **Food / beverage / alcohol** -> occasion, ritual, warmth, humor, heritage asset, sensory proof, or social connection.
- **Service / platform** -> life friction removed, invisible orchestration, comedy, format disruption, or everyday epic.
- **B2B / productivity** -> responsibility, time, coordination, risk, competence, complexity, or unseen work.

## Treatment Direction

For every category, decide whether the route primarily works as **product-led / image-led film** or **narrative film** before developing it.

- **Product-led / image-led film**: product, material, body, space, light, typography, CGI motion, or atmosphere carries the idea. Use this when the brand needs symbolic elevation, visual memory, product desirability, or a mood film. Still require visible cause and effect: object/material/body -> pressure/desire -> transformation -> brand evidence.
- **Narrative film**: protagonist, social situation, conflict, ritual, or journey carries the idea. Use this when the brand needs empathy, cultural relevance, humor, tension, or human reversal. The story must still have a clear directorial point of view.

Do not treat these directions as "no story" versus "story." Product-led films need visual cause and effect; narrative films need brand-owned visual form.

## Software Service And UI-Minimal Rule

For software service, platform, AI, B2B productivity, agent, SaaS, marketplace, and app-based brands, do not make complex UI screens carry the film unless the user explicitly asks for a UI-heavy product demo. Translate product capability into physical, spatial, human, symbolic, or material proof.

- Treat UI as a trigger, light source, or final brand lockup, not the main proof system.
- Keep visible UI minimal: one input field, one readable brand name, one simple icon, one large card, or one final product lockup.
- Show capability through the world changing: objects organize, light routes connect, rooms transform, physical tasks complete, people react, a process becomes visible, or an invisible system gains a material form.
- For AI / agent products, visualize work through paper, cards, folders, models, lights, paths, rooms, machines, timelines, characters, scenes, or orchestration.
- Product proof should be filmable without UI text. If the product is removed, the visible transformation should no longer make sense in the same way.

In final prompts, describe screens as `soft screen glow`, `minimal input bar`, `simple branded symbol`, or `clean final lockup` unless detailed UI is essential. Use positive control language such as `the screen remains minimal and readable, with only the specified brand mark and one large input area visible`.

## Style And Commercial Routing

Read `/workspace/.skills/brand-film-30s/references/tvc-type-routing.md` to choose the commercial type / production approach. The selected type must define visual style, lighting, camera/lens, editing rhythm, sound design, main subject, scene design, story structure, 30s beat template, product/brand role, and prompt requirements. Do not use type labels as decoration.

Read `/workspace/.skills/brand-film-30s/references/style-reference-routing.md` to choose a reference direction by brand task, not by personal taste. For Seedance 2.5, the style reference must be a strong film / advertising style anchor, not a mild mood label. Translate it into camera language, visual/art direction, color/material system, lighting behavior, editing rhythm, and sound motif.

When using surreal, uncanny, dreamlike, impossible, mythic transformation, heightened visual logic, or any phrase like `超现实`, first define one visible world rule through `/workspace/.skills/brand-film-30s/references/style-reference-routing.md` before writing the final prompt.

Use style references as production shorthand only. Do not copy protected characters, exact scenes, exact dialogue, franchise symbols, celebrity likenesses, or another brand's signature asset. If brand safety matters, translate the named reference into generic production language in the final prompt.

Style keywords should be generated from the brief, not selected from a fixed list. First infer the category tension, audience, product role, commercial type, and brand world, then create 4-8 keywords that describe camera behavior, light, material, rhythm, world texture, and sound. Examples such as `日式生活电影`, `欧洲艺术片`, `indie film 碎片氛围`, `A24式轻微异样`, `奢侈品神话`, `音乐舞蹈片`, `手持纪实`, `VHS/8mm 复古影像`, `末日`, `原子朋克`, `黑色电影雨夜`, `复古未来主义`, `冷战实验室`, and `霓虹赛博` are inspiration only, not a style menu.

Treat broad labels such as `奢侈品神话`, `史诗尺度`, `末日`, `原子朋克`, `复古未来主义`, `纪念碑科幻`, `未来感`, and `霓虹赛博` as unfinished placeholders. Before finalizing, either translate the label into brand-specific human-scale proof, material texture, camera behavior, lighting behavior, and sound motif, or replace it with a more precise style anchor created for the brief.

When using `Shunji Iwai-style lyrical youth memory` / `岩井俊二式青春记忆`, make the signature photographic system explicit: low saturation, pale blue-white-green palette, strong window backlight, visibly overexposed whites, shallow depth of field, handheld floating observation, partial body framing, soft focus, white-light dissolve, slight film grain, wind moving curtains / paper / hair, and quiet piano plus environmental silence.

## Route Development

For each concept, build the route in this order:

1. Name the category tension in plain language.
2. Choose the film genre and commercial type that can carry the tension.
3. Choose the expression form: live-action, CGI/VFX, motion graphics, mixed media, stylized animation, documentary fragments, screen format, or hybrid.
4. Choose one primary style reference and translate it into style keywords, camera language, light, color/materials, editing rhythm, and sound.
5. Define a clear visual idea for the invisible feeling or product truth.
6. Define the motion spine / continuity device.
7. Decide the brand world: where the film happens and what aesthetic rules govern it.
8. Design the protagonist or subject as a specific role, not a generic demographic.
9. Make the product or brand asset structural.
10. End with a memorable brand line.

Avoid route variations that only change wording. Vary the category tension, film genre, visual idea, protagonist, expression form, and product function.

## Story Boldness

Do not default to safe, ordinary brand stories. A brand film may be elegant and restrained, but it should not be bland. When the brief is open, prefer one distinctive trait: extreme premise, strange ritual, heightened social rule, impossible object, surreal spatial logic, subculture code, mythic transformation, genre twist, animated metaphor, VFX proof, format disruption, or a highly specific human situation.

Before finalizing, ask whether the story has a recognizable feature beyond the brand name: a world rule, visual format, sound rule, character behavior, impossible transformation, editing device, object motif, or final image. If not, make the premise sharper.

## Classic Case Library

When the user asks for classic cases, benchmarks, brand-film examples, or wants a concept that references Dior, Nike, On Running, Apple, or similar canonical brands, read `/workspace/.skills/brand-film-30s/references/classic-cases.md`. Use the cases as creative mechanisms, not as templates to copy.

For each borrowed case, identify what brand problem it solved, what category tension it used, what film mechanism made it memorable, what visual style and symbols carried the brand, what can be reused, and what must not be copied.

## Output Format

Default to one fully developed, production-ready route unless the user explicitly asks for multiple concepts, alternatives, routes, or comparisons. For brand film, TVC, product promotion film, or video-generation requests, prioritize one strong concept with a detailed, paste-ready `Video Prompt` that includes concrete protagonist, scene, emotional arc, product timing, sound, and brand line.

**Compact creative-plan rule**: for concrete brand-film, TVC, campaign film, brand-story, product-promotion, storyboard-prompt, or Seedance/video-generation tasks, read `/workspace/.skills/brand-film-30s/references/compact-spec-output.md` and create a readable standalone complete creative plan markdown file by default, unless the user explicitly asks for a fast prompt, chat-only answer, no file creation, or strategy-only guidance. Before the final chat response, write the complete creative plan with `sandbox_write` to the designated output path defined in `compact-spec-output.md`. Follow the file naming rules from `compact-spec-output.md`; do not define a separate naming scheme in `SKILL.md`. Do not merely mention a path in chat without writing the file, and do not place output files inside `/workspace/.skills/brand-film-30s/`. Do not weaken the final Seedance 2.5 prompt to make the chat shorter. Move route reasoning, category diagnosis, trend judgment, originality checks, and risks into the complete creative plan file. In the chat, use the user-facing structure `大的思路总结` / `完整创意方案可见：{written_output_path}` / `这是为你规划好的 prompt` / `你说“同意生成”，我就直接为你开拍。`

**Language consistency rule**: match the user's primary language for the chat response, spec, and final prompt unless the target market requires another language or the user explicitly requests another language. For Chinese requests, use Chinese field labels and Chinese dialogue by default. Keep only brand names, product names, platform names, model names, and widely recognized style references in their original language.

When compact spec output is not used because the user asked for a chat-only answer, no file creation, or strategy-only guidance, use a concise in-chat `Brand Film Spec` with these fields, translated into the user's language when appropriate:

```text
Brand Film Spec:
Brand:
Category:
Assumed audience:
Brand stage:
Campaign goal:
Category tension:
Cultural timing:
Brand asset to use:
Product truth:
Film genre:
Expression form:
Commercial type / production approach:
Style reference:
Style keywords:
Lighting logic:
Visual idea:
Motion spine:
Brand world:
Protagonist / subject:
Product narrative function:
One-sentence brand idea:
3-second opening:
Emotional build:
Brand/product proof moment:
Final brand line:
Script beats:
Camera / editing / sound:
Originality and brand fit check:
Why it works:
Risks to avoid:
Extensions:
video_generation_prompt:
```

Only when the user explicitly asks for multiple routes, output 2-3 distinct routes. Each route must include a compact big-idea summary and a `video_generation_prompt` for Seedance 2.5. Do not make the user select a route before seeing usable prompts.

## Seedance 2.5 Prompt Rules

Read `/workspace/.skills/brand-film-30s/references/seedance25-brand-prompt.md` before writing final prompts. Default to Seedance 2.5 and 30-second videos unless the user asks for another duration or delivery format.

The final prompt must preserve:

- `风格与视觉参考`
- `场景`
- `主体`
- `各个分镜的具体内容`

Prompt requirements:

- Start Chinese prompts with `时长：30秒，比例：16:9。` by default.
- State the task type: generate, reference, edit, extend, or stitch.
- Use 5-6 timed beats for 30 seconds.
- Bind recurring entities with stable labels: `品牌1`, `产品1`, `主体1`, `场景1`.
- In `场景`, specify location type, spatial depth, core props, material surfaces, light sources, atmosphere, and where the brand/product sits in the space.
- In `主体`, describe only visible human / product / object details that will actually appear later.
- Every beat must start with `拍法`, then `画面内容`, optional `品牌/产品露出`, and `声音`.
- In every `拍法`, include shot size, angle, camera position, movement, lens feel, composition, foreground/background relation, and editing transition.
- In every `画面内容`, include shot-specific lighting, material texture, atmosphere, color, reflection, shadow density, product/skin/fabric/glass highlights, and the exact physical change in the frame.
- In every `声音`, include music density or deliberate silence, sound design, key Foley/environment detail, rhythm change or stillness, and how the beat lands emotionally.
- Only include `品牌/产品露出` when the logo, product, packaging, UI, symbol, store, vehicle, or brand asset is actually visible.
- The product proof or brand mechanism must appear before the final brand line.
- The final beat should usually be a brand lockup with product / brand asset, logo placement, slogan or brand line placement, hold duration, sound cue, and spoken brand name / slogan when appropriate.

## Silent Checks

Run these checks during development and rewrite weak routes before finalizing. Do not dump the full checklist into user output unless the user asks for critique.

- Is the category tension real and specific?
- Is the commercial type clear enough to guide visual style, sound, camera, subject, and story development?
- Can the audience understand the visual idea without a paragraph of explanation?
- Does the brand or product structurally matter?
- Is the first 2-3 seconds distinctive?
- Is there a motion spine across the 30 seconds?
- Are camera, light, sound, and pacing concrete enough to shoot or generate?
- Is the concept modern for the category, or only a traditional premium montage?
- Does the ending create a full brand mnemonic rather than only a silent logo card?
- Are there cultural, representation, claim, or AI-authenticity risks?
