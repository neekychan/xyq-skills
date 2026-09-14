# Compact Brand Film Spec Output

Use this reference when a brand-film response would otherwise become long, mixed-language, or overloaded with strategy notes. The goal is to create a good conversation experience while preserving a full-quality Seedance 2.5 `Video Prompt`.

## Output Split

Separate the deliverable into three layers:

1. **Conversation summary**: short user-facing answer in the user's primary language.
2. **Complete creative plan markdown**: readable strategy, route, production logic, and risk checks.
3. **Seedance 2.5 Video Prompt**: paste-ready generation prompt, never weakened by the compact chat format.

Default behavior:

- When the user provides a concrete brand, product, campaign, category, or visual brief and asks for a brand film, TVC, campaign film, brand story, product promotion film, route, storyboard prompt, or Seedance/video-generation prompt, create a readable standalone Brand Film Spec markdown file by default.
- Do not create a spec file only when the user explicitly asks for a fast prompt, a short chat-only answer, no file creation, or strategy-only guidance.
- In chat, show only the big idea summary, the complete creative plan path, the final planned prompt, and the generation consent line.
- Put detailed diagnosis, assumptions, rejected routes, category notes, trend reasoning, originality checks, and risk checks in the spec markdown instead of the conversation.
- If the user asks for multiple routes, show a compact route table in chat and put full route specs in the markdown. Each selected route still needs a usable Seedance 2.5 prompt unless the user asks for strategy only.
- If no file can be created, include a compact `Brand Film Spec` block before the prompt, keep it under the minimum needed fields, and briefly say that a standalone spec could not be created.

## Language Rule

Use one primary language per deliverable. The final chat response must follow the user's primary input language, including the route summary, spec path sentence, field labels, and `video_generation_prompt`, unless the user explicitly requests another target language or market.

- If the user writes in Chinese, write the chat response, spec, and Seedance prompt in Chinese by default.
- If the user writes in English, write the chat response, spec, and Seedance prompt in English by default.
- Keep only brand names, product names, platform names, model names, and widely recognized style references in their original language.
- Avoid mixed field labels like `Brand`, `Category tension`, `Script beats`, or `Video Prompt` inside an otherwise Chinese deliverable. Use `品牌`, `品类张力`, `分镜节奏`, and `video_generation_prompt`.
- If the target market requires English, write the entire chat deliverable, spec, and prompt in English and do not mix Chinese beat labels into it.

## Spec Markdown Template

Create a standalone markdown file named with a short brand, product, or campaign slug by default for concrete brand-film or prompt-generation tasks. The file should be readable for humans, not only optimized for video models.

```markdown
# Brand Film Spec - {品牌/项目名}

## 结论
- 推荐路线：
- 商业类型 / 制作方式：
- 表达形式：
- 一句话品牌创意：
- 观众记忆点：

## 背景与判断
- 品牌 / 产品：
- 品类：
- 假设人群：
- 品牌阶段：
- 传播目标：
- 品类张力：
- 文化时机：
- 品牌资产：
- 产品真相：

## 电影化路线
- 电影类型：
- 风格参考：
- 风格关键词：
- 打光逻辑：
- 视觉想法：
- 品牌世界：
- 主体 / 主角：
- 产品 / 品牌叙事功能：
- 运动脊柱：
- 最终品牌句：

## 30秒节奏
- 0-3秒：
- 3-8秒：
- 8-14秒：
- 14-21秒：
- 21-27秒：
- 27-30秒：

## 制作控制
- 镜头：
- 剪辑：
- 光线：
- 色彩：
- 声音 / BGM：
- 品牌或产品露出：
- 横竖屏判断：

## 原创性与风险
- 独特开场：
- 品牌视觉代码：
- 产品后果：
- 一眼记忆：
- 风险规避：

## Seedance 生成注意
- 画面必须证明：
- 风格必须保留：
- 商品 / 品牌出现时刻：
- 品牌名或品牌句口播：
- 生成控制：
```

## Chat Summary Template

Use this compact chat shape after creating or referencing the complete creative plan markdown. Do not use the word `spec` in user-facing Chinese chat unless the user uses it first. For Chinese users, call the file `完整创意方案` or `品牌片方案稿`.

大的思路总结：
{用 2-4 句话说明核心创意、为什么这样拍、品牌 / 产品怎么起作用。不要堆 bullet point，不展开完整推导。}

完整创意方案可见：
{relative_path}

这是为你规划好的 prompt：
```text
{paste-ready Seedance 2.5 prompt}
```
你说“同意生成”，我就直接为你开拍。



If the user only asks for strategy, do not fabricate a prompt. Explain the split and apply the spec template only as far as the request needs.

## Prompt Quality Guard

Compact chat output must not remove these Seedance prompt requirements:

- `时长：30秒，比例：16:9。` by default for cinematic brand films, unless the user asks for vertical/social-first.
- one task type: generate, reference, edit, extend, or stitch.
- `风格与视觉参考`, `场景`, `主体`, and `各个分镜的具体内容`.
- one primary style reference or coherent style family with camera, lighting, color/material, texture, editing rhythm, and sound motif translated into production detail.
- stable labels such as `品牌1`, `产品1`, `主体1`, `场景1`.
- 5-6 timestamped beats for 30-second films unless the user changes duration.
- beat fields in the selected language, with camera first: `拍法`, `画面内容`, optional `品牌/产品露出`, and `声音`.
- motion spine or continuity device reflected in the beats.
- product proof or brand mechanism visible before the final brand line.
- final brand mnemonic: visual lockup, readable brand/product, spoken brand name or brand line when appropriate, and sonic cue.
- positive generation guidance only in the final prompt.

The complete creative plan can be concise; the final planned prompt cannot be vague.
