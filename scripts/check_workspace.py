#!/usr/bin/env python3
"""Check a harness workspace for entry files, stage contracts, and broken relative links."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

STAGE_RE = re.compile(r"^\d{2}_")
REQUIRED_HEADINGS = ("reads", "does", "writes", "check")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def relative_links(text: str) -> list[str]:
    links = []
    for target in LINK_RE.findall(text):
        target = target.strip().split("#", 1)[0]
        if not target or target.startswith(("http://", "https://", "mailto:", "/", "#")):
            continue
        links.append(target)
    return links


def check(workspace: Path) -> dict:
    errors: list[str] = []
    agents = workspace / "AGENTS.md"
    if not agents.exists():
        errors.append("missing AGENTS.md")
        return {"path": str(workspace), "stages": [], "errors": errors}

    stages = sorted([p for p in workspace.iterdir() if p.is_dir() and STAGE_RE.match(p.name)])
    if not stages:
        errors.append("no numbered stage folders")

    for stage in stages:
        context = stage / "CONTEXT.md"
        if not context.exists():
            errors.append(f"{stage.name}: missing CONTEXT.md")
            continue
        body = context.read_text(encoding="utf-8")
        lowered = body.lower()
        for heading in REQUIRED_HEADINGS:
            if f"## {heading}" not in lowered:
                errors.append(f"{stage.name}: missing ## {heading.title()}")

    for source in [agents] + [s / "CONTEXT.md" for s in stages if (s / "CONTEXT.md").exists()]:
        body = source.read_text(encoding="utf-8")
        for target in relative_links(body):
            resolved = (source.parent / target).resolve()
            if not resolved.exists():
                errors.append(f"{source.relative_to(workspace)}: broken link: {target}")

    return {"path": str(workspace), "stages": [s.name for s in stages], "errors": errors}


def main() -> int:
    parser = argparse.ArgumentParser(description="Check a harness workspace.")
    parser.add_argument("workspace", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    if not args.workspace.exists():
        print(f"not found: {args.workspace}")
        return 2

    result = check(args.workspace)

    if args.json:
        print(json.dumps(result, indent=2))
    elif result["errors"]:
        print(f"{args.workspace}: {len(result['errors'])} error(s)")
        for error in result["errors"]:
            print(f"  - {error}")
    else:
        print(f"{args.workspace}: OK ({len(result['stages'])} stages)")

    return 1 if result["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
