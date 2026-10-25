from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import check_contracts  # noqa: E402


class ContractTests(unittest.TestCase):
    def test_examples_pass(self) -> None:
        skill = check_contracts.json.loads((ROOT / "examples" / "skill.research-brief.json").read_text(encoding="utf-8"))
        adapter = check_contracts.json.loads((ROOT / "examples" / "adapter.substack.json").read_text(encoding="utf-8"))
        self.assertEqual(check_contracts.validate_skill(skill), [])
        self.assertEqual(check_contracts.validate_adapter(adapter), [])

    def test_bad_permission_fails(self) -> None:
        skill = {
            "name": "example",
            "version": "1.0.0",
            "description": "A valid description for a test skill.",
            "inputs": {"topic": "string"},
            "outputs": {"path": "path"},
            "permissions": ["root:everything"],
            "failure_policy": "stop",
            "tests": ["one"],
        }
        errors = check_contracts.validate_skill(skill)
        self.assertTrue(any("permission" in error for error in errors))

    def test_bad_adapter_kind_fails(self) -> None:
        adapter = {
            "name": "example",
            "version": "1.0.0",
            "kind": "telepathy",
            "operations": ["do"],
            "auth": "none",
            "idempotent": True,
        }
        errors = check_contracts.validate_adapter(adapter)
        self.assertTrue(any("kind" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
