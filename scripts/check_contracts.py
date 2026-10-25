#!/usr/bin/env python3
"""Validate the example skill and adapter manifests without third-party packages."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_REQUIRED = ("name", "version", "description", "inputs", "outputs", "permissions", "failure_policy")
ADAPTER_REQUIRED = ("name", "version", "kind", "operations", "auth", "idempotent")
PERMISSIONS = {"files:read", "files:write", "network:read", "publish:draft", "images:generate"}
KINDS = {"publishing", "storage", "images", "search"}
AUTH = {"none", "api_key", "oauth", "session"}
FAILURE = {"stop", "retry", "fallback", "human"}


def _is_str_map(value) -> bool:
    return isinstance(value, dict) and all(isinstance(v, str) for v in value.values())


def validate_skill(data: dict) -> list[str]:
    errors: list[str] = []
    for key in SKILL_REQUIRED:
        if key not in data:
            errors.append(f"missing field: {key}")

    name = data.get("name", "")
    if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9][a-z0-9-]{1,63}", name):
        errors.append("name must be lowercase kebab-case")

    version = data.get("version", "")
    if not isinstance(version, str) or not re.fullmatch(r"\d+\.\d+\.\d+", version):
        errors.append("version must be semantic, e.g. 1.0.0")

    description = data.get("description", "")
    if not isinstance(description, str) or not 20 <= len(description) <= 280:
        errors.append("description must be 20 to 280 characters")

    if not _is_str_map(data.get("inputs")):
        errors.append("inputs must be a map of string types")
    if not _is_str_map(data.get("outputs")):
        errors.append("outputs must be a map of string types")

    perms = data.get("permissions")
    if not isinstance(perms, list) or any(p not in PERMISSIONS for p in perms):
        errors.append("permissions contain an unknown scope")

    policy = data.get("failure_policy")
    if policy not in FAILURE:
        errors.append("failure_policy must be stop, retry, fallback, or human")

    tests = data.get("tests", [])
    if not isinstance(tests, list) or any(not isinstance(t, str) for t in tests):
        errors.append("tests must be a list of strings")

    return errors


def validate_adapter(data: dict) -> list[str]:
    errors: list[str] = []
    for key in ADAPTER_REQUIRED:
        if key not in data:
            errors.append(f"missing field: {key}")

    name = data.get("name", "")
    if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9][a-z0-9-]{1,63}", name):
        errors.append("name must be lowercase kebab-case")

    version = data.get("version", "")
    if not isinstance(version, str) or not re.fullmatch(r"\d+\.\d+\.\d+", version):
        errors.append("version must be semantic, e.g. 1.0.0")

    if data.get("kind") not in KINDS:
        errors.append("kind must be publishing, storage, images, or search")
    if data.get("auth") not in AUTH:
        errors.append("auth must be none, api_key, oauth, or session")

    ops = data.get("operations")
    if not isinstance(ops, list) or not ops or any(not isinstance(o, str) for o in ops):
        errors.append("operations must be a non-empty list of strings")

    if not isinstance(data.get("idempotent"), bool):
        errors.append("idempotent must be boolean")

    return errors


def classify(data: dict) -> str:
    return "adapter" if "kind" in data else "skill"


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate example manifests.")
    parser.add_argument("paths", nargs="*", type=Path)
    args = parser.parse_args()

    paths = args.paths or [
        ROOT / "examples" / "skill.research-brief.json",
        ROOT / "examples" / "adapter.substack.json",
    ]

    failed = False
    for path in paths:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            print(f"{path}: cannot read: {exc}")
            failed = True
            continue

        kind = classify(data)
        errors = validate_skill(data) if kind == "skill" else validate_adapter(data)
        if errors:
            failed = True
            print(f"{path}: {len(errors)} error(s)")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"{path}: OK ({kind})")

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
