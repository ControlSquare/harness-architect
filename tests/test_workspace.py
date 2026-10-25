from __future__ import annotations

import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import check_workspace  # noqa: E402


class WorkspaceTests(unittest.TestCase):
    def test_example_workspace_passes(self) -> None:
        result = check_workspace.check(ROOT / "examples" / "workspace")
        self.assertEqual(result["errors"], [])

    def test_missing_context_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            copy = Path(tmp) / "workspace"
            shutil.copytree(ROOT / "examples" / "workspace", copy)
            (copy / "02_map" / "CONTEXT.md").unlink()
            result = check_workspace.check(copy)
        self.assertTrue(any("02_map" in error for error in result["errors"]))

    def test_missing_check_heading_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            copy = Path(tmp) / "workspace"
            shutil.copytree(ROOT / "examples" / "workspace", copy)
            context = copy / "04_verify" / "CONTEXT.md"
            context.write_text(context.read_text(encoding="utf-8").replace("## Check", "## Notes"), encoding="utf-8")
            result = check_workspace.check(copy)
        self.assertTrue(any("## Check" in error for error in result["errors"]))

    def test_broken_link_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            copy = Path(tmp) / "workspace"
            shutil.copytree(ROOT / "examples" / "workspace", copy)
            (copy / "01_intake" / "CONTEXT.md").write_text(
                (copy / "01_intake" / "CONTEXT.md").read_text(encoding="utf-8") + "\n[missing](missing.md)\n",
                encoding="utf-8",
            )
            result = check_workspace.check(copy)
        self.assertTrue(any("broken link" in error for error in result["errors"]))


if __name__ == "__main__":
    unittest.main()
