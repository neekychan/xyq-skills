# 输出模式（Output Patterns）

当技能需要产出一致、高质量的输出时，使用这些模式。

## 模板模式（Template Pattern）

为输出格式提供模板。让严格程度与你的需要相匹配。

**对于严格要求（如 API 响应或数据格式）:**

```markdown
## 报告结构

始终使用这个精确的模板结构:

# [分析标题]

## 执行摘要
[关键发现的一段式概述]

## 关键发现
- 发现 1，附支撑数据
- 发现 2，附支撑数据

## 建议
1. 具体可执行的建议
2. 具体可执行的建议
```

**对于灵活指引（当适应性有用时）:**

```markdown
## 报告结构

这里是一个合理的默认格式，但请运用你的判断:

# [分析标题]

## 执行摘要
[概述]

## 关键发现
[根据你的发现调整各节]

## 建议
[针对具体情境量身定制]
```

## 示例模式（Examples Pattern）

对于输出质量依赖于看到示例的技能，提供输入/输出对:

```markdown
## 提交信息格式

按照以下示例生成提交信息:

**示例 1:**
输入: Added user authentication with JWT tokens
输出:
feat(auth): implement JWT-based authentication

Add login endpoint and token validation middleware

遵循这种风格: type(scope): 简短描述，然后是详细说明。
```

相比单纯的描述，示例能让 agent 更清晰地理解所期望的风格和细节程度。
