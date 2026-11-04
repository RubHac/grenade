# Grenade / No Slop

A reader-centered artifact skill built around progressive disclosure. This repository is a fork of the original [Grenade by Ruben Hassid](https://github.com/rubenhassid1/grenade). The skill remains named `noslop`.

## How it works

The active instructions live in [`plugins/noslop/skills/noslop/SKILL.md`](plugins/noslop/skills/noslop/SKILL.md), **not in this README**.

1. **Level 1 — Router:** user intent, requested output format and critical policy constraints.
2. **Level 2 — Workflows:** only the selected artifact type (decision brief, report, dashboard, guide, slides, interactive tool, cheat sheet, repair, web app).
3. **Level 3 — References:** content integrity, design, format selection, visual style, accessibility, quality checks and deployment security, read only as needed.

For example, a requested report in PDF follows the report workflow and PDF production route; it is **not forced into HTML**. The original design conventions remain a default, with explicit user branding taking precedence.

## Owner decisions and restrictions

Owner-approved decisions R01–R10 are recorded in [the decision register](docs/phase-3-decision-register.md). In particular:

- **Preserve all material facts.** Peripheral text may be shortened for readability.
- **Strict caps are retained:** up to four sections beneath the first screen, five items in a card/list and one table; the first screen retains 50–120 words (original exception for reference sheets).
- Visuals only where they improve comprehension; no obligatory chart in each section.
- Claude style by default, with explicit brand/user overrides.
- Choose targeted repair or rebuild by defect severity; no required 50% text reduction.
- Clarify only missing material details; never re-ask answered questions.
- **Do not publish or deploy without explicit user permission and jointly approved access controls.**

## Quality and evaluation

Use `python3 scripts/validate_skill.py` for the structural and policy checks. The evaluation scenarios and scoring rubric are under `evals/`; they are designed for comparative model runs and do **not** imply an automated end-to-end model evaluation.

HTML examples from the upstream project remain in [`examples/`](examples/). They are examples, not proof that the updated skill passes browser or usability tests.

## Development status

The owner **authorized merging PR #1 into `main` on 2026-11-04**. This authorization does **not** cover a hosted deployment, marketplace release or external distribution. End-to-end model A/B evaluations, browser QA and token-consumption measurements remain pending. Plugin installation and marketplace release metadata require a separately approved release stage.

## Attribution

Original [Grenade](https://github.com/rubenhassid1/grenade) by Ruben Hassid, based in part on [unslop](https://github.com/heydamir/unslop) by Damir Sokolovsky. See [LICENSE](LICENSE) for licensing.
