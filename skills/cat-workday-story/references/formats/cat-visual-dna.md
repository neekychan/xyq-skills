# 小猫视觉DNA分析规范

> 这些是可适配的模式与句式，按场景改写，不要逐字照搬。

本文件定义多模态分析小猫照片时的分析维度和输出JSON规范，供分析层在阶段1使用。

## 输入检查

- 必须至少存在一张小猫照片。
- 若上传多张猫图，必须判断：同一只猫 / 不同猫 / 同一只猫不同角度 / 姿势参考 / 场景参考 / 无关图片。
- 若图片中包含多只猫，必须标注主角候选并要求用户确认 [Cat_Main]。
- 若无小猫照片，立即终止流程。

## 分析维度

### 毛色与花纹
- 毛色：橘猫、狸花、三花、奶牛、黑猫、白猫、银渐层、布偶、暹罗等。
- 花纹位置：额头、鼻梁、脸颊、胸口、四肢、尾巴。
- 毛发长度：长毛、短毛、中长毛。

### 脸部特征
- 脸型：圆脸、尖脸、扁脸、长脸。
- 眼睛：颜色、形状、大小、神态。
- 耳朵：大小、朝向、折耳/立耳、耳尖颜色。

### 体型与姿势
- 体型：胖、瘦、圆润、幼猫、成年猫。
- 姿势：坐、趴、站、躺、抬爪、回头、盯镜头。

### 表情与神态
- 表情：高冷、困、无辜、委屈、警觉、呆萌、暴躁、严肃、好奇。
- 气质：整体给人的感觉描述。

### 身份锚点
- 身份锚点：最不能改变的识别特征。

## 职业适配分析

必须输出至少5个职业候选，每个包含：职业名称、适配理由、职场环境、职业梗潜力、反差萌点。

适配依据：神态是否像打工人、毛色气质是否适合某类职业、姿势是否适合该工作场景、是否适合佩戴职业服装或道具、适合的拟人化程度。

## 风险分析

必须输出以下潜在风险：
- 小猫脸部不清
- 毛色容易漂移
- 姿势不适合拟人化
- 道具遮挡小猫脸
- 职业服装遮挡识别特征
- 图片角度太特殊
- 多猫主体不明确
- 生成时可能变成卡通猫或人形猫

## 输出JSON Schema

最终输出必须为严格JSON对象，不附加解释。包含以下顶层字段：
- input_summary: has_cat_image, total_images, main_cat_candidate, need_user_confirmation
- cat_visual_dna: fur_color, fur_pattern, face_shape, eye_features, ear_features, body_type, pose, expression, identity_anchors
- cat_temperament_profile: personality_guess, workplace_persona_potential, comedy_potential
- profession_fit_candidates: 数组，每项含 profession, fit_reason, workplace_environment, daily_actions, workplace_gags, cat_reaction_potential
- workplace_environment_candidates: 数组
- prop_candidates: 数组
- anthropomorphic_level_suggestion: 轻拟人/中拟人/强拟人
- generation_risks: 数组
