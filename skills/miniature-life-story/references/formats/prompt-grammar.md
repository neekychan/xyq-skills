# 提示词语法规范

## 全局视觉风格基调（所有图像/视频必须包含）
所有资产须保持统一的「微缩模型摄影」美学：
- 移轴镜头浅景深，远景虚化明显，焦外呈奶油感圆形散景
- 材质感精致：布料纤维可见，木质纹理清晰，玻璃反光真实，人偶表面细腻不塑料
- 光线柔和漫射，避免硬阴影，整体氛围温暖治愈
- 禁止卡通/动漫/3D塑料感/黏土质感

## 图像提示词结构（四层组装，顺序不得颠倒）
### ① 主体描述
明确说明画面核心内容（人物、场景、道具），指定比例关系与尺寸感：
- 大道具必须标注尺寸对比，如"与人偶等高的咖啡杯"、"众多小人合力推动的信封"
- 角色描述需明确服装、发型、表情、动作
- 场景描述需包含空间结构、道具摆放、环境细节

### ② 微缩模型美学基调（每张图必须包含）
中文版本：
> 实拍风格的微缩世界场景，移轴摄影效果，浅景深，前景与远景轻微虚化，中间主体清晰，真实材质质感，高细节，超清摄影，自然光，柔和散景
英文版本（可选）：
> live-action style miniature world, tilt-shift photography, shallow depth of field, foreground and background softly blurred, subject in sharp focus, realistic material texture, highly detailed, ultra-sharp photography, natural light, soft bokeh

### ③ 光线与色调（按场景选用）
- 日间温暖/黄昏金光：温暖电影感光影，金色夕阳斜射，暖金色调，柔和丁达尔效应
- 清晨柔光：清晨漫射柔光，浅金色氛围，空气通透感
- 夜晚梦幻：柔和月光，温暖烛光，细小灯串散景，冷暖对比
- 室内精致：柔和顶光，奶油白环境光，窗边柔光，温馨居家氛围

### ④ 氛围收尾词（按需选用）
梦幻宁静氛围 / 温暖治愈感 / 电影感氛围 / cozy温馨感

## 角色参考图专用规范（16:9横版拼接图）
必须明确指定为16:9横版单张图，左右分区：
- **左侧（人脸大头照）**：left half: close-up portrait of [角色名] as a miniature figurine, [发型+发色], [服装上半身], delicate facial features, soft skin texture, sharp focus on face
- **右侧（全身三视图）**：right half: three-view full-body sheet of the same character — front view, side view, back view arranged horizontally, full costume including shoes, clear silhouette, same miniature figurine aesthetic
- **整体收尾**：single image, 16:9 aspect ratio, plain neutral background, 1:12 scale model aesthetic, highly detailed craftsmanship, no text labels

## 图像负向提示词（所有图像必须附加）
```
no subtitles, no text, no watermark, no harsh shadows, no blurry faces, no distorted proportions, no cartoon style, no anime style, no 3D plastic look, no clay texture, no giant human hands
```

## 视频提示词结构（四个区块，顺序不得颠倒）
### 区块一：全局视觉与美学基调（每条必须包含）
> 微距移轴摄影，微缩模型世界，浅景深，焦外奶油散景，[具体色调描述，如"温暖金黄漫光，奶茶色调，窗边柔光形成轻微丁达尔效应"]，精致手工质感，非写实非动漫，材质真实细腻

### 区块二：人物与场景资产锚定
逐一声明参考图对应的资产身份，顺序与传入的图片顺序一致：
```
<<<image_1>>> 作为主角[角色名]，[简要体态/服装/情绪状态描述]
<<<image_2>>> 作为配角[角色名]，[简要体态描述]
<<<image_3>>> 作为场景背景[场景名]，[光线/空间氛围说明]
```
末尾必须加尺寸对比锚定句：凡涉及大于人偶身体的道具，标注"众多人偶合力操作"，突出尺寸落差（如"巨大的咖啡杯盖"、"与人偶等高的信封"）。

### 区块三：剧本与动作时间线
按时间段拆分镜头内容，每段包含三个子项：
```
[00.0s - XX.Xs]
- 镜头机位：[景别 + 运镜，如：近景，缓慢推进]
- 视觉画面：
  - [前景]：[失焦前景元素，如道具边缘、人偶轮廓]
  - [主体]：[焦点内的核心动作，必须指定具体角色，禁止"有人/某人"]
  - [背景]：[虚化背景氛围，如温暖光斑、模糊场景细节]
- 听觉声效：[环境音 + 动作音效描述；如有对白用{对白内容}格式标注，音效用<音效描述>格式]
```
- 时间段划分对齐分镜规划时长（4s-10s），段落数量1-3段
- **旁白严禁写入视频prompt**：旁白必须单独生成作为独立音频轨道，prompt末尾必须附加`no music, no narration`

### 区块四：生成约束与负向提示词
**固定负向（每条必须包含）**：
```
no subtitles, no text overlay, no watermark
no music, no background music, no narration, no voiceover
no fast cuts, no shaky camera
no cartoon style, no anime style, no 3D plastic look, no clay feel
no oversized human hands, no giant figures inconsistent with miniature scale
no floating objects, no glowing props, no physically impossible actions
```
**按镜头追加（如适用）**：
- 无角色镜头：`no human figures`
- 纯特写镜头：`no wide-angle distortion`
- 夜间场景：`no overexposed highlights`

## 镜头语言词库
| 效果 | 描述词 |
|---|---|
| 缓慢推进 | slow push-in, camera gently moves closer |
| 轻微横摇 | slow pan right/left, gentle horizontal sweep |
| 俯拍全景 | top-down overhead shot, bird's-eye view of miniature world |
| 跟随移动 | smooth follow shot, tracking the character gently |
| 锁定定镜 | static lock-off, camera holds still |
| 微微仰拍 | low-angle shot, slight upward tilt |
