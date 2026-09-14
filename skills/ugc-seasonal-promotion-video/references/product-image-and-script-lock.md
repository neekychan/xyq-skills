# Product Image And Script Lock

Use this reference whenever the user provides a fixed script, voiceover, timestamped copy, product image, product screenshot, product card, package photo, or says to follow the script.

## Script-To-Video Lock

When the user provides a specified script:

- Preserve the user script as the source of truth.
- Keep line order, meaning, product name, campaign occasion, price, coupon, gift, final price, deadline, and CTA.
- Split the script into 4-6 video beats according to punctuation, timestamps, semantic pauses, or campaign benefit changes.
- Map each script line to one visible action: price card, coupon card, gift reveal, product proof, product-card bridge, countdown, or CTA.
- Use `voiceover_zh` as the user script line when the user asks to preserve wording.
- Use `sticker_text` as a short offer tag that supports the same line.

Seedance 2.0 positive wording:

```text
按用户脚本逐句生成口播，每句口播对应一个镜头动作。
每个 voiceover_zh 使用用户脚本原句或等义短句。
画面动作服务当前脚本利益点：价格、券、赠品、到手量、限时或CTA。
脚本中的商品名、规格、价格、赠品和活动节点按用户输入呈现。
```

## Revision Handling

When the user asks to modify an existing script or any related execution detail:

- Apply the user's requested change first: tone, length, CTA, offer, hook, persona, wording, sequence, or product claim.
- Preserve unchanged script meaning and factual claims.
- Output the revised script/video prompt after the change.
- If the user says to strengthen promotion, convert product explanation into price, coupon, gift, final quantity, limited-time, or CTA lines.
- If the user says to reduce repetition, assign each line a different information role:
  1. Hook
  2. brightest offer/mechanism
  3. one product proof sentence
  4. campaign time + offer path
  5. single CTA

Revision mapping:

- Script wording changes update `中文口播`.
- Persona changes update `达人画像` and every visible `人物呈现`.
- Product image changes update product-image lock and every product appearance.
- Gift changes update gift reveal, sticker text, and CTA bundle.
- Price/coupon changes update price card, coupon card, voiceover, and sticker text.
- Campaign occasion changes update scene, hook, wording, CTA, and visual symbols.
- Transition changes update every affected `镜头`.
- Screenshot/phone changes update screenshot-card, phone-bridge, and mechanism-card handling.

## Product Image Lock

When the user provides product images, use the image as the visual anchor for every product appearance.

Preserve:

- package shape, silhouette, box/bottle/tube/bag structure
- logo and brand mark placement
- printed product name and visible package text
- capacity, count, flavor/color/version text when visible
- label layout and hierarchy
- dominant color blocks, patterns, icons, illustrations
- cap, nozzle, pump, lid, hanger, handle, box flap, seal, or pouch structure
- material and texture: glossy, matte, transparent, paper, plastic, metal, fabric
- product size ratio and visible dimensions
- front/back orientation and SKU
- multi-pack quantity and arrangement

Seedance 2.0 positive wording:

```text
产品外观以用户上传图片为视觉锚点。
所有镜头保持同一包装形状、logo位置、文字排版、颜色块、图案、材质和尺寸比例。
产品正面标签、品牌名、规格文字、容量/数量信息按用户图片呈现。
产品相对手、桌面、手机、赠品和包装盒的大小比例保持一致。
```

## Gift And Add-On Lock

Visible gifts and add-ons follow user image, page copy, or screenshot evidence.

- Match gift type, color, package form, bottle/tube/jar/box shape, and visible capacity.
- If evidence is unclear, use generic placeholders: `赠品礼`, `加赠小样`, `[确认赠品名称]`.
- Keep gift quantity consistent across beats once gifts are placed.
