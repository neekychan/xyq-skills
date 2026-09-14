---
name: ugc-seasonal-promotion-video-30s
description: >
  Use for 618, 99 sale, Double 11, Double 12, Qixi, Lunar New Year sale, back-to-school sale, brand day, member day, category day, live-room specials, flash sale, coupon stack, full reduction, discount, gift, add-on, final price, 0.01-yuan benefit, product card, and campaign-commerce UGC video prompts for Seedance/Pippit/Xiaoyunque. Route here whenever the user explicitly mentions a campaign occasion or promotion node such as 618/双11/99大促/七夕/年货节/品牌日 together with commerce video, 带货视频, 商品视频, 口播脚本, or product images, even if they also request 剧情, 短剧, 富二代, 霸总, 反转, 玩梗, drama, meme, or story-style creative. In that conflict, treat story/drama as the opening hook inside this campaign-promotion skill. Focus on campaign occasion, savings, coupons, gifts, final price, action path, strong visual hooks, product-image consistency, script-to-video preservation, and conversion.
---

# UGC Seasonal Promotion Video 30s

## Goal

Generate campaign-commerce UGC video prompts and scripts for 618, 99, Double 11, Qixi, Lunar New Year sale, brand day, member day, category day, live-room specials, and other ecommerce promotion occasions.

The core output makes users quickly understand:

1. What is being sold.
2. Which campaign occasion this belongs to.
3. How much they save or what they get.
4. Which coupon/gift/final-price mechanism applies.
5. What action to take next.

## Duration Support

- This package generates 30-second campaign promotion videos only.
- 30s uses the expanded 8-beat spine: `Hook -> brightest offer/mechanism -> mechanism/gift reveal -> product proof 1 -> product proof 2/use scenario -> campaign time + offer path -> urgency/trust reminder -> purchase CTA`.
- Do not stretch a 15s script. A 30s script adds new visual information, one extra product-use proof or scenario, and a clearer offer path while keeping promotion value dominant.

## Routing Priority

Use this skill when the request contains an explicit campaign occasion or promotion node plus a commerce/video task.

High-priority routing signals:

- Campaign occasion: `618`, `年中大促`, `99大促`, `双11`, `双十一`, `双12`, `七夕`, `520`, `年货节`, `开学季`, `品牌日`, `会员日`, `超级品牌日`, `好物节`, `购物节`.
- Commerce/video task: `带货视频`, `营销视频`, `商品视频`, `促销视频`, `大促视频`, `直播间视频`, `口播脚本`, `分镜`, `小云雀视频`, `Seedance视频`, product image, product title, price, coupon, gift, product card.

Conflict handling:

- If the user says `618带货视频`, `双11商品视频`, `七夕促销脚本`, or another explicit campaign-commerce task, route to this skill.
- If the same request also includes `剧情`, `短剧`, `富二代`, `霸总`, `反转`, `玩梗`, `drama`, `meme`, or story-like setup, keep this skill and use that story idea as the Hook.
- Route to a pure story-commerce skill only when the user mainly asks for story/plot commerce and gives no explicit campaign occasion, promotion node, coupon, gift, final price, or campaign purchase path.

## Mandatory Reference Loading

Execution Gate: Required Reference Loading. Every run must read this `SKILL.md` first, then load the required reference files below before writing any final script, storyboard, review, or video prompt. Do not produce a final answer from this skill using only the main `SKILL.md`.

### Core Campaign Rules

For every task handled by this skill:

1. Read `/workspace/.skills/ugc-seasonal-promotion-video-30s/references/full-campaign-promotion-rules.md` before deciding the promotion structure.
2. Read `/workspace/.skills/ugc-seasonal-promotion-video-30s/references/product-image-and-script-lock.md` before using product images, product screenshots, fixed scripts, product cards, package photos, or user-supplied copy.

### Final Video Prompt / Seedance Output

If the final answer will include `video_generation_prompt`, Seedance prompt, Pippit/Xiaoyunque video prompt, 视频生成提示词, 分镜提示词, storyboard prompt, or any paste-ready video model prompt:

1. Read `/workspace/.skills/ugc-seasonal-promotion-video-30s/references/seedance-positive-execution.md` before writing the final prompt.

Hard rule: if `video_generation_prompt` appears in the final output, `seedance-positive-execution.md` must have been read in this turn.

### Campaign Occasion Routing

If the user names or implies a campaign occasion, shopping festival, seasonal node, brand/member day, category day, live-room special, or asks to adapt the promotion to a specific event:

1. Read `/workspace/.skills/ugc-seasonal-promotion-video-30s/references/campaign-occasion-routing.md` before choosing campaign wording, motive, visual symbols, and CTA.

### Promotion Hook And Benefit Rhythm

If the task involves visual hooks, first-3-second hook, deal rhythm, gifts, coupons, 0.01-yuan benefits, final price, stock-up quantity, live-room benefit, or multiple creative cases:

1. Read `/workspace/.skills/ugc-seasonal-promotion-video-30s/references/promotion-hook-and-benefit-rhythm.md` before choosing the hook and benefit order.

### Screenshot / Phone / Card UI

If the user provides screenshots, product-page screenshots, order/coupon/product-card images, or asks for phone UI, mechanism cards, screenshot cards, platform cards, product cards, coupon cards, or CTA cards:

1. Read `/workspace/.skills/ugc-seasonal-promotion-video-30s/references/screenshot-phone-ui-rules.md` before describing screenshot, phone, or card presentation.

### Creator Persona

If the output includes a visible creator, host, buyer, character, duo/group, short-drama role, meme reaction, try-on/review/demo role, or multiple persona options:

1. Read `/workspace/.skills/ugc-seasonal-promotion-video-30s/references/creator-persona-routing.md` before defining persona, styling, expression, role fit, and creator timing.

### Review / Critique / Final QA

If the user asks for review, critique, compliance checking, optimization feedback, or revision validation:

1. Read `/workspace/.skills/ugc-seasonal-promotion-video-30s/references/qa-checklist.md` before answering.

Before any final deliverable, silently run the QA checklist logic from `/workspace/.skills/ugc-seasonal-promotion-video-30s/references/qa-checklist.md` when the output is a complete script, storyboard, or video prompt.

Do this loading check silently. Do not expose "read rules", "references read", or similar process notes in the user-facing response or generated video prompt.

Internal reference visibility rule:

- Reading `SKILL.md` and `references/*` is an internal execution step only.
- Reference file names, file paths, section titles, loading status, and checklist status can be used to guide reasoning, but they must stay out of the user-facing answer.
- The final response should contain only the useful deliverable, such as the video prompt, revised script, storyboard, or concise completion note.
- Never start the user-facing answer with a "read files", "loaded references", "executed rules", or path list summary.

## Production Paths

Choose exactly one path:

- `New promo video`: user provides product image, title, page info, price, coupon, gift, link, or campaign context.
- `Script-to-video`: user provides fixed script, voiceover, timestamps, shot list, or says "按照这个脚本", "不要改文案", "照着这段口播生成".
- `Revision`: user asks to modify, replace, shorten, strengthen, reorder, or regenerate script, creator persona, visual hook, product details, gift details, price, campaign occasion, CTA, transition, screenshot handling, phone UI, or storyboard. Apply the user's requested edits, preserve unchanged parts, then output the revised script/video prompt.
- `Reference remix`: user provides screenshots, competitor video, reference style, product page, or top material.

## Core Rules

- Identify `campaign_occasion` first. Default to 618 only when the user does not specify another campaign.
- Set duration to 30s.
- Use this 30s script structure by default: `Hook -> brightest offer/mechanism -> mechanism/gift reveal -> product proof 1 -> product proof 2/use scenario -> campaign time + offer path -> urgency/trust reminder -> purchase CTA`.
- Promotion benefits dominate the video, but do not repeat the same benefit in every beat. Put the brightest price/mechanism/gift point in one main beat, then move on to product proof and action path.
- Product proof is compact. Use two different proof beats, such as texture + use scenario, capacity + storage, taste + sharing, function + before-after, try-on + occasion, or parameter + scenario.
- Use positive Seedance 2.0 execution language: describe what to show, where to place it, how to transition, how the phone/card/screenshot appears, and how the product remains consistent.
- User-provided product images are visual anchors. Preserve product text, logo, package shape, size ratio, color blocks, label layout, visible SKU, count, and gift packaging.
- User-provided scripts are script locks. Preserve line order, meaning, campaign claims, product name, and CTA unless the user asks for rewriting.
- User-provided screenshots may appear as independent screenshot cards, picture-in-picture evidence cards, tabletop printed cards, or full-screen evidence inserts.
- Action-path visuals use platform-neutral product cards, coupon cards, mechanism cards, or a stable phone showing one simplified card. Screenshot assets stay outside phone frames. The video environment stays as a real product table, creator desk, home scene, gift table, brand counter, or simple commerce desk; platform icons and full app surfaces are replaced by neutral cards and stickers.
- When a phone appears, the screen shows one simplified product card, coupon card, order card, or benefit card with short readable offer text. The composition is a real phone/card prop beside the product, then returns to the physical product, gift, package, or creator scene.
- Short stickers are selective foreground emphasis layers. Select 4-5 sticker moments for the 30s video: Hook, brightest offer, mechanism/gift, campaign path, and CTA. Place stickers in clean foreground safe zones with clear margins, above the visual layer, beside the product or in upper/lower empty space. Keep product, hands, face, logo, package text, and gift pile readable.
- CTA voiceover matches the user's platform, link, live-room, coupon, product-card, or shop context. Use natural purchase urgency, such as `快点击下方链接抢购吧！`, `快来直播间抢购吧！`, `来直播间更划算，手慢无！`, `点击下方链接领券购买。`, `来直播间领优惠券，到手更划算。` Adapt these patterns to the user's exact offer and purchase path.
- Product-proof and emotion beats can use a clean visual frame when the product action and voiceover already carry the information.
- Hand/product actions use one clear object per hand action. To show many products or gifts, place items one by one, reveal an already arranged bundle table, pan across a stable lineup, or pull back to the full set after the items have settled.
- Decide whether a visible creator is needed based on the script concept. A visual hook can combine creator + product + gifts + mechanism cards in the same frame. Gift pile, coupon mechanism, tabletop flat lay, package close-up, bundle reveal, and product proof may be product-only or creator-in-frame; choose the version that makes the hook more dramatic and believable.
- If a creator is used in the video, place creator + product/benefit together in the first 0-2s or 2-5s whenever the concept benefits from reaction, oral recommendation, live-room urgency, unboxing, gift reveal, or deal-hunter drama.
- When a visible creator is used, the persona must fit the product and campaign. Specify age, gender/relationship, face temperament, hairstyle and hair color, makeup, accessories, clothing, role, scene, posture/action, and delivery state.
- When a beat includes a visible creator, include `人物呈现`: face/hair/makeup/accessories/clothing/posture/action/expression/scene detail that matches the persona and current script task. Generate expressions dynamically from product category, creator type, buyer motivation, use scenario, role personality, relationship tension, and story beat. Keep the same identity, outfit, hair, and makeup within one video while changing micro-expressions, gaze, posture, and gestures between beats. When a beat is product-only, write `人物呈现：无人物出镜，产品/赠品/机制卡为主体`.
- All visible creators need persona-fit expression variation, including non-story UGC. Examples: refined skincare creator uses restrained surprise, confident self-use, careful texture proof, calm urgency; household stock-up creator uses practical excitement, quantity-checking focus, family-use approval; food creator uses curiosity, tasting delight, sharing excitement; 3C/appliance reviewer uses focused evaluation, upgrade satisfaction, decisive recommendation; gift buyer uses soft anticipation, heart-flutter, warm approval.
- Creator styling and scene also adapt to the primary benefit route and campaign occasion. Live-room traffic uses host-like posture, desk/product-card scene, fast urgent expression, clean top, product in hand. Gift mechanism uses gift-table/vanity/unboxing scene, excited reveal, warmer outfit or refined styling. Discount/direct price uses deal-hunter energy, price card/coupon desk, sharper expression, practical clothing. Stock-up uses home storage/kitchen/bathroom/dorm scene, practical excitement, casual clothes. Festival gifting uses date/gift/table scene, soft anticipation, polished outfit. Brand/member day uses official counter/live desk, confident trust expression, restrained premium styling.
- Story-skin hooks use role-specific emotion design. When the Hook uses 剧情/短剧/富二代/霸总/反转/逆袭/玩梗, define `主角` and `配角` separately. For each visible role, write: role identity, relationship to product, starting attitude, conflict emotion, reversal emotion, product-proof emotion, action-path emotion, ending emotion. Choose emotions according to the actual script and persona instead of reusing a fixed arc. Keep every emotion change tied to the product effect, campaign benefit, or purchase path.
- Voiceover uses role-based script progression. Across 5 beats, each line has a different job: `视觉/口播Hook -> 最亮利益点 -> 产品功效/功能一句证明 -> 活动时间与获取优惠路径 -> 单一购买CTA`. The same price, discount, coupon, or gift wording appears once as the main offer, then only returns in the final CTA with a new action wording if needed.
- Case diversity rule: when generating multiple cases, vary at least four dimensions across outputs: opening hook type, creator presence timing, creator persona, scene, camera rhythm, first benefit point, gift reveal method, CTA path, and tone. Give each case a distinct 0-8s structure.
- Product adaptation rule: choose hook, product-proof sentence, scene, creator role, offer framing, and CTA according to product category. Skincare uses texture/use-result proof; daily goods use quantity/storage/use-frequency proof; food uses taste/portion/freshness proof; appliances use before-after/function proof; fashion uses try-on/occasion proof; 3C uses parameter/use-scenario proof.
- Revision response rule: when the user modifies any part, respond by updating that exact part and regenerating a complete coherent output. Examples: script changes update `中文口播`; persona changes update `达人画像` and every visible `人物呈现`; product image changes update `商品与素材锁定` and every product shot; gift/price/CTA changes update benefit beats and stickers; transition changes update every `镜头` field that depends on it.

## Default Output

Default output is one paste-ready `video_generation_prompt` for Seedance 2.0 / Pippit / Xiaoyunque.

Use this structure unless the user asks for something else:

```text
video_generation_prompt:
时长：30秒，比例：9:16。
任务：生成一条 {campaign_occasion} 大促 UGC 带货短视频。

商品与素材锁定：
[写清产品图片锁定、脚本锁定、截图卡呈现方式]

达人画像：
[根据脚本创意判断是否需要达人出镜；如需要，写年龄段、性别或关系、脸型气质、发型发色、妆容、配饰、服装、生活身份、场景、姿态动作、表达状态，并根据脚本、人设、关系、场景生成动态表情设计；如为剧情/反转/逆袭故事皮，分别写主角与配角的角色身份、起始态度、冲突情绪、反转情绪、产品证明情绪、行动路径情绪、结尾情绪；如不需要，写“本片以产品/赠品/机制卡为主体，无固定达人出镜”]

角色分工：
[如为单人视频，写“单主角：承担推荐、产品证明和CTA”，并根据脚本任务设计表情变化。如为故事皮/多人视频，分别写主角与配角：角色功能、人设性格、关系张力、每段情绪、动作。主角和配角的表情符合各自人设与剧情位置，形成差异化反应]

利益点与节点适配：
[写清主利益点类型和节点：直播间引流/赠品机制/打折直降/领券满减/0.01锁权益/囤货/礼赠/品牌日会员权益等。根据该利益点和节点调整达人表情、服装、背景、道具、动作和节奏]

花字策略：
[30秒选择4-5个花字节点；花字作为前景强调层，放在画面空白安全区，与商品主体、手、脸、logo、包装文字和赠品堆叠区并列排布；产品证明段使用清爽画面承载动作信息]

转场方法：
[从推荐转场库中选择具体转场]

分镜：
0-3s / [中文镜头标题]
- 本镜任务：Hook，可用口播Hook或视觉Hook，必须让商品和大促氛围同时出现
- 人物呈现：[有人物则写妆发服饰动作；无人物则写“无人物出镜，产品/赠品/机制卡为主体”]
- 画面动作：
- 镜头：
- 中文口播：[Hook句，负责抓人，后续用不同句式推进]
- 短花字：[从全片4-5个花字节点中选择；如使用，放在前景安全区，与商品/手/脸并列清晰呈现]
- 声画匹配：

3-7s / [中文镜头标题]
- 本镜任务：说清最亮利益点，只讲一个最强价格、机制、券补、赠品或到手量
- 人物呈现：[有人物则写妆发服饰动作；无人物则写“无人物出镜，产品/赠品/机制卡为主体”]
- 画面动作：
- 镜头：
- 中文口播：[最亮利益点句]
- 短花字：[从全片4-5个花字节点中选择；如使用，放在前景安全区，与商品/手/脸并列清晰呈现]
- 声画匹配：

7-11s / [中文镜头标题]
- 本镜任务：展开机制/赠品/到手组合，让用户看懂多得了什么或怎么领
- 人物呈现：[有人物则写妆发服饰动作；无人物则写“无人物出镜，产品/赠品/机制卡为主体”]
- 画面动作：
- 镜头：
- 中文口播：[机制/赠品展开句，和3-7s不同]
- 短花字：[从全片4-5个花字节点中选择；如使用，放在前景安全区，与商品/手/脸并列清晰呈现]
- 声画匹配：

11-15s / [中文镜头标题]
- 本镜任务：产品证明1，展示一个功能/功效/规格/质地/口味/容量/参数
- 人物呈现：[有人物则写妆发服饰动作；无人物则写“无人物出镜，产品/赠品/机制卡为主体”]
- 画面动作：
- 镜头：
- 中文口播：[产品证明句1，一句话]
- 短花字：[产品动作作为主要信息层；需要强调规格/功效短词时，在边角安全区使用小贴纸]
- 声画匹配：

15-19s / [中文镜头标题]
- 本镜任务：产品证明2或使用场景，和上一段不同
- 人物呈现：[有人物则写妆发服饰动作；无人物则写“无人物出镜，产品/赠品/机制卡为主体”]
- 画面动作：
- 镜头：
- 中文口播：[产品证明句2或使用场景句，一句话]
- 短花字：[产品动作作为主要信息层；需要强调规格/场景短词时，在边角安全区使用小贴纸]
- 声画匹配：

19-23s / [中文镜头标题]
- 本镜任务：说明活动时间、优惠获取方式和购买路径
- 人物呈现：[有人物则写妆发服饰动作；无人物则写“无人物出镜，产品/赠品/机制卡为主体”]
- 画面动作：
- 镜头：
- 中文口播：[活动时间+领券/进直播间/点商品卡/下方链接/下单路径句]
- 短花字：[从全片4-5个花字节点中选择；如使用，放在前景安全区，与商品/手/脸并列清晰呈现]
- 声画匹配：

23-27s / [中文镜头标题]
- 本镜任务：限时/信任/库存/节点提醒，强化现在买的理由
- 人物呈现：[有人物则写妆发服饰动作；无人物则写“无人物出镜，产品/赠品/机制卡为主体”]
- 画面动作：
- 镜头：
- 中文口播：[限时、限量、信任、现货、节点提醒句，需有依据或用占位]
- 短花字：[从全片4-5个花字节点中选择；如使用，放在前景安全区，与商品/手/脸并列清晰呈现]
- 声画匹配：

27-30s / [中文镜头标题]
- 本镜任务：单一CTA收束，回到商品和最强行动
- 人物呈现：[有人物则写妆发服饰动作；无人物则写“无人物出镜，产品/赠品/机制卡为主体”]
- 画面动作：
- 镜头：
- 中文口播：[CTA收束句，根据用户提供的购买路径和优惠类型匹配，例如“快点击下方链接抢购吧！”“快来直播间抢购吧！”“来直播间更划算，手慢无！”“点击下方链接领券购买”“来直播间领优惠券，到手更划算”]
- 短花字：[从全片4-5个花字节点中选择；如使用，放在前景安全区，与商品/手/脸并列清晰呈现]
- 声画匹配：
```

## Upload Package Structure

Agent Buddy upload package should contain:

```text
ugc-seasonal-promotion-video-30s/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── campaign-occasion-routing.md
    ├── creator-persona-routing.md
    ├── full-campaign-promotion-rules.md
    ├── product-image-and-script-lock.md
    ├── promotion-hook-and-benefit-rhythm.md
    ├── qa-checklist.md
    ├── screenshot-phone-ui-rules.md
    └── seedance-positive-execution.md
```
