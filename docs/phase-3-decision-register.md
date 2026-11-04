# Phase 3 — owner decision register (PARTIALLY APPROVED)

This register prepares, but does not implement, policy decisions.

| ID | Existing rule or restriction | Owner discussion |
|---|---|---|
| R01 | Always plain HTML; priority over other formats | **APPROVED — replace:** Honor the user's explicitly requested output format. If none is specified, select the best-fit format or clarify if needed. |
| R02 | Each section must start with a visual | **APPROVED — relax:** Use visualization only when it adds comprehension value; do not require a visual in every section. |
| R03 | Hard limits: 4 sections, 5 items, 1 table | **APPROVED — keep strict:** Retain the current hard limits: at most 4 sections under the first screen, at most 5 items per card/list, and at most 1 table. No adaptive relaxation. Approved 2026-11-04. |
| R04 | First-screen 50–120 words | **APPROVED — keep strict:** The first-screen word-count range of 50–120 words remains mandatory, preserving the original source's stated exceptions (e.g. one-page reference sheet) and header-line exclusion. Approved 2026-11-04. |
| R05 | 2-line paragraph and 10-word table cell | **APPROVED — relax:** Treat the 2-line paragraph and 10-word table-cell limits as readability guidelines, not hard limits. Preserve clarity and scannability; allow longer text when needed for meaning. Approved 2026-11-04. |
| R06 | Claude's visual identity and five text sizes | **APPROVED — relax:** Use Claude's design language as the default; honor explicit user preferences or enterprise branding, including theme, palette, typography, and sizing as needed. Approved 2026-11-04. |
| R07 | Rebuild usually required, ~50% word reduction | Preserve working structure when suitable? |
| R08 | Vercel passcode called 'private by default' | Define enterprise security baseline? |
| R09 | Three reader questions, ask nothing else | Allow essential contextual clarification? |
| R10 | Compress visually while preserving every material detail | Agree precedence and evaluation rules? |

Decisions must be recorded as **keep, relax, or replace**, with rationale and approved wording before any corresponding edits. R01, R02, R03, R04, and R05 approved on 2026-11-04; implementation is deferred while other decisions are discussed. All undecided rules remain intact.
