## UGC Visual Style / UGC 视觉风格

## Table of Contents

- [UGC Visual Style / UGC 视觉风格](#ugc-visual-style-ugc-视觉风格)
- [Character Performance, Lip Sync, And Optional Text Rules / 人物表演、口型和可选文字规则](#character-performance-lip-sync-and-optional-text-rules-人物表演-口型和可选文字规则)
  - [Optional Subtitle Rule / 可选字幕规则](#optional-subtitle-rule-可选字幕规则)
- [Product Consistency Rules / 商品一致性规则](#product-consistency-rules-商品一致性规则)
- [Scale And Real-World Size Rules / 尺寸比例规则](#scale-and-real-world-size-rules-尺寸比例规则)
- [Physical Plausibility Rules / 全品类物理可执行性规则](#physical-plausibility-rules-全品类物理可执行性规则)
- [Continuity And Transition Rules / 镜头连续性规则](#continuity-and-transition-rules-镜头连续性规则)
- [Music And Sound Rules / 音乐和声音规则](#music-and-sound-rules-音乐和声音规则)
- [Speech Timing / 口播时长控制](#speech-timing-口播时长控制)


Default visual style:

- vertical 9:16 / 竖屏 9:16
- Apple native camera style / 苹果原相机拍摄风格
- natural indoor or everyday light / 自然光或日常室内光
- real home, street, store, desk, kitchen, bathroom, car, office, or use-case environment / 真实家中、街头、门店、桌面、厨房、浴室、车内、办公室或使用场景
- close-up and medium-close framing / 近景和中近景
- slight handheld movement / 轻微手持晃动
- product appears early and stays in use / 产品早出现，并保持在使用中
- not studio-shot unless requested / 非用户要求，不要棚拍
- not polished brand commercial / 不要像精修品牌广告

Creator energy:

- friend recommendation / 朋友安利: warm, casual, useful / 温暖、自然、有用
- real review / 真实测评: objective, hands-on, "I test it for you" / 客观、动手试、“我替你测”
- value recommendation / 性价比推荐: practical, direct, price/value aware / 实用、直接、强调价值
- daily-life UGC / 日常 UGC: relaxed, lightly messy, real routine / 放松、略有生活杂感、真实日常
- expert/authority / 专业型: concise, confident, still product-in-use / 简洁、自信，但产品仍要在使用中
- store visit / 探店型: curious, present, sensory, place-specific / 好奇、在场、感官化、有地点细节

## Finished-Video Stability Rules / 成片稳定性规则

Use these rules whenever the output will be used by SD2.0 or another video generator.

成片稳定性优先级高于花哨剪辑。内部 `seedance_generation_package` 要让模型知道每一镜保持什么、何时切换、如何承接。

- Use one stable 4-shot structure for 15 seconds: `0-3s / 3-7s / 7-12s / 12-15s`.
- Each shot has one main scene, one camera state, one main action, one product proof, and one spoken line.
- Each shot holds for at least 3 seconds before switching.
- Product appears in the first 3 seconds and remains tied to action in every later beat.
- Use the same creator, same product, same visual world, and same platform texture across all beats.
- The camera follows hand, face, product, or phone screen movement instead of jumping to unrelated scenes.
- Cuts happen after completed action, completed spoken line, product placement, expression change, result reveal, or music beat.
- Multi-item and multi-SKU displays use visible set-up and reset: full set shown -> one item handled -> item placed down -> next item handled.
- The internal package should preserve this compact global stability rule and expand it into per-shot fields:

```text
全片使用稳定4镜结构，每镜至少3秒，每镜一个主要动作和一句短口播；商品、主体1、场景光线和手部动作保持连续，镜头在动作完成或口播结束后自然切换。
```

## Creator Authenticity Rules / 达人真实性规则

The creator should feel like a believable buyer, user, reviewer, parent, store visitor, player, or recommender.

达人真实性来自“角色与商品关系”，不是颜值堆叠。

- Define `主体1` before the timeline with role, age band, hair/outfit, scene, product relationship, and speaking tone.
- Use the confirmed `creator_portrait_image` as the protagonist reference.
- Keep `主体1` face, age, hairstyle, outfit logic, body proportion, and role stable across all shots.
- Give `主体1` category-matched behavior: skincare creator applies texture, parent handles child/family product, office worker uses commute item, store visitor shows package and environment, gamer points to event/reward page.
- Show natural expression changes: curiosity in hook, focus during proof, small satisfaction at result, confident CTA.
- Keep creator speech conversational and short, like a real recommendation.
- If the user asks to adjust the creator, update portrait, persona wording, script tone, and video prompt together.
- Final prompt should include:

```text
将主体1定义为同一位[年龄段/达人角色]，[发型/穿搭/气质]，[与商品关系]；全片保持主体1脸部、发型、穿搭风格、身体比例和角色身份一致，主体1按真实生活方式完成试用、反应和口播。
```

## Character Performance, Lip Sync, And Optional Text Rules / 人物表演、口型和可选文字规则

When a person appears on camera, write explicit performance direction instead of leaving the face static.

只要有人物出镜，就要写清楚人物表演，不要让角色固定一个表情。

- Define the on-camera protagonist before the shot beats. Use `主体1` plus 2 to 4 stable visible traits, such as approximate age range, hair style, outfit, role/temperament, and relation to the product. Reuse the same protagonist wording across all shots / 分镜前先定义出镜主角。使用“主体1”加 2 到 4 个稳定可见特征，例如大致年龄段、发型、穿搭、角色/气质、与商品的关系。全片复用同一套人物写法。
- If there is a person reference, keep the reference person's visible identity cues and do not replace them with a generic influencer look. If no person reference exists, choose a normal product-appropriate UGC persona and avoid exaggerated facial beauty descriptors / 有真人参考时，保持参考人物的可见身份线索，不替换成模板化网红形象。没有真人参考时，选择普通且符合商品的人物设定，避免夸张脸部颜值描述。
- Keep age, hair, outfit, body scale, and creator role consistent unless a visible wardrobe transition or role change is part of the user request / 除非用户要求可见换装或角色变化，否则年龄感、发型、穿搭、身体比例和达人角色保持一致。
- Use expressive but natural facial changes across beats: curious hook, small smile when recommending, focused look during demo, surprised or satisfied reaction at the result, confident CTA / 每个节拍要有自然表情变化：开头好奇、推荐时轻微微笑、演示时专注、看到结果时惊喜或满意、CTA 时自信
- The creator should visibly speak when there is voiceover or spoken dialogue: lips move naturally in sync with each spoken line / 有口播或对白时，人物嘴巴必须自然动起来，并和台词同步
- Do not generate voice-only talking-head content where the mouth stays closed or frozen / 不要生成只有声音、嘴巴不动或表情冻结的口播人物
- Do not generate a full subtitle layer by default / 默认不生成完整字幕层
- In-video text may use stable short text for key information: flower text, sticker text, price tags, pop-up words, bullet-screen style keywords, label cards, arrow callouts, or stamp-style CTA / 画内文字可以对关键信息使用稳定短文字：花字、贴纸字、价格牌、弹出词、弹幕式关键词、标签卡、箭头标注或印章式 CTA
- Keep in-video text focused on keywords, numbers, offers, selling points, result words, and CTA / 画面文字只突出关键词、数字、优惠、卖点、结果词和 CTA
- If in-video effect text is used, keep it short and readable: 2 to 8 Chinese characters or 1 to 4 English words per effect element / 画内特效字保持短且可读：每个特效元素 2 到 8 个汉字或 1 到 4 个英文词
- Use creative text effects sparingly. Default to one effect text element per beat; use two only when the beat must show both a price/offer and a CTA or result keyword / 花字和特效文字少量使用。默认每个节拍一个特效字元素；只有同一节拍必须同时展示价格/优惠和 CTA 或结果词时才用两个
- Leave clean visual space between effect text elements and the product/person; the video should not feel text-heavy / 特效字和商品/人物之间保留干净画面空间，视频不要显得满屏文字
- Place optional text inside platform-safe areas so it is not covered by app UI, captions, usernames, product cards, comment buttons, like/share buttons, live badges, or bottom navigation / 可选画面文字放在平台安全区内，避开 App UI、标题文案、用户名、商品卡、评论按钮、点赞分享按钮、直播标识和底部导航
- Default 9:16 safe layout: keep key effect text in the upper-middle or beside the product/face, and keep the right edge clear for vertical interaction buttons / 默认 9:16 安全布局：关键花字放在上中部或商品/人脸旁，右侧边缘留给点赞评论分享按钮
- Platform placement: Douyin keep text away from right-side buttons and bottom product/caption area; Kuaishou keep text above bottom action/caption area; Xiaohongshu keep text away from bottom title/comment area and avoid covering note-style product details; WeChat keep text clear of bottom title/action UI / 平台位置：抖音避开右侧按钮和底部商品卡/标题区；快手文字高于底部操作/标题区；小红书避开底部标题评论区，并避免遮住笔记式商品细节；微信视频号避开底部标题和操作区
- When a product card, deal card, order page, or app UI is visible, place effect text close to the highlighted price or CTA without covering it / 当商品卡、团购卡、订单页或 App UI 出现时，特效字贴近价格或 CTA 但不遮挡
- Use in-video text only for short keyword overlays, price tags, offer tags, result words, or CTA labels / 画面内文字只用于短关键词、价格牌、优惠标签、结果词或 CTA 标签
- Important numbers, discounts, product names, and CTAs should be spoken by the creator and optionally shown as very short keyword overlays / 重要数字、优惠、产品名和 CTA 由达人口播，画面里最多用极短关键词辅助

### Optional Subtitle Rule / 可选字幕规则

Subtitles are optional, not default.

字幕是可选项，不是默认项。

- If the user explicitly requests subtitles or provides subtitle copy, use one source of truth for speech and subtitles / 如果用户明确要求字幕或提供字幕文案，口播和字幕使用同一份文本
- When subtitles are requested, keep the subtitle wording identical to the corresponding spoken line / 用户要求字幕时，字幕文案与对应口播保持一致
- Unless the user asks for another language, requested subtitles and effect text should be Chinese; do not add bilingual subtitles by default / 除非用户要求其他语言，已请求的字幕和特效字使用中文；默认不添加双语字幕
- Keep `spoken_line` short enough for the beat duration before generating the video prompt / 生成视频 prompt 前先把 `spoken_line` 压到适合该时间段的长度
- If full subtitles are handled by the platform caption layer, keep in-video text to short key information only / 如果完整字幕由平台字幕层承载，视频画面只用短花字/贴纸字/价格牌等突出关键信息
- If subtitles are requested, do a final line-by-line check: each spoken line, subtitle line, and beat order should be identical / 如果用户要求字幕，最后逐行检查：口播、字幕和时间顺序完全一致

## Product Consistency Rules / 商品一致性规则

Preserve the user's product identity across the whole video.

全片必须保持用户提供商品的一致性。

- If the user provides product images, keep the product's shape, color, packaging, logo placement, material, texture, and key visual details consistent across all shots / 如果用户提供商品图，需保持商品形状、颜色、包装、logo 位置、材质、纹理和关键视觉细节一致
- Do not invent a different product, color, size, label, package, accessory, or variant unless the user asks for it / 不要擅自生成不同商品、颜色、尺寸、标签、包装、配件或款式
- If the user provides multiple variants, colors, flavors, sizes, or styles, show each relevant variant clearly and keep them visually distinct / 如果用户提供多个款式、颜色、口味、尺寸或风格，要清楚展示每个相关款式，并保持差异可见
- When multiple variants are shown, describe the order and placement: for example, "three colors lined up on the same table, camera pans from black to pink to silver" / 展示多款式时，要写清楚顺序和摆放，例如“三个颜色并排放在同一桌面，镜头从黑色扫到粉色再到银色”
- For any multi-SKU, multi-color, multi-flavor, multi-style, multi-size, before/after, or state-change display, never let the product visually morph or instantly switch without a transition / 任何多 SKU、多颜色、多口味、多款式、多尺码、前后对比或状态变化展示，都不能让产品无转场直接变形或瞬间换款
- Use this stable switch pattern for all categories: show the full set first -> pick up or point to one item -> use/show that item -> place it down in a stable position -> hold a clear frame -> cut to the next item already supported -> continue / 所有品类使用稳定切换模式：先集合展示 -> 拿起或指向一个商品 -> 使用或展示 -> 放回稳定位置 -> 保持清晰画面 -> 切到下一件已获得支撑的商品 -> 继续
- Use clear transition states: product placed down then next product picked up, tabletop reset, rack/shelf/box layout cutaway, mirror reset, fitting-room reset, packaging close-up, creator points to the next item, or camera pans across a clearly arranged lineup / 使用清晰转场状态：放下当前商品再拿起下一个、桌面重置、衣架/货架/盒内排列插入、镜前重置、试衣间重置、包装特写、达人指向下一个、镜头扫过清晰排列的整组商品
- Keep the lens-facing foreground clear. Hands stay at the product-use plane and retain visible wrist/forearm connection while the cut occurs after the action reaches a stable end state / 镜头前景保持清晰；手停留在商品使用平面，并保持手腕和前臂连接可见，切换发生在动作到达稳定结束状态之后
- Category examples: shoes need foot-off-camera or hand-held shoe reset; bags need tabletop lineup or creator holds the next bag; accessories/jewelry need macro reset before wearing; cosmetics/skincare need shade/package lineup before application; snacks/drinks need flavor lineup before tasting; electronics/appliances need device placed down before switching models; toys need full-set layout before feature demo; restaurant dishes need serving, picking up, bite, or plate transition / 品类示例：鞋子用脚离镜或手拿鞋重置；包用桌面并排或达人手持下一只包；配饰/珠宝佩戴前先微距重置；美妆/护肤上脸前先展示色号/包装排列；零食/饮品先展示口味排列再试吃；数码/家电先放下设备再切型号；玩具先展示全套再演示功能；餐饮菜品用上菜、夹起、入口或盘子转场
- For clothing and try-on videos, finish the current outfit pose and cut on a clear unobstructed frame; use a mirror reset, fitting-room cut, or rack/bed layout cutaway, then begin the next shot with the next outfit fully worn / 服装试穿视频里，当前穿搭姿态完成后在清晰无遮挡画面切换；使用镜前重置、试衣间切换或衣架/床面展示插入，下一镜从新穿搭已完整穿戴的状态开始
- If showing multiple clothing variants, show the variants off-body first, then try on one by one with a reset between outfits / 多款服装展示时，先离身展示全部款式，再逐套试穿，每套之间有重置切点
- Keep product continuity during handoffs, close-ups, demos, and result shots; the object in hand must remain the same product shown at the start / 拿起、特写、演示、结果镜头中产品要连续，手里的物品必须和开头展示的是同一商品
- If the product has packaging plus actual item, show both only when helpful and make clear which one is packaging and which one is the usable product / 如果有外包装和本体，必要时同时展示，并明确哪个是包装、哪个是可使用产品
- Do not let the model replace the user's product with generic stock-looking items / 不要让模型把用户商品替换成通用库存感物品

## Scale And Real-World Size Rules / 尺寸比例规则

Keep every product at a believable real-world size relative to hands, face, tableware, furniture, phone screens, plates, packaging, and the environment.

所有商品都要相对手、脸、餐具、家具、手机屏幕、盘子、包装和环境保持可信的真实尺寸。

- Use a familiar size anchor in close-ups: hand, fingers, spoon, chopsticks, cup, plate, phone, package, table, shelf, shoe, face, or car/person scale / 特写中使用熟悉参照物：手、手指、勺子、筷子、杯子、盘子、手机、包装、桌面、货架、鞋、脸或车/人比例
- Small foods and loose items stay small: sunflower seeds, nuts, candy pieces, beads, pills, grains, seasoning, jewelry parts, and toy accessories should fit naturally between fingertips, on a spoon, in a small bowl, or inside packaging / 小食物和零散小物保持小尺寸：瓜子、坚果、糖粒、珠子、药片、谷物、调料、珠宝配件和玩具小件，应自然位于指尖、勺子、小碗或包装内
- Large products use wide shots with human/environment scale: cars, furniture, appliances, luggage, strollers, sports gear, and store installations should be shown beside people, doors, rooms, roads, or shelves / 大件商品用带人和环境比例的广角：汽车、家具、家电、行李箱、婴儿车、运动装备和门店装置，应和人、门、房间、道路或货架同框
- Food portions use plates, bowls, trays, cups, skewers, chopsticks, spoons, or hands as scale anchors / 食物分量用盘、碗、托盘、杯、签子、筷子、勺或手作为比例参照
- When showing a package and the item inside, keep the item size compatible with the package size / 展示包装和内容物时，内容物尺寸和包装尺寸保持一致

## Physical Plausibility Rules / 全品类物理可执行性规则

Every product, body movement, hand action, object movement, fabric movement, liquid movement, tool use, food movement, and scene change should be physically possible in the real world.

所有商品、人体动作、手部动作、物体移动、衣物/软物运动、液体运动、工具使用、食物移动和场景变化，都要符合真实世界物理规律。

- Use one main physical interaction per shot: one hand action, one tool action, one object action, one body movement, or one result reveal / 每个镜头只安排一个主要物理互动：一个手部动作、一个工具动作、一个物体动作、一个身体动作或一个结果呈现
- For multiple separated objects, use sequential handling: pick up item A -> place it down or stabilize it -> pick up item B / 多个分离物体使用顺序动作：拿起 A -> 放下或固定 A -> 再拿起 B
- When multiple objects move together, show a real support system: two hands, tray, plate, box, basket, bag, shelf, hanger, rack, cart, tabletop slide, clamp, tongs, chopsticks, spoon, spatula, or packaging insert / 多个物体一起移动时，展示真实支撑系统：双手、托盘、盘子、盒子、篮子、包、货架、衣架、推车、桌面推动、夹具、夹子、筷子、勺子、锅铲或包装内托
- Keep object count realistic in each action: the frame may show many items, while the action manipulates one item, one connected pair, or one supported group / 每个动作中的物体数量保持真实：画面可以展示很多物品，但动作只操作一个物品、一对连接物或一个被支撑的小组
- Heavy or bulky items use two hands, a stable surface, wheels, handles, or a supporting person / 重物或大件使用双手、稳定表面、轮子、把手或辅助人员支撑
- Small loose items use a container, palm, fingertips, tweezers, scoop, spoon, tray, or close-up supported handling / 小而松散的物品使用容器、手掌、指尖、镊子、量勺、勺子、托盘或近景支撑动作
- Flexible or soft items such as clothing, towels, bedding, bags, straps, noodles, cables, and paper bend, fold, hang, drape, swing, or slide naturally under gravity / 衣服、毛巾、床品、包带、面条、线缆、纸张等柔软物体按重力自然弯曲、折叠、下垂、摆动或滑动
- Rigid items such as bottles, boxes, electronics, appliances, shoes, watches, toys, and furniture keep their shape and move as solid objects / 瓶子、盒子、数码产品、家电、鞋、腕表、玩具、家具等硬物保持形状，按整体刚体移动
- Liquids flow downward, fill containers, splash only on impact, and stay inside cups, bottles, bowls, sinks, pans, or surfaces that support them / 液体向下流动，进入容器，只有撞击时飞溅，并由杯子、瓶子、碗、水槽、锅或表面承接
- Powders, creams, gels, foams, and makeup textures spread from contact pressure and stay on the touched surface / 粉末、乳霜、凝胶、泡沫和彩妆质地通过接触压力铺开，并停留在接触表面
- Wearable items follow the body: clothes drape on shoulders/waist, shoes stay on feet, bags hang from hand/shoulder, jewelry stays attached to ear/neck/wrist/finger / 可穿戴物跟随身体：衣服挂在肩腰，鞋在脚上，包挂在手/肩，珠宝固定在耳/颈/腕/手指
- Body motion stays anatomically plausible: hands reach within arm range, the person shifts weight naturally, walking has foot contact with the ground, sitting uses a chair or surface / 人体动作符合结构：手在臂展范围内伸取，身体自然转移重心，走路有脚部接地，坐下有椅子或表面支撑
- Product demos keep cause and effect visible: hand presses, twists, pours, opens, applies, plugs in, scans, or picks up -> product responds -> result appears / 产品演示保持因果可见：手按压、旋转、倒出、打开、涂抹、插入、扫描或拿起 -> 产品响应 -> 结果出现
- For food content, show many pieces on a supported surface, then lift one bite, one piece, or one small supported portion / 食物内容中，很多食材先放在有支撑的表面上，再夹起一口、一片或一小份
- For all categories, prefer "show many, manipulate one" unless a real support object carries the group / 所有品类优先使用“展示很多，操作一个”；只有真实支撑物承载时才移动一组
- Keep scale physically plausible: small objects stay small relative to fingers and containers; large objects stay large relative to people and rooms / 保持物体比例真实：小物相对手指和容器保持小，大物相对人和空间保持大

## Physical And Spatial Accuracy Rules / 物理与空间准确性规则

These rules reduce object drift, spatial jumps, hand errors, and impossible product handling.

- Anchor every product with a real surface or body relationship: hand, table, shelf, package, face, body part, floor, wall, phone, plate, cup, bag, hanger, or store counter.
- Keep the product in the same spatial relationship through connected shots: if it starts in the right hand, close-up should still show the same right-hand handling or a clear reset.
- Use visible support for any group movement: tray, box, basket, bag, rack, cart, two hands, tabletop, shelf, plate, bowl, or container.
- Use `show many, manipulate one`: many products may appear in frame, but the action focuses on one product, one connected pair, or one supported group.
- Keep person and environment scale credible: face, hand, table, phone, door, chair, shelf, room, street, car, or store sign should establish size.
- Use one continuous physical cause-and-effect chain per proof beat:

```text
手部动作 -> 商品接触/启动/打开/涂抹/试穿/点击 -> 可见结果 -> 表情或口播确认
```

- For app, order, game, group-buying, or reward pages, keep screen content on a device or picture-in-picture panel, then return to real product/service in the next beat.
- Final prompt should include:

```text
所有物体和人体动作符合真实物理和空间关系：每镜一个主要物理互动；多个分离物体按顺序拿起、放下或由稳定支撑承载；商品始终有手、桌面、包装、身体、屏幕或场景物体作为比例和位置参照。
```

## Continuity And Transition Rules / 镜头连续性规则

Reduce hard cuts by writing action continuity into the prompt.

通过写清楚动作承接，减少视频生成中的生硬切镜。

- For stable video generation, use 4 connected shots for 15-second content by default / 面向稳定视频生成时，15 秒默认使用 4 个有承接的镜头
- Each shot should last at least 3 seconds before switching; preferred 15s rhythm is `0-3s`, `3-7s`, `7-12s`, `12-15s` / 每个镜头至少保持 3 秒再切换；15 秒优先节奏是 `0-3s`、`3-7s`、`7-12s`、`12-15s`
- Sales videos should have rhythm layers: fast hook, clear product/selling point, stable proof, value confirmation, CTA. Keep speech energetic while leaving visual pauses for action and proof / 带货视频要有节奏层次：快速钩子、清楚商品/卖点、稳定证明、价值确认、CTA。口播有能量，同时给动作和证明留出画面停顿
- Use 5 shots only when the user explicitly asks for faster rhythm or when the content has five clearly different visual actions; in that case every cut still follows a completed action / 只有用户明确要更快节奏，或内容确实有五个清楚不同的视觉动作时才用 5 镜；即便如此，每次切换也要接在动作完成后
- Avoid many isolated micro-shots / 避免大量互不相关的碎镜头
- Each shot should inherit something from the previous shot: same hand position, same product orientation, same surface, same body movement, same gaze direction, same environment, or same speaking rhythm / 每个镜头都应继承上一镜的某个元素：手的位置、产品朝向、桌面、身体动作、视线、环境或说话节奏
- Prefer match-on-action transitions: hand reaches for product -> close-up of hand opening product -> product touches surface/skin/object -> result close-up / 优先用动作匹配转场：伸手拿产品 -> 手部打开产品特写 -> 产品接触表面/皮肤/物体 -> 结果特写
- Bridge real scenes to screenshots or app pages through one visible device: the creator lifts the device from a resting position with wrist and forearm connected -> holds one page at a readable angle -> camera makes one controlled move toward the screen -> next beat returns to product or face / 实景到截图或 App 页面通过一个可见设备桥接：达人从静止位置自然举起设备，手腕和前臂连接可见 -> 以可读角度稳定展示一个页面 -> 镜头做一次受控推进 -> 下一节拍回到商品或人脸
- Keep screenshots and UI pages grounded: show one authoritative page plane per shot on one phone, tablet, laptop, projected board, or single picture-in-picture panel next to the creator/product / 截图和 UI 页面保持有载体：每镜只展示一个权威页面平面，呈现在一台手机、平板、电脑、投影板或单个画中画面板中
- After a screenshot, return to the real product, store, package, reward, or service within the next beat so the video remains connected / 截图之后，下一个节拍回到真实商品、门店、包装、福利或服务，让视频保持连贯
- Use phrases such as `smooth handheld continuation`, `natural in-camera movement`, `match-on-action transition`, `the camera follows the hand`, `same real setting`, and `continuous product handling` / 使用这些提示词来强化连续性
- Avoid abrupt scene jumps, unrelated backgrounds, sudden angle changes, and disconnected product positions / 避免突然换场景、无关背景、突然换角度、产品位置断裂
- Do not describe transitions as "fast cuts" unless the user explicitly wants high-energy editing / 除非用户明确要高能快剪，否则不要写 fast cuts
- Cut or transition only when the picture has changed: a new product action, new expression, new hand movement, new result, new angle with purpose, or new scene detail / 只有画面发生有效变化时才切镜：新的产品动作、新表情、新手部动作、新结果、有目的的新角度或新场景细节
- Do not cut while the frame is static, the creator is holding the same pose, or the product has not changed position / 画面静止、达人姿势没变、产品位置没变时不要切镜
- Match transition rhythm to the content and music: slower for trust-building reviews and Xiaohongshu seeding, tighter for Douyin conversion, grounded and readable for Kuaishou, moderate and trust-led for WeChat / 切换节奏要匹配内容和音乐：测评和小红书种草更稳，抖音转化更紧凑，快手更接地气且易看懂，微信视频号更适中且重可信
- Maintain a harmonious edit rhythm: cuts should land on hand actions, expression changes, result reveals, spoken phrase endings, or music beats / 保持和谐剪辑节奏：切点落在手部动作、表情变化、结果揭示、口播短句结束或音乐节拍上
- Transition checklist before every cut: the current spoken line is complete, the action is complete, the product position is stable, the next shot has a new visual purpose, and the first frame of the next shot clearly continues or resets the action / 每次切换前检查：当前口播说完、动作完成、产品位置稳定、下一镜有新的视觉目的、下一镜首帧能清楚承接或重置动作

The video should feel like one person naturally filming a recommendation, test, or visit, not a stitched commercial montage.

视频应像一个人自然拍摄推荐、测评或探店，而不是拼接感很强的商业混剪。

## Lighting And Exposure Rules / 光影与曝光规则

Lighting must be written as physical scene information and compiled into every shot sent to the video tool.

光影必须写成可执行的物理信息，并编译到传给视频工具的每个镜头中。

Each shot specifies:

- key light source: window, ceiling ambient, vanity light, desk lamp, store light, outdoor daylight
- key light direction: front-left, front-right, side, back-side, overhead
- softness: curtain-filtered soft light, cloudy soft light, broad ambient light, controlled direct sunlight
- color temperature and white balance
- fill level and background brightness
- face exposure and product exposure
- product highlight behavior
- continuity with the previous shot

Rules:

- A connected scene keeps the same primary light source, direction, shadow direction, color temperature and background brightness.
- Face and product remain readable in one stable exposure range.
- Product color follows the source image under neutral white balance.
- Reflective products use broad soft highlights and readable edges.
- Matte products use gentle side light to reveal surface texture.
- Transparent containers use side or back-side light while the front label remains readable.
- Food uses soft side light to reveal texture and moisture with natural color.
- Phone and app screens use controlled surrounding brightness so the screen remains legible.
- Exposure changes happen through a visible scene change or camera reset.

Convert abstract wording into physical wording:

- `高级光影` -> `左前方窗户柔光作为主光，右侧低强度环境补光，面部和商品保持同一曝光，背景低半档`
- `氛围感` -> state the practical light, color temperature, background brightness and product highlight
- `电影感` -> state contrast, light direction, lens feel, depth of field and camera movement

## Camera, Framing And Motion Rules / 构图、机位与运镜规则

Each shot uses one defined camera state and at most one primary movement.

每个镜头使用一个明确镜头状态和最多一个主要运镜。

Each shot specifies:

- shot size: wide, medium, waist-up, chest-up, close-up, macro
- angle: eye-level, slight high angle, tabletop top-down, 30-degree product angle, low product hero angle
- camera height relative to face, chest, table or product
- lens feel: phone wide, natural main-camera, portrait-like medium focal length, macro detail
- composition and subject/product position
- focus target and depth of field
- stabilization mode
- movement type
- movement start composition
- movement end composition
- movement speed, distance and duration
- stable hold before or after movement

Rules:

- Camera movement follows one purpose: reveal product, follow hand, move from face to product, reveal result or land on CTA.
- Movement has a visible start and end. Example: `从达人胸部中景开始，镜头在0.8秒内缓慢推近约15厘米，结束于商品和手部近景，稳定停留1秒`.
- Product identity remains readable during motion.
- Focus changes once at most in a shot and names both focus targets.
- Camera height, horizon and screen direction stay continuous inside the same scene.
- A close-up follows an establishing shot or a visible hand-follow move that shows where the product is.
- Proof shots hold until action and result are readable.
- Connected shots inherit hand position, product orientation, gaze direction, scene and light, or use a clear reset composition.

Convert abstract wording into executable wording:

- `丝滑运镜` -> movement type + start + end + speed + distance + hold
- `快速切换` -> exact cut point after action or spoken line completion
- `多角度展示` -> list the exact shot order and purpose for each angle
- `高级镜头` -> shot size + angle + lens feel + focus + motion purpose

## Music And Sound Rules / 音乐和声音规则

Music must support the product, person, platform, and content type.

音乐必须和商品、人物形象、平台和内容类型匹配。

- Choose music mood by product and creator: upbeat for impulse buys, soft lifestyle for Xiaohongshu seeding, practical warm rhythm for Kuaishou, energetic trend sound for Douyin, warm trust-led music for WeChat, clean minimal music for reviews, sensory music for store visits / 根据商品和人物选音乐：冲动消费用轻快，小红书种草用柔和生活方式，快手用实用温暖节奏，抖音用有平台感的热歌/热梗音色，微信视频号用温暖可信音乐，测评用干净弱音乐，探店用有感官氛围的音乐
- The music should not overpower speech; dialogue and product sounds stay clear / 音乐不能压过口播，台词和产品声音要清楚
- When the user asks for current popular songs or trending sounds, verify the latest platform trend data before naming specific songs / 如果用户要求当前热门歌曲或热门音频，必须先确认最新平台趋势，再写具体歌名
- If current trend data is unavailable, describe the music direction instead of inventing song names: mood, genre, tempo/BPM, beat strength, and platform fit / 如果无法确认实时趋势，不要编歌名，改写音乐方向：情绪、风格、速度/BPM、鼓点强弱、适配平台
- Use platform-native music choices: Douyin/Kuaishou/Xiaohongshu hot sounds, trending BGM, or legally usable commercial music matching the content / 优先选择平台原生音乐：抖音/快手/小红书热歌、热门 BGM，或可商用且匹配内容的音乐
- Align cuts to music beats only when there is visual change; do not cut on every beat if the image is static / 只有画面有变化时才跟音乐节拍切，不要画面没变化也每拍硬切
- If the output is a prompt for a video model, include music as a direction such as `upbeat Douyin-style trending pop BGM, low volume under clear speech` instead of relying on a specific copyrighted track / 如果输出给视频模型，用音乐方向描述，例如 `upbeat Douyin-style trending pop BGM, low volume under clear speech`，不要依赖特定版权歌曲

## Audio-Visual Synchronization Rules / 视听同步规则

Use these rules for lip sync, narration, BGM, sound effects, and editing rhythm.

- Each shot uses one short `spoken_line`, usually around 2 seconds of speech.
- After each spoken line, reserve visual time for action completion, reaction, or product placement.
- When `主体1` speaks on camera, mouth movement, facial expression, and slight head movement synchronize with the spoken line.
- When voiceover is used off-camera, show matching hand action, product close-up, screen tap, or result proof during the line.
- BGM stays lower than speech and matches platform, product, creator persona, and content type.
- Sound effects are used only for product appearance, action completion, price/offer pop-up, result reveal, or CTA; avoid continuous stacked effects.
- Cuts can land on music beats only when there is meaningful visual change.
- Final prompt should include:

```text
每个镜头一句短 spoken_line，主体1口播时嘴型、表情和轻微头部动作自然同步；BGM 音量低于口播，音效只在产品出现、动作完成、优惠弹出、结果呈现或 CTA 时轻量出现。
```

## Speech Timing / 口播时长控制

For 15-second effect-first commerce videos:

- each beat should carry one spoken idea / 每个节拍只承载一个口播信息
- For stable video generation, use one spoken line per shot, not continuous dense narration / 面向稳定视频生成时，每个镜头只说一句，不连续密集旁白
- Leave a small natural pause after each spoken line so the visual action can finish / 每句口播后留一个自然停顿，让画面动作完成
- product name can appear on screen instead of being repeated in speech / 产品名可放屏幕文字，不必反复口播
- move specs, variants, pack size, discounts, and detailed ingredients into visual text when speech is dense / 规格、版本、包装、折扣、成分等可放画面文字
- Chinese lines should be conversational and short, usually 6 to 12 Chinese characters per shot in stable mode / 中文台词要短、口语化，稳定模式下每镜通常 6 到 12 个汉字
- When the user explicitly requests English or another language, keep that language's spoken lines short enough for the beat; English stable mode is around 3 to 6 words per shot / 只有用户明确要求英文或其他语言时，才使用对应语言台词；英文稳定模式下每镜约 3 到 6 个词
- For a 4-second shot, reserve about 2 seconds for speech and 2 seconds for visual action, reaction, or pause / 4 秒镜头里，约 2 秒给口播，约 2 秒给动作、反应或停顿
- never force a long CTA into the final seconds; shorten the verdict first / 不要把长 CTA 硬塞进结尾，先压缩结论

## Video Rhythm Rules / 视频节奏规则

Use the persuasive rhythm below by default:

```text
0-3s: hook, product visible, reason to watch
3-7s: product returns to main selling point, first proof action
7-12s: visible result, detail, comparison, process, or reaction
12-15s: value confirmation and one CTA
```

Rules:

- 0-3s should create curiosity, urgency, value, result, or problem recognition.
- 3-7s must clearly return to the product and main selling point.
- 7-12s should be the most stable proof section, not a dense montage.
- 12-15s should close with one CTA while product remains visible.
- Keep the whole video layered: fast enough to catch attention, stable enough for proof, calm enough for CTA.
- If using a meme, drama, absurd hook, or price-led opening, reconnect to product by 3-7s.
- If using local service or group-buying, show package/store/process before CTA.
- If using game/IP/event, show reward/game/event proof before CTA.
