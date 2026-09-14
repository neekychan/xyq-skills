# xyq-skills

一个用于 **AI 短剧 / AI 视频生成 / Agent 工作流** 的 skills 合集仓库。

这里的 skills 不是可执行代码。它们是一套可直接被 Agent 平台（如 Qoder、AI Studio）加载的提示词工程文件、工作流配置和风格参考。每个 skill 通常包含一份 `SKILL.md`，说明这个 skill 能解决什么问题、输入输出是什么、应该怎么调用。

## 这个仓库能做什么

- 快速生成各种风格的 AI 短剧脚本、分镜、提示词。
- 给 AI 视频生成工具（如 Seedance、可灵、Runway、Pika 等）提供结构化提示词模板。
- 给 Agent 提供可复用的视频生产工作流，比如字幕、封面、剪辑、配音、转 Hyperframes。
- 作为个人或团队的 AI 视频生成知识库，方便沉淀和复用。

## 仓库结构

| 路径 | 内容 | 数量 |
|---|---|---|
| `skills/` | 短剧、风格化视频、营销视频、提示词模板等生成类 skills | 176 个 |
| `agents/skills/` | Agent 工作流、工具类 skills，包括字幕、Hyperframes、Remotion 转换等 | 28 个 |

## 适用场景

| 场景 | 对应 skill 示例 |
|---|---|
| 古风 / 神话短剧 | `3d-ancient-drama`、`chinese-mythology-style` |
| 港风 / 武侠 / 昭和动画等风格化视频 | `hongkong-noir-night-style`、`shaw-brothers-wuxia-style`、`tezuka-showa-cartoon-style` |
| 商品 / 品牌营销视频 | `story-commerce-video`、`brand-film-30s`、`marketing-video-creator` |
| AI 视频提示词优化 | `video_creation`、`expert-product-promotion` |
| 自动化字幕 / 封面 / 剪辑 | `embedded-captions`、`captions-overlay`、`remotion-to-hyperframes` |

## 怎么用

1. 克隆仓库：

```bash
git clone git@github.com:neekychan/xyq-skills.git
```

2. 按平台要求放到对应目录。

Qoder 示例：

```bash
# 短剧 / 视频生成 skills
cp -R xyq-skills/skills ~/.agents/skills

# Agent 工具 skills
cp -R xyq-skills/agents/skills ~/.agents/skills
```

AI Studio 示例：

```bash
cp -R xyq-skills/skills /path/to/your/agent/skills
cp -R xyq-skills/agents/skills /path/to/your/agent/skills
```

3. 刷新 Agent 平台，即可在对话或工作流中调用这些 skill。

## 来源

- `skills/`：主要来自 `skills_collection.zip` 短剧 / AI 视频生成 skill 合集。
- `agents/skills/`：来自 AI Studio Agent skills 集合，用于视频生产工作流。

## 注意事项

- 仓库内含字体、示例素材等二进制资源，工作区约 50 MB，完整克隆约 80 MB。
- 部分 skill 目录名包含空格，Windows 用户请注意路径兼容性。
- skill 内容会随 AI 模型和平台能力变化而持续更新，建议定期拉取最新版。

## 关键词

AI 短剧、AI 视频生成、Seedance、Qoder skills、Agent skills、短剧提示词、视频风格化、营销视频、Remotion、Hyperframes、AI Studio、视频工作流。
