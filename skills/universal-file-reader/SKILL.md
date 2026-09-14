---
name: universal-file-reader
description: 综合本地文件读取和解析 skill。当需要检查、预览、抽取或转换本地文件为 Markdown、JSON 或适合 CSV 的结构化文本时优先阅读本SKILL，支持 PDF、XLS、XLSX、XLSM、XLSB、ODS、CSV、TSV、DOCX、PPTX、TXT、Markdown、JSON、XML、HTML，以及可能需要 LibreOffice 转换的 legacy Office 文件。适用于快速阅读文档、检查电子表格、抽取表格、生成适合 RAG 的 Markdown、判断文件是否包含机器可读文本。不适用于高保真版式编辑或没有 OCR 引擎时的权威 OCR。
---

# 通用文件读取器

## 快速开始

优先使用统一调度入口：

```bash
python3 /workspace/.skills/universal-file-reader/scripts/file_reader.py "/absolute/path/to/input.xlsx" --out-dir "/absolute/path/to/output-dir"
```

调度脚本会写出：

- `content.md`：可读 Markdown
- `content.json`：结构化解析数据

如果调用方需要直接从 stdout 读取解析内容，使用：

```bash
python3 /workspace/.skills/universal-file-reader/scripts/file_reader.py "/absolute/path/to/input.pdf" --stdout --no-write
```

`--stdout` 默认输出 Markdown。需要结构化 JSON 时使用：

```bash
python3 /workspace/.skills/universal-file-reader/scripts/file_reader.py "/absolute/path/to/input.xlsx" --stdout json --no-write
```

对于 spreadsheet/CSV，默认全量读取。只有需要限制输出规模时，才显式传 `--max-rows`：

```bash
python3 /workspace/.skills/universal-file-reader/scripts/file_reader.py "/absolute/path/to/input.xlsx" --max-rows 200 --stdout --no-write
```

`--max-rows 0` 与不传 `--max-rows` 等价，表示不限制行数。`--all-rows` 也保留为全量读取的显式写法。

其他类型也默认全量读取。只有需要控制输出规模时，才显式使用限制参数：

```bash
# PDF 只读前 5 页
python3 /workspace/.skills/universal-file-reader/scripts/file_reader.py "/absolute/path/to/input.pdf" --max-pages 5 --stdout --no-write

# 文本、PDF、DOCX、PPTX 的 Markdown 最多输出 20000 个字符
python3 /workspace/.skills/universal-file-reader/scripts/file_reader.py "/absolute/path/to/input.docx" --max-chars 20000 --stdout --no-write
```

`--max-chars 0` 与不传 `--max-chars` 等价，表示不限制字符数。

## 决策树

1. 常规请求使用 `/workspace/.skills/universal-file-reader/scripts/file_reader.py`，它会按扩展名分发。
2. 用户询问 sheet、列、公式或表格值时，对 `.xls`、`.xlsx`、`.xlsm`、`.xlsb`、`.ods`、`.csv`、`.tsv` 可直接使用 `/workspace/.skills/universal-file-reader/scripts/parse_spreadsheet.py`。
3. 用户询问 PDF 页码、表格、扫描文本或 PDF 解析质量时，对 `.pdf` 可直接使用 `/workspace/.skills/universal-file-reader/scripts/parse_pdf.py`。
4. 对 `.docx` 或 `.pptx` 可直接使用 `/workspace/.skills/universal-file-reader/scripts/parse_office.py`。
5. 对 `.txt`、`.md`、`.json`、`.xml` 或 `.html` 可直接使用 `/workspace/.skills/universal-file-reader/scripts/parse_text.py`。

## 表格解析

优先做结构化 spreadsheet 抽取，不要只做纯文本转换。

对于 `.xlsx` 和 `.xlsm`，当需要公式、sheet 名、维度和单元格值时，优先使用 `openpyxl`。只有当 workbook 已经由 Excel 或 LibreOffice 保存过缓存公式结果时，才使用 `--data-only` 读取缓存值。

部分导出的 `.xlsx` 会把 worksheet 的 `<dimension>` 写错，例如实际有很多行但声明成 `A1`。这会让 `openpyxl` read-only 模式只读到表头。脚本会调用 `reset_dimensions()`，并在结果可疑时使用 ZIP XML 流式解析兜底，直接读取 `xl/worksheets/*.xml` 中的行数据。

对于 `.xls`，优先使用 `xlrd` 或带兼容 engine 的 `pandas`。如果都失败，先用 LibreOffice 转换：

```bash
soffice --headless --convert-to xlsx --outdir "/tmp/out" "/absolute/path/input.xls"
```

对于 `.xlsb`，优先使用带 `pyxlsb` 或 `calamine` engine 的 `pandas`。

对于 `.csv` 和 `.tsv`，内置解析器只依赖 Python 标准库。

## PDF 解析

先尝试抽取已有文本层。`/workspace/.skills/universal-file-reader/scripts/parse_pdf.py` 会按可用情况尝试这些引擎：

1. `PyMuPDF` (`fitz`)：快速按页抽取文本。
2. `pdfplumber`：抽取文本，并尽量抽取表格。
3. `pdftotext`：Poppler 提供的命令行文本抽取工具，适合作为稳健降级方案。
4. `pypdf`：纯 Python 文本降级方案。


如果输出为空或非常稀疏，说明 PDF 可能是扫描件或图片型 PDF。不要把这类结果当作完整解析，需要使用`PyMuPDF` (`fitz`)：将PDF渲染为图片，然后使用`sandbox_read`方法读取图片理解用户的文件。

## Office 与文本解析

对于 `.docx`，优先使用 `python-docx`；不可用时脚本会降级到 ZIP 包内的基础 WordprocessingML 文本读取。

对于 `.pptx`，优先使用 `python-pptx`；不可用时脚本会降级到 slide XML 文本读取。

对于 `.doc` 和 `.ppt`，先用 LibreOffice 转成 `.docx` 或 `.pptx`，再解析转换后的文件。

对于 `.json`、`.xml` 和 `.html`，使用 `/workspace/.skills/universal-file-reader/scripts/parse_text.py` 输出可读 Markdown 和简洁结构化元数据。

## 依赖策略

脚本要求 Python 3.10 或更高版本。默认设计是轻依赖并尽量降级，所以只安装当前文件类型需要的依赖。

```bash
# PDF: Python 文本/表格降级引擎
python3 -m pip install pymupdf pdfplumber pypdf

# Spreadsheet: .xls, .xlsx, .xlsm, .xlsb, .ods
python3 -m pip install pandas openpyxl xlrd pyxlsb python-calamine odfpy

# Office: .docx 和 .pptx
python3 -m pip install python-docx python-pptx

# HTML/XML 辅助解析
python3 -m pip install beautifulsoup4 lxml
```

系统工具单独安装：

```bash
apt-get install poppler-utils libreoffice
```

`poppler` 提供 `pdftotext`，适用于 Python PDF 库未安装或文本抽取效果较弱时。LibreOffice 提供 `soffice`，适用于 `.doc` 和 `.ppt` 转换、`.xls` 修复、spreadsheet 公式重算。

依赖与格式映射：

- `.pdf`：`pymupdf`、`pdfplumber`、`pypdf`，或系统 `pdftotext`。
- `.xlsx`、`.xlsm`：优先 `openpyxl`；`pandas` 也可配合 engine 读取。
- `.xls`：`xlrd` 或 `pandas`；解析失败时使用 LibreOffice 转换。
- `.xlsb`：`pandas` 配合 `pyxlsb` 或 `python-calamine`。
- `.ods`：`pandas` 配合 `odfpy` 或 `python-calamine`。
- `.docx`：优先 `python-docx`；ZIP XML 降级方案可读取基础文本。
- `.pptx`：优先 `python-pptx`；ZIP XML 降级方案可读取基础幻灯片文本。
- `.json`、`.xml`、`.html`、`.txt`、`.md`、`.csv`、`.tsv`：标准库可用；`beautifulsoup4` 可提升 HTML 抽取效果。

如果依赖不可用，继续使用任何成功的降级解析器，并按 `check_dependencies.py` 或解析器报错原文说明缺失依赖。

## 输出说明

向用户汇报结果时：

- 链接 `content.md` 作为可读输出。
- 当用户需要 sheet 名、页码、行数据、warning 或结构化元数据时，链接 `content.json`。
- 调用方需要管道读取内容时，使用 `--stdout --no-write`，避免 stdout 混入 summary JSON。
- 调用方需要管道读取结构化结果时，使用 `--stdout json --no-write`。
- 按脚本输出原文说明缺失依赖。
- Spreadsheet/CSV 默认全量读取；只有用户明确要求预览或限流时，才使用 `--max-rows N`。
- PDF 默认读取全部页；只有用户明确要求页数限制时，才使用 `--max-pages N`。
- Text/PDF/DOCX/PPTX 默认不截断 Markdown；只有用户明确要求字符限制时，才使用 `--max-chars N`。
- 解释发现时保留来源坐标：PDF 使用 page number，spreadsheet 使用 sheet name 和 row number，PPTX 使用 slide number。
