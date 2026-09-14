---
name: ugc-marketing-video-idea
description: Generate a product-matched UGC creator portrait, then call ugc_idea_generator to produce the sales script and video from the product input and creator portrait. Use when the user needs the chain product input -> creator portrait -> script -> video.
tools: ["ugc_idea_generator", "sandbox_generate_image", "dynamic_questionnaire"]
---

# UGC Creator Portrait To Video Generator

This skill generates a UGC creator portrait first, then calls `ugc_idea_generator` to produce the script and video.

It must not:

- treat the creator portrait as the product image
- let creator clothing, accessories, phone, cup, furniture, or background props replace the product
- call `ugc_idea_generator` without passing the active creator portrait as the video character reference
- add expanded product briefs, captions, consistency notes, parsed fields, or rewritten instructions into the `ugc_idea_generator` request

The generated or uploaded creator portrait must become the video protagonist/person image. The product itself must come from the user's product image, product assets, or product text.

## Required Tools

Use these exact tool names:

```text
sandbox_generate_image
ugc_idea_generator
dynamic_questionnaire
```

## Workflow

1. Parse user product input into `product_info`:
   - product_name
   - category
   - selling_point
   - target_user
   - platform
   - offer
   - user_requirements

   `product_info` is internal only for creator-persona selection and image generation. Do not pass `product_info` into `ugc_idea_generator`, and do not append it into `user_input`.

2. Choose a product-matched creator persona:
   - language/market fit
   - age band
   - creator role
   - hairstyle/outfit/temperament
   - real scene
   - relationship to product
   - speaking tone

3. Check whether the user already uploaded a usable creator/person reference image:
   - If yes, do not call `sandbox_generate_image`.
   - Use the uploaded creator image as `creator_portrait_image`.
   - Create `creator_image_caption` from the uploaded creator image and product context.
   - Still return the consistency fields so the downstream algorithm knows the uploaded image is only the creator reference.

4. If the user did not upload a usable creator/person reference image, call `sandbox_generate_image` to generate the creator portrait.

5. Before calling `sandbox_generate_image`, internally build a complete high-quality creator image prompt. This internal prompt must be the exact full prompt that will be passed to the image tool, but it must not be exposed to the user.

6. Use a deterministic output path only when generating a new portrait:

```text
/workspace/出镜达人/creator_portrait_subject_1.png
```

7. After the image returns, create `creator_image_caption` and `product_consistency_note`.

8. After the active creator portrait is available, show the creator portrait summary and call `dynamic_questionnaire` before `ugc_idea_generator`.
   - `继续生成视频`: call `ugc_idea_generator` with the current materials and the user's original instruction.
   - `先修改方案`: wait for the user's revision request, including creator/reference changes, and do not call `ugc_idea_generator` yet.

9. Pass only the minimal handoff package into `ugc_idea_generator` after the user selects `继续生成视频`:
   - `materials`: all user-uploaded images/files first, then the active `creator_portrait_image`
   - `user_input`: the user's original instruction text exactly as received

   Do not add `product_info`, `creator_image_caption`, `product_consistency_note`, `product_source_of_truth`, `creator_reference_scope`, `non_product_elements`, rewritten prompts, extra requirements, or summarized briefs to the `ugc_idea_generator` request.
   Do not construct `user_input` from internal fields. `user_input` must not start with labels such as `product_info:`, `raw_user_input:`, `product_assets:`, `creator_portrait_image:`, or `generation_requirement:`.

10. Return:
   - `creator_portrait_image`
   - `creator_image_caption`
   - `product_consistency_note`
   - script result from `ugc_idea_generator`
   - video result from `ugc_idea_generator`

## Image Tool Rule

If the user provided a suitable creator/person reference image, do not call `sandbox_generate_image`. Use the uploaded image directly as the creator reference.

Only call `sandbox_generate_image` when the user did not provide a suitable creator/person reference image.

Do not satisfy the request by only writing a portrait prompt.

Before every `sandbox_generate_image` call, internally prepare a full high-quality creator image prompt and use that exact complete prompt as the image generation prompt. Never call the image tool with only a short prompt such as "generate a realistic UGC creator portrait". Do not expose the internal prompt or its field name to the user.

The image request should include:

- product category
- target buyer/user
- user input language and target market
- creator role
- age band
- hairstyle/outfit/temperament
- realistic domestic UGC scene
- relationship to product
- 4:5 vertical portrait requirement by default
- no text or watermark
- output path

## Internal High-Quality Image Prompt Rule

Always build a complete internal prompt before image generation. The quality of the generated image depends on the full prompt being passed through unchanged, but this internal prompt is not part of the user-facing answer.

Required behavior:

- Always prepare a complete internal high-quality creator image prompt before calling `sandbox_generate_image`.
- The complete internal prompt must be passed into the `sandbox_generate_image` tool call as the actual image-generation prompt.
- The `sandbox_generate_image` prompt argument must be exactly the same complete internal prompt.
- Do not compress, translate, summarize, or rewrite the internal prompt into a shorter tool prompt.
- Do not reveal the internal prompt, its variable name, or detailed parameter list to the user.
- Do not use generic phrases alone, such as `真实达人图`, `美妆达人自拍`, or `高质感UGC照片`.
- The prompt must include concrete details for: camera perspective, framing, gesture, expression, hairstyle, makeup, outfit, scene, light direction, background objects, skin texture, anti-AI texture constraints, aspect ratio, product-boundary constraints, and watermark/text constraints.
- If a product category changes, keep the same prompt structure but adapt the person, scene, pose, styling, and everyday objects to that product.

The user-facing output after generation should be a short Chinese summary only:

```text
达人参考图已生成完毕。请先确认是否继续生成视频；确认后会将用户原始指令、用户上传素材和达人参考图传给 ugc_idea_generator 生成脚本和视频。

达人信息汇总：
creator_portrait_image
{达人参考图路径或图片引用}

creator_image_caption
{中文caption}

product_consistency_note
{中文商品一致性说明}
```

## Realism And Framing Rule

By default, generate a realistic 4:5 vertical smartphone-style creator portrait.

Use these rules when writing the `sandbox_generate_image` request:

- Use `4:5 vertical portrait` by default. Use 3:4 only when the frontend/downstream pipeline explicitly requires 3:4 or when the product category requires a fuller body view.
- Prefer half-body or waist-up composition. The creator should occupy about 60%-70% of the frame, with the face and upper body clearly visible.
- Make the image look like a real UGC creator reference photo, not a studio campaign, beauty editorial, model portfolio, or commercial product ad.
- Make the creator feel like a native-platform creator: relaxed, slightly candid, believable, and not posed like a professional model.
- Use soft natural light by default, such as diffused window light, cloudy-day daylight, curtain-filtered window light, or ordinary indoor ambient light. Keep shadows soft and low-contrast.
- For a more textured native selfie look, controlled real sunlight is allowed when it feels like an ordinary phone photo: sunlight can create believable highlights and shadows on face, shoulder, table, wall, or background, but it must not look like studio lighting or a commercial beauty shoot.
- Avoid fake hard light: unnatural sharp window-shaped light patches, overly dramatic side shadows, blown-out face highlights, oily-looking skin shine, glossy beauty lighting, and commercial spotlight effect.
- Preserve real skin texture: visible pores, natural skin tone variation, slight under-eye texture, tiny blemishes or redness when appropriate, and no plastic smoothing.
- For portrait image generation, make skin realism explicit: avoid waxy skin, clay-like skin, airbrushed skin, blurred pores, fake porcelain texture, overly even skin color, plastic highlight, and AI-beauty-filter smoothness.
- Preserve natural hair details: flyaway hair, uneven strands, natural hair volume, believable hairline, and no wig-like perfect shape.
- Use a relaxed real-person expression: soft smile, neutral listening face, casual eye contact, or slight in-the-moment reaction. Avoid frozen smile, doll-like face, blank stare, or exaggerated influencer posing.
- Make the creator feel approachable and warm, like a real person who would share a product with friends. Prefer gentle eye contact, slight smile, relaxed cheeks, friendly micro-expression, and an open upper-body posture.
- Avoid cold model expression, distant gaze, overly posed chin-on-hand portrait, luxury influencer attitude, aloof beauty-shot mood, or facial expression that feels too perfect and emotionally flat.
- Preserve realistic body and hand details: natural shoulders, normal posture, believable hands, casual arm placement, and real clothing folds.
- Prefer a phone-camera look without showing the phone as a visible prop. Do not make the creator hold a phone in frame by default.
- If a visible phone must appear in the creator portrait, treat it only as a still-photo capture prop, not as a persistent action reference for downstream video.
- Preserve real human details overall: slight asymmetry, small facial imperfections, realistic fabric wrinkles, natural hands, and relaxed expression.
- Avoid over-smoothed skin, plastic face, perfect symmetry, glossy retouching, cinematic lighting, luxury set design, excessive depth-of-field blur, or influencer poster style.
- Keep the background ordinary and believable: bedroom, desk, living room, bathroom counter, kitchen, street, store, car, or office depending on category.
- Mild real-life clutter is allowed when it supports authenticity, but it must not introduce product-like props that confuse the downstream algorithm.
- Do not duplicate the product or product-like props in the portrait. For example, do not show one headphone on the creator and another headphone on the table unless the product is explicitly headphones and the user wants both.
- If the product is not meant to appear in the portrait, do not include it. Generate only the creator and a neutral scene.
- Do not add visible text, watermark, AI-generated badge, labels, fake brand logos, screen UI, subtitles, posters with readable words, or packaging text.

Add this default realism sentence to the image request:

```text
生成一张4:5竖版真实手机照片风格的原生感UGC达人参考图，非棚拍、非商业广告、非精修写真。人物为半身或腰部以上构图，占画面约60%-70%，使用柔和自然光，如窗帘过滤后的窗光、阴天散射光或普通室内环境光，避免直射阳光、硬阴影、墙面硬边光斑和脸部强高光。达人需要有亲切感，像真实会给朋友分享产品的人，眼神友好，轻微自然微笑，脸部表情放松，身体姿态自然打开，不要高冷模特感、疏离感、冷淡凝视或过度摆拍。保留真实皮肤纹理、毛孔、轻微肤色变化、眼下自然纹理、自然碎发、真实发际线、衣服褶皱、普通生活背景和轻微手机拍摄感。画面默认不要出现手机，不要让达人手持手机；手机感只作为拍摄质感，不作为可见道具或后续视频动作参考。皮肤不要蜡感、塑料感、磨皮过度、陶瓷感、AI美颜滤镜感、油亮反光。无文字、无水印、无AI生成角标、无logo。
```

Add this anti-confusion sentence when the product should not appear in the portrait:

```text
本次只生成达人本人和中性真实场景，不生成商品，不生成疑似商品的重复道具；达人衣服、配饰、桌面物品和背景物品都不代表商品。
```

## UGC Idea Generator Handoff Rule

After the active `creator_portrait_image` is generated or bound, call `dynamic_questionnaire` before `ugc_idea_generator`. Do not call `ugc_idea_generator` in the same turn that first shows a newly generated or newly bound creator portrait unless the user has already explicitly requested immediate generation after seeing it.

The confirmation question must offer:

- `继续生成视频`: use the current creator portrait and original user instruction to call `ugc_idea_generator`.
- `先修改方案`: wait for revision, including creator/reference changes, and do not generate yet.

Only after the user selects `继续生成视频`, call `ugc_idea_generator` to create the script and video.

The `ugc_idea_generator` request must stay minimal. Do not arrange or expand the tool input with extra parsed fields. The tool call should only contain:

```text
{
  "materials": [
    "{用户上传的图片/文件路径或素材引用，保持原顺序}",
    "{creator_portrait_image}"
  ],
  "user_input": "{用户原始指令全文，保持原文，不改写、不扩写、不追加说明}"
}
```

`materials` rules:

- Include every user-uploaded image/file that is available in the current request, including product images, reference images, screenshots, and uploaded creator images.
- Append the active generated or bound `creator_portrait_image` after the user-uploaded materials.
- If the active creator portrait is also a user-uploaded person image, include that uploaded image once in `materials`.
- Do not include captions, product summaries, consistency notes, or machine-readable handoff fields in `materials`.

`user_input` rules:

- Use the user's original instruction text exactly as received.
- Preserve the user's product name, CTA, platform, style, and follow-up requirements only if they appeared in the original instruction.
- Do not add generated captions, product_info, product_consistency_note, creator_reference_scope, non_product_elements, generation_requirement, or any extra explanation.
- Do not rewrite the original instruction into a new prompt.

If `ugc_idea_generator` returns separate script and video fields, keep both. If it returns a single combined result, return that combined result after the creator summary.

## High-Texture Native Selfie Pattern

When the user wants more realism, higher texture, or native creator feeling, write the image request as a concrete phone selfie scene instead of a generic portrait. Do not copy the same kitchen scene for every product; adapt the scene, pose, styling, and background objects to the product category and target market.

Use this structure:

```text
生成一张超真实的手机前置摄像头自拍质感照片：[符合语言/市场/商品的人物]在[符合商品使用场景的真实生活地点]，[肩部以上/胸前近景/半身近景]构图，[看向镜头/手托腮/整理头发/拿杯子/比V/自然微笑等非手机动作]，[具体表情和亲切感]。[发型、妆容、穿搭]符合[商品品类/目标用户]。默认画面里不要出现手机，不要让达人手持手机。

画面中有[真实生活光线]，在[脸/肩膀/桌面/墙面/背景]形成自然高光和阴影，但不过曝、不油亮、不商业棚拍。背景是[具体生活空间]，出现少量与场景合理相关的日常物品，[列出3-6个生活物件]，整体有真实生活感，不要过度整理。

使用手机自拍视角的近距离透视感，轻微广角畸变，画面比例4:5，像普通iPhone/安卓手机随手拍，清晰但不商业摄影。手机感只代表拍摄质感，画面中不需要出现手机，也不要把拿手机作为达人动作。肤质真实，有细节毛孔、轻微肤色变化、眼下自然纹理和自然光影，不要美颜过度、不要塑料皮、不要蜡感、不要AI生成角标、不要文字水印。
```

Product-adaptive selfie scene examples:

- 美妆/护肤/香水：卧室梳妆台、浴室镜前、窗边化妆桌、厨房餐桌；可有镜子、化妆刷、纸巾、发夹、水杯、护肤小样等生活物件，但不要让道具替代商品。
- 服饰/鞋包/饰品：卧室穿搭区、衣柜旁、玄关镜前、咖啡店座位、街边自然光；可有衣架、帆布包、杂志、钥匙、镜子等生活物件。
- 食品/饮品：厨房餐桌、便利店外、办公室茶水区、客厅茶几；可有杯子、餐巾纸、零食盒、外卖袋、水瓶等生活物件。
- 数码/工具/办公用品：办公桌、书桌、车内、宿舍桌面；可有电脑、鼠标、线材、便签、咖啡杯、书本等生活物件。
- 母婴/家居/日用品：客厅、厨房、儿童房、洗手台、阳台；可有收纳盒、湿巾、玩具、毛巾、杯子、家务用品等生活物件。
- 本地生活/服务/课程/App/游戏：门店外、街边、咖啡店、通勤路上、沙发或书桌自拍；不要生成虚假实体商品，用人物和场景表达目标人群。

For each generated prompt, include at least:

- one exact camera perspective, such as `手机前置摄像头自拍质感`, `近距离自拍透视`, or `轻微广角畸变`
- one exact pose or gesture that does not rely on holding a phone, such as `自然微笑`, `手托腮`, `比V`, `拿杯子`, `整理头发`, `看向镜头`
- one exact lighting setup, such as `窗边阳光`, `窗帘过滤光`, `阴天散射光`, or `普通室内环境光`
- one exact real-life background with 3-6 everyday objects
- one skin realism sentence and one anti-AI/anti-commercial sentence

## Product And Creator Consistency Rule

The creator portrait is a human-character reference for the downstream algorithm. It must not redefine, replace, or visually invent the product.

Use these rules when writing the `sandbox_generate_image` request:

- The user's product image is the only source of truth for product appearance.
- Preserve the product's category, shape, color, package, logo position, material, texture, size, SKU, and visible variants from the user-provided product image or product text.
- The creator's clothing, accessories, background props, and scene objects must be visually distinct from the product, so the downstream algorithm does not confuse outfit or props with the product.
- If the creator holds or uses the product in the portrait, describe it as `holding the user-provided product as a reference object, preserving the exact product appearance from the product image`.
- If product appearance is uncertain, generate the creator portrait without the product in hand; use a neutral pose and leave product handling to the downstream algorithm using the product image.
- Do not let the creator's outfit copy the product packaging colors, logo, label blocks, or product shape unless the product is clothing and the user explicitly wants try-on.
- For non-apparel products, keep the creator outfit simple and neutral, such as plain white, light gray, beige, black, denim, or low-saturation daily clothing.
- For apparel, shoes, bags, jewelry, or accessories, clearly state whether the creator is wearing/holding the actual product. If uncertain, show the creator as a matching presenter, not wearing a generated substitute.
- Do not add extra items that look like the product category unless they are intentionally the product. For headphones, bags, shoes, bottles, jars, food packages, phones, jewelry, or clothing, avoid duplicate or competing props that could be read as another SKU.
- If the product is not visible in the user input or the algorithm will use a separate product image later, prefer `creator-only portrait`: no product in hand, no product on table, no product-like prop in the foreground.

## Product Boundary Rules By Category

Use these category rules to prevent downstream product/person confusion.

### Non-Apparel Products

For skincare, makeup, food, drink, home goods, appliances, electronics, toys, local services, games, apps, courses, and other non-apparel products:

- The creator's clothes are always personal styling, not the product.
- The creator's jewelry, bag, phone case, cup, furniture, plants, posters, and background props are scene objects, not the product.
- Keep creator styling plain and low-conflict so it does not copy product packaging, brand colors, label shapes, or logo-like graphics.
- If the product must appear in the portrait, make it small and clearly separate from clothing/background, such as `holding the user-provided product bottle/package in one hand`.
- If the product is a service, app, game, course, coupon, store, or event, do not generate a fake physical product. Use the creator as a presenter and leave product/service facts to the downstream algorithm.

### Apparel And Try-On Products

For clothing products:

- If the user provides a clear clothing product image and explicitly wants try-on, the creator may wear the product.
- The clothing must strictly preserve the product image: silhouette, color, fabric, collar, sleeve length, hem, pattern, buttons, zipper, logo placement, decoration, fit, and visible details.
- The creator's body, face, hairstyle, pose, and scene may be generated; the garment design must not be redesigned.
- If the product image is unclear or the user did not ask for try-on, generate a neutral creator/presenter. The creator's outfit is not the product.
- For children's clothing, the adult creator should usually be a parent/presenter unless the user provides or requests a child wearer reference.

Use this note for apparel try-on:

```text
该商品为服装，达人图中服装仅在用户明确要求试穿且商品图清晰时作为商品试穿呈现；服装外观严格以用户商品图为准，包括版型、颜色、材质、图案、领口、袖长、下摆和logo位置。达人私服或背景服饰不代表商品。
```

Use this safer note when apparel product appearance is uncertain:

```text
该商品为服装，但当前达人图仅作为人物参考；达人身上的中性穿搭不代表商品。服装商品外观以后续传入的用户商品图或明确商品描述为准。
```

### Shoes, Bags, Jewelry, And Accessories

For shoes, bags, jewelry, watches, glasses, hats, scarves, belts, and accessories:

- Clearly state whether the creator is wearing/holding the actual product.
- If actual product appearance is not clear, use the creator as a presenter and do not generate a substitute accessory.
- Keep unrelated accessories minimal so the algorithm does not mistake them for the product.
- For jewelry/watches/glasses, avoid extra decorative accessories on the same body part unless they are the product.
- For bags/shoes, avoid background bags/shoes that compete with the product.

### Beauty, Skincare, And Personal Care

- The creator's skin/hair/makeup state is part of the persona, not proof of product effect unless the user explicitly provided that claim.
- The bottle, jar, tube, palette, or device appearance must come from the product image.
- If product packaging is not clear, do not invent brand packaging; generate the creator without product in hand or with a generic blank placeholder only if the downstream system supports replacing it.
- Keep bathroom/vanity props generic and visually distinct from product packaging.

### Food And Drink

- Plates, cups, tableware, kitchen props, and other foods in the background are scene props, not the product.
- If the exact food/package image is provided, preserve package color, label, portion form, and visible flavor/variant.
- If exact appearance is uncertain, generate only the creator and neutral eating/drinking scene; leave product visuals to the product image.

### Home, Digital, Tools, And Appliances

- Background furniture, phone, laptop, lamps, storage boxes, appliances, and tools are props unless explicitly identified as the product.
- Keep props low-detail and neutral.
- If the product is a device/appliance/tool, product size and shape must come from the user product image.

### Local Service, App, Game, Event, And Virtual Products

- The creator portrait should not invent a physical product.
- Use the creator as a presenter, visitor, player, or host.
- Storefronts, phone screens, event pages, coupons, rewards, and UI details are handled by the downstream algorithm or product assets, not by the creator portrait.

## Handoff Consistency Fields

Always return enough text for the frontend/algorithm to separate person and product:

```text
product_source_of_truth:
商品外观以后续传入的用户商品图/商品素材为准。

creator_reference_scope:
达人图只用于人物身份、脸部、发型、穿搭风格、气质、场景、画面真实感和口吻参考。达人图中的手机拍摄感只代表画面质感，不要求后续视频中达人持续拿手机。

creator_market_fit:
达人形象需跟随用户输入语言、产品信息和目标市场。中文且无其他市场要求时默认中国达人；其他语言根据语言、URL、币种、平台、地点词和商品信息推断对应市场与人群。

non_product_elements:
达人服装、配饰、背景道具、手机、杯子、家具、植物、海报、电脑、耳机、包、鞋、瓶罐、餐具等默认不是商品，除非 product_info 明确标记为商品。若达人图中出现手机，手机只是拍摄或生活道具，不是后续视频的持续动作要求。

creator_image_source:
若用户已上传达人图，则使用用户上传图作为达人参考，不再生成新达人图；若未上传，则使用sandbox_generate_image生成。

portrait_aspect_ratio:
默认4:5竖版；仅当前端或下游算法明确要求时才改为其他比例。
```

Add this product consistency sentence to the image request when product images are provided:

```text
达人形象只作为人物参考，用户提供的商品图是商品外观唯一依据；达人服装、配饰和背景道具与商品保持清楚区分。若画面中出现商品，商品外观严格保持用户商品图中的形状、颜色、包装、logo位置、材质、尺寸比例和款式，不生成替代商品。
```

Add this safer sentence when product appearance is uncertain:

```text
本次只生成达人本人，不在达人图中生成商品；后续算法使用用户提供的商品图作为商品外观依据。
```

## Creator Persona Guide

Choose one persona that fits the product:

First follow the user's language, market, and product context when choosing creator ethnicity, appearance, styling, scene, and social-platform feel:

- If the user input is Chinese and no other target market is specified, default to a Chinese creator in a China-market UGC scene.
- If the user input is English, Spanish, French, German, Japanese, Korean, Arabic, Thai, Vietnamese, Indonesian, Portuguese, or another language, infer the likely target market from the language, product, platform, currency, location words, URL, and user requirements.
- Match the creator's ethnicity/region style to the inferred target market when reasonable. For example, Japanese input or Japan-market product can use a Japanese creator; Korean input can use a Korean creator; Spanish input can use a Latin American or Spain-market creator depending on context; English input can use a US/UK/Australia/global-market creator depending on product and platform.
- If the product page, brand, SKU, packaging, or user requirement clearly points to a specific country or region, follow that market over the language alone.
- If the user explicitly specifies creator gender, ethnicity, region, age, style, or persona, follow the user's explicit instruction.
- If the user uploads a creator reference image, follow the uploaded person's visible identity and style; do not generate or replace the creator.
- Do not randomly mix market signals. Avoid Chinese creator for a clearly overseas-market product unless requested, and avoid overseas creator for a clearly China-market Chinese request unless requested.
- The caption should mention the creator persona in a way that matches the target market, without making unsupported claims about nationality if the evidence is only inferred.

- 护肤/美妆：优先选择好看、精致但真实的女性达人，可带自然妆或精致日常妆；场景为梳妆台、浴室镜前、卧室窗边或日常化妆区；光线自然柔和，皮肤有真实纹理，不要磨皮假脸；口吻温和可信
- 彩妆/香水/个护精致类：可选择更精致的美女达人，妆容、发型和穿搭更完整，但仍保持手机原生感、自然光、真实皮肤质感和生活化场景，不要棚拍大片
- 服饰/鞋包：根据商品风格选择精致穿搭美女、自然风美女、通勤感达人、辣妹风达人或户外生活方式达人；场景为镜前、街头、咖啡店、通勤路上或卧室穿搭区；强调上身/搭配/质感，但不要让达人私服替代商品
- 母婴/家庭：真实宝妈或家庭照顾者，客厅/儿童房/厨房，口吻实用安心
- 数码/工具：男性或中性实测达人，桌搭/车内/办公场景，口吻直接专业
- 食品/饮品：生活方式试吃达人，厨房/餐桌/店内，口吻自然有食欲
- 本地生活：探店达人，门店/街边/服务场景，口吻真实到场
- 日用品/家居：实用生活用户，家中真实场景，口吻省事、好用、可信

Beauty does not mean plain. `Natural` means natural light, believable camera, real skin texture, and native UGC scene. For beauty, fashion, fragrance, jewelry, and style-led products, the creator may be attractive, polished, well-styled, and wearing makeup as long as the image still feels like a real creator photo rather than a studio ad or AI beauty portrait.

Use this persona selection rule:

- 精致型商品，如美妆、彩妆、香水、饰品、服饰、鞋包：优先生成好看、精致、有审美的女性达人，可以有妆容、发型和穿搭完成度。
- 自然功效型商品，如护肤、个护、母婴、健康、家居、食品：优先生成亲和、可信、自然生活感达人。
- 专业功能型商品，如数码、工具、家电、运动装备：优先生成实测感、专业感或生活方式达人，不强行美女化。
- If the product or target user suggests male, parent, senior, child, professional, outdoor, or niche creator identity, follow the product fit instead of defaulting to a young female creator.

## Caption Format

Return a concise caption using this format:

```text
creator_image_caption:
一位[年龄段]的[达人角色]，[发型/穿搭/气质]，在[真实场景]中，适合为[商品品类]做UGC带货/种草。她/他的商品关系是[为什么适合推荐该商品]，口吻[自然/专业/实用/朋友式]。
```

The caption must also include a product consistency note:

```text
product_consistency_note:
达人图仅作为人物参考；商品外观以后续传入的用户商品图为准。达人服装、配饰和背景道具不代表商品，不替代商品图中的真实商品。
```

If the product is apparel, shoes, bags, jewelry, or accessories, the note must explicitly say whether the product is worn/held in the creator portrait or whether the creator is only a presenter.

Example:

```text
creator_image_caption:
一位25岁左右的护肤测评达人，长发低马尾，穿浅色针织衫，站在室内梳妆台前，自然光照明，真实生活感，适合为敏感肌修护保湿水做UGC种草。她的商品关系是敏感肌护理体验者，口吻温和、可信、像朋友推荐。

product_consistency_note:
达人图仅作为人物参考；玉泽保湿水的外观以后续传入的用户商品图为准。达人服装、配饰和背景道具不代表商品，不替代商品图中的真实商品。
```

## Output Format

Use the compact Chinese output format below by default. Do not expose the internal high-quality creator image prompt, prompt variable name, detailed generation parameters, or long creator-appearance details to the user.

```text
达人参考图已生成完毕。请先确认是否继续生成视频；确认后会将用户原始指令、用户上传素材和达人参考图传给 ugc_idea_generator 生成脚本和视频。

达人信息汇总：

creator_portrait_image
{达人参考图路径或图片引用}

creator_image_caption
{中文caption。只保留年龄段、达人类型、发型/穿搭/气质、场景、适合的商品品类、商品关系和口吻。不展开完整生图细节。}

product_consistency_note
{中文商品一致性说明。说明达人图仅作为人物参考，商品外观以后续商品图为准，达人服装、配饰、背景道具不代表商品。}

script
{ugc_idea_generator 生成的脚本}

video_result
{ugc_idea_generator 产出的视频结果或视频任务信息}
```

Only output additional fields such as `product_source_of_truth`, `creator_reference_scope`, `creator_market_fit`, `non_product_elements`, `creator_image_source`, `portrait_aspect_ratio`, or `product_info` when the frontend/downstream pipeline explicitly requires them. Do not send these additional fields to `ugc_idea_generator`.

All user-facing descriptions must be written in Chinese. English field keys may be kept only when they are required by the downstream pipeline or match the established UI format. Do not output English descriptive sentences.

## Revision Rule

If the user asks to change the creator image, call `sandbox_generate_image` again with the revision instruction and return the updated image plus updated caption.

After the revised creator image is accepted or generated, ask the same `dynamic_questionnaire` confirmation again. Only after the user selects `继续生成视频`, call `ugc_idea_generator` again with only `materials` and `user_input`: user-uploaded materials first, the revised `creator_portrait_image` last, and the user's original instruction text unchanged.

## Final Consistency Check

Before returning the creator summary, script, and video result, check:

- If generating a new creator portrait, the internal high-quality creator image prompt is detailed enough for the image model but not exposed to the user.
- The actual image tool prompt matches the full internal high-quality creator image prompt, not a shortened version.
- `ugc_idea_generator` receives only `materials` and `user_input`.
- `materials` contains all user-uploaded images/files first and the active creator portrait last.
- `user_input` is the user's original instruction text exactly as received.
- The `ugc_idea_generator` request does not include expanded product_info, creator captions, consistency notes, rewritten prompts, or extra requirements.
- The creator portrait does not visually redefine the product.
- If the user uploaded a creator/person image, `sandbox_generate_image` was not called and the uploaded image is used as `creator_portrait_image`.
- The creator's ethnicity/region style follows the user input language, target market, product information, or uploaded creator reference.
- The caption clearly separates `creator_reference_scope` from `product_source_of_truth`.
- For non-apparel products, the creator's outfit and accessories are not described as the product.
- For apparel products, the caption states whether the creator is wearing the actual product or only acting as a presenter.
- For accessories, shoes, bags, and jewelry, unrelated styling items are not confused with the product.
- For services, apps, games, events, and virtual products, no fake physical product is invented.
- `product_consistency_note` is present.
- `non_product_elements` is present.

## Hard Rules

- Only use `sandbox_generate_image` for image generation.
- After creator image generation or binding, call `dynamic_questionnaire` before `ugc_idea_generator`.
- Only call `ugc_idea_generator` for script and video generation after the user selects `继续生成视频`.
- Do not manually write the final script when `ugc_idea_generator` is available.
- The `ugc_idea_generator` handoff must contain only `materials` and `user_input`.
- `materials` must contain user-uploaded materials and the active creator portrait; `user_input` must contain the user's original instruction text.
- Do not pass product_info, creator_image_caption, product_consistency_note, product_source_of_truth, creator_reference_scope, non_product_elements, rewritten prompts, generation requirements, or long summaries to `ugc_idea_generator`.
- Return the creator portrait summary plus the script/video result from `ugc_idea_generator`.
