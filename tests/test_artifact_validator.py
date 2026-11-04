import importlib.util
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "validate_artifact.py"
spec = importlib.util.spec_from_file_location("validate_artifact", SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

VALID = ('<!doctype html><html lang="en"><head><title>Example</title>'
         '<meta name="viewport" content="width=device-width, initial-scale=1">'
         '</head><body><main><h1>Example</h1><p>Readable information.</p>'
         '</main></body></html>')


class BasicArtifactChecks(unittest.TestCase):
    def test_complete_example_passes(self):
        self.assertEqual(module.validate_html(VALID), [])

    def test_missing_title_viewport_and_lang_fail(self):
        html = '<html><body><main><h1>A</h1></main></body></html>'
        reasons = module.validate_html(html)
        self.assertIn("Missing html lang attribute", reasons)
        self.assertIn("Missing nonempty title", reasons)
        self.assertIn("Missing viewport meta tag", reasons)

    def test_duplicate_ids_flagged(self):
        self.assertIn("Duplicate DOM IDs", module.validate_html(
            VALID.replace("</main>", '<div id="a"></div><p id="a">X</p></main>')))

    def test_missing_main_flagged(self):
        self.assertIn("Missing main landmark",
                      module.validate_html(VALID.replace("<main>", "<div>").replace("</main>", "</div>")))


if __name__ == "__main__":
    unittest.main()
