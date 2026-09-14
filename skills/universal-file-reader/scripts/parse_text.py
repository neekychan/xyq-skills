#!/usr/bin/env python3
"""Parse text-like files into Markdown and compact metadata."""

from __future__ import annotations

import argparse
import html.parser
import json
import sys
from pathlib import Path
from xml.etree import ElementTree as ET


class TextHTMLParser(html.parser.HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []

    def handle_data(self, data: str) -> None:
        text = data.strip()
        if text:
            self.parts.append(text)


def _read_text(path: Path) -> tuple[str, str]:
    for encoding in ("utf-8-sig", "utf-8", "gb18030", "latin-1"):
        try:
            return path.read_text(encoding=encoding), encoding
        except UnicodeDecodeError:
            continue
    return path.read_text(errors="replace"), "replace"


def _truncate(text: str, max_chars: int | None) -> tuple[str, list[str]]:
    if max_chars is None or max_chars <= 0 or len(text) <= max_chars:
        return text, []
    return text[:max_chars] + "\n\n[truncated]\n", [f"Text limited to {max_chars} characters."]


def _parse_json(text: str) -> tuple[str, dict, list[str]]:
    data = json.loads(text)
    if isinstance(data, dict):
        meta = {"json_type": "object", "keys": list(data.keys())[:100]}
    elif isinstance(data, list):
        meta = {"json_type": "array", "length": len(data)}
    else:
        meta = {"json_type": type(data).__name__}
    pretty = json.dumps(data, ensure_ascii=False, indent=2)
    return f"```json\n{pretty}\n```", meta, []


def _parse_xml(text: str) -> tuple[str, dict, list[str]]:
    root = ET.fromstring(text)
    meta = {"root_tag": root.tag, "child_count": len(list(root))}
    return f"```xml\n{text.strip()}\n```", meta, []


def _parse_html(text: str) -> tuple[str, dict, list[str]]:
    try:
        from bs4 import BeautifulSoup

        soup = BeautifulSoup(text, "html.parser")
        title = soup.title.string.strip() if soup.title and soup.title.string else ""
        visible = soup.get_text("\n", strip=True)
        return visible, {"title": title}, []
    except ModuleNotFoundError:
        parser = TextHTMLParser()
        parser.feed(text)
        return "\n".join(parser.parts), {}, ["beautifulsoup4 not installed; used basic HTMLParser fallback."]


def parse_text(path: Path, max_chars: int | None = 0) -> dict:
    text, encoding = _read_text(path)
    suffix = path.suffix.lower()
    warnings: list[str] = []
    meta: dict = {"encoding": encoding}
    content = text
    parser = "plain-text"

    try:
        if suffix == ".json":
            content, parsed_meta, parsed_warnings = _parse_json(text)
            meta.update(parsed_meta)
            warnings.extend(parsed_warnings)
            parser = "json"
        elif suffix == ".xml":
            content, parsed_meta, parsed_warnings = _parse_xml(text)
            meta.update(parsed_meta)
            warnings.extend(parsed_warnings)
            parser = "xml"
        elif suffix in {".html", ".htm"}:
            content, parsed_meta, parsed_warnings = _parse_html(text)
            meta.update(parsed_meta)
            warnings.extend(parsed_warnings)
            parser = "html"
    except Exception as exc:
        warnings.append(f"Structured parsing failed, returned raw text instead: {exc}")
        content = text

    content, truncate_warnings = _truncate(content, max_chars)
    warnings.extend(truncate_warnings)
    markdown = f"# {path.name}\n\nParser: `{parser}`\n\n{content.strip()}"
    return {
        "parser": parser,
        "file_type": suffix.lstrip(".") or "text",
        "source": str(path),
        "metadata": meta,
        "warnings": warnings,
        "markdown": markdown,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Parse text-like files into Markdown/JSON.")
    parser.add_argument("input")
    parser.add_argument("-o", "--output", help="Markdown output path")
    parser.add_argument("--json", help="JSON output path")
    parser.add_argument("--max-chars", type=int, default=0, help="Maximum Markdown characters. Default 0 means no limit.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    path = Path(args.input).expanduser().resolve()
    try:
        result = parse_text(path, max_chars=args.max_chars)
    except Exception as exc:
        print(f"Text parse failed: {exc}", file=sys.stderr)
        return 1

    if args.output:
        Path(args.output).expanduser().resolve().write_text(result["markdown"] + "\n", encoding="utf-8")
    else:
        print(result["markdown"])
    if args.json:
        Path(args.json).expanduser().resolve().write_text(
            json.dumps({k: v for k, v in result.items() if k != "markdown"}, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
