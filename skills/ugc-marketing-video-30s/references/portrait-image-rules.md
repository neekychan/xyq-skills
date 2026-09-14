# 国内 UGC 达人画像生成规则

Use this reference whenever the skill needs to generate, bind, revise, or hand off an on-camera creator portrait for a domestic UGC marketing video.

The creator portrait is a character reference for the downstream script and video generation. It should help the video protagonist feel real, product-matched, and stable, but it must not redefine the product or force unwanted actions into the video.

## Required Tool

Creator portrait generation must use:

```text
sandbox_generate_image
```

Hard requirements:

- Use only `sandbox_generate_image` for creator portrait image generation.
- First classify uploaded materials: person/model/creator images versus product images, screenshots, packaging images, links, and non-person references.
- If the user uploaded a suitable creator/person/model reference image, use that uploaded image as `creator_portrait_image` and do not call `sandbox_generate_image` unless the user asks to replace or adjust the person.
- Product-only images, packaging images, screenshots, product links, and non-person references do not count as creator/person references.
- If no suitable person image is supplied, call `sandbox_generate_image` before script writing.
- Use a deterministic output path such as `/workspace/出镜达人/creator_portrait_subject_1.png`.
- After portrait generation or binding, use the active portrait as the character reference for script and video prompt writing.

## Internal High-Quality Creator Image Prompt Rule

Before calling `sandbox_generate_image`, internally build a complete high-quality creator image prompt. This skill only fixes the image tool name; it does not fix or expose the underlying image model.

This internal prompt must:

- Be passed into the `sandbox_generate_image` tool call as the actual image-generation prompt.
- Stay unchanged when passed to the tool. Do not compress, summarize, translate, or rewrite it into a shorter prompt.
- Not be exposed to the user. Do not show the internal prompt, prompt variable name, or detailed generation parameter list in the user-facing response.
- Include concrete details for camera perspective, framing, gesture, expression, hairstyle, makeup, outfit, scene, light direction, background objects, skin texture, anti-AI texture constraints, aspect ratio, product-boundary constraints, and watermark/text constraints.
- Be written in Chinese for Chinese/default domestic tasks.

Never call the image tool with only short generic wording such as:

```text
生成真实UGC达人图
生成美妆达人自拍
生成高质感人物图
```

## Workflow

1. Parse product and user context:
   - product_name
   - category
   - selling_point
   - target_user
   - platform
   - offer
   - user_requirements
   - user input language and target market

2. Choose a product-matched creator persona:
   - language/market fit
   - age band
   - creator role
   - hairstyle/outfit/temperament
   - real scene
   - relationship to product
   - speaking tone

3. Check whether the user uploaded a usable creator/person/model reference:
   - If yes, bind it as `creator_portrait_image`.
   - Preserve visible identity and style cues.
   - Create a concise `creator_image_caption`.
   - Do not call `sandbox_generate_image`.
   - If uploaded materials contain only product assets, packaging, screenshots, links, scenery, props, or non-person references, continue to image generation.

4. If no suitable creator/person image is supplied:
   - Internally build the full high-quality creator image prompt.
   - Call `sandbox_generate_image` with that exact full prompt.
   - Save/bind the result to `/workspace/出镜达人/creator_portrait_subject_1.png`.
   - Create a concise `creator_image_caption` and `product_consistency_note`.

5. If the user asks to adjust the creator image:
   - Call `sandbox_generate_image` again with the revision instruction.
   - Use a deterministic next path such as `/workspace/出镜达人/creator_portrait_subject_1_v2.png`.
   - Refresh script and video prompt to match the latest accepted portrait.
   - Do not proceed to video generation while the latest user intent is portrait adjustment.

## Realism And Framing Rule

Default portrait style:

- Use 4:5 vertical portrait by default. Use another ratio only when the frontend/downstream model explicitly requires it.
- Prefer half-body, bust, or waist-up composition. The creator should occupy about 60%-70% of the frame.
- Make the image feel like a real domestic UGC creator reference photo, not a studio campaign, beauty editorial, model portfolio, stock photo, or commercial ad.
- Preserve real skin texture: pores, slight skin tone variation, under-eye texture, tiny blemishes or redness when appropriate.
- Explicitly avoid waxy skin, plastic skin, clay-like skin, porcelain skin, airbrushed pores, overly even skin color, AI beauty filter texture, and oily face highlights.
- Preserve natural hair details: flyaway hair, uneven strands, natural volume, believable hairline.
- Make the creator approachable and warm: friendly eyes, slight natural smile, relaxed cheeks, open posture, like a real person who would share a product with friends.
- Avoid cold model expression, distant gaze, overly posed portrait mood, luxury influencer attitude, aloof beauty-shot mood, and emotionally flat perfect face.
- Use believable light: soft window light, curtain-filtered light, cloudy daylight, ordinary indoor ambient light, or controlled real sunlight that looks like an ordinary phone photo.
- Avoid fake hard light, unnatural sharp window-shaped patches, blown-out facial highlights, oily shine, glossy beauty lighting, commercial spotlight, and studio key light.
- Keep the background ordinary and believable, with mild life details when useful.
- Do not add visible text, watermark, AI-generated badge, fake logo, screen UI, subtitles, readable posters, or packaging text.

Default internal prompt sentence to include:

```text
生成一张4:5竖版真实手机照片风格的原生感UGC达人参考图，非棚拍、非商业广告、非精修写真。人物为半身或腰部以上构图，占画面约60%-70%。达人需要有亲切感，像真实会给朋友分享产品的人，眼神友好，轻微自然微笑，脸部表情放松，身体姿态自然打开。保留真实皮肤纹理、毛孔、轻微肤色变化、眼下自然纹理、自然碎发、真实发际线、衣服褶皱、普通生活背景和轻微手机拍摄感。皮肤不要蜡感、塑料感、磨皮过度、陶瓷感、AI美颜滤镜感、油亮反光。无文字、无水印、无AI生成角标、无logo。
```

## High-Texture Native Selfie Pattern

When the product benefits from a high-texture native creator look, write the internal image prompt as a concrete phone-photo scene, not a generic portrait.

Important distinction:

- Keep the phone-shot texture.
- Do not make the creator visibly hold a phone by default.
- Phone-camera feel means near-distance perspective, slight wide-angle distortion, ordinary phone HDR, casual framing, and real-life lighting.
- If a visible phone must appear, treat it only as a still-photo prop. It is not a persistent action reference for downstream video.

Use this internal prompt structure:

```text
生成一张超真实的手机前置摄像头自拍质感照片：[符合语言/市场/商品的人物]在[符合商品使用场景的真实生活地点]，[肩部以上/胸前近景/半身近景]构图，[看向镜头/手托腮/整理头发/拿杯子/比V/自然微笑等非手机动作]，[具体表情和亲切感]。[发型、妆容、穿搭]符合[商品品类/目标用户]。默认画面里不要出现手机，不要让达人手持手机。

画面中有[真实生活光线]，在[脸/肩膀/桌面/墙面/背景]形成自然高光和阴影，但不过曝、不油亮、不商业棚拍。背景是[具体生活空间]，出现少量与场景合理相关的日常物品，[列出3-6个生活物件]，整体有真实生活感，不要过度整理。

使用手机自拍视角的近距离透视感，轻微广角畸变，画面比例4:5，像普通iPhone/安卓手机随手拍，清晰但不商业摄影。手机感只代表拍摄质感，画面中不需要出现手机，也不要把拿手机作为达人动作。肤质真实，有细节毛孔、轻微肤色变化、眼下自然纹理和自然光影，不要美颜过度、不要塑料皮、不要蜡感、不要AI生成角标、不要文字水印。
```

Each internal prompt should include:

- one exact camera perspective, such as `手机前置摄像头自拍质感`, `近距离自拍透视`, or `轻微广角畸变`
- one non-phone pose or gesture, such as `自然微笑`, `手托腮`, `比V`, `拿杯子`, `整理头发`, `看向镜头`
- one exact light setup, such as `窗帘过滤光`, `阴天散射光`, `窗边阳光`, or `普通室内环境光`
- one real-life background with 3-6 everyday objects
- one skin realism sentence
- one anti-AI / anti-commercial sentence
- one product-boundary sentence

Product-adaptive scene examples:

- 美妆/护肤/香水：卧室梳妆台、浴室镜前、窗边化妆桌、厨房餐桌；可有镜子、化妆刷、纸巾、发夹、水杯、护肤小样等生活物件，但不要让道具替代商品。
- 服饰/鞋包/饰品：卧室穿搭区、衣柜旁、玄关镜前、咖啡店座位、街边自然光；可有衣架、帆布包、杂志、钥匙、镜子等生活物件。
- 食品/饮品：厨房餐桌、便利店外、办公室茶水区、客厅茶几；可有杯子、餐巾纸、零食盒、外卖袋、水瓶等生活物件。
- 数码/工具/办公用品：办公桌、书桌、车内、宿舍桌面；可有电脑、鼠标、线材、便签、咖啡杯、书本等生活物件。
- 母婴/家居/日用品：客厅、厨房、儿童房、洗手台、阳台；可有收纳盒、湿巾、玩具、毛巾、杯子、家务用品等生活物件。
- 本地生活/服务/课程/App/游戏：门店外、街边、咖啡店、通勤路上、沙发或书桌自拍质感；不要生成虚假实体商品，用人物和场景表达目标人群。

## Language And Market Fit

The creator should follow the user's language, product information, and target market:

- Chinese input with no other target market: default to a Chinese creator in a China-market UGC scene.
- Other languages: infer likely market from language, product, platform, currency, location words, URL, and user requirements.
- If the product page, brand, SKU, packaging, or user requirement clearly points to a country/region, follow that market over the language alone.
- If the user specifies creator gender, ethnicity, region, age, style, or persona, follow the explicit instruction.
- If the user uploaded a creator image, follow the uploaded person's visible identity and style.
- Do not randomly mix market signals.

## Creator Persona Fit

Choose one creator persona that fits the product:

- 护肤/美妆：优先选择好看、精致但真实的女性达人，可带自然妆或精致日常妆；场景为梳妆台、浴室镜前、卧室窗边或日常化妆区；光线自然，皮肤有真实纹理，口吻温和可信。
- 彩妆/香水/精致个护：可选择更精致的美女达人，妆容、发型和穿搭更完整，但仍保持手机原生感、自然光、真实皮肤质感和生活化场景。
- 服饰/鞋包：根据商品风格选择精致穿搭美女、自然风美女、通勤感达人、辣妹风达人或户外生活方式达人；强调上身/搭配/质感，但不要让达人私服替代商品。
- 母婴/家庭：真实宝妈或家庭照顾者，客厅/儿童房/厨房，口吻实用安心。
- 数码/工具：男性或中性实测达人，桌搭/车内/办公场景，口吻直接专业。
- 食品/饮品：生活方式试吃达人，厨房/餐桌/店内，口吻自然有食欲。
- 本地生活：探店达人，门店/街边/服务场景，口吻真实到场。
- 日用品/家居：实用生活用户，家中真实场景，口吻省事、好用、可信。

Natural does not mean plain. For beauty, fashion, fragrance, jewelry, and style-led products, the creator may be attractive, polished, well-styled, and wearing makeup, as long as the image still feels like a real creator photo rather than a studio ad or AI beauty portrait.

## Product And Creator Consistency

The creator portrait is a human-character reference. It must not redefine or invent the product.

Use these rules in the internal image prompt and handoff:

- The user's product image is the source of truth for product appearance.
- Preserve the product's category, shape, color, package, logo position, material, texture, size, SKU, and visible variants from the user-provided product image or text.
- If product appearance is uncertain, prefer a creator-only portrait: no product in hand, no product on table, no product-like prop in the foreground.
- The creator's clothing, accessories, background props, and scene objects must be visually distinct from the product.
- Do not add extra items that look like the product category unless they are intentionally the product.
- Do not let the creator outfit copy product packaging colors, logo, label blocks, or product shape unless the product is clothing and the user explicitly wants try-on.
- For non-apparel products, keep creator outfit simple and neutral.
- For apparel, shoes, bags, jewelry, or accessories, clearly state whether the creator is wearing/holding the actual product. If uncertain, show the creator as a matching presenter, not wearing a generated substitute.
- If a phone appears in the portrait, it is only a shooting/life prop, not a downstream video requirement. The video should not keep the creator holding a phone unless the script explicitly needs a phone bridge.

Add this product consistency sentence when product images are provided:

```text
达人形象只作为人物参考，用户提供的商品图是商品外观唯一依据；达人服装、配饰和背景道具与商品保持清楚区分。若画面中出现商品，商品外观严格保持用户商品图中的形状、颜色、包装、logo位置、材质、尺寸比例和款式，不生成替代商品。
```

Add this safer sentence when product appearance is uncertain:

```text
本次只生成达人本人，不在达人图中生成商品；后续算法使用用户提供的商品图作为商品外观依据。
```

## User-Facing Output

After generating or binding the portrait, keep the user-facing output compact and Chinese.

Do not expose:

- internal high-quality creator image prompt
- prompt variable names
- full appearance parameter list
- long hidden reasoning
- English descriptive sentences

Default user-facing portrait summary:

```text
达人参考图已生成完毕，我整理达人信息后直接生成营销视频提示词。

达人信息汇总：

creator_portrait_image
{达人参考图路径或图片引用}

creator_image_caption
{一位[年龄段]的[达人角色]，[发型/穿搭/气质]，在[真实场景]中，适合为[商品品类]做UGC带货/种草。她/他的商品关系是[为什么适合推荐该商品]，口吻[自然/专业/实用/朋友式]。}

product_consistency_note
{达人图仅作为人物参考；商品外观以后续传入的用户商品图为准。达人服装、配饰和背景道具不代表商品，不替代商品图中的真实商品。}
```

Only output additional fields when the frontend or downstream pipeline explicitly requires them.

## Handoff Fields For Downstream

When the pipeline needs structured handoff, include these fields internally or in machine-readable output:

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
用户上传达人图 / sandbox_generate_image生成达人图

portrait_aspect_ratio:
默认4:5竖版；仅当前端或下游算法明确要求时才改为其他比例。
```

## Final Check

Before script writing and video prompt writing, confirm:

- If no suitable uploaded creator image exists, `sandbox_generate_image` was called.
- The actual tool prompt was the complete internal high-quality creator image prompt, not a shortened prompt.
- The internal prompt was not exposed to the user.
- The portrait is 4:5 by default unless a specific downstream requirement says otherwise.
- The portrait does not visually redefine the product.
- The product image remains the source of truth for product appearance.
- The creator's market/ethnicity/region style follows user language, target market, product info, or uploaded creator reference.
- The portrait does not force the video protagonist to keep holding a phone.
- `creator_image_caption` and `product_consistency_note` are present.
