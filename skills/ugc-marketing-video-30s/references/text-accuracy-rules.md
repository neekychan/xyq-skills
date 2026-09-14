# 文字准确性规则 / Text Accuracy Rules

Use this reference before writing optional in-frame text, subtitles, price tags, product cards, CTA labels, app screenshots, or any text that appears inside the video.

## Text Source Of Truth

Visible video text may only come from:

- user-provided product name, brand, SKU, offer, price, coupon, CTA, or subtitle copy
- selected hook keyword
- selected benefit keyword
- selected result keyword
- selected CTA keyword
- platform-safe generic labels such as `实测`, `上身`, `到店`, `先领券`, `看商品卡`

For exact text such as price, coupon, dosage, package quantity, dates, model names, account names, store names, and product names, preserve the user's original characters.

## Short Text Rule

For SD2.5 stability, use short text elements:

- Chinese effect text: 2-8 characters per element
- English effect text: 1-4 words per element
- One text element per beat by default
- Two text elements only when the same beat must show both offer and CTA/result

Good examples:

```text
先看效果
券后到手
一套够用
真实上身
到店核销
福利别漏
```

## Subtitle Rule

Subtitles are not default.

- If the user requests subtitles, subtitles must reuse the exact `spoken_line`.
- Render one subtitle layer only.
- Keep subtitle position stable in the lower safe area.
- Keep flower text separate from subtitles.
- If the platform will add captions, keep generated video text to keywords only.

## Placement Rule

Place text in platform-safe areas:

- Douyin: upper-middle or beside product/face; keep right side and bottom product card area clear.
- Xiaohongshu: upper-middle, side label, or note-style small tag; keep bottom title/comment zone clear.
- Kuaishou: middle-upper or product side; keep bottom caption/action area clear.
- WeChat Channels: upper-middle or product side; keep bottom title/action area clear.
- Store/group-buying pages: place label near price/package but keep the original price and CTA readable.

## Text Timing Rule

Each text element should appear only when its matching visual proof is visible:

- hook text appears in 0-3s and disappears before proof gets crowded
- benefit text appears with product action
- result text appears with visible result
- CTA text appears in 27-30s with product or phone entrance visible

## Number And Offer Accuracy

For price, discount, coupon, quantity, and date:

- Use user-provided exact number.
- Do not round or rewrite the number.
- Do not invent missing discount.
- If the price is unclear, write generic `福利价` or ask the user.
- Speak important offer once and optionally show one short price tag.

## App/Screenshot Text Rule

When showing screenshots, app pages, order pages, game reward pages, or group-buying pages:

- Show them on a phone, tablet, laptop, or picture-in-picture panel.
- Keep screenshot text stable and readable by limiting camera movement.
- Use hand tap, pointing gesture, or phone raise as the bridge.
- Return to real product, store, package, or creator reaction in the next beat.

## Final Text Accuracy Check

Before final output, confirm:

- No long paragraphs are requested inside the generated video frame.
- Exact user-provided text stays exact.
- Text does not cover product, face, mouth, hands, price, app UI, or CTA button.
- Optional text matches the spoken line, proof action, or CTA of the same beat.
- Full subtitles are present only when requested.
