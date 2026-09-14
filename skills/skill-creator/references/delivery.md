# 交付技能给用户

当产出的技能通过 `quick_validate.py` 校验后，把它作为技能产物（skill artifact）交付给用户。

技能的原生形态是一个**目录**（`SKILL.md` + `references/`），但面向用户的交付物必须是单个文件。所以交付始终分两步:**把目录打包成 `/workspace/assets/<skill-name>.zip`，然后呈现这个 assets 路径。**

## 如何交付

交付统一走确定性四步流水线,本文件是唯一事实源:**内容校验 → 打包 → ZIP 内容与结构校验 → 呈现**。四步全部 PASS 才交付,任一失败回退修正。

### 第 1 步 —— 把技能目录打包成 .zip（主流程:从父目录打包）

把校验通过的技能主目录打包成单个归档，命名与技能同名，并直接输出到 `/workspace/assets/`。**从父目录 `/workspace/.skill_tmp` 打包 `<skill-name>` 目录**,使归档内为单一顶层目录 `<skill-name>/SKILL.md`(安装器接受的两种结构之一):

```bash
mkdir -p /workspace/assets
rm -f /workspace/assets/<skill-name>.zip          # 防止旧包残留导致 zip 追加/结构污染
cd /workspace/.skill_tmp && zip -r /workspace/assets/<skill-name>.zip <skill-name> \
  -x '*__pycache__*' '*.pyc' '*.DS_Store' '*/.*' '.*' '__MACOSX/*'
```

- **从父目录 `cd /workspace/.skill_tmp` 后 `zip -r ... <skill-name>`**，使归档内为单一顶层目录 `<skill-name>/`，其下直接含 `SKILL.md`(安装器可识别的结构)。
- 排除清单必须覆盖:暂存/垃圾文件（`__pycache__`、`*.pyc`、`*.DS_Store`）、隐藏文件与隐藏目录（`.*`、`*/.*`）、以及 macOS 元数据目录（`__MACOSX/`）。这些若混入会造成"多个顶层项"，让安装器无法定位 `SKILL.md`。
- 打包前先 `rm -f` 目标 zip，禁止往已存在的包里追加。
- 产出的技能不打包脚本，所以归档中应只包含 `<skill-name>/SKILL.md` 和 `<skill-name>/references/`——没有 `scripts/`。`SKILL.md` 的 frontmatter 必须含已填好的 `tools` 字段。
- 产出技能内部引用 references 一律用**相对路径**（如 `references/INDEX.md`），不要写死任何绝对路径或运行时容器路径。产出技能运行在隔离会话里，绝对路径不可移植，相对路径才能在用户侧正确加载。

### 第 1.5 步 —— 打包后自检（强制，不通过不得交付）

安装器只接受两种归档结构:(1) `SKILL.md` 在归档根目录;(2) 归档只有一个一级目录、且该目录直接含 `SKILL.md`。打包后**必须**用同款逻辑校验最终 ZIP，校验失败（退出码 1）就返回第 1 步修正，禁止进入第 2 步呈现:

```bash
python3 /workspace/.skills/skill-creator/scripts/quick_validate.py --zip /workspace/assets/<skill-name>.zip
```

- 该命令用与安装器一致的规则检查最终归档，能拦住"多顶层项（如夹带 `__MACOSX/`）"这类会触发 `SKILL.md not found` 的问题。主流程从父目录打包,归档内为单一顶层目录 `<skill-name>/SKILL.md`,属安装器接受结构。
- 只有该自检打印 `PASS` 且退出码为 0 时，才能继续第 2 步。

### 第 2 步 —— 把 .zip 呈现给用户

使用呈现产物（surface-artifact）能力，把**`/workspace/assets/` 下打包好的 `.zip` 文件**（而非目录）展示出来，并将产物类型设为 `skill`:

```
present_sandbox_file(
  path = "/workspace/assets/<skill-name>.zip",   # 打包好的技能归档
  type = "skill"                                  # 将该产物标记为可交付的技能
)
```

- `path` —— 第 1 步产出的 `/workspace/assets/<skill-name>.zip`（前端可以接收的单个文件）。
- `type` —— 必须为 `skill`，以便该产物作为可交付的技能而非通用文件来呈现。

## 交付之后

呈现技能产物卡片之后，只向用户回复一句:

`已完成并添加到技能`

不要再追加技能名称、用途、触发场景、改写摘要、校验结果、后续建议或任何解释性文字。卡片已经承载了交付动作，文字回复只保留这一句固定确认。

## 迭代

要修订已交付的技能,编辑 `SKILL.md` / `references/`,重新运行 `quick_validate.py` 做内容校验,再按第 1 步重新打包(从父目录 `cd /workspace/.skill_tmp` 后 `zip -r ... <skill-name>`),然后按第 1.5 步用 `quick_validate.py --zip` 做结构自检,自检通过后再用 `present_sandbox_file` 交付。
