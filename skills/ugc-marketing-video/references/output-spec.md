# UGC Marketing Video Output Spec

Use this reference as the final output contract for concrete UGC marketing video, product sales video, seeding, review, local-deal, game/IP/event, reference-remake, creator-portrait-to-script, storyboard-prompt, or video-generation tasks.

The goal is to keep the user-facing chat clear and lightweight while preserving a detailed internal generation chain: Nano Banana Pro creator portrait, direct user-facing script, and a complete `seedance_generation_package` passed to the video generation tool.

## Mandatory Reference Gate

This output spec must not be used alone. Before writing the user-facing script or compiling `seedance_generation_package`, the agent must use `sandbox_read` with workspace-form paths to read the mandatory references declared in `SKILL.md`, including `/workspace/.skills/ugc-marketing-video/references/seedance-generation-contract.md`, plus category, platform and diversity references when relevant.

The required reference set also includes `/workspace/.skills/ugc-marketing-video/references/input-consistency-rules.md`, `/workspace/.skills/ugc-marketing-video/references/creator-persona-library.md`, `/workspace/.skills/ugc-marketing-video/references/hook-library.md`, `/workspace/.skills/ugc-marketing-video/references/benefit-voiceover-library.md`, `/workspace/.skills/ugc-marketing-video/references/cta-library.md`, `/workspace/.skills/ugc-marketing-video/references/marketing-expression-rules.md`, `/workspace/.skills/ugc-marketing-video/references/text-accuracy-rules.md`, and `/workspace/.skills/ugc-marketing-video/references/seedance-generation-contract.md`. Read `/workspace/.skills/ugc-marketing-video/references/diversity-rules.md` when generating multiple options or variants.

If those references have not been read with `sandbox_read`, stop and read them before generating the prompt. Keep the reference-reading process internal and do not mention it in the user-facing answer.

## Output Split

Separate the workflow into visible and internal layers:

1. **Visible `creator_portrait_image`**: the active supplied or Nano Banana Pro generated creator image reference.
2. **Visible `script`**: a concise 15-second UGC sales script that maps hook, visible action, benefit line, optional short in-frame text, product proof and CTA.
3. **Internal routing and checks**: reference loading, category judgment, platform rules, product-proof logic, text checks, physical checks and quality checks.
4. **Internal `seedance_generation_package`**: the complete self-contained video-tool payload. It contains material IDs, product identity, creator identity, global visual rules, lighting, camera, per-shot instructions, audio/text behavior, continuity and final checks.

Default behavior:

- For normal user requests, do not create a separate markdown file. This UGC skill should usually return a compact chat answer.
- Create a separate spec markdown only when the user asks for a full plan, multiple routes, a reusable strategy document, audit notes, or when the answer would otherwise become long.
- Do not output hidden reference-reading steps, category scoring, rejected routes, or long strategy notes by default.
- Keep `seedance_generation_package` hidden by default. Show it only when the user explicitly asks for the full Seedance prompt, model instructions, video-tool payload, or audit details.
- If the user asks for multiple options, provide 2-3 compact routes; each route should still have a usable prompt or a clearly stated next step.
- After the creator portrait and script are visible, call `dynamic_questionnaire` once to ask whether to continue video generation or revise first. Do not rely on a plain-text consent sentence.
- If the user confirms the creator portrait and script by selecting `继续生成视频`, proceed directly to video generation when a video-generation tool is available.
- If the user asks to adjust the creator portrait, revise the portrait first with `sandbox_generate_image` using Nano Banana Pro instructions, then update the script and internal generation package.

## Default Chat Template

Use this shape for the first visible response after a normal UGC marketing-video request.

````text
creator_portrait_image
{已提供或 Nano Banana Pro 生成的达人画像引用。}

脚本
```text
0-3s: {直接画面动作}；口播：“……”；可选短花字：“……”
3-7s: {直接画面动作}；口播：“……”；可选短花字：“……”
7-12s: {直接画面动作}；口播：“……”；可选短花字：“……”
12-15s: {直接画面动作}；口播：“……”；可选短花字：“……”
```

确认达人形象和脚本后即可开始生成视频；商品一致性、场景、光影、构图、运镜、动作、声音、文字和连续性细节会通过内部生成包直接传给视频工具。
````

After this visible response, call `dynamic_questionnaire` with one radio question:

- `继续生成视频`: continue with video generation from the displayed creator portrait, script, materials, and internal generation package.
- `先修改方案`: wait for revisions and do not generate video yet.

For Chinese users, keep the output in Chinese. Keep only product names, brand names, platform names, model names, and widely recognized tool names in their original language.

## Rationale Rules

The rationale should be useful but short:

- Explain the hook, proof, and CTA logic in normal user language.
- Mention the primary selling point or usage scene.
- Do not expose "I read references", "I selected scenario 1", "quality checklist", "risk check", or other internal workflow labels.
- Do not turn the rationale into a long marketing strategy memo.

Good rationale pattern:

```text
这条视频先用真实使用场景把商品放到用户眼前，再用一个可见动作证明核心卖点，最后用自然口播收束到购买/咨询/到店动作。这样比单纯展示商品更容易让观众理解“为什么现在需要它”。
```

## Internal Generation Contract

Before video generation, compile `seedance_generation_package` using `seedance-generation-contract.md`. It must include:

- duration and ratio, default `15秒，9:16竖版`
- platform/content assumption, default `抖音 UGC 带货视频`
- `material_manifest` with stable IDs and authority roles for every product, screenshot, reference and creator asset
- a detailed `product_identity_lock` covering silhouette, proportions, colors, material, package, logo, label, structural details, scale, variants, accessories and verified claims
- `creator_identity_lock` based on the active Nano Banana Pro or user-supplied portrait
- `global_visual_bible` covering scene, background layout, color, light, exposure, white balance, depth of field, camera height, lens feel and motion style
- one primary selling point per video unless the user explicitly asks for more
- product visible early, normally within the first 3 seconds
- active creator portrait reference: if no suitable person image was supplied, use the Nano Banana Pro generated `creator_portrait_image` returned through `sandbox_generate_image`
- video reference/垫图 list: pass `video_generation_materials` with `seedance_generation_package`; user-uploaded product/reference materials define product appearance, and `creator_portrait_image` defines the protagonist/person identity
- creator persona richness: bind `主体1` with role, age band, hairstyle/outfit, scene, product relationship, and speaking tone from the persona library
- detailed `shot_instructions` for `0-3s / 3-7s / 7-12s / 12-15s`
- selected hook mechanism in 0-3s
- benefit voiceover lines in 3-7s and 7-12s that translate feature into human value
- platform-matched CTA in 12-15s with one clear next step
- input consistency control: product, offer, CTA, and visual facts stay aligned with user assets
- finished-video stability control: 4 stable shots, at least 3 seconds per shot, one main action per shot
- creator authenticity control: same confirmed creator portrait, role, face, outfit logic, and speaking tone
- physical/spatial control: sequential handling, stable support, real scale anchors
- text accuracy control: short exact text, safe placement, subtitles only when requested
- audio-visual sync control: one short spoken line per shot, lip sync, BGM below speech
- marketing control: one main selling point with visible proof and one CTA
- a stable protagonist definition when any person appears: define `主体1` with 2 to 4 visible traits, role, and relation to the product; reuse `主体1` across all person shots
- a clear product relation in every beat
- Chinese spoken lines by default
- subtitles only when the user explicitly asks for subtitles or provides subtitle copy
- short in-frame text only when it helps explain an offer, result, selling point, product name, or CTA
- safe placement for any requested subtitles or in-frame text
- visible proof through action, result, comparison, reaction, store evidence, screen bridge, or use process
- if using an absurd interruption, meme, or surprising visual hook, it must return to product and selling point by the first half of the video
- product consistency: appearance, color, SKU, package, logo, material, size, and variants follow user assets
- protagonist consistency: if a reference person is provided, keep that person's visible identity cues; if no person reference is provided, use a lightweight product-appropriate UGC persona without exaggerated beauty traits
- physically plausible handling: one main action per shot, sequential operation, visible support
- natural transition points after completed action, expression change, product placement, result reveal, or music beat
- a natural CTA that fits the platform and product
- per-shot lighting fields: source, direction, softness, color temperature, fill, product highlight, exposure and continuity
- per-shot camera fields: shot size, angle, camera height, lens feel, framing, focus, stabilization, movement, movement start/end/speed/distance and hold time
- per-shot product state: source asset ID, SKU, orientation, support, scale anchor, start state and end state
- per-shot action mechanics: acting hand, entry direction, grip/contact point, physical response and stable end state
- `continuity_ledger` connecting creator position, hand position, product position/orientation/state, scene, light direction, camera height, gaze and audio

## Timing Rule

Prefer a stable 4-shot structure for 15 seconds:

```text
0-3s: 钩子 / 具体优惠 / 结果前置，商品可见
3-7s: 回到商品和主卖点，开始上手或场景证明
7-12s: 展示可见结果、对比、细节、反应或流程证明
12-15s: 价值确认 + 自然 CTA，产品仍在画面中
```

If a reference file or platform pattern requires 5 beats, only use 5 beats when it improves clarity. Do not split into many tiny shots that make generation unstable.

## Tool Payload Style

Write the internal tool payload as positive execution instructions.

- Use words like `保持`, `展示`, `呈现`, `拿起`, `放下`, `承接`, `完成`, `回到`, `同步`, `复用`, `放置`.
- Convert negative constraints into positive actions before visible output.
- Keep process and safety checks internal when they are naturally negative.
- The tool payload describes what the model creates, maintains, shows, connects and completes.

## Confirmation And Revision

When the user confirms:

```text
已确认，我将按这个达人形象和脚本，使用完整内部生成包开始生成视频。
```

Only treat the user as confirmed when they select `继续生成视频` in `dynamic_questionnaire` or explicitly request generation after seeing the current creator portrait and script. Then proceed to video generation when available.

When the user asks for a change, revise the visible script and the internal `seedance_generation_package`, then keep the same visible output shape:

````text
脚本
```text
{更新后的直接时间轴脚本}
```

确认后即可基于这个版本开始生成视频。
````

If the change targets the creator portrait, call `sandbox_generate_image` again with Nano Banana Pro instructions, show the updated `creator_portrait_image`, and refresh the script and internal generation package. Do not restart the full parameter flow unless the requested change depends on a missing core asset or an impossible decision.

## When To Create A Separate Plan File

Create a separate markdown creative-plan file only when useful:

- user asks for full plan, full strategy, multiple routes, or audit/review
- the answer would otherwise become long
- the user needs a reusable plan for a team or production workflow
- the user asks to compare platforms, content types, or categories in detail

If a separate file is created, keep chat compact and put detailed reasoning in the file. For Chinese users, call it `完整创意方案` or `品牌片方案稿`; do not use the word `spec` in visible Chinese chat unless the user used it first. The final chat still includes the direct timestamped script.

Use this compact chat shape after creating or referencing the complete creative plan markdown:

````text
大的思路总结：
{用 2-4 句话说明核心创意、为什么这样拍、品牌 / 产品怎么起作用。不要堆 bullet point，不展开完整推导。}

完整创意方案可见：
{relative_path}

脚本：
```text
{direct timestamped script}
```
随后使用 `dynamic_questionnaire` 询问：
- `继续生成视频`
- `先修改方案`
````

If the user only asks for strategy, do not fabricate a prompt. Explain the split and apply the creative-plan template only as far as the request needs.

Suggested markdown title:

```markdown
# UGC营销视频方案 - {产品/项目名}
```

Suggested sections:

```markdown
## 结论
- 推荐内容路线：
- 主卖点：
- 一句话创意：
- 转化动作：

## 商品与人群
- 产品真相：
- 目标用户：
- 使用场景：
- 核心顾虑：
- 可见证明：

## 视频结构
- 开头钩子：
- 卖点证明：
- 画面动作：
- 口播：
- CTA：

## 15秒节奏
- 0-3秒：
- 3-7秒：
- 7-12秒：
- 12-15秒：

## 生成控制
- 视觉质感：
- 商品一致性：
- 可选字幕与花字：
- 转场：
- 物理动作：
- 风险点：
```

## Quality Guard

Before final output, check:

- The answer uses the compact user-facing shape and avoids a long strategy dump.
- The active creator portrait is present before script and video generation when no suitable person reference was supplied.
- Internal `video_generation_materials` includes user-uploaded materials plus the active creator portrait.
- The script is present and matches the active creator portrait.
- Internal `seedance_generation_package` is self-contained and directly usable by the video tool.
- Each relevant reference conclusion is compiled into a package field, shot field or final check.
- The package contains product identity, creator identity, source material IDs, light, camera, action, sound, text and continuity.
- A default phone-camera visual system is used when no other style is specified.
- Product appears early and remains tied to the action.
- If subtitles are requested, speech and subtitles match.
- Chinese remains the default visible language.
- One main selling point is emphasized.
- The CTA is natural and not too long for the final seconds.
- Internal reference loading and quality checks are not exposed.
- Absurd hooks remain staged, non-injurious, and product-led.
