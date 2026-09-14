# storyboard-grid-XX.png Composition Guide

Use this guide only after the video's exploration direction and current-round quantity are confirmed, every selected SKU's product-consistency gate is complete, the storyboard-frame cost has been disclosed, and the user has explicitly selected that video for visual-storyboard mode. Do not read or execute this guide for a script-only video. Every opted-in video has exactly one complete `storyboard-grid-XX.png`. The output keeps that name for compatibility, but its layout is a ratio-aware annotated storyboard sheet rather than a model-rendered grid with text.

Before any image-generation call covered by this guide, the agent must have successfully loaded `image_generate` through `load_skill` for the current batch, as required by `SKILL.md`. Apply that skill only as image-domain knowledge for prompt quality, reference conditioning, composition, framing, consistency, and actually disclosed model capabilities. This guide and `SKILL.md` remain authoritative for route selection, call count, no-text raw frames, file formats, annotations, composition, and confirmation flow. Do not let `image_generate` replace an explicit current-context disclosure of exact `seedream_5.0_pro`.

Each opted-in visual-mode video has one strict chain:

```text
accepted information + confirmed storyboard + video XX direction
-> raw no-text storyboard frames
-> complete source manifest _internal/storyboard-sheet-XX.json
-> complete storyboard-grid-XX.png
-> complete generation-plan-XX.md
-> user confirmation of the actual visual package
-> direct execution when the environment can consume that package
-> otherwise, only the required internal target lowering
```

Never reuse one complete sheet for multiple complete scripts. Do not create user-visible part sheets. When target lowering is required after confirmation, an internal target prompt uses only its actual same-suffix internal target sheet. Script-only videos follow `SKILL.md` and `generation-plan-template.md` and never enter this guide merely to manufacture a pair.

## Non-Negotiable Boundary

Image models generate only the visual frames in the target video ratio. They must not generate shot numbers, timecodes, annotations, subtitles, dialogue bubbles, technical labels, or the bottom information bar. Model-rendered text is too unreliable for this asset.

Every identifiable on-screen character must have an accepted visual anchor before any frame containing that character is generated. Reuse a usable user-provided character image directly; do not generate a cleaner duplicate. Otherwise reuse the exact character's accepted canonical anchor. If neither exists, first load `image_generate` as required, confirm the paid call, generate a single-character neutral/default anchor under `assets/anchors/canonical/`, present it through `present_sandbox_file`, and confirm it through `dynamic_questionnaire`. A prose description or a prior storyboard frame does not satisfy this gate. Attach the accepted character anchor to every applicable image call and map it explicitly as `图[N]（角色身份与必须保持的特征）`.

Before raw-frame generation, verify from `_internal/batch-status.md` that the earlier per-SKU product-consistency gate is complete and load every accepted direct product image and supplementary state reference into the applicable image calls. Do not repeat the questionnaire merely because this guide was opened. If translating the confirmed story into raw frames reveals a genuinely new visible product angle/state that was absent from the completed audit, stop, reopen the Product View And State Coverage Contract, resolve that new gap, and only then return here. User media remains authoritative, and every accepted supplementary state image must be attached with it to applicable calls through explicit `图[N]` semantics.

The engineering layer must:

1. read the accepted information and confirmed storyboard, apply the video's confirmed exploration direction, and use the already-loaded `image_generate` knowledge to improve the model-facing visual request;
2. send the complete image-relevant content to the image model rather than a filename;
3. generate or extract the ordered no-text frames;
4. write the internal JSON manifest;
5. run the bundled Python compositor to add all text and assemble the final sheet.

Attach the maximum useful set of applicable user-provided product/SKU/package, character, scene, prop, brand, style, palette, and lighting images directly, together with every relevant accepted product state reference, confirmed agent-generated anchor, and accepted derived-state reference, through the image tool's actual reference-image inputs. More relevant source information improves identity and visual consistency. A local path mentioned in prompt text does not attach a file. Never generate a normalized duplicate merely to satisfy this attachment list, and never omit a relevant attachment merely to make the request shorter.

The current image call may use visual evidence only from images actually present in its final `ImageList`. Images inspected by the agent, inventoried in project files, sent to another call, or summarized in Prompt but omitted from this call are visually unavailable to the model. Do not write preservation or consistency instructions that depend on an omitted image. Confirmed text facts may be stated as facts, but their text does not recreate the omitted image's exact identity, shape, layout, texture, or other visual signal.

The image model cannot perceive local paths or filenames. Before writing `Prompt`, finalize the ordered `ImageList`. Introduce every attached item in the Prompt with the tool-supported one-based syntax `图[N]（语义信息）`, where `N` exactly matches its position in `ImageList`. The semantic information must say what the image depicts, its source/role, relevant view or state, how it should be used, and what must remain unchanged. Example: `图[1]（用户提供的蓝色 SKU 商品正面图，作为商品身份参考，保持瓶型、蓝色标签与 Logo）` and `图[2]（已确认的女性角色基准图，保持面部、短发和白色上衣）`. Never mention the local filename/path in Prompt, never skip an attached index, and rebuild the mapping whenever list order changes. The final Prompt must enumerate every concrete image and must not contain unresolved `图[N]` placeholders. If `ImageList` is empty, omit all numbered-image language.

For each `sandbox_generate_image` call, provide required `Prompt` and absolute `OutputPath`, plus the ordered `ImageList` or `[]`. `OutputRatio` accepts only `1:1`, `16:9`, `4:3`, or `9:16`. Set `IsIntermediate: true` for raw contact sheets, individual raw shots, generated anchors, and derived-state images because the final user-facing storyboard sheet is composed later. If the target video ratio is not supported, select the closest same-orientation supported `OutputRatio`, describe the intended target framing in Prompt, then use deterministic normalization before composition. Do not pass `Model`: it is a legacy schema trace and is not supported by the actual tool.

Invocation shape with two references:

```json
{
  "Prompt": "参考图说明：图[1]（用户提供的蓝色 SKU 商品正面图，保持瓶型、标签和 Logo）；图[2]（已确认的女性角色基准，保持面部、短发和白色上衣）。生成一张 9:16 的无文字分镜画面……",
  "ImageList": [
    "/workspace/batch-video-projects/.../uploads/product-blue-front.png",
    "/workspace/batch-video-projects/.../assets/anchors/canonical/character-woman.png"
  ],
  "OutputPath": "/workspace/batch-video-projects/.../_internal/storyboard-01/shot-01.png",
  "OutputRatio": "9:16",
  "IsIntermediate": true
}
```

Paths appear only in `ImageList` and `OutputPath`. The model-facing `Prompt` contains only numbered semantic references.

Build a reference payload manifest before each image call:

- `candidate_references`: every available material relevant to at least one shot in this call, with source (`user`, `generated-anchor`, or `derived`), entity/style role, and path;
- `attached_references`: the ordered actual media paths sent through `ImageList`, each with its one-based `image_index` and exact semantic label used as `图[N]（...）` in Prompt;
- `omitted_references`: normally empty; when non-empty, record the disclosed hard count/type/size limit and why each item could not be attached.

For an exact-`seedream_5.0_pro` contact-sheet batch, use the union of references relevant to all used cells. For one-image-per-shot generation, reattach the complete useful set for that shot on every independent call. Do not assume a previous call carries visual context. If a hard reference limit exists, prioritize the exact product/SKU and identity-critical character sources, then scene/space, recurring props, style/brand, and derived-state references; use all available slots and disclose material omissions. If an omission can materially affect product identity or creative consistency, confirm the constrained selection through `dynamic_questionnaire` before the image call. Keep the final `ImageList` order stable within the call and write the corresponding semantic-index preamble before the creative instruction.

## Choose The Image Route

Choose the route only from an explicit exact active-model disclosure in the current runtime/tool context. `sandbox_generate_image` cannot select or override the model and must never receive a `Model` argument.

| Current active-model disclosure | Required route |
|---|---|
| Exact `seedream_5.0_pro` | Route A: up to nine shots in one `3 x 3` contact sheet |
| Exact `seedream_5.0` | Route B: one image per shot |
| Any other, ambiguous, inferred, historical, or absent disclosure | Route B: one image per shot |

### Route A: Up to nine shots per 3x3 contact sheet

Use this route only when the current context explicitly states that the active image model's exact identifier is `seedream_5.0_pro`. Its role here is to produce up to 9 ordered storyboard frames in one image call; it does not decide how many shots the story needs. Exact matching is mandatory: `seedream_5.0` is a different model and must not enter this route. Neither `Seedream 5.0`, `Seedream Pro`, a family mention, an inferred model, a prior run, nor an absent disclosure qualifies.

- For each batch, attach all candidate references relevant to any used cell, subject only to a disclosed hard tool limit. Do not pass only a product image when character, scene, prop, or style references are also available and relevant.

- For a complete video with `S` confirmed shots, make `ceil(S / 9)` image calls. Divide the shots into consecutive batches of at most 9 without changing their order.
- Set `OutputRatio` to the exact target video ratio when it is one of `1:1`, `16:9`, `4:3`, or `9:16`; otherwise use the closest same-orientation supported value and describe the intended target framing in Prompt. Request one image containing `3 列 x 3 行，共 9 格` for each batch, read left-to-right and top-to-bottom.
- Each used cell must be composed for the intended target video ratio. Unsupported tool ratios such as `3:4`, `4:5`, or `21:9` are framing instructions only, never values passed to `OutputRatio`; normalize the split cells deterministically afterward.
- Fill the first `K` cells for that batch in exact order, where `1 <= K <= 9`. Describe those shots completely, including subject, environment, composition, action, camera intent, product placement, and shared visual consistency.
- If `K < 9`, require cells `K+1` through `9` to be plain blank placeholders with no subject, scene, object, decoration, or text. Do not let the model invent extra shots to fill capacity.
- Require all nine cell slots to be flush: no borders, gutters, frames, or separator lines of any color. Intentional blank tail cells are slots in the matrix, not spacing around or between used cells.
- These contact sheets are raw image-generation batches for the complete virtual-machine plan. Do not anticipate or encode later video-call boundaries here.
- Do not ask the model to render annotations or a bottom information bar.
- After generation, split the first `K` cells directly in row-major order. Do not add a manual or automated visual acceptance gate for the raw Seedream contact sheet. Minor white borders, gutters, separator lines, imperfect blank tail cells, or other cosmetic contact-sheet artifacts are acceptable; do not reject, regenerate, or fall back to Route B because of them. Only an image-generation tool failure or an unreadable/corrupt source file blocks this route.

Model-facing prompt shape:

```text
参考图说明：图[1]（{对象、来源、视角/状态、用途、必须保持的特征}）；图[2]（{对象、来源、视角/状态、用途、必须保持的特征}）；...；图[N]（{语义信息}）。

一张 {目标视频比例，例如 9:16} 的无文字分镜画面，3 列 x 3 行共 9 格，按从左到右、从上到下的顺序阅读，每格内部均按 {同一目标视频比例} 镜头构图。本张承载 {K，1 至 9} 个实际分镜：前 {K} 格依次为：格1，{纯画面描述，并明确使用哪些图[N]保持什么内容}；...；格{K}，{纯画面描述，并明确使用哪些图[N]}。如 K 小于 9，格 {K+1} 至格9 必须保持纯色空白，不得补画主体、场景、物品、装饰或文字。九个格位紧密贴合，不得出现白线、黑线或任何颜色的分隔线，不得出现边框、画框、沟槽或格间空隙；尾部空白格是九宫格内的占位格，不是格间留白。已使用的相邻格通过不同镜头构图自然区分，不要让画面融合或跨格延伸。全图不得出现镜头序号、时间码、标题、字幕、台词气泡、标注、信息栏、水印或其他文字。整体视觉保持一致：{角色、商品、场景、风格、色板、光线、质感与构图基准}。保持图[N]中已确认的商品外观、包装、角色身份、服装、场景空间和画风跨格一致；不要新增未确认的商品文字、价格、卖点、声明或 CTA。
```

### Route B: One image per shot

Use this route for `seedream_5.0`, every other image model, every ambiguous label, and every case where the current context does not explicitly disclose the exact active identifier `seedream_5.0_pro`. This is the mandatory default, not a quality-based guess.

- Generate all `S` shots in the complete duration-driven video. This route requires exactly `S` image calls; explain that cost without treating it as a reason to rewrite the story.
- Generate exactly one no-text image for each confirmed shot. Use a schema-supported `OutputRatio`; when the target ratio is unsupported, describe target framing in Prompt and normalize the result deterministically before composition.
- On every shot call, reattach all useful user-provided materials and accepted generated/derived references for that shot. Independent calls are stateless; never rely on references sent to a prior shot.
- Keep filenames ordered, for example `_internal/storyboard-01/shot-01.png` through `shot-06.png` for a confirmed six-shot example unit.
- Before generating shot 1, make a reference checklist that separates user-provided direct references from agent-generated anchors. Mark every product, character, scene, recurring prop, palette, lighting, and style source as `用户提供，直接复用`, `需主动生成并确认`, `不需要`, or `探索项`.
- `不需要` is invalid for an identifiable character that appears on screen. Such a character must resolve to `用户提供，直接复用` or an accepted `需主动生成并确认` anchor before its first frame call. Anonymous background crowds are the only character-like exception.
- A usable user-provided product or entity image is already the direct reference, regardless of background, pose, crop, handling state, or missing alternate angles. Never generate a clean, isolated, neutral, redrawn, or confirmation baseline for it. Attach the actual supplied image to applicable calls. If a cleaner source is essential, request it from the user or disclose the limitation.
- Generate an anchor when a consistency-critical identity lacks a usable user-provided image. This is mandatory for every identifiable appearing character without an anchor, including a character supplied only as a text description; for other entities, generate only when the confirmed direction genuinely requires a stable new identity. Place the first accepted generated image under `assets/anchors/canonical/`; it is the baseline and must not trigger a second baseline-generation call. Explain and confirm this paid call before starting it.
- Apply placement, interaction, opening, pouring, damage, occupancy, and other changing states only in the storyboard-frame prompt. When an altered state must persist, store it separately under `assets/anchors/derived-states/` and keep every user source and generated anchor unchanged.
- Repeat the accepted user-provided direct references, accepted product state references, agent-generated anchors, style sources, and relevant derived-state references in every prompt and attach the maximum useful actual media set whenever the tool supports them. A previous prompt, filename, or phrase such as `同前` does not carry context into an independent call.
- Keep each prompt focused on one shot. Do not ask a model that is weak at multi-panel layout to create a grid.
- If the model cannot accept reference images, use the same concise character, product, scene, prop, palette, lighting, and rendering description in every shot prompt, explain the consistency risk to the user, and get confirmation before proceeding when identity or product consistency is business-critical.
- Reject and regenerate any individual frame containing unwanted model-rendered labels, subtitles, or stray text before composition.

If Route A cannot produce a readable image file because the image-generation call fails or returns corrupt output, explain the technical failure before considering Route B because the affected unit would change from `ceil(S / 9)` image calls to `S`. Cosmetic contact-sheet artifacts, including white separator lines, never justify this fallback.

Model-facing prompt shape:

```text
参考图说明：图[1]（{对象、来源、视角/状态、用途、必须保持的特征}）；图[2]（{对象、来源、视角/状态、用途、必须保持的特征}）；...；图[N]（{语义信息}）。

生成一张 {目标视频比例，例如 9:16} 的无文字分镜画面，这是第 {镜头序号}/{完整视频确认的总镜头数} 个镜头。画面内容：{在本镜头中组合主体、环境、景别、构图、动作、镜头意图、产品露出和所需状态，并明确图[N]分别约束哪些主体或视觉属性}。严格保持相关图[N]中的商品外观、包装、Logo、SKU、角色身份、服装、场景结构、关键道具、风格、色板和光线。不得出现镜头序号、时间码、标题、字幕、台词气泡、标注、信息栏、水印或其他新增文字；不得新增未确认的价格、卖点、声明或 CTA。
```

## Internal Manifest

Create `_internal/storyboard-sheet-XX.json` from the accepted information, confirmed storyboard, and this video's confirmed exploration direction. This is an internal rendering input, not a user-visible deliverable. The matching script is written only after this sheet is complete.

Use UTF-8 JSON with this shape:

```json
{
  "video_ratio": "9:16",
  "shots": [
    {
      "number": 1,
      "timecode": "00:00-00:02",
      "shot_size": "全景",
      "purpose": "建立环境",
      "visual": "深夜城市俯瞰，写字楼只有一扇窗亮着暖黄灯。",
      "action": "镜头中的主体动作；没有时可留空",
      "product": "商品露出方式；没有时可留空",
      "camera": "镜头运动；没有时可留空",
      "transition": "缓慢下降，切入办公室。",
      "audio": "城市夜环境音，轻钢琴渐入。",
      "voiceover": "旁白｜旁白｜凌晨两点，他还在和最后一个 bug 较劲。"
    }
  ],
  "global_info": {
    "角色与一致性": "角色、商品、包装、服装、场景等跨镜头必须一致的内容。",
    "视觉与情绪": "画风、色板、光线、质感、情绪和节奏。",
    "技术规格": "镜头数量、总时长、目标视频比例；有声内容可含旁白、角色对白和角色独白；不生成字幕。"
  }
}
```

Manifest rules:

- The number and order of `shots` must exactly match the confirmed storyboard and raw images; the later script must preserve this same order.
- `video_ratio` must use positive `width:height` notation, such as `16:9`, `1:1`, `4:5`, or `9:16`. If omitted, the compositor keeps backward-compatible `16:9` behavior. Prefer writing it explicitly.
- Required shot fields are `timecode`, `shot_size`, `visual`, `transition`, `audio`, and `voiceover`.
- `action`, `product`, `camera`, and `purpose` are optional but useful.
- `voiceover` contains spoken content only and keeps this field name for compositor compatibility. Use `说话角色｜旁白/对白/独白｜完整台词`; when several lines occur in one shot, list them in order separated by `；`. Use `无` for a silent shot. Role/type labels are annotations and control data, not words to be spoken. Do not put subtitles or screen text into it. Distinct speaking characters remain distinct roles and later map to separate confirmed voice anchors by default.
- `replacement_image` is optional. When present, it must be the absolute sandbox path of a newly generated single-shot image for that exact shot. One or multiple shots may define it. The compositor loads the original grid or image sequence first, then replaces only those indexed shots.
- Keep the total annotation for one shot concise, normally within about 150 Chinese characters across all fields. Preserve executable information; remove rationale and literary repetition.
- `global_info` must contain one to four short titled sections; use the three shown above by default.

## Lower Only When Direct Execution Fails

Do not add video-call parts to the complete source manifest before the user confirms the visual package containing `storyboard-grid-XX.png` and `generation-plan-XX.md`. After confirmation, first check whether the current environment can directly consume that package. If it can, pass the complete sheet as actual reference media and skip this section. Only when a hard capability constraint blocks direct use should the agent copy source data into `_internal/runtime/video-XX/runtime-manifest.json`; add call boundaries only when multiple video calls are truly required:

```json
{
  "shots": [
    {
      "number": 1,
      "part": 1,
      "timecode": "00:00-00:02",
      "global_timecode": "成片 00:00-00:02",
      "shot_size": "全景",
      "visual": "本镜头的完整画面说明。",
      "transition": "本段内的转场或结尾交接画面。",
      "audio": "本镜头的环境音和配乐。",
      "voiceover": "说话角色｜旁白/对白/独白｜本镜头的完整台词。"
    }
  ],
  "global_info": {
    "角色与一致性": "跨段复用的用户原始商品、角色、场景和道具参考；如有，另列已确认的主动生成基准与派生状态参考。",
    "视觉与情绪": "跨段保持不变的风格、色板、光线、质感与节奏。",
    "技术规格": "成片比例、总时长；每段独立生成；保留明确标注说话角色的旁白、对白和独白，不生成字幕。"
  },
  "parts": {
    "1": {
      "label": "第 1 段 / 共 2 段",
      "handoff": "从明确的开场状态开始；结尾固定在可供下一段承接的动作与构图。"
    },
    "2": {
      "label": "第 2 段 / 共 2 段",
      "handoff": "开场承接上一段实际尾帧中的角色位置、商品朝向、光线与动作趋势。"
    }
  }
}
```

Split-manifest rules:

- Every shot must have a positive integer `part`; parts must be contiguous ordered blocks starting at 1.
- `timecode` is local to the tool call and restarts at zero for each part. `global_timecode`, when retained for internal assembly and status only, records the shot's place in the finished video but is never rendered on the storyboard image or copied into the model-facing `generation-input-part-YY.md`.
- Keep common `global_info` to at most three sections unless it already contains `段落衔接`; the compositor adds or replaces that fourth section for each part.
- Keep each part's `handoff` concrete and concise: opening state, ending state, subject position, product orientation, camera direction, light, and audio carry-over as relevant.
- Use one ordered raw-frame set for the full video. The compositor groups the frames by `part`; do not duplicate or reorder them per call.

Compose all internal runtime sheets in one command:

```bash
python3 scripts/compose_storyboard_sheet.py \
  --manifest _internal/runtime/video-03/runtime-manifest.json \
  --images \
    _internal/storyboard-03/shot-01.png \
    _internal/storyboard-03/shot-02.png \
    _internal/storyboard-03/shot-03.png \
    _internal/storyboard-03/shot-04.png \
  --split-by-part \
  --output _internal/runtime/video-03/storyboard-input.png
```

This writes `_internal/runtime/video-03/storyboard-input-part-01.png`, `_internal/runtime/video-03/storyboard-input-part-02.png`, and so on. Each output is independently checked against the `<6000px` limit and pairs only with `_internal/runtime/video-03/generation-input-part-01.md`, `_internal/runtime/video-03/generation-input-part-02.md`, and so on. Do not present these internal parts block by block by default.

For Seedream source grids, use the same ordered `--grid-image` or `--grid-images` inputs and `--grid-shot-counts` used by the complete preview, but switch to the runtime manifest, add `--split-by-part`, omit `--no-max-dimension`, and write into `_internal/runtime/video-XX/`.

## Compose The Final Sheet

The bundled script requires Pillow and a CJK-capable font. Use the active environment's Python when Pillow is available.

For one Seedream contact sheet with six used cells and three intentional blank tail cells:

```bash
python3 scripts/compose_storyboard_sheet.py \
  --manifest _internal/storyboard-sheet-01.json \
  --grid-image _internal/storyboard-01/raw-grid.png \
  --grid-rows 3 \
  --grid-cols 3 \
  --grid-shot-counts 6 \
  --no-max-dimension \
  --output storyboard-grid-01.png
```

For twelve shots supplied as two Seedream contact sheets, with nine used cells in the first and three in the second:

```bash
python3 scripts/compose_storyboard_sheet.py \
  --manifest _internal/storyboard-sheet-01.json \
  --grid-images \
    _internal/storyboard-01/raw-grid-01.png \
    _internal/storyboard-01/raw-grid-02.png \
  --grid-rows 3 \
  --grid-cols 3 \
  --grid-shot-counts 9 3 \
  --no-max-dimension \
  --output storyboard-grid-01.png
```

`--grid-shot-counts` tells the compositor how many leading row-major cells to extract from each source sheet; all remaining tail cells are intentional blanks. The counts must match the number of source sheets, each count must be between 1 and 9 for a `3 x 3` grid, and their sum must equal the complete source-manifest shot count. Pack the complete sequence independently of future video-call boundaries.

For individually generated frames:

```bash
python3 scripts/compose_storyboard_sheet.py \
  --manifest _internal/storyboard-sheet-01.json \
  --images \
    _internal/storyboard-01/shot-01.png \
    _internal/storyboard-01/shot-02.png \
    _internal/storyboard-01/shot-03.png \
    _internal/storyboard-01/shot-04.png \
    _internal/storyboard-01/shot-05.png \
    _internal/storyboard-01/shot-06.png \
  --no-max-dimension \
  --output storyboard-grid-01.png
```

## Replace One Or More Shots

Do not regenerate a complete Seedream contact sheet merely because the user rejects individual shots. Generate one new no-text image per rejected shot with the applicable user-provided direct references plus accepted generated/derived references. Rebuild that call's ordered `ImageList` and `图[N]（语义信息）` Prompt mapping, use a supported `OutputRatio`, and deterministically normalize to the target ratio if needed. Then update only the corresponding shot objects in `_internal/storyboard-sheet-XX.json`:

```json
{
  "number": 3,
  "timecode": "00:04-00:06",
  "shot_size": "特写",
  "visual": "替换后的完整画面说明。",
  "action": "替换后的主体动作。",
  "product": "替换后的商品露出。",
  "camera": "替换后的镜头运动。",
  "transition": "替换后的转场。",
  "audio": "替换后的环境音与配乐。",
  "voiceover": "说话角色｜旁白/对白/独白｜替换后的完整台词。",
  "replacement_image": "/workspace/batch-video-projects/.../_internal/storyboard-01/shot-03-v2.png"
}
```

Set `replacement_image` on every rejected shot, so one compositor run can replace one or many shots. Keep passing the original `--grid-image`, `--grid-images`, or `--images` arguments. The compositor resolves the complete original sequence, loads each replacement, preserves its aspect ratio, and normalizes it to the exact pixel width and height of the original indexed frame before overlaying it:

- default `--fit contain`: scale to fit and add the existing dark frame background where ratios differ;
- `--fit cover`: scale and center-crop to fill the original frame size;
- never stretch a replacement, resize the sheet around it, reorder other shots, or alter unmarked frames;
- the output JSON reports all applied shot numbers in `replacement_shots`.

The manifest is the source for rendered annotations, so updating `voiceover` redraws that shot's spoken line on the revised sheet. The compositor does not generate the replacement image, synthesize audio, or rewrite `generation-plan-XX.md`. The agent must update the matching script's same shot whenever visual instructions, timing, audio, or spoken lines change, then re-present the revised complete `storyboard-grid-XX.png` and `generation-plan-XX.md` for confirmation. Keep `replacement_image` in any later runtime manifest so target-specific sheets use the accepted replacement instead of the original contact-sheet cell.

Resolve the compositor path from this skill's installation directory. Resolve every project manifest, raw image, runtime input, and output as an absolute path under the active `/workspace/batch-video-projects/...` project; the commands above use relative paths only for readability. Never depend on an arbitrary current working directory.

The compositor chooses the layout from `video_ratio`:

- target width >= target height: use a vertical list; every frame is on the left and its structured annotation is on the right. Frame height is fixed at `576px` before safety scaling and frame width is calculated from the target ratio. A six-shot individual-route `16:9` sheet is `2048 x 3776`; a nine-shot contact-sheet version is `2048 x 5504`;
- target width < target height: use a horizontal strip; frames are arranged left-to-right and every annotation sits directly below its frame. Frame width is fixed at `648px` before safety scaling and frame height is calculated from the target ratio. A six-shot individual-route `9:16` sheet is `3888 x 2192`; a nine-shot contact-sheet version is `5832 x 2192`;
- divider thickness follows semantic role rather than axis. The strong `10px` divider separates different shots; the lighter `6px` divider separates one shot's frame from its annotation. Therefore a vertical list uses strong horizontal shot dividers and a light vertical frame/annotation divider, while a horizontal strip uses strong vertical shot dividers and a light horizontal frame/annotation divider. Draw strong shot dividers after all shot cards so they remain continuous and are not covered by adjacent frames;
- both layouts use program-drawn dark boundaries and a `320` pixel shared information bar at the bottom;
- neither layout renders `global_timecode` or an absolute finished-video time.

The compositor uses `contain` by default so unexpected source ratios are not cropped. Generate frames in the target video ratio whenever possible. Use `--fit cover` only after verifying that edge cropping will not remove the product or required action.

For the complete user-facing virtual-machine plan, use `--no-max-dimension` so it remains complete and readable. The resulting sheet is also eligible for direct video-model input when its actual dimensions and file satisfy the current environment. If it exceeds a target limit such as `<6000px`, preserve the user-facing sheet and create a separate target-safe internal sheet only after confirmation. Internal target sheets never use `--no-max-dimension`; keep the default `5992px` cap. The compositor also rejects image-count mismatches and text that cannot fit at the safe minimum font size; fix source content instead of cropping text.

## Final Verification

Before presenting the resource for confirmation, verify:

- the output exists and the compositor reports the expected shot count;
- the complete source preview contains the entire finished-video sequence and remains readable; it is not required to be below `6000px`;
- every frame maps to its own annotation in the selected ratio-aware layout;
- shot order matches the confirmed storyboard and this video's exploration direction exactly;
- text is readable, not clipped, and contains no unresolved placeholders;
- product, character, scene, and style consistency are acceptable;
- the image contains no generated subtitles;
- the complete sheet maps only to the same-suffix complete script; direct execution uses this visual package once, while lowered multi-call execution never passes the full package unchanged to every part.

After visually inspecting the complete sheet, write the matching complete script. Present the actual complete PNG and Markdown files through `present_sandbox_file` using its runtime-visible schema and summarize the visual package in conversation. Then launch `dynamic_questionnaire` with closed confirmation/revision choices plus an open change request; do not add a custom/other option. A path or summary alone is insufficient. After confirmation, execute the visual package directly when compatible; compile internal target sheets and prompts only when a hard environment constraint blocks direct use.
