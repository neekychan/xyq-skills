#!/usr/bin/env python3
"""Dispatch local file parsing into Markdown and JSON outputs."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from parse_office import parse_docx, parse_pptx
from parse_pdf import parse_pdf
from parse_spreadsheet import parse_spreadsheet
from parse_text import parse_text


SPREADSHEET_EXTENSIONS = {".xls", ".xlsx", ".xlsm", ".xlsb", ".ods", ".csv", ".tsv"}
PDF_EXTENSIONS = {".pdf"}
DOCX_EXTENSIONS = {".docx"}
PPTX_EXTENSIONS = {".pptx"}
TEXT_EXTENSIONS = {".txt", ".md", ".markdown", ".json", ".xml", ".html", ".htm", ".log"}
LEGACY_OFFICE_EXTENSIONS = {".doc", ".ppt"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Read a local file and write Markdown plus JSON extraction outputs."
    )
    parser.add_argument("input", help="Input file path")
    parser.add_argument("--out-dir", help="Output directory. Defaults to <input>.parsed")
    parser.add_argument(
        "--stdout",
        nargs="?",
        const="markdown",
        choices=["markdown", "json"],
        help="Print parsed content to stdout. Defaults to Markdown when no value is provided.",
    )
    parser.add_argument(
        "--no-write",
        action="store_true",
        help="Do not write content.md/content.json. Useful with --stdout.",
    )
    parser.add_argument(
        "--max-rows",
        type=int,
        default=0,
        help="Spreadsheet/CSV data row limit. Default 0 means no limit.",
    )
    parser.add_argument("--all-rows", action="store_true", help="Read all spreadsheet/CSV rows.")
    parser.add_argument("--max-pages", type=int, help="PDF page limit")
    parser.add_argument("--max-chars", type=int, default=0, help="Text output character limit. Default 0 means no limit.")
    parser.add_argument("--sheet", help="Spreadsheet sheet name to parse")
    parser.add_argument(
        "--data-only",
        action="store_true",
        help="For openpyxl-backed workbooks, read cached formula results instead of formulas.",
    )
    return parser.parse_args()


def write_outputs(result: dict, out_dir: Path) -> dict:
    out_dir.mkdir(parents=True, exist_ok=True)
    md_path = out_dir / "content.md"
    json_path = out_dir / "content.json"

    md_path.write_text(result.get("markdown", "").rstrip() + "\n", encoding="utf-8")
    serializable = {k: v for k, v in result.items() if k != "markdown"}
    json_path.write_text(
        json.dumps(serializable, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return {"markdown": str(md_path), "json": str(json_path)}


def structured_result(result: dict) -> dict:
    return {k: v for k, v in result.items() if k != "markdown"}


def convert_legacy_office(path: Path) -> None:
    suffix = path.suffix.lower()
    target = "docx" if suffix == ".doc" else "pptx"
    raise RuntimeError(
        f"Legacy {suffix} files should be converted first. Try: "
        f"soffice --headless --convert-to {target} --outdir /tmp {path}"
    )


def parse_file(path: Path, args: argparse.Namespace) -> dict:
    suffix = path.suffix.lower()
    if suffix in PDF_EXTENSIONS:
        return parse_pdf(path, max_pages=args.max_pages, max_chars=args.max_chars)
    if suffix in SPREADSHEET_EXTENSIONS:
        max_rows = 0 if args.all_rows else args.max_rows
        return parse_spreadsheet(
            path,
            max_rows=max_rows,
            sheet=args.sheet,
            data_only=args.data_only,
        )
    if suffix in DOCX_EXTENSIONS:
        return parse_docx(path, max_chars=args.max_chars)
    if suffix in PPTX_EXTENSIONS:
        return parse_pptx(path, max_chars=args.max_chars)
    if suffix in TEXT_EXTENSIONS or not suffix:
        return parse_text(path, max_chars=args.max_chars)
    if suffix in LEGACY_OFFICE_EXTENSIONS:
        convert_legacy_office(path)
    raise RuntimeError(f"Unsupported file type: {suffix or '(no extension)'}")


def main() -> int:
    args = parse_args()
    input_path = Path(args.input).expanduser().resolve()
    if not input_path.is_file():
        print(f"Input file not found: {input_path}", file=sys.stderr)
        return 1

    out_dir = None
    if not args.no_write:
        out_dir = (
            Path(args.out_dir).expanduser().resolve()
            if args.out_dir
            else Path(f"{input_path}.parsed").resolve()
        )

    try:
        result = parse_file(input_path, args)
        outputs = write_outputs(result, out_dir) if out_dir else {}
    except Exception as exc:
        print(f"Parse failed: {exc}", file=sys.stderr)
        return 1

    if args.stdout == "markdown":
        sys.stdout.write(result.get("markdown", "").rstrip() + "\n")
        return 0
    if args.stdout == "json":
        print(json.dumps(structured_result(result), ensure_ascii=False, indent=2))
        return 0

    summary = {
        "input": str(input_path),
        "parser": result.get("parser"),
        "outputs": outputs,
        "warnings": result.get("warnings", []),
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
