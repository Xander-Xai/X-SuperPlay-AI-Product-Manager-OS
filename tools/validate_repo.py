#!/usr/bin/env python3
"""Validate local Markdown paths and curriculum entrypoints (stdlib only)."""
from pathlib import Path
from urllib.parse import unquote
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
required = [
    "README.md", "ROADMAP.md", "GOVERNANCE.md",
    "05-AI-Product-Management/README.md",
    "09-Product-Engineering/README.md",
    "09-Product-Engineering/30-60-90.md",
    "12-Assessments/rubric.md", "resources/source-migration-map.md",
]
errors = []
for name in required:
    if not (ROOT / name).is_file():
        errors.append("Missing required path: " + name)

markdown = list(ROOT.rglob("*.md"))
link_re = re.compile(r"!?(?:\\[[^\\]]*\\])\\(([^)]+)\\)")
for file in markdown:
    contents = file.read_text(encoding="utf-8")
    for raw in link_re.findall(contents):
        url = raw.strip().split(" ", 1)[0].strip("<>")
        if url.startswith(("https://", "http://", "mailto:", "#")):
            continue
        local = unquote(url.split("#", 1)[0].split("?", 1)[0])
        if not local:
            continue
        target = (file.parent / local).resolve()
        if ROOT.resolve() not in target.parents and target != ROOT.resolve():
            errors.append("Escaping path: " + str(file.relative_to(ROOT)) + " -> " + url)
        elif not target.exists():
            errors.append("Broken local link: " + str(file.relative_to(ROOT)) + " -> " + url)
if errors:
    print("\\n".join(errors))
    sys.exit(1)
print("OK:", len(markdown), "markdown files; core entrypoints and local links")
