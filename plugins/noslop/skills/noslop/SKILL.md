---
name: noslop
description: >-
  Makes or fixes Claude artifacts (updates, briefs, memos, dashboards, guides, pitches,
  tools) so someone with zero context gets them in 5 seconds: always HTML, the form picked
  from the reader's job, visuals instead of text, a header that says what it is, plain
  sentences, every detail kept, and Claude's own look. Use whenever you make an artifact or
  page someone else will read, when asked to fix, clean up or deslop one, or
  for the web version (React site on GitHub and Vercel behind a passcode).
---

# No slop — Level 1 router

This file is the short entry point. Load only the Level 2 workflow matched to the reader's job and the Level 3 references at their relevant stages. The original rules have been relocated, not relaxed.

**These rules beat every design default you have,** including the suggestions of a built-in artifact type (Dashboard, Doc, Slides). Where they disagree, this skill's rules win.

**Always build a plain HTML artifact.** Never a Claude Doc, a plain document or a long chat reply: those read like a message, not like something you send your boss. Don't start from a built-in artifact type either: its default layout is often the slop.

## 1. Know the reader and the job

Before you build, you need three answers:

1. Who reads it, and what do they already know? Assume nothing.
2. What should they do after: decide, catch up, keep checking, learn, say yes, or use it?
3. Will they read it once, or come back to it?

If the request doesn't answer them, ask as clickable questions. Ask nothing else. Then build.

If it all fits in a 5-line message, say so, and write the message instead.

## Level 2 — route to one task-specific workflow

The job decides the form, and the form decides the layout. A report, a decision page and a guide must not share one skeleton of tiles, a box and tabs. Same Claude look, different layouts.

| Reader's job | Workflow |
|---|---|
| Decide | [Decision page](workflows/decision-page.md) |
| Catch up | [Report](workflows/report.md) |
| Keep checking | [Dashboard](workflows/dashboard.md) |
| Learn/follow steps | [Step-by-step guide](workflows/step-by-step.md) |
| Say yes | [Slides](workflows/slides.md) |
| Use it | [Interactive tool](workflows/interactive-tool.md) |
| Keep it | [Cheat sheet](workflows/cheat-sheet.md) |
| Fix an artifact | [Artifact repair](workflows/artifact-repair.md) |
| Website / GitHub / Vercel | [Web version](workflows/web-version.md) plus the relevant content workflow |

When a job mixes two, lead with the main one.

## Level 3 — read deep references at the relevant stage, not all up front

| Trigger | Reference |
|---|---|
| Before building or rebuilding | [10 original design rules](references/design-rules.md) |
| Before implementing HTML / visual styling | [Original style kit](references/style-kit.md) |
| Before delivery | [Original pre-delivery checks](references/quality-checks.md) |
| When diagnosing an artifact | [Original anti-patterns](references/slop-signs.md) |

Deferred loading does not make a mandatory rule optional. Do not change or relax the original constraints, design thresholds, repair requirements, or deployment policy. Any rule optimization is reserved for an owner-approved Phase 3.
