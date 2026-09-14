---
name: fashion-bighead-sticker-prompt
display_name: 时尚大头贴提示词
description: 根据用户上传的人物或角色图片，生成一个高一致性的中文成品图片生成提示词，将原图角色转化为时尚大头贴纸风格头像。当用户上传人物/角色图片并要求生成头像提示词、人像 prompt、参考图改写、贴纸头像、大头照风格化、保留人物一致性出图提示词时触发此技能。当前默认风格为俏皮时髦的棚拍级大头贴纸头像，纯白背景，配半透明茶棕色复古墨镜、精致耳钉和活泼发饰。
tools: ["sandbox_generate_image"]
---

# Fashion Big-Head Sticker Avatar Prompt

This skill turns a user's uploaded reference image into a **directly usable Chinese image-generation prompt** for a stylized avatar transformation.

The goal is not to describe the image loosely. The goal is to produce a **high-constraint finished prompt** that protects identity consistency while converting the source character into a fashionable big-head sticker style.

## Use this skill when

Use this skill whenever the user wants to:

- turn an uploaded character image into a stylized avatar prompt
- keep strong identity consistency from a reference image
- make a sticker-style big-head portrait prompt
- rewrite a rough idea into a finished Chinese prompt for image models
- preserve the original person's age feel, facial identity, hair features, and recognition while changing styling
- generate a prompt for a white-background social avatar, sticker head, emoji-style portrait, or themed headshot

This skill currently defaults to a **playful, fashionable big-head sticker** treatment with pure white background and studio-quality portrait polish, but it should still work if the user phrases the request casually, such as:

- "把这张图做成头像提示词"
- "按上传图写一个大头贴 prompt"
- "保留本人特征，做贴纸头像"
- "给我一个适合出图的中文成品提示词"
- "把这张角色图改成牛仔帽大头照"

## Do not use this skill when

Do not use this skill for:

- pure image editing execution when the user wants you to directly modify the picture instead of writing a prompt
- video prompts
- poster copywriting or layout design
- generic text summarization
- cases where the user only wants a one-line style tag list instead of a finished prompt

## Core working principles

1. Treat the uploaded image as the **only identity reference**.
2. Preserve the subject's core recognizability before style.
3. Change styling without changing identity, age feel, or hair structure.
4. Output a prompt that is already usable, not a brainstorming note.
5. When the user's request is vague, keep the established default style rather than drifting into unrelated aesthetics.

## Default style definition

Unless the user explicitly asks for another direction, generate a prompt for this target:

- playful
- fashionable
- high-definition studio portrait quality
- big-head sticker avatar
- pure white background
- square 1:1 composition
- floating full head only
- transparent tea-brown retro sunglasses
- delicate gemstone or silver stud earrings
- lively colorful hair clips
- subtle soft floating shadow

## Required output structure

Always output in the following structure:

## 成品提示词
Write one complete Chinese finished prompt in polished natural language. It should be directly reusable in an image model.

## 负面提示词
List the key things that must not appear.

## 一致性控制要点
Summarize the identity-preservation logic in 3-6 bullets.

## 可调参数建议
Give a few optional tuning directions only if they are genuinely useful, such as making it cuter, more retro, or more photographic without breaking identity consistency.

## Prompt construction method

When writing the final prompt, make sure it covers these dimensions:

### 1) Identity anchor
Explicitly state that **[图片 1] is the only identity reference**.

### 2) Character consistency
Preserve as much of the subject's core recognition as possible, including where relevant:

- face shape
- facial proportion
- eye spacing
- eyebrow shape
- nose shape
- mouth shape
- ear contour
- skin tone
- hair color
- hairline
- hair length
- hair texture
- distinctive facial traits
- real age feel

For non-child subjects, adapt naturally: preserve the subject's original age presentation rather than forcing a childlike look.

### 3) Expression adjustment
If the user did not specify another expression, preserve the most vivid and interesting expression from the source image first. You may gently enhance its playful charm, but do not change the core emotional meaning.

Preferred direction:

- keep the original mood and facial intent
- make the expression slightly more lively, cheeky, and cute
- preserve the original spirit rather than replacing it with a generic smile

This enhancement should improve charm **without deforming facial features or weakening recognizability**.

### 4) Head-only transformation
Remove background, neck, shoulders, clothing, hands, body, and extra people. Keep only a complete floating head silhouette suitable for a sticker avatar.

If the source image is profile, candid, or off-angle, gently correct it toward an almost frontal view with the head vertically centered and the left-right structure naturally coordinated. Do not force perfect symmetry if doing so would alter identity.

Never crop:

- hair top
- ears
- chin
- head outline

### 5) Hair preservation
Hair must be preserved very carefully. Keep the original:

- hair color
- hairline
- core hairstyle features
- overall length logic
- recognizable silhouette

You may tidy the hair so it looks more fluffy, refined, and glossy with clearer strands, but do not massively change length, do not turn straight hair into exaggerated curls, and do not replace the hairstyle with a generic template.

### 6) Fashion accessories
Add a pair of retro fashionable semi-transparent tea-brown sunglasses with:

- rounded oval cat-eye silhouette
- transparent light-brown frame
- brown gradient lenses
- proportion appropriate to the subject's face size
- lenses that remain moderately transparent so the original eyes and gaze are still faintly visible

Never use fully opaque black lenses.

Add delicate small silver or colored gemstone stud earrings with restrained size and symmetrical placement. Do not generate oversized statement earrings.

On one side of the hair, add two or three small shiny colorful hair clips with pink, yellow, blue, or transparent crystal-like accents. The arrangement should feel lively and playful but not crowded, with clean tiny highlight sparkle.

All accessories must fit the subject's scale and sit in physically believable positions with correct occlusion against hair, ears, and face. They should enhance a retro-cool playful-child vibe without overpowering the identity.

### 7) Visual quality
Target:

- high-resolution commercial studio portrait look
- sharp but natural detail
- soft even front studio lighting
- reduced backlight issues, noise, blur, color cast, and uneven shadow from the source
- clean translucent skin texture with light healthy cheek warmth
- clear eyes, lips, teeth, and hair detail

Do not alter original tooth traits or add extra beauty features such as:

- braces
- tooth gems
- adult makeup

### 8) Composition and background
Use:

- 1:1 square composition
- head occupying the main visual area
- even breathing room around the silhouette
- clean pure white background
- complete and delicate edge extraction around the head
- no leftover background fragments or broken hair strands
- very soft subtle floating shadow

The result should feel suitable for social avatars, stickers, or emoji packs.

## Negative prompt logic

The negative prompt should strongly suppress these categories whenever relevant:

- neck, shoulders, torso, clothes, hands, body
- original environment or messy background
- identity drift
- age drift
- gender-expression drift
- skin tone drift
- template influencer face
- over-enlarged eyes
- nose shrinking
- face-shape distortion
- adult makeup
- braces
- tooth gems
- hats, necklaces, or unspecified accessories
- cartoon, illustration, toy, 3D doll, plastic skin
- cropped hair top, ears, or chin
- accessory misalignment
- warped glasses frame
- floating earrings
- hair clips merging into scalp
- duplicated facial features
- extra ears
- text, watermark, border, logos
- extra people
- other anatomy errors

## Adaptation rules

When the user's uploaded subject is not a child, do not force child wording. Rewrite the age-related instructions so they preserve the subject's real age presentation.

When the uploaded subject is not clearly human but is a stylized character, preserve the same identity logic: core facial structure, hair or head silhouette, distinguishing accessories, and recognizable traits should remain stable.

When a requested element would conflict with identity consistency, prioritize identity consistency first and write the prompt accordingly.

## Style guidelines for the final answer

- Write in Chinese.
- Output polished, finished wording rather than notes.
- Do not expose internal reasoning.
- Do not apologize unless something is actually missing.
- If the user gives extra style requirements, incorporate them while preserving the identity-control backbone.
- Keep protected placeholders byte-for-byte unchanged if they appear in user input.

## Example response skeleton

## 成品提示词
请以用户上传的[图片 1]作为唯一人物身份参考，……

## 负面提示词
不要生成……

## 一致性控制要点
- [图片 1] 是唯一身份参考
- 保留原始年龄感与核心五官比例
- 严格保留发型长度、发际线与卷直结构

## 可调参数建议
- 如果想更复古，可加强……
- 如果想更像商业棚拍，可增强……
