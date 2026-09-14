#!/usr/bin/env python3
"""Report optional parser dependencies for universal-file-reader."""

from __future__ import annotations

import json
import shutil


GROUPS = {
    "pdf": {
        "modules": ["fitz", "pdfplumber", "pypdf"],
        "commands": ["pdftotext"],
        "install": "python3 -m pip install pymupdf pdfplumber pypdf; brew install poppler  # macOS, or apt-get install poppler-utils on Linux",
    },
    "spreadsheet": {
        "modules": ["pandas", "openpyxl", "xlrd", "pyxlsb", "python_calamine", "odf"],
        "commands": [],
        "install": "python3 -m pip install pandas openpyxl xlrd pyxlsb python-calamine odfpy",
    },
    "office": {
        "modules": ["docx", "pptx"],
        "commands": [],
        "install": "python3 -m pip install python-docx python-pptx",
    },
    "html": {
        "modules": ["bs4", "lxml"],
        "commands": [],
        "install": "python3 -m pip install beautifulsoup4 lxml",
    },
}


def module_status(module: str) -> bool:
    try:
        __import__(module)
        return True
    except Exception:
        return False


def main() -> int:
    report = {}
    for group, details in GROUPS.items():
        modules = {module: module_status(module) for module in details["modules"]}
        commands = {command: bool(shutil.which(command)) for command in details["commands"]}
        report[group] = {
            "ok": any(modules.values()) or any(commands.values()),
            "modules": modules,
            "commands": commands,
            "install": details["install"],
        }
    report["system"] = {
        "libreoffice_soffice": bool(shutil.which("soffice")),
        "libreoffice_note": "Install LibreOffice for .doc/.ppt conversion, .xls repair, and formula recalculation.",
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
