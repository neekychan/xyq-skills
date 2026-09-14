# xyq-skills

短剧、AI 视频生成与 Agent 工作流 skills 合集。

本仓库主要面向支持 `.agents/skills` 或 `agents/skills` 结构的 Agent 平台（如 Qoder、AI Studio）。

## 目录结构

| 路径 | 说明 | 数量 |
|---|---|---|
| `skills/` | 短剧、风格化视频、营销视频等生成类 skills | 176 个 |
| `agents/skills/` | Agent 工作流、工具类 skills | 28 个 |

## 使用方式

1. 克隆仓库：

```bash
git clone git@github.com:neekychan/xyq-skills.git
```

2. 根据平台要求，把 `skills/` 或 `agents/skills/` 放到对应目录。

Qoder 示例：

```bash
# 短剧/视频生成 skills
cp -R xyq-skills/skills ~/.agents/skills

# Agent 工具 skills
cp -R xyq-skills/agents/skills ~/.agents/skills
```

3. 重启或刷新 Agent 平台，即可加载 skills。

## 来源

- `skills/`：主要来自 `skills_collection.zip` 短剧 skill 合集。
- `agents/skills/`：来自 AI Studio Agent skills 集合。

## 注意事项

- 仓库内包含字体、示例素材等二进制资源，工作区约 50 MB，完整克隆约 80 MB。
- 部分 skill 目录名包含空格，在 Windows 环境使用时请注意路径兼容性。
