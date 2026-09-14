# 视频 Prompt 文法

> 这些是可适配的模式与句式，按场景改写，不要逐字照搬。

本文件定义视频生成Prompt的完整文法、模板和负向约束写法，供Prompt层在阶段10构建视频Prompt时遵循。

## 核心原则

- Prompt必须保留所有已确认要素：小猫身份锚点、职业身份、工作场景、职场梗、每段小猫动作、镜头语言、首尾衔接。
- **不得新增未确认的职业、场景、人物、道具、字幕或Logo。**
- 职场梗必须通过画面行为表现，不能只写"表现职场梗"。
- 使用正向措辞描述画面，负向约束统一放在末尾。

## 小猫身份锚点写法

每个Prompt必须包含以下身份锁定语句：

```
严格参考 [Cat_Main]，保持同一只小猫的毛色、花纹、脸型、眼睛、耳朵、体型比例、神态和可识别表情；不得换猫，不得变成人，不得改变毛色和花纹。
```

## 职业场景写法

必须写清楚职业环境和道具。例如：

- **程序员猫**：夜晚办公室工位、电脑蓝光、键盘、咖啡杯、代码屏幕。
- **设计师猫**：设计桌、手绘板、色卡、参考图墙、修改意见便签。
- **咖啡店员猫**：咖啡机、外带杯、收银台、围裙、奶泡壶。
- **老板猫**：老板椅、会议桌、报表、大屏、茶杯。
- **客服猫**：大耳机、电脑屏幕、聊天窗口、工单系统。
- **医生猫**：诊室、白大褂、听诊器、病例夹、药柜。
- **老师猫**：讲台、黑板、粉笔、作业本、教案。
- **厨师猫**：厨房料理台、锅、围裙、食材、厨师帽。
- **主播猫**：补光灯、手机支架、麦克风、弹幕屏、商品台。
- **摄影师猫**：相机、三脚架、灯架、反光板。
- **保安猫**：岗亭、监控屏、对讲机、制服、登记本。
- **便利店店员猫**：收银台、货架、扫码枪、关东煮、饭团。
- **办公室白领猫**：办公桌、电脑、文件夹、会议室、打印机。
- **律师猫**：律所办公室、文件柜、合同、法典、会议桌。

## 职场梗写法

职场梗必须通过画面动作表现。不要只写"表现职场梗"。

**正确写法示例：**

> "小猫爪子拍在键盘上，屏幕弹出一排报错，旁边三杯咖啡，猫眼逐渐放空。"

> "小猫坐在会议桌尽头，爪子压在报表上，身后的屏幕显示上升箭头，表情严肃得像在画饼。"

> "小猫认真打奶泡，奶泡从杯子里溢出来流到吧台上，小猫一脸无辜地看着镜头。"

**错误写法示例：**

> ~~"表现程序员改bug的职场梗"~~

> ~~"画面中有职场梗元素"~~

## 视频Prompt完整模板

```
严格参考 [Cat_Main]，保持同一只小猫的毛色、花纹、脸型、眼睛、耳朵、体型和神态。当前职业是 [Profession_Main]，场景为 [Workplace_Main]。画面中小猫正在进行 {具体工作动作}，使用 {职业道具}，体现 {职场日常/职场梗}。镜头采用 {景别与运镜}，光影为 {职业场景光线}，小猫表情为 {困/无辜/严肃/崩溃/得意}。动作按时间推进：先 {动作1}，然后 {动作2}，最后 {动作3或pose}。结尾为下一镜头预留 {动作/道具/镜头方向}。
负向约束：no cat identity drift, no different cat, no human transformation, no wrong fur color, no wrong fur pattern, no extra cat, no random person, no animal abuse, no dangerous injury, no blood, no horror, no random text, no watermark, no unauthorized logo, no profession mismatch, no distorted cat face, no missing limbs, no extra limbs, no subtitles unless requested.
```

## beat 填充指引

每个15s片段的Prompt内按时间轴组织beat：

```
0-2s: {职业钩子建立——小猫身份+职业身份第一眼可辨}
2-3s: {视觉重点推进——第一个动作或场景展开}
3-5s: {工作日常铺垫——小猫开始干这个职业的活}
5-7s: {职场梗铺垫——梗点或冲突酝酿}
7s: {笑点/高潮——第一次笑点、梗点、职业名场面或情绪高潮}
7-10s: {情绪延续——高潮后的反应或升级}
10-12s: {第二波梗——新的职场日常或第二个梗点}
12-14s: {情绪升级——崩溃、摸鱼、犯困或得意}
14-15s: {名场面定格——可截图传播的打工猫名场面，为下一段预留接口}
```

## 负向约束（完整版）

每个Prompt末尾必须附加以下负向约束：

```
no cat identity drift, no different cat, no human transformation, no wrong fur color, no wrong fur pattern, no extra cat, no random person, no animal abuse, no dangerous injury, no blood, no horror, no random text, no watermark, no unauthorized logo, no profession mismatch, no distorted cat face, no missing limbs, no extra limbs, no subtitles unless requested.
```

## 视频生成方式说明

- **≤15s的片段**：用一次视频生成即可拿到完整成片。上述beat（0-2s/3s/7s等）是同一次生成内部的时间轴描述，不需要分段多次生成。
- **>15s的成片**：拆成多个≤15s片段分别生成，再做后处理拼接。
- 每个Storyboard Shot对应一次视频生成。

## 完整Prompt示例（程序员猫·15s片段）

```
严格参考 [Cat_Main]，保持同一只小猫的橘色短毛、额头M形条纹、圆脸、黄绿色大眼睛、立耳和微胖体型。当前职业是程序员猫，场景为深夜办公室工位。画面中小猫正在进行深夜加班改bug的工作，使用双屏电脑、键盘和咖啡杯，体现需求又改了、代码跑不起来的职场梗。镜头采用中景平视缓推转特写俯视转近景平视，光影为蓝色屏幕光为主光源配红色报错光对比，小猫表情从专注变为呆滞再变为崩溃。动作按时间推进：先端坐工位前爪搭键盘盯屏幕，然后爪子拍键盘屏幕弹出红色报错框猫眼放空，最后趴在键盘上旁边三杯咖啡。结尾为下一镜头预留趴在键盘上的姿势和深夜办公室环境。
负向约束：no cat identity drift, no different cat, no human transformation, no wrong fur color, no wrong fur pattern, no extra cat, no random person, no animal abuse, no dangerous injury, no blood, no horror, no random text, no watermark, no unauthorized logo, no profession mismatch, no distorted cat face, no missing limbs, no extra limbs, no subtitles unless requested.
```
