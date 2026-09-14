# Compact Spec Output

Use this reference when a story-commerce response would otherwise become long, mixed-language, or overloaded with strategy notes. The goal is to keep the chat concise while preserving the full reasoning needed to write a strong Seedance 2.0 prompt.

## Output Split

Separate the deliverable into three layers:

1. **Conversation summary**: short user-facing answer in the user's language.
2. **Story Commerce Spec markdown**: full reasoning, route choice, proof chain, and risk checks.
3. **Seedance 2.0 prompt**: paste-ready video-generation prompt, never weakened by the compact chat format.

Default behavior:

- When the user provides a concrete product and asks for creative concepts, story-commerce scripts, plot-led short videos, storyboard prompts, or Seedance video-generation prompts, create a readable Story Commerce Spec markdown file by default.
- Do not create a spec file only when the user explicitly asks for a fast prompt, a short chat-only answer, no file creation, or strategy-only guidance.
- Choose the output path before writing: default to `/workspace/projects/{project_name}_creative_plan.md`; when the task has uploaded/source assets or will produce asset files, use `/workspace/assets/{project_name}/creative_plan.md`.
- Build `{project_name}` in Chinese when the user's primary language is Chinese: use the user's product/brand name plus the chosen short-drama route or concept direction, such as `歪马送酒_饭局救场反转` or `小云雀_重生效率反杀`. Keep brand names, product names, and widely recognized English names in their original form when that is how the user provided them.
- Write the selected output path with `sandbox_write` before the final chat response. If `sandbox_write` is unavailable or fails, include a compact `Story Commerce Spec` block before the prompt and briefly say that the standalone file could not be created.
- In chat, show only the route summary, the spec markdown link, and the final `video_generation_prompt`.
- The spec path shown in chat must be a Markdown link, not a bare path. Use Chinese-readable link text such as `[完整创意方案]({absolute_path})` or `[短剧带货完整方案]({absolute_path})` so the user sees clickable blue text. If the path contains spaces or special characters, wrap the URL target in angle brackets, for example `[完整创意方案](</workspace/projects/my project_creative_plan.md>)`.
- Put detailed diagnosis, alternatives, route rejection, category notes, and checklist reasoning in the spec markdown instead of the conversation.
- If the user asks for multiple routes, show a compact route table in chat and put full route specs in the markdown.
- If no file can be created, include a compact `Story Commerce Spec` block before the prompt, but keep it under the minimum needed fields and briefly say that a standalone spec could not be created.

## Language Rule

Use one primary language per deliverable. The final chat response must follow the user's primary input language, including the route summary, spec path sentence, field labels, and `video_generation_prompt`, unless the user explicitly requests another target language or market.

- If the user writes in Chinese, write the spec and Seedance prompt in Chinese by default.
- If the user writes in English, write the chat response, spec, and Seedance prompt in English by default.
- Keep technical labels Chinese: `产品`, `人群`, `戏剧类型`, `爽点`, `可见证明`, `分镜`, `声音`.
- Keep only product names, brand names, platform names, and model names in their original language.
- Avoid mixed field labels like `Product proof`, `Script beats`, `Visual baseline` inside a Chinese deliverable. Use `产品证明`, `脚本节奏`, `视觉基调`.
- If the target market requires English, write the entire prompt in English and do not mix Chinese beat labels into it.

## Spec Markdown Template

Create a standalone markdown file named with a short product or campaign slug by default for concrete product-led creative or prompt-generation tasks. The file should be readable for humans, not only optimized for video models.

```markdown
# 短剧带货 Spec - {产品/项目名}

## 结论
- 推荐戏剧类型：
- 内容路线：
- 一句话创意：
- 观众记忆点：

## 商品与人群
- 产品真相：
- 目标人群：
- 购买/使用场景：
- 核心顾虑：

## 戏剧结构
- 3秒钩子：
- 施压关系：
- 错误判断：
- 压力锁：
- 主角隐藏选择：
- 产品剧情功能：
- 爽点：
- 可见证明：
- 见证者反应：
- 转化句：

## 角色与视觉
- 主体1：
- 反派1：
- 关键见证者：
- 视觉参考：
- 借用维度：
- 场景：

## 15秒节奏
- 0-3秒：
- 3-7秒：
- 7-12秒：
- 12-15秒：

## Seedance 生成注意
- 画面必须证明：
- 商品出现时刻：
- 商品名口播：
- 风险规避：
```

## Chat Summary Template

Use this compact chat shape after creating or referencing the spec markdown:

```text
我会用「{戏剧类型} / {内容路线}」来写，因为它能让产品承担「{产品剧情功能}」，不是普通道具。

完整创意方案可见：[完整创意方案]({absolute_path})

video_generation_prompt:
{paste-ready Seedance 2.0 prompt}
```

If the user only asks for strategy, do not fabricate a prompt. Explain the split and offer the template or apply it to the skill.

## Prompt Quality Guard

Compact output must not remove these Seedance prompt requirements:

- `时长：15秒，比例：9:16。`
- one task type: generate, reference, edit, extend, or stitch
- stable labels such as `产品1`, `主体1`, `反派1`
- distinct visible character designs
- concrete visual reference and borrowed dimensions
- 3-4 timestamped shots for 15 seconds
- beat fields in the selected language, with camera first
- product visible before conversion
- spoken product name at least once
- unified dialogue language

The spec can be compact; the final prompt cannot be vague.
