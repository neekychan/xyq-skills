# 渐进式披露模式（Progressive Disclosure Patterns）

把 SKILL.md 正文控制在精要范围、保持在 500 行以内，以尽量减少上下文膨胀。当接近这个上限时，把内容拆分到独立文件中。在把内容拆分到其他文件时，始终在 SKILL.md 中引用它们，并清楚说明何时去读它们，以便技能的读者知道它们存在以及何时使用。

**关键原则:** 当一个技能支持多种变体、框架或选项时，在 SKILL.md 中只保留核心工作流和选择指引。把各变体特有的细节（模式、示例、配置）移到独立的参考文件中。

**模式 1:高层指南配合 references**

```markdown
# PDF 处理

## 快速开始

用 pdfplumber 提取文本:
[代码示例]

## 高级功能

- **表单填写**: 完整指南见 FORMS.md
- **API 参考**: 所有方法见 REFERENCE.md
- **示例**: 常见模式见 EXAMPLES.md
```

agent 只在需要时才加载 FORMS.md、REFERENCE.md 或 EXAMPLES.md。

**模式 2:按领域组织**

对于涉及多个领域的技能，按领域组织内容，以避免加载无关的上下文:

```
bigquery-skill/
├── SKILL.md (概览与导航)
└── references/
    ├── finance.md (营收、计费指标)
    ├── sales.md (商机、销售管道)
    └── product.md (API 使用、功能)
```

当用户询问销售指标时，agent 只读取 sales.md。

**模式 3:条件式细节**

展示基础内容，链接到高级内容:

```markdown
# DOCX 处理

## 创建文档
用 docx-js 创建新文档。见 DOCX-JS.md。

## 编辑文档
对于简单编辑，直接修改 XML。

**对于修订（tracked changes）**: 见 REDLINING.md
**对于 OOXML 细节**: 见 OOXML.md
```

agent 只在用户需要这些功能时才读取 REDLINING.md 或 OOXML.md。

**重要准则:**

- **避免深层嵌套的引用** - 让 references 距 SKILL.md 保持一层深度。
- **为较长的参考文件加结构** - 对于超过 100 行的文件，在顶部包含一个目录（table of contents），以便 agent 在预览时能看到完整范围。
