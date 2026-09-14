#!/usr/bin/env python3
"""Parse PDF files with optional PyMuPDF, pdfplumber, pdftotext, or pypdf engines."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Iterable


def _truncate(text: str, max_chars: int | None) -> str:
    if max_chars is None or max_chars <= 0 or len(text) <= max_chars:
        return text
    return text[:max_chars] + "\n\n[truncated]\n"


def _table_to_markdown(rows: Iterable[Iterable[object]]) -> str:
    normalized = [["" if cell is None else str(cell).replace("\n", " ").strip() for cell in row] for row in rows]
    if not normalized:
        return ""
    width = max(len(row) for row in normalized)
    normalized = [row + [""] * (width - len(row)) for row in normalized]
    header = normalized[0]
    body = normalized[1:]
    lines = [
        "| " + " | ".join(header) + " |",
        "| " + " | ".join(["---"] * width) + " |",
    ]
    lines.extend("| " + " | ".join(row) + " |" for row in body)
    return "\n".join(lines)


def _parse_with_pymupdf(path: Path, max_pages: int | None) -> tuple[list[dict], list[str]]:
    import fitz

    pages: list[dict] = []
    warnings: list[str] = []
    with fitz.open(path) as doc:
        limit = min(len(doc), max_pages or len(doc))
        for index in range(limit):
            page = doc[index]
            text = page.get_text("text").strip()
            if not text:
                warnings.append(f"Page {index + 1} returned no text.")
            pages.append({"page": index + 1, "text": text, "tables": []})
    return pages, warnings


def _parse_with_pdfplumber(path: Path, max_pages: int | None) -> tuple[list[dict], list[str]]:
    import pdfplumber

    pages: list[dict] = []
    warnings: list[str] = []
    with pdfplumber.open(path) as pdf:
        limit = min(len(pdf.pages), max_pages or len(pdf.pages))
        for index, page in enumerate(pdf.pages[:limit], start=1):
            text = (page.extract_text() or "").strip()
            tables = page.extract_tables() or []
            table_payloads = [{"rows": table, "markdown": _table_to_markdown(table)} for table in tables]
            if not text and not table_payloads:
                warnings.append(f"Page {index} returned no text or tables.")
            pages.append({"page": index, "text": text, "tables": table_payloads})
    return pages, warnings


def _parse_with_pypdf(path: Path, max_pages: int | None) -> tuple[list[dict], list[str]]:
    from pypdf import PdfReader

    reader = PdfReader(str(path))
    pages: list[dict] = []
    warnings: list[str] = []
    limit = min(len(reader.pages), max_pages or len(reader.pages))
    for index in range(limit):
        text = (reader.pages[index].extract_text() or "").strip()
        if not text:
            warnings.append(f"Page {index + 1} returned no text.")
        pages.append({"page": index + 1, "text": text, "tables": []})
    return pages, warnings


def _parse_with_pdftotext(path: Path, max_pages: int | None) -> tuple[list[dict], list[str]]:
    binary = shutil.which("pdftotext")
    if not binary:
        raise RuntimeError("pdftotext executable not found.")

    command = [binary, "-layout", "-enc", "UTF-8"]
    if max_pages:
        command.extend(["-f", "1", "-l", str(max_pages)])
    command.extend([str(path), "-"])

    completed = subprocess.run(
        command,
        check=False,
        capture_output=True,
        text=True,
    )
    if completed.returncode != 0:
        stderr = completed.stderr.strip() or "no stderr"
        raise RuntimeError(f"pdftotext exited with {completed.returncode}: {stderr}")

    raw_pages = completed.stdout.split("\f")
    pages = []
    warnings = []
    for index, text in enumerate(raw_pages, start=1):
        cleaned = text.strip()
        if not cleaned and index == len(raw_pages):
            continue
        if not cleaned:
            warnings.append(f"Page {index} returned no text.")
        pages.append({"page": index, "text": cleaned, "tables": []})

    stderr = completed.stderr.strip()
    if stderr:
        warnings.append(f"pdftotext stderr: {stderr}")
    return pages, warnings


def parse_pdf(path: Path, max_pages: int | None = None, max_chars: int | None = 0) -> dict:
    engines = [
        ("pymupdf", _parse_with_pymupdf, "python3 -m pip install pymupdf"),
        ("pdfplumber", _parse_with_pdfplumber, "python3 -m pip install pdfplumber"),
        ("pdftotext", _parse_with_pdftotext, "brew install poppler  # macOS, or apt-get install poppler-utils on Linux"),
        ("pypdf", _parse_with_pypdf, "python3 -m pip install pypdf"),
    ]
    errors: list[str] = []

    for engine_name, parser, install_hint in engines:
        try:
            pages, warnings = parser(path, max_pages)
            markdown_parts = [f"# {path.name}", "", f"Parser: `{engine_name}`", ""]
            for page in pages:
                markdown_parts.extend([f"## Page {page['page']}", "", page.get("text", ""), ""])
                for table_index, table in enumerate(page.get("tables", []), start=1):
                    markdown_parts.extend([f"### Table {table_index}", "", table.get("markdown", ""), ""])
            markdown = _truncate("\n".join(markdown_parts).strip(), max_chars)
            if not any(page.get("text") or page.get("tables") for page in pages):
                warnings.append("No extractable text found. This may be a scanned or image-only PDF.")
            return {
                "parser": engine_name,
                "file_type": "pdf",
                "source": str(path),
                "pages": pages,
                "warnings": warnings,
                "markdown": markdown,
            }
        except ModuleNotFoundError as exc:
            errors.append(f"{engine_name}: missing {exc.name}. Install with: {install_hint}")
        except Exception as exc:
            errors.append(f"{engine_name}: {exc}")

    raise RuntimeError("No PDF parser succeeded. " + " | ".join(errors))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Parse a PDF into Markdown/JSON.")
    parser.add_argument("input")
    parser.add_argument("-o", "--output", help="Markdown output path")
    parser.add_argument("--json", help="JSON output path")
    parser.add_argument("--max-pages", type=int)
    parser.add_argument("--max-chars", type=int, default=0, help="Maximum Markdown characters. Default 0 means no limit.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    path = Path(args.input).expanduser().resolve()
    try:
        result = parse_pdf(path, max_pages=args.max_pages, max_chars=args.max_chars)
    except Exception as exc:
        print(f"PDF parse failed: {exc}", file=sys.stderr)
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
