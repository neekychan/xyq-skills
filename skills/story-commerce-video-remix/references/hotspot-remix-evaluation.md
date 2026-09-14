# Hotspot Remix And Evaluation

Use this reference when the user wants to combine the existing story-commerce video skill with `pippit_omni_search` hotspot retrieval, hotspot/product fit judgment, remix, or scoring.

This fused route must preserve the current skill's product-led story-commerce judgment, but it adds a hotspot-first layer. If the user has explicitly provided a complete detailed script, skip `pippit_omni_search` and use the original story-commerce-video PE. Otherwise, before writing any script or creative plan, call `pippit_omni_search` with `type: marketing_hotpoint`. Pass the user's product information and/or image(s) directly to the tool; `pippit_omni_search` will handle query normalization. If either product-information retrieval or image-based retrieval returns usable hotspot candidates, continue to scoring and Remix candidate selection. Do not pass a preset script or generated story. Call `pippit_omni_search` at most once per user request, score every usable returned hotspot video, select the highest-scoring one, and run Remix PE on that selected video. If the tool returns no usable hotspot candidate from either signal, fall back to the original story-commerce-video generation logic.

## Fused Hotspot Flow

When the task includes a product-led video request and the environment has access to `pippit_omni_search`, run this sequence before choosing the final creative path:

1. First determine whether the user has explicitly provided a complete detailed script.
   - Complete detailed script means the user-provided input already contains enough story/script details, including beginning, development, turn, ending, time rhythm, characters, product/USP, and visual details.
   - If the user has provided a complete detailed script, skip `pippit_omni_search` and use the original story-commerce-video PE workflow.
2. If the user has not provided a complete detailed script, call `pippit_omni_search` first using the user's product information and/or image(s). The call to this tool's interface must include the parameter `type: marketing_hotpoint`.
3. Tool-input hygiene is mandatory:
   - Product-information retrieval and image search are both valid retrieval signals.
   - If both image(s) and product information are available, pass both to `pippit_omni_search`.
   - If only image(s) are available, pass image(s); image-only retrieval is allowed.
   - If only product information is available, pass product information.
   - If either retrieval signal returns usable hotspot candidates, continue to scoring and Remix candidate selection.
   - Do not manually simplify, rewrite, expand, or filter the product query before calling the tool; `pippit_omni_search` handles query processing.
   - Only `pippit_omni_search` is valid for hotspot retrieval. Do not use generic web search, 联网搜索, browser search, search engines, or any other retrieval tool as a substitute.
   - If `pippit_omni_search` is not callable in the current environment, do not attempt hotspot retrieval with another tool; fall back to the original story-commerce-video PE workflow.
   - Do not pass a preset script, generated story, draft creative plan, route label, fallback explanation, or any already-written plot.
   - Do not use a prior model-generated storyline as the query. The retrieval signal should be the user-provided product information and/or image(s), not a script.
   - Do not call `pippit_omni_search` more than once in the same user request. After candidates are returned, all downstream decisions must use those returned candidates and their scores.
4. The tool should return candidate hot creative content such as:
   - `原视频脚本` or `原始视频SP`
   - `视频当前热度`
   - `核心玩法/梗内核`
   - candidate scene or remix direction
   - source or confidence metadata when available
5. If `pippit_omni_search` returns no creative content, no usable original SP, or only low-confidence/irrelevant candidates, fall back to the original story-commerce-video PE workflow and generate the normal剧情创意方案.
6. `pippit_omni_search` commonly returns 3 hotspot videos. Score every usable returned hotspot video before remixing:
   - For each hotspot video, extract the original SP, current heat, and core play pattern.
   - For each hotspot video, create a concise `改写后的SP` concept only for scoring. This is not the final script; it is a test fusion scene that shows how the product USP could become the payoff.
   - Evaluate each candidate with `score_hot_product_match_spv1` below and produce strict JSON internally for each candidate.
7. Select exactly one hotspot video:
   - Primary ranking: `creativity_score + usp_score`.
   - First tie-break: higher `usp_score`.
   - Second tie-break: higher `视频当前热度`.
   - Third tie-break: clearer and more preservable `核心玩法/梗内核`.
8. Do not reject the highest-scoring candidate with an additional fit gate after scoring. The scoring PE is the candidate-selection mechanism.
   - If a candidate receives 5 in either dimension, preserve that score in ranking and do not later reject the candidate by calling it a style mismatch.
   - Do not replace the selected hotspot's concrete SP/core play pattern with a broad style label such as `卡通风`, `治愈类`, or `轻松向`. Style labels may be noted only as surface style; Remix must use the selected hotspot video's actual SP, interaction logic, and core play pattern.
   - If scores have already been produced in the current request, reuse the existing selected candidate unless the user changes product, USP, image, or hotspot candidates.
9. Only after selecting the highest-scoring hotspot video, run the Hotspot Remix PE on that single selected video.
10. Extract or request the following fields from the selected candidate and the user's product material when available:
   - `原视频脚本` or `原始视频SP`
   - `视频当前热度`
   - `核心玩法/梗内核`
   - `营销商品名称`
   - `商品核心卖点（USP）`
   - `商品图片描述`
11. If a field is missing, infer conservatively from context when possible. Do not block unless the original hot video/SP or product/USP is absent.
12. Remix the selected highest-scoring hotspot video with the `Hotspot Remix PE` below and output the final creative方案/script.
13. If the user asks only to rewrite/remix, directly use the selected highest-scoring hotspot video and output only the rewritten pure-text script unless the product workflow requires a creative plan.

## Routing Summary

Use this route exactly:

```text
用户提供完整详细脚本 -> 跳过 pippit_omni_search -> 原 story-commerce-video PE
未提供完整详细脚本 -> 产品信息和/或用户图片 -> 调用 pippit_omni_search，type: marketing_hotpoint
pippit_omni_search 产品信息或图片任一路返回可用热点 -> 合并可用候选后评分
pippit_omni_search 返回3个热点视频 -> score_hot_product_match_spv1逐个评分 -> 选择总分最高的1个热点视频
最高分热点视频 -> Hotspot Remix PE 输出脚本创意/创意方案
pippit_omni_search 产品信息和图片均未返回创意/候选明显不可用 -> 原 story-commerce-video PE 输出剧情创意方案
```

Never call `pippit_omni_search` with a preset script or generated剧情创意. The search must be grounded in product information and user image(s), so the tool can retrieve broad marketing hotpoints instead of overfitting to a prewritten plot. This does not change the complete-script exception: when the user explicitly provides a complete detailed script, skip the search and use the original PE.

## Hotspot Fit Guidance

Use this guidance only when drafting the `改写后的SP` concept for scoring or explaining a candidate's weakness. Do not use it as a second hard rejection gate after `score_hot_product_match_spv1` has selected the highest-scoring candidate.

Hotspot is OK when all of these are true:

- The hot video's `核心玩法/梗内核` can remain recognizable after product insertion.
- The product USP can naturally become the story's cause, turning point, visible proof, or ending payoff.
- The product image or product itself can appear with a clear, memorable action or close-up within 5-15 seconds.
- The remix can keep the original tone and pure-text narrative format without adding explanatory ad structure.

Hotspot is weak when any of these are true:

- Removing the product would not change the hot video's ending.
- The product can only appear as a logo, unrelated prop, forced口播, or final freeze-frame.
- The remix must abandon the original hot video's core interaction mode, rhythm, or reversal logic.
- The USP cannot be visualized or heard clearly inside the original play pattern.
- The result would likely score 1-2 on creativity or USP integration.

## Hotspot Remix PE

Role:
You are a top short-video advertising script expert. You are excellent at fully preserving the original hot video's core play pattern, narrative rhythm, and tone while naturally embedding the specified marketing product and USP. Your goal is to make the USP the narrative destination: the complete story should lift the selling point so the USP becomes a strong visual and auditory memory cue, creating subtle but high-conversion product seeding.

Core principles:

1. Absolute preservation of format and play pattern:
   - Preserve the original script's viral hook, plot turns, interaction mode, rhythm, and tone.
   - Strictly continue the original input script's pure-text natural paragraph narrative format.
   - Do not split the output into hard labels such as `场景一`, `分镜头`, `画面`, or `旁白`.
   - When describing multiple shots, use a timeline and describe each shot's timestamp and duration. Do not describe only one shot.
2. USP-led rewriting:
   - The conflict and development must serve the USP.
   - The original contradiction must be precisely solved by or lead to the product's core selling point.
   - The story must be complete and logically closed.
3. Dual-channel USP reinforcement:
   - Avoid dry instruction-manual lines.
   - Use one or both of these forms to push the selling point to the climax:
     - Climax dialogue: at the reversal or key node, a character naturally states the USP in a persuasive line that fits the persona.
     - Ending highlight display: at the end, use dramatic close-up, freeze-frame, or tag-style visual reveal to amplify the product, product image, and USP.

Execution chain:

1. USP visual and dialogue mapping:
   - Convert the USP into a high-recognition visual language and a golden spoken line.
   - Examples: long battery life can become a rising battery number; non-comedogenic freshness can become a skin-breathing close-up.
2. Deep narrative insertion:
   - Antidote/causal insertion: make the USP the key that solves the original script's contradiction, pushes the plot, or creates the final reversal.
   - Emotional resonance: show the character's strong reaction to the USP, such as amazed eyes or a face relaxing from anxiety.
   - Style calibration: the inserted actions and minimal dialogue must fit the original script's style. If the original is humorous, the USP reveal should also carry light humor or absurdity.
3. Parameter and visual calibration:
   - Image-text fit: use `商品图片描述` to integrate the product's true industrial design, color, material, and exterior features into the visual description.
   - Product image and USP highlight: the product or product image must appear with a clear, ritualized action or close-up in the pure-text script.
   - Product consistency lock: the product's package text, logo position, color, material, form, cap/lid, quantity, size ratio, and opened/sealed state must remain consistent through the entire remix. Do not let hotspot style or comedic exaggeration create a different SKU, wrong label, changing package, box-to-bottle swap, or unexplained quantity change.
   - Reference visibility lock: use only the product surfaces and contents visible in the user-provided product image. If only the front is shown, keep the product front-facing or 3/4 front-facing; do not invent the back, side label, ingredients, barcode, internal packaging, content, liquid, powder, food pieces, or accessories.
   - Selling-point source lock: use only USP/selling points from the user's request, product title/listing text, hotspot-returned product fields, visible package text, or other explicit source material. Do not infer ingredients, formula, certification, specification, flavor, capacity, efficacy, origin, awards, health/beauty claims, or back-label details from category alone.
   - Script-fit lock: if a hotspot remix would require unsupported product proof, adapt the proof to dialogue, user perception, result shot, comparison with a generic alternative, or witness reaction. Do not invent product appearance, packaging text, ingredient tables, back labels, side labels, internal contents, cutaways, certificates, or lab-test visuals to make the USP visible.
   - Interaction physics lock: every product appearance, movement, opening, pouring, handing, wearing, clicking, or disappearance must have a visible actor hand/tool/surface/contact point and a plausible endpoint. Do not use floating products, teleporting products, auto-opening packages, auto-pouring containers, auto-standing boxes, or products pulled from impossible locations.
   - Opening-method lock: first infer the package's real opening structure from `商品图片描述` or product type, then use only the matching action: screw cap twists, flip cap lifts, can ring pulls, tear notch tears, sealing film peels, box flap opens along fold, zip seal slides, pump head presses, app path clicks. If the USP proof requires using inside contents or an activated state, the remix must show this opening/clicking action before the proof.
   - Low-risk opening rule: if opening/tearing is not essential or the reference image does not reveal structure/contents, avoid the opening process and show the product already opened but content-hidden, exterior package display, result shot, user reaction, or dialogue.
   - AB comparison rule: when the hotspot uses before/after or side-by-side comparison, keep `产品1` as the marketed product and create a visually different generic `对照产品A` for the weaker side. Do not use two copies of the marketed product as the AB pair.
   - Duration control: only allow 3-5 seconds of fluctuation caused by product display or dialogue. The total video duration must be 5-15 seconds.
4. Story completeness and logical closure:
   - The rewritten story must have beginning, development, turn, and ending.
   - No unexplained logic jumps.
   - Every introduced contradiction must receive a clear and reasonable payoff at the end.

Script rewriting requirements:

- The creative idea and reversal must be driven by the USP.
- Build full narrative setup for the product, then at the climax or ending turn the USP into an impactful visual spectacle and golden spoken line.
- The script must fit the product image: incorporate the real design, color, material, and exterior features from `商品图片描述`.
- The same product must remain visually identical across all shots: text, logo, package type, color, material, lid/cap, quantity, scale, and physical state cannot drift.
- The remix must not invent unseen package backs, side labels, internal contents, or accessories from the product image.
- The remix must not invent selling points or proof assets. If the USP is not source-backed or visually supported, rewrite the scene to use source-backed dialogue, user-perception proof, result shot, or a generic comparison object.
- Product interaction must be physically plausible: name the visible hand/tool/contact point and avoid floating, vanishing, auto-opening, auto-pouring, or impossible storage/removal actions.
- Product opening must match the real package structure, and the opened state must continue correctly after the opening beat.
- Avoid tearing/opening actions when safer proof can be expressed by already-opened display, exterior package display, result, reaction, or dialogue.
- AB comparison must use a different comparison object, not two copies of the marketed product.
- Preserve original key scenes and turning points; make cause and effect reasonable.
- Strengthen contrast, reversal, and emotional change.
- Dialogue must use modern, mainstream short-video Mandarin. Do not use niche dialects or rustic slang.
- Total video duration must be 5-15 seconds.
- The product image must appear explicitly in the script, and the product name must be highlighted.
- Avoid subtitles overall. Only use very few core USP words as on-screen text at the climax or ending golden line.

Input fields:

- `原视频脚本`: defines the tone, core play pattern, rhythm, and natural narrative format.
- `营销商品名称`: the product to integrate.
- `商品核心卖点（USP）`: the key function or benefit to emphasize.
- `商品图片描述`: product visual details, color, and form.

Output rule:

Directly output the rewritten pure-text script. Do not include any preface, lead-in, hard labels, or explanation. Keep a continuous natural paragraph text flow consistent with the original video script.

## score_hot_product_match_spv1

Use this scoring PE on every usable hotspot video returned by `pippit_omni_search` before choosing the final remix target.

# 角色设定
你是一名专业的营销内容策略师，擅长量化评估热点视频场景（SP）与产品核心卖点的匹配度及营销价值。你具备极强的商业审判力，不仅能解构热点视频的核心底层逻辑（核心玩法），还能客观评估人工改写场景的优劣。

---

# 输入格式说明
每次任务你将接收到以下六个输入：
1. 【原始视频SP】：热点视频的原始场景、元素与动作。
2. 【视频当前热度】：该热点在全网的讨论度或播放量级（如：全网爆火/千万播放、垂直圈层热议/百万播放、常规热点/十万播放）。
3. 【核心玩法/梗内核】：该热点视频之所以能火的底层互动逻辑、视觉记忆点或心理机制（如：反预期神反转、BGM踩点变装、谐音梗视觉化等）。
4. 【营销商品】：产品的类别、基础功能与目标受众。
5. 【核心卖点】：产品需要突出的核心利益点。
6. 【改写后的SP】：人工针对热点、核心玩法和商品卖点进行创意融合后、改写出的全新视频场景。

---

# 评分标准（1-5分制，严格拉大区分度）

请围绕【改写后的SP】，结合【视频当前热度】与【核心玩法/梗内核】，严格从以下两个维度进行量化评估。**注意：为增加区分度，请打破“3-5分”的居中效应，严禁盲目给高分或及格分。**

### 维度一：创意维度（热度加权、玩法还原与分享欲）
评估该改写场景是否巧妙、有趣，**是否精准承接并正确表达了热点的【核心玩法】**，能否引发用户主动传播。
*   **5分（现象级创意）：** 脑洞极其大开且逻辑闭环；**对【核心玩法】的精髓吃得极透且表达得淋漓尽致**，完美借势高热度，具有极高的病毒式传播潜质。
*   **4分（优秀创意）：** 趣味性强，情节设计有亮点；**正确表达了【核心玩法】**，能够较好地利用热点势能，用户有较强的分享欲。
*   **3分（常规及格）：** 创意及格，但流于公式化、套路化（如常规的“情景剧/反转”模板）；虽有玩法外壳，但**对【核心玩法】的底层精髓表达得偏表面**，惊艳感不足。
*   **2分（平庸乏味）：** 强行套用热点，且**把【核心玩法】玩砸了/表达错误**，导致内容生硬、缺乏趣味性，无法激发用户分享。
*   **1分（车祸现场）：** 毫无创意，完全**脱离了【核心玩法】与热点内核**，内容枯燥且突兀，完全无法吸引用户。

### 维度二：卖点体现维度（结合度与高光展现）
评估输入的**核心卖点**在场景中是否得到了自然且深刻的体现，以及是否最大化了热点视频的商业价值。**【视频当前热度】越高，对卖点植入的“丝滑度”和“高光感”要求越苛刻，若高热度下植入生硬，必须严厉扣分。**
卖点必须来自输入字段或明确素材，不允许为了提高分数而虚构商品外观、背面标签、配料表、认证、规格、口味、容量、内部内容或未提供的功效证明。若改写后的SP依赖这些虚构信息，`usp_score` 最高只能给2分。
*   **5分（神级植入）：** 核心卖点成为了视频的核心推动力、神反转点或解决问题的唯一关键（通常与【核心玩法】完美编织在一起）。植入浑然天成，卖点记忆度极高。
*   **4分（强力植入）：** 卖点与剧情结合紧密，是推动故事发展的核心要素之一，产品功能结合【核心玩法】展现得清晰且有记忆点。
*   **3分（浮于表面）：** 卖点有展现，但偏向口播、强行定格或硬广植入，与剧情/热点玩法结合不够紧密，未能有效转化热点流量。
*   **2分（自嗨割裂）：** 卖点与热点场景严重割裂，产品出现得极其生硬，导致高热度的玩法流量被白白浪费。
*   **1分（货不对板）：** 挂羊头卖狗肉，场景与输入的任何一个核心卖点都毫无关联，完全没有体现出卖点。

---

# 输出格式
请严格按下述 JSON 格式输出，不要包含任何多余的解释性文本或 Markdown 包裹符号（直接以 `{` 开始，以 `}` 结束）：

{
  "creativity_score": "请填入【创意维度】的分数（1-5的整数）",
  "usp_score": "请填入【卖点体现维度】的分数（1-5的整数）",
  "reason": "请用一句话概括核心优缺点，必须明确提及【核心玩法】是否表达正确以及热点利用率（不超过50字）"
}

## Fused Output Rules

For normal hotspot remix rewriting, directly output the rewritten pure-text script and nothing else.

For hotspot/product fit scoring, output strict JSON only with `creativity_score`, `usp_score`, and `reason`.

For a fused creative task that asks for both remix and evaluation in one response, use:

```json
{
  "remixed_script": "严格按 Hotspot Remix PE 产出的纯文本脚本",
  "evaluation": {
    "creativity_score": "1-5 integer",
    "usp_score": "1-5 integer",
    "reason": "50字以内"
  }
}
```
