---
name: story-commerce-video-remix
description: >-
  Create narrative commerce short-video concepts focused on 狗血/霸总/绿茶/小三/宫斗/反转/重生 and creative micro-drama containers such as 古装错位、恋综、审判、末日、科幻、时间循环. After picking one genre direction, outputs a Seedance 2.0-ready 15-second video_generation_prompt with 3-4 timestamped shots, global visual direction, distinct subject character design, product-name dialogue exposure, director-style beat fields ordered as 拍法/画面内容/商品露出/声音, and hard constraints for product consistency, package text stability, quantity/state continuity, physical interaction causality, and correct opening/tearing/clicking method based on the real package structure. Also supports calling pippit_omni_search with type marketing_hotpoint to search hotspot creative content from the user's original request and user images, then runs hotspot SP/product matching, hot-video core-play remix, and remixed-SP scoring when suitable content is returned while preserving product/package consistency. Use when the user wants 短剧风创意带货, 剧情向带货短视频, 短剧爽感, 三秒hook, 爆款开头, 商品推广创意, 带货脚本, 分镜提示词, Seedance提示词, 热点remix, 热点融合, SP评估, 商品一致性约束, 包装/字迹稳定, 撕开/打开动作约束, product-led story ads, or a reusable thinking framework that maps audience, emotion, conflict, camera, pacing, sound, and product proof into a shootable conversion video.
---

# 短剧风创意带货

## Top-Level Routing: Hotspot Search First

This routing rule has highest priority for product-led video generation.

1. First determine whether the user has explicitly provided a complete detailed script.
   - Complete detailed script means the user-provided input already contains enough story/script details, including beginning, development, turn, ending, time rhythm, characters, product/USP, and visual details.
   - If the user has provided a complete detailed script, skip `pippit_omni_search` and process it with the original story-commerce-video PE workflow.
2. If the user has not provided a complete detailed script, call `pippit_omni_search` before creating any script, creative plan, Seedance prompt, or story route.
   - Pass the product information and/or user image(s) provided by the user directly to `pippit_omni_search`; the tool will handle any query normalization.
   - If both product information and image(s) are available, pass both.
   - If only product information is available, pass the product information.
   - If only image(s) are available, pass the image(s).
   - If either product-information retrieval or image-based retrieval returns usable hotspot candidates, continue to scoring and Remix candidate selection.
   - The call to this tool's interface must include `type: marketing_hotpoint`.
   - Only `pippit_omni_search` is valid for hotspot retrieval. Do not use generic web search, 联网搜索, browser search, search engines, or any other retrieval tool as a substitute.
   - If `pippit_omni_search` is not callable in the current environment, do not attempt hotspot retrieval with another tool; fall back to the original story-commerce-video PE workflow.
   - Do not pass a preset script, generated story, draft creative plan, route label, fallback explanation, or any already-written plot into `pippit_omni_search`; doing so pollutes the hotspot search.
   - Call `pippit_omni_search` at most once per user request. Do not search again after scoring candidates.
3. How to use `pippit_omni_search`: `Query`: the user’s original creative request, product analysis, selling points, etc.; `SearchType`: fixed as `marketing_hotpoint`; `ImageList`: user-provided image asset, used to retrieve relevant product hotspot videos.
4. If `pippit_omni_search` returns no creative content, no usable hotspot/SP, irrelevant candidates, or fewer than one usable candidate, fall back to the original story-commerce-video PE workflow and generate the normal剧情创意方案.
5. If `pippit_omni_search` returns hotspot videos, expect up to 3 candidate hotspot videos. For each usable candidate, run the scoring flow in `references/hotspot-remix-evaluation.md` with `score_hot_product_match_spv1`.
   - For scoring only, first create a concise `改写后的SP` concept that shows how this hotspot could fuse with the product USP.
   - Score each candidate with `creativity_score` and `usp_score`.
   - Rank by `creativity_score + usp_score`; if tied, prefer higher `usp_score`; if still tied, prefer higher heat and clearer core play pattern.
6. Select only the highest-scoring hotspot video and use the Hotspot Remix PE on that selected video to output the final creative方案/script.
   - If any candidate has already been scored in the current request, reuse the existing score and selected candidate; do not rescore from scratch unless the user changes the product, USP, image, or hotspot candidates.
   - If a candidate receives a 5 in either dimension, preserve that score in ranking and do not later reject it by describing the hotspot style as mismatched.
   - Do not replace the selected hotspot's original SP/core play pattern with a broad style label such as `卡通风`, `治愈类`, or `轻松向`. Style labels may be noted, but the Remix must be based on the selected hotspot video's concrete SP and core play pattern.
7. Do not use an additional fit gate to reject the highest-scoring candidate after scoring. The scoring PE is the candidate-selection mechanism.

Route summary:

```text
用户提供完整详细脚本 -> 跳过 pippit_omni_search -> 原 story-commerce-video PE
未提供完整详细脚本 -> 产品信息和/或用户图片 -> 调用 pippit_omni_search，接口参数 type: marketing_hotpoint
pippit_omni_search 返回3个热点视频 -> score_hot_product_match_spv1逐个评分 -> 选择总分最高的1个 -> 热点Remix PE输出脚本创意
pippit_omni_search 无可用热点/候选明显不可用 -> 原 story-commerce-video PE 输出剧情创意方案
```

## Core Principle

Do not start from product features. Start from the likely buyer's content taste and short-drama appetite: what kind of story does this audience already watch, what relationship pressure keeps them watching, and what kind of reversal feels satisfying to them. Then make the product the decisive proof inside that genre's payoff.

The durable engine is:

**product category -> likely TA -> short-drama genre fit -> genre-specific audience fantasy -> relationship pressure -> 3-second abnormal hook -> escalating conflict -> product as plot function -> visible proof -> emotional payoff -> conversion line**

The product should not feel inserted. It should explain, reverse, or prove the story. A good story-commerce idea passes this test: **without this product, the protagonist cannot win in this exact way; but the audience should not feel the product pitch before the story has created pressure.**

This skill is category-agnostic. Apply it to physical goods, apps, AI tools, local services, courses, consumer electronics, beauty products, food, health products, home goods, B2B software, IP merchandise, travel products, or offline retail. Change the proof form and conflict setting to fit the category instead of defaulting to software screens or creator workflows.

## Execution Gate: Required Reference Loading

Before generating any answer, decide the task type and load the required references. Do not draft the final answer until the required files below have been read.

This loading policy is mandatory and should be followed before the later fast checklists in `SKILL.md`. The checklists are memory aids after loading references, not replacements for reading the reference files.

### Story-Commerce Route Selection

If the user asks for 创意, 带货脚本, 剧情向短视频, 短剧风, 分镜, 商品推广创意, multiple routes, product-led story ads, or any concept generation:

1. Read `/workspace/.skills/story-commerce-video-remix/references/genre-routing.md`（需要时使用 sandbox_read 工具读取） before choosing the route.

### Hotspot Remix / SP Evaluation

If the task is a product-led video request, or if the user provides or asks about 原视频脚本, 原始视频SP, 热点视频, 热点内容, 核心玩法/梗内核, remix, 热点融合, SP评估, or hotspot/product fit:

1. Read `/workspace/.skills/story-commerce-video-remix/references/hotspot-remix-evaluation.md`（需要时使用 sandbox_read 工具读取） before rewriting, scoring, or deciding whether the hotspot can carry the product.
2. If the user has explicitly provided a complete detailed script, skip `pippit_omni_search` and use the original story-commerce-video PE workflow.
3. If the user has not provided a complete detailed script, call `pippit_omni_search` first using the product information and/or the user's image(s) from the original user request. The call to this tool's interface must include the parameter `type: marketing_hotpoint`.
   - Product-information retrieval and image-based retrieval are both valid. If either returns usable hotspot candidates, continue to scoring and Remix candidate selection.
   - If both image(s) and product information are available, pass both; if only one is available, pass that one.
   - Do not manually simplify, rewrite, expand, or filter the product query before calling the tool; `pippit_omni_search` handles query processing.
4. Only `pippit_omni_search` is valid for hotspot retrieval. Do not use generic web search, 联网搜索, browser search, search engines, or any other retrieval tool as a substitute. If `pippit_omni_search` is not callable, skip hotspot retrieval and fall back to the original story-commerce-video route.
5. Do not pass a preset script, generated story, draft creative plan, route label, fallback explanation, or any already-written plot into `pippit_omni_search`.
6. If `pippit_omni_search` returns no creative content, no usable original SP, or only irrelevant/low-confidence candidates, fall back to the original story-commerce-video route.
7. If `pippit_omni_search` returns hotspot videos, evaluate each usable candidate with `score_hot_product_match_spv1` before remixing. The tool commonly returns 3 hotspot videos; score all 3 when all are usable.
8. For each candidate, extract `原视频脚本/原始视频SP`, `视频当前热度`, `核心玩法/梗内核`, `营销商品名称`, `商品核心卖点（USP）`, and `商品图片描述` when present. Create a concise `改写后的SP` concept for scoring only, then output that candidate's score as strict JSON internally.
9. Select only the highest-scoring candidate by `creativity_score + usp_score`; tie-break by higher `usp_score`, then higher heat/core-play clarity. Reuse candidate scores already produced in the current request and do not call `pippit_omni_search` again after scoring.
10. Apply the route: `pippit_omni_search返回3个热点视频 -> score_hot_product_match_spv1逐个评分 -> 最高分1个热点视频 -> 热点Remix`; `pippit_omni_search未返回创意/候选明显不可用 -> original story-commerce-video product-led generation`.
11. The skill itself should not output baseline-vs-enhanced experiment comparisons; online traffic splitting and comparison are handled outside the skill.
12. If the user only asks for remix rewriting and the hotspot is OK, directly output the rewritten pure-text script and do not append analysis, evaluation, or Markdown.
13. If the user asks for evaluation/scoring, output strict JSON only as defined in `hotspot-remix-evaluation.md`.

### Final Video Prompt / Seedance Output

If the final answer will include `video_generation_prompt`, Seedance prompt, 视频生成提示词, 分镜提示词, 开拍提示词, production-ready prompt, or any paste-ready video model prompt, even if the user did not explicitly say "Seedance":

1. Read `/workspace/.skills/story-commerce-video-remix/references/seedance-prompt-writing.md`（需要时使用 sandbox_read 工具读取） before writing the final prompt.

Hard rule: if `video_generation_prompt` appears in the final output, `seedance-prompt-writing.md` must have been read in this turn.

### Compact Creative Plan Output

If the answer should create a standalone creative plan markdown, or if the task is a concrete product-led creative concept, story-commerce script, plot-led short video, storyboard prompt, or Seedance video-generation prompt and the user has not opted out of file creation:

1. Read `/workspace/.skills/story-commerce-video-remix/references/compact-spec-output.md`（需要时使用 sandbox_read 工具读取） before writing the plan file.

### Review / Critique Tasks

If the user asks whether a script or prompt meets requirements, asks for review, or asks if something is compliant:

1. Read `/workspace/.skills/story-commerce-video-remix/references/critique-checklist.md`（需要时使用 sandbox_read 工具读取） before answering.

### Category Grounding

For any concrete product, after loading the route and Seedance references needed for the task, load exactly one category reference that matches the product's primary buying context. Do not load every category file.

### Final Self-Check

Before the final response, verify:

- `genre-routing.md` was used for route choice when the task involved story-commerce generation.
- `hotspot-remix-evaluation.md` was used when the task involved hotspot SP, core play pattern, remix, or hotspot/product scoring.
- Hotspot routing followed the fused gate: `用户提供完整详细脚本 -> 原PE`; `未提供完整详细脚本 -> 产品信息和/或用户图片 -> pippit_omni_search(type: marketing_hotpoint)`; `产品信息或图片任一路有可用热点 -> score_hot_product_match_spv1逐个评分 -> 最高分1个 -> Remix PE输出脚本创意`; `产品信息和图片均无可用热点/候选明显不可用 -> original story-commerce剧情创意方案`.
- `seedance-prompt-writing.md` was used if a video prompt is included.
- If a Chinese `video_generation_prompt` is included, it starts with `时长：15秒，比例：9:16。`
- The prompt contains 3-4 timestamped shots by default for 15-second output.
- Each beat uses `拍法` / `画面内容` / `声音`, and only uses `商品露出` when the product is actually visible in that beat.
- The prompt or remix script includes a hard `产品一致性` constraint: the same product keeps identical package text, logo position, color, shape, material, cap/lid, bottle/box form, quantity, size ratio, and visible USP across every shot.
- The prompt or remix script includes a hard `交互物理约束`: every product movement is caused by a visible hand/body/tool/surface action; products cannot float, teleport, appear/disappear without cause, stand upright automatically, open by themselves, pour/spill from a sealed package, or change state between shots without an onscreen action.
- Hotspot remix preserves the selected hotspot's interaction logic only when it can obey product consistency and physical interaction rules. Never keep a viral gag by making the product change SKU, packaging, text, quantity, or physical state impossibly.
- The final prompt does not reuse example products, sample character details, sample dialogue, sample visual references, or bracketed placeholders from any reference file.
- Hotspot remix outputs preserve the original script's pure-text narrative format, include timeline details for multiple shots, keep total duration within 5-15 seconds, explicitly show the product/product image, and mention the product name.

## Product Consistency And Interaction Hard Gate

Before writing any final script, hotspot remix, or `video_generation_prompt`, lock a single `产品1` specification. Treat this as a hard contract, not a creative suggestion:

- **Packaging text lock**: exact brand/product name, major front-label words, logo position, readable text direction, and any visible typography must stay the same. Never invent similar-looking Chinese/English text, wrong characters, or alternate labels.
- **Appearance lock**: package form, color blocks, pattern, material, cap/lid, box/bottle/bag shape, opening position, and size ratio to the hand/body/table must stay consistent across all shots.
- **Reference-visible lock**: only use surfaces and contents visible in the user's reference images. If only the front is shown, keep product shots front-facing or 3/4 front-facing and do not invent back labels, side panels, ingredients, barcode, internal trays, inner bags, liquids, powders, food pieces, accessories, or package contents.
- **Selling-point source lock**: only use selling points explicitly provided by the user, visible front-package text, product title/listing text, hotspot-returned product fields, or other user-provided source material. Do not infer ingredients, formula, certification, flavor, capacity, specification, efficacy, origin, awards, health/beauty claims, or back-label information from category alone.
- **Script-fit lock**: adapt the hotspot remix to the real known selling points and visible product information. If the selected hotspot requires unsupported visual proof, change the proof method while preserving the core play pattern rather than inventing product appearance, package content, label text, ingredients, or internal structure.
- **Quantity lock**: the number of visible product units cannot change unless a shot explicitly shows a person adding/removing a unit. No `2 boxes become 3`, no bottle/box switching, no product transforming into another SKU.
- **State lock**: sealed/opened/poured/worn/clicked/used states must follow visible cause and effect. If a product is unopened in one shot and open in the next, show the hand opening it or keep it unopened.
- **Opening-method lock**: identify the real package opening structure before scripting: screw cap, flip cap, pull tab, tear notch, zip seal, box flap, shrink film, pump head, sachet edge, can ring, or app click path. Use only the matching open action for that structure.
- **Required-open lock**: if the product proof depends on inside content, pouring, eating, applying, taking out, using, or showing the opened package, include a close hand-action shot where the package is actually opened before the proof. Do not skip the opening beat.
- **Commerce truth lock**: the product shown in the video must match the product described by the user or reference image in shape, flavor/color/spec, package type, and usage scene. If uncertain, describe fewer anchors rather than inventing wrong ones.

Interaction constraints are equally mandatory:

- A visible actor, hand, tool, surface, gravity, or contact point must cause every product motion.
- Products cannot hover in midair, pop into frame, vanish, auto-stand, auto-open, auto-pour, or move while nobody touches them.
- Opening/tearing/pouring/clicking/applying/wearing actions must specify the actor's hand, grip, direction, contact point, and visible endpoint.
- Match the opening action to the package structure: twist screw caps, lift flip caps, pull can rings, tear along notches, peel sealing films, unfold box flaps, slide zip seals, press pump heads, or tap/click app controls. Do not tear a rigid box, unscrew a sachet, pull a ring from a bottle without a ring, or pour from a package that has not been opened.
- After opening, maintain the opened state in later shots: cap removed or flipped, seal broken, flap open, tear edge visible, pump pressed, or app page changed.
- Prefer low-risk alternatives to tearing/opening actions when the reference image does not clearly show the package structure or contents: already-opened but content-hidden package, exterior package display, hand placing the product, user reaction, result shot, or product-name dialogue.
- For AB or before/after comparisons, define a separate `对照产品A` or `错误选择A` with different visual anchors. Do not compare `产品1` against another copy of `产品1`.
- When a selling point cannot be visually proven from provided assets, express it as a user-perception line, scene fit, product-name dialogue, or neutral result shot. Do not create a fake package back, ingredient table, side label, cutaway, internal content, or lab-test image to prove it.
- The product should not be pulled from impossible places such as mouth, clothing, cake, drawer, or pocket unless that exact storage is plausible for the product size and was visually established.
- Do not use physically impossible proof such as liquid emerging from a sealed box, a hard box folding like cloth, a bottle becoming a sachet, or a package instantly repairing itself.

If any of these gates fail, rewrite the prompt or remix script instead of adding an explanation.

## Continuous Mindshare, Not One-Off Ads

Short-drama commerce is usually stronger as a **series mindshare system** than as a single ad. A one-off video can create traffic, but a repeated short-drama pattern can teach the audience one product meaning over time.

Before writing a concept, decide the repeatable product symbol or mental hook the series should build. Examples:

- A skincare gift set becomes "the proof that she is cared for and ready to face bias."
- A work tool becomes "the quiet weapon that helps her win every deadline."
- A swim dress becomes "the swimsuit she does not need to keep covering."

Then design multiple story situations around the same mental hook. The plots can vary, but the product meaning should stay stable. This is how short-drama commerce compounds:

**single product focus -> repeated audience pressure -> varied short-drama scenes -> same product proof -> same value sentence -> live room/cart conversion**

Do not treat each script as an isolated commercial. When the product has enough scene potential, propose a series arc or 3-5 repeatable episodes that reinforce the same mental association. Each episode should create a new conflict, but the audience should remember the same product phrase after every video.

Good series mindshare is specific:

- "Han Shu = anti-aging red gift set" is stronger than "a skincare brand."
- "A swimsuit she does not need to keep covering" is stronger than "a pretty swimsuit."
- "One person can finish the urgent delivery" is stronger than "an efficient app."

Avoid scattering the brand across too many products, emotions, and plot meanings in the same campaign. Short-drama traffic converts best when viewers only need to remember one product, one pressure, and one reason to buy now.

## Input Diagnosis

Before writing ideas, identify:

- **Product truth**: the smallest concrete value the product can prove on screen.
- **Audience segment**: who most wants this value now, not the broad market.
- **Series mindshare**: whether this should be a single concept or a repeatable short-drama series, and what exact product phrase the audience should remember across episodes.
- **Short-drama audience fit**: what genre this TA likely enjoys, such as 女频逆袭, 男频逆袭, 甜宠, 霸道总裁, 重生复仇, 赘婿/战神, 家庭伦理, 职场爽剧, 悬疑反转, or comedy misunderstanding.
- **Genre fantasy**: what the audience wants to feel in that genre: being chosen, being protected, being vindicated, making money, returning stronger, exposing hypocrisy, repairing family misunderstanding, or winning professional respect.
- **Oppression or misunderstanding relationship**: who pressures or misreads the protagonist: boss, ex, mother-in-law, spouse, relatives, classmate, competitor, customer, coach, friend, neighbor, or public crowd.
- **Product plot function**: whether the product is the reversal evidence, status signal, caring gift, secret weapon, wrong-choice correction, hidden identity clue, family-care proof, efficiency weapon, or final reveal key.
- **Subject character design**: define each important person as a visually distinct role, not a generic gender/age label. Include face shape, hairstyle silhouette, outfit texture/color, posture, expression habit, role-coded styling, and one memorable visual anchor that separates `主体1` from `反派1` and bystanders.
- **Aesthetic and trend context**: only when relevant, identify what styling fear, taste anxiety, or social comparison this product can resolve inside the story.
- **Emotional button**: anxiety, easy money, dream fulfillment, social proof, professional confidence, revenge, belonging, beauty/status, safety, care, convenience.
- **Viewing context**: platform, length, language, creator identity, budget, and whether the video needs to connect to live room, cart, coupon, or series follow-up.
- **Dog-blood opening device**: the first-3-second melodramatic event that can stop scrolling: public accusation, betrayal hint, family pressure, love-rival provocation, boss humiliation, identity misread, embarrassing exposure, or absurd misunderstanding.
- **Proof form**: before/after, saved time, generated output, physical transformation, social reaction, money/order result, expert approval, role fantasy becoming visible.
- **Genre stance**: short-drama revenge, workplace conflict, romance/family misunderstanding, family recognition, social comparison, hidden identity, or delayed reveal.
- **Category behavior**: how this product is actually bought, used, displayed, trusted, shared, or recommended.

For fashion, beauty, shoes, accessories, home, food, travel, and other taste-led categories, do not jump directly from product type to a generic story. First infer the product's social pressure role:

- Who wants to be seen using it, and what identity, confidence, or status does it signal?
- What situation makes the audience afraid of being judged, compared, exposed, or embarrassed?
- What adjacent brands, outfits, scenes, creators, or reference images would the audience recognize?
- Is the product mainstream, quietly premium, nostalgic, functional, playful, technical, ugly-cute, minimal, status-coded, or anti-status?
- What would the audience be afraid of looking like if styled badly?
- For wine, premium beverages, banquet gifts, and other social-taste products, wardrobe is part of the reversal proof. Do not default the protagonist to plain homewear when the plot is about face, gifting, hospitality, or being judged at a table. Dress the protagonist in restrained but occasion-ready styling, such as a black tailored dress with a burgundy silk top, a wine-red satin blouse with a black high-waist skirt, subtle pearl or gold accessories, and clean makeup. The outfit should signal "quietly prepared and tasteful" without overpowering the product.

If the user gives little context, make a reasonable assumption and state it briefly. Do not block on questions unless the product, audience, or platform is unknowable.

## Priority Genre Focus

When choosing the short-drama direction, prioritize the following high-engagement genre types. These are the core emotional engines of short-drama commerce:

| Priority genre | Core hook | Typical antagonist | Audience fantasy |
|---|---|---|---|
| **狗血** | Extreme betrayal, public humiliation, family scandal, absurd injustice | Ex, best friend, family member, boss | Emotional catharsis, justice, dramatic reversal |
| **霸总** | Cold/powerful man meets underestimated woman, identity gap, contract relationship | Love rival, scheming secretary, disapproving family | Being chosen, protected, elevated by someone powerful |
| **绿茶** | Two-faced antagonist pretends innocent while scheming; protagonist exposes her | Green-tea rival (friend, colleague, sister-in-law) | Seeing through fake people, exposing hypocrisy |
| **小三** | Third party intrudes; protagonist fights back or gets sweet revenge | The other woman/man, the cheating partner | Dignity, self-worth, decisive revenge or graceful exit |
| **宫斗** | Power hierarchy, alliance and betrayal, strategic maneuvering in group dynamics | Senior wife, scheming colleague, mother-in-law, social queen | Outsmarting enemies, rising through strategy |
| **反转** | Audience is led to believe one thing; truth is the opposite at the end | Misread protagonist, false accusation, hidden identity | Surprise, satisfaction, "I didn't see that coming" |
| **重生** | Protagonist gets a second chance; avoids past mistakes, preemptively defeats enemies | Former betrayers, bad choices, ignorant past self | Foresight, revenge, correcting regrets, smarter choices |

**Rule**: After diagnosing the product and TA, pick ONE primary genre from the above list. Do not blend multiple genres weakly. One genre, one clear emotional engine, one reversal type. The product must serve as the key prop in that genre's specific payoff.

## Short-Drama Genre Routing

Before scripting, choose one primary short-drama genre and one selling mode. Keep the product as the decisive plot proof, not a generic sponsor prop.

Follow `Execution Gate: Required Reference Loading` before route selection. The fast route selector below is only a memory aid after reading `genre-routing.md`, not a replacement.

Fast route selector:

- Visible beauty, style, taste, or social perception improvement -> use 女频逆袭 / public reversal.
- Giftable, intimate, comforting, or care-signaling product -> use 甜宠 / relationship recognition.
- Time-saving, mistake-preventing, output-improving product -> use 职场爽剧 / deadline competence win.
- Hidden daily problem causing awkward behavior -> use misunderstanding reveal.
- Corrects a bad choice, regret, cheap substitute, or outdated method -> use 重生 / wrong-choice correction.
- Status-coded object -> use hidden identity, social flex, or public recognition.

Satisfying reversal requirements:

- Clear antagonist or hostile witness.
- Immediate stakes: public respect, deadline, relationship pressure, money, face, or status.
- Product-enabled proof that answers the antagonist's exact wrong judgment.
- Payoff happens in front of the person who misjudged the protagonist.

Product-to-drama check before writing:

1. Which genre does this target audience already enjoy?
2. What exact pressure line opens the first 3 seconds?
3. Who misjudges, humiliates, doubts, or tests the protagonist?
4. What hidden choice does the protagonist make?
5. What visible product proof makes the antagonist change their mind?
6. What conversion sentence naturally follows the payoff?

## Output Format

**Compact creative-plan rule**: for concrete product-led creative concepts, story-commerce scripts, plot-led short videos, storyboard prompts, or Seedance video-generation prompts, follow `Execution Gate: Required Reference Loading`, then create a readable standalone complete creative plan markdown file by default, unless the user explicitly asks for a fast prompt, chat-only answer, no file creation, or strategy-only guidance. Before the final chat response, write the complete plan with `sandbox_write` to the designated output path defined in `compact-spec-output.md`. Follow the file naming rules from `compact-spec-output.md`; do not define a separate naming scheme in `SKILL.md`. Do not merely mention a path in chat without writing the file. When mentioning the written plan in chat, use the Markdown-link format defined in `compact-spec-output.md`, such as `[完整创意方案]({absolute_path})`, rather than a bare path. Do not weaken the final Seedance 2.0 prompt to make the chat shorter. Move reasoning detail into the plan file; keep the conversation focused on the selected route, the plan markdown link actually written, and the paste-ready `video_generation_prompt`.

**Language consistency rule**: match the user's primary language for the chat response, spec, and final prompt unless the target market requires another language or the user explicitly requests another language. For Chinese requests, use Chinese field labels and Chinese dialogue by default. Keep only product names, brand names, platform names, and model names in their original language. Avoid mixed labels such as `Product`, `Script beats`, `Visual baseline`, or `Product proof` inside an otherwise Chinese deliverable.

When delivering a concept, use this format unless the user asks otherwise:

```text
产品：
目标人群：
内容路线：
戏剧类型：
一句话创意：
3秒钩子：
产品剧情功能：
可见证明：
转化句：

video_generation_prompt:
```

Use the longer legacy field set only inside the standalone spec markdown or when the user explicitly asks to see full reasoning in the conversation.

For multiple routes, output 3-6 distinct concepts. Vary the short-drama genre, creative container, audience, visual reference, and product plot function rather than writing small wording variations of the same idea.

## Seedance 2.0 Prompt Writing

Default deliverable is one pasteable `video_generation_prompt` after one genre direction is selected. Whenever this skill produces a final `video_generation_prompt`, the Seedance reference is mandatory, regardless of whether the user explicitly mentions Seedance.

When compact spec mode is used, the final prompt remains full quality and self-contained. The chat may be short, but the prompt must still include enough production detail for Seedance 2.0 to generate the video without reading the separate spec.

Follow `Execution Gate: Required Reference Loading` before writing the final prompt. The compact standard below is only a quick checklist after reading `seedance-prompt-writing.md`.

Required compact standard:

- Start Chinese prompts with `时长：15秒，比例：9:16。`
- State task type: generate, reference, edit, extend, or stitch.
- For cinematic or reference-heavy prompts, write the global setup before the beat list in this order: `标题 -> 视觉基调 -> 画面风格 -> 主题与情绪 -> 色彩与色调 -> 光影设计 -> 拍摄设备/镜头语言 -> 声音 -> 关键元素 -> 场景 -> 分镜`.
- Bind product, protagonist, antagonist, and scene with stable labels such as `产品1`, `主体1`, `反派1`.
- Immediately after binding `产品1`, add a `产品一致性` sentence that freezes its text, logo, package form, color, cap/lid, quantity, size ratio, and state continuity across all shots.
- Add a `交互物理约束` sentence before the shot list: all product movements must be caused by visible hands/tools/surfaces; no floating, teleporting, auto-opening, auto-standing, auto-pouring, or unexplained disappearance.
- Give each recurring character a distinct visual design: face shape, hairstyle silhouette, outfit, posture, expression habit, and one memorable anchor. Avoid generic prompts like `年轻女性，黑色长发`.
- Include a concrete visual reference anchor and specify borrowed dimensions: lighting, lens, costume, production design, pacing, mood, or composition.
- For 15s prompts, output only 3-4 timestamped shots by default. Do not split into 5-6 micro-beats. Prefer this compact pacing: `0-3秒` abnormal hook + relationship pressure, `3-7秒` protagonist choice + product/ability activation, `7-12秒` main visible proof escalation, `12-15秒` payoff and product-name conversion line. If the story is extremely simple, combine the last two into a 3-shot structure; if product operation needs clarity, keep all 4 shots.
- Every beat must start with `拍法`, then write `画面内容`, optional `商品露出`, and `声音`. `拍法` must explain shot size, angle, composition, camera position, and camera movement before describing the story content. The visible proof or payoff must be written directly inside `画面内容`, not as a separate result field.
- Only write `商品露出` when the product is actually visible, used, handed over, worn, opened, clicked, or otherwise present in that exact beat. If the product does not appear in the shot, omit the `商品露出` line entirely. Do not describe absent, hidden, upcoming, or off-screen product details inside a beat.
- `拍法` cannot stop at `近景` or `大全景`; it must say how to shoot: front/side/back angle, high/low/eye-level camera, handheld/fixed/tracking/push-in/pull-back, foreground/background relation, and whether the camera follows the subject.
- Spoken lines use `{}`, music uses `（）`, sound effects use `<>`.
- Product proof must be visible before the conversion line.
- The script dialogue or voiceover must explicitly say the product name at least once, preferably in the final conversion line. Do not rely only on package text or the `商品露出` field for product-name exposure.
- Avoid medical/financial/health overclaims and avoid vague proof such as only saying the protagonist is confident.
- Treat examples and templates in the Seedance reference as structure only. Replace every sample-like detail with content grounded in the user's product, audience, category, and chosen route before output.

## Critique Checklist

Follow `Execution Gate: Required Reference Loading` for review tasks. Review for: audience specificity, genre fit, 3-second hook, pressure relationship, product plot function, visible proof, witness reaction, Seedance field completeness, and claim safety.

## Category References

**Mandatory category loading**: for any concrete product, follow `Execution Gate: Required Reference Loading` and load exactly the reference that matches the product category after reading the genre/Seedance references needed for the task. Use the SKILL.md workflow first, then pull category-specific proof forms, conflicts, and examples from these files:

- **Physical consumer goods / home goods / cleaning**: `/workspace/.skills/story-commerce-video-remix/references/physical-goods.md`（需要时使用 sandbox_read 工具读取）
- **Food and beverage**: `/workspace/.skills/story-commerce-video-remix/references/food-beverage.md`（需要时使用 sandbox_read 工具读取）
- **Beauty and personal care**: `/workspace/.skills/story-commerce-video-remix/references/beauty-personal-care.md`（需要时使用 sandbox_read 工具读取）
- **Fashion / shoes / accessories / lifestyle**: `/workspace/.skills/story-commerce-video-remix/references/fashion-lifestyle.md`（需要时使用 sandbox_read 工具读取）
- **Services / courses / local business**: `/workspace/.skills/story-commerce-video-remix/references/services-courses.md`（需要时使用 sandbox_read 工具读取）
- **Apps / software / AI tools**: `/workspace/.skills/story-commerce-video-remix/references/software-ai-tools.md`（需要时使用 sandbox_read 工具读取）
- **B2B / enterprise / high-consideration products**: `/workspace/.skills/story-commerce-video-remix/references/b2b-enterprise.md`（需要时使用 sandbox_read 工具读取）

If a product spans multiple categories, load the primary buying context first. Example: an AI design course is usually **services/courses** if the user is buying learning outcomes, but **software/AI tools** if the user is promoting the tool itself.

Do not reuse all routes in one video. Choose the route that best matches the category, audience, and strongest proof.
