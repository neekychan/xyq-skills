---
name: ugc-marketing-video-30s
description: Create Seedance 2.5-ready 30-second UGC marketing video workflows for Douyin, Kuaishou, Xiaohongshu, WeChat, and related short-video generation tools. Use when the active route is 30s, when the user needs UGC30s, 30秒带货, 30秒种草, 30秒产品测评, 30秒卖点展示, 30秒达人探店, 30秒团购/本地生活转化, Seedance 2.5 UGC, reference-video adaptation, sales-script-to-video, or a paste-ready 30-second video_generation_prompt from product text, images, links, scripts, CTAs, offers, or reference videos.
tools: ["ugc_idea_generator", "sandbox_generate_image"]
---

# UGC Marketing Video

## Seedance 2.5 Override

This is the 30-second Seedance 2.5 version of the UGC marketing video skill. Follow the user's explicit duration first; if no duration is specified, default to `30秒，9:16竖版` for this skill.

Before writing a final 2.5 prompt, read:

1. `/workspace/.skills/ugc-marketing-video-30s/references/output-spec-30s.md`
2. `/workspace/.skills/ugc-marketing-video-30s/references/seedance25-prompt-rules.md`

Then read the existing category, platform, creative, hook, benefit, CTA, consistency, and quality references as needed. The 30-second Seedance 2.5 prompt contract is authoritative for this skill.

Default 30-second UGC rhythm:

- `0-3秒`: hook, concrete offer, or pain/desire trigger; product appears early when possible.
- `3-8秒`: believable creator and real usage context.
- `8-14秒`: product appears as action and the main selling point becomes clear.
- `14-21秒`: proof 1, such as hands-on demo, process, comparison, store proof, or screen bridge.
- `21-27秒`: proof 2, result, reaction, social proof, or before/after confirmation.
- `27-30秒`: product name, value confirmation, and one natural CTA.

Turn product information, images, links, offers, scripts, CTAs, or reference videos into a domestic UGC marketing chain: product understanding -> 小云雀 matches and generates a creator portrait -> user can adjust the creator image -> the skill writes the script -> the skill writes the final `video_generation_prompt` -> video generation uses the user materials and creator portrait as reference/垫图.

This is the self-writing version. Do not call `ugc_idea_generator`. The only required image-generation tool is `sandbox_generate_image`; the skill does not restrict the underlying image model selected by the frontend/runtime.

Keep the chat lightweight, but do not skip references. This skill is a routing hub; detailed behavior lives in bundled `references/`. In the hosted workspace, reference files must be addressed through `/workspace/.skills/ugc-marketing-video-30s/references/...` and read with `sandbox_read`.

**IMPORTANT**：It is **forbidden** to use `ugc_idea_generator` to generate ideas. Ideas must be generated according to the following guidelines.

## Mandatory Reference Loading

Before writing any final `video_generation_prompt`, read the references needed for the task. Use `sandbox_read` with the workspace-form paths shown below. Do not replace these with local machine paths, relative markdown links, or `/tmp` paths.

Minimum required references for every final prompt:

1. Use `sandbox_read` to read `/workspace/.skills/ugc-marketing-video-30s/references/output-spec-30s.md`
2. Use `sandbox_read` to read `/workspace/.skills/ugc-marketing-video-30s/references/interaction-flow.md`
3. Use `sandbox_read` to read `/workspace/.skills/ugc-marketing-video-30s/references/input-consistency-rules.md`
4. Use `sandbox_read` to read `/workspace/.skills/ugc-marketing-video-30s/references/production-scenarios.md`
5. Use `sandbox_read` to read `/workspace/.skills/ugc-marketing-video-30s/references/creative-strategy-focus.md`
6. Use `sandbox_read` to read `/workspace/.skills/ugc-marketing-video-30s/references/creative-type-library.md`
7. Use `sandbox_read` to read `/workspace/.skills/ugc-marketing-video-30s/references/creator-persona-library.md`
8. Use `sandbox_read` to read `/workspace/.skills/ugc-marketing-video-30s/references/hook-library.md`
9. Use `sandbox_read` to read `/workspace/.skills/ugc-marketing-video-30s/references/benefit-voiceover-library.md`
10. Use `sandbox_read` to read `/workspace/.skills/ugc-marketing-video-30s/references/cta-library.md`
11. Use `sandbox_read` to read `/workspace/.skills/ugc-marketing-video-30s/references/marketing-expression-rules.md`
12. Use `sandbox_read` to read `/workspace/.skills/ugc-marketing-video-30s/references/text-accuracy-rules.md`
13. Use `sandbox_read` to read `/workspace/.skills/ugc-marketing-video-30s/references/performance-rules.md`
14. Use `sandbox_read` to read `/workspace/.skills/ugc-marketing-video-30s/references/seedance25-prompt-rules.md`
15. Use `sandbox_read` to read `/workspace/.skills/ugc-marketing-video-30s/references/quality-checklist.md`
16. Use `sandbox_read` to read `/workspace/.skills/ugc-marketing-video-30s/references/portrait-image-rules.md`

Conditional required references:

- Use `sandbox_read` to read `/workspace/.skills/ugc-marketing-video-30s/references/category-strategy.md` when a concrete product category, buyer, usage scene, proof form, offer, or CTA matters.
- Use `sandbox_read` to read `/workspace/.skills/ugc-marketing-video-30s/references/platform-rules.md` when a platform is specified or platform behavior affects format, pacing, CTA, or text placement.
- Use `sandbox_read` to read `/workspace/.skills/ugc-marketing-video-30s/references/diversity-rules.md` when generating multiple versions, variants, or repeated revisions.

Do not write or preview the final prompt until these references have been read. Keep reference reading internal; do not tell the user which files were read unless they ask.

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
   - If no suitable person image is supplied and `sandbox_generate_image` is available, internally build the full high-quality creator-image prompt described in `portrait-image-rules.md`, then pass that complete prompt unchanged into `sandbox_generate_image`. Do not expose the internal prompt to the user.
   - Default to a 4:5 high-realism native UGC creator portrait. Keep phone-shot texture, but do not make the creator visibly hold a phone by default; visible phones are only props, not persistent downstream video actions.
   - Use a deterministic `output_path` under `/workspace/出镜达人/`, such as `/workspace/出镜达人/creator_portrait_subject_1.png`.
   - Show the generated or supplied creator portrait with a compact Chinese `creator_image_caption` and `product_consistency_note`. If the user asks to adjust the portrait, call `sandbox_generate_image` again with the revision and use the latest accepted portrait for later steps.
7. Generate a concise 30-second sales script after the active creator portrait is selected:
   - Choose the 0-3s hook from `hook-library.md`; the hook must include visible product entry and connect back to proof by 8-14s.
   - Write the 8-14s, 14-21s, and 21-27s benefit proof lines with `benefit-voiceover-library.md`; each benefit line must map user need -> visible product action -> human benefit.
   - Write the 27-30s CTA with `cta-library.md`; the CTA must match platform and conversion goal and use only one next action.
   - Apply `marketing-expression-rules.md` so the video has one main selling point, visible proof, and platform-matched CTA.
   - Keep timed beats, visible action, short spoken lines, optional short in-frame text, product proof, and CTA aligned with the confirmed creator portrait.
8. Apply `text-accuracy-rules.md`, `performance-rules.md`, and `seedance25-prompt-rules.md` before writing the final prompt. The final prompt must include compact positive control for input consistency,成片稳定性, 达人真实性, 物理与空间准确性, 文字准确性, 视听同步, 视频节奏, 营销表达, and 多样性 when relevant.
9. Build `video_generation_materials` before any video generation or video-generation handoff:
   - Put all user-uploaded product images, product assets, reference images, screenshots, and files first, preserving their original order.
   - Put the active `creator_portrait_image` last. If the active portrait is an uploaded user person image that is already in the list, do not duplicate it; mark that uploaded image as the active `creator_portrait_image`.
   - Treat `video_generation_materials` as the actual reference/垫图 list for the video tool or frontend generation pipeline.
   - The final `video_generation_prompt` must refer to these materials: user product assets are the product appearance source of truth; `creator_portrait_image` is the protagonist/person reference.
10. Check the result with `quality-checklist.md`.
11. Return the compact user-facing shape defined in `output-spec-30s.md`. If the user confirms the creator portrait and script, proceed to video generation when a generation tool is available, passing both `video_generation_materials` and `video_generation_prompt`.

## Default Output

Unless the user asks for analysis, multiple options, or a shooting plan, return:

````text
思路简述：
{1-3 sentences explaining the creator fit, hook, proof, and CTA logic in user-facing language.}

creator_portrait_image
{supplied or generated creator portrait image reference. If no suitable person image is supplied and `sandbox_generate_image` is available, this section must contain the 小云雀-generated portrait reference, not only a prompt. If the user asks to adjust the portrait, regenerate it first and do not proceed to video generation until the latest feedback is handled.}

creator_image_caption
{concise Chinese creator summary: age band, creator role, hair/outfit/temperament, scene, product fit, product relationship, and tone. Do not expose the internal image prompt.}

product_consistency_note
{Chinese note explaining that the portrait is only the character reference; product appearance follows the user's product image/assets; creator clothing, accessories, phone, and background props are not the product.}

video_generation_materials
{ordered reference/垫图 list: user-uploaded product/reference materials first, active creator_portrait_image last. Use this list when calling a video generation tool or handing off to the frontend video pipeline.}

script
{a concise 30-second UGC sales script with 0-3s / 3-8s / 8-14s / 14-21s / 21-27s / 27-30s beats, action, spoken_line, optional short in-frame text, and CTA.}

video_generation_prompt
```text
{paste-ready prompt}
```

确认达人形象和脚本后即可开始生成视频；也可以继续调整达人形象、卖点、风格、台词、尺寸或平台。
````

If the user says "只要 prompt", output only `video_generation_prompt` followed by a fenced `text` code block containing the prompt.

If a complete creative plan markdown file has been created or referenced, keep the chat compact and use:

````text
大的思路总结：
{2-4 sentences explaining the core idea, why this route works, and how the product drives the conversion.}

完整创意方案可见：
{absolute_path}

这是为你规划好的 Seedance 2.5 prompt：
```text
{paste-ready prompt}
```
你说“同意生成”，我就直接为你开拍。
````

For Chinese users, call the file `完整创意方案` or `品牌片方案稿`; do not use the word `spec` in user-facing Chinese chat unless the user uses it first.

If the user only asks for strategy, do not fabricate a `video_generation_prompt`. Explain the direction only, or create the plan file only as far as the request needs.

If the user confirms the prompt, proceed directly to video generation when a generation tool is available.

If the user requests edits, revise the current prompt directly. Do not restart the full parameter flow unless the edit depends on a missing core asset or impossible decision.

## Defaults

- Format: `30秒，9:16竖版`
- Platform: `抖音` unless specified
- Language: Chinese spoken lines by default
- Subtitles: optional; only add them when the user explicitly requests subtitles or provides subtitle copy
- Visual texture: `苹果原相机拍摄风格，自然光，真实生活场景，轻微手持晃动，平台原生 UGC 感`
- Creator persona: choose one product-matched persona from `creator-persona-library.md` before image generation; bind age, role, appearance, scene, product relationship, and tone.
- Creator portrait: if no suitable person reference is supplied, call `sandbox_generate_image` through 小云雀 to create a product-appropriate domestic UGC creator portrait before script writing. Internally pass the complete high-quality creator-image prompt from `portrait-image-rules.md` into the tool; do not expose that prompt to the user. Use `/workspace/出镜达人/` as the default stable directory and deterministic subject file names. The user can ask to adjust the creator image before video generation.
- Video reference/垫图: before video generation, always use user-uploaded product/reference materials plus the active `creator_portrait_image` as `video_generation_materials`; pass this ordered list together with the final `video_generation_prompt` to the video tool or frontend pipeline.
- Script: after the active creator portrait is available, generate a 30-second script before or alongside the final `video_generation_prompt`; use `hook-library.md`, `benefit-voiceover-library.md`, and `cta-library.md` to vary the opening, benefit explanation, and closing action while keeping the protagonist consistent with the portrait.
- Timing: prefer stable 5-6-shot rhythm, `0-3s / 3-8s / 8-14s / 14-21s / 21-27s / 27-30s`
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

- Keep final prompts self-contained; the video model should not need to read the spec or references.
- Use positive execution wording in visible prompts.
- Avoid exposing internal routing, reference names, checklist logic, or rejected options.
- Do not generate full subtitles by default.
- Use optional in-frame text only for short offer, selling point, result, product-name, or CTA cues.
- Keep product appearance, SKU, package, logo, material, scale, and variants consistent with user assets.
- Keep physical actions plausible: one main action per shot, sequential handling, visible support.
- Let cuts happen after completed action, expression change, product placement, result reveal, spoken phrase ending, or music beat.
