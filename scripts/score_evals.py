#!/usr/bin/env python3
"""Summarize actual scored model runs. Never fabricate outcomes or token savings."""
import argparse
import json
import statistics
from collections import defaultdict
from pathlib import Path

METRICS = (
    "routing_ok", "format_ok", "material_integrity_ok", "r03_ok", "r04_ok",
    "visual_value_ok", "branding_ok", "clarifications_ok", "security_ok",
)
CRITICAL = ("format_ok", "material_integrity_ok", "r03_ok", "r04_ok", "security_ok")


def score(rows):
    groups = defaultdict(list)
    for row in rows:
        groups[row["variant"]].append(row)
    result = {}
    for variant, cases in groups.items():
        scores = {}
        for metric in METRICS:
            scored = [r[metric] for r in cases if isinstance(r.get(metric), bool)]
            scores[metric] = {"passed": sum(scored), "evaluated": len(scored),
                              "rate": (round(sum(scored) / len(scored), 4) if scored else None)}
        tokens = [r["context_tokens"] for r in cases if isinstance(r.get("context_tokens"), int) and r["context_tokens"] >= 0]
        critical_failed = [r["case_id"] for r in cases if any(r.get(m) is False for m in CRITICAL)]
        result[variant] = {"cases": len(cases), "metrics": scores,
                           "median_context_tokens": statistics.median(tokens) if tokens else None,
                           "critical_failures": critical_failed}
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("runs", type=Path, help="Actual observed run results in JSONL; required")
    opts = parser.parse_args()
    rows = [json.loads(line) for line in opts.runs.read_text(encoding="utf-8").splitlines() if line.strip()]
    for index, row in enumerate(rows, 1):
        if not all(isinstance(row.get(k), str) and row[k] for k in ("variant", "case_id")):
            parser.error("Line %d is missing variant/case_id" % index)
    print(json.dumps(score(rows), indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
