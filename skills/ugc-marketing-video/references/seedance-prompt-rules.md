## Output Behavior / 输出规则

Match the user's requested deliverable:

- Default user-facing deliverable is the active creator portrait plus one direct timestamped script / 默认用户侧交付是当前达人参考图加一份直接时间轴脚本
- Compile the detailed Seedance/video-tool instructions internally with `seedance-generation-contract.md` and pass them directly to the generation tool / 使用 `seedance-generation-contract.md` 在内部编译详细 Seedance/视频工具指令，并直接传给生成工具
- Keep the detailed product lock, light, camera, motion, physical, audio, text and continuity instructions out of normal user-facing chat / 商品锁、光影、镜头、运镜、物理、声音、文字和连续性详细指令不在普通用户回复中展开
- Do not output long strategy notes, hidden category analysis, or full production shooting plans unless the user asks for them / 不要默认输出长策略说明、隐藏品类分析或完整拍摄执行方案
- First choose one of the three production scenarios: new video from product content, video from a fixed script, or viral video remake / 先选择三大生产场景之一：基于产品内容全新制作、基于明确脚本产出视频、基于爆款视频复刻
- For domestic UGC generation, enrich the script with the dedicated references before the final video prompt: creator persona, hook, benefit voiceover, and CTA / 国内 UGC 生成时，在最终视频 prompt 前使用独立 references 丰富脚本：达人形象、hook、利益点口播和 CTA
- Apply the dedicated quality rules before compiling the final internal package: input consistency, text accuracy, marketing expression, diversity when relevant, and final quality check / 编译最终内部生成包前应用专门质量规则：输入一致性、文字准确性、营销表达、多样性和最终质量检查
- If the user explicitly asks for the full model prompt or video-tool payload, show the compiled `seedance_generation_package` in a fenced `text` code block / 用户明确要求完整模型 prompt 或视频工具 payload 时，才展示 `seedance_generation_package`
- If size and platform are not specified, default to a 9:16 Douyin sales video, then provide the adjustment note for size/platform/extra requirements when useful / 用户未指定尺寸和平台时，默认输出 9:16 抖音带货视频，必要时附上尺寸/平台/补充要求的调整提示
- Do not create a required pre-generation selection UI or mandatory confirmation card. Adjustment options are optional after output, not required before output / 不要创建生成前必选的选择 UI 或强制确认卡片。调整选项是输出后的可选入口，不是输出前的必填项
- Default creator portrait notes, scripts, spoken lines, optional text effects, and prompt body should be Chinese. Subtitles are generated only when the user explicitly requests them or provides subtitle copy. Use English, bilingual text, or overseas platform wording only when the user explicitly requests it / 默认达人画像说明、脚本、口播、可选特效字和 prompt 主体使用中文。只有用户明确要求字幕或提供字幕文案时才生成字幕。只有用户明确要求时才使用英文、双语或海外平台表达
- If optional platform choices are shown, use `抖音 / 小红书 / 快手 / 微信 / 其他` by default; do not show TikTok, Instagram Reels, or YouTube Shorts unless the user asks for overseas platforms / 如果展示可选平台，默认使用 `抖音 / 小红书 / 快手 / 微信 / 其他`；用户未要求海外平台时不要展示 TikTok、Instagram Reels 或 YouTube Shorts
- When the user confirms the creator portrait and script, proceed directly to video generation if a video-generation tool is available. Use the internal `seedance_generation_package` and `video_generation_materials` as generation sources / 用户确认达人图和脚本后，如有视频生成工具，直接把内部生成包和垫图列表传给工具
- If the environment cannot generate video directly, keep the package internally ready; show it only when the user asks for the full model payload / 当前环境无法直接生成视频时，内部保留完整生成包；用户要求完整模型 payload 时再展示
- If the user provides a detailed script or explicit follow-up instruction, follow it directly and use default rules only for continuity, scale, pacing, platform-safe optional text, and physical plausibility / 用户提供详细脚本或明确后续指令时，直接按用户需求做，默认规则只用于连续性、尺寸、节奏、平台安全可选文字和物理合理性
- If the user asks for a script, output a timestamped script with actions and spoken lines / 用户要脚本时，输出带时间戳、动作和台词的脚本
- The default domestic chain may also output a concise timestamped script even when the user did not explicitly ask, because the script is the bridge between creator portrait and SD2.0 video prompt / 国内默认链路即使用户没有明确要求，也可以输出简洁时间轴脚本，因为脚本是达人画像和 SD2.0 视频 prompt 之间的桥梁
- If the user asks for a shooting plan, output a concise shooting plan / 用户要拍摄方案时，输出简洁拍摄方案
- If the user asks for multiple options, provide 2 to 3 distinct angles, each with one selling point / 用户要多个方案时，给 2 到 3 个不同角度，每个只主打一条卖点
- If the user asks for different platforms, output separate platform-specific versions with different hook style, pacing, CTA, music direction, and visual treatment / 用户要求多平台时，分别输出平台版本，每个平台有不同钩子、节奏、CTA、音乐方向和视觉样式
- If the user asks for different content types such as 带货、种草、测评、探店, output each type with its own method, structure, and proof logic / 用户要求不同内容类型时，分别按带货、种草、测评、探店等类型输出各自的方法、结构和证明逻辑
- If the user asks for creative types or reference-ad analysis, output category strategy plus creative type strategy, and give each creative type a timestamped rhythm / 用户要求创意类型或参考广告分析时，输出品类策略加创意类型策略，并给每种创意类型明确时间节奏
- If the user asks for group-buying or local deals, include package contents, deal price/value, redemption path, valid scene, store proof, and buy/reserve/navigate CTA / 用户要求团购或本地生活优惠时，输出套餐内容、团购价/价值、核销路径、适用场景、门店证明和购买/预约/导航 CTA
- If the user asks for game/IP/event content, include player/event motivation, gameplay or interaction proof, reward/ticket value, and download/reserve/join/check-in CTA / 用户要求游戏、IP 或活动内容时，输出玩家/活动动机、玩法或互动证明、福利/票券价值，以及下载/预约/参与/打卡 CTA
- If the user says "直接可用", "给视频生成工具", "生成视频", "directly usable", "for video generation", or similar, prioritize a direct-call video prompt / 用户要求直接可用或用于视频生成时，优先输出可直接调用的视频 prompt

## Video-Generation Positive Prompting Rules / 视频生成正向指令规则

When the target is video generation, compile the internal package as positive execution instructions.

当目标是视频生成时，prompt 使用正向执行指令。

- Treat this as a hard rule for `seedance_generation_package`: the tool payload describes what to create, maintain, show, connect and complete / 内部工具包描述要创建、保持、呈现、承接和完成的内容
- Prefer positive words: `保持`, `使用`, `呈现`, `镜头跟随`, `动作完成后切换`, `每镜保持至少3秒`, `口播清晰自然`, `商品外观保持一致` / 优先使用正向词：保持、使用、呈现、镜头跟随、动作完成后切换、每镜保持至少3秒、口播清晰自然、商品外观保持一致
- Convert negative constraints into positive actions before final output / 最终输出前把负向约束改写成正向动作
- Keep process rules and safety analysis internal when they are phrased negatively; the tool payload uses executable positive wording / 负向表述的流程规则和安全分析只在内部使用；工具 payload 使用可执行的正向措辞
- Use "stable 4-shot structure" for 15 seconds: `0-3s`, `3-7s`, `7-12s`, `12-15s` / 15 秒使用“稳定 4 镜结构”：`0-3s`、`3-7s`、`7-12s`、`12-15s`
- Use `苹果原相机拍摄风格` as the default visual texture, with natural light, real environment, slight handheld movement, and platform-native UGC feel / 默认视觉质感使用“苹果原相机拍摄风格”，配合自然光、真实环境、轻微手持晃动和平台原生 UGC 感
- Each shot has one camera state, one main action, and one spoken line; subtitles are added only when requested / 每个镜头只有一个镜头状态、一个主动作和一句口播；只有用户要求时才加字幕
- Use transitions as positive events: `action completes and product rests`, `clean cut to the established next state`, `tabletop reset`, `mirror or fitting-room reset`, `product placed down then next product picked up`, `camera pans across a stable lineup` / 用正向事件写转场：动作完成且商品放稳、清晰切到已建立的下一状态、桌面重置、镜前或试衣间重置、放下当前商品再拿起下一个、镜头扫过稳定排列
- Keep the foreground clear throughout every cut. Hands stay connected to product interaction at a natural distance from the lens, and the next shot begins from a stable established composition / 每次切换时镜头前景持续清晰；手只在自然距离内完成商品互动，下一镜从稳定且已建立的构图开始
- Use stable Chinese creative text in the video frame only for key information such as offer, selling point, result, and CTA / 画面里只用稳定中文花字/贴纸字/价格牌等突出优惠、卖点、结果和 CTA
- Place optional text in platform-safe areas, away from right-side buttons, bottom captions, product cards, comment areas, and live/action UI / 可选画面文字放在平台安全区，避开右侧按钮、底部标题、商品卡、评论区和直播/操作 UI
- Before tool handoff, replace negative trigger words with positive alternatives in every field sent to the video model / 传给工具前，把会发送给视频模型的负向触发词改成正向替代表达

## SD2.0 Stability Control Blocks / SD2.0 稳定控制块

When compiling the SD2.0 internal package, include positive control blocks for the following dimensions when relevant:

### Input Consistency / 输入一致性

```text
商品外观全片保持与用户素材一致，包括形状、颜色、包装、logo位置、材质纹理、尺寸比例和已提供款式；口播、花字、价格、优惠、CTA 均使用用户提供或已确认的信息。
```

### Finished-Video Stability / 成片稳定性

```text
全片使用稳定4镜结构，每镜至少3秒，每镜一个主要动作、一句短口播和一个产品证明点；镜头在动作完成、口播结束、产品放稳、表情变化或结果出现后自然切换。
```

### Creator Authenticity / 达人真实性

```text
主体1使用已确认 creator_portrait_image 作为角色参考，全片保持同一脸部、发型、穿搭风格、身体比例和达人身份；主体1按真实生活方式完成试用、反应和口播。
```

### Physical And Spatial Accuracy / 物理与空间准确性

```text
所有物体和人体动作符合真实物理与空间关系：每镜一个主要物理互动；多个分离物体按顺序拿起、放下或由托盘、盒子、双手、桌面、货架、包装、容器等稳定支撑承载；商品始终有手、桌面、包装、身体、屏幕或场景物体作为比例参照。
```

### Text Accuracy / 文字准确性

```text
画面文字只使用短关键词、价格牌、优惠标签、结果词或CTA标签；每个文字元素保持2到8个汉字，默认每节拍一个文字元素；用户要求字幕时，字幕直接复用对应 spoken_line，只渲染一层完整字幕。
```

### Audio-Visual Sync / 视听同步

```text
每个镜头一句短 spoken_line，主体1口播时嘴型、表情和轻微头部动作自然同步；BGM 音量低于口播，音效只在产品出现、动作完成、优惠弹出、结果呈现或 CTA 时轻量出现。
```

### Video Rhythm / 视频节奏

```text
0-3秒建立观看理由并让商品出现，3-7秒回到商品和主卖点，7-12秒展示可见证明或结果，12-15秒完成价值确认和一个自然 CTA；全片有快有稳，证明段清楚可读。
```

### Marketing Expression / 营销表达

```text
全片只突出一个主卖点，卖点通过可见动作证明；口播把商品功能转成人话利益点，CTA 与平台和转化目标一致，并且只给一个下一步动作。
```

### Diversity / 多样性

For multiple outputs:

```text
多版本之间至少改变达人类型、hook机制、证明动作、场景、利益点口播或CTA中的三个维度，同时保持商品事实、优惠和CTA目标一致。
```

Positive rewrite examples / 正向改写示例:

- Instead of "不要硬切", write "镜头在动作完成后自然切换，下一镜首帧承接上一镜的手部动作或产品位置"
- Instead of "不要字幕错误", write "用户要求字幕时，字幕直接复用同一句 `spoken_line`"
- Instead of "不要衣服变形", write "多款服装先集合展示；当前款式动作完成并放稳后切换，下一镜从新款式已穿戴完整、人物姿态稳定的画面开始"
- Instead of "do not cut while static", write "each cut happens after a completed action, expression change, product placement, result reveal, or music beat"
- Instead of "不要出现双语字幕", write "用户要求字幕时，字幕语言使用中文，除非用户指定其他语言"
- Instead of "不要出现两行字幕", write "用户要求字幕时，只渲染一层完整字幕，花字只显示短关键词"
- Instead of "不要把商品换成别的款", write "商品外观全程保持与用户素材一致，包括颜色、版型、包装、logo 和关键细节"
- Instead of "不要画面过快", write "每个镜头保持至少 3 秒，口播后保留动作完成和自然停顿"
- Instead of "不要多个物品一起乱动", write "多个物品先集合展示，再按顺序拿起、放下或由托盘/盒子/双手稳定承载"

Internal package sanitization checklist / 内部生成包净化检查:

- The internal `seedance_generation_package` uses positive verbs such as `保持`, `展示`, `呈现`, `放置`, `拿起`, `跟随`, `承接`, `完成`, `回到`, `同步`, `复用`, `保留` / 内部 `seedance_generation_package` 使用保持、展示、呈现、放置、拿起、跟随、承接、完成、回到、同步、复用、保留等正向动词
- Product consistency is written as `商品外观保持一致` instead of "do not change product" / 商品一致性写成“商品外观保持一致”，不用“不要换商品”
- Optional subtitle consistency is written as `用户要求字幕时，字幕直接复用 spoken_line，只渲染一层完整字幕` instead of default subtitle generation / 可选字幕一致性写成“用户要求字幕时，字幕直接复用 spoken_line，只渲染一层完整字幕”，不要默认生成字幕
- Transition control is written as `动作完成后自然切换` instead of "do not hard cut" / 转场控制写成“动作完成后自然切换”，不用“不要硬切”
- Physical plausibility is written as `一个主动作、顺序操作、稳定支撑` instead of "do not violate physics" / 物理合理性写成“一个主动作、顺序操作、稳定支撑”，不用“不要违反物理”
- If a negative sentence remains useful as an internal quality check, keep it in `final_render_checks`; convert the generation instruction into a positive visible state or action / 如果负向句只适合作为内部质量检查，放入 `final_render_checks`；实际生成指令改写为正向的可见状态或动作

## Default Visible Script And Internal Tool Package / 默认可见脚本与内部工具包

Default user-facing response shape / 默认用户可见回复形态：

````text
creator_portrait_image
[已提供或由 Nano Banana Pro 生成的达人垫图]

脚本
```text
0-3s: [画面动作]；口播：“……”
3-7s: [画面动作]；口播：“……”
7-12s: [画面动作]；口播：“……”
12-15s: [画面动作]；口播：“……”
```

确认达人形象和脚本后即可开始生成视频。
````

The visible script is the main user artifact. Before video generation, compile the script and every applicable reference into `seedance_generation_package` according to `seedance-generation-contract.md`.

用户可见主产物是直接脚本。生成视频前，按照 `seedance-generation-contract.md`，把脚本和所有适用 reference 编译进 `seedance_generation_package`。

The internal package must be self-contained. Every shot explicitly binds product and creator asset IDs, product state, scene, lighting, exposure, camera framing, lens feel, movement start and end, physical action chain, spoken line, audio behavior, text behavior and continuity. The video tool should not need to infer these controls from a short generic sentence.

内部生成包必须自包含。每一镜都明确绑定商品和达人素材 ID、商品状态、场景、光源与曝光、构图与焦段、运镜起止、物理动作链、口播、声音、文字和连续性，不让视频工具从泛化短句中自行补全关键控制。

Show the full internal package only when the user explicitly asks for the Seedance prompt, detailed model instructions, or video-tool payload.
