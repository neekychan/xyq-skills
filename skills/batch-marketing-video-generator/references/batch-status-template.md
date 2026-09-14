# _internal/batch-status.md Template

Use this structure for `_internal/batch-status.md`. This is internal only. Do not present it as a user-facing business deliverable.

```markdown
# Internal Batch Status

## Current
- Project directory: /workspace/batch-video-projects/...
- Batch mode: active / explicitly exited; activation or exit source/time:
- Current stage:
- Latest user authorization:
- Next action:
- `marketing-video-creator` creative knowledge loaded for this batch: no / yes / failed; source/time:
- `image_generate` image knowledge loaded before first image generation: no / yes / failed; source/time:
- Speaking-identity anchors: not assessed / role inventory incomplete / voice descriptions awaiting confirmation / generating neutral samples / awaiting presentation / awaiting confirmation / accepted / not applicable; every narrator/dialogue/monologue/off-screen role, language, accepted timbre and relevant baseline tone, anchor path, explicitly shared performer if any, and source/time:
- Information understanding: missing / drafted / accepted / needs update
- Information file presentation: not presented / presented / failed / needs re-presentation
- Creative assistant: not started / running / complete / blocked / explicitly skipped / stale after information change
- Creative assistant accepted-information version, task request/time, System Prompt file, child `sandbox_bash` time command/raw output, derived current date/timezone, platform priorities, freshness windows, previous/current handoff, cumulative explored-direction registry, historical deduplication validation, search count/types, heat evidence, negative-news safety validation, concise conclusions, and user-facing recommendation-and-basis note delivered yes/no with summary:
- Storyboard: missing / drafted / accepted / needs update
- Storyboard file presentation: not presented / presented / failed / needs re-presentation
- Complete virtual-machine packages: missing / partial / awaiting confirmation / confirmed / needs update
- Execution route: generation quantity not confirmed / authorized IDs selected / not evaluated / direct actual package / target lowering pending / target lowering ready / running / complete / needs reevaluation
- Planned total:
- Planned total confirmation/source:
- Completed video IDs:
- Remaining video IDs:
- Current preparation round:
- Preparation-round requested quantity:
- Preparation-round quantity confirmation/source:
- Preparation-round selected video IDs:
- Confirmed ready but ungenerated video IDs:
- Video-generation round: not started / quantity awaiting answer / authorized / running / complete
- Video-generation round number, requested quantity, confirmation/source/time, selected video IDs, and ready-but-excluded video IDs:
- Current-round product view/state coverage: not assessed / router awaiting answer / upload branch selected / awaiting actual upload / upload received, re-audit pending / detail branch selected / details needed / factual summary awaiting confirmation / generation authorized / generating / awaiting reference presentation / awaiting reference confirmation / accepted reference / skip branch selected / risk confirmation pending / skipped with accepted risk / covered by user media; per-SKU required states, latest form ID, actual answers, and source paths:
- Current-round visual-storyboard coverage: blocked by product consistency / awaiting cost disclosure / awaiting decision / decided; per-video visual / script-only choice, disclosed frame-call cost, confirmation source/time:
- Current-round complete resources: not started / preparing / awaiting confirmation / changes requested / confirmed
- Current-round on-screen character anchors: not assessed / missing / generating / awaiting confirmation / accepted / not applicable; identities and source paths:
- Current-round complete files presented through `present_sandbox_file`: no / partial / yes
- All presented file paths/versions, stage, and result:
- Latest questionnaire stage/path: not launched / awaiting answer / answered; closed choice and open-text summary:

## Execution Capability And Call Units
| Video | User target duration | Video model | Disclosed max duration/call | Capability source/check time | Direct-execution result/blocker | Required calls | Runtime call durations and finished-video ranges | Execution state |
|---|---|---|---|---|---|---|---|---|
| 01 |  |  |  |  | direct / blocked by concrete hard constraint | 1 / N |  | not authorized / direct / lowering pending / lowered / needs reevaluation |

## Files
| Kind | Path | State | Notes |
|---|---|---|---|
| information | information-understanding.md |  |  |
| creative-handoff | _internal/creative-assistant-handoff-v01.md | internal only | accepted-information version / complete / blocked / stale |
| story-master | storyboard.md (user-visible: 故事母版) |  |  |
| storyboard-grid-01 | storyboard-grid-01.png | optional: not selected / selected / generated / accepted |  |
| script-01 | generation-plan-01.md |  |  |
| voice-anchor-01 | assets/anchors/voice/voice-anchor-01.wav | internal generation reference; presented for voice confirmation | neutral text / exact speaking role |

## Complete Virtual-Machine Package Progress
| Video | Round | Confirmed exploration direction | Package mode | Complete script | Optional storyboard-frame cost decision | Exact image-model disclosure/source/time | Image route and calls/used cells | Raw frames | Source manifest | Optional complete storyboard sheet/dimensions | Package confirmation | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 01 |  |  | visual / script-only | generation-plan-01.md | selected + disclosed calls / skipped + zero storyboard-frame calls | exact `seedream_5.0_pro` + source/time / `seedream_5.0` / other / absent / not needed | contact sheets only for exact Pro disclosure; otherwise one shot per call / none | optional | optional: _internal/storyboard-sheet-01.json | optional: storyboard-grid-01.png; WxH; complete and readable | not prepared / awaiting / changes requested / confirmed | planned / generating / generated / blocked / skipped / failed |  |

## Direct References, Generated Anchors, And Derived References
| Video | Shot count | User-provided direct references | Product state references / accepted skip | Agent-generated canonical anchors | Separate style reference | Other derived state/continuity refs | Paid reference reason and confirmation | Per-image-call payload coverage |
|---|---|---|---|---|---|---|---|---|
| 01 | duration-driven confirmed count `S` | paths and entity roles; reused unchanged | paths + covered states / exact skipped risk | none / paths and entity roles |  | none / paths and purpose | not needed / reason + awaiting / confirmed | candidate / ordered ImageList + `图[N]（语义）` mapping / omitted with hard-limit reason |

## Speaking Identity Anchors
| Speaking role ID | User-facing role | Speech use | Videos/shots | Language | Accepted timbre | Role/campaign baseline tone/energy/rhythm | Neutral TTS text | Anchor path | Presentation/confirmation | Explicitly shared performer | Video-call AudioList coverage |
|---|---|---|---|---|---|---|---|---|---|---|---|
| narrator-01 | 旁白 | narration | 01, 02, ... | zh / en |  |  | unrelated to product/script | assets/anchors/voice/voice-anchor-01.wav |  | no | every applicable direct/lowered/retry call / missing |
| character-xiaolin | 小林 | dialogue / monologue | 01 shots 2-4 | zh / en |  |  | unrelated to product/script | assets/anchors/voice/voice-anchor-02.wav |  | no | every applicable direct/lowered/retry call / missing |

## Internal Runtime Calls
| Video | Part | Local time | Finished-video time | Handoff | Internal prompt | Optional internal storyboard input | Image dimensions <6000 when present | Tool-call status | Actual prior end-frame/reference passed | Part output |
|---|---|---|---|---|---|---|---|---|---|
| 03 | 01/02 | 00:00-00:08 | 00:00-00:08 |  | _internal/runtime/video-03/generation-input-part-01.md | _internal/runtime/video-03/storyboard-input-part-01.png | yes / no | planned / generating / generated / needs revision / failed | none; opening part |  |
| 03 | 02/02 | 00:00-00:07 | 00:08-00:15 |  | _internal/runtime/video-03/generation-input-part-02.md | _internal/runtime/video-03/storyboard-input-part-02.png | yes / no | waiting for prior part / planned / generating / generated / needs revision / failed |  |  |

## Decisions
- YYYY-MM-DD HH:mm:
```

Rules:

- Keep this file concise and operational.
- Keep `Batch mode` marked `active` after this skill is loaded, across context compression, resume, revisions, retries, single-video rounds, and completed rounds. Mark it `explicitly exited` only when the user clearly says batch production is cancelled, no longer needed, or replaced by a non-batch workflow; record the exact user wording and time. A request scoped to one video or one round is never sufficient evidence of exit.
- Store the active project's absolute `/workspace/batch-video-projects/...` path here and use it for resume and file resolution; never depend on an arbitrary current working directory.
- It may contain status, paths, generation outputs, failures, retries, and recovery notes.
- Do not copy long product facts, storyboard tables, or full scripts here; link to the user-facing files instead.
- Record each conversation-confirmed video direction and its mandatory one-to-one mapping to `generation-plan-XX.md`. Record raw visual frames, source manifest, and complete `storyboard-grid-XX.png` only when that video is explicitly in visual mode.
- After `information-understanding.md` is accepted and before `storyboard.md` is written, record the creative-assistant `task` request, exact System Prompt file path, accepted-information version, the child's `sandbox_bash` time command/raw output and derived date/timezone, platform priorities, expected output handoff, task result, actual search count/types, searched date windows/platforms, available heat evidence, negative-news safety validation, and concise conclusions. The main Agent does not fetch or infer the child's current time. Keep the handoff internal and never mark research complete from a task response when the expected file is missing, empty, blocked, stale, lacks child-obtained system time, is platform-blind, or uses tragic/harmful negative news as inspiration. Before story-master writing, separately record that the main Agent gave the user a concise recommendation-and-basis note grounded in accepted facts, audience fit, actual platform evidence, and historical differentiation; this note is informative and creates no new confirmation gate.
- Reuse a complete handoff across ordinary production rounds. Mark it stale and run a successor with the latest valid previous handoff only when accepted information changes a creative premise, the user requests fresh research/new creative families, or existing directions are exhausted or rejected. Record whether the successor read the supplied handoff, preserved and updated its cumulative explored-direction registry, and provided substantive differences rather than renamed repeats. Record an explicit user-authorized skip separately from failure.
- Record the `image_generate` load result before the first image-generation call. On resume, a recorded success prevents duplicate loading; a missing or failed record requires a successful `load_skill` call before any new anchor, derived-state, contact-sheet, individual-shot, or replacement-image generation.
- Immediately after current-round IDs are selected, complete and record product consistency for every selected SKU before disclosing optional storyboard-frame cost or asking for visual/script-only mode. Only after that gate is complete, record the cost and user's per-video choice. For visual mode, record that the complete sheet was completed and inspected before its complete script. For script-only mode, record zero storyboard-frame calls and verify the script has no missing-grid dependency. Record that every actual package was presented and confirmed before direct execution or target lowering.
- For visual-mode videos, record the exact active image-model identifier disclosed by the current runtime/tool context, its disclosure source and check time, selected route, and complete preview dimensions. Do not infer or normalize model names. The full user-facing preview may exceed `6000px`; record whether `--no-max-dimension` was used and whether it remains readable. Do not invent an image-model route for a skipped grid unless another required image asset is actually generated.
- Record every accepted local shot replacement by video ID and shot number, including replacement image path/version and whether visual, timing, audio, and `voiceover` fields were synchronized to the manifest and complete generation script.
- Record the user's target finished-video duration and the story/shot count from the accepted storyboard whose creative content applied the learned `marketing-video-creator` knowledge.
- Only after video-generation-round quantity is confirmed, record the selected video model's disclosed capabilities and direct-execution check for the execution-selected IDs across duration, ratio, reference-media limits/types, script/input limits, generation mode, other hard constraints, and complete-sheet dimensions/file support only when a sheet exists. Do not evaluate ready-but-unselected packages yet. Recheck when model selection or capability changes.
- If the actual package fits, mark the route `direct actual package`, required calls `1`, and do not create `_internal/runtime/`. If direct use is blocked, record the exact hard constraint, the minimum required adaptation, and why any multi-call count is minimal. Do not lower or split for creative or implementation convenience.
- For every complete video, record shot count `S` separately from image-call cost. For an opted-in grid, only an explicit current disclosure of exact `seedream_5.0_pro` uses `ceil(S / 9)` contact-sheet calls; `seedream_5.0`, every other/ambiguous model, or no disclosure uses `S` one-shot calls. For a skipped grid, record zero storyboard-frame calls. Character anchors, product-state references, and hard target-required images remain separate costs.
- Record user-provided direct references separately from agent-generated canonical anchors and derived-state/continuity references. A usable supplied product/entity image must show `reused unchanged` and must not have a paid generated baseline. For every generated anchor, record the new identity it establishes, why existing media or text was insufficient, and the user's confirmation; the first accepted generated image is the baseline.
- Before the visual-storyboard question, package preparation, or related image/video generation, record each selected SKU's required visible views/states, which actual user images cover them, every uncovered detail, and the user's resolution choice. Record branch selection separately from branch completion. For upload, record the actual returned media paths and re-audit result; prose or a selected submit option is not an upload. For details, record the actual text answers, unresolved fields, factual summary, planned calls, and explicit generation authorization. For a generated product state reference, record actual paid image calls, intermediate state paths when used, final `assets/anchors/product-states/...` path, presentation result, and acceptance. For skip, record the exact warned risk and the separate explicit acceptance. Never treat a router answer, missing response, generic confirmation, skipped grid, or unrelated user message as completion of any branch. Keep visual-storyboard coverage marked `blocked by product consistency` until every affected SKU is resolved.
- Before finalizing a package or generating any image/video containing an identifiable character, record that character's exact accepted anchor path and source (`user direct` or `generated canonical`). When missing, record paid-call confirmation, generated path, `present_sandbox_file` result, and acceptance. Never mark current-round character anchors complete while an appearing identifiable character has no accepted image anchor, even when its grid was skipped.
- Before finalizing the first package containing speech, inventory narrator, dialogue characters, monologue characters, and off-screen speakers separately. Record each recurring role's accepted timbre plus role/campaign-relevant baseline tone/energy/rhythm and exact video/shot use. Distinct roles use distinct anchors unless the user explicitly confirms one performer/voice for several roles. If a role lacks an accepted neutral anchor, generate exactly one with `sandbox_generate_audio` using only `Type: tts`, supported `Lang`, unrelated neutral `Text`, accepted `VoiceDesc`, and absolute `OutputPath`; omit `AudioList` and all other optional fields for this new neutral anchor, and never use it for actual narration, dialogue, monologue, BGM, sound effects, or environment sound. Record neutral text, actual call, path, role-labeled presentation result, and user confirmation. Its words must be unrelated, but its delivery tone must fit that role and campaign.
- For every contact-sheet batch, individual-shot, generated-anchor, or derived-state image call, record all candidate relevant references; the exact ordered `ImageList`; each path's one-based `图[N]（语义信息）` Prompt label; `OutputRatio`, `OutputPath`, and `IsIntermediate: true`; and any omitted relevant references. Never record or pass a `Model` tool argument. Omission is allowed only for a disclosed hard count/type/size limit. Record the priority decision and never treat a filename/path in Prompt as an attachment or semantic identity.
- Record the target `video_ratio` and resulting compositor layout: width >= height uses a vertical list; width < height uses a horizontal strip.
- Only for target lowering, record one row per internal call, including local and finished-video ranges, intended handoff, internal prompt, optional same-suffix internal sheet, target dimension check when an image exists, actual prior-part continuity reference, and call status. Leave this section unused for direct execution. The finished-video count remains one.
- Keep finished-video absolute ranges in this status file and `runtime-manifest.json` only. Model-facing `generation-input-part-YY.md` files and runtime storyboard images use local timecodes starting at `00:00`.
- Run split calls sequentially. Do not mark a later part ready to call until the prior part has been inspected and its actual handoff recorded.
- Keep each part output and record the final concatenated video under the parent video ID.
- Record the preparation round before creating any per-video resources. Never infer that all remaining videos belong to it.
- Keep planned total, preparation-round quantity (the existing current-round quantity), and video-generation-round quantity independent. Default planned total is a recommendation of 6; both round quantities separately recommend 1. Planned total controls directions, preparation quantity controls scripts/optional grids, and video-generation quantity controls actual execution-selected IDs. Never fill one from another.
- Record successful `present_sandbox_file` presentation of the actual `information-understanding.md` before marking information understanding accepted, and of the actual `storyboard.md` under the user-visible name **故事母版** before marking it accepted. Also record that the post-presentation shared-batch explanation and next-step explanation were given before the confirmation form. A conversation summary alone is insufficient. Revisions require re-presentation.
- Record whether every current-round mandatory `generation-plan-XX.md` and every selected optional `storyboard-grid-XX.png` was successfully presented through `present_sandbox_file`, including actual paths/versions and package mode. Do not mark packages awaiting confirmation until all files that actually belong to them were presented successfully. Package confirmation records content readiness only and never records video-generation quantity or execution authorization.
- Immediately before any execution capability evaluation, target lowering, or video call, record a separate video-generation-round quantity and selected IDs. If no explicit execution-scoped quantity exists, the questionnaire is mandatory and recommends one video even when every script/grid already exists and is confirmed. Record ready-but-unselected IDs separately and leave their packages unchanged. Generic confirmation/continuation, planned total, preparation quantity, package confirmation, or a prior generation round never satisfies this gate.
- Record the relevant `dynamic_questionnaire` stage and response whenever progress pauses for confirmation. Treat a material open-text correction as a revision request even if the closed choice says confirm.
- For every video-generation call, record prompt transport as either `Prompt="" + PromptPath=<absolute self-contained file>` or `Prompt=<complete expanded text> without PromptPath`, plus the actual `ImageList` and ordered `AudioList`. For narration/dialogue/monologue, record the one-based `音频[N]` to speaking-role mapping; verify that every role speaking in that call has its exact accepted anchor, no silent/irrelevant role is added without reason, and the transported prompt says each sample is timbre-only, forbids sample words/timing, and follows the script's speaker assignments and actual lines. Reattach the same role anchor to every direct, lowered-part, and retry call where that role speaks. Never record or use a placeholder prompt that tells the model to read a file.
- After a video-generation round completes, update completed IDs, clear only that execution authorization, and ask again before generating any ready remainder. Keep unchanged package confirmations. Clear preparation-round resource state only when moving to a genuinely new preparation round.
- On resume or "continue", read this file first, then read the relevant user-facing deliverable.
