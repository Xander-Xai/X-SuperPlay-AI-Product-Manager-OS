#!/usr/bin/env python3
"""Offline demand-driven learning router. No network, no personal data."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "docs/atlas/knowledge-catalog.json"
SOURCES = ROOT / "resources/authorities.json"
SCENARIOS = ROOT / "docs/scenarios/scenarios.json"
UPSTREAM = ROOT / "resources/upstream-pm-knowledge-index.json"

def read():
    topics = json.loads(DATA.read_text(encoding="utf-8"))["topics"]
    sources = json.loads(SOURCES.read_text(encoding="utf-8"))["sources"]
    scenarios = json.loads(SCENARIOS.read_text(encoding="utf-8"))["scenarios"]
    return topics, sources, scenarios

def check():
    topics, sources, scenarios = read()
    errs = []
    by_id = {t["id"]: t for t in topics}
    src = {s["id"]: s for s in sources}
    if len(by_id) != len(topics) or len(src) != len(sources):
        errs.append("Duplicate topic/source IDs")
    for t in topics:
        if not all(t.get(k) for k in ("name","why","exercise","evidence","trigger","resources")):
            errs.append("Incomplete topic: " + t.get("id","?"))
        for dep in t["requires"]:
            if dep not in by_id: errs.append(f"Unknown dependency {t['id']} -> {dep}")
        for sid in t["resources"]:
            if sid not in src: errs.append(f"Unknown source {t['id']} -> {sid}")
    state, stack = {}, []
    def visit(k):
        if state.get(k) == 2: return
        if state.get(k) == 1:
            errs.append("Cycle: " + " > ".join(stack + [k])); return
        state[k] = 1; stack.append(k)
        for dep in by_id[k]["requires"]:
            if dep in by_id: visit(dep)
        stack.pop(); state[k] = 2
    for k in by_id: visit(k)
    for s in scenarios:
        if not (ROOT / f"docs/scenarios/{s['id']}.md").exists():
            errs.append("No scenario document: " + s["id"])
        for t in s["topics"]:
            if t not in by_id: errs.append("Unknown scenario topic: " + t)
    if len(topics) < 50 or len(sources) < 18 or len(scenarios) < 5:
        errs.append("Coverage below minimum documented curriculum scope")
    return errs, topics, sources, scenarios

def route(key, deep=False):
    errs, topics, sources, _ = check()
    if errs: raise ValueError("\n".join(errs))
    by = {t["id"]: t for t in topics}
    src = {s["id"]: s for s in sources}
    if key not in by: raise ValueError(f"Unknown knowledge ID {key}; use list/search")
    chosen = [key]; seen = {key}
    def add(i):
        for dep in by[i]["requires"]:
            if dep not in seen:
                seen.add(dep); chosen.append(dep)
                if deep: add(dep)
    add(key)
    for i in chosen:
        t=by[i]
        print(f"[{i}] {t['name']} {'<-- TARGET' if i==key else '<-- concept prerequisite'}")
        print("  Why:", t["why"])
        if t.get("definition"): print("  Definition:", t["definition"])
        if t.get("plain"): print("  Plain language:", t["plain"])
        print("  Trigger:", t["trigger"])
        print("  Dependencies:", ", ".join(t["requires"]) or "none")
        print("  Experiment:", t["exercise"])
        print("  Evidence:", t["evidence"])
        for sid in t["resources"]:
            s=src[sid]
            print("  Source:", sid, s["title"], s["url"])
    refs = json.loads(UPSTREAM.read_text(encoding="utf-8"))["references"]
    for ref in refs:
        if key in ref["target_ids"]:
            print("  Private upstream reference:", ref["id"], ref["area"], ref["url"], "(requires access)")
    return chosen

def main(argv=None):
    parser=argparse.ArgumentParser(description="Demand -> knowledge dependencies -> official sources -> exercise")
    sub=parser.add_subparsers(dest="command", required=True)
    sub.add_parser("list")
    look=sub.add_parser("search"); look.add_argument("text")
    r=sub.add_parser("route"); r.add_argument("id"); r.add_argument("--deep",action="store_true")
    s=sub.add_parser("scenario"); s.add_argument("id")
    sub.add_parser("validate")
    a=parser.parse_args(argv)
    errs, topics, sources, scenarios=check()
    if errs: print("\n".join(errs),file=sys.stderr); return 2
    if a.command=="validate":
        print(f"OK: {len(topics)} nodes, {len(sources)} sources, {len(scenarios)} scenarios; no dangling IDs/cycles")
    elif a.command=="list":
        for t in topics: print(t["id"],t["domain"],t["name"],"=>",t["trigger"])
    elif a.command=="search":
        q=a.text.casefold(); m=[t for t in topics if q in " ".join([t["id"],t["name"],t["why"],t["trigger"],t["exercise"]]).casefold()]
        for t in m: print(t["id"], t["name"], "->", t["trigger"])
        if not m: print("No match; check full Atlas or adjust keyword")
    elif a.command=="route":
        try: route(a.id, a.deep)
        except ValueError as e: print(str(e),file=sys.stderr); return 2
    else:
        found=next((v for v in scenarios if v["id"]==a.id),None)
        if found is None: print("Unknown scenario; try: "+", ".join(v["id"] for v in scenarios),file=sys.stderr); return 2
        print("Scenario:",found["title"],"\nFailures:",found["failure_cases"],"\nSuccess evidence:",found["done"])
        print("Suggested topic set (select only current primary gap):",", ".join(found["topics"]))
        route(found["topics"][0])
    return 0

if __name__=="__main__":
    raise SystemExit(main())
