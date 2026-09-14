## Platform Defaults / 平台默认策略

## Table of Contents

- [Platform Defaults / 平台默认策略](#platform-defaults-平台默认策略)
- [Post-Input Default And Adjustment Prompt / 输入后的默认产出与调整提示](#post-input-default-and-adjustment-prompt-输入后的默认产出与调整提示)
- [Platform Ad Format Strategy / 平台广告格式策略](#platform-ad-format-strategy-平台广告格式策略)
  - [Douyin / 抖音电商](#douyin-抖音电商)
  - [Kuaishou / 快手](#kuaishou-快手)
  - [Xiaohongshu / 小红书](#xiaohongshu-小红书)
  - [Overseas Platforms / TikTok / Reels / Shorts / 海外平台](#overseas-platforms-tiktok-reels-shorts-海外平台)


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

After the user confirms parameters and provides any optional materials, show the active creator portrait and a concise Chinese timestamped script. Compile the full model instructions internally as `seedance_generation_package`.

用户确认参数并提供可选素材后，展示当前达人垫图和简洁中文时间轴脚本。完整模型指令在内部编译为 `seedance_generation_package`。

Visible confirmation format / 用户可见确认格式:

````text
creator_portrait_image
[达人垫图]

脚本
```text
0-3s: [画面动作]；口播：“……”
3-7s: [画面动作]；口播：“……”
7-12s: [画面动作]；口播：“……”
12-15s: [画面动作]；口播：“……”
```

确认达人形象和脚本后即可开始生成视频。
````

When the user replies `我已确认以上信息`, `确认`, `可以`, `符合预期`, `生成视频`, or similar, compile all applicable reference rules into the confirmed `seedance_generation_package`, attach `video_generation_materials`, and directly generate the video.

当用户回复“我已确认以上信息”“确认”“可以”“符合预期”“生成视频”等表达时，把所有适用 reference 规则编译进已确认的 `seedance_generation_package`，附带 `video_generation_materials`，直接生成视频。

If the user requests changes, revise the visible script and the corresponding internal package fields together. Do not restart parameter confirmation unless the change depends on a missing core asset or impossible decision.

用户提出修改时，同时更新可见脚本和内部生成包对应字段。除非修改依赖缺失核心素材或无法判断的关键决策，否则不重新走参数确认流程。

Do not use a large mandatory multi-choice confirmation form before generation. Do not force the user to select platform, selling-point direction, duration, CTA, language, or style before output. Infer missing parts from the user's prompt and defaults. Ask a short plain-text follow-up only when the product or core task cannot be identified.

生成前不要使用大型强制多选确认表单。不要强制用户先选择平台、卖点方向、时长、CTA、语言或风格。信息缺失时先根据用户输入和默认设置推断。只有无法判断商品或核心任务时，才用一句简短自然语言追问。

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

For the first response after a normal user prompt, use this compact style:

普通用户输入后的首次回复，使用类似 `ugc-commerce` 的简洁格式：

```text
creator_portrait_image
[已提供或 Nano Banana Pro 生成的达人垫图]

脚本
0-3s: [直接画面动作]；口播：“……”
3-7s: [直接画面动作]；口播：“……”
7-12s: [直接画面动作]；口播：“……”
12-15s: [直接画面动作]；口播：“……”

确认后即可开始生成视频。默认按 9:16 竖版抖音带货视频产出。
```

Do not output the full reasoning, category strategy, creative strategy, long planning document, or internal package by default. Use `creator_portrait_image` plus concise `script` as the default visible confirmation artifact. Only include analysis, multiple options, long shooting plans, or the complete tool payload when the user explicitly asks.

默认不要输出完整推理、品类策略、创意策略、长规划文档或内部生成包。默认用户可见确认产物使用 `creator_portrait_image` 和简洁 `script`。只有用户明确要求分析、多方案、长拍摄方案或完整工具 payload 时才展开。

If the user provides a detailed script, fixed copy, reference shot description, or follow-up instruction, follow the user's provided requirements and apply the default safety/quality rules only as support. Do not override a clear user requirement with the default Douyin/9:16/sales-video assumption.

如果用户已经提供详细脚本、固定文案、参考镜头描述或后续明确指令，就按照用户需求执行，默认安全和质量规则只作为辅助。不要用默认抖音/9:16/带货视频假设覆盖用户的明确要求。

## Platform Ad Format Strategy / 平台广告格式策略

When the user asks for platform-specific output, create distinct scripts, style choices, and visual formats for each platform instead of reusing one script everywhere.

当用户要求按平台输出时，不要把同一套脚本复制到所有平台；要基于平台广告格式分别生成脚本、风格和样式。

### Douyin / 抖音电商

- Format: vertical 9:16, 15-30s, hook within 1-2s, product visible before 3s / 格式：竖屏 9:16，15-30 秒，1-2 秒内钩子，3 秒前产品入镜
- Style: fast but coherent, creator-led, visible proof, clear purchase cue / 风格：节奏快但连贯，达人主导，可见证明，购买提示明确
- Script: pain/desire -> product reason -> hands-on demo -> result proof -> CTA / 脚本：痛点/欲望 -> 产品理由 -> 实操 -> 结果证明 -> CTA
- CTA: shop now, click product card, limited offer, comment keyword / CTA：立即购买、点商品卡、限时优惠、评论关键词

### Kuaishou / 快手

- Format: vertical 9:16, practical demo or direct recommendation, value proof early / 格式：竖屏 9:16，实用演示或直接推荐，价值证明前置
- Style: grounded, everyday, trustworthy, less polished / 风格：接地气、日常、可信、不过度精致
- Script: "I tried this" -> practical use -> price/value -> result -> direct CTA / 脚本：“我试过” -> 实用场景 -> 价格/价值 -> 结果 -> 直接 CTA
- CTA: ask to buy, follow, enter live room, use coupon / CTA：下单、关注、进直播间、领券

### Xiaohongshu / 小红书

- Format: vertical 9:16, recommendation/review/note-like video, stronger lifestyle context / 格式：竖屏 9:16，种草/测评/笔记感视频，生活方式场景更强
- Style: less aggressive, experience-led, aesthetic but real, trust-first / 风格：不强卖，体验导向，有审美但真实，先建立信任
- Script: personal situation -> discovery/use -> detail proof -> result feeling -> soft CTA / 脚本：个人场景 -> 发现/使用 -> 细节证明 -> 结果感受 -> 软 CTA
- CTA: save, comment, search product, check notes, ask for link / CTA：收藏、评论、搜索产品、看笔记、问链接

### Overseas Platforms / TikTok / Reels / Shorts / 海外平台

Use this section only when the user explicitly asks for overseas platforms, English copy, bilingual output, TikTok Shop, Instagram Reels, or YouTube Shorts.

只有用户明确要求海外平台、英文文案、双语输出、TikTok Shop、Instagram Reels 或 YouTube Shorts 时，才使用本节。

- Format: vertical 9:16, creator-first, hook-driven, visual demo, caption-friendly when subtitles are requested / 格式：竖屏 9:16，达人优先，强钩子，可视化演示；用户要求字幕时适配字幕
- Style: platform-native UGC, quick opening, clear transformation or reaction / 风格：平台原生 UGC，快速开头，清楚变化或反应
- Script: pattern interrupt -> product-in-use -> proof -> reaction -> CTA / 脚本：打断滑走 -> 产品使用 -> 证明 -> 反应 -> CTA
- CTA: shop link, link in bio, save, comment, learn more / CTA：购物链接、主页链接、收藏、评论、了解更多
