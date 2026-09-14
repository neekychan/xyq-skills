---
name: ugc-seasonal-promotion-video
description: >
  当用户需要围绕 618、99 大促、双11、双12、七夕、年货节、开学季、开门红、返场、年中大促、电商促销、直播间带货、限时秒杀、低价试用、0.01元购、1分钱抢、叠券、满减、折扣、赠品、加赠、买赠、到手价、专享价、小黄车、商品卡或大促素材生成 UGC 营销视频、口播脚本、直播切片脚本、短视频生成 prompt、Seedance/Pippit/小云雀视频 prompt 时调用。重点是突出大促节点、省钱、折扣、赠品、价格锚点、行动路径和直播间成交转化。
  Use this skill for 618, 99 sale, Double 11, Double 12, Qixi, Lunar New Year sale, back-to-school sale, mid-year sale, ecommerce promotion, live-commerce, flash sale, low-price trial, 0.01-yuan deal, coupon stack, full reduction, discount, gift, add-on, final price, exclusive price, yellow-cart, product-card, UGC commerce video, voiceover script, live-room clip script, and Seedance/Pippit/Xiaoyunque video prompts. The focus is campaign occasion, savings, discounts, gifts, price anchors, action path, and live-room conversion.
---

# UGC Seasonal Promotion Video / 时令与大促营销视频

## Goal / 目标

Turn product facts, offer mechanics, discount info, gifts, live-room benefits, product images, links, scripts, or reference videos into conversion-first campaign promotion videos. Default campaign is 618 when the user does not specify another occasion.

把商品信息、优惠机制、折扣、赠品、直播间权益、商品图、链接、脚本或参考视频，转成适合抖音、快手、小红书、微信等平台的大促带货短视频。用户未指定节点时默认按 618 处理；用户指定 99、双11、七夕、年货节等节点时，所有口播、花字、视觉符号和 CTA 自动适配该节点。核心目标是让用户快速看懂：现在买省多少、折扣怎么叠、赠品有什么、怎么领、怎么拍。

## Skill Responsibility Split / 技能分工

Use this skill for campaign promotion mechanism logic:

- campaign occasion routing: 618, 99, Double 11, Qixi, Lunar New Year, back-to-school, etc.
- Hook route, benefit route, CTA route
- price/coupon/gift/final-price/stock-up/live-room benefit logic
- what the user saves, gets, and does next

Follow `ugc-marketing-video` for visual execution quality:

- scene aesthetics, creator performance, camera movement, transition quality
- product consistency, physical plausibility, hand/action completion
- safe layout, text readability, lip sync, and overall commercial beauty

Default visual priority is real product, verified gifts, creator reaction, creator-with-gift-table shots, bundle table, price/coupon mechanism cards, and stable phone-bridge shots. Creator and gift pile can appear in the same frame when it improves emotion, urgency, or trust. For most videos, convert screenshot facts into real product shots, gift layouts, and concise mechanism cards.

## Trigger / 触发

Use this skill when the user mentions any shopping-festival or promotion-oriented intent:

- 平台大促：618、年中大促、99大促、99划算节、双11、双十一、双12、双十二、年货节、春节不打烊、开门红、返场、年终大促、周年庆、平台周年庆、超级品牌日、品牌日、会员日、超级会员日、粉丝节、宠粉节、直播节、好物节、购物节、开仓日、清仓节、补贴日、百亿补贴、国补、限时秒杀、限量抢购、预售、定金、尾款、爆品日、尖货日、品类日。
- 节日礼赠：元旦、春节、元宵节、妇女节、女王节、女神节、白色情人节、清明、劳动节、五一、母亲节、护士节、520、父亲节、端午节、七夕、情人节、中秋节、国庆节、教师节、重阳节、万圣节、感恩节、平安夜、圣诞节、跨年。
- 季节场景：春季上新、夏日大促、秋冬上新、冬季囤货、换季促、开学季、毕业季、暑期、寒假、春游、露营季、出游季、旅行季、运动季、婚礼季、乔迁季、装修季、收纳季、年终囤货、返工季、返校季、通勤季。
- 品类节点：美妆节、护肤节、香氛节、家清节、家电节、数码节、母婴节、宠物节、食品节、酒水节、生鲜节、服饰节、内衣节、鞋包节、珠宝节、家装节、家具节、车品节、健康节、医护节、户外节、运动节、摄影节、游戏节、潮玩节、文具节。
- 直播间与达人专场：直播间福利、达人专场、明星专场、总裁价到、老板价到、工厂直播、仓库直播、产地直播、源头工厂、品牌自播、官方直播间、私域专享、粉丝专享、老客专享、新人专享、会员专享、88VIP、黑卡、PLUS会员、超会专享。
- 省钱、折扣、满减、叠券、券包、到手价、爆价、低价、买一赠一、第二件半价、加赠、赠品
- 0.01元购、1分钱抢、0元试用、低价试用、拍下锁权益、先领券、点小黄车、商品卡
- 需要生成 618/99/双11/七夕/年货节等带货视频、促销口播、直播切片、投流素材、Seedance/Pippit/小云雀视频 prompt
- 兜底触发：任何包含 `大促`、`节`、`季`、`专场`、`品牌日`、`会员日`、`福利日`、`补贴`、`抢购`、`秒杀`、`预售`、`返场`、`囤货`、`礼遇`、`宠粉`、`开仓`、`清仓`、`上新`、`直播间机制` 的商品营销任务。

## Campaign Occasion Adaptation / 大促节点适配

Before writing any script or prompt, identify `campaign_occasion`. If the user says 618, use 618. If the user says 99, Double 11, Qixi, Lunar New Year, back-to-school, brand day, category day, member day, live-room special, or another campaign, replace all visible and spoken campaign wording with that occasion. If no occasion is specified, default to 618.

Campaign occasion affects four things:

1. `口播称呼`: say the correct event name, such as `618`, `99大促`, `双11`, `七夕礼遇`, `年货节`, `开学季`, `品牌日`.
2. `视觉符号`: choose event-appropriate props, colors, and scenes without weakening the promotion mechanic.
3. `购买动机`: map the deal to the occasion: stock-up, gifting, seasonal change, relationship gift, household replenishment, beauty refresh, back-to-school prep, or New Year hosting.
4. `CTA`: use the action that matches the platform and occasion: `先领券`, `点商品卡`, `进直播间`, `现在下单`, `给TA备礼`, `年货先囤`, `开学先备齐`.

Campaign occasion vocabulary / 大促节点词表:

- `平台年中/年末型`: 618、年中大促、99大促、99划算节、双11、双十一、双12、双十二、年终大促、年度盛典、返场、开门红。Core motive: lowest-price feeling, coupon stack, final price, stock-up, gift pile, countdown.
- `预售/锁价型`: 预售、定金、尾款、抢先购、提前购、先享价、锁权益、0.01元锁、1分钱抢。Core motive: lock benefit now, pay later, limited benefit.
- `补贴/券包型`: 百亿补贴、官方补贴、平台补贴、国补、消费券、满减券、跨店满减、店铺券、品类券、88VIP券、PLUS券、会员券。Core motive: stack discount and show the claim path.
- `品牌/会员型`: 超级品牌日、品牌日、品牌周年庆、会员日、超级会员日、黑卡日、PLUS会员日、88VIP、粉丝节、宠粉节、老客专享、新人专享。Core motive: exclusive benefit, member gift, points, official brand backing.
- `直播间/达人型`: 直播间福利、达人专场、明星专场、总裁价到、老板价到、工厂直播、仓库直播、产地直播、品牌自播、官方直播间。Core motive: live-exclusive mechanism, yellow cart/product card, limited gift, fast CTA.
- `春节/年货型`: 年货节、春节、春节不打烊、元旦、跨年、元宵节、团圆季。Core motive: family stock-up, New Year gifting, hosting, pantry restock, red-gold festive benefit.
- `女性/礼赠型`: 女王节、女神节、妇女节、母亲节、520、七夕、情人节、白色情人节、圣诞节、平安夜、教师节。Core motive: gift for self/TA, limited gift box, premium add-on, romance or care scene.
- `家庭/亲子型`: 父亲节、母亲节、儿童节、开学季、返校季、寒假、暑期、毕业季。Core motive: family prep, student/dorm setup, parent-child use, useful bundle.
- `季节换新型`: 春季上新、夏日大促、秋冬上新、换季促、冬季囤货、出游季、露营季、旅行季、运动季、通勤季、返工季。Core motive: immediate seasonal use, wardrobe/vanity/home refresh, bundle prep.
- `生活事件型`: 婚礼季、乔迁季、装修季、收纳季、搬家季、新居季、年终囤货。Core motive: scenario purchase, full-set solution, one-time stock-up.
- `品类专属型`: 美妆节、护肤节、香氛节、洗护节、家清节、家电节、数码节、母婴节、宠物节、食品节、酒水节、生鲜节、服饰节、内衣节、鞋包节、珠宝节、家装节、家具节、车品节、健康节、医护节、户外节、运动节、摄影节、游戏节、潮玩节、文具节。Core motive: category-specific need plus campaign deal.
- `清仓/上新型`: 开仓日、清仓节、换季清仓、尾货清仓、上新日、新品首发、尖货日、爆品日。Core motive: limited stock, price drop, new launch gift, hurry CTA.

Occasion routing examples:

- `618 / 年中大促`: strongest price, coupon stack, gift pile, stock-up, limited-time benefit. Visual tone: high-energy deal room, gift table, coupon cards, product pile.
- `99大促 / 99划算节`: value-for-money, daily stock-up, practical savings, low-threshold coupon. Visual tone: household replenishment, drawer/shelf refilled, price card impact.
- `双11 / 双12`: annual lowest-price feeling, big cart, presale/deposit, cross-store full reduction, stock-up wall. Visual tone: cart burst, countdown, full-table haul, order checklist.
- `七夕 / 情人节 / 520`: gifting and self-love, couple/friend surprise, gift box, romance benefit, limited gift. Visual tone: gift table, ribbon, mirror/vanity, date-prep scene; keep promotion explicit with price/gift/coupon cards.
- `年货节 / 春节`: family stock-up, gifting, hosting, New Year package, multi-pack value. Visual tone: dining table, living room, red-gold accents, gift boxes, pantry restock.
- `开学季`: student/dorm/office prep, back-to-school set, useful bundle, low unit price. Visual tone: desk, backpack, dorm shelf, checklist.
- `超级品牌日 / 会员日`: brand-exclusive benefits, member gift, points, official subsidy, live-room special. Visual tone: brand desk, membership card, official benefit card.

Do not leave `618` wording in a non-618 campaign unless the product page explicitly uses 618. Replace generic stickers too: `618到手¥X` becomes `{campaign_occasion}到手¥X`; `618福利` becomes `{campaign_occasion}福利`.

## Core Judgment / 核心判断

大促视频优先回答三个问题：

1. `比平时省多少`: 平时价/优惠前价 -> {campaign_occasion} 到手价 -> 省了 ¥X 或低至 X 折。
2. `额外多拿什么`: 买赠力度、加赠数量、赠品价值、组合装、会员权益、低价试用或直播间权益。
3. `多久内怎么拿`: 限时节点、限量赠品、先领券、点击下方链接购买、进入直播间购买、点小黄车、拍 0.01 元链接、加购、下单或评论关键词。

## Hook + Benefit + CTA Routing / 钩子-利益点-行动路由

Before writing the prompt, choose one Hook route, one primary Benefit route, and one CTA route. Keep them aligned across picture, voice, and sticker text.

Hook routes / 钩子路由：

- Regular-price comparison / 平时价对比：use when regular/original price and campaign final price exist. Voice pattern: `平时¥X，{campaign_occasion}¥Y` or `这单省¥X`. Visual: product with before/after price sticker.
- Price drop / 价格直降：use when final price, official reduction, or subsidy is clear. Voice pattern: `优惠前¥X，现在¥Y` or `{campaign_occasion}到手¥X`. Visual: product with large price sticker.
- Coupon stack / 叠券路径：use when coupons, 88VIP, or full reduction are central. Voice pattern: `先领券，再看商品卡` or `券补一起叠`. Visual: front-facing phone coupon page plus product.
- Gift pile / 赠品堆叠：use when gifts are visually strong. Voice pattern: `买X送Y`, `赠品这一套一起给`, or `赠品价值¥X`. Visual: gift lineup, open box, or bundle flat lay.
- Deposit lock / 定金锁权益：use when presale or deposit mechanism is central. Voice pattern: `定金¥X先锁` or `尾款日再付`. Visual: deposit button, presale page, and product.
- Live-room benefit / 直播间权益：use when live-exclusive price, yellow cart, or host clip exists. Voice pattern: `进直播间先领券` or `点小黄车看第一件`. Visual: host/product desk plus phone product card.
- Limited benefit / 限时限量：use when deadline, limited gift, or limited coupon exists. Voice pattern: `今晚前领这张券`, `赠品限量发`, or `X点前这个价`. Visual: countdown sticker plus product/gift.
- Stock-up value / 囤货值感：use for daily goods, family size, or multi-pack. Voice pattern: `{campaign_occasion}一次囤更划算` or `这一箱够用很久`. Visual: quantity spread or storage scene.

Benefit routes / 利益点路由：

- Saving comparison / 对比平时省钱：show regular/original price, campaign final price, and saved amount. Sticker examples: `平时¥X`, `省¥X`, `低至X折`.
- Final price / 到手价：show product plus final price, with original price as comparison. Sticker examples: `到手¥X`, `省¥X`.
- Official subsidy / 官方补贴：show official subsidy tag or platform subsidy card. Sticker examples: `官方补贴¥X`, `平台补贴`.
- Coupon/full reduction / 券与满减：show coupon page, product card, or order price. Sticker examples: `满X减Y`, `先领券`.
- Gift intensity / 买赠力度：show buy-gift quantity, gift size, gift value, and gift lineup. Sticker examples: `买X赠Y`, `加赠X件`, `赠品¥X`.
- Member benefit / 会员权益：show 88VIP, points, member gift, or member coupon. Sticker examples: `会员券`, `积分加倍`.
- Limited-time benefit / 限时福利：show deadline, countdown, limited coupon, or gift window. Sticker examples: `今晚截止`, `X点前`, `限量发`.
- Low-price action / 0.01元动作：show verified low-price link, reservation, or lock-benefit action. Sticker examples: `0.01元锁`, `先拍权益`.
- Service benefit / 履约服务：show free shipping, fast delivery, installment, or after-sales as support. Sticker examples: `免运`, `分期免息`, `售后无忧`.

CTA routes / 行动路由：

- Claim coupon / 领券：coupon or full reduction exists. CTA wording pattern: `点击下方链接领券购买`, `先领券再抢`, `领券后到手更划算`.
- Click lower link / 下方链接购买：product link, landing link, or video caption link exists. CTA wording pattern: `快点击下方链接抢购吧！`, `点击下方链接领券购买`, `下方链接直接抢`.
- Product card / 商品卡：short-video ecommerce page exists. CTA wording pattern: `点商品卡领券购买`, `点商品卡看这波优惠`, `商品卡里直接抢`.
- Live-room benefit / 直播间优惠：live benefit exists. CTA wording pattern: `快来直播间抢购吧！`, `来直播间更划算，手慢无！`, `来直播间领优惠券，到手更划算`.
- Yellow cart / 小黄车：live-commerce route exists. CTA wording pattern: `点小黄车看这波优惠`, `小黄车里直接抢`.
- Pay deposit / 付定金：presale deposit exists. CTA wording pattern: `先付定金锁权益`, `定金先锁这个价`.
- Lock low-price benefit / 锁权益：0.01 yuan or reservation exists. CTA wording pattern: `先锁权益再下单`, `0.01先锁这波福利`.
- Place order / 下单：final price is clear. CTA wording pattern: `这个价现在下单更划算`, `看准这套直接下单`.

CTA matching rule: choose wording from the user's actual purchase path, platform, coupon type, live-room benefit, product-card path, link path, or reservation path. Keep the CTA warm and action-oriented, with shopping urgency and benefit clarity.

## Production Path / 生产路径

Choose exactly one production path before writing.

Production paths / 生产路径：

- New promo video / 全新大促视频：use when product images, title, page info, price, coupon, or gift are provided. Build a 30s prompt from Hook + Benefit + Mechanism/Gift Reveal + Product Proof + Urgency + CTA.
- Script-to-video / 脚本视频化：use when the user provides exact voiceover or timeline. Preserve line meaning; map each line to matching `shot_action`, `camera`, and `sticker_text`.
- Reference remix / 参考素材复刻：use when the user gives screenshots, competitor video, or top material style. Reuse hook rhythm and CTA shape; replace product, price, gift, and platform facts with the current product.

## Script-To-Video Execution / 指定脚本视频化

Use this path when the user provides a fixed script, fixed voiceover, timestamped copy, shot list, or says `按照这个脚本`, `不要改文案`, `照着这段口播生成`, `脚本如下`.

Script priority:

- The user-provided script is the source of truth. Keep every line's meaning, order, and campaign claim.
- Split the script into 4-6 video beats according to punctuation, timestamps, or semantic pauses.
- Map each script line to one visible promotion action: price card, coupon card, gift reveal, product proof, product-card bridge, countdown, or CTA.
- Keep `voiceover_zh` equal to the user script line when the user asks to preserve wording.
- `sticker_text` condenses the same beat into a shorter offer tag; it does not replace or rewrite the spoken script.
- If the script contains unverifiable price, gift, 0.01 yuan, ranking, or deadline claims, keep the user's wording only when the user explicitly provided it as the desired script; otherwise mark uncertain facts with placeholders.

Script-to-video output shape:

```text
script_lock / 脚本锁定：preserve user script line order and meaning.
Beat 1: script_line_1 -> shot_action -> camera -> sticker_text -> visual_audio_match
Beat 2: script_line_2 -> shot_action -> camera -> sticker_text -> visual_audio_match
...
```

For Seedance 2.0, write script preservation as positive execution language:

- `按用户脚本逐句生成口播，每句口播对应一个镜头动作。`
- `每个 voiceover_zh 使用用户脚本原句或等义短句。`
- `画面动作服务当前脚本利益点：价格、券、赠品、到手量、限时或CTA。`
- `脚本中的商品名、规格、价格、赠品和活动节点按用户输入呈现。`

## Mandatory Campaign Visual Hooks / 必选大促视觉钩子

Every campaign output must choose one visible promotion hook before writing the timeline. The hook is a visual event, not a spoken explanation.

- `福利奇观`: a table, shelf, suitcase, drawer, or vanity fills with the main product plus verified gifts/add-ons; use for daily goods, beauty, snacks, baby, household, and pet products.
- `赠品摆开`: main product appears, then verified gifts or add-ons are placed one by one until the table visibly fills up.
- `表情包反应`: creator reacts with meme-style shock, frozen face, exaggerated stare, split-screen chat reaction, or sticker-style expression after seeing the campaign benefit; immediately show the product and offer card.
- `夸张剧情`: use safe, stylized, clearly comedic drama such as boss/运营“手滑上链接”, friend group rushing in, creator sliding into frame, suitcase bursting open, or a symbolic parachute/airplane-jump meme to chase the campaign deal. Keep it non-realistic, non-injury, brand-safe, and finish the joke within 2 seconds.
- `从天而降福利`: verified gifts, coupon cards, or product packs visually drop into a basket/table/vanity in a controlled, stylized way. Objects land cleanly and remain consistent; no physical chaos or product deformation.
- `0.01元权益`: only use when evidence confirms a 0.01 yuan, 1-cent, trial, reservation, or lock-benefit action. If unverified, write `[0.01元权益如属实展示]` or replace with `限量福利`.
- `到手量暴击`: show a clear `买X到手Y`, `买50ml到手80ml`, `拍1发N`, or bundle quantity reveal when evidence exists.
- `券包砸脸`: show coupon/subsidy/member benefit cards stacking beside the product, with each card fully visible and readable.
- `限时抢跑`: show countdown, deadline, limited gift, or live-room exclusive card beside the product.
- `福利堆山`: show full-table gift proof, open-box bundle, or shelf/vanity replenished with the product and verified add-ons.

The first 3 seconds must show one of these hooks with the product visible or revealed by second 2. Open with a promotion event: gift pile, coupon card, final-price card, final-quantity card, 0.01 benefit card, countdown card, meme reaction tied to the offer, or CTA card. At least three beats in a 30s video must show explicit promotion visuals.

Visual hooks can be high-drama, but the payoff must be commercial: by second 3 the viewer knows the product category, the campaign benefit type, and why to keep watching. A dramatic hook that does not land on price, coupon, gift, final quantity, limited time, or CTA fails.

## Conversion Rhythm / 高转化节奏

Campaign outputs are made for promotion impact with fast entry, clear savings, and compact deal explanation. Default speech is medium-fast, clear, compact, and discount-dense.

- Use `medium-fast deal-hunter delivery`: quick cuts, short spoken lines, clear price stickers, and immediate deal entry.
- Promotion benefits are the main story and must feel louder than product education: price, discount, coupon, subsidy, gift, 0.01 yuan action, live-room benefit, limited time, and CTA fill 80-90% of the video.
- In explicit campaign promotion requests, use `promotion-dominant mode`: promotion benefits occupy 90%+ of visible action and spoken content. Product selling points are only proof tags, not explanation segments.
- Product functional selling points are supporting proof only. Use at most one micro proof phrase, normally under 1 second or one half-sentence, then immediately return to gift/coupon/final-price/CTA.
- Default 30s balance: eight promotion beats, with two compact product-proof or scenario beats attached to promotion value. Do not create a standalone product-selling-point beat unless the user explicitly asks for product education.
- If a draft feels like a product explainer, rewrite it into a promotion clip by replacing feature explanation with `到手量`, `赠品`, `券`, `满减`, `限时`, or `先领券再拍`.
- Every spoken line carries one of these: price advantage, discount, subsidy, coupon, gift, urgency, or action path.
- Keep Chinese spoken lines short: normally 8-16 Chinese characters, one sentence per beat.
- Keep voice pace controlled: medium-fast, clear articulation, natural 0.2-0.4 second pause between beats, with a lively campaign deal-explainer rhythm.
- Put the savings comparison in the first 2 seconds when evidence exists: regular/original price, campaign final price, and saved amount. Good hooks: `平时¥X，{campaign_occasion}¥Y`, `这单省¥X`, `到手才¥X`, `买正装送这一堆`.
- Use this default order: `regular-price comparison -> final price -> discount stack -> gift intensity -> limited-time CTA`. For soft seeding requests, keep the same offer order with gentler wording.
- Repeat the main price advantage visually at least twice: first hook and final CTA.
- Use stronger contrast when evidence exists: `平时¥X / {campaign_occasion}¥Y / 省¥Z`, `优惠前¥X / 到手¥Y`, `买X送Y`, `赠品价值¥X`, `低至X折`, `X点前这个价`, `定金¥X锁`.
- Product proof is supporting evidence. Keep it as a tag attached to the deal: `这个规格现在¥X`, `敏感肌可囤这个价`, `大牌这价可囤`, `买正装还送同款`. Avoid lines that only explain ingredients, texture, function, efficacy, origin, technology, certification, ranking, or usage steps without a campaign benefit.
- Use promotion-first lines such as `到手¥X`, `买60赠60`, `30元定金先锁`, `先领券再拍`.
- Voiceover prompts explicitly request: `中快语速，吐字清楚，每句之间有短停顿，像{campaign_occasion}直播切片，每2-3秒给一个促销利益点`.

### Product-Selling-Point Suppression / 卖点讲解压缩

For campaign deal ads, product selling points must not become the narrative. Treat them as reasons to believe the deal, not topics to explain.

- Use this default structure: `{campaign_occasion}福利爆点 -> 券/到手价 -> 赠品/到手量 -> 限时/限量 -> CTA`.
- Product proof appears as one short tag attached to a deal beat, after the price/coupon/gift logic is already visible.
- A 30s script may contain two different product-proof phrases, and both phrases must include or sit beside a promotion cue such as `这个规格{campaign_occasion}可囤`, `这套现在送`, `这个正装价才值得冲`.
- If a line does not include `{campaign_occasion}`, `券`, `赠`, `送`, `到手`, `省`, `满减`, `叠`, `限时`, `抢`, `0.01`, `商品卡`, `直播间`, or `先领`, rewrite it.
- Visual proof such as texture, use effect, ingredient, material, certification, flavor, capacity, or function must be shorter than the gift/coupon/final-price reveal and cannot occupy the opening or closing beat.
- If offer facts are incomplete, do not fill time with product selling points. Use placeholders and promotion framing: `[填写真实到手价]`, `[确认赠品名称]`, `先领券`, `限量福利`, `以实际活动为准`.

## Voiceover Diversity / 口播话术多样性

Campaign voiceover sounds like a real deal explainer with varied, concrete promotion wording.

- Use standard Mandarin Putonghua, clean close-mic sound, clear consonants and vowels, complete word endings, and steady medium-fast delivery.
- Keep background music below the voice. The spoken deal information stays crisp and easy to understand on mobile speakers.
- Prefer numbers, mechanisms, and actions over vague intensifiers.
- Each `voiceover_zh` uses a different sentence pattern across the 5 beats.
- Before finalizing, build a `voiceover_sequence` and check adjacent lines. Neighboring `voiceover_zh` lines use different openings, different sentence structures, and different benefit focuses.
- Final CTA uses a new action sentence when the opening already used the savings anchor. Good: first line `平时¥X，{campaign_occasion}¥Y`; final line `省¥Z后点下方链接`.
- Generic excitement words appear at most once in a full 30s script; concrete benefits carry the main persuasion.
- Use one concrete claim per line. Good: `券后¥99。` `买一套送两件。` `先领满减券。`
- Do not use two neighboring lines for product education such as ingredients, efficacy, texture, usage method, or brand story.
- In a 30s campaign ad, at least 6 out of 8 spoken lines should include a promotion cue: `{campaign_occasion}`, `券`, `赠`, `到手`, `省`, `满减`, `叠`, `限时`, `抢`, `商品卡`, `直播间`, or `先领`.
- Product-selling-point wording must be promotion-attached. Good: `这个规格{campaign_occasion}送同款。` Bad: `它的质地很轻薄，适合日常护肤。`
- Rotate phrasing by function:
  - savings comparison: `平时¥X，{campaign_occasion}¥Y`, `这单省¥X`, `优惠前¥X现在¥Y`, `低至X折`
  - price shock: `到手¥X`, `券后¥X`, `低到¥X`
  - discount path: `先领券`, `官方立减¥X`, `补贴还能叠`, `定金先锁`
  - gift intensity: `买X送Y`, `加赠X件`, `赠品价值¥X`, `赠品限量`
  - urgency/trust: `今晚截止`, `X点前这个价`, `已售X万+`, `回购榜第X`
  - CTA: `点击下方链接购买`, `进入直播间购买`, `先领券再拍`, `点商品卡`, `现在锁权益`
- For the same product, keep the 5 spoken lines semantically progressive: savings comparison -> final price/coupon/subsidy -> gift intensity -> limited/trust/use -> action.

## Voiceover Route / 口播话术路由

Choose a voiceover route based on Hook + Benefit + CTA. Rotate routes across batch outputs.

Voiceover route options / 口播路由文字版：

- Savings anchor / 省钱锚点：use when regular/original price and campaign price exist. Sentence style: comparison sentence. Example: `平时¥X，{campaign_occasion}¥Y，省¥Z`.
- Price anchor / 价格锚点：use when original price and final price are clear. Sentence style: final-price sentence. Example: `优惠前¥X，现在¥Y`.
- Coupon guide / 领券攻略：use with coupon, full reduction, 88VIP, or product card. Sentence style: action sentence. Example: `先领券，再看商品卡`.
- Subsidy stack / 补贴叠加：use with official, platform, or government subsidy. Sentence style: mechanism sentence. Example: `官方补贴¥X还能叠`.
- Gift intensity / 买赠力度：use when gift or bundle is strong. Sentence style: quantity/value sentence. Example: `买X送Y，赠品价值¥Z`.
- Limited-time push / 限时推动：use with deadline, limited gift, or limited coupon. Sentence style: deadline sentence. Example: `X点前还是这个价`.
- Presale lock / 预售锁价：use with deposit, reservation, or tail payment. Sentence style: step sentence. Example: `定金¥X先锁`.
- Lower-link command / 下方链接指令：use when product link or video caption link exists. Sentence style: direct purchase sentence. Example: `点击下方链接购买`.
- Live-room command / 直播间指令：use when live benefit or yellow cart exists. Sentence style: command sentence. Example: `进入直播间购买`.
- Trust proof / 信任背书：use with sales, ranking, repeat purchase, or old-customer evidence. Sentence style: proof sentence. Example: `已售X万，老客多`.
- Stock-up reminder / 囤货提醒：use for daily goods or family-size products. Sentence style: usage sentence. Example: `{campaign_occasion}一次囤齐`.

Voiceover route sequence for default 30s:

```text
Beat 1: Hook with product and campaign atmosphere
Beat 2: Brightest savings anchor or price/mechanism anchor
Beat 3: Mechanism, gift, coupon stack, member benefit, or final quantity reveal
Beat 4: Product proof 1
Beat 5: Product proof 2 or use scenario
Beat 6: Campaign time and offer path
Beat 7: Limited-time push, trust proof, stock reminder, or delivery/availability reason
Beat 8: CTA command matched to the user's purchase path
```

## Voice-Picture Match / 声画同步

Voice, picture, and sticker describe the same current beat.

- When `voiceover_zh` says a price, the frame shows product + price sticker or order/coupon page.
- When `voiceover_zh` says a coupon/subsidy path, the frame shows coupon page, product card, order page, or a clear coupon sticker.
- When `voiceover_zh` says a gift/add-on, the frame shows the gift lineup, package, or bundle.
- When `voiceover_zh` says a function or use proof, the frame shows that exact product use or proof action.
- When `voiceover_zh` says CTA, the frame shows product + CTA sticker, live room desk, product card, or button area.
- The same beat's `shot_action`, `camera`, `voiceover_zh`, and `sticker_text` refer to the same offer, product, or action.
- Finish one spoken line before switching to the next unrelated scene. Cut after a completed line, completed product action, or visible price/gift reveal.

Preferred 30s script structure:

```text
0-3s: Hook. Product visible; use visual hook or oral hook from the campaign hook library.
3-7s: Brightest offer. Say one strongest price, coupon/subsidy mechanism, gift, final quantity, 0.01 benefit, or live-room benefit.
7-11s: Mechanism/gift reveal. Show gift placement, coupon stack, price card, bundle reveal, or benefit card.
11-15s: Product proof 1. One product-specific function/effect/specification/use-scene sentence with matching visual proof.
15-19s: Product proof 2 or scenario. Add a different compact proof or real-life use scene.
19-23s: Campaign time + offer path. Say deadline/activity window and how to get the offer.
23-27s: Urgency/trust reminder. Show deadline, limited gift, stock, official benefit, fast delivery, or verified proof.
27-30s: Single CTA. Product visible; one purchase action only.
```

## Seedance/Seedream Prompt Language / 模型可执行语言

Write prompts in concrete visual language that Seedance, Seedream, Pippit, and 小云雀 can execute.

- Use bilingual execution labels in the final prompt when useful: `time / 时间`, `script_task / 本镜任务`, `shot_action / 画面动作`, `camera / 镜头`, `voiceover_zh / 中文口播`, `sticker_text / 短花字`, `visual_audio_match / 声画匹配`.
- Default video language is Chinese: keep `voiceover_zh` and `sticker_text` in Chinese for China ecommerce. Use English clauses to clarify execution, camera, timing, and model constraints. Add `voiceover_en` or `sticker_text_en` for explicitly requested bilingual creative.
- `shot_action` describes visible subjects and movement: product placement, hand action, unboxing, coupon page, gift lineup, usage shot.
- `camera` describes framing and motion: close-up, medium shot, push-in, quick cut, table flat lay, handheld, front-facing phone shot.
- `voiceover_zh` is the spoken line. It is short, medium-fast, standard Mandarin, clear, and progressive.
- `sticker_text` is a short offer tag or price sticker. It is placed near the product, coupon, gift, or CTA area.
- `script_task` names the current task for the beat: Hook, brightest offer, product proof, campaign time + offer path, or CTA.
- Keep `voiceover_zh` and `sticker_text` as different text in the same beat. Voice says the message; sticker compresses the offer.
- Keep each beat's `voiceover_zh` different from the previous beat. Keep each beat's `sticker_text` different from the previous beat.
- Keep adjacent `voiceover_zh` lines visibly different in wording. Use different first words, different verbs, and different sentence structures across neighboring beats.
- The main price can appear in beat 1 and beat 5, using different expressions: `到手¥X` first, `领券后¥X` or `¥X再拍` at the end.
- Sticker text works as price tags, coupon tags, gift tags, urgency tags, and CTA tags. Default text layer uses short stickers, price tags, offer tags, and CTA tags. Requested subtitle deliverables use `subtitle_text`.

Script progression pattern:

```text
Beat 1 voiceover: hook. Sticker: campaign/hook tag.
Beat 2 voiceover: brightest offer/mechanism. Sticker: price/mechanism/gift tag.
Beat 3 voiceover: one product proof sentence. Sticker: product-proof tag.
Beat 4 voiceover: campaign time + offer path. Sticker: deadline/path tag.
Beat 5 voiceover: single action. Sticker: CTA tag.
```

## Real-Scene Transition Rules / 实景转场规则

Keep transitions natural inside real-life footage. Scene changes feel like edits from a real phone-shot video.

- Choose the transition method from this positive transition set: `direct quick cut after action completion`, `push-in to price card`, `pull-back to full gift table`, `pan across product/gift lineup`, `tilt from product to creator reaction`, `rack focus from product to coupon card`, `match cut on product shape`, `match cut from package close-up to bundle flat lay`, `cut from table flat lay to usage close-up`, `cut from creator reaction to gift reveal`, `cut from product placement to final CTA bundle`.
- Every beat names one positive transition or camera movement in `camera`.
- Use hands as functional product actions inside the shot: holding the product, opening the package, placing verified gifts on the table, pointing to a coupon card edge, applying the product, pressing a button, or placing the item down.
- Hand action happens inside product, phone, package, gift, or usage beats. The hand belongs to the visible creator or the same off-screen creator.
- When a hand appears, keep it at product/table/phone distance with visible wrist and forearm context and a clear purpose. The scene cut happens after the hand action finishes and the product or gift is readable.
- Default visible hand count is one hand. For two-handed unboxing or product use, show two hands from the same creator, with left and right hands in natural positions.
- Each visible hand has natural scale, visible wrist connection, five aligned fingers, readable joints, and a comfortable product-use angle.
- Keep the lens view open and readable during scene changes. Product, package, phone, table surface, or creator remains the continuity anchor.
- Scene changes are completed by camera movement, focus shift, match cut, or direct quick cut after the current action completes.
- If a hand places a product or gift, cut after the item is fully placed and the product/gift remains visible as the continuity anchor.
- Preferred scene changes: `direct quick cut to gift lineup`, `direct quick cut to coupon page`, `direct quick cut to product use close-up`.

### Recommended Transition Library / 推荐转场库

Pick one of these by scene type:

- `福利堆山`: product close-up -> direct quick cut to full gift table -> pull-back to show all items.
- `赠品逐个出现`: hand places gift A -> item settles -> direct quick cut to gift B placement -> final pull-back to bundle.
- `券/价格机制`: product close-up -> rack focus to independent price card beside product -> push-in to final price.
- `手机商品卡`: product on table -> direct quick cut to stable front-facing phone on stand -> direct quick cut back to product and gift table.
- `达人反应`: creator meme reaction -> direct quick cut to product + offer card -> push-in to coupon/gift.
- `使用证明`: table flat lay -> match cut on product shape -> usage close-up -> direct quick cut back to final CTA bundle.
- `直播间风格`: host holds product -> direct quick cut to product-card phone on stand -> direct quick cut to live-room desk with product and CTA sticker.

## Execution Stability / 执行稳定性维度

Use these rules for every campaign output.

- Product consistency: product appearance stays consistent with user assets, including shape, color, packaging, logo placement, material, texture, size, SKU, label, and gift packaging.
- Product image lock: when the user provides product images, use the image as the visual anchor for every product appearance. Preserve the product's packaging text, logo, brand mark, label layout, color blocks, pattern, cap/nozzle/box shape, material, size ratio, visible dimensions, count, SKU, and front/back orientation.
- Product text lock: visible text printed on product packaging follows the user image. Keep brand name, product name, capacity, count, flavor/color/version name, and key package slogans in the same approximate position and hierarchy as the image.
- Product scale lock: product size stays consistent across beats relative to hand, face, table, phone, shelf, bag, box, and gift items. Multi-pack quantities and package dimensions match the user image or page evidence.
- Product angle lock: when using a user-provided product image as reference, keep the same recognizable front label, logo placement, package silhouette, and dominant color in close-ups, table shots, unboxing, usage shots, and CTA bundle shots.
- Gift evidence consistency: visible gifts must match user-provided images, screenshots, or page copy. Match gift type, package shape, color, bottle/tube/jar form, and capacity when visible. If evidence is unclear, use placeholders such as `[确认赠品名称]`, `赠品礼`, or `加赠小样` instead of inventing gift names or packaging.
- Product connection: product, package, phone page, gift, or coupon remains connected to every beat.
- One main action per beat: each shot has one clear physical action such as place product, open package, show coupon, lay out gift, apply product, press button, or hold product to camera.
- Product lineup meaning: do not start with a meaningless static row of products. Product lineups must reveal a benefit, such as gifts added one by one, `买X到手Y` comparison, bundle reveal, full-table gift proof, or final CTA bundle.
- Physical plausibility: separated objects move one by one or with visible support such as hand, box, tray, table, shelf, bag, rack, or packaging insert.
- Scale: product size stays believable relative to hand, face, table, phone, package, shelf, bag, or room.
- Action completion: cut after the spoken line finishes, product is placed, gift is revealed, coupon page is visible, or result is shown.
- Safe layout: place price stickers, offer tags, and CTA cards in clean foreground safe zones near product, coupon, gift, or CTA action.
- Text safe area: every price sticker, offer tag, mechanism card, and CTA sticker stays fully inside the visible frame with clear margins. No cropped Chinese characters, half-cut numbers, off-screen text, or text over the creator's eyes/mouth/product logo.
- Number context: every visible number stays paired with a readable unit or benefit, such as `ml`, `元`, `抽`, `件`, `满减`, `到手`, `叠减`, or `券`.
- Long offer splitting: split long mechanisms into multiple short stickers across beats instead of one oversized line.
- Default text layer: use short stickers, price tags, offer tags, and CTA tags.
- Transition safety: scene changes use camera movement, focus shift, match cut, or direct quick cut after a completed action. Hands stay in the product interaction area and the lens view stays open.
- Hand action safety: hands complete product, phone, package, gift, or usage actions inside the shot; the next scene begins with a readable product, gift, phone, or price-card composition.

For offer facts waiting for confirmation, use placeholders:

- Good placeholders: `[填写真实到手价]`, `[确认赠品名称]`, `[0.01元权益如属实展示]`
- Use verified price, stock, gift, countdown, and exclusive rules from user input or visible page evidence.
- For gift-heavy videos, prefer `main product -> first verified gift -> more verified gifts -> full table reveal`. Each gift is placed with a visible hand action and remains on the table after placement.

## Input Handling / 输入处理

Parse all evidence before writing. Prioritize:

1. User's current instruction and fixed script.
2. Product title, SKU, link, page copy, price, coupon, discount, gift, live-room rule.
3. Uploaded product image, offer screenshot, product card, live-room screenshot, reference video.
4. Category inference for uncovered fields.

Extract these fields when available:

- Product: name, category, SKU, size, quantity, variants, visual appearance.
- Offer: original price, final price, discount, coupon, full reduction, gift, bundle, 0.01 yuan action, live-room-exclusive benefit.
- Proof: one compact product proof that supports the promotion, such as texture, use result, before/after, capacity, taste, fit, or real handling.
- CTA: click lower link, enter live room, claim coupon, click yellow cart, click product card, place order, comment keyword.
- Risk: whether price, stock, gift, countdown, and 0.01 yuan claims are verified or placeholders.

## Creative Routes / 创意路由

Choose one primary route. Keep each video focused on one primary saving mechanism. The order of judgment is: Hook route -> Benefit route -> CTA route -> platform -> scene -> category -> creator persona.

Creative route options / 创意路由文字版：

- 大促到手价爆点 / Final-price shock：best for clear final price or discount. Hook examples: `{campaign_occasion}到手才¥X`, `这波比平时省¥X`.
- 叠券攻略 / Coupon-stack guide：best for multiple coupons, full reduction, and platform subsidy. Hook example: `先领这张券，再点商品卡`.
- 赠品加赠 / Gift-with-purchase：best for strong gift, bundle, sample pack, or extra SKU. Hook examples: `买正装送这一整套`, `赠品比正装还香`.
- 0.01元引导 / 0.01 yuan action：best for trial, reservation, lock benefit, or low-price link. Hook examples: `0.01元先锁权益`, `1分钱拍这个链接`.
- 直播间切片 / Live-room clip：best for host, urgency, product card, or yellow cart. Hook example: `进直播间先领券再拍`.
- 省钱测评 / Value proof review：best when a price hook needs quick trust proof. Hook example: `这个价，我先看赠品和规格`.
- 囤货清单 / Stock-up list：best for daily goods, snacks, household, or multi-SKU. Hook example: `{campaign_occasion}这几样适合一次囤`.

## Benefit-Point Routing / 利益点路由

Pick the strongest verified benefit point first. Each video normally uses one primary promotion benefit and one supporting product proof. Product proof stays compact, no longer than one short beat, and explains why this offer is worth taking during the current campaign. If price/gift/coupon already carries the ad, skip product proof and use the time for promotion impact.

Benefit route options / 利益点路由文字版：

- 到手价 / final price：use when final price, single-item discount, or official direct reduction is provided. Creative logic: product appears immediately; price sticker appears in 0-3s; proof beat supports the price.
- 官方立减 / one-item discount：use when the platform emphasizes simple rules, one-price purchase, or clear direct reduction. Creative logic: say `不用凑单` or `直接这个价`; show one clear price path.
- 国补/平台补/店补 / subsidy stack：use for appliances, 3C, phones, tablets, smart watches, and high-ticket goods. Creative logic: show final price and one subsidy path first; function demo appears as short value proof.
- 叠券/满减 / coupon stack：use with multiple coupons, 88VIP, platform coupon, category coupon, or store coupon. Creative logic: show a simple path: claim coupon -> product card -> order; keep phone page stable.
- 赠品/加赠 / gift：use when gift is visually strong, limited, bundled, or useful. Creative logic: lay out full bundle; show gift size, quantity, and value.
- 0.01元/1分钱 / low-price action：use with trial, member gift, reservation, lock benefit, or low-price link. Creative logic: use verified evidence; keep action path very short.
- 直播间权益 / live-room benefit：use with live-exclusive price, yellow cart, product card, host explanation, or limited gift. Creative logic: host/product appears in first shot; stable product-card display; CTA enters live room.
- 囤货/组合装 / stock-up bundle：use for daily goods, food, paper, cleaning, baby, pet, or family use. Creative logic: show quantity, storage, unit value, and repeat-use reason.
- 实测/对比 / proof-led value：use when a low price needs trust reinforcement. Creative logic: one visible test such as texture, before/after, capacity, taste, fit, cleaning, or speed; return to price or gift after proof.
- 夏季/换季/出游 / seasonal need：use with sunscreen, apparel, travel, outdoor, drinks, or seasonal care. Creative logic: tie purchase timing to immediate use: `{campaign_occasion}刚好把夏天要用的买齐`.

## Platform Routing / 平台路由

When the platform is unspecified, default to Douyin-style conversion video. When the user names a platform, adapt the same offer to the platform behavior.

Platform route options / 平台路由文字版：

- 抖音 / Douyin：top material style is store live-room clip, product-card conversion, short-video traffic, search follow-up, and consumption coupon subsidy. Execution: hook within 1-2s; product visible before 3s; show product-card or coupon path; give one direct CTA.
- 快手 / Kuaishou：top material style is live preview, highlight spread, clip-linked product, price-value ratio, and real experience. Execution: grounded practical tone; emphasize guarantee, real use, and plain savings language.
- 淘宝天猫 / Taobao Tmall：top material style is official direct reduction, brand hero item, new launch, member benefit, and AI shopping calculation. Execution: use brand/product trust as support; foreground `现在买就是这个价` and member benefit.
- 京东 / JD：top material style is government subsidy, appliances/home, 3C digital, onsite/offsite linkage, and service fulfillment. Execution: highlight subsidy, parameters, service, delivery, installation, trade-in, and warranty as deal support.
- 小红书 / Xiaohongshu：top material style is scenario seeding, list, review, trend outfit, and travel guide. Execution: softer CTA; explain the scene value, then mention where to claim the offer.

## Scenario Routing / 场景路由

Select scenes that make the product need feel immediate. The scene supports the benefit point and keeps the promotion information visible.

Scenario route options / 场景路由文字版：

- 直播间桌面 / live-room desk：best for live benefit, product card, gift, and low-price action. Visual proof: host holds product, stable product-card display, gift lineup.
- 居家囤货 / home stock-up：best for daily goods, food, cleaning, baby, and pet. Visual proof: pantry, bathroom, laundry, kitchen, or storage cabinet.
- 夏季出游 / summer travel：best for sunscreen, apparel, drinks, outdoor gear, and bags. Visual proof: travel bag, sunscreen reapply, poolside, camping table, or commute.
- 通勤办公 / commute-office：best for beauty, skincare, snacks, portable electronics, and apparel. Visual proof: desk, restroom mirror, handbag, quick touch-up, or compact use.
- 家电升级 / appliance upgrade：best for appliances, phones, tablets, and smart devices. Visual proof: old-vs-new, one function demo, capacity, speed, or energy saving.
- 礼赠/套装 / gifting set：best for beauty sets, food gift boxes, health, and premium goods. Visual proof: unboxing, package texture, recipient scenario, or gift lineup.
- 真实测评 / real review：best for products needing quick trust. Visual proof: one test, one comparison, one visible result.
- 宠物/亲子 / pet-parenting：best for pet, baby, and family safety products. Visual proof: real reaction, parent handling, gentle close-up, or usage steps.

## Category Top List / 品类 Top 素材

Use category rules to choose product proof and creator persona after selecting the primary benefit point.

Category route options / 品类路由文字版：

- 美妆护肤/彩妆/防晒：top material routes are final price plus gift set, visible proof, live-room sample/member gift, and brand hero item. Show texture, hand/face test, before/after, gift lineup, or travel pouch as one compact support beat.
- 家电/家居/3C数码：top material routes are subsidy-stacked final price, upgrade pain point, trade-in, and product-card/search conversion. Show final price, subsidy path, one key function, service, or warranty cue as deal support.
- 食品饮料/零食/粮油：top material routes are stock-up list, health cue, taste reaction, bundle, and family pack. Show pack count, ingredient/health cue, eating/drinking reaction, or storage as value proof.
- 服饰/内衣/鞋靴/运动户外：top material routes are summer travel, commute outfit, try-on effect, trend list, and function benefit. Show full-body try-on, walking turn, fabric movement, or color/style switch as quick proof.
- 洗护清洁/家清/纸品日用：top material routes are cleaning effect, stock-up value, and family scene. Show before/after, wipe path, foam, quantity, or unit-use reason.
- 母婴/个护/营养保健：top material routes are ingredient/safety cue, professional trust, large-pack stock-up, and usage steps. Show ingredient/safety cue, usage steps, family buyer, or repeat-use need.
- 宠物食品/宠物用品：top material routes are pet reaction, ingredient/palatability, stock-up value, and multi-pet solution. Show pet reaction, kibble/texture, bowl/cleaning result, or daily cost.

## Phone And UI Display Rules / 手机页与商品卡规则

Phone, coupon, order, benefit, product, and CTA cards are conversion bridges. Real product, gift, package, creator reaction, or usage result remains the main proof.

- Default visual priority: real product, gift pile, unboxing, bundle table, creator reaction, and concise independent mechanism cards.
- Use screenshot and product-page information as evidence. Extract the verified facts into short stickers such as `买50到手80`, `最高叠减380`, `先领券再拍`, or `点商品卡`.
- Use phone/card shots as one short bridge when product card, coupon card, order card, yellow-cart action, or live-room benefit is useful for the action path.
- Independent mechanism cards are flat 2D offer cards or physical tabletop cards placed in a clean safe zone beside the product, with margin, shadow, and stable hierarchy.
- User-provided screenshot assets can appear as independent flat evidence cards: full-screen insert card, picture-in-picture card, tabletop printed card, or floating rectangular reference card with border and shadow. The card is a separate visual layer beside the product.
- Prefer stable phone display: phone held vertically beside the face, placed on a table, or mounted on a simple stand.
- Phone front screen faces the camera when card content appears. The visible display surface is a flat luminous screen inside the phone bezel, showing one simplified platform-neutral product card, coupon card, order card, benefit card, or CTA card with short readable offer text.
- When the phone back is visible, it appears as a normal solid phone back with camera lenses and matte/glossy body material. The phone back stays as a continuous physical back panel with camera module, logo area, and natural material reflection.
- Fingers point to the screen edge or a sticker arrow while the screen remains visible; the face, product, and key card stay readable.
- Small card text can remain soft and secondary. Use effect stickers such as `先领券`, `0.01会员礼`, `单支低至¥128`, `点小黄车` for key information.
- Keep phone/card shots short, then return to the real product in the next beat.
- Phone/card beats flow into a real product, gift, package, use result, or creator product desk shot in the next beat.

Phone/card composition methods:

- `Evidence-to-card`: screenshot fact -> short offer sticker -> product/gift shot. Example: screenshot says 满1400赠礼, video shows product + verified gifts + sticker `满额赠礼`.
- `Screenshot-card`: user-provided screenshot asset -> independent flat reference card with border/shadow -> direct quick cut to real product or gift table. The screenshot card stays outside any phone frame.
- `Phone-bridge`: real product on table -> direct quick cut to stable front-facing phone on stand showing a simplified recreated product card/coupon page -> direct quick cut back to product/gift table.
- `Mechanism-card`: product close-up -> rack focus to independent price/coupon card in a blank safe zone -> push-in to product and CTA.
- `Live-room-card`: host/product desk -> stable phone product card beside product -> product stays visible while CTA sticker appears.

## Reference Screenshot Handling / 参考截图使用规则

Treat user screenshots as evidence sources for product, price, coupon, gift, and UI facts. User-provided screenshots may appear directly as independent screenshot cards. Screenshot facts can also be converted into real product/gift shots plus concise offer stickers or independent mechanism cards.

- Use a single-source layout per beat: one product scene, one gift layout, one independent screenshot card, one phone-bridge shot, or one independent mechanism card beside the product.
- When multiple screenshots are provided, select the screenshot that matches the current `script_task`, then present it as one independent screenshot card or translate its key fact into one concise offer sticker.
- Show one front-facing phone screen at a time when the action path needs product card, coupon page, order page, or live-room benefit proof. The phone screen sits inside one visible phone bezel and presents one clear page.
- Transition from phone/card evidence back to physical product with one of these paths: `phone on stand -> direct quick cut to product table`, `phone beside product -> rack focus to product`, `coupon card -> pull-back to gift table`, `product card -> direct quick cut to CTA bundle`.
- Screenshot presentation methods: `independent screenshot card`, `picture-in-picture screenshot card`, `tabletop printed screenshot card`, or `full-screen evidence insert`. Use border, shadow, and clear safe margins so the screenshot reads as an intentional evidence layer.
- Phone screen presentation methods: `simplified product card`, `simplified coupon page`, `simplified order page`, or `simplified live-room benefit page`. Use short reconstructed text and stable front-facing phone composition.
- Screenshot-derived mechanisms render as clean offer cards in fixed safe zones with margin, shadow, and readable hierarchy. The physical product/gift scene remains the primary layer.
- Use one screenshot-derived fact per beat. Use the other beats for product, gift, coupon card, final price, countdown, or CTA visuals.
- Keep raw screenshot text as secondary evidence. Extract key verified facts into short stickers: final price, coupon, subsidy, gift, deadline, or CTA.
- Keep one primary visual hierarchy in each frame: product/gift first for price/proof/gift beats; phone first only for explicit coupon/action-path UI requests.
- When showing a screenshot-derived card, keep the surrounding real scene simple: table, hand, product, or creator desk.

## Subtitle, Lip Sync, and Repeat Control / 字幕口型同步与重复控制

Default text layer uses short offer stickers. `subtitle_mode` is `off`. `sticker_text` is a short offer tag. Requested subtitle deliverables bind subtitles to the exact spoken line.

- With default settings, output `voiceover_zh` and `sticker_text`.
- For requested subtitles, set `subtitle_text` equal to the exact `voiceover_zh` of the same beat. One spoken line maps to one subtitle line.
- Subtitle timing follows the spoken line: appears when the line starts, stays through the line, clears before the next spoken line.
- When a visible creator speaks to camera, mouth movement matches the current `voiceover_zh` from start to finish of that line.
- Product B-roll uses off-screen voiceover with product, coupon, gift, or usage action visible. Creator-speaking beats show the creator mouth matching the current line.
- Build a `script_task_map` before the timeline: beat 1 hook, beat 2 brightest offer/mechanism, beat 3 product proof, beat 4 campaign time + offer path, beat 5 CTA.
- The brightest offer appears once as the main offer. The final CTA may reference it with new action wording, but the middle beats move to product proof and purchase path.
- Keep `voiceover_zh`, `sticker_text`, and requested `subtitle_text` semantically aligned with the same script task.

## Creator Persona Diversity / 达人画像多样性

When creator persona is unspecified, infer a persona from the product category, buyer role, use scenario, and promotion route. Rotate creator persona across different products in a batch evaluation.

默认根据品类、购买决策者、真实使用场景和优惠路径选择更贴合转化的达人身份，并在 `video_generation_prompt` 开头明确写出达人外观和状态。多商品批量输出时主动轮换达人画像。

Creator persona must fit the product. Build it from visible variables, not a generic "young woman" or "host".

达人形象必须和产品适配。生成前先组合这些变量，让人物、场景和商品像同一个真实消费场景：

- `年龄段`: 18-24 学生/初入职场，25-35 通勤/精致生活，30-45 家庭采购/高客单决策，40-55 成熟自用/家庭囤货。
- `性别呈现/关系`: 女性、男性、中性实用派、情侣、母女、亲子、夫妻、室友、同事、宠物主人、直播间主播。
- `脸型与气质`: 圆脸亲和、鹅蛋脸精致、方脸干练、长脸成熟、清冷、甜美、元气、专业、居家、户外、克制高级。
- `发型发色`: 黑色低马尾、自然披发、短发、丸子头、空气刘海、深棕卷发、利落背头、运动帽发型；发色和产品调性、场景光线协调。
- `妆容`: 素颜感、通勤淡妆、精致约会妆、干练职场妆、户外防晒妆、成熟气质妆；高客单美妆和香氛用更精致但不过度的妆容。
- `配饰`: 耳钉、项链、手表、眼镜、发夹、丝巾、帽子、托特包、运动包、母婴包、宠物牵引绳；配饰服务场景，不抢商品。
- `服装`: 白衬衫、针织衫、居家服、通勤西装、运动外套、连衣裙、围裙、户外防晒衣、学生卫衣、直播间简洁上衣；颜色和商品包装/节日节点协调。
- `场景`: 浴室洗手台、梳妆台、厨房、客厅、洗衣区、办公室、宿舍、户外露营、旅行箱、宠物角、母婴房、直播间桌面、品牌柜台。
- `表达状态`: 朋友式爆料、deal hunter 快节奏、冷静实测、居家囤货、礼赠推荐、直播间急促提醒、meme 震惊反应、专业测评。

Batch persona rotation:

- For multiple products or multiple case outputs, rotate at least four dimensions: age bracket, scene, styling, role, creator timing, hook type, benefit order, or CTA route.
- Keep one persona consistent within a single video: same face, hair, makeup, outfit, accessories, and role across all creator-facing beats.
- Match persona to price tier: low-price stock-up uses practical buyer; high-ticket beauty/fragrance uses refined self-use or gifting creator; household goods use family decision-maker; 3C/appliance uses upgrade buyer or practical reviewer; pet uses pet owner; baby products use parent/caregiver.

## Creator Persona Routing / 达人画像路由

Pick creator persona after category, benefit point, platform, and scene. Write the creator as a visible role with age bracket, styling, posture, setting, and delivery style.

Creator persona route options / 达人画像路由文字版：

- 美妆护肤、防晒、彩妆 + 到手价/赠品：use a 25-35-year-old practical beauty buyer or commuter woman. Visual and performance: clean makeup, bathroom vanity or office restroom, calm review, one hand/face texture proof.
- 高客单护肤、礼盒、香水 + 赠品/礼赠：use a 30-40-year-old refined self-use or gifting creator. Visual and performance: restrained outfit, gift table, slow unboxing, premium but friendly tone, gift value visible.
- 防晒、服饰、箱包、墨镜 + 夏季出游：use a 20-35-year-old outdoor/travel user. Visual and performance: travel bag, poolside/camping/commute scene, energetic clear demonstration, offer sticker visible.
- 女装、鞋靴、配饰 + 上身效果：use a 20-35-year-old try-on creator or commute outfit creator. Visual and performance: full-body mirror, walking turn, fabric movement, outfit switch through visible cut, price/gift shown as overlay.
- 男装、运动户外、数码配件：use a 25-40-year-old practical reviewer or neutral outdoor user. Visual and performance: hands-on demo, straightforward tone, function proof as support for deal value.
- 家电、家居、家清 + 国补/囤货/功能证明：use a 30-45-year-old household decision-maker, renter, or couple. Visual and performance: kitchen/living room/laundry scene, practical demo, old-vs-new or before/after proof tied to subsidy or final price.
- 3C数码、手机、智能设备 + 国补/升级：use a 25-40-year-old digital reviewer or upgrade buyer. Visual and performance: desk setup, device close-up, one speed/capacity/camera/battery proof, concise discount explanation.
- 食品饮料、零食、粮油 + 囤货/健康化：use a family buyer, office sharer, or dorm stock-up user. Visual and performance: kitchen/office/dorm table, pack count display, tasting reaction, storage scene, unit-value sticker.
- 母婴、个护、营养保健：use a 30-40-year-old parent, family caregiver, or professional practical creator. Visual and performance: gentle handling, ingredient/safety cue, simple use step, stock-up or coupon benefit visible.
- 宠物食品、宠物用品：use a pet owner or multi-pet family user. Visual and performance: pet reaction, bowl/toy/litter scene, owner hands guide product, natural home light, daily-cost or stock-up benefit visible.
- B2B、课程、软件、AI工具：use a founder, operator, designer, or workplace project owner. Visual and performance: desk/computer scene, screen as secondary bridge, output/result proof, professional tone, offer path visible.
- 0.01元、先领券、直播间福利：use a fast deal guide, store-live host, or platform benefit finder. Visual and performance: live-room desk, product in hand, stable phone front-screen display, fast clear command.
- 小红书种草/攻略：use a friend-like experience sharer, checklist creator, commuter, or travel user. Visual and performance: softer expression, lifestyle scene, reason-first explanation, light CTA with offer sticker.
- 快手质价比/真实体验：use a grounded practical buyer, family user, or industry-belt seller. Visual and performance: plain language, real environment, direct value proof, strong trust cue.

Creator prompt formula:

```text
达人画像：[年龄段] + [性别呈现/关系] + [脸型与气质] + [发型发色] + [妆容] + [配饰] + [服装] + [生活角色] + [场景] + [姿态/动作] + [表达状态]。
```

Examples:

- `达人画像：30岁左右通勤女性，鹅蛋脸清爽气质，黑色低马尾，通勤淡妆，小耳钉，白衬衫，办公室洗手台自然光，手边放产品和券卡，冷静实测语气。`
- `达人画像：35岁左右家庭采购者，圆脸亲和，深棕短发，轻淡妆，无夸张配饰，米色针织上衣，厨房台面自然光，边收纳边讲囤货理由。`
- `达人画像：28岁户外出游女性，元气健康气质，高马尾，户外防晒妆，墨镜和帆布包，浅色防晒衣，旅行包场景，动作轻快，先展示套组再补涂。`
- `达人画像：32岁数码测评男性，方脸干练，短发，黑框眼镜，深色T恤，桌面设备场景，手持产品做一个证明动作，表达简洁。`

Vary persona across these dimensions when possible:

- apparent age bracket: early 20s, late 20s, 30s, 40s, mature family buyer
- gender presentation options: female, male, couple, parent, neutral hands-focused reviewer
- face and temperament: friendly round face, refined oval face, practical square face, mature calm face, sweet, cool, energetic, professional, homey, premium
- hair style and hair color: low ponytail, loose hair, short hair, bun, bangs, brown waves, clean short cut, cap hairstyle
- makeup: no-makeup look, commute light makeup, refined date makeup, professional workplace makeup, outdoor sunscreen makeup, mature premium makeup
- accessories: earrings, necklace, watch, glasses, hair clip, scarf, tote bag, sports bag, parent bag, pet leash
- clothing: shirt, knit top, homewear, suit jacket, sports jacket, dress, apron, sun-protection jacket, hoodie, live-room clean top
- lifestyle role: commuter, office worker, gift buyer, parent, home organizer, beauty enthusiast, practical value shopper, outdoor/travel user, appliance upgrader
- scene texture: bathroom vanity, office desk, bedroom closet, kitchen counter, living-room sofa, balcony laundry area, poolside/travel bag, live-room desk
- performance style: calm expert review, fast deal-hunter, friend-to-friend recommendation, practical household demo, gift-selection comparison, first-use reaction

Category persona guidance:

- Beauty, skincare, fragrance, lip, haircare: choose between beauty enthusiast, office commuter, gift buyer, or mature self-care user based on product price and use case; match age and style to price tier and use scene.
- Hair tools: use a morning-routine commuter, date-night prep creator, salon-at-home reviewer, or long-hair practical tester; show hair state before and after.
- Home appliances and household goods: use a household decision-maker, parent, couple, renter, or practical value shopper; product proof comes from real home use and practical demonstration.
- Apparel, swimwear, accessories: match wearer and buying context; for swimwear, use beach/pool/travel prep or try-on mirror scene with respectful, product-focused framing.
- Gifts and premium sets: use gift giver, couple, friend-to-friend recommendation, or office gifting scenario; emphasize presentation, unboxing, and who it is for.
- Daily stock-up items: use value shopper, family buyer, or dorm/office user; emphasize quantity, unit price, storage, and repeat-use reason.

Batch rule:

- In a multi-case evaluation, adjacent outputs use varied persona, scene, and opening style when products allow.
- Several beauty/personal-care cases rotate buyer motivations: self-use, gifting, commute touch-up, travel pouch, mature care, quick repair.
- Keep persona descriptions concise and executable. Good: `30岁左右通勤女性，美妆但不夸张，办公室洗手台自然光`.

## Default Structure / 默认结构

Default video: 30s. Default ratio is 9:16 vertical. Style is seasonal/campaign commerce UGC with Chinese speech or host voiceover, short stickers and price tags as selective on-screen emphasis. Default voice rhythm is medium-fast and compact. The lines follow a script structure, not a repeated benefit list.

Before writing the timeline:

1. Identify the primary benefit point: final price, direct reduction, subsidy, coupon, gift, 0.01 yuan action, live-room benefit, stock-up bundle, or seasonal need.
2. Identify the platform: Douyin, Kuaishou, Taobao/Tmall, JD, Xiaohongshu, or generic ecommerce.
3. Identify one optional category proof type as support: texture, function, try-on, capacity, taste, cleaning, pet reaction, family use, etc. Skip it when it weakens campaign urgency.
4. Identify one action path: claim coupon, click product card, enter live room, click yellow cart, place order, search, save, or consult.
5. Identify creator persona route: buyer role, age bracket, scene, styling, posture, and delivery style. If creator appears, choose a clear creator timing pattern: creator + product/benefit at 0-2s, creator + product/benefit at 2-5s, creator throughout the video, or creator for one proof/reaction beat.
6. Keep the final video focused on one primary promotion benefit point, visible mechanism/gift reveal, two compact product proof or scenario points, and one clear purchase path.

```text

0-3s: Hook。商品和大促氛围必须入镜；用福利奇观、表情包反应、从天而降福利、券卡堆叠、开箱溢出、0.01权益、倒计时抢跑等抓人。
3-7s: 最亮利益点。只讲一个最强优惠：到手价、优惠前后价、券补机制、买赠、赠品量、0.01动作、直播间权益或现货速发。
7-11s: 机制/赠品展开。把最强利益点可视化为赠品逐个摆开、券卡叠加、到手量对比、机制卡或价格卡。
11-15s: 产品证明1。用一个品类相关证明动作说明为什么值得买。
15-19s: 产品证明2或使用场景。补充一个不同的产品事实、使用场景、容量/规格/质地/口味/参数/效果方向。
19-23s: 活动时间 + 优惠路径。说清截止时间、领券/链接/商品卡/直播间/预约/下单路径。
23-27s: 限时/信任/库存/节点提醒。用活动期、限量赠品、现货速发、官方权益或用户提供的真实证据增强行动理由。
27-30s: 单 CTA。产品、赠品或机制卡仍在画面中，给一个明确购买动作。
```

Each beat includes:

- scene/action
- product relation
- one short `voiceover_zh` with the current script task
- one short `sticker_text`, such as `{campaign_occasion}到手¥X`, `先领券`, `加赠X`, `0.01元锁`, `点击下方链接`, `进直播间`
- use short stickers, price tags, offer tags, and CTA tags as the default on-screen text; requested subtitle deliverables add exact `subtitle_text`

Voice and sticker examples:

```text
0-2s voiceover_zh: `先别划，这桌福利是认真的吗？` sticker_text: `{campaign_occasion}大促`
2-5s voiceover_zh: `真正狠的是，到手只要¥X。` sticker_text: `到手¥X`
5-8s voiceover_zh: `它这个[功能/规格/质地/口味]，日常用刚好。` sticker_text: `[产品证明短词]`
8-12s voiceover_zh: `活动到X号，先领券再点商品卡。` sticker_text: `X号截止`
12-15s voiceover_zh: `看准这套，快点击下方链接抢购吧！` sticker_text: `下方链接`
```

## Live-Room Optimization / 直播间优化

For live-room tasks, make the video feel like a believable high-conversion clip:

- Host faces camera with product in hand in the first 3 seconds.
- Show product card, coupon, yellow-cart action, or live-room benefit through a platform-neutral product card, coupon card, mechanism card, CTA card, or a phone on stand showing one simplified neutral card.
- Use short command lines that match the user's actual path: `快点击下方链接抢购吧！`, `快来直播间抢购吧！`, `来直播间更划算，手慢无！`, `点击下方链接领券购买`, `来直播间领优惠券，到手更划算`, `先领券再拍`, `0.01元先锁`, `赠品限量发`.
- Return from card/phone bridge to real product, gifts, package, usage result, or creator desk within the next beat.
- Keep urgency concrete: limited gift, limited coupon, activity period, or live-room-exclusive action. Use placeholders for claims waiting for confirmation.

## Skill Rules To Preserve / 必须沉淀执行的规则

- Default first judgment: `省钱锚点` before style. Identify regular/original price, campaign final price, saved amount, discount percentage, direct reduction, coupon, subsidy, gift, 0.01 yuan action, live-room benefit, or stock-up value.
- One video normally has one primary saving mechanism. Keep secondary benefits as visual support.
- The 30s timeline follows eight script tasks: hook, brightest offer, mechanism/gift reveal, product proof 1, product proof 2/use scenario, activity time + offer path, urgency/trust reminder, CTA.
- Product function appears as two compact proof or scenario moments that supports the deal value. Product proof should be product-specific and should not become long product education.
- Product and strongest benefit point appear in the first 0-2 seconds.
- Creator can appear together with product, gifts, and mechanism cards in the first 0-2s or 2-5s. Gift pile, coupon mechanism, flat lay, and bundle reveal are not forced to be no-creator shots.
- The first 5 seconds contain a strong hook plus one brightest offer/mechanism.
- When evidence exists, the first hook states or shows `平时/优惠前¥X -> {campaign_occasion}到手¥Y -> 省¥Z`.
- Spoken delivery defaults to medium-fast, short, clear, conversion-focused lines.
- Voiceover pace is medium-fast, clear, and steady, with short pauses between beats.
- Every beat has a new script task. Do not turn every beat into the same price/coupon/gift explanation.
- The 5-8 second beat shows one product-specific proof: effect, function, specification, taste, capacity, use scenario, before-after, try-on, parameter, or real use.
- Phone/product-card/coupon information uses stable platform-neutral card display; key information appears through short stickers, arrows, and price tags.
- Screenshot references are evidence sources. User-provided screenshots appear as independent screenshot cards, picture-in-picture evidence cards, tabletop printed cards, or full-screen evidence inserts. Phone screens show one simplified neutral product card, coupon card, order card, benefit card, or CTA card as an action-path bridge.
- Real-scene transitions use positive transition methods: direct quick cut, push-in, pull-back, pan, tilt, rack focus, match cut on product shape, or cut from table flat lay to usage close-up.
- Hands appear for meaningful product/phone/package/gift/usage actions inside a shot with natural body context. Each hand action operates one clear object. Multi-product scenes use one-by-one placement, pre-arranged bundle reveal, pan across a stable lineup, creator pointing to an arranged bundle, or split table zones. Scene changes are handled by camera movement, focus shift, match cut, or direct quick cut, with the lens view open and readable.
- Price, gift, stock, countdown, live-exclusive price, lowest-price claim, and 0.01 yuan benefit use user-provided facts or visible evidence.
- Short stickers are selective foreground emphasis layers. Select 4-5 sticker moments for the 30s video: Hook, brightest offer, mechanism/gift, campaign time/path, and CTA. Place stickers in clean safe zones with clear margins, as a foreground layer beside the product or in upper/lower empty space. Keep product body, logo, package text, hands, creator face, and gift pile readable. Product-proof or emotion beats can use clean visuals when product action and voiceover carry the information. Requested subtitle deliverables add exact `subtitle_text`.
- Each selected sticker uses wording different from the voiceover in the same beat. Beats without selected stickers can keep clean product visuals.
- Each beat has a unique script task. Repeated benefits are expressed only in the final CTA with new action wording when needed.
- Requested subtitle deliverables set each `subtitle_text` equal to the exact `voiceover_zh` for that beat and follow the same timing.
- Creator-speaking beats use the current `voiceover_zh` as the on-camera spoken line. Product B-roll uses off-screen voiceover.
- Voiceover uses varied sentence patterns and concrete benefits/product facts/action words; generic excitement words appear at most once per script.
- Prompt language uses concrete Seedance/Seedream-readable fields: `time`, `script_task`, `shot_action`, `camera`, `voiceover_zh`, `sticker_text`, `visual_audio_match`.
- Promotion video includes two compact visible product proof or scenario beats matched to the category: skincare texture/effect direction, daily-goods count/storage/use-frequency, food taste/portion/freshness, appliance function/before-after, fashion try-on/fabric, 3C parameter/scenario, or another product-specific proof.
- For multi-output or batch generation, vary at least four of these dimensions across outputs: hook type, creator presence timing, persona, scene, camera rhythm, first benefit point, gift reveal method, CTA path, and tone. Give each case a distinct 0-8s structure.

## Claim Safety / 宣称边界

Treat these as factual claims that need user evidence:

- price, original price, final price, discount percentage
- gift name, gift quantity, gift value
- stock limit, countdown, deadline, today-exclusive wording
- `0.01元`, `1分钱`, `0元试用`, live-room exclusive price
- sales ranking, bestseller, official subsidy, lowest price

For central claims awaiting evidence:

- Ask one short clarification.
- Or write a placeholder in the prompt, e.g. `[填写真实到手价]`, `[确认赠品名称]`, `[0.01元权益如属实展示]`.

## Output Behavior / 输出交付

Default deliverable is one compact bilingual Chinese+English `video_generation_prompt`, directly usable for Seedance 2.0 / Seedream / Pippit / 小云雀. The video content defaults to Chinese voiceover and Chinese short stickers; English appears as execution guidance for timing, camera, action, and consistency. Visible model-facing prompt uses positive execution wording: describe what to show, keep, face, place, point to, return to, and complete.

For script requests, output timestamped script. For multiple-concept requests, give 2-3 options, each with one primary saving mechanism.

Default response shape:

```text
video_generation_prompt:
生成一条 30秒 9:16 竖版 {campaign_occasion} 大促 UGC 带货短视频。

结构：Hook -> 最亮利益点 -> 机制/赠品展开 -> 产品证明1 -> 产品证明2/使用场景 -> 活动时间+优惠路径 -> 限时/信任提醒 -> CTA。

0-3s: Hook，商品和大促氛围同框。
3-7s: 最亮利益点，只讲一个最强价格/机制/券补/赠品/到手量。
7-11s: 机制或赠品展开，用赠品摆开、券卡叠加、到手量对比、机制卡或价格卡可视化。
11-15s: 产品证明1，一句话展示功能、功效、规格、质地、口味、容量或参数。
15-19s: 产品证明2或使用场景，和上一段不同。
19-23s: 活动时间与优惠路径，说明截止时间、领券、链接、商品卡、直播间、预约或下单路径。
23-27s: 限时、信任、库存或节点提醒，使用用户提供的真实证据或占位。
27-30s: 单一CTA，匹配用户购买路径，例如“快点击下方链接抢购吧！”“快来直播间抢购吧！”“点击下方链接领券购买”“来直播间领优惠券，到手更划算”。

全片使用真实商品桌、达人桌、礼品桌、居家/品牌柜台等场景；购买路径用平台中性商品卡、优惠卡、机制卡、CTA卡或手机里的单张简化中性卡表达。
```

## QA Checklist / 质检

Before final output, check:

- Campaign or promotion context is obvious in the first 3 seconds.
- The first 3 seconds use a mandatory campaign visual hook: gift pile, 0.01 verified benefit, final quantity, coupon stack, countdown, live-room exclusive, occasion-specific gift scene, or full-table benefit reveal.
- At least two beats show explicit promotion visuals, not just product education or beauty B-roll.
- The main savings anchor is concrete and focused in the first 2 seconds.
- When evidence exists, the prompt states or shows regular/original price, campaign final price, and saved amount.
- The first 5 seconds contain both savings comparison or final price and discount/coupon path.
- Buy-gift intensity is concrete: buy what, get what, gift quantity/value, and whether it is limited-time or limited-quantity.
- Gift names, colors, bottle/tube/jar forms, and capacities match user images or page evidence; unclear gifts are placeholders, not invented products.
- Limited-time benefit is concrete: deadline, countdown, activity window, or limited gift/coupon.
- Spoken lines are short, medium-fast, clear, and discount-dense.
- Voiceover has brief pauses between beats and keeps a medium-fast, clear, steady delivery.
- Final prompt uses bilingual Chinese+English execution guidance. Default `voiceover_zh` and `sticker_text` stay Chinese. Bilingual creative requests may add `voiceover_en` or `sticker_text_en`.
- Every beat gives a promotion benefit or claim action.
- Product appears early and returns after any screen or coupon page.
- Price, gift, stock, countdown, and 0.01 yuan claims are evidence-backed or placeholders.
- There is one clear action path.
- Default output sets `subtitle_mode: off` and selects 4-5 short sticker moments for the whole video. Subtitle requests add exact `subtitle_text`.
- Each beat's `voiceover_zh` differs from the previous beat.
- Selected sticker text uses different wording from the voiceover in the same beat.
- Voiceover uses concrete price, coupon, gift, time, ranking, and action words with varied wording.
- Voice, picture, and any selected sticker refer to the same current offer, product, or action.
- Product appearance, scale, and package/gift details stay consistent with user assets.
- Product lineups are meaningful: they show gift accumulation, bundle comparison, benefit reveal, or CTA bundle, not a static decorative row.
- Scene changes use the recommended positive transition library: direct quick cut after action completion, push-in, pull-back, pan, tilt, rack focus, match cut, phone-bridge, mechanism-card reveal, or product-to-gift table reveal.
- Each beat has one main physical action, and cuts happen after action completion or spoken-line completion.
- Effect text, price stickers, offer stickers, and CTA stickers are short, stable, platform-safe, and placed in foreground safe zones.
- Stickers and mechanism cards are fully visible inside the frame, with clean margins and clear layering beside the face/product/logo/package text/hands/gift pile.
- The final CTA is direct and suitable for live-commerce conversion.
- The final CTA uses exactly one action based on product context: `点击下方链接购买`, `进入直播间购买`, `点商品卡`, `点小黄车`, `先领券`, or `下单`.
- Platform logic is reflected: Douyin conversion/card, Kuaishou trust/value, Taobao/Tmall brand/member benefit, JD subsidy/service, Xiaohongshu scene/review.
- Category proof is visible and specific, with real product use or measurable detail.
- Phone/commerce-card information uses one stable method: screenshot-card, evidence-to-card, phone-bridge, mechanism-card, product-card, coupon-card, benefit-card, or CTA-card. User-provided screenshots are shown as independent evidence cards; phone screens show one simplified platform-neutral card inside the phone bezel. Phone back appears as a normal physical back panel with camera lenses and material reflection.
- Screenshot-derived cards sit in fixed safe zones with clear margins, border/shadow, and a readable rectangular card shape beside the product or as a full-screen evidence insert.
- Real-scene transitions use the positive transition set named in the prompt. Hands appear inside product/phone/package/gift/usage actions, while scene changes use camera movement, focus shift, match cut, or direct quick cut.
