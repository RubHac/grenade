#!/usr/bin/env python3
"""Offline skill-package policy and reference validation. No network or publication."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "plugins" / "noslop" / "skills" / "noslop"
ROUTER = SKILL_DIR / "SKILL.md"
DECISIONS = ROOT / "docs" / "phase-3-decision-register.md"
SCENARIOS = ROOT / "evals" / "scenarios.jsonl"
failures = []
checks = 0


def check(name, ok, detail=""):
    global checks
    checks += 1
    if ok:
        print("PASS", name)
    else:
        failures.append(name + (": " + detail if detail else ""))
        print("FAIL", name, detail)


def get_text(path):
    if not path.is_file():
        return ""
    return path.read_text(encoding="utf-8")


def main():
    router = get_text(ROUTER)
    decision_text = get_text(DECISIONS)
    check("Router exists with skill metadata", router.startswith("---\nname: noslop\n") and "description:" in router)
    check("Small Level 1 router (< 8500 characters)", 0 < len(router) < 8500)
    check("No mandatory HTML override", "Never force HTML" in router and "Always build a plain HTML" not in router)
    check("Strict R03 caps retained", all(t in router for t in ("4 sections", "5 items per card/list", "1 table")))
    check("Strict R04 first-screen word range retained", "50–120 words" in router)
    check("User-controlled format in router", "requested format" in router)
    check("Material accuracy prioritized", "Preserve accurate, material" in router)
    check("Owner approval required before publication", "explicit user approval" in router and "Never publish" in router)
    check("Default Claude branding may be overridden", "Claude's style is the default" in router)
    check("R02 visuals optional", "only where they improve understanding" in router)
    check("R05 paragraph/cell heuristics", "readability heuristics" in router)
    check("R07 no mandatory text cut", "no mandatory 50% word cut" in router)

    expected_workflows = [
        "decision-page", "report", "dashboard", "step-by-step", "slides",
        "interactive-tool", "cheat-sheet", "artifact-repair", "web-version",
    ]
    for name in expected_workflows:
        p = SKILL_DIR / "workflows" / (name + ".md")
        check("Workflow " + name, p.is_file() and len(get_text(p)) > 100)

    references = [
        "design-rules", "style-kit", "quality-checks", "slop-signs",
        "content-integrity", "format-selection", "accessibility", "deployment-security",
    ]
    for name in references:
        p = SKILL_DIR / "references" / (name + ".md")
        check("Reference " + name, p.is_file() and len(get_text(p)) > 100)

    markdown = [ROOT / "README.md", DECISIONS, ROOT / "docs" / "baseline-2026-11-04.md"]
    markdown.extend(SKILL_DIR.rglob("*.md"))
    md_link = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for md in markdown:
        contents = get_text(md)
        if not contents:
            failures.append("Missing markdown: " + str(md))
            continue
        for target in md_link.findall(contents):
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
                continue
            base = target.split("#", 1)[0]
            if not base:
                continue
            dest = (md.parent / base).resolve()
            check("Local link " + md.relative_to(ROOT).as_posix() + " -> " + base,
                  dest.exists() and dest.is_relative_to(ROOT.resolve()))

    for index in range(1, 11):
        token = "R%02d" % index
        rows = [line for line in decision_text.splitlines() if line.startswith("| " + token + " |")]
        check("Owner decision " + token + " approved", len(rows) == 1 and "APPROVED" in rows[0])
    check("Decisions retain no-merge/no-publish gate", "do not merge or publish" in decision_text.lower())

    scenarios = []
    if SCENARIOS.exists():
        for line_no, line in enumerate(get_text(SCENARIOS).splitlines(), 1):
            if not line.strip():
                continue
            try:
                item = json.loads(line)
            except json.JSONDecodeError as e:
                failures.append("Invalid JSONL line %d: %s" % (line_no, e))
                continue
            for key in ("id", "prompt", "expected_workflows", "expected_format", "critical_assertions"):
                if key not in item:
                    failures.append("Scenario %d missing %s" % (line_no, key))
            for workflow in item.get("expected_workflows", []):
                check("Scenario workflow exists: " + str(item.get("id")) + " / " + workflow,
                      (SKILL_DIR / "workflows" / (workflow + ".md")).exists())
            scenarios.append(item)
    check("At least 14 evaluation scenarios", len(scenarios) >= 14)
    check("Unique scenario IDs", len({s.get("id") for s in scenarios}) == len(scenarios))
    check("No scenario requests actual deployment", all(not s.get("execute_deployment", False) for s in scenarios))

    print("\nSummary: %d checks, %d failures" % (checks, len(failures)))
    if failures:
        print("\n".join(" - " + item for item in failures))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
