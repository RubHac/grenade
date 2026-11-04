---
name: noslop
description: >-
  Create or improve reader-centered decision pages, reports, dashboards,
  guides, presentations, tools and reference sheets. Choose the output format
  requested by the user; route through the relevant workflow and load only
  the deeper guidance needed. Use for artifact creation, repair, and web
  implementation when requested.
---

# No slop — Level 1 router

You are creating or improving an artifact for a real reader. **Load this router first. Read only the matching Level 2 workflow and the Level 3 references needed for the current step.** Never load the entire library by default.

## Intake and non-negotiable decisions

Establish: (1) who reads it and what they already know; (2) what they must do—decide, catch up, monitor, learn, approve, use or reference; (3) one-time or recurring use. **Use facts already provided; only ask clarification questions if material information is missing.** If a five-line chat response does the job and no artifact is requested, use it.

- **Output format (R01):** Honor the user's explicitly requested format (HTML, PDF, presentation, document, etc.). If unspecified, choose the form and delivery medium that fit the job. Ask only when the format changes the task materially. Never force HTML. If the requested format cannot be produced with available tools, say so rather than silently substituting one.
- **Information priority (R10):** Preserve accurate, material and decision-relevant facts first; achieve clarity second; optimize brevity and visuals third. Peripheral information may be removed. Do not invent facts, baselines or functional controls.
- **Strict layout limits (R03):** On each relevant page/screen, at most **4 sections beneath the first screen**, **5 items per card/list**, and **1 table**. Do not silently violate these limits or discard essential information: if they conflict, request an explicit resolution.
- **Strict first-screen rule (R04):** **50–120 words**, excluding the header line, with the original reference/cheat-sheet exception. Make context, point, reasons and next action apparent without scrolling.
- **No publishing (R08):** Never publish, deploy, push a live artifact, or expose its data without **explicit user approval** and jointly agreed security/access controls. Creating a file or working branch is not permission to publish.

## Level 2 — pick the reader's job first

| Task | Read this Markdown file |
|---|---|
| Decide / brief / memo | [Decision page](workflows/decision-page.md) |
| Catch up / recurring update | [Report](workflows/report.md) |
| Keep checking / tracking | [Dashboard](workflows/dashboard.md) |
| Learn / follow steps | [Step-by-step guide](workflows/step-by-step.md) |
| Say yes / pitch | [Slides](workflows/slides.md) |
| Use it / calculate / plan | [Interactive tool](workflows/interactive-tool.md) |
| Keep for reference | [Cheat sheet](workflows/cheat-sheet.md) |
| Diagnose / repair artifact | [Artifact repair](workflows/artifact-repair.md), then the relevant content workflow if needed |
| Build an actual web app | [Web implementation](workflows/web-version.md), plus the relevant content workflow |

When a task spans two forms, lead with the reader's primary job. A requested medium does not force a different reader job: for example, a decision brief can be a document or HTML.

## Level 3 — selective, step-specific reference loading

| Need / stage | Read |
|---|---|
| Choose format when unclear or adapting layouts | [Format selection](references/format-selection.md) |
| Before drafting substantive content | [Content integrity](references/content-integrity.md) |
| Before visual/page layout | [Design rules](references/design-rules.md) |
| When designing HTML/web visuals | [Style kit](references/style-kit.md) |
| When using interactive, multilingual or RTL layouts | [Accessibility and RTL](references/accessibility.md) |
| When diagnosing an existing artifact | [Slop signs](references/slop-signs.md) |
| Before delivering any finished artifact | [Quality checks](references/quality-checks.md) |
| Only when deployment is requested and approved | [Deployment and security](references/deployment-security.md) |

**R02:** Use charts, diagrams and imagery only where they improve understanding; never force a visual per section. **R05:** Two-line paragraphs and ten-word table cells are readability heuristics, not hard gates. **R06:** Claude's style is the default, overridden by explicit user or enterprise branding. **R07:** Repair or rebuild according to severity; no mandatory 50% word cut. These rules are expanded only in relevant Level 3 guidance.

Execution: intake → select task and format → read relevant rules → build → verify against original material → run final checks → deliver without unauthorized publishing.
