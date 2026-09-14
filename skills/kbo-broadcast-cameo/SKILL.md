---
name: kbo-broadcast-cameo
display_name: KBO转播客串
description: 生成用户本人出现在韩国KBO棒球联赛MBC Sports+转播观众席的仿真直播截图与15秒直播片段，包含真实转播UI、韩文字幕条、现场解说与氛围音。触发场景：用户希望制作自己"客串"体育赛事直播的趣味视频/图片，提供个人照片与播报称谓即可生成。
tools: ["sandbox_generate_image", "render_video", "sandbox_generate_video", "sandbox_process_video"]
---

# KBO转播客串生成器

## 1. 核心原则 + 持久引擎

以真实韩国棒球联赛转播的"观众席切镜"为核心范式，通过高度还原的转播UI、现场氛围与自然人物动作，制造"我真的出现在职业赛事直播中"的真实感与趣味性。身份相似度是第一优先级，转播质感是第二优先级，自然表演是第三优先级。

持久引擎(因果链):
**[用户本人照片+播报称谓] -> [身份严格保留] -> [真实转播场景植入] -> [自然非表演感动作] -> [完整转播UI+音轨] -> [以假乱真的直播片段] -> [趣味传播/社交分享价值]**

## 2. 质量测试（可证伪）

1. 静态截图中，人物面部特征与参考照片相似度达到90%以上，无面部结构变形，亲友可一眼认出；
2. 转播UI完全符合MBC Sports+ KBO直播真实样式，无AI生成的乱码文字，比分条、台标、名字条位置正确；
3. 15秒视频中人物动作自然松弛，无夸张表演，全程保持身份一致性，无镜头切换、无角度变化、无UI动画；
4. 音轨包含韩语解说、现场观众噪音、 vendors叫卖声，无背景音乐，完全匹配真实直播听感。
以上四条任一不满足则判定为不合格，需重新生成。

## 3. 输入诊断（生产前必须确认）

### 前置必填检查（缺一则终止流程，等待用户补充，不得使用默认值）
1. **本人参考图**：清晰的正面自拍照或头像，用于保留面部特征，无过度遮挡、无强滤镜；
2. **播报称谓**：将出现在转播名字条上的完整文字（例如："VaVa - Flova AI Creator"），直接替换模板中所有[NAME]占位符，不得虚构。

### 固定参数（无需用户确认，技能内置）
- 赛事：KBO韩国棒球联赛 LG Twins vs Doosan Bears 常规赛
- 场馆：首尔蚕室综合运动场棒球场
- 转播方：MBC Sports+
- 比分：LG 3-1 Doosan，7局上半
- 画幅：16:9横屏
- 截图分辨率：2K
- 视频分辨率：720p，时长15秒，一镜到底无剪辑
- 语言：所有Prompt使用英文撰写，解说音为韩语，UI文字为韩语转播样式
- 合规：无敏感内容，属于趣味二创，不涉及商业侵权

## 4. 路由表

| 输入特征 | 选用路线 |
|---|---|
| 用户提供合格参考图+播报称谓 | 标准双阶段生成流程（先图后视频） |
| 参考图面部模糊/遮挡/多人 | 提示用户更换清晰单人正面照后再继续 |
| 用户对截图人物相似度不满意 | 重新生成静态截图，不进入视频阶段 |
| 用户对最终视频效果不满意 | 保留已确认的截图作为首帧，重新生成视频 |

## 5. 工作流（严格按顺序执行，不得跳过暂停节点）

### 阶段1：前置校验
- 检查用户是否已上传清晰本人正面参考图；
- 检查用户是否已提供播报称谓文字；
- 任一缺失则立即告知用户补充，不得使用默认值、不得虚构内容。

### 阶段2：生成静态转播截图（暂停节点，必须等用户确认）
1. 使用参考图生图能力，绑定用户上传的本人照片作为身份参考；
2. 分辨率设置为2K，画幅16:9；
3. Prompt严格使用下方「图像Prompt模板」，将[NAME]替换为用户提供的播报称谓；
4. 生成完成后立即向用户展示截图，明确等待用户确认："请确认截图中人物相似度是否满意，满意后将继续生成视频，不满意可重新生成截图"；
5. **必须等用户明确确认满意后，方可进入阶段3**，不得自动推进。

### 阶段3：生成15秒转播视频
1. 使用多模态生视频能力，双参考输入：
   - 参考1（首帧参考）：阶段2用户已确认的静态截图
   - 参考2（身份参考）：用户上传的原始本人照片
2. 分辨率设置为720p，时长15秒，开启音频生成；
3. Prompt严格使用下方「视频Prompt模板」，将[NAME]替换为用户提供的播报称谓；
4. 15秒视频一次生成完整成片，无需分段拼接。

### 阶段4：交付与迭代
1. 向用户展示最终15秒视频；
2. 提供两个选项：① 确认满意，交付最终产物；② 不满意，说明问题后重新生成（若人物相似度问题则回到阶段2，若动作/音轨问题则直接重生成视频）。

## 6. Prompt模板（严格使用，不得随意修改核心要素）

### 图像Prompt模板（英文撰写，绑定用户参考图）
```
A screenshot from a live KBO (Korea Baseball Organization) game TV broadcast on MBC Sports+. The camera cuts to the audience — the reference image person is one of the audience sitting between, sitting and smiling naturally, unaware they're on camera. The subject is sitting in the rows of the stands at Jamsil Baseball Stadium in Seoul, South Korea. **Hardlock: do not alter their facial structure; strictly preserve their likeness from the reference image.** Full KBO broadcast overlay: static scorebug at the bottom showing LG Twins vs Doosan Bears regular season matchup, LG Twins leading 3–1 in the 7th inning; MBC Sports+ network logo watermark in the top-left corner; 16:9 aspect ratio. Above the scorebug, a clean broadcast name graphic in Korean broadcast style reads: "[NAME]", white text on a semi-transparent dark bar, styled like a real KBO broadcast identifier. The image looks exactly like a real Korean TV sports broadcast screenshot — broadcast color grading, slight compression artifacts, interlacing grain, Korean UI typography. All on-screen graphics are completely static, no animation.
```

### 视频Prompt模板（英文撰写，双参考绑定：已确认截图为图1，原始参考图为图2）
```
A realistic live KBO broadcast shot of the subject sitting in the front stands at Jamsil Baseball Stadium, Seoul, during an LG Twins vs Doosan Bears regular season game. The shot feels like a real TV cutaway when the MBC Sports+ broadcast camera finds a notable guest in the crowd. Preserve the subject's identity and likeness from the reference images throughout the entire clip.

The subject is seated in the stadium stands, smiling naturally and not over-performing for the camera. Not locked into eye contact with the lens — they occasionally glance toward the field, then toward the camera, then back toward the field.

One continuous take. No cuts. No angle changes.

Action sequence: They smile casually in their seat as the camera lands on them, looking around naturally. They then give a relaxed, natural wave toward the camera — the crowd around them cheers and reacts. They glance up toward the scoreboard above the outfield wall, then look back at the camera. They cheer briefly with visible excitement reacting to the on-field action, then turn to say something to the person beside them and laugh — we don't hear them speak. They finish by clapping naturally while smiling. All movement is subtle, believable, and human. No exaggerated acting. No direct talking to camera.

Broadcast style: real live Korean sports TV broadcast look, telephoto broadcast camera feel, natural outdoor stadium lighting under evening lights, slight broadcast compression, slight interlacing / TV grain, authentic crowd movement in background, Korean baseball stadium atmosphere with LG Twins and Doosan Bears fan sections visible. Subject remains in their stadium seat for the full 15 seconds.

On-screen graphics: static bottom scorebug showing LG Twins vs Doosan Bears KBO regular season layout — completely unchanged for the entire 15 seconds, no animation, no score updates, LG Twins leading 3–1 in the 7th inning. MBC Sports+ logo watermark top-left corner. Above the scorebug, broadcast name graphic reads: "[NAME]" — Korean broadcast style, white text on semi-transparent dark bar, present for the full duration.

{Two male KBO broadcast commentators in Korean, casual and warm tone: "[NAME] 씨가 오늘 잠실 구장을 찾아주셨습니다. 7회 접전이 펼쳐지는 가운데 관중석에서 LG와 두산의 명승부를 직접 지켜보고 계시네요. 팬들의 뜨거운 응원에 [NAME] 씨도 함께 즐기고 계신 것 같습니다."} <natural baseball stadium crowd noise, vendor sounds, and ambient stadium atmosphere throughout>

no music, no subtitles, no scene cuts, no angle changes, no scorebug animation or updates, no exaggerated gestures, no constant direct eye contact with camera, no talking to camera
```

## 7. 静默自检（出稿前内部检查，不展示给用户）
- [ ] 已确认用户提供了清晰本人参考图，无遮挡、无多人；
- [ ] 已确认用户提供了播报称谓，未使用默认值或虚构内容；
- [ ] 静态截图生成后已暂停，等待用户确认相似度，未自动推进；
- [ ] 视频生成时双参考图绑定正确：已确认的截图为首帧，原始照片为身份参考；
- [ ] Prompt中所有[NAME]占位符已完全替换为用户提供的称谓，无残留；
- [ ] 视频参数正确：720p、15秒、一镜到底、无剪辑、开启音频；
- [ ] 所有生成Prompt为英文，无中英混杂；
- [ ] 视频音轨包含韩语解说+现场氛围音，无背景音乐；
- [ ] 全程无镜头切换、无角度变化、UI全程静态无动画；
- [ ] 人物动作自然松弛，无夸张表演、无直视镜头说话。
