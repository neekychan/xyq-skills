#!/usr/bin/env python3
"""
agent 技能的快速校验脚本

用法:
    quick_validate.py <skill-name> [--creative]
    quick_validate.py <skill-name> --distill [--with-references]
    quick_validate.py <absolute-path-to-skill> [--creative]
    quick_validate.py --zip <path-to-skill.zip>

示例:
    quick_validate.py my-skill
    quick_validate.py /workspace/.skill_tmp/my-skill --creative
    quick_validate.py --zip /workspace/assets/my-skill.zip

技能在构建期位于 /workspace/.skill_tmp/<skill-name>/（临时构建目录）。

校验一个产出的技能（面向用户的交付物）:
  - SKILL.md 存在性 + YAML frontmatter
  - 允许的 frontmatter 属性（name/display_name/description/tools/license/image_model/video_model）
  - hyphen-case 的 name、description 约束
  - display_name 字段: 必填且非空，且必须为中文（至少包含一个中文字符）；建议尽量 < 10 个中文字符（超过仅警告）
  - tools 字段: 必填且非空，取值只能来自允许的生成工具集合；视频三件套配套使用
  - image_model / video_model 字段: **可选**（默认不写）；一旦出现必须是单个字符串、
    取值在支持的模型清单内，且与 tools 自洽（图片模型需图片工具、视频模型需视频三件套）
  - 不打包脚本
  - 保密红线: SKILL.md / references 正文内不得点名内部或第三方外部的生成工具/模型(扫描提示，警告级)
  - 路径契约(已放宽): references 内部引用用相对路径，不写死绝对/容器路径
  - 违禁词/不合规内容: 扫描敏感词并以警告形式提示作者复核(不阻断，避免误杀)
  - --creative: 额外检查创意类 8 支柱齐备(以警告形式提示，不阻断)
  - --distill: 分支 C 默认要求只含 SKILL.md，不得有 references/

关于 tools 字段: 产出的技能必须在 frontmatter 用 `tools` 声明它依赖
哪些生成工具(这是触发后运行时实际可调用的工具白名单)。允许的取值:
  - "sandbox_generate_image"            生成图片
  - "render_video" / "sandbox_generate_video" / "sandbox_process_video"
                                        生成视频(三件套，配套一起使用)
选择规则:
  - 只生成图片            -> ["sandbox_generate_image"]
  - 只生成视频            -> ["render_video","sandbox_generate_video","sandbox_process_video"]
  - 既生图又生视频        -> 上面四个工具全列
注意: 这些工具名只允许出现在 frontmatter 的 `tools` 字段；SKILL.md / references
的正文仍以能力方式描述要做的事，不在正文里点名这些工具(保密红线)。

关于 image_model / video_model 字段(可选): 用于把该技能使用的生成模型固定下来。
**默认不写**——缺省时由平台按默认模型执行。只有在用户显式要求指定模型，或从用户
输入/上传内容里识别到模型信息时才设置。取值必须逐字来自支持的模型清单(见
references/model-catalog.md)。模型名同样只允许出现在这两个 frontmatter 字段里。
"""

import sys
import re
import posixpath
import zipfile
import yaml
from pathlib import Path

# 临时构建目录（skill-creator 创建的技能先落这里，最终打包到 /workspace/assets）
SKILLS_BASE_PATH = Path("/workspace/.skill_tmp")

# 产出的技能中可接受的 frontmatter 属性。
# `tools` 现在是**必填**字段(声明该技能依赖哪些生成工具)。
# `display_name` 是**必填**字段(技能的中文展示名，给最终用户看)。
# `image_model` / `video_model` 是**可选**字段(指定该技能使用的生成模型;默认不写)。
# `metadata`/`priority`/`visibility` 已移除——不再写进产物。
ALLOWED_PROPERTIES = {
    'name', 'display_name', 'description', 'tools', 'license',
    'image_model', 'video_model',
}

# 用于判定 display_name 是否包含中文字符(CJK 统一表意文字基本区)。
CJK_PATTERN = re.compile(r'[一-鿿]')

# 允许在 `tools` 中声明的生成工具白名单。
IMAGE_TOOLS = {'sandbox_generate_image'}
VIDEO_TOOLS = {'render_video', 'sandbox_generate_video', 'sandbox_process_video'}
ALLOWED_TOOLS = IMAGE_TOOLS | VIDEO_TOOLS

# 支持的生成模型清单(可选字段 image_model / video_model 的取值白名单)。
# 取值大小写敏感，必须逐字命中——视频侧的写法本身并不统一(Seedance_2.5 与
# seedance2.0_direct 并存)，不要按规律推断。展示名仅用于向用户反问时呈现。
IMAGE_MODELS = {
    'seedream_5.0_pro': 'Seedream 5.0 Pro',
    'seedream_5.0': 'Seedream 5.0 Lite',
    'seedream_4.3': 'Seedream 4.0 美感版',
    'nova2': '旗舰生图模型 V2-Flash',
    'seedream_4.5': 'Seedream 4.5',
    'seedream_4.1': 'Seedream 4.1',
    'seedream_4': 'Seedream 4',
    'nano_banana_pro_1': 'Nano Banana Pro',
}
VIDEO_MODELS = {
    'Seedance_2.5': 'Seedance 2.5',
    'Seedance_2.0_mini_lite': 'Seedance 2.0 Mini 体验版',
    'Seedance_2.0_mini': 'Seedance 2.0 Mini',
    'seedance2.0_fast_vision': 'Seedance 2.0 Fast VIP',
    'seedance2.0_vision': 'Seedance 2.0 VIP',
    'seedance_2.0_fast': 'Seedance 2.0 Fast',
    'seedance2.0_direct': 'Seedance 2.0',
}

SCRIPT_EXTENSIONS = {'.py', '.sh', '.js', '.ts', '.rb', '.pl', '.bash'}

# 保密红线: 这些为构建期路径/运行时容器路径，产出技能里不应出现(应改用相对路径)。
ABSOLUTE_PATH_PATTERNS = [
    r'/workspace/\.skills',
    r'/workspace/\.skill_tmp',
    r'/home/mira/\.session',
    r'/data/plugins/',
]

# 创意类支柱的标题信号(出现其一即视为该支柱存在)。
# 注意: "保密红线"不在此列——它是作者侧元规则，不应作为章节写进产物(见 META_LEAK_TERMS)。
CREATIVE_PILLAR_SIGNALS = {
    "核心原则/持久引擎": ["核心原则", "持久引擎", "Core Principle", "durable engine"],
    "质量测试": ["质量测试", "quality test", "concept is strong"],
    "输入诊断": ["输入诊断", "落 prompt 前", "输入解析", "Input Diagnosis"],
    "路由表": ["路由表", "Routing Table"],
    "强制加载 reference": ["强制加载", "必读", "INDEX.md", "Mandatory Reference"],
    "输出契约": ["输出契约", "beat", "时间码", "Output Contract"],
    "静默自检": ["静默自检", "自检", "Silent Check"],
}

# 建造期元信息泄漏: 这些是 skill-creator 的内部建造概念/作者侧元规则，
# 绝不应作为章节或说明文字出现在产出的技能里(出现即视为泄漏，校验失败)。
META_LEAK_TERMS = [
    "保密红线",
    "母库",
    "会话隔离",
    "构建期",
    "建造期",
    "pure-text skill",
    "No scripts (pure-text",
    "纯文本规则",
    "mother library",
    "session isolation",
]

# 违禁词 / 不合规内容筛查(警告级)。
# 目的: 帮助作者在交付前复核上传技能里可能夹带的敏感/违规文字。
# 采用"提示而非阻断"策略, 因为这些词在正当语境下也可能出现(如合规说明),
# 硬失败会误杀。命中即提请作者人工判断并做最小必要处理。
BANNED_CONTENT_TERMS = [
    # 色情低俗
    "色情", "porn", "裸体", "情色",
    # 暴力血腥
    "血腥", "暴恐", "恐怖袭击",
    # 仇恨歧视 / 人身攻击
    "种族歧视", "仇恨言论",
    # 违法违规
    "赌博", "毒品", "洗钱", "诈骗",
    # 隐私 / 机密泄露信号词
    "身份证号", "银行卡号", "密码明文",
]

# 具名工具/模型泄漏(警告级): 产出技能正文应以能力描述,不点名任何
# 内部或第三方外部的生成工具/模型。命中即提示作者改为能力化表述。
# 采用"提示而非阻断"策略, 名单为启发式, 硬失败可能误杀正当引用。
NAMED_TOOL_TERMS = [
    # 动作/工具名(源平台写法)
    "TextToImage", "ImageToImage",
    # 第三方模型名
    "GPT Image", "Seedance", "Seedream", "Nano Banana", "Kling", "Suno", "Mureka", "MiniMax",
]


def _validate_model_fields(frontmatter):
    """校验可选的 image_model / video_model 字段。

    返回 (ok: bool, message: str)。两字段均**可选**——缺省时由平台按默认模型执行,
    这是默认且推荐的情形。一旦出现则必须: 是单个非空字符串、取值逐字命中支持清单、
    并与 `tools` 自洽(图片模型需图片工具、视频模型需视频三件套)。
    """
    tool_set = set(frontmatter.get('tools') or [])

    checks = (
        ('image_model', IMAGE_MODELS, IMAGE_TOOLS, '图片'),
        ('video_model', VIDEO_MODELS, VIDEO_TOOLS, '视频'),
    )

    for field, catalog, required_tools, kind in checks:
        if field not in frontmatter:
            continue

        value = frontmatter.get(field)
        if not isinstance(value, str):
            return False, (
                f"'{field}' 必须是单个字符串取值，得到的是 {type(value).__name__}。"
                f"例如 {field}: {next(iter(catalog))}"
            )
        value = value.strip()
        if not value:
            return False, (
                f"'{field}' 不能为空。要么填一个支持的{kind}模型取值，要么整个删掉该字段"
                "(不设置即走平台默认模型)。"
            )
        if value not in catalog:
            # 取值写错时最常见的两种原因: 填了展示名, 或大小写/分隔符不符。
            label_hit = next(
                (v for v, label in catalog.items() if label.lower() == value.lower()), None)
            case_hit = next(
                (v for v in catalog if v.lower() == value.lower()), None)
            hint = ''
            if label_hit:
                hint = f" 你填的像是展示名，对应取值应为 '{label_hit}'。"
            elif case_hit:
                hint = f" 取值大小写/分隔符不符，正确写法为 '{case_hit}'。"
            return False, (
                f"'{field}' 取值 '{value}' 不在支持的{kind}模型清单内。{hint}"
                f"支持的取值: {', '.join(sorted(catalog))}。"
                "若用户要求的模型不在清单内，应把支持清单反问给用户改选，不要就近替换。"
            )
        if not (tool_set & required_tools):
            return False, (
                f"'{field}' 与 'tools' 不自洽: 声明了{kind}模型，但 'tools' 里没有{kind}生成工具。"
                f"请补齐 {', '.join(sorted(required_tools))}，或删除 '{field}' 字段。"
            )

    return True, ''


def _strip_frontmatter_lines(text):
    """返回 [(行号, 行内容)]，跳过文件开头的 YAML frontmatter 块。

    frontmatter 里的 `tools` / `image_model` / `video_model` 是合法的具名声明，
    不应被"正文点名工具/模型"的扫描误判，因此扫描正文时把该块排除。
    """
    lines = text.splitlines()
    start = 0
    if lines and lines[0].strip() == '---':
        for i in range(1, len(lines)):
            if lines[i].strip() == '---':
                start = i + 1
                break
    return [(i, lines[i - 1]) for i in range(start + 1, len(lines) + 1)]


def _scan_named_tools(skill_path):
    """扫描 .md 正文里点名的具名工具/模型(警告级)。返回 [(file, line, term, snippet)]。

    frontmatter 块被排除——`tools` / `image_model` / `video_model` 是允许出现
    具名取值的唯一位置。
    """
    hits = []
    for p in skill_path.rglob('*.md'):
        try:
            for i, line in _strip_frontmatter_lines(p.read_text(errors='ignore')):
                for term in NAMED_TOOL_TERMS:
                    if term in line:
                        hits.append((str(p.relative_to(skill_path)), i, term, line.strip()[:80]))
                        break
        except Exception:
            continue
    return hits


def _scan_banned_content(skill_path):
    """扫描 .md 文本里可能的违禁/不合规词(警告级)。返回 [(file, line, term, snippet)]。"""
    hits = []
    for p in skill_path.rglob('*.md'):
        try:
            for i, line in enumerate(p.read_text(errors='ignore').splitlines(), 1):
                for term in BANNED_CONTENT_TERMS:
                    if term in line:
                        hits.append((str(p.relative_to(skill_path)), i, term, line.strip()[:80]))
                        break
        except Exception:
            continue
    return hits


def resolve_skill_path(skill_path_or_name):
    """把技能路径解析为绝对路径。"""
    path = Path(skill_path_or_name)
    if path.is_absolute():
        return path
    return SKILLS_BASE_PATH / skill_path_or_name


def _scan_scripts(skill_path):
    """返回在技能目录下找到的、打包的可执行脚本文件列表。"""
    found = []
    scripts_dir = skill_path / 'scripts'
    if scripts_dir.is_dir():
        found.append(str(scripts_dir.relative_to(skill_path)) + '/')
    for p in skill_path.rglob('*'):
        if p.is_file() and p.suffix.lower() in SCRIPT_EXTENSIONS:
            found.append(str(p.relative_to(skill_path)))
    return found


def _scan_absolute_paths(skill_path):
    """扫描 .md 文本里写死的绝对/容器路径(违反相对路径契约)。返回 [(file, line, snippet)]。"""
    hits = []
    for p in skill_path.rglob('*.md'):
        try:
            for i, line in enumerate(p.read_text(errors='ignore').splitlines(), 1):
                for pat in ABSOLUTE_PATH_PATTERNS:
                    if re.search(pat, line):
                        hits.append((str(p.relative_to(skill_path)), i, line.strip()[:80]))
                        break
        except Exception:
            continue
    return hits


def _scan_meta_leaks(skill_path):
    """扫描 .md 文本里泄漏的建造期元信息。返回 [(file, line, term, snippet)]。"""
    hits = []
    for p in skill_path.rglob('*.md'):
        try:
            for i, line in enumerate(p.read_text(errors='ignore').splitlines(), 1):
                for term in META_LEAK_TERMS:
                    if term in line:
                        hits.append((str(p.relative_to(skill_path)), i, term, line.strip()[:80]))
                        break
        except Exception:
            continue
    return hits


def _check_creative_pillars(content):
    """返回缺失的创意支柱名列表(基于 SKILL.md 文本信号)。"""
    missing = []
    for pillar, signals in CREATIVE_PILLAR_SIGNALS.items():
        if not any(sig in content for sig in signals):
            missing.append(pillar)
    return missing


def validate_skill(
        skill_path_or_name,
        creative=False,
        distill=False,
        with_references=False):
    """对产出的 agent 技能进行结构 + tools 字段校验。

    返回 (valid: bool, message: str, warnings: list[str])
    """
    warnings = []
    skill_path = resolve_skill_path(skill_path_or_name)

    skill_md = skill_path / 'SKILL.md'
    if not skill_md.exists():
        return False, "未找到 SKILL.md", warnings

    content = skill_md.read_text()
    if not content.startswith('---'):
        return False, "未找到 YAML frontmatter", warnings

    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return False, "frontmatter 格式无效", warnings

    try:
        frontmatter = yaml.safe_load(match.group(1))
        if not isinstance(frontmatter, dict):
            return False, "frontmatter 必须是一个 YAML 字典", warnings
    except yaml.YAMLError as e:
        return False, f"frontmatter 中的 YAML 无效: {e}", warnings

    # tools 规则 (a): 产出的技能**必须**声明 `tools` 字段。
    if 'tools' not in frontmatter:
        return False, (
            "产出的技能缺少必填的 'tools' 字段。请在 frontmatter 声明该技能依赖的生成工具，"
            "例如 tools: [\"sandbox_generate_image\"]（仅生图）或 "
            "tools: [\"render_video\", \"sandbox_generate_video\", \"sandbox_process_video\"]（仅生视频）；"
            "既生图又生视频则四个全列。"
        ), warnings

    # tools 规则 (b): 必须是非空列表。
    tools = frontmatter.get('tools')
    if not isinstance(tools, list):
        return False, (
            f"'tools' 必须是一个列表（YAML 数组），得到的是 {type(tools).__name__}。"
            "例如 tools: [\"sandbox_generate_image\"]"
        ), warnings
    if len(tools) == 0:
        return False, (
            "'tools' 不能为空。请至少声明一个生成工具：图片用 \"sandbox_generate_image\"；"
            "视频用 \"render_video\"+\"sandbox_generate_video\"+\"sandbox_process_video\"。"
        ), warnings

    # tools 规则 (c): 取值只能来自允许的白名单。
    tool_set = set(tools)
    unknown_tools = tool_set - ALLOWED_TOOLS
    if unknown_tools:
        return False, (
            f"'tools' 含未知工具: {', '.join(sorted(unknown_tools))}。"
            f"允许的取值: {', '.join(sorted(ALLOWED_TOOLS))}"
        ), warnings

    # tools 规则 (d): 视频三件套必须配套出现，不能只列其一/其二。
    video_used = tool_set & VIDEO_TOOLS
    if video_used and video_used != VIDEO_TOOLS:
        missing_video = VIDEO_TOOLS - tool_set
        return False, (
            "视频生成工具必须配套一起声明。缺少: "
            f"{', '.join(sorted(missing_video))}。"
            "三件套 render_video / sandbox_generate_video / sandbox_process_video 必须同时列出。"
        ), warnings

    # 允许的属性
    unexpected_keys = set(frontmatter.keys()) - ALLOWED_PROPERTIES
    if unexpected_keys:
        return False, (
            f"frontmatter 中存在未预期的 key: {', '.join(sorted(unexpected_keys))}。"
            f"允许的为: {', '.join(sorted(ALLOWED_PROPERTIES))}"
        ), warnings

    # image_model / video_model 规则(可选字段; 出现即校验取值与 tools 自洽性)。
    model_ok, model_msg = _validate_model_fields(frontmatter)
    if not model_ok:
        return False, model_msg, warnings

    # 必需字段
    if 'name' not in frontmatter:
        return False, "frontmatter 中缺少 'name'", warnings
    if 'display_name' not in frontmatter:
        return False, (
            "产出的技能缺少必填的 'display_name' 字段。请在 frontmatter 声明该技能的"
            "中文展示名(给最终用户看)，例如 display_name: 倒挂金钩。"
        ), warnings
    if 'description' not in frontmatter:
        return False, "frontmatter 中缺少 'description'", warnings

    # display_name: 必填、非空、且必须为中文(至少含一个中文字符)。
    display_name = frontmatter.get('display_name', '')
    if not isinstance(display_name, str):
        return False, f"display_name 必须是字符串，得到的是 {type(display_name).__name__}", warnings
    display_name = display_name.strip()
    if not display_name:
        return False, "display_name 不能为空。请填写该技能的中文展示名，例如 display_name: 倒挂金钩。", warnings
    if not CJK_PATTERN.search(display_name):
        return False, (
            f"display_name '{display_name}' 必须为中文(至少包含一个中文字符)。"
            "例如 display_name: 倒挂金钩。"
        ), warnings
    if len(display_name) > 64:
        return False, f"display_name 过长（{len(display_name)} 字符）。最多 64。", warnings
    if len(display_name) >= 10:
        warnings.append(
            f"display_name '{display_name}' 有 {len(display_name)} 个字符，建议尽量控制在 10 个中文字符以内，更简洁易读。"
        )

    # name
    name = frontmatter.get('name', '')
    if not isinstance(name, str):
        return False, f"name 必须是字符串，得到的是 {type(name).__name__}", warnings
    name = name.strip()
    if name:
        if not re.match(r'^[a-z0-9-]+$', name):
            return False, f"name '{name}' 应为 hyphen-case（仅限小写字母、数字、连字符）", warnings
        if name.startswith('-') or name.endswith('-') or '--' in name:
            return False, f"name '{name}' 不能以连字符开头/结尾，也不能含连续连字符", warnings
        if len(name) > 64:
            return False, f"name 过长（{len(name)} 字符）。最多 64。", warnings

    # description
    description = frontmatter.get('description', '')
    if not isinstance(description, str):
        return False, f"description 必须是字符串，得到的是 {type(description).__name__}", warnings
    description = description.strip()
    if description:
        if '<' in description or '>' in description:
            return False, "description 不能含尖括号（< 或 >）", warnings
        if len(description) > 1024:
            return False, f"description 过长（{len(description)} 字符）。最多 1024。", warnings

    # 不打包脚本: 产出的技能不携带可执行脚本，逻辑折叠进文字指令。
    scripts = _scan_scripts(skill_path)
    if scripts:
        return False, (
            f"产出的技能不得打包脚本。发现: {', '.join(scripts)}。"
            f"请改为把逻辑折叠进文字指令中。"
        ), warnings

    # 路径契约(已放宽): 写死绝对/容器路径 -> 失败(应改相对路径)。
    abs_hits = _scan_absolute_paths(skill_path)
    if abs_hits:
        sample = '; '.join(f"{f}:{ln}" for f, ln, _ in abs_hits[:5])
        return False, (
            f"产出的技能内不得写死绝对/容器路径(路径契约: 用相对路径 references/...)。发现于: {sample}"
            + ("..." if len(abs_hits) > 5 else "")
        ), warnings

    # 元信息泄漏: 建造期概念/作者侧元规则不得写进产物 -> 失败。
    leak_hits = _scan_meta_leaks(skill_path)
    if leak_hits:
        sample = '; '.join(f"{f}:{ln}('{term}')" for f, ln, term, _ in leak_hits[:6])
        return False, (
            "产出的技能内泄漏了建造期元信息(保密红线/母库/会话隔离/构建期/纯文本规则 等)。"
            "这些是作者侧元规则，应'照做'而非'写进产物'。请删除。发现于: " + sample
            + ("..." if len(leak_hits) > 6 else "")
        ), warnings

    # 违禁词/不合规内容筛查(警告级, 不阻断——避免误杀正当语境)。
    banned_hits = _scan_banned_content(skill_path)
    if banned_hits:
        sample = '; '.join(f"{f}:{ln}('{term}')" for f, ln, term, _ in banned_hits[:6])
        warnings.append(
            "疑似违禁/不合规词命中, 请人工复核并对违规片段做最小必要删除或改写(其余内容保留): "
            + sample + ("..." if len(banned_hits) > 6 else "")
        )

    # 具名工具/模型泄漏筛查(警告级, 不阻断——名单为启发式, 避免误杀正当引用)。
    named_hits = _scan_named_tools(skill_path)
    if named_hits:
        sample = '; '.join(f"{f}:{ln}('{term}')" for f, ln, term, _ in named_hits[:6])
        warnings.append(
            "疑似点名了具名工具/模型(内部或第三方外部), 产出技能正文应改为能力化表述"
            "(只去掉工具/模型名本身, 分辨率/时长/画幅/帧率/音频等质量参数逐字保留): "
            + sample + ("..." if len(named_hits) > 6 else "")
        )

    ref_root = skill_path / 'references'
    if distill and ref_root.exists() and not with_references:
        return False, (
            "分支 C 默认只能包含 SKILL.md，不得创建 references/。"
            "只有用户明确要求 references 时才允许，并需使用 --with-references 校验。"
        ), warnings

    # 创意类完整性(警告级，不阻断)
    if creative or distill:
        missing = _check_creative_pillars(content)
        if distill and not with_references:
            missing = [item for item in missing if item != "强制加载 reference"]
        if missing:
            warnings.append("创意类支柱可能缺失/未命中信号: " + ", ".join(missing))
        if not distill and not ref_root.is_dir():
            warnings.append("缺少 references/ 词库目录")
        elif ref_root.is_dir():
            ref_count = sum(1 for _ in ref_root.rglob('*.md'))
            if ref_count < 3:
                warnings.append(f"references 下 reference 偏少({ref_count})，建议补充相关行业/体裁词")

    model_bits = [
        f"{f}={frontmatter[f]}" for f in ('image_model', 'video_model') if f in frontmatter
    ]
    model_note = ('、已声明 ' + '/'.join(model_bits)) if model_bits else '、未设置模型字段(走平台默认)'
    ok_msg = f"技能有效!（已声明 tools、含中文 display_name、无脚本、相对路径{model_note}）"
    return True, ok_msg, warnings


def validate_zip(zip_path):
    """用与安装器一致的规则校验最终交付的 .zip 结构。

    安装器只接受两种归档结构:
      (1) SKILL.md 直接位于归档根目录;
      (2) 归档只有一个一级目录，且该目录直接含 SKILL.md。

    返回 (valid: bool, message: str)
    """
    zp = Path(zip_path)
    if not zp.exists():
        return False, f"未找到 ZIP: {zip_path}"
    if not zipfile.is_zipfile(zp):
        return False, f"不是有效的 ZIP 文件: {zip_path}"

    with zipfile.ZipFile(zp) as z:
        raw = z.namelist()

    # 过滤 macOS 元数据目录与隐藏项(与打包时的排除清单口径一致)。
    def _is_noise(name):
        if '__MACOSX' in name:
            return True
        base = posixpath.basename(name.rstrip('/'))
        return base.startswith('.')

    entries = [n for n in raw if n.strip('/') and not _is_noise(n)]
    files = [n for n in entries if not n.endswith('/')]
    root_files = [f for f in files if '/' not in f]
    tops = {n.split('/')[0] for n in entries}

    rule1 = 'SKILL.md' in root_files
    rule2 = len(tops) == 1 and f"{next(iter(tops))}/SKILL.md" in files

    if rule1:
        return True, "PASS: SKILL.md 位于归档根目录，安装器可识别。"
    if rule2:
        return True, f"PASS: SKILL.md 位于唯一顶层目录 '{next(iter(tops))}/' 下，安装器可识别。"

    # 失败: 给出可诊断的顶层项信息，便于定位是"多顶层项"还是"双层嵌套"。
    return False, (
        "FAIL: SKILL.md 既不在归档根目录、也不在唯一顶层目录下，安装器将报 "
        "'SKILL.md not found in skill package'。\n"
        f"  实际顶层项: {sorted(tops)}\n"
        "  修复: 从技能目录内部打包(cd 进目录后 zip . )，并排除 __MACOSX/、.* 等噪声项；"
        "不要出现多个顶层项，也不要把目录再嵌套一层。"
    )


if __name__ == "__main__":
    args = sys.argv[1:]

    # --zip 模式: 校验最终交付归档的结构(安装器同款规则)。
    if '--zip' in args:
        idx = args.index('--zip')
        if idx + 1 >= len(args):
            print("用法: quick_validate.py --zip <path-to-skill.zip>")
            sys.exit(1)
        zip_arg = args[idx + 1]
        print(f"正在校验交付归档: {zip_arg}")
        ok, msg = validate_zip(zip_arg)
        print(msg)
        sys.exit(0 if ok else 1)

    creative = '--creative' in args
    distill = '--distill' in args
    with_references = '--with-references' in args
    positional = [a for a in args if not a.startswith('--')]

    if with_references and not distill:
        print("X --with-references 只能与 --distill 一起使用")
        sys.exit(1)

    if len(positional) != 1:
        print("用法: quick_validate.py <skill-name> [--creative | --distill [--with-references]]")
        print("      quick_validate.py <absolute-path-to-skill> [--creative]")
        print("      quick_validate.py --zip <path-to-skill.zip>")
        print("\n选项:")
        print("  --creative   额外检查创意类 8 支柱齐备(警告级)")
        print("  --distill    校验分支 C 默认只有 SKILL.md、没有 references/")
        print("  --with-references  用户明确要求时允许分支 C 携带 references/")
        print("  --zip <zip>  校验最终交付归档结构(安装器同款规则)")
        print("\n示例:")
        print("  quick_validate.py my-skill")
        print("  quick_validate.py /workspace/.skill_tmp/my-skill --creative")
        print("  quick_validate.py /workspace/.skill_tmp/my-skill --distill")
        print("  quick_validate.py --zip /workspace/assets/my-skill.zip")
        print(f"\n技能在构建期位于 {SKILLS_BASE_PATH}/<skill-name>/")
        sys.exit(1)

    skill_input = positional[0]
    resolved_path = resolve_skill_path(skill_input)
    print(f"正在校验技能: {resolved_path}")

    valid, message, warnings = validate_skill(
        skill_input,
        creative=creative,
        distill=distill,
        with_references=with_references,
    )
    print(message)
    for w in warnings:
        print(f"  ⚠ 提示: {w}")
    sys.exit(0 if valid else 1)
