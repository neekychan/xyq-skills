#!/usr/bin/env python3
"""直接校验实际交付的《故事脚本.md》，只做脚本能确定性判定的结构检查。

设计原则（本轮重构）：脚本只保留“正确产物一定能通过”的确定性结构/格式检查，
不再做任何“首镜必须体现某关键词/某自明钩子”“开场留白与台词是否矛盾”“场景是否
回访”等需要语义理解或依赖有限关键词表的判断——那类检查一个写法正确的脚本换个
说法就永远匹配不上，会让 Agent 反复改写却过不了校验、无限卡死。开场钩子是否成立、
场景是否回访这类创意/语义约束，改由 Agent 依据 `contract-*.md` 正文自行保证。

校验不通过时，errors 里返回自然语言问题描述（中文），直接告诉阅读者哪里出了
问题、该怎么改。"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


EXPECTED_COLUMNS = ["镜号", "时长", "画面描述", "景别", "光影氛围", "对白·旁白", "音效", "运镜"]
INTERNAL_PATTERNS = (
    ("Hook Scope", re.compile(r"\bHook\s*Scope\b", re.I)),
    ("Bridge", re.compile(r"\bBridge\b", re.I)),
    ("Body takeover", re.compile(r"\bBody\s*takeover\b", re.I)),
    ("内部机制编号", re.compile(r"(?<![A-Za-z0-9])(?:BH|SO|S|D|R|H|P)\d{2}(?![A-Za-z0-9])")),
    ("内部字段", re.compile(r"\b(?:selected_content_program|program_lock|opening_hook_contract)\b", re.I)),
)
DURATION_RE = re.compile(r"(\d+(?:\.\d+)?)\s*(?:s|秒)", re.I)


def _cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def _is_separator(cells: list[str]) -> bool:
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell.replace(" ", "")) for cell in cells)


def _load_contract(path: str | None) -> dict[str, Any]:
    if not path:
        return {}
    return json.loads(Path(path).read_text(encoding="utf-8"))


def validate_story_text(text: str, contract: dict[str, Any] | None = None) -> dict[str, Any]:
    contract = contract or {}
    errors: list[str] = []
    details: dict[str, Any] = {}
    lines = text.splitlines()

    h1_lines = [line.strip() for line in lines if line.startswith("# ")]
    if h1_lines != ["# 故事脚本"]:
        errors.append("标题不对：全文有且只能有一个一级标题，且必须是「# 故事脚本」。")

    header_indexes = [i for i, line in enumerate(lines) if line.lstrip().startswith("|") and _cells(line) == EXPECTED_COLUMNS]
    if len(header_indexes) != 1:
        errors.append(
            "分镜表结构不对：全文必须有且只有一张 8 列表格，表头必须是「"
            + " | ".join(EXPECTED_COLUMNS)
            + "」。"
        )
        return {"ok": False, "errors": errors, "details": details}

    header_index = header_indexes[0]
    if header_index + 1 >= len(lines) or not _is_separator(_cells(lines[header_index + 1])):
        errors.append("分镜表缺少合法的表头分隔行（表头下面那行 |---|---| 格式不对）。")

    table_indexes: set[int] = {header_index, header_index + 1}
    rows: list[list[str]] = []
    cursor = header_index + 2
    while cursor < len(lines) and lines[cursor].lstrip().startswith("|"):
        row = _cells(lines[cursor])
        table_indexes.add(cursor)
        if len(row) != len(EXPECTED_COLUMNS):
            errors.append(f"第 {cursor + 1} 行分镜的列数不对：必须正好是 {len(EXPECTED_COLUMNS)} 列。")
        else:
            rows.append(row)
        cursor += 1

    if not rows:
        errors.append("分镜表里没有任何镜头行。")

    bgm_indexes = [i for i, line in enumerate(lines) if line.strip().startswith("**全片 BGM**")]
    if len(bgm_indexes) != 1:
        errors.append("必须有且只有一行「**全片 BGM**」说明。")

    allowed_indexes = {i for i, line in enumerate(lines) if not line.strip()}
    allowed_indexes.update(table_indexes)
    allowed_indexes.update(bgm_indexes)
    allowed_indexes.update(i for i, line in enumerate(lines) if line.strip() == "# 故事脚本")
    extras = [lines[i].strip() for i in range(len(lines)) if i not in allowed_indexes and lines[i].strip()]
    if extras:
        errors.append("故事脚本里混入了多余的、用户不该看到的段落：这个文件只能包含「# 故事脚本」标题、那张分镜表和「**全片 BGM**」一行，请删掉其它内容。")
        details["extra_sections"] = extras[:8]

    for label, pattern in INTERNAL_PATTERNS:
        if pattern.search(text):
            errors.append(f"泄漏了内部工作流标签「{label}」:面向用户的故事脚本不能出现内部机制名/编号/字段名，请删除或改写。")
            details.setdefault("internal_labels", []).append(label)

    durations: list[float] = []
    for row in rows:
        match = DURATION_RE.search(row[1])
        if not match:
            errors.append(f"镜号 {row[0] or '?'} 的时长格式不对：时长列必须写成「数字+秒」或「数字+s」。")
            continue
        durations.append(float(match.group(1)))
    total = round(sum(durations), 3)
    details["duration_seconds"] = total
    expected_duration = contract.get("duration_seconds")
    if expected_duration is not None and abs(total - float(expected_duration)) > 0.2:
        errors.append(f"总时长对不上：各镜头时长加起来是 {total:g} 秒，但要求是 {float(expected_duration):g} 秒。")

    errors = list(dict.fromkeys(errors))
    return {"ok": not errors, "errors": errors, "details": details}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("story_script")
    parser.add_argument("--contract")
    args = parser.parse_args()
    text = Path(args.story_script).read_text(encoding="utf-8")
    result = validate_story_text(text, _load_contract(args.contract))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
