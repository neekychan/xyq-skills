# 输入一致性规则 / Input Consistency Rules

Use this reference before persona selection, script writing, and compilation of `seedance_generation_package`. The goal is to keep product facts, visual assets, user instructions, and final video behavior aligned.

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

Before writing the script, create an internal material manifest and product identity card.

Assign stable IDs:

```text
material_manifest:
- product_ref_1: primary product appearance source
- product_ref_2: secondary angle, detail or confirmed variant
- detail_ref_1: texture, label, accessory or structural detail
- ui_ref_1: price, coupon, order, app or page evidence
- creator_ref_1: active creator_portrait_image
```

Every physical-product shot cites at least one `product_ref_*`. Every creator shot cites `creator_ref_1`. UI screenshots establish page facts and do not replace the physical product source.

```text
product_identity:
- product_name:
- brand:
- category:
- exact_sku_or_variant:
- object_count:
- core_selling_point:
- target_user:
- silhouette_and_proportions:
- dominant_and_secondary_colors:
- material_and_surface_finish:
- package_structure:
- logo_position_and_orientation:
- label_layout_and_key_graphics:
- cap_nozzle_handle_button_port_layout:
- included_accessories:
- product_vs_package_relationship:
- real_world_scale_anchor:
- visible_distinctive_details:
- allowed_states:
- allowed_variants:
- offer/price:
- CTA:
- platform:
- source_asset_ids:
- source_facts_and_claims:
```

Use this card as the single source of truth for the creator portrait, script, and internal video-tool package.

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

The internal package should express the following positive product lock:

```text
商品外观全片保持与用户素材一致，包括形状、颜色、包装、logo位置、材质纹理、尺寸比例和已提供款式。
```

The internal video-tool package repeats the relevant product fingerprint inside every physical-product shot:

```text
product_state:
- asset_id:
- selected_sku:
- orientation:
- visible_label_or_screen_side:
- holder_or_support:
- location_in_frame:
- scale_anchor:
- state_at_start:
- state_at_end:
```

For connected shots, carry forward product orientation, support, scale and state. Variant changes use a visible reset and cite the new variant asset ID.

## Text And Image Conflict Handling

Use these rules:

- If title says one product and image shows another, ask which product to use.
- If the image shows a person and the title describes a child/baby product, use the adult as parent/presenter unless the user says otherwise.
- If the user provides a script, preserve script order and claims; adjust only pacing, visible action, and SD2.0 stability.
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
3-7s: core selling point and proof action
7-12s: visible result/detail/comparison
12-15s: CTA tied to the same product or offer
```

If the creator portrait is adjusted, refresh the script and internal package to match the latest persona and product relationship.

## Final Input Consistency Check

Before final output, confirm:

- The same product appears in the portrait instructions, visible script, and internal package.
- The same offer/CTA is used in spoken line, optional text, and final beat.
- The same platform assumption controls hook, pacing, text placement, and CTA.
- The internal package does not add facts absent from user input or visible assets.
- Every physical-product shot cites an authoritative product asset ID.
- Every connected shot preserves the product fingerprint, orientation, scale and physical state.
