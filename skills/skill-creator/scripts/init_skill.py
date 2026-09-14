#!/usr/bin/env python3
"""
技能初始化器（agent 版） - 从模板创建一个新技能

用法:
    init_skill.py <skill-name>              # 通用技能骨架（无脚本，含 tools 字段）
    init_skill.py <skill-name> --creative   # 创意类（视频/图片）技能骨架(8 支柱 + 词库脚手架)
    init_skill.py <skill-name> --distill    # 分支 C 轨迹蒸馏骨架（默认仅 SKILL.md）

示例:
    init_skill.py my-new-skill
    init_skill.py tiktok-ugc-maker --creative
    init_skill.py distilled-workflow --distill

技能创建在 /workspace/.skill_tmp/<skill-name>/（临时构建目录），最终从该目录打包到 /workspace/assets。
产出的技能不打包 scripts/ 目录，但**必须**在 frontmatter 声明 `tools` 字段
（依赖的生成工具白名单）。产出技能内部引用 references 一律用相对路径
（references/...），不写死绝对路径。

frontmatter 另有两个**可选**字段 `image_model` / `video_model`（指定该技能使用的
生成模型）。骨架里以注释形式给出，**默认保持注释状态/删除**——只有在用户显式要求
指定模型，或从用户输入/上传内容里识别到模型信息时才启用，取值见
references/model-catalog.md。
"""

import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# tools 字段选择规则（写进两个模板的 TODO 注释）
# ---------------------------------------------------------------------------
# 产出的技能必须声明 `tools`（依赖的生成工具白名单）。允许的取值:
#   图片: "sandbox_generate_image"
#   视频: "render_video" / "sandbox_generate_video" / "sandbox_process_video"（三件套配套）
# 选择规则:
#   只生图          -> tools: ["sandbox_generate_image"]
#   只生视频        -> tools: ["render_video", "sandbox_generate_video", "sandbox_process_video"]
#   既生图又生视频  -> 四个工具全列
TOOLS_TODO = (
    '["TODO_REPLACE_ME"]  '
    '# 只生图填 ["sandbox_generate_image"]；'
    '只生视频填 ["render_video", "sandbox_generate_video", "sandbox_process_video"]；'
    '既生图又生视频则四个全列。把 TODO_REPLACE_ME 换成实际工具名。'
    '注: sandbox_generate_video 支持 <=15s 视频一次生成完整成片，'
    '成片超过 15s 才需拆成多个 <=15s 片段分别生成再拼接。'
)

# ---------------------------------------------------------------------------
# 可选的模型字段(image_model / video_model)——默认不启用
# ---------------------------------------------------------------------------
# 以注释形式写进骨架 frontmatter, 提醒作者「有这个能力, 但默认别用」:
#   仅当 ① 用户显式要求指定模型, 或 ② 从用户输入/上传内容里识别到模型信息时,
#   才取消注释并填入合法取值(取值清单见 references/model-catalog.md)。
#   其余情况保持注释或整行删除, 由平台按默认模型执行。
MODEL_FIELDS_TODO = (
    "# 以下两个字段为**可选**, 默认保持注释(或删除本两行)——不要主动帮用户设置模型。\n"
    "# 仅当用户显式要求指定模型, 或从用户输入/上传内容里识别到模型信息时, 才取消注释并填入\n"
    "# 支持清单内的取值(清单见 skill-creator 的 references/model-catalog.md);\n"
    "# 用户要求的模型不在清单内时, 把支持清单反问给用户改选, 不要就近替换。\n"
    "# image_model: <支持清单中的图片模型取值, 如 seedream_5.0>\n"
    "# video_model: <支持清单中的视频模型取值, 如 Seedance_2.0_mini>"
)

# ---------------------------------------------------------------------------
# 通用骨架（保持原有的轻量 TODO 模板）
# ---------------------------------------------------------------------------
SKILL_TEMPLATE = """---
name: {skill_name}
display_name: [TODO: 该技能的中文展示名，给最终用户看，必须为中文，例如 倒挂金钩。尽量控制在 10 个中文字符以内。]
description: [TODO: 完整、信息充分地说明这个技能做什么以及何时使用它。包含何时（WHEN）使用这个技能——触发它的具体场景、文件类型或任务。不含尖括号; 最多 1024 字符。]
tools: {tools_todo}
{model_fields_todo}
---

# {skill_title}

## Overview

[TODO: 用 1-2 句话说明这个技能为 agent 启用了什么能力。]

## When to Use

[TODO: 触发条件——应当激活这个技能的场景/意图。]

## Constraints

[TODO: 贯穿这个技能执行全程的全局 do/don't 规则。]

## Workflow (Steps)

[TODO: 分步骤 SOP。对每个步骤，以能力的方式说明要做什么（例如 读取一个文件、把一个文件展示给用户）——不要点名内部工具。]

## Input Parsing

[TODO: 如何把用户输入/上传的材料解析为结构化参数。不需要则删除。]

## Structuring This Skill

[TODO: 选择最契合这个技能用途的结构。常见模式:

1. 基于工作流（顺序流程）: ## Overview -> ## Workflow -> ## Step 1 -> ## Step 2...
2. 基于任务（工具集合）: ## Overview -> ## Quick Start -> ## Task A -> ## Task B...
3. 参考/准则（标准/规范）: ## Overview -> ## Guidelines -> ## Specifications...
4. 基于能力（集成系统）: ## Overview -> ## Core Capabilities -> ### 1. Feature...

模式可以混用。完成后删除整个 "Structuring This Skill" 小节。]

## Resources

### references/
按需加载进上下文的文档（schema、API 文档、政策）。让 SKILL.md 保持精简。

### 不打包脚本
这个技能不打包任何脚本。把所有逻辑表达为文字指令 / SOP，以驱动
agent 运行时已有的工具，并以能力的方式描述（正文不点名 frontmatter 里声明的工具名）。
"""

EXAMPLE_REFERENCE = """# {skill_title} 的参考文档

这是一个详细参考文档的占位符。
请替换为实际的参考内容，或在不需要时删除。

## 何时需要参考文档

- 全面的 API 文档
- 详细的工作流指南
- 复杂的多步骤流程
- 对主 SKILL.md 而言过长的信息
- 仅在特定用例下才需要的内容

## 结构建议

### 工作流指南示例
- 前置条件
- 分步骤说明（以能力的方式描述每个步骤）
- 常见模式
- 故障排查
- 最佳实践
"""


# ---------------------------------------------------------------------------
# 创意类骨架（视频/图片技能的黄金架构 —— 8 支柱）
# ---------------------------------------------------------------------------
CREATIVE_SKILL_TEMPLATE = """---
name: {skill_name}
display_name: [TODO: 该技能的中文展示名，给最终用户看，必须为中文，例如 倒挂金钩。尽量控制在 10 个中文字符以内。]
description: [TODO: 说明这个创意技能做什么(为哪种产品/行业/平台/市场生成什么样的视频或图片创意与最终 prompt)，以及何时触发(具体的素材类型/平台/市场/意图)。不含尖括号; 最多 1024 字符。]
tools: {tools_todo}
{model_fields_todo}
---

[TODO: 语言规则——本骨架默认中文。请把整份 SKILL.md 与所有 references 改写为该技能目标市场/受众的工作语言(与 description 一致)。例如目标为 US/TikTok/英语受众则整体写英文，不要中英混杂。完成后删除本行。]

# {skill_title}

## 1. 核心原则 + 持久引擎

[TODO: 一句话核心原则(这类创意成立的根本机理，而非套路)。]

持久引擎(因果链，按本技能领域改写):
**[输入要素] -> [张力] -> [钩子] -> [升级] -> [产品作为剧情/证据功能] -> [可见证据] -> [情感回报] -> [转化/记忆点]**

## 2. 质量测试（可证伪）

[TODO: 一条可证伪的判据。范式: "如果没有这个产品/这个机制，[主角/画面]就无法以这种方式取胜/证明/转折"。不通过就重做，不要进入出 prompt 阶段。]

## 3. 输入诊断（落 prompt 前必须想清楚的维度）

[TODO: 把用户输入解析为结构化参数。至少覆盖:
- 产品品类与核心卖点
- 目标市场与对白语种(不要只翻译语言，要本地化)
- 目标平台与画幅(见 references/formats/platforms-markets.md)
- 目标生成模型代际与产物(视频/图片)
- 受众压力 / 文化钩子
- 体裁路线(brand-film / ugc / short-drama / ...)
- craft 层取舍(光/镜/VFX/声/色材)——**仅当工艺是本技能核心，或用户/上传文件已提供时才展开；否则略过**
- 合规敏感点(健康/金融/酒精/博彩/儿童/可持续/AI/网红披露)]

## 4. 路由表（按输入选路线）

[TODO: 一张表，把"输入特征"映射到"体裁/卖法/要加载的 reference"。让 SKILL.md 当路由枢纽，不当执行手册。若涉及工艺层且已建 craft/，一并映射进去。]

| 输入特征 | 选用路线 | 必读 reference |
|---|---|---|
| [TODO] | [TODO] | references/... |

## 5. 强制加载 reference（硬规则）

落 prompt 前，**必须**按路由结果加载对应 references，并把相关词汇/句式写进本技能的实际产出。不得跳过、不得凭记忆糊。
- 行业词: references/industries/
- 体裁与平台: references/formats/
- prompt 文法: references/formats/video-prompt-grammar.md
- craft 工艺: references/craft/（**可选**，仅当已按需创建时才加载）

## 6. 输出契约（固定字段 / 时间码 beat）

[TODO: 规定产出格式。短视频用时间码 beat(0-3s/3-7s/7-12s/12-15s)，每个 beat 定义主体动作/相机/光/产品曝光/声音。图片用构图+光+材质+情绪四件套。最终 prompt 用正向措辞，不堆否定式约束。]

[TODO: 写清视频生成方式——**时长 ≤15s 的成片用一次视频生成即可拿到完整片段**，上面的多段 beat(0-3s/3-7s/…)是同一条 prompt 内的时间轴，不是分段多次生成；只有成片 >15s 时，才拆成若干 ≤15s 片段各自一次生成，再做后处理拼接/配乐/字幕。以能力方式表述"一次生成一段 ≤15s 成片"，不点名任何内部工具(工具名只写在 frontmatter 的 tools 字段)。]

## 7. 静默自检（出稿前，不外显）

[TODO: 一份 checklist。范式见各 reference 结尾的"落 prompt 前自检"。覆盖: 市场是否明确、首 3 秒是否兑现 hook、产品是否有决定性功能、证据是否在 CTA 前可见、成片是否 ≤15s(若是则一次生成完整片段而非分段拼接；若 >15s 是否已切成 ≤15s 片段)、措辞是否正向、宣称是否保守、披露是否注明、模型代际/日期是否标注、全文语言是否与目标市场一致无混杂。]
"""

# 分支 C 默认只交付 SKILL.md。轨迹中的经验、护栏和专业信息全部内联，
# 不生成或引用 references/；只有用户明确要求时才回退到创意类富骨架。
DISTILL_SKILL_TEMPLATE = """---
name: {skill_name}
display_name: [TODO: 该技能的中文展示名，必须为中文。]
description: [TODO: 说明该技能沉淀的可复用创作能力及触发场景。]
tools: {tools_todo}
{model_fields_todo}
---

[TODO: 全文使用目标市场/受众的工作语言，完成后删除本行。]

# {skill_title}

## 必用技能

[TODO: 若轨迹中含非 skill-creator 的 load_skill 调用，在此逐个写入固定句式(按需加载，不解析其内部流程):
使用 skill 加载工具加载 `${{skill名称}}`
本节必须位于「输入」与「工作流」之前(skill 需提前加载)。若轨迹无任何被加载的 Skill，则整节删除。]

## 输入

[TODO: 列出必需输入与可选输入；素材缺失时只追问缺失项，齐全时直接执行。]

## 1. 核心原则

[TODO: 用一句话概括从轨迹中验证过的核心机制。]

## 2. 质量标准

[TODO: 写入可证伪的质量判据与轨迹中验证过的关键护栏。]

## 3. 输入诊断

[TODO: 区分固定流程与每次任务的可变输入。]

## 4. 工作流 SOP

[TODO: 写入提纯后的最短成功路径。若轨迹含 load_skill，必须按 Skill 调用保留规则写入固定句式，不得展开其内部流程。]

## 5. 输出契约

[TODO: 规定产出结构、关键参数与质量要求。]

## 6. 静默自检

[TODO: 交付前检查流程、参数、Skill 调用和质量门是否完整。]
"""

# 创意技能自带的 references 脚手架(占位，作者按领域填充并改写为目标语言)
# 注意: craft/ 默认不建。仅当用户明确要求工艺层，或上传文件本身已含灯光/运镜/声音等
# 工艺信息时，作者才手动创建 references/craft/ 并填充。默认只铺 industries/ + formats/。
CREATIVE_REFERENCE_DIRS = [
    "industries",
    "formats",
]

CREATIVE_INDEX = """# 创意词库导航

> 可适配的模式与句式，按场景改写，不要逐字照搬。
> 🕒 平台/趋势/模型版本会变，标注假设与日期，定期更新。
> [TODO 给作者(写完删除本行): 本文件及同目录词条请改写为本技能目标市场的语言；正文不要出现任何关于本技能制作过程的内部说明。]

## industries/ —— 行业词
- [TODO: 只保留本技能覆盖的行业文件]

## formats/ —— 体裁与平台
- formats/platforms-markets.md —— 平台规则与市场本地化/合规
- formats/video-prompt-grammar.md —— prompt 文法(beat 结构、实体标签、正向措辞)
- [TODO: 按需保留 brand-film-tvc / ugc-marketing / short-drama-commerce]

## craft/ —— 工艺层（可选，默认不建）
> 默认**不创建** craft/ 目录。仅当以下任一成立时才手动新建 `references/craft/` 并撰写:
> ① 用户明确要求覆盖灯光/运镜/VFX/声音/材质/色彩等工艺层;
> ② 用户上传的文件本身已含这类工艺信息(直接改写沉淀即可)。
> 不满足则跳过，把工艺要点内联进 formats/ 的 prompt 文法或输出契约即可，别为凑目录空写 craft。
"""

CREATIVE_REFERENCE_STUB = """# [TODO: reference 标题]

> 可适配的模式与句式，按场景改写，不要逐字照搬。

[TODO 给作者(写完删除本说明): 把与本技能领域相关的词汇/句式/路由填进来，
删除不相关的行业/体裁，避免技能臃肿。每个文件结尾保留一份"落 prompt 前自检"。
全文用本技能目标市场的语言；正文不要出现任何关于本技能制作过程的内部说明。]
"""


def title_case_skill_name(skill_name):
    """把连字符分隔的技能名转换为用于显示的 Title Case。"""
    return ' '.join(word.capitalize() for word in skill_name.split('-'))


# 临时构建目录（skill-creator 创建的技能先落这里，最终打包到 /workspace/assets）
SKILLS_BASE_PATH = "/workspace/.skill_tmp"


def init_skill(skill_name, creative=False, distill=False, with_references=False):
    """
    用模板 SKILL.md 初始化一个新技能目录（无脚本，frontmatter 含 tools 字段）。

    参数:
        skill_name: 技能名称（hyphen-case）
        creative:   True 时生成创意类(视频/图片)8 支柱骨架 + 词库脚手架
        distill:    True 时生成分支 C 轨迹蒸馏骨架，默认仅 SKILL.md
        with_references: 分支 C 中用户明确要求 references 时设为 True

    返回:
        所创建技能目录的路径，出错时返回 None
    """
    skill_dir = Path(SKILLS_BASE_PATH) / skill_name

    if skill_dir.exists():
        print(f"X 错误: 技能目录已存在: {skill_dir}")
        return None

    try:
        skill_dir.mkdir(parents=True, exist_ok=False)
        print(f"OK 已创建技能目录: {skill_dir}")
    except Exception as e:
        print(f"X 创建目录出错: {e}")
        return None

    creative = creative or distill
    include_references = not distill or with_references
    skill_title = title_case_skill_name(skill_name)
    if distill and not with_references:
        template = DISTILL_SKILL_TEMPLATE
    else:
        template = CREATIVE_SKILL_TEMPLATE if creative else SKILL_TEMPLATE
    skill_content = template.format(
        skill_name=skill_name,
        skill_title=skill_title,
        tools_todo=TOOLS_TODO,
        model_fields_todo=MODEL_FIELDS_TODO,
    )

    skill_md_path = skill_dir / 'SKILL.md'
    try:
        skill_md_path.write_text(skill_content)
        suffix = (
            "（分支 C 蒸馏骨架）"
            if distill and not with_references
            else ("（创意类 8 支柱骨架）" if creative else "")
        )
        print("OK 已创建 SKILL.md" + suffix)
    except Exception as e:
        print(f"X 创建 SKILL.md 出错: {e}")
        return None

    if include_references:
        try:
            references_dir = skill_dir / 'references'
            references_dir.mkdir(exist_ok=True)

            if creative:
                for rel in CREATIVE_REFERENCE_DIRS:
                    (references_dir / rel).mkdir(parents=True, exist_ok=True)
                (references_dir / 'INDEX.md').write_text(CREATIVE_INDEX)
                (references_dir / 'formats' /
                 'platforms-markets.md').write_text(CREATIVE_REFERENCE_STUB)
                (references_dir / 'formats' /
                 'video-prompt-grammar.md').write_text(CREATIVE_REFERENCE_STUB)
                print("OK 已创建创意词库脚手架: references/{INDEX.md, industries/, formats/}")
                print("   提示: 按本技能领域撰写相关行业/体裁词进上述目录(会话隔离，运行时只能读到本技能自己的 references/)")
                print("   注意: craft/ 工艺层默认不建。仅当用户明确要求，或上传文件已含灯光/运镜/声音等工艺信息时，才手动创建 references/craft/ 并填充。")
            else:
                (references_dir / 'reference.md').write_text(
                    EXAMPLE_REFERENCE.format(skill_title=skill_title))
                print("OK 已创建 references/reference.md")
        except Exception as e:
            print(f"X 创建资源目录出错: {e}")
            return None
    else:
        print("OK 分支 C 默认仅创建 SKILL.md（用户未明确要求 references）")
    print("(无 scripts/ —— 产出的技能不打包脚本)")

    print(f"\nOK 技能 '{skill_name}' 已初始化于 {skill_dir}")
    print("提示: frontmatter 里的 image_model / video_model 为可选字段，默认保持注释——")
    print("      只有用户显式要求指定模型、或从用户输入/上传内容里识别到模型信息时才启用。")
    print("\n下一步:")
    if distill and not with_references:
        print("1. 将轨迹中的成功路径、护栏和可变输入全部写入 SKILL.md")
        print("2. 不创建 references/；只有用户明确要求时才使用 --with-references")
        print("3. 运行 quick_validate.py <skill-name> --distill 校验")
        print("4. 打包成 .zip，通过 present_sandbox_file (type=skill) 交付")
    elif creative:
        print("1. 编辑 SKILL.md: 逐条完成 8 支柱 TODO，打磨 description，填写中文 display_name，并确认 tools 字段(生图/生视频)")
        print("2. 按本技能领域撰写相关词进 references/{industries,formats}/，更新 INDEX.md；craft/ 仅在需要时再建")
        print("3. 对照黄金架构(references/creative-skill-patterns.md)自检 8 支柱齐备")
        print("4. 运行 quick_validate.py 校验")
        print("5. 打包成 .zip，通过 present_sandbox_file (type=skill) 交付")
    else:
        print("1. 编辑 SKILL.md: 完成 TODO，打磨 description，填写中文 display_name，并确认 tools 字段(生图/生视频)")
        print("2. 自定义或删除 references/ 中的示例文件")
        print("3. 准备好后运行 quick_validate.py")
        print("4. 把技能目录打包成 .zip，然后通过 present_sandbox_file (type=skill) 交付 —— 见 SKILL.md 第 5 步")

    return skill_dir


def main():
    args = [a for a in sys.argv[1:]]
    distill = '--distill' in args
    with_references = '--with-references' in args
    creative = '--creative' in args or distill
    positional = [a for a in args if not a.startswith('--')]

    if with_references and not distill:
        print("X --with-references 只能与 --distill 一起使用")
        sys.exit(1)

    if len(positional) != 1:
        print("用法: init_skill.py <skill-name> [--creative | --distill [--with-references]]")
        print("\n技能名称要求:")
        print("  - hyphen-case 标识符（例如 'data-analyzer'）")
        print("  - 仅限小写字母、数字和连字符")
        print("  - 最多 64 个字符")
        print("\n选项:")
        print("  --creative   生成创意类(视频/图片)8 支柱骨架 + 词库脚手架")
        print("  --distill    生成分支 C 轨迹蒸馏骨架，默认仅 SKILL.md")
        print("  --with-references  分支 C 中仅在用户明确要求时创建 references")
        print("\n示例:")
        print("  init_skill.py my-new-skill")
        print("  init_skill.py tiktok-ugc-maker --creative")
        print("  init_skill.py distilled-workflow --distill")
        print("  init_skill.py distilled-workflow --distill --with-references")
        print(f"\n技能创建在 {SKILLS_BASE_PATH}/<skill-name>/")
        sys.exit(1)

    skill_name = positional[0]

    print(f"正在初始化技能: {skill_name}")
    print(f"   位置: {SKILLS_BASE_PATH}/{skill_name}")
    mode = '｜分支 C 蒸馏骨架' if distill else ('｜创意类骨架' if creative else '')
    print(f"   类型: 无脚本，frontmatter 含必填 tools 字段{mode}")
    print()

    result = init_skill(
        skill_name,
        creative=creative,
        distill=distill,
        with_references=with_references,
    )
    sys.exit(0 if result else 1)


if __name__ == "__main__":
    main()
