# Quality checks — Level 3 delivery gate

Before delivery, read as the intended recipient with no additional context. Apply the original clarity checks together with owner decisions R01–R10.

## Content integrity — must pass
- Are every material number, claim, unit, definition, source attribution, date, condition and exception correct and preserved? Distinguish supplied facts, derived values and assumptions.
- Are the reader's point, reasons, material risks, requested action and responsible party evident?
- Did we remove only peripheral or redundant information, rather than inventing or omitting essential information?
- Are totals, denominators, period-over-period baselines and linked claims internally consistent?
- Did the user receive the requested **output format**, not an unsolicited HTML substitute?

## Readability and appearance
- Is the first screen self-contained and between **50–120 words**, excluding the header line, with the original reference-sheet exception?
- Are the **strict R03 limits** met: maximum 4 sections beneath the first screen, 5 entries per card/list and 1 table on a page/screen? If incompatible with material content, stop and ask for a resolution.
- Are headings direct and natural? Is one focal point obvious? Are explanatory paragraphs short enough to scan without losing meaning?
- Are charts or illustrations present **only when beneficial**? Does each visual contain valid labels and units? There is no mandatory visual per section.
- Are repeated content, decorative graphs, empty badges, repeated asks and pointless helper text removed?
- Does the result follow Claude's default appearance **unless** user or enterprise branding overrides it?
- In HTML/web output, inspect or test around 1440px and 400px widths when browser tooling is available; check responsiveness, overflow, keyboard operation, contrast and RTL direction as applicable.
- For PDFs, documents, presentations, etc., use format-specific preview and accessibility checks rather than HTML-only checks.

## Operational and security gate
- Are interactive controls actually functional, with valid sample data clearly labeled as sample?
- Was no publication, live deployment, content exposure or permission change performed without explicit user approval and agreed access controls?
- Report checks actually performed and unresolved limitations honestly. Do not claim automated validation or user testing unless run.

If any critical check fails, fix the artifact; if an unresolvable conflict affects essential information and R03/R04, ask for direction before delivery.
