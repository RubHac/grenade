# Validation and evaluation status — 2026-11-04

## Scope
Working branch: `refactor/progressive-disclosure-l1-l2-20261104`. Pull request: [#1](https://github.com/RubHac/grenade/pull/1) (Draft). Main branch not updated, no artifact deployment performed.

## Observed automated validation

GitHub Actions run: [41790337743](https://github.com/RubHac/grenade/actions/runs/41790337743) — **successful**, commit `cc83fa6f51799df501ab4cc5adb0c0cec8c73b3e`.

| Check | Observed result |
|---|---|
| Python compilation of tools and tests | Passed |
| Skill structural and policy validator | **124 checks, 0 failures** |
| Artifact HTML static validator unit tests | **4 passed** |
| Evaluation scorer unit tests | **3 passed** |
| Total unit tests | **7 passed** |
| Evaluation case inventory | **18 scenarios**, with known workflow targets |
| Owner decision coverage | R01–R10 marked approved and reflected in draft skill files |
| Actual instruction token savings | **Not measured** |
| Model-executed A/B evaluation | **Not run** |
| Actual browser preview at 1440/400 | **Not run** |
| PDF/DOCX/PPTX generation tests | **Not run** |
| Human reader usability testing | **Not run** |
| Deployed access control testing | **Not run (deployment not authorized)** |

The static validator checks key policy statements, document existence, local Markdown links, evaluation metadata and relevant workflows. It cannot determine whether a generative model consistently follows those instructions in real tasks.

## Known residual risks
1. The modular Level 1 router loads fewer initial characters than the original, but depends on models loading the needed deeper references when required; routing and total-token overhead must be measured.
2. Strict R03 and R04 requirements may collide with preserving material information or non-HTML layouts; instructions require clarification rather than silent omission.
3. Formatting and brand overrides for PPTX, DOCX, PDF, spreadsheets and RTL need real artifact output tests.
4. The HTML lint script performs **static checks only**; it cannot confirm JS behavior, first-screen word counts, browser rendering, accessibility conformance or business fact fidelity.
5. No deployment policy has been exercised; R08 forbids publication before explicit owner approval and jointly agreed security.
6. Plugin release metadata/version has intentionally **not** been changed pending release approval.

## Evaluation method and acceptance gates

Use [scenarios.jsonl](../evals/scenarios.jsonl) and [evaluation-rubric.md](../evals/evaluation-rubric.md) for actual original-vs-modular skill runs. Only record observed results; report pass/fail plus unmeasured dimensions. `scripts/score_evals.py` will calculate summaries from recorded real run results. Do not turn hypothetical target improvements into measured claims.

## Decision boundary

**No merge or publication authorized.** Revisit after real model, output-format and browser evaluations; obtain separate owner approval for merging and for any live deployment.
