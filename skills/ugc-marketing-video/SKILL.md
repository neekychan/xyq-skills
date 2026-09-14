---
name: ugc-marketing-video
display_name: UGC营销带货视频
description: Create domestic UGC marketing video workflows for Douyin, Kuaishou, Xiaohongshu, WeChat, and related short-video generation tools. Use when the user needs UGC带货, 种草, 口播, 好物推荐, 产品测评, 卖点展示, 效果展示, 达人探店, 团购/本地生活转化, 游戏/IP活动转化, 爆款复刻, reference-video adaptation, sales-script-to-video, product-led conversion ads, meme/visual hooks, a Nano Banana Pro creator portrait, a concise user-facing script, or a detailed Seedance/video-generation-tool payload from product text, images, links, scripts, CTAs, offers, or reference videos.
tools: ["sandbox_generate_image", "sandbox_generate_video", "sandbox_generate_audio", "render_video", "sandbox_process_video"]
---

# UGC Marketing Video

Turn product information, images, links, offers, scripts, CTAs, or reference videos into a domestic UGC marketing chain: product understanding -> Nano Banana Pro generates or revises the creator portrait through `sandbox_generate_image` -> user can adjust the creator image -> the skill writes the concise script -> all relevant reference rules are compiled into an internal `seedance_generation_package` -> Seedance/video generation uses the user product materials and creator portrait as reference/垫图.

This is the self-writing version. Do not call `ugc_idea_generator`. Creator portrait generation uses Nano Banana Pro through `sandbox_generate_image`.

Keep the chat lightweight, but do not skip references. This skill is a routing hub; detailed behavior lives in bundled `references/`. In the hosted workspace, reference files must be addressed through `/workspace/.skills/ugc-marketing-video/references/...` and read with `sandbox_read`.

## Mandatory Reference Loading

Before writing the user-facing script or compiling the internal `seedance_generation_package`, read the references needed for the task. Use `sandbox_read` with the workspace-form paths shown below. Do not replace these with local machine paths, relative markdown links, or `/tmp` paths.

Minimum required references for every final script and internal generation package:

1. Use `sandbox_read` to read `/workspace/.skills/ugc-marketing-video/references/output-spec.md`
2. Use `sandbox_read` to read `/workspace/.skills/ugc-marketing-video/references/interaction-flow.md`
3. Use `sandbox_read` to read `/workspace/.skills/ugc-marketing-video/references/input-consistency-rules.md`
4. Use `sandbox_read` to read `/workspace/.skills/ugc-marketing-video/references/production-scenarios.md`
5. Use `sandbox_read` to read `/workspace/.skills/ugc-marketing-video/references/creative-strategy-focus.md`
6. Use `sandbox_read` to read `/workspace/.skills/ugc-marketing-video/references/creative-type-library.md`
7. Use `sandbox_read` to read `/workspace/.skills/ugc-marketing-video/references/creator-persona-library.md`
8. Use `sandbox_read` to read `/workspace/.skills/ugc-marketing-video/references/hook-library.md`
9. Use `sandbox_read` to read `/workspace/.skills/ugc-marketing-video/references/benefit-voiceover-library.md`
10. Use `sandbox_read` to read `/workspace/.skills/ugc-marketing-video/references/cta-library.md`
11. Use `sandbox_read` to read `/workspace/.skills/ugc-marketing-video/references/marketing-expression-rules.md`
12. Use `sandbox_read` to read `/workspace/.skills/ugc-marketing-video/references/text-accuracy-rules.md`
13. Use `sandbox_read` to read `/workspace/.skills/ugc-marketing-video/references/performance-rules.md`
14. Use `sandbox_read` to read `/workspace/.skills/ugc-marketing-video/references/seedance-prompt-rules.md`
15. Use `sandbox_read` to read `/workspace/.skills/ugc-marketing-video/references/quality-checklist.md`
16. Use `sandbox_read` to read `/workspace/.skills/ugc-marketing-video/references/portrait-image-rules.md`
17. Use `sandbox_read` to read `/workspace/.skills/ugc-marketing-video/references/seedance-generation-contract.md`

Conditional required references:

- Use `sandbox_read` to read `/workspace/.skills/ugc-marketing-video/references/category-strategy.md` when a concrete product category, buyer, usage scene, proof form, offer, or CTA matters.
- Use `sandbox_read` to read `/workspace/.skills/ugc-marketing-video/references/platform-rules.md` when a platform is specified or platform behavior affects format, pacing, CTA, or text placement.
- Use `sandbox_read` to read `/workspace/.skills/ugc-marketing-video/references/diversity-rules.md` when generating multiple versions, variants, or repeated revisions.

Do not write the final script or compile the generation package until these references have been read. Keep reference reading internal; do not tell the user which files were read unless they ask.

## Workflow

1. Parse all user inputs: product text, title, image, link, script, video, offer, target platform, CTA, and follow-up instructions. Apply `input-consistency-rules.md` to create a single product identity before generation.
2. Classify the production scenario using `production-scenarios.md`:
   - new video from product content
   - video from fixed script
   - viral/reference remake
3. Choose one primary creative focus using `creative-strategy-focus.md` and the relevant templates in `creative-type-library.md`.
4. Use category and platform references when relevant.
5. Choose a product-matched creator persona using `creator-persona-library.md`. Bind age band, role, appearance, scene, product relationship, and speaking tone before image generation.
6. Generate or bind the creator portrait before script writing using `portrait-image-rules.md`:
   - First classify uploaded materials into product/reference assets and person/model/creator assets.
   - If the user supplied a suitable person/model/creator reference image, bind that uploaded image as `creator_portrait_image`; preserve visible identity cues and do not call `sandbox_generate_image` unless the user asks to replace or adjust the person.
   - If the user supplied only product images, screenshots, packaging images, links, or non-person reference materials, treat that as no suitable person image.
   - If no suitable person image is supplied and `sandbox_generate_image` is available, internally build the full high-quality creator-image prompt described in `portrait-image-rules.md`. **Mandatory model routing**: prepend `[Model: chatgpt-image-2]` to the very beginning of the Prompt parameter (before any visual description) to ensure the backend routes to the correct image generation model; do not omit this prefix or place it elsewhere in the prompt. Pass that complete prompt (with the model prefix) into `sandbox_generate_image`. Do not expose the internal prompt or the model prefix to the user.
   - Default to a 4:5 high-realism native UGC creator portrait. Keep phone-shot texture, but do not make the creator visibly hold a phone by default; visible phones are only props, not persistent downstream video actions.
   - Use a deterministic `output_path` under `/workspace/出镜达人/`, such as `/workspace/出镜达人/creator_portrait_subject_1.png`. Ensure the directory exists via `sandbox_bash` (e.g. `mkdir -p /workspace/出镜达人`) before generating.
   - Show the generated or supplied creator portrait by calling `present_sandbox_file` with the portrait filepath, accompanied by a compact Chinese `creator_image_caption` and `product_consistency_note`. If the user asks to adjust the portrait, call `sandbox_generate_image` again with the revised prompt (also prepended with `[Model: chatgpt-image-2]`) and use the latest accepted portrait for later steps.
7. Generate a concise 15-second sales script after the active creator portrait is selected:
   - Choose the 0-3s hook from `hook-library.md`; the hook must include visible product entry and connect back to proof by 3-7s.
   - Write the 3-7s and 7-12s benefit proof lines with `benefit-voiceover-library.md`; each benefit line must map user need -> visible product action -> human benefit.
   - Write the 12-15s CTA with `cta-library.md`; the CTA must match platform and conversion goal and use only one next action.
   - Apply `marketing-expression-rules.md` so the video has one main selling point, visible proof, and platform-matched CTA.
   - Keep timed beats, visible action, short spoken lines, optional short in-frame text, product proof, and CTA aligned with the confirmed creator portrait.
8. Apply `text-accuracy-rules.md`, `performance-rules.md`, and `seedance-prompt-rules.md` before generation.
9. Compile every relevant reference conclusion into the internal `seedance_generation_package` using `seedance-generation-contract.md`:
   - create `material_manifest` with a stable ID and role for every product, screenshot, reference and creator asset
   - create a detailed `product_identity_lock` from the authoritative product assets
   - create `creator_identity_lock` from the active Nano Banana Pro or user-supplied creator portrait
   - define one `global_visual_bible` with scene, lighting, color, exposure, lens feel and motion style
   - convert every script beat into detailed `shot_instructions` with source asset IDs, product state, creator state, composition, lighting, camera, movement start/end/speed, action mechanics, speech, sound, text, transition and continuity
   - create `continuity_ledger` and `final_render_checks`
   - keep this package internal and pass it to Seedance/video generation tool; do not append it to the normal user-facing script
10. Build `video_generation_materials` before any video generation or video-generation handoff:
   - Put all user-uploaded product images, product assets, reference images, screenshots, and files first, preserving their original order.
   - Put the active `creator_portrait_image` last. If the active portrait is an uploaded user person image that is already in the list, do not duplicate it; mark that uploaded image as the active `creator_portrait_image`.
   - Treat `video_generation_materials` as the actual reference/垫图 list for the video tool or frontend generation pipeline.
   - The internal generation package must refer to these materials: user product assets are the product appearance source of truth; `creator_portrait_image` is the protagonist/person reference.
11. Check the script and complete internal package with `quality-checklist.md`.
12. Return the compact user-facing shape defined in `output-spec.md`: creator portrait plus direct timestamped script. After the visible creator portrait and script are shown, call `dynamic_questionnaire` with one `radio` question:
   - `继续生成视频`: proceed to video generation using the displayed creator portrait, script, `video_generation_materials`, and `seedance_generation_package`.
   - `先修改方案`: wait for the user's revision request and do not generate video yet.

The final confirmation must be a `dynamic_questionnaire`, not only a natural-language sentence such as `你说同意生成`. If the user changes the creator portrait, script, product facts, assets, duration, ratio, voiceover, subtitles, or prompt package, update the visible package and ask the same confirmation again before generation.

13. When the user confirms `继续生成视频`, execute video generation and delivery:
    - Ensure output directory exists using `sandbox_bash` (e.g. `mkdir -p /workspace/output`).
    - Determine segment count from the `seedance_generation_package`:
      - Single-segment (default 15s): call `sandbox_generate_video` once. Compile the `shot_instructions` into the Prompt parameter following `seedance-prompt-rules.md` and `seedance-generation-contract.md`; pass `video_generation_materials` as ImageList (product/reference assets first, active `creator_portrait_image` last); set Ratio and Duration from defaults or user specification; set OutputPath to a deterministic path such as `/workspace/output/final.mp4`.
      - Multi-segment: call `sandbox_generate_video` for each segment in parallel, each with its own shot instructions compiled into Prompt, shared ImageList (`video_generation_materials`), matching Ratio, and per-segment Duration; use deterministic output paths such as `/workspace/output/shot_01.mp4`, `/workspace/output/shot_02.mp4`. After all segments succeed, call `render_video` with `video_paths` ordered by segment sequence and `output_path` set to the final assembly path.
    - If TTS voiceover is needed (spoken lines with specific voice), generate audio via `sandbox_generate_audio` before video generation and pass via AudioList; otherwise let the video model generate speech from `{台词}` in the Prompt.
    - After the final video file is ready (single-segment output or `render_video` assembly), call `present_sandbox_file` with `filepath` set to the final video path and `interrupt=true` to deliver and terminate. Do not add extra summary or follow-up questions after delivery; wait for the user to initiate further requests.
    - If video generation fails due to safety review or content policy, stop immediately and inform the user without retrying.

## Default Output

Unless the user asks for analysis, multiple options, a shooting plan, or the full model payload, return:

````text
creator_portrait_image
{supplied or Nano Banana Pro generated creator portrait image reference.}

脚本
{a concise 15-second UGC sales script with 0-3s / 3-7s / 7-12s / 12-15s beats, action, spoken_line, optional short in-frame text, and CTA.}

确认达人形象和脚本后即可开始生成视频；完整商品一致性、光影、构图、运镜、动作、声音和连续性指令将直接传给视频生成工具。
````

If the user explicitly asks for the full Seedance prompt, model instruction, generation payload, or audit details, output the compiled `seedance_generation_package` in a fenced `text` code block. Otherwise keep it internal.

If a complete creative plan markdown file has been created or referenced, keep the chat compact and use:

````text
大的思路总结：
{2-4 sentences explaining the core idea, why this route works, and how the product drives the conversion.}

完整创意方案可见：
{absolute_path}

脚本：
```text
{direct timestamped script}
```
随后使用 `dynamic_questionnaire` 询问：
- `继续生成视频`
- `先修改方案`
````

For Chinese users, call the file `完整创意方案` or `品牌片方案稿`; do not use the word `spec` in user-facing Chinese chat unless the user uses it first.

If the user only asks for strategy, do not fabricate a script or generation package. Explain the direction only, or create the plan file only as far as the request needs.

If the user confirms the prompt through the `dynamic_questionnaire` option `继续生成视频`, proceed directly to step 13 (video generation and delivery).

If the user requests edits, revise the current prompt directly. Do not restart the full parameter flow unless the edit depends on a missing core asset or impossible decision.

## Defaults

- Format: `15秒，9:16竖版`
- Platform: `抖音` unless specified
- Language: Chinese spoken lines by default
- Subtitles: optional; only add them when the user explicitly requests subtitles or provides subtitle copy
- Visual texture: `苹果原相机拍摄风格，自然光，真实生活场景，轻微手持晃动，平台原生 UGC 感`
- Creator persona: choose one product-matched persona from `creator-persona-library.md` before image generation; bind age, role, appearance, scene, product relationship, and tone.
- Creator portrait: if no suitable person reference is supplied, use `sandbox_generate_image` with the complete Nano Banana Pro image prompt from `portrait-image-rules.md` to create a product-appropriate domestic UGC creator portrait before script writing. The Prompt parameter must always begin with `[Model: chatgpt-image-2]` (mandatory model routing prefix, placed before all visual description text; include it for initial generation and any regeneration/adjustment). Do not expose that internal image prompt or the model prefix. Use `/workspace/出镜达人/` as the default stable directory and deterministic subject file names.
- Video reference/垫图: before video generation, always use user-uploaded product/reference materials plus the active `creator_portrait_image` as `video_generation_materials`.
- Internal model payload: compile all relevant reference rules into `seedance_generation_package`, including detailed product identity, source material IDs, global scene/light/camera rules, per-shot light and movement instructions, physical action, audio/text behavior and continuity.
- Script: after the active creator portrait is available, generate a direct 15-second user-facing script; use `hook-library.md`, `benefit-voiceover-library.md`, and `cta-library.md` while keeping the protagonist consistent with the portrait.
- Timing: prefer stable 4-shot rhythm, `0-3s / 3-7s / 7-12s / 12-15s`
- Selling point: one primary selling point per video unless the user asks for more
- Product: visible early and tied to the proof action

## Routing Notes

Use these only after reading the required references:

- Concrete offer, price, coupon, package, group-buying, final price -> offer-led sales or local-deal route.
- Product page, screenshots, app flow, service flow -> screen bridge or cutout presenter route.
- Beauty, apparel, home, food, electronics, toy, game, local service -> read category strategy.
- "更有趣", meme, funny opening, absurd interruption, deadpan review, strong hook -> use the absurd/meme/visual hook engine in `creative-type-library.md`.
- Reference video, competitor video, screenshots, viral link, "复刻", "像这个" -> use viral remake. Adapt hook, rhythm, proof mechanism, and creator energy; replace all product facts and wording.
- Script, fixed copy, narration, host lines, "把这个脚本视频化" -> preserve the script meaning and order; map each line to visible action and product proof.

## Prompt Guardrails

- Keep the internal `seedance_generation_package` self-contained; the video model should not need to read the skill or references.
- Compile every relevant reference conclusion into a concrete package field or shot field.
- Use positive execution wording in the tool payload.
- Avoid exposing internal routing, reference names, checklist logic, or rejected options.
- Do not generate full subtitles by default.
- Use optional in-frame text only for short offer, selling point, result, product-name, or CTA cues.
- Keep product appearance, SKU, package, logo, material, scale, and variants consistent with user assets.
- Keep physical actions plausible: one main action per shot, sequential handling, visible support.
- Let cuts happen after completed action, expression change, product placement, result reveal, spoken phrase ending, or music beat.
- Define lighting and camera for every shot: source, direction, softness, color temperature, exposure, shot size, angle, camera height, lens feel, focus, movement start/end/speed and hold time.
