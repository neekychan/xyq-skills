## Core Judgment / 核心判断

## Table of Contents

- [Core Judgment / 核心判断](#core-judgment-核心判断)
- [Inputs / 输入](#inputs-输入)
  - [Input Evidence Priority / 输入证据优先级](#input-evidence-priority-输入证据优先级)
- [Platform Defaults / 平台默认策略](#platform-defaults-平台默认策略)
- [Post-Input Default And Adjustment Prompt / 输入后的默认产出与调整提示](#post-input-default-and-adjustment-prompt-输入后的默认产出与调整提示)


Use this skill when the user's real target is:

- conversion, sales, lead generation, product click-through, or order intent
- product seeding, sales voiceover, ecommerce UGC, or product recommendation
- making a selling point, use case, result, or comparison visible
- showing effect, proof, store atmosphere, product handling, creator reaction, or before/after
- game download, game pre-registration, version update, skin/character/event promotion, or IP activity conversion

当用户真实目标是以下任一情况时使用本 skill：

- 转化、卖货、引流、点击、下单意图
- 带货、口播、种草、好物推荐、UGC 广告
- 让卖点、效果、使用场景、对比结果被看见
- 展示产品效果、证明点、店铺氛围、产品使用、达人反应、前后对比
- 游戏下载、游戏预约、版本更新、皮肤/角色/活动推广、IP 联动或线下活动转化

Do not optimize primarily for abstract brand tone unless the user explicitly asks. Brand tone may shape wording, but conversion proof and visible selling points lead.

除非用户明确要求，否则不要优先优化抽象品牌调性。品牌语气可以影响表达，但优先级低于转化、可视化卖点和效果证明。

## Inputs / 输入

Accept any combination of:

- product URL, product name, product image, product page copy, listing text, or SKU notes
- CTA, offer, platform, duration, language, audience, creator persona, or tone
- existing sales script or voiceover copy
- reference viral video, competitor video, or desired content format
- store, restaurant, local service, offline location, or influencer visit details

可接受以下任意组合：

- 商品链接、商品名、商品图片、详情页文案、SKU 信息
- CTA、优惠、平台、时长、语言、受众、达人设定、语气
- 已有带货脚本、口播稿、卖点文案
- 参考爆款视频、竞品视频、想要的内容形式
- 门店、餐厅、本地服务、线下地点、达人探店信息

If key information is missing:

- If CTA is missing, use a light natural CTA or mark `[CTA]`
- If product details are thin, infer only from visible/provided facts and ask for missing proof points when needed
- If a URL or image cannot be parsed, ask for product category, main selling point, proof point, price/offer, and CTA

如果关键信息缺失：

- 缺 CTA 时，使用自然轻 CTA，或保留 `[CTA]`
- 商品信息不足时，只基于可见/已提供事实推断，必要时询问证明点
- 链接或图片无法解析时，询问品类、主卖点、证明点、价格/优惠、CTA

### Input Evidence Priority / 输入证据优先级

Before writing, parse all user-provided information, not only uploaded images.

生成前必须综合解析用户提供的所有信息，而不是只看上传图片。

Evidence priority / 信息优先级：

1. Explicit user instruction and current follow-up request / 用户当前明确指令和追问
2. Product title, product name, SKU title, listing text, and page copy / 商品标题、商品名、SKU 标题、详情页文案
3. Product URL, store URL, product page, landing page, and any parsed facts from the page / 商品链接、店铺链接、落地页和可解析页面事实
4. User-provided selling points, price, offer, CTA, platform, audience, and script / 用户提供的卖点、价格、优惠、CTA、平台、人群和脚本
5. Uploaded product images, model images, screenshots, video links, or reference videos / 用户上传的商品图、模特图、截图、视频链接或参考视频
6. Visual inference from images when text is missing / 文本缺失时再基于图片做视觉推断

Role and evidence handling / 角色与信息处理：

- Build the product role from all inputs: product category, target wearer/user, buyer decision-maker, presenter/host, and visual reference person / 综合所有输入建立商品角色：品类、目标穿着者/使用者、购买决策者、展示者/达人、图片参考人物
- Use text, title, link, SKU, and page copy to identify the product category, intended user, purchase motivation, and conversion goal / 使用文本、标题、链接、SKU 和详情页文案判断商品品类、目标使用者、购买动机和转化目标
- Use uploaded images to preserve product appearance, colors, materials, cut, pattern, packaging, visible variants, styling, and possible presenter image / 使用上传图片还原商品外观、颜色、材质、版型、图案、包装、可见款式、搭配方式和可能的出镜人物形象
- When a person appears or the video needs a presenter, define one stable protagonist before writing the shot beats. Bind the person with 2 to 4 visible traits: approximate age range, gender presentation when relevant, hair style, outfit, role/temperament, and relation to the product. Keep the same protagonist across all shots unless the user asks for multiple people / 只要有人物出镜或视频需要达人，就先定义一个稳定主角，再写分镜。用 2 到 4 个可见特征绑定人物：大致年龄段、必要时的性别呈现、发型、穿搭、角色/气质、与商品的关系。除非用户要求多人，全片保持同一个主角。
- If the user provides a person reference, preserve the reference person's visible identity cues and write them positively, e.g. `参考图人物作为主体1，保持同一位短发、白色T恤、自然生活感的年轻女性达人形象，全片由主体1试用并口播` / 如果用户提供真人参考图，保留参考人物的可见身份线索，并用正向句式表达，例如“参考图人物作为主体1，保持同一位短发、白色T恤、自然生活感的年轻女性达人形象，全片由主体1试用并口播”。
- If no person reference is provided, create a lightweight, product-appropriate protagonist description. Do not invent exaggerated beauty traits, celebrity likeness, or generic influencer face. Prefer ordinary UGC roles such as `年轻上班族女生`, `真实宝妈达人`, `通勤男生`, `探店达人`, `美妆测评朋友`, or `实用型家庭用户` / 如果没有真人参考图，生成轻量、符合商品目标人群的人物描述。不要编夸张颜值、明星相似脸或模板化网红脸。优先使用普通 UGC 角色，如“年轻上班族女生”“真实宝妈达人”“通勤男生”“探店达人”“美妆测评朋友”“实用型家庭用户”。
- Keep protagonist wording stable in the internal package: introduce `主体1` once, then reuse `主体1` or the same short role label in every beat that contains the person / 内部生成包中人物写法要稳定：先定义“主体1”，之后每个有人物的节拍都复用“主体1”或同一个短角色标签。
- The image person can be the main character when the person matches the target user, the product use case, or the user's explicit request / 当图片人物与目标使用者、商品使用场景或用户明确要求一致时，图片人物可以作为主角
- The image person can be a presenter, parent, seller, host, reviewer, store staff, or scale reference when the person is showing the product rather than using it / 当图片人物是在展示商品而不是最终使用商品时，可设定为展示者、家长、卖家、主播、测评者、店员或比例参照
- If the product title says `男童`, `女童`, `儿童`, `宝宝`, `中大童`, `童装`, or similar, treat the product as children's wear; use child wearing, hanger display, folded stack, or parent/host handling as the main proof scene / 商品标题出现“男童、女童、儿童、宝宝、中大童、童装”等词时，按童装处理；主要证明场景使用儿童上身、衣架展示、叠放展示或家长/主播手持展示
- For kids' products, an adult in the image can appear as parent/host/presenter while the product benefit is shown for the child wearer or child-use scene / 儿童商品中，图片成人可作为家长、主播或展示者出镜，同时商品效果展示给儿童穿着者或儿童使用场景
- For adult apparel, beauty, skincare, accessories, fitness, commuter, lifestyle, or creator-use products, a matching image person can naturally become the try-on model, user, or creator protagonist / 成人服饰、美妆、护肤、配饰、运动、通勤、生活方式或创作者使用类商品中，匹配的图片人物可自然成为试穿模特、使用者或达人主角
- If image appearance and text category differ, preserve the visible product appearance from the image while choosing the role setup from the product need / 图片外观和文本品类不一致时，商品外观按图片还原，角色设置按商品需求判断
- If product title, link, image, and user instruction conflict in a way that changes the core product or protagonist, ask one short clarification question before generation / 当商品标题、链接、图片和用户指令互相冲突，并影响核心商品或主角判断时，生成前用一句话澄清

Video-generation role phrasing / 视频生成角色正向表达：

- Write role logic as positive execution: `图片中的成年人作为家长达人手持展示童装，儿童穿着同款做转身和抬手动作` / 角色逻辑使用正向执行句式：“图片中的成年人作为家长达人手持展示童装，儿童穿着同款做转身和抬手动作”
- For matching adult products, write: `参考图人物作为主角试穿/试用，保持参考人物气质和商品外观一致` / 成人商品且人物匹配时写：“参考图人物作为主角试穿/试用，保持参考人物气质和商品外观一致”
- For product-only images, write: `使用手部、衣架、桌面、镜前或生活场景展示商品，主角身份按商品目标人群设定` / 只有商品图时写：“使用手部、衣架、桌面、镜前或生活场景展示商品，主角身份按商品目标人群设定”
- For generated protagonists, write: `将主体1定义为同一位[年龄段/角色]，[发型/穿搭/气质]，全片保持主体1形象一致，由主体1完成试用、反应和口播` / 生成型主角写：“将主体1定义为同一位[年龄段/角色]，[发型/穿搭/气质]，全片保持主体1形象一致，由主体1完成试用、反应和口播”。

Supported input parsing / 输入解析范围：

- Product title / 商品标题: extract category, gender/age, season, material, style, scene, year/newness, and variants / 提取品类、性别年龄、季节、材质、风格、场景、年份新款和款式
- Product link / 商品链接: use page text, title, images, price, SKU, and offer when accessible; if inaccessible, rely on the pasted title and uploaded assets / 链接可访问时解析标题、图片、价格、SKU 和优惠；不可访问时依赖用户粘贴标题和上传素材
- Video link / 视频链接: use it as reference for rhythm, hook, shot logic, creator energy, and platform style; replace all product facts with the user's product facts / 视频链接作为节奏、钩子、镜头逻辑、达人状态和平台风格参考；商品事实全部替换成用户商品
- Reference images / 参考图: preserve product identity, colors, patterns, texture, shape, and visible variants; infer category from image only when text gives no category / 参考图用于保持商品身份、颜色、图案、质地、形状和可见款式；只有文本没有品类时才由图片推断品类

## Platform Defaults / 平台默认策略

- Douyin / 抖音电商: faster hook, stronger visible proof, clearer CTA, product appears early / 开头更快，证明更强，CTA 更明确，商品更早出现
- Kuaishou / 快手: direct, practical, value-for-money, everyday credibility / 更直接、更实用、更强调性价比和生活可信度
- Xiaohongshu / 小红书: experience-led recommendation/review, lifestyle context, softer CTA / 更像体验种草和测评，生活方式场景更强，CTA 更软
- WeChat Channels / 微信视频号: trust-based recommendation, acquaintance-like tone, clear service/value cue, moderate rhythm / 更强调可信推荐、熟人感表达、清楚服务或价值提示，节奏适中
- Generic UGC feed / 通用 UGC 信息流: believable creator, real environment, handheld phone-shot style, product-in-use / 真实达人、真实环境、手机手持感、商品在使用中
- Overseas platforms such as TikTok, Instagram Reels, and YouTube Shorts are used only when the user explicitly asks for overseas platform output / 只有用户明确要求海外平台时，才使用 TikTok、Instagram Reels、YouTube Shorts 等平台策略

If platform is unspecified, default to a Douyin-style vertical 9:16 sales video. Do not block output by asking size/platform questions first; produce the default version and add a short adjustment prompt for the user.

未指定平台时，默认生成 9:16 竖版抖音带货视频。不要因为缺尺寸/平台先卡住追问；先产出默认版本，再给用户一个简短的调整提示。

If an optional adjustment entry is shown, its platform choices should be `抖音 / 小红书 / 快手 / 微信 / 其他`. Do not show `TikTok / Instagram Reels / YouTube Shorts` in the default interaction unless the user explicitly asks for overseas platforms.

如果展示可选调整入口，平台选项使用 `抖音 / 小红书 / 快手 / 微信 / 其他`。默认交互里不要展示 `TikTok / Instagram Reels / YouTube Shorts`，除非用户明确要求海外平台。

## Post-Input Default And Adjustment Prompt / 输入后的默认产出与调整提示

After the user enters a product prompt, script, image, URL, or short request, default to this assumption unless the user specifies otherwise:

用户输入商品 prompt、脚本、图片、链接或简短需求后，除非用户另有指定，默认按以下设置产出：

- Default format / 默认尺寸: `9:16 vertical / 9:16 竖版`
- Default platform / 默认平台: `Douyin / 抖音`
- Default content type / 默认类型: `sales video / 带货视频`
- Default goal / 默认目标: visible product benefit and conversion / 展示商品效果并促进转化
- Default language / 默认语言: `Chinese spoken lines; subtitles only when requested / 中文口播；用户要求时才加字幕`

Default generation chain / 默认生成链路：

1. Parse product and conversion goal / 解析商品和转化目标
2. Choose a richer creator persona from `creator-persona-library.md` / 从 `creator-persona-library.md` 选择更具体的达人设定
3. Use Nano Banana Pro through `sandbox_generate_image` to match and generate a product-appropriate creator portrait when no suitable person reference is supplied / 没有合适真人参考图时，通过 `sandbox_generate_image` 使用 Nano Banana Pro 生成匹配商品的达人形象
4. Let the user adjust the creator portrait if needed / 用户可反馈调整达人形象
5. Generate the 15-second sales script from `hook-library.md`, `benefit-voiceover-library.md`, and `cta-library.md` / 基于 `hook-library.md`、`benefit-voiceover-library.md` 和 `cta-library.md` 生成 15 秒带货脚本
6. Compile all reference rules into an internal `seedance_generation_package`; after `dynamic_questionnaire` confirmation, pass it directly to the video generation tool / 把所有相关 reference 规则编译成内部生成包，经过 `dynamic_questionnaire` 确认后直接传给视频工具

Use a lightweight confirmation flow only when the environment supports interactive cards or the user expects video generation. Keep confirmation short and practical.

只有在环境支持交互卡片，或用户明确期待继续生成视频时，才使用轻量确认流程。确认内容要短、实用。

Lightweight confirmation card / 轻量确认卡:

- Card title should follow the product/task, e.g. `男童衬衫种草视频参数确认` / 卡片标题跟随商品任务，例如“男童衬衫种草视频参数确认”
- Ask only these core items by default / 默认只确认以下核心项：
  1. `是否需要旁白配音`: default `需要`; optional `不需要`
  2. `视频比例选择`: default `9:16 竖版（适合短视频平台）`; optional `16:9 横版（适合电商平台投放）`, `4:3 常规比例`, `3:4 竖版电商比例`
  3. `是否有其他补充要求`: free text, optional, placeholder `请输入补充信息，没有可留空`
- Do not ask the user to select platform by default. Use `抖音` unless the user provided another domestic platform / 默认不要让用户选择平台，未指定时使用抖音；用户已指定小红书、快手、微信等平台时按用户指定
- Do not include overseas platform choices in the card unless explicitly requested / 卡片里不要出现海外平台选项，除非用户明确要求
- Do not ask for selling-point direction, duration, CTA, language, or style as mandatory fields / 不要把卖点方向、时长、CTA、语言或风格设为必选项
- If the user has already provided a detailed script, fixed platform, ratio, voiceover choice, or generation instruction, skip repeated confirmation and execute directly / 如果用户已经提供详细脚本、固定平台、比例、是否配音或明确生成指令，跳过重复确认并直接执行

If product images or model/try-on images are important but missing, ask one short material question after the first confirmation:

如果商品图或模特展示图对结果很重要但缺失，在第一次确认后只追问一句素材问题：

```text
为了生成更贴合真实商品效果的视频，请问是否有这款商品图片或模特展示图可以提供？如果没有，我将基于描述直接生成通用风格视频。
```

After the user confirms parameters and provides any optional materials, first generate or bind the active creator portrait, then build `video_generation_materials`, write the direct script, and compile the internal `seedance_generation_package`. Show the creator portrait and script to the user; pass the full package directly to the video generation tool.

用户确认参数并提供可选素材后，先生成或绑定当前达人形象，再整理 `video_generation_materials`、生成直接脚本，并把所有相关 references 编译成内部 `seedance_generation_package`。用户侧只展示达人图和脚本；完整生成包直接传给视频工具。

Creator portrait step / 达人形象步骤：

- First classify uploaded materials into person/model/creator references and product/reference assets / 先把用户上传素材区分为人像/模特/达人参考图，以及商品图/参考素材
- Before calling `sandbox_generate_image`, choose one persona type and bind role, age band, visible styling, scene, product relationship, and speaking tone / 调用 `sandbox_generate_image` 前，先选择一种达人类型，并绑定角色、年龄段、可见造型、场景、商品关系和口播气质
- If the user supplied a suitable person/model/reference image, use it as `creator_portrait_image` and preserve visible identity cues / 用户提供合适真人或模特参考图时，将其作为 `creator_portrait_image` 并保留可见身份线索
- If the user supplied only product images, screenshots, packaging images, links, scenery, props, or non-person references, treat that as no suitable person image / 如果用户只提供商品图、截图、包装图、链接、场景图、道具图或非人像参考图，则视为没有合适达人参考图
- If no suitable person image is supplied and `sandbox_generate_image` is available, internally build the full high-quality creator image prompt from `portrait-image-rules.md`, pass that complete prompt into `sandbox_generate_image`, then write the script / 没有合适真人参考图且 `sandbox_generate_image` 可用时，必须先按 `portrait-image-rules.md` 内部构建完整高质量达人图提示词，并把完整提示词传入该工具生成达人画像，再写脚本
- The image request should include product category, target buyer, creator role, domestic platform style, 4:5 portrait framing, realistic UGC scene, phone-shot texture without visible phone-holding by default, and `output_path`, e.g. `/workspace/出镜达人/creator_portrait_subject_1.png` / 生图请求包含商品品类、目标人群、达人角色、国内平台风格、4:5 构图、真实 UGC 场景、默认不手持手机的手机拍摄质感和 `output_path`
- Do not expose the full internal image prompt to the user; show only the generated portrait, concise `creator_image_caption`, and `product_consistency_note` / 不向用户外露完整内部生图提示词，只展示生成的达人图、简洁达人说明和商品一致性说明
- Show the portrait reference before or together with the script; do not hide it inside the video prompt / 达人图需要在脚本前或脚本一起展示，不要只写进视频 prompt
- If the user says `达人不合适`, `换个达人`, `发型改一下`, `穿搭调整`, `更像宝妈`, `更年轻`, `更生活化`, or similar, regenerate the portrait with `sandbox_generate_image`, then refresh the script and internal generation package / 用户反馈达人形象不合适时，先重新调用 `sandbox_generate_image` 改图，再更新脚本和内部生成包
- Do not start video generation while the latest user intent is portrait adjustment / 用户最新意图是调整达人形象时，不要开始生成视频

Video reference / 垫图 step:

- Build `video_generation_materials` before script confirmation or video generation.
- Put user-uploaded product images, product assets, reference images, screenshots, and files first, preserving their original order.
- Put the active `creator_portrait_image` last. If the active portrait is an uploaded user person image already present in the material list, keep it once and mark it as the active portrait.
- When the user confirms generation, pass `video_generation_materials` together with `seedance_generation_package` to the video generation tool or frontend pipeline.
- The package states that user product materials define product appearance and `creator_portrait_image` defines the protagonist/person identity.
- Do not rely on text-only prompt handoff when images are available.

视频垫图步骤：

- 在脚本确认或生成视频前整理 `video_generation_materials`。
- 用户上传的商品图、商品素材、参考图、截图、文件放在前面，并保持原顺序。
- 当前 `creator_portrait_image` 放在最后。若当前达人图本身就是用户上传的人像图且已经在素材列表中，只保留一次，并标记为当前达人图。
- 用户确认生成时，把 `video_generation_materials` 和 `seedance_generation_package` 一起传给视频生成工具或前端生成链路。
- 内部生成包中说明用户商品素材决定商品外观，`creator_portrait_image` 决定主体人物形象。
- 有图片素材时，不要只用纯文本 prompt 交付。

Script enrichment step / 脚本丰富度步骤：

- Choose one hook mechanism for 0-3s from `hook-library.md`; do not reuse the same first spoken line across multiple outputs / 从 `hook-library.md` 选择 0-3 秒钩子机制；多条输出时不要复用同一句开头口播
- Choose one main benefit transformation from `benefit-voiceover-library.md`; convert feature into user-facing value and visible proof / 从 `benefit-voiceover-library.md` 选择主利益点表达；把功能转成用户利益和可见证明
- Choose a platform-matched CTA from `cta-library.md`; use one clear next action only / 从 `cta-library.md` 选择符合平台的 CTA；只保留一个明确下一步
- Keep the hook, benefit voiceover, and CTA all in the same creator voice / hook、利益点口播和 CTA 要保持同一个达人口吻
- If the user asks for more variety, vary persona, hook mechanism, proof action, benefit wording, and CTA together / 用户要求更多变化时，同时变化达人类型、钩子机制、证明动作、利益点口播和 CTA

User-facing confirmation format / 用户确认格式:

```text
creator_portrait_image
[已提供或 Nano Banana Pro 生成的达人画像引用。]

脚本
0-3s: [直接画面动作]；口播：“……”；可选短花字：“……”
3-7s: [直接画面动作]；口播：“……”；可选短花字：“……”
7-12s: [直接画面动作]；口播：“……”；可选短花字：“……”
12-15s: [直接画面动作]；口播：“……”；可选短花字：“……”

确认达人形象和脚本后即可开始生成视频；商品一致性、光影、构图、运镜、动作、声音、文字和连续性细节会通过内部生成包直接传给视频工具。
```

After this visible confirmation artifact, call `dynamic_questionnaire` with one radio question:

- `继续生成视频`: continue with video generation from the displayed creator portrait, script, `video_generation_materials`, and internal generation package.
- `先修改方案`: wait for revisions and do not generate video yet.

When the user selects `继续生成视频` in `dynamic_questionnaire`, or explicitly says `生成视频` after seeing the current visible artifact, directly generate the video using the confirmed `video_generation_materials`, `creator_portrait_image`, script and `seedance_generation_package`. The next user-facing step should be video generation.

当用户在 `dynamic_questionnaire` 中选择“继续生成视频”，或在看过当前可见方案后明确说“生成视频”等表达时，直接基于已确认的 `video_generation_materials`、`creator_portrait_image`、脚本和 `seedance_generation_package` 生成视频。

If the user requests changes, revise the visible script and internal `seedance_generation_package`. Do not restart parameter confirmation unless the requested change depends on a missing core asset or impossible decision.

如果用户认为达人形象、脚本或视频细节有问题，直接按用户反馈修改对应部分。达人形象问题先调用 `sandbox_generate_image` 更新图片，再同步调整脚本和内部生成包；商品、光影、运镜、动作、声音或文字问题直接更新生成包的对应字段。

Revision prompt format / 修改后提示格式:

```text
已按你的要求更新达人图/脚本和内部视频生成细节。

creator_portrait_image
[如本次改了达人形象，展示最新达人画像引用；如未改，可引用当前确认版本。]

脚本
[更新后的 15 秒脚本。]

确认后即可基于这个版本开始生成视频。
```

Do not use a large mandatory multi-choice parameter form before generation. The required final `dynamic_questionnaire` may contain only the two next-step options `继续生成视频` and `先修改方案`. Do not force the user to select platform, selling-point direction, duration, CTA, language, or style before output. Infer missing parts from the user's prompt and defaults. Ask a short plain-text follow-up only when the product or core task cannot be identified.

生成前不要使用大型强制参数确认表单。必须使用的最终 `dynamic_questionnaire` 只包含“继续生成视频”和“先修改方案”两个下一步选项。不要强制用户先选择平台、卖点方向、时长、CTA、语言或风格。信息缺失时先根据用户输入和默认设置推断。只有无法判断商品或核心任务时，才用一句简短自然语言追问。

At the end of the output, add this short user-facing adjustment note when useful:

必要时在输出末尾添加以下简短调整提示：

```text
默认按 9:16 竖版抖音带货视频产出。
如果不满意，可以继续调整：
1. 尺寸：16:9 横版 / 9:16 竖版 / 4:3 方版 / 3:4 竖版
2. 投放平台：抖音 / 小红书 / 快手 / 微信 / 其他
3. 补充要求：风格、节奏、卖点、模特、场景、价格优惠、画面文字等
```

Use the adjustment note as guidance, not as a blocker. If the user already specified size, platform, and requirements, do not repeat the full note unless it helps.

这个调整提示是后续修改入口，不是生成前置阻塞。如果用户已经明确尺寸、平台和要求，就不必完整重复。

For the first response after a normal user prompt, use the compact `ugc-commerce` style:

普通用户输入后的首次回复，使用类似 `ugc-commerce` 的简洁格式：

```text
creator_portrait_image
[supplied or Nano Banana Pro generated creator portrait reference]

脚本
[concise 15-second script]

确认达人形象和脚本后即可开始生成视频；详细商品锁、光影、构图、运镜、动作、声音、文字和连续性规则将通过内部生成包传给视频工具。
```

Do not output the full reasoning, category strategy, creative strategy, internal material manifest or generation package by default. Use `creator_portrait_image` and a concise `script` as the default user-facing confirmation artifact.

默认不输出完整推理、品类策略、创意策略、素材清单或内部生成包。用户侧默认只展示 `creator_portrait_image` 和简洁 `script`。

If the user provides a detailed script, fixed copy, reference shot description, or follow-up instruction, follow the user's provided requirements and apply the default safety/quality rules only as support. Do not override a clear user requirement with the default Douyin/9:16/sales-video assumption.

如果用户已经提供详细脚本、固定文案、参考镜头描述或后续明确指令，就按照用户需求执行，默认安全和质量规则只作为辅助。不要用默认抖音/9:16/带货视频假设覆盖用户的明确要求。
