# Phase 3 — owner decision register (ALL 10 DECISIONS APPROVED; IMPLEMENTED IN DRAFT BRANCH FOR VALIDATION)

These decisions are approved and incorporated into the modular runtime skill on the draft branch. Validation and release gates remain separate.

| ID | Existing rule or restriction | Owner discussion |
|---|---|---|
| R01 | Always plain HTML; priority over other formats | **APPROVED — replace:** Honor the user's explicitly requested output format. If none is specified, select the best-fit format or clarify if needed. |
| R02 | Each section must start with a visual | **APPROVED — relax:** Use visualization only when it adds comprehension value; do not require a visual in every section. |
| R03 | Hard limits: 4 sections, 5 items, 1 table | **APPROVED — keep strict:** Retain the current hard limits: at most 4 sections under the first screen, at most 5 items per card/list, and at most 1 table. No adaptive relaxation. Approved 2026-11-04. |
| R04 | First-screen 50–120 words | **APPROVED — keep strict:** The first-screen word-count range of 50–120 words remains mandatory, preserving the original source's stated exceptions (e.g. one-page reference sheet) and header-line exclusion. Approved 2026-11-04. |
| R05 | 2-line paragraph and 10-word table cell | **APPROVED — relax:** Treat the 2-line paragraph and 10-word table-cell limits as readability guidelines, not hard limits. Preserve clarity and scannability; allow longer text when needed for meaning. Approved 2026-11-04. |
| R06 | Claude's visual identity and five text sizes | **APPROVED — relax:** Use Claude's design language as the default; honor explicit user preferences or enterprise branding, including theme, palette, typography, and sizing as needed. Approved 2026-11-04. |
| R07 | Rebuild usually required, ~50% word reduction | **APPROVED — relax:** Choose targeted edits vs. rebuilding based on defect severity and reader needs; do not mandate ~50% text reduction or visibly different structure. Preserve all material information and factual integrity. Approved 2026-11-04. |
| R08 | Vercel passcode called 'private by default' | **APPROVED — replace:** Do not publish or deploy any artifact without the owner's explicit approval, and jointly select/approve the authentication and security mechanism before publishing. No default automatic deployment or assumption that a shared passcode is adequate. Approved 2026-11-04. |
| R09 | Three reader questions, ask nothing else | **APPROVED — relax:** Use the three reader questions as an intake baseline, not a strict maximum. Ask additional questions only when material information is missing; never re-ask information already supplied. Approved 2026-11-04. |
| R10 | Compress visually while preserving every material detail | **APPROVED — clarify priority:** First preserve factual accuracy and all material, decision-relevant information; next optimize clarity; then brevity and visual design. Peripheral/nonmaterial content may be omitted to improve brevity and presentation. If strict R03/R04 constraints conflict with preserving material information, ask the owner for a decision rather than silently omitting it. Approved 2026-11-04. |

All ten policy decisions R01–R10 were approved in the owner discussion on 2026-11-04. **These decisions are reflected in the draft skill files.** Keep the pull request in draft; do not merge or publish until separately authorized. R03 and R04 remain strict; material content conflicts trigger clarification.
