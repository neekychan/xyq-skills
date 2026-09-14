# 输入一致性规则 / Input Consistency Rules

Use this reference before persona selection, script writing, and final `video_generation_prompt`. The goal is to keep product facts, visual assets, user instructions, and final video behavior aligned.

## Evidence Priority

Resolve product facts in this order:

1. Latest explicit user instruction
2. Product title/name/SKU text
3. Product URL or page facts when accessible
4. User-provided selling points, offer, CTA, platform, audience, and script
5. Uploaded product images, screenshots, reference images, or video references
6. Visual inference only when text facts are missing

When facts conflict in a way that changes product category, protagonist, CTA, or claim, ask one short clarification question before generation.

## Product Identity Binding

Before writing the script, create an internal product identity card:

```text
product_identity:
- product_name:
- category:
- core_selling_point:
- target_user:
- visual_appearance:
- package/logo/color/material:
- variants/SKU:
- offer/price:
- CTA:
- platform:
- source_facts:
```

Use this card as the single source of truth for the creator portrait, script, and video prompt.

## Visual Asset Consistency

If the user provides product images, preserve:

- product shape
- color
- material/texture
- packaging
- logo position
- visible size
- variant order
- accessory relationship
- product-to-hand or product-to-body scale

The final prompt should say:

```text
商品外观全片保持与用户素材一致，包括形状、颜色、包装、logo位置、材质纹理、尺寸比例和已提供款式。
```

## Text And Image Conflict Handling

Use these rules:

- If title says one product and image shows another, ask which product to use.
- If the image shows a person and the title describes a child/baby product, use the adult as parent/presenter unless the user says otherwise.
- If the user provides a script, preserve script order and claims; adjust only pacing, visible action, and SD2.5 stability.
- If the user provides offer or price, keep exact numbers and names in the script and optional short text.
- If the URL is inaccessible, rely on pasted title, user text, and uploaded assets.

## Claim Consistency

Only use claims grounded in user input or visible proof.

- Strong claims such as medical effect, permanent result, official certification, guaranteed performance, financial benefit, or safety promise require user-provided evidence.
- If evidence is not provided, use experience phrasing such as `用起来`, `看起来`, `这个状态`, `这一点`, `我实测下来`.
- Do not invent ingredient, certification, discount, brand, SKU, or platform policy details.

## Script Consistency

Every beat should connect to the same product identity:

```text
0-3s: product appears or enters frame
3-8s: core selling point and proof action
8-14s: visible result/detail/comparison
14-21s: second proof, usage context, or reaction tied to the same product
21-27s: value confirmation with product or offer still visible
27-30s: CTA tied to the same product or offer
```

If the creator portrait is adjusted, refresh the script and prompt to match the latest persona and product relationship.

## Final Input Consistency Check

Before final output, confirm:

- The same product appears in persona prompt, script, and video prompt.
- The same offer/CTA is used in spoken line, optional text, and final beat.
- The same platform assumption controls hook, pacing, text placement, and CTA.
- The final prompt does not add facts absent from user input or visible assets.
