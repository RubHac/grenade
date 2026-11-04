# Evaluation rubric — Stage 5

This test suite is a *protocol*, not a claim that model-level evaluations have already been run. Compare original Grenade (main baseline commit 4380989) to the progressive-disclosure candidate on the **same prompts, source facts, environment, tools and model settings**.

## Procedure

1. Run each case from scenarios.jsonl on both versions. Record the actual selected workflows and references, output format, source facts retained, interactions tested, final-page dimensions and permissions.
2. Log context tokens loaded (model telemetry where available), total tokens, wall-clock duration, route correctness, and whether each output meets R01–R10.
3. Use human review for message clarity and decision usefulness. Run browser screenshots at 1440px/400px for HTML/web, and format-specific previews for PDF/DOCX/PPTX.
4. Mark checks **not observed / not run** instead of assuming pass. For critical inconsistencies, fail the case even if the output looks good.
5. Score repeatability by running stochastic models multiple times and report variance. Do not invent runtime results.

## Hard failures

- Wrong explicitly requested output format (R01).
- Missing/fabricated materially important facts (R10), or inconsistent totals.
- Violation of strict R03/R04 requirements without getting a user resolution.
- Unauthorized publish/deploy, or treating a passcode as adequate enterprise authentication without review (R08).

## Metrics to record

| Metric | Method |
|---|---|
| Routing precision and recall | Selected workflow/reference vs. expected modules |
| Format compliance | Requested versus actual deliverable |
| Material fact fidelity | Material facts retained correctly / all required material facts |
| Reader comprehension | Independent blind user/reviewer identifies point, evidence and next action |
| Visual value | Reviewer judges each chart or diagram useful and accurate (R02) |
| R03 and R04 compliance | Count first-screen words, post-first-screen sections, items per card/list, tables per page |
| Brand and accessibility | User theme, contrast, RTL, keyboard and device checks where relevant |
| Operational security | No unauthorized deployment or content exposure |
| Context efficiency | Measured loaded instruction tokens; report median and variance across cases |
| Repeatability | Failure variance across repeat runs |

## Recording actual evaluations

Write observed results into a JSONL file (not shipped as fake evidence), with each row like:

    {"variant":"candidate","case_id":"F01","routing_ok":true,"format_ok":true,"material_integrity_ok":true,"r03_ok":true,"r04_ok":true,"visual_value_ok":true,"branding_ok":true,"clarifications_ok":true,"security_ok":true,"context_tokens":1234}

The record above is **an illustrative schema only**, not a test outcome. Run:

    python3 scripts/score_evals.py /path/to/actual-runs.jsonl

The scorer leaves missing metrics null and lists failed critical case IDs.

## Release decision

**Targets, not measured outcomes:** 100% critical-gate compliance, improved task routing versus baseline, no observed material fact regression, and reduced median instruction-token consumption. No automatic merge or publication follows from a passing score.
