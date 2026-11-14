#!/usr/bin/env python3
"""Check curriculum entrypoints, Markdown relative links and obvious public safety gaps."""
from pathlib import Path
from urllib.parse import unquote
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
required = [
    "README.md", "ROADMAP.md", "GOVERNANCE.md",
    "05-AI-Product-Management/README.md",
    "09-Product-Engineering/README.md",
    "09-Product-Engineering/roadmap.md",
    "09-Product-Engineering/30-60-90.md",
    "09-Product-Engineering/lab-track.md",
    "12-Assessments/rubric.md",
    "resources/source-migration-map.md",
]
errors = []
for name in required:
    if not (ROOT / name).is_file():
        errors.append("Missing: " + name)

# Match standard Markdown link targets, including image links; external URLs excluded below.
link_re = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
checked = 0
for file in ROOT.rglob("*.md"):
    content = file.read_text(encoding="utf-8")
    for raw in link_re.findall(content):
        target_text = raw.strip().split(" ", 1)[0].strip("<>")
        if target_text.startswith(("https://", "http://", "mailto:", "#")):
            continue
        local = unquote(target_text.split("#", 1)[0].split("?", 1)[0])
        if not local:
            continue
        checked += 1
        target = (file.parent / local).resolve()
        try:
            target.relative_to(ROOT.resolve())
        except ValueError:
            errors.append("Path escapes repo: " + str(file.relative_to(ROOT)) + " -> " + local)
            continue
        if not target.exists():
            errors.append("Broken local link: " + str(file.relative_to(ROOT)) + " -> " + local)

if checked < 25:
    errors.append("Too few internal Markdown links examined: " + str(checked))
if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"OK: {checked} local links checked; all key files and links exist")
