import importlib.util
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "score_evals.py"
spec = importlib.util.spec_from_file_location("score_evals", SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class EvaluationScorerTests(unittest.TestCase):
    def test_does_not_invent_missing_metrics(self):
        scores = module.score([{"variant": "candidate", "case_id": "F01"}])
        self.assertIsNone(scores["candidate"]["metrics"]["routing_ok"]["rate"])
        self.assertIsNone(scores["candidate"]["median_context_tokens"])

    def test_reports_critical_failure_without_hiding_it(self):
        scores = module.score([
            {"variant": "candidate", "case_id": "F01",
             "format_ok": False, "material_integrity_ok": True,
             "context_tokens": 900}
        ])
        self.assertEqual(scores["candidate"]["critical_failures"], ["F01"])
        self.assertEqual(scores["candidate"]["metrics"]["format_ok"]["rate"], 0.0)

    def test_median_tokens_only_from_observed_values(self):
        scores = module.score([
            {"variant": "baseline", "case_id": "F01", "context_tokens": 1200},
            {"variant": "baseline", "case_id": "F02", "context_tokens": 2000},
            {"variant": "candidate", "case_id": "F01", "context_tokens": 700},
        ])
        self.assertEqual(scores["baseline"]["median_context_tokens"], 1600)
        self.assertEqual(scores["candidate"]["median_context_tokens"], 700)
        self.assertEqual(scores["candidate"]["cases"], 1)


if __name__ == "__main__":
    unittest.main()
