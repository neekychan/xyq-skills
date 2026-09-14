## Choose The Content Task / 选择内容任务

## Table of Contents

- [Choose The Content Task / 选择内容任务](#choose-the-content-task-选择内容任务)
- [Three Production Scenarios / 三大生产场景](#three-production-scenarios-三大生产场景)
  - [Scenario 1: New Video From Product Content / 场景一：基于产品内容全新制作](#scenario-1-new-video-from-product-content-场景一基于产品内容全新制作)
  - [Scenario 2: Video From A Fixed Script / 场景二：基于明确脚本产出视频](#scenario-2-video-from-a-fixed-script-场景二基于明确脚本产出视频)
  - [Scenario 3: Viral Video Remake / 场景三：基于爆款视频做复刻](#scenario-3-viral-video-remake-场景三基于爆款视频做复刻)


Classify the request into one primary task before writing:

- `带货视频 / Sales video`: product-led conversion video with CTA
- `口播种草 / Voiceover seeding`: creator speaks to camera, benefit-driven recommendation
- `好物推荐 / Product recommendation`: daily-use reason and why it is worth buying
- `产品测评 / Product review`: test, reaction, pros/cons, tactile details, verdict
- `卖点展示 / Benefit demo`: one or two benefits made visible through action or comparison
- `效果展示 / Effect demo`: before/after, result shot, measurable or instantly readable proof
- `达人探店 / Influencer store visit`: location, atmosphere, signature product/service, value, CTA
- `团购视频 / Group-buying deal video`: local deal, package value, redemption process, store visit, group meal/service package, coupon CTA
- `游戏/IP活动视频 / Game and IP campaign video`: game download, pre-registration, update, skin/character/event, offline IP activity, ticketing or check-in CTA
- `UGC风格短视频 / UGC-style short video`: realistic user-shot product use, casual and believable
- `爆款视频复刻 / Viral remake`: adapt hook, pacing, structure, shot logic, and emotional engine
- `带货脚本视频化 / Sales-script-to-video`: convert copy into timestamped visuals, actions, camera, spoken lines, and CTA

Then pick one compatible video structure. Do not force every format into one output.

先判断用户最核心的内容任务，再选择一个匹配的视频结构。不要把所有形式都塞进一个视频。

## Three Production Scenarios / 三大生产场景

Before writing, first classify the request into one production scenario. This decision controls the output method.

正式输出前，先判断用户属于哪一种生产场景。这个判断决定后续怎么生成。

### Scenario 1: New Video From Product Content / 场景一：基于产品内容全新制作

Use when the user provides product information, product images, product URL, product selling points, product page copy, store details, or a CTA, but does not provide a fixed script or a reference viral video to remake.

当用户提供商品信息、商品图、商品链接、卖点、详情页文案、门店信息或 CTA，但没有给明确脚本，也没有要求复刻某条爆款视频时，使用此场景。

Coverage / 覆盖范围:

- 带货视频 / Sales video
- 口播种草 / Voiceover seeding
- 好物推荐 / Product recommendation
- 产品测评 / Product review
- 卖点展示 / Benefit demo
- 效果展示 / Effect demo
- 达人探店 / Influencer store visit
- 团购视频 / Group-buying deal video
- UGC 风格短视频 / UGC-style short video

Rules / 规则:

- Build the product brief first: category, target buyer, use scene, pain point, primary selling point, visible proof, CTA / 先建立商品简报：品类、目标用户、使用场景、痛点、主卖点、可视化证明、CTA
- Choose one primary content type from the coverage list, or create separate outputs if the user asks for multiple types / 从覆盖范围里选择一个主类型；如果用户要求多个类型，则分别输出
- Pick one primary selling point per video; do not stack every feature / 每条视频只主打一条卖点，不堆所有功能
- Use the timed template under `Format Patterns / 内容结构` for the chosen type / 使用下方 `Format Patterns / 内容结构` 中对应类型的时间轴模板
- Make product proof visible through action, result, comparison, reaction, or store/location evidence / 通过动作、结果、对比、反应或门店/地点证据让证明可见
- If product images are provided, preserve product identity and show all provided variants when relevant / 如果提供商品图，保持商品一致性；有多款式时按需展示所有款式
- Default output is `creator_portrait_image`, concise timestamped `script`, and `video_generation_prompt`; use long shooting plans or expanded analysis only when the user asks for analysis, options, or a production plan / 默认输出 `creator_portrait_image`、简洁时间轴 `script` 和 `video_generation_prompt`；只有用户要求分析、多方案或拍摄方案时，才展开长拍摄方案或分析

Default output method / 默认输出方法:

1. Identify platform and content type / 判断平台和内容类型
2. Build product brief / 建立商品简报
3. Choose one selling-point angle / 锁定一个卖点角度
4. Apply the content type's 5-beat timeline / 套用对应类型的 5 段时间轴
5. Add product consistency, facial expression, lip-sync, optional text, music, and transition constraints / 加入商品一致、表情、口型、可选画面文字、音乐和转场约束
6. Compress the result into one directly usable `video_generation_prompt` / 将结果压缩成一段可直接调用的 `video_generation_prompt`

### Scenario 2: Video From A Fixed Script / 场景二：基于明确脚本产出视频

Use when the user provides a fixed script, voiceover text, sales copy, host lines, spoken paragraph, fixed copy, or says "把这个脚本视频化", "turn this script into a video", "根据这段口播生成视频".

当用户提供明确脚本、口播文案、销售文案、主持词、台词段落、指定文案，或说“把这个脚本视频化 / 根据这段口播生成视频 / turn this script into a video”时，使用此场景。

Rules / 规则:

- Preserve the user's core script meaning, order, CTA, required wording, and selling claims unless they ask for rewriting / 保留用户脚本的核心意思、顺序、CTA、指定措辞和卖点宣称，除非用户要求改写
- Compress only when the script is too long for the requested duration; do not silently remove core claims / 只有脚本超过时长时才压缩，不要悄悄删掉核心卖点
- Convert every important line into: scene, camera, creator action, product position, visible proof, and spoken line / 把每个重要句子转成：场景、镜头、达人动作、产品位置、可见证明和口播台词
- Spoken lines should preserve the script meaning and order; if the user requests subtitles, keep them aligned with the spoken lines / 口播要保留脚本含义与顺序；如果用户要求字幕，字幕与口播保持一致
- Ensure the creator's mouth visibly moves during each spoken line / 每句口播时达人嘴巴必须可见并自然动
- Add missing visual logic: what appears on screen, how the product is handled, what result is shown, how shots connect / 补足视觉逻辑：画面有什么、产品怎么拿/用、结果怎么展示、镜头如何承接
- Do not invent new claims that are not in the script or provided product facts / 不要新增脚本和商品事实里没有的卖点宣称

Timed conversion method / 时间轴转换方法:

1. `0-3s` use the strongest opening line as hook and turn it into a visual opening / 用最强开头句做钩子，并转成视觉开场
2. `3-8s` keep the next logical script point and show product/context / 保留下一句逻辑重点，并展示产品或场景
3. `8-14s` turn the main claim into product action or visible proof / 把主卖点句转成产品动作或可见证明
4. `14-21s` compress supporting copy into one short line plus result/reaction / 把辅助文案压缩成一句短口播，加结果或反应
5. `21-27s` preserve value confirmation with product in frame / 保留价值确认，产品在画面中
6. `27-30s` preserve CTA and lip-sync / 保留 CTA 和口型同步

Default output method / 默认输出方法:

1. Parse script into beats / 拆解脚本节拍
2. Keep or lightly compress wording / 保留或轻压缩文案
3. Map each line to visible action and proof / 把每句映射到画面动作和证明
4. Add lip-sync and optional text placement only when useful / 加入口型，并只在需要时加入画面文字位置
5. Output timestamped video prompt or shooting script / 输出时间轴视频 prompt 或拍摄脚本

### Scenario 3: Viral Video Remake / 场景三：基于爆款视频做复刻

Use when the user provides a viral video, reference video, competitor video, link, transcript, shot description, screenshot sequence, or asks to "复刻爆款", "copy this style", "make one like this", "adapt this viral video".

当用户提供爆款视频、参考视频、竞品视频、链接、转写稿、分镜描述、截图序列，或说“复刻爆款 / 按这个风格做 / 做一个类似的 / adapt this viral video”时，使用此场景。

Rules / 规则:

- Remake structure, not protected expression: adapt hook mechanism, pacing, shot rhythm, proof mechanism, creator energy, music mood, and CTA shape / 复刻结构，不复刻受保护表达：迁移钩子机制、节奏、镜头律动、证明机制、达人状态、音乐氛围和 CTA 形态
- Do not copy exact wording, distinctive identity, watermark, brand assets, choreography, or unique creative expression unless the user owns the material or explicitly asks for internal reuse / 不复制原文、独特人物身份、水印、品牌资产、编舞或独特创意表达，除非用户拥有素材或明确内部复用
- Replace all product facts with the user's product facts; never keep the reference product's claims / 所有商品事实必须替换成用户商品事实，不保留参考商品宣称
- Preserve platform-native style: opening pressure, rhythm, creator emotion, proof reveal, and CTA logic / 保留平台原生风格：开头压力、节奏、达人情绪、证明揭示和 CTA 逻辑
- Keep the user's product visually consistent; if multiple variants exist, integrate them into the remade structure / 保持用户商品视觉一致；如有多款式，把多款式融入复刻结构
- If the reference includes music, extract the music mood and beat behavior; use current/trending platform music only after verification / 如果参考视频有音乐，提取音乐情绪和节拍行为；只有确认实时趋势后才写具体热门歌曲
- Do not make a frame-by-frame clone unless the user owns the source and asks for close internal adaptation / 不做逐帧克隆，除非用户拥有源素材并要求内部强复刻

Remake analysis checklist / 复刻分析清单:

- Hook type: question, shock, result-first, pain point, contradiction, price/value, celebrity/creator cue / 钩子类型：提问、震惊、结果前置、痛点、反差、价格价值、达人线索
- Shot rhythm: number of shots, cut speed, action continuity, beat placement / 镜头节奏：镜头数量、切换速度、动作承接、节拍点
- Character energy: excited, calm review, friend recommendation, expert, store explorer / 人物状态：兴奋、冷静测评、朋友安利、专业型、探店型
- Proof mechanism: demo, comparison, before/after, reaction, store atmosphere, social proof / 证明机制：演示、对比、前后对比、反应、店铺氛围、社会证明
- Music and sound: mood, tempo, beat strength, platform-native sound behavior / 音乐声音：情绪、速度、鼓点强弱、平台原生音频特征
- CTA shape: direct purchase, comment keyword, save/search, product card, store visit / CTA 形态：直接购买、评论关键词、收藏搜索、商品卡、到店

Timed remake method / 时间轴复刻方法:

1. `0-3s` adapt the hook mechanism with new product facts and original wording / 用新商品事实改写钩子机制，文案必须原创
2. `3-8s` adapt the reference context and creator energy to the user's product scene / 把参考视频的场景推进和达人状态迁移到用户商品场景
3. `8-14s` adapt the proof mechanism with user's product action, result, or comparison / 用用户商品动作、结果或对比复刻证明机制
4. `14-21s` adapt the reveal/payoff with visible proof and expression change / 用可见证明和表情变化复刻揭示/爽点
5. `21-27s` adapt value confirmation with product visible / 产品保持可见，复刻价值确认方式
6. `27-30s` adapt CTA shape for the target platform with new wording / 按目标平台复刻 CTA 形态，但文案重写

Default output method / 默认输出方法:

1. Extract reference structure / 提取参考结构
2. Replace product facts and proof / 替换商品事实和证明机制
3. Rewrite all spoken lines / 重写全部口播
4. Preserve rhythm, mood, and platform-native style / 保留节奏、氛围和平台原生风格
5. Output a legally safer adapted video prompt or script / 输出更稳妥的改写版视频 prompt 或脚本
