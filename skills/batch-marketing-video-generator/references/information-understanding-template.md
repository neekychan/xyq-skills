# information-understanding.md Template

Use this fixed structure for `information-understanding.md`. This is a user-visible business deliverable. Keep it concise and readable.

```markdown
# 信息理解

## 1. 商品与目标
| 项目 | 内容 |
|---|---|
| 商品/品牌 |  |
| SKU/变体/套装 |  |
| 目标人群 |  |
| 使用场景 |  |
| 视频目标 |  |
| 计划总数 | 用户指定并确认 N 条 / 用户未指定，已推荐并确认 6 条 |
| 目标语言/市场 |  |
| 比例/时长 |  |
| 声音与字幕 | 可使用旁白、角色对白和角色独白；不生成字幕 |
| 已知的说话角色与声音方向 | 记录用户已指定的旁白/角色声音要求；尚未设计的创意角色标注“待故事确认后确定”，不要在事实阶段虚构 |

## 2. 卖点与可用事实
| 信息 | 内容 | 来源 | 使用边界 |
|---|---|---|---|
| 核心卖点 |  |  |  |
| 证明点/效果展示 |  |  |  |
| 规格/材质/参数 |  |  |  |
| 价格/优惠 |  |  |  |

## 3. Hook 与 CTA
| 项目 | 内容 | 是否已确认 |
|---|---|---|
| 可用 Hook 方向 |  | 是 / 否 |
| CTA 语气 |  | 是 / 否 |
| CTA 具体渠道/落地页 |  | 已确认 / 未确认，使用通用 CTA |

## 4. 固定内容与探索方向
| 类型 | 内容 | 是否已确认 | 说明 |
|---|---|---|---|
| 固定内容 | 商品事实 / 核心卖点 / 语言 / CTA规则 / 视觉基准 / 时长比例 | 是 / 否 |  |
| 商品/SKU探索 | 多商品 / 多SKU / 颜色 / 口味 / 套装 / 价格档位 | 是 / 否 / 不适用 |  |
| 角色探索 | 同一角色 / 不同角色 / 手模 / 达人 / 顾客类型 | 是 / 否 / 不适用 |  |
| 场景探索 | 使用场景 / 人群 / 场地 / 时间 / 情绪 | 是 / 否 / 不适用 |  |
| 表达探索 | Hook / 卖点角度 / 证明方式 / CTA语气 / 风格节奏 | 是 / 否 |  |
| 推荐测试组合 |  | 待用户确认 / 已确认 |  |

## 5. 素材检查
| 素材 | 对应内容 | 用途 | 是否可直接使用 | 备注 |
|---|---|---|---|---|
| A01 |  | 商品 / 人物 / 场景 / 风格 / 不确定 | 是 / 否 / 需确认 |  |

## 6. 实体与视觉参考
| 检查项 | 来源与结论 | 说明 |
|---|---|---|
| 商品/包装参考 | 用户提供，直接复用 / 需主动生成 / 不需要 | 用户已有可用商品图时禁止再生成商品基准图；保留实际素材状态并直接引用 |
| 分镜预计需要的商品角度/状态 | 正面 / 背面 / 侧面 / 顶部 / 底部 / 开合 / 拆装 / 内容物 / 使用状态 / 其他 | 按商品/SKU分别记录；只列创意预计会用到的内容 |
| 商品状态素材覆盖 | 已覆盖 / 部分缺失 / 未提供 | 列出现有素材已覆盖和仍缺少的角度、状态与细节；本轮方向确定后先完成精确检查与缺口处理，再询问是否生成分镜图 |
| 缺失状态处理 | 等待用户补充实拍 / 补充细节后生成状态参考图 / 用户确认跳过风险 / 不需要 | 生成参考图或跳过都必须由用户明确确认 |
| 角色参考 | 用户提供，直接复用 / 已有已确认基准 / 需主动生成 / 不需要 | 任何可识别出镜角色都必须有角色图锚点；用户有可用角色图时直接复用，否则在完成对应视频包或生成相关画面前生成并确认一次基准图；仅匿名背景人群可标记不需要 |
| 场景参考 | 用户提供，直接复用 / 需主动生成 / 不需要 | 仅当 Agent 主动创造新场景且需跨镜保持一致时生成一次空场景基准图 |
| 道具参考 | 用户提供，直接复用 / 需主动生成 / 不需要 | 仅当 Agent 主动创造关键道具且需跨镜保持一致时生成一次基准图 |
| 风格/灯光/色调参考 |  | 与实体参考分开记录 |
| 是否需要派生状态参考 |  | 例如开封商品、持续液位、特定摆放；不得覆盖用户原始素材或已确认的主动生成基准 |
| 逐镜生成时需实际附带的参考 | 用户原始素材 / 主动生成基准 / 风格 / 已确认派生状态 |  |

## 7. 待确认信息
| 问题 | 为什么需要确认 | 不确认时的处理方式 |
|---|---|---|
|  |  |  |
```

Rules:

- Do not include status/logs, workflow history, internal file decisions, tool details, or long reasoning.
- Write and confirm this factual boundary before launching the creative assistant. Do not use network inspiration or a creative-assistant handoff to author or revise product facts in this file; the handoff belongs only to later story-master and direction work.
- Record only facts useful for storyboard and script writing.
- Record the user's intended duration for each finished video under `比例/时长`. This creative target is separate from the selected video model's per-call maximum and must not be silently shortened to fit one tool call.
- Mark unknown or conflicting product facts plainly. Do not turn them into claims.
- Explicitly separate fixed content from exploration directions. Batch generation should not move to storyboard until the exploration direction is confirmed.
- Exploration directions can be product/SKU, character, scene, audience, Hook, selling-point angle, proof method, CTA tone, rhythm, or style.
- If the input contains multiple products/SKUs/variants/bundles/colors/flavors/price tiers, treat product/SKU as a possible exploration direction and ask whether the user wants to compare them, combine them, or focus on one.
- If the user did not specify what to explore, use `dynamic_questionnaire` to recommend a compact mix and request confirmation through closed choices plus an open direction question. Include `按你推荐组合` as an acceptable business choice, but do not add a custom/other option.
- Put asset checking here, but keep it to conclusions: usable materials, missing materials, role ambiguity, which user images will be reused directly, and whether any new agent-created identity genuinely requires a generated reference.
- Preserve every relevant user image as a separate material entry with its product/SKU, entity, scene, prop, or visual-style role. Do not keep only one representative image when the remaining images can add useful identity, angle, packaging, environment, or style information to later storyboard-frame calls.
- Record known or anticipated product views and states separately for each SKU. Examples include device front/back/ports/screens, bottle cap-on/cap-off/seal/liquid level, cosmetics closed/opened/dispensed, packaging sealed/torn/content-visible, apparel front/back/fastened/worn, footwear side/sole/laced, bags zipped/open/interior, appliances closed/open/attachment/display, furniture folded/unfolded/drawer-open, and vehicles with doors/trunk/charging-port open or closed. Do not request states the creative direction will not use.
- If current materials are likely insufficient, record the conclusion and the three permissible next choices: upload real views (recommended), describe and confirm hidden/state details before generating a product state reference, or explicitly skip with consistency risk. Do not invent the user's selection in this file.
- A usable user-provided product or entity image is the direct reference. Do not prescribe or generate a second clean, isolated, neutral, redrawn, or same-state confirmation baseline for it, even when its background or state is not ideal. A supplementary product state reference is permitted only for a confirmed-story view/state that the source does not show, after the user chooses generation and confirms its missing details and paid calls; it never replaces the source. Ask for a cleaner user source or disclose the limitation when necessary.
- Inventory every distinct identifiable character planned to appear in the batch and state whether its anchor is user-provided, already accepted, or must be generated before the applicable current-round package is finalized or any related image/video generation begins. A hand model, presenter, customer, creator, spokesperson, or other recognizable role requires an anchor; only anonymous background crowds may omit one.
- Generate a canonical entity reference when a required consistency-critical identity lacks a usable user-provided image. For every identifiable appearing character this is mandatory; for other entities it remains limited to genuinely necessary new identities. The first accepted generated reference is its baseline; do not generate a baseline of that baseline. Confirm the reason and paid image call first.
- Apply placement, interaction, opening, pouring, damage, occupancy, and other shot-specific states only in shot-level image or video generation. If an altered state must persist, record a separate derived-state/continuity reference without replacing the canonical anchor.
- When image calls are independent, identify the actual user-provided direct references, agent-generated anchors, and accepted derived references that must be reused across calls. Reusing user assets costs no extra generation call; generate only genuinely new consistency-critical identities and confirm their cost before image generation.
- Resolve planned total before storyboard work. If it is missing, use `dynamic_questionnaire` with `6 条（推荐）`, a few useful closed quantities, and an open constraints question; do not add `其他数量`. Wait for explicit confirmation and do not silently assume the default. Planned total controls the number of exploration directions.
- Record planned total in this file. Do not record preparation-round or video-generation-round quantity here; each authorization belongs in conversation and `_internal/batch-status.md` at its later gate.
- Clearly total-scoped wording supplies planned total. `先准备 N 条方案` supplies only preparation-round quantity; `这一轮先生成 N 条视频` supplies only video-generation-round quantity. If wording such as `先做 N 条` or bare `生成 N 条` is ambiguous for the current stage, ask which scope it refers to. Never copy one quantity into another.
- CTA channel-specific routes must come from the user or be confirmed by the user. If not confirmed, use a generic CTA and do not invent platform/store/search/link/QR/private-message details.
- Preserve user-specified target languages and voice requirements. In this factual file, list only speaking identities already supplied or required by the user; do not invent creative characters before the story is designed. Mark unresolved creative speaking roles as `待故事确认后确定`. After the story master and concrete per-video directions establish the actual cast, inventory narrator, on-screen dialogue roles, character monologues, and off-screen voices under this skill's later speaking-identity gate without reopening this factual file solely because the creative treatment introduced a role. Distinct speaking characters are distinct voices by default, including one-line roles, while an explicitly confirmed same-performer choice may share one voice. Keep visual character identity and speaking identity separate. Never put neutral TTS sample text, anchor paths, tool parameters, or generation status in this file. The default batch requirement is no generated subtitles, captions, dialogue bubbles, title cards, or added screen text; packaging text objectively present in confirmed reference material may remain.
- Complete information collection first; use `dynamic_questionnaire` for every pause that needs user answers, pairing closed choices with an open text question and never adding a custom/other option. Do not repeatedly write and present partial versions as each answer arrives. Once the material information and planned total are sufficiently resolved, create and check the consolidated file, present the actual `information-understanding.md` through `present_sandbox_file`, then show the key content in conversation. Launch its confirmation questionnaire only after presentation succeeds. If revised after review, re-present the actual revised file before launching the form again.
