## Quality Checklist / 质量检查

Before output, check:

## Final Dimension Checklist / 最终维度检查

Run this section before the visible answer and again before sending a prompt to SD2.5.

### 输入一致性

- Product name, category, appearance, offer, CTA, platform, and visual assets are aligned.
- Exact user-provided price, discount, product name, SKU, date, package count, or CTA text is preserved.
- Conflicting product facts have been resolved or clarified.
- The creator portrait, script, and video prompt refer to the same product.

### 成片稳定性

- 30 seconds uses stable `0-3s / 3-8s / 8-14s / 14-21s / 21-27s / 27-30s` rhythm.
- Each shot has at least 3 seconds.
- Each shot has one main action, one product proof, and one short spoken line.
- Cuts happen after action, speech, expression, product placement, result, or music beat.

### 达人真实性

- `主体1` is specific: role, age band, styling, scene, product relationship, and speaking tone.
- Confirmed `creator_portrait_image` is used as the character reference.
- Face, age, hairstyle, outfit logic, body proportion, and role stay stable.
- Creator behavior matches product category and platform tone.

### 物理与空间准确性

- Every product has hand, table, package, body, screen, store, or environment scale support.
- Multiple separated objects move sequentially or with visible support.
- Body motion, hand reach, wearable placement, liquid, powder, fabric, and rigid objects follow real-world logic.
- Screenshots and app pages are bridged through a visible device or picture-in-picture panel.

### 文字准确性

- In-frame text is short, usually 2-8 Chinese characters per element.
- Exact user-provided numbers and names are unchanged.
- Text sits in platform-safe areas and does not cover face, product, hands, CTA, price, or UI.
- Full subtitles appear only when requested and reuse `spoken_line` exactly.

### 视听同步

- Each beat has one short `spoken_line`.
- On-camera mouth movement matches speech.
- Voiceover aligns with matching hand action, product proof, screen tap, or result.
- BGM stays below speech; sound effects are light and purposeful.

### 视频节奏

- 0-3s creates a reason to watch and shows/introduces the product.
- 3-8s returns to product and main selling point.
- 8-14s presents stable visible proof, result, detail, comparison, or reaction.
- 14-21s adds a second proof, usage context, or reaction.
- 21-27s completes value confirmation with product visible.
- 27-30s closes with one CTA.

### 营销表达

- There is one main selling point.
- The selling point is proven visually, not only spoken.
- Feature wording is translated into human benefit.
- CTA matches platform and conversion goal.
- Strong claims are grounded in user-provided evidence or softened into experience language.

### 多样性

- If multiple variants are generated, at least three dimensions differ: persona, hook, proof action, scene, benefit wording, CTA, camera framing, music, or text style.
- Product facts, offer, and conversion target remain consistent across variants.
- First spoken lines are not repeated.

### 最终检查

- The final `video_generation_prompt` is self-contained.
- The prompt is written in positive SD2.5 execution wording.
- Negative failure words are kept out of the visible generation prompt where possible.
- The prompt includes compact control for consistency, stability, creator, physics, text, sync, rhythm, marketing, and diversity when relevant.

- Is the user's goal treated as conversion or visible proof, not only brand tone? / 是否把目标当作转化或可见证明，而不是只做品牌调性？
- Does the first 3 seconds create a reason to keep watching? / 前 3 秒是否有继续看的理由？
- If the first 3 seconds use price, meme, drama, or visual induction, does 3-6 seconds clearly return to the product and selling point? / 如果前 3 秒用了价格、玩梗、剧情或视觉诱导，3-7 秒是否清楚回到商品和卖点？
- If the user provided a concrete offer, is it placed early as a short hook and then connected to product proof? / 如果用户提供具体优惠，是否已前置为短钩子，并连接到商品证明？
- Is there one primary selling point? / 是否只有一个主卖点？
- Does the product appear early? / 产品是否早出现？
- Is the product shown in use, not just displayed? / 产品是否在使用中，而不是只摆拍？
- Is the proof visible? / 证明是否可见？
- If no suitable person reference was supplied, has `sandbox_generate_image` been used to generate a product-appropriate creator portrait before script writing? / 如果用户没有提供合适真人参考图，是否已在写脚本前调用 `sandbox_generate_image` 生成符合商品的达人画像？
- Was the complete internal high-quality creator portrait prompt passed into `sandbox_generate_image` without exposing the full prompt to the user? / 是否已把完整内部高质量达人图提示词传入 `sandbox_generate_image`，且没有向用户外露完整提示词？
- Has the creator persona been enriched with role, age band, visible styling, scene, product relationship, and speaking tone? / 达人形象是否已细化角色、年龄段、可见造型、场景、商品关系和口播气质？
- Is the active creator portrait shown or referenced as `creator_portrait_image` before video generation? / 视频生成前是否已展示或引用当前 `creator_portrait_image`？
- If the user requested creator portrait adjustments, has the latest portrait feedback been handled before script or video generation? / 如果用户要求调整达人形象，是否已先处理最新画像反馈，再继续脚本或视频生成？
- Does the concise script match the active creator portrait, product category, platform, and CTA? / 简洁脚本是否与当前达人画像、商品品类、平台和 CTA 保持一致？
- Does the 0-3s hook use a clear hook mechanism and connect back to the product by 3-8s? / 0-3 秒是否使用明确钩子机制，并在 3-7 秒回到商品？
- Do 3-8s and 8-14s translate product features into human benefits with visible proof? / 3-7 秒和 7-12 秒是否把商品功能转成人话利益点，并配有可见证明？
- Does the CTA match the platform and conversion goal with only one next action? / CTA 是否匹配平台和转化目标，并且只保留一个下一步动作？
- Are spoken lines short enough for the duration? / 台词是否足够短？
- In stable mode, does each shot contain only one short spoken line with a natural pause? / 稳定模式下，每个镜头是否只有一句短口播并留出自然停顿？
- Does the on-camera creator have varied natural expressions and visible mouth movement when speaking? / 出镜达人是否有自然表情变化，口播时嘴巴是否动？
- Does the default prompt avoid full subtitle generation unless the user requested subtitles or provided subtitle copy? / 默认 prompt 是否避免生成完整字幕，除非用户要求字幕或提供字幕文案？
- If subtitles are requested, do they match spoken lines and stay short, stable, and low-risk for text glitches? / 如果用户要求字幕，字幕是否和口播一致，并保持简短稳定、降低崩坏风险？
- If subtitles are requested, are they Chinese-only unless the user explicitly requested another language? / 如果用户要求字幕，除非用户明确要求其他语言，字幕是否只用中文？
- If subtitles are requested, is every subtitle line aligned with the corresponding spoken line? / 如果用户要求字幕，每一句字幕是否与对应口播一致？
- Are creative text effects used sparingly, normally one per beat and only two when the beat needs both offer and CTA/result? / 花字和特效文字是否少量使用，通常每节拍一个，只有优惠和 CTA/结果必须同时出现时才用两个？
- Are optional text elements placed in platform-safe areas, away from right-side buttons, bottom captions, product cards, deal cards, comments, and live/action UI? / 可选文字元素是否放在平台安全区，避开右侧按钮、底部标题、商品卡、团购卡、评论区和直播/操作 UI？
- Does the product stay visually consistent with the user's provided product images or details? / 商品是否和用户提供的图片或信息保持视觉一致？
- If multiple variants, colors, or styles are provided, are they all shown clearly and distinctly? / 如果用户提供多个款式、颜色或风格，是否都被清楚展示并区分？
- Are all hand actions and object movements physically plausible, with one object or one supported group handled at a time? / 所有手部动作和物体移动是否物理合理，一次只操作一个物体或一个被支撑的小组？
- Are product sizes believable with visible scale anchors, especially small foods, loose items, jewelry parts, accessories, and large products? / 商品尺寸是否有可信比例参照，尤其是小食物、零散小物、珠宝配件、配饰和大件商品？
- Across all categories, do separated items move sequentially or with visible support instead of moving together unsupported? / 所有品类中，分离物体是否按顺序移动或由可见支撑承载，而不是无支撑一起移动？
- Do soft items, rigid items, liquids, powders/creams/gels, wearable items, and body movements follow realistic gravity, contact, support, and body mechanics? / 软物、硬物、液体、粉末/乳霜/凝胶、可穿戴物和人体动作是否符合真实重力、接触、支撑和身体结构？
- Are transitions continuous rather than abrupt? / 镜头是否自然承接而非生硬切换？
- If screenshots, app pages, deal pages, order pages, or reward pages appear, are they bridged through a phone/tablet/laptop/gesture and followed by a return to the real product or service? / 如果出现截图、App 页、团购页、订单页或福利页，是否通过手机/平板/电脑/手势桥接，并回到真实商品或服务？
- Does the whole sales video feel persuasive with rhythm layers, rather than rushed from beginning to end? / 整条带货视频是否有说服节奏层次，而不是从头到尾都很急？
- For video generation, does each shot last at least 3 seconds and use the stable 5-6-shot rhythm when possible? / 面向视频生成时，每个镜头是否至少 3 秒，并尽量使用稳定 5-6 镜节奏？
- Does each cut happen after a completed action, completed spoken line, expression change, product placement, result reveal, or music beat? / 每次切换是否发生在动作完成、口播完成、表情变化、产品放稳、结果出现或音乐节拍处？
- Is the prompt written mainly as positive execution instructions instead of negative prohibitions? / prompt 是否以正向执行指令为主，而不是负向禁止句？
- Does music match the platform, product, creator image, and content type without overpowering speech? / 音乐是否匹配平台、商品、人物形象和内容类型，并且不压过口播？
- Are cuts made only when the visual content changes meaningfully or lands on a purposeful beat? / 是否只在画面有效变化或有意义节拍处切镜？
- If multiple platforms are requested, are the scripts and styles truly platform-specific? / 如果要求多平台，脚本和风格是否真正按平台区分？
- If multiple content types are requested, does each type follow its own output method? / 如果要求多内容类型，每种类型是否按自己的输出方法生成？
- For group-buying videos, are package contents, deal price/value, redemption path, store proof, and CTA clear without dense unreadable text? / 团购视频是否清楚展示套餐内容、团购价/价值、核销路径、门店证明和 CTA，同时避免密集不可读文字？
- For group-buying package items, are many items shown on a supported surface and only one item/action handled at a time? / 团购套餐内容是否在有支撑表面展示，并且一次只操作一个物品或动作？
- Is the CTA natural and aligned with the platform? / CTA 是否自然且符合平台？
- Can the result be pasted into a video model, shooting brief, or creator workflow with minimal rewriting? / 输出是否能少改或不改地给视频模型、拍摄简报或达人执行？
