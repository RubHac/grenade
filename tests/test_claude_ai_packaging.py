import importlib.util
import tempfile
import unittest
from pathlib import Path
from zipfile import ZipFile

REPO = Path(__file__).resolve().parents[1]
MODULE = REPO / "scripts" / "build_claude_ai_skill.py"
spec = importlib.util.spec_from_file_location("build_claude_ai_skill", MODULE)
pack = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pack)


class ClaudeAISkillPackagingTest(unittest.TestCase):
    def test_source_is_valid_for_claude_ai(self):
        name, desc, docs = pack.validate_source()
        self.assertEqual(name, "noslop")
        self.assertLessEqual(len(desc), 200)
        self.assertGreaterEqual(len(docs), 10)

    def test_zip_has_exactly_one_skill_root(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "noslop-claude-ai.zip"
            result = pack.package(target)
            with ZipFile(target) as archive:
                names = archive.namelist()
                self.assertEqual(archive.testzip(), None)
                self.assertTrue(all(n.startswith("noslop/") for n in names))
                self.assertIn("noslop/SKILL.md", names)
                self.assertIn("noslop/references/content-integrity.md", names)
                self.assertIn("noslop/workflows/report.md", names)
                self.assertFalse(any(".claude-plugin" in n or n.startswith("scripts/") for n in names))
                self.assertEqual(len(names), result["files"])

    def test_description_too_long_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "noslop"
            root.mkdir()
            (root / "SKILL.md").write_text(
                "---\nname: noslop\ndescription: >-\n  " + "x" * 201 +
                "\n---\n\n# Test\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "description"):
                pack.validate_source(root)

    def test_broken_reference_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "noslop"
            (root / "references").mkdir(parents=True)
            for file in pack.MANDATORY:
                dest = root / file
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_text("# Placeholder\n", encoding="utf-8")
            (root / "SKILL.md").write_text(
                "---\nname: noslop\ndescription: A short useful skill.\n---\n"
                "[Missing](references/does-not-exist.md)\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Broken/unsafe link"):
                pack.validate_source(root)


if __name__ == "__main__":
    unittest.main()
