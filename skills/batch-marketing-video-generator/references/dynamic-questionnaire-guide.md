# Dynamic Questionnaire Guide

Use `dynamic_questionnaire` whenever the workflow pauses for a user decision, confirmation, correction, or material missing answer. Use plain conversation only when the tool is unavailable.

## Form Contract

- Keep `title` concise and no more than 20 words.
- Use stable unique IDs for questions and options.
- Pair at least one closed `radio` or `checkbox` question with one open `text` question.
- Use `radio` for one decision and `checkbox` when multiple selections are valid.
- Put the recommended choice first and label it clearly, for example `6 条（推荐）`, `先准备 1 条方案（推荐）`, or `先生成 1 条（推荐）`.
- Do not add options named `自定义`, `其他`, `其他选项`, `其他数量`, `自行填写`, or equivalents. The form supplies its own custom option.
- Use a separate open question such as `还有哪些内容需要补充或调整？`; keep it optional and provide a useful placeholder.
- Combine related decisions in one form when practical. Do not create a long sequence of one-question interruptions.
- When the form contains only one `radio` question, the runtime schema requires one emoji per option. Prefer the normal closed-question-plus-text shape, which avoids a single-question form.
- For file confirmation, call `present_sandbox_file` first, summarize the content in conversation, and only then launch this form.

## Standard Confirmation Shape

Adapt labels and IDs to the stage. Do not copy a generic option when a business-specific choice would be clearer.

```json
{
  "title": "确认信息理解",
  "questions": [
    {
      "id": "information_decision",
      "title": "这份信息理解是否可以继续使用？",
      "type": "radio",
      "options": [
        {
          "id": "confirm_information",
          "label": "确认并继续",
          "value": "confirm",
          "selected": false
        },
        {
          "id": "revise_information",
          "label": "需要修改",
          "value": "revise",
          "selected": false
        }
      ]
    },
    {
      "id": "information_notes",
      "title": "还有哪些内容需要补充或调整？",
      "type": "text",
      "placeholder": "可填写要修改的事实、卖点、数量、语言或素材说明"
    }
  ]
}
```

## Stage Choices

- Planned total: closed quantity choices headed by `6 条（推荐）`, plus an open constraints question. Do not offer `其他数量`.
- Exploration direction: recommended combination and a few input-relevant directions as `radio` or `checkbox`, plus an open direction-description question. `按你推荐组合` is a real business choice and is allowed; `自定义方向` is not.
- Information understanding: `确认并继续` / `需要修改`, plus open corrections.
- Creative research blocker, only after accepted information when `task`, the System Prompt file, search tool, or expected handoff is unavailable/blocked: `重试创意搜索（推荐）` / `使用现有创意知识继续`, plus an open research constraint. Do not present the internal handoff or ask the user to approve the child's reasoning. Record the second choice as an explicit research skip for that accepted-information version.
- Story master (`storyboard.md`): after successful presentation and the shared-batch/next-step explanation, use `确认故事母版` / `需要修改`, plus open shot/timing/speaking-role/narration/dialogue/monologue corrections. Never call it merely `故事板` in the user-facing form.
- Preparation round: `先准备 1 条方案（推荐）`, useful larger choices, and `准备全部剩余方案` when applicable, plus open notes. This selects how many scripts/optional grids to prepare, not how many videos to generate. Do not offer `其他数量`.
- Product state coverage, immediately after current-round IDs are selected and before any visual-storyboard question: complete the router and its selected follow-up branch for every affected SKU. Product consistency is required for script-only and visual-mode videos alike.
- Visual-storyboard coverage, only after product consistency is resolved and storyboard-frame cost is disclosed: for multiple videos use `仅首条生成分镜图（推荐）` / `本轮全部生成分镜图` / `本轮跳过分镜图，只生成脚本`, plus an open field for a named subset. For one video use `生成分镜图` / `跳过分镜图，只生成脚本`, with the recommendation chosen from actual visual complexity and cost sensitivity. Record the answer per video and do not carry it into later rounds without explicit instruction.
- Complete actual packages: after presenting both files for visual-mode videos and scripts alone for script-only videos, use `确认方案内容，进入生成安排` / `先修改`, plus open revision details. This confirms package content only and never authorizes video calls or supplies a generation quantity.
- Video-generation round: after package confirmation and immediately before any capability check, target lowering, or video call, use `先生成 1 条（推荐）`, useful larger quantities bounded by confirmed ready ungenerated packages, and `生成全部已确认视频` when applicable, plus an open field for preferred video IDs or notes. Ask by default even when every grid and script already exists. Skip only for an explicit execution-scoped quantity; package confirmation, preparation quantity, prior execution quantity, or generic `继续` is insufficient.
- Next round: while confirmed ready packages remain, ask the next video-generation-round quantity with `先生成 1 条（推荐）`, useful larger choices, `生成全部已确认视频`, `先修改方案`, and `暂停`, plus open notes. When no ready package remains but planned directions remain unprepared, ask the next preparation-round quantity with `先准备 1 条方案（推荐）`, useful larger choices, `准备全部剩余方案`, `先修改方向`, and `结束`, plus open notes.
- Asset or anchor decision: user-provided usable product/entity images default to direct reuse and do not need a generated-baseline decision. Use `media`, `character`, `multi_character`, `radio`, or `checkbox` only to resolve a genuine gap or confirm a paid anchor for a new agent-created identity, and add an open text question for usage constraints or corrections.
- Speaking-role anchors: when narration, dialogue, or monologue is planned and one or more roles lack accepted timbre anchors, list every speaking identity separately. Recommend one voice description per role, including voice texture plus role/campaign-relevant tone, energy, and rhythm. For several roles, use a grouped confirmation such as `按推荐声音生成全部角色样本（推荐）` / `先调整角色声音`, plus an open field that accepts role-specific corrections; do not collapse all characters into one narrator voice. After presenting each role-labeled neutral sample, use `确认这些角色的音色和语气` / `调整部分角色`, plus an open field naming the role and change. Explain that sample words are unrelated and never enter the video, sample performance fits its role, and actual narration/dialogue/monologue plus line-level delivery come from the script. Do not add a custom/other option.
- Product state coverage router: when required product views or states are missing, use `上传更多商品实拍（推荐）` / `补充细节并生成状态参考图` / `跳过并接受一致性风险`, plus an open notes question. This form only selects a branch. It does not collect the required branch payload and must not be treated as upload completion, factual detail, risk acceptance, or generation authorization. Block the later visual-storyboard form until this branch is fully complete.

Treat the closed answer and open text as one response. If the user selects a confirmation choice but writes a material correction, apply the correction and reconfirm rather than treating the selection alone as authorization.

## Product State Branch Forms

The questionnaire schema has no conditional show/hide rules. Therefore, after the product-state router is answered, the next workflow action must be the selected branch's collection or risk-confirmation node. Normally this means launching the follow-up form immediately. If the same returned response already contains the complete matching payload, such as actual attached media for the upload branch or sufficiently detailed text in the router's open field for the detail branch, validate that payload and move only to that branch's next node (re-audit or factual-summary confirmation); do not ask for the same input twice. Do not move to skill loading, file preparation, paid image generation, storyboard generation, or any later stage first.

### Upload branch

Use a form containing:

- a `media` question requesting the actual missing product images. Use `assets: []` when the runtime renders an empty media field as an upload/selection box; otherwise include available relevant media and explicitly ask the user to attach new images in conversation;
- a `text` question asking which SKU, angle, and state each image shows;
- a `radio` question with `提交图片并重新检查（推荐）`, `改为补充细节`, and `改为跳过并评估风险`.

Do not mark this branch complete when the user returns no actual media. A statement such as `已上传`, a filename typed into text, or a selected submit option is not an image attachment. Stay at `awaiting upload`, or route to the newly selected branch. After files arrive, re-audit coverage and explicitly list any remaining gap before proceeding.

### Detail branch

Use a form containing actual text inputs for the fields that are missing, such as:

- `缺失角度与结构` - back, side, top/bottom, interior, connector, cap/nozzle, hinge, opening, or removable-part geometry;
- `材质颜色与标识` - materials, finish, transparency, exact colors, labels, Logo placement, and unchanged identity details;
- `状态变化` - open/closed, cap-on/cap-off, sealed/opened, contents/fill level, folded/unfolded, assembled/disassembled, screen/interface, or in-use behavior;
- a `radio` question with `提交这些细节供核实（推荐）`, `改为上传实拍`, and `改为跳过并评估风险`.

Ask only fields relevant to the actual SKU and confirmed shots. Empty or vague answers do not complete this branch. Repeat a smaller detail form for unresolved facts. Once sufficient, summarize every fact and assumption in conversation, disclose the exact planned image-call count, and launch a separate form with `确认细节并生成` / `继续补充细节` / `改为上传实拍` / `改为跳过并评估风险`, plus an open correction field. Only `确认细节并生成` authorizes the paid image call.

### Skip branch

First state the exact missing views/states and likely consequences, such as changing nozzle geometry, cap construction, back label, connector placement, liquid level, or opening mechanism. Then launch a separate form with `返回上传实拍（推荐）`, `改为补充细节`, and `接受上述一致性风险并继续`, plus an open constraint field. Only the last explicit response completes the skip branch. The router's `跳过` choice alone does not.

### Generated reference confirmation

After generation, call `present_sandbox_file` for the actual product state reference image, explain its panel/state order in conversation, then launch a form with `确认状态参考图` / `需要修改` / `改为上传实拍` / `改为跳过并评估风险`, plus an open correction field. Do not use the reference downstream until `确认状态参考图` is returned without a material correction.
