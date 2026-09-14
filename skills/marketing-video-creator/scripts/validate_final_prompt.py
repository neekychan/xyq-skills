#!/usr/bin/env python3
"""扫描实际的《视频生成Prompt.md》，只做脚本能确定性判定的结构与冲突检查。

设计原则（本轮重构）：**脚本只保留“正确产物一定能通过”的确定性检查**，
不再做任何“必须出现某个措辞/关键词/句式”的正向关键词匹配，也不做需要语义
理解的分类判断（静态收尾 vs 真实动作、开场留白、尺寸类比等）。原因：那类
检查依赖有限的关键词表，而一个写法正确的 Prompt 换个说法就会永远匹配不上，
导致 Agent 反复改写却始终过不了校验、无限卡死。那些语义/创意层面的约束改由
Agent 依据各 `contract-*.md` 正文自行保证，不再交给脚本裁决。

保留的检查都属于两类不会误伤正确产物的判定：
1. **结构/格式**：能否解析出带时间戳的分镜节拍（正确产物本来就有）。
2. **禁止项缺席 + 自相矛盾**：某个明确的禁用词不能出现、互斥指令不能同时出现
   （正确产物本来就不会踩，属于确定性回归网）。

校验不通过时，errors 里返回自然语言问题描述（中文），直接说清哪里出了问题、
该怎么改。
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


TIME_RANGE = re.compile(
    r"(?P<start>\d+(?:\.\d+)?)\s*(?:s|秒)?\s*[-–—~至]\s*"
    r"(?P<end>\d+(?:\.\d+)?)\s*(?:s|秒)",
    re.IGNORECASE,
)
NO_TEXT_TERMS = ("无字幕", "不要字幕", "不出现任何文字", "无画面文字", "no subtitles")
ADD_TEXT_TERMS = ("花字", "字幕出现", "出现字幕", "底部字幕", "屏幕文字", "on-screen text")


def _norm(value: Any) -> str:
    return str(value or "").strip().lower()


def _as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _contains_any(text: str, terms: list[str] | tuple[str, ...]) -> bool:
    lowered = text.lower()
    return any(_norm(term) in lowered for term in terms if _norm(term))


def parse_timeline(prompt: str) -> list[dict[str, Any]]:
    timeline_start = 0
    for marker in ("各个分镜", "分镜具体内容", "timestamped beats"):
        position = prompt.lower().find(marker.lower())
        if position >= 0:
            timeline_start = max(timeline_start, position)
    timeline_text = prompt[timeline_start:]
    matches = list(TIME_RANGE.finditer(timeline_text))
    beats: list[dict[str, Any]] = []
    for index, match in enumerate(matches):
        start = float(match.group("start"))
        end = float(match.group("end"))
        block_end = (
            matches[index + 1].start() if index + 1 < len(matches) else len(timeline_text)
        )
        beats.append(
            {
                "start": start,
                "end": end,
                "duration": max(0.0, end - start),
                "text": timeline_text[match.start():block_end],
            }
        )
    return beats


def _flatten_forbidden_imports(value: Any) -> list[str]:
    terms: list[str] = []
    for item in _as_list(value):
        if isinstance(item, str):
            terms.append(item)
        elif isinstance(item, dict):
            terms.extend(str(term) for term in _as_list(item.get("terms")))
    return terms


def validate_prompt(prompt: str, contract: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    lowered = prompt.lower()
    beats = parse_timeline(prompt)

    # 1. 结构门：必须能解析出带时间戳的分镜节拍。正确产物本来就有。
    if not beats:
        errors.append("最终 Prompt 里找不到可解析的分镜时间轴：必须写成「0-3秒」这样的带时间戳的分镜节拍。")

    # 2. 禁止项缺席门：这些是明确列出的禁用词，正确产物本来就不会出现。
    #    只做“不能出现”判定，不做“必须出现某措辞”的正向匹配（后者会误伤正确产物、导致卡死）。
    for term in _as_list(contract.get("forbidden_sku_terms")):
        if _norm(term) in lowered:
            errors.append(f"最终 Prompt 里出现了禁用的 SKU 变体/材质术语「{term}」:请删掉，它和锁定的 SKU 不符。")
    for term in _as_list(contract.get("unsupported_claim_terms")):
        if _norm(term) in lowered:
            errors.append(f"最终 Prompt 里出现了无证据支撑的宣称「{term}」:没有证据的功效话术不能写。")

    forbidden_imports = _flatten_forbidden_imports(contract.get("forbidden_imports"))
    for term in forbidden_imports:
        if _norm(term) in lowered:
            errors.append(f"最终 Prompt 里混入了被禁止的方案外来元素「{term}」:请删掉，它不属于选定方案。")

    # 3. 自相矛盾门:字幕指令不能既要“无字幕”又要“出现字幕/花字”。
    if _contains_any(prompt, NO_TEXT_TERMS) and _contains_any(prompt, ADD_TEXT_TERMS):
        errors.append("字幕/画面文字指令自相矛盾：Prompt 里既要求「无字幕」又要求「出现字幕/花字」，二者只能留一个。")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt", help="Path to the actual 视频生成Prompt Markdown")
    parser.add_argument("--contract", required=True, help="Path to internal JSON lock")
    args = parser.parse_args()

    prompt = Path(args.prompt).read_text(encoding="utf-8")
    contract = json.loads(Path(args.contract).read_text(encoding="utf-8"))
    errors = validate_prompt(prompt, contract)
    result = {"ok": not errors, "errors": errors}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
