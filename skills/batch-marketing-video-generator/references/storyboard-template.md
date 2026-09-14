# storyboard.md Template

Use this fixed structure for `storyboard.md`. Keep that exact file path, but always call it **故事母版** to users. It is the single reusable mother story for the batch, not a list of every video version and not one video's final storyboard.

`storyboard.md` should contain only the storyboard table. Keep discussion about overall direction, why a direction was chosen, and confirmation history in conversation or `_internal/batch-status.md`, not in this file.

```markdown
# 故事母版

| 分镜 | 时间 | 已确定内容 | 探索项/留空项 | 画面 | 动作/镜头 | 说话角色与有声内容意图 | 产品露出 | 素材引用 | 注意事项 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 示例时间 |  |  |  |  |  |  |  |  |
| 2 | 示例时间 |  |  |  |  |  |  |  |  |
| 3 | 示例时间 |  |  |  |  |  |  |  |  |
| 4 | 示例时间 |  |  |  |  |  |  |  |  |
| 5 | 示例时间 |  |  |  |  |  |  |  |  |
| 6 | 示例时间 |  |  |  |  |  |  |  |  |
```

Rules:

- This is the final shared story-master table, not a planning log.
- The table itself is the reusable story structure: put already confirmed elements in `已确定内容`, and leave the parts meant to differ blank or mark them as `探索项` in `探索项/留空项`.
- Keep only one copy of the shot sequence. Do not add a `视频` column, video numbers, or repeated rows for every video version.
- Do not add separate sections for fixed content, exploration directions, rationale, status, or logs.
- Use confirmed facts and exploration constraints from `information-understanding.md`, explicit conversation choices, the accepted creative-assistant handoff, and the already-loaded `marketing-video-creator` knowledge. Accepted information is authoritative for facts; searched inspiration may improve story expression but may not add product claims. Do not cite the internal handoff, URLs, search history, or research reasoning inside `storyboard.md`.
- Product/SKU, character, and scene can be exploration items. Keep them open in this table when they are meant to differ across videos.
- The six rows above illustrate the table shape; they are not a fixed default. Use the user's target duration and the creative knowledge learned from `marketing-video-creator` to design the full story structure, exact shot count, and real time ranges. `batch-marketing-video-generator` still controls this file's format and confirmation flow. Add or remove rows accordingly.
- Do not resolve, mention, or mark the selected video model's per-call duration limit here. This table describes the complete finished video and is independent of later runtime splitting.
- The image route does not control the story count. For a complete video with `S` confirmed shots, only a current explicit exact active-model disclosure of `seedream_5.0_pro` permits `ceil(S / 9)` contact-sheet calls with unused trailing cells left blank. `seedream_5.0`, every other/ambiguous model, and no disclosure require `S` one-shot image calls. `sandbox_generate_image` cannot receive a `Model` argument.
- Keep the confirmed complete duration, timing, and shot count aligned with every full script. For opted-in visual-mode videos, also keep the raw-frame set, source manifest, and full storyboard sheet aligned.
- Do not mark future video-call boundaries or add local call timecodes. Those are derived internally only after the complete per-video resources are confirmed.
- `说话角色与有声内容意图` describes spoken audio only. Identify the intended speaker and whether the beat is narration, dialogue, or monologue; when the speaker itself is an exploration item, mark it clearly instead of silently defaulting to narrator. Do not plan generated subtitles, captions, dialogue bubbles, or title cards unless the user explicitly changes the no-subtitle requirement.
- Do not create separate `storyboard-01.md` files unless the user explicitly asks.
- Do not include asset audit details, tool arguments, or generation prompt text.
- After this table is confirmed, present each video's concrete exploration direction in conversation. Do not add those video-specific choices to this file.
- Before creating per-video resources, ensure the preparation-round quantity is explicit or confirmed independently from planned total. When it is missing, use `dynamic_questionnaire` with `先准备 1 条方案（推荐）`, useful closed alternatives, and an open notes question; do not add `其他数量`. Then complete the required per-SKU product angle/state consistency gate for those selected directions. Only after that gate is resolved may the agent disclose storyboard-frame cost and ask which preparation-round videos should receive an optional `storyboard-grid-XX.png`. For a multi-video preparation round, normally recommend only the first selected video. This quantity never authorizes later video generation.
- Every selected video gets exactly one complete self-contained `generation-plan-XX.md`. Only opted-in videos first get one complete same-suffix `storyboard-grid-XX.png`, which the script explicitly uses with a shot-for-shot mapping. Script-only videos get no raw storyboard frames, source manifest, or grid, and their scripts must carry complete shot-level visual instructions. Never create user-visible part files.
- Cost estimates count user-provided direct references as zero image-generation calls, show zero storyboard-frame calls for script-only videos, and list any confirmed character-anchor, product-state-reference, or other derived-state calls separately from optional storyboard-frame calls.
- Present the actual `storyboard.md` through `present_sandbox_file`, using **故事母版** as the display name when the runtime schema supports one, then show the table or a compact readable version in conversation.
- After presentation succeeds, explain that one **故事母版** serves the whole planned batch: `已确定内容` remains shared and `探索项` will be filled differently for each video, so this does not mean the workflow will make only one video.
- Then explain the upcoming steps in this exact order: confirm the mother story; review and confirm the planned-total exploration directions; choose the current-round video quantity with 1 recommended when missing; complete every selected product's required angle/state consistency preparation; review storyboard-frame cost and choose which videos need an optional **分镜图**; create and present each actual **脚本** or **分镜图 + 脚本** package; confirm the packages; generate only that round; repeat for later rounds.
- Keep that explanation and next-step guidance in conversation, not inside `storyboard.md`. Launch `dynamic_questionnaire` only after presentation and explanation, using `确认故事母版` / `需要修改` plus an open change request and no custom/other option. If revised, re-present the actual revised file and repeat the relevant explanation before launching the form again.
