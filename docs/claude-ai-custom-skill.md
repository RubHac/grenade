# Claude.ai Custom Skills — installation and acceptance checks

**Target:** Personal Custom Skill in Claude.ai (not a Claude Code plugin or marketplace release).

Official sources:
- [Claude Help: Create Custom Skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)
- [Claude Help: Use Skills](https://support.claude.com/en/articles/12512180-use-skills-in-claude)
- [Claude skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)

## Build

From the repository root:

```bash
python3 scripts/build_claude_ai_skill.py --output dist/noslop-claude-ai.zip
python3 -m unittest discover -s tests -v
```

Resulting archive (do not double-zip):

```text
noslop-claude-ai.zip
└── noslop/
    ├── SKILL.md
    ├── workflows/
    │   └── [nine task-specific Markdown workflows]
    └── references/
        └── [eight selective Markdown references]
```

It deliberately excludes the GitHub plugin metadata, repository README, validation tools, examples, and any scripts, preventing incorrect nested roots and unneeded files.

The CI workflow builds this same ZIP and attaches it as the `noslop-claude-ai-review` job artifact. GitHub's Actions artifact download may wrap the ZIP in an outer archive: extract the outer archive first, then upload **only** `noslop-claude-ai.zip` to Claude.ai. This artifact is a review build, not a public release.

## Install in Claude.ai

1. Enable **Create and edit files / Code execution** (under Settings > Capabilities; organization policies may override).
2. Open **Customize > Skills > + > Create skill > Upload a skill**.
3. Upload the `noslop-claude-ai.zip` file. Enable/toggle the skill on.
4. Verify that Claude can select the skill for ordinary artifact requests. For a second check, explicitly ask Claude to use `noslop`.

Do not upload the GitHub repository ZIP, or `plugins/noslop/`, because Claude.ai expects a single folder matching the frontmatter `name` at the root of the archive.

**Documentation discrepancy:** The Claude Help article spells the filename `skill.md` in one section; Anthropic's official Skill structure documentation specifies uppercase `SKILL.md`. This package uses `SKILL.md` and requires an actual upload test to confirm behavior in your Claude.ai account.

## Manual smoke tests (after installation)

Use synthetic, non-sensitive content. Observe actual selected skill/references, requested format, and generated result.

| Test | Prompt | Pass criteria |
|---|---|---|
| Auto trigger | "Create a decision brief comparing two proposals with these sample costs..." | Claude activates noslop without being told to |
| Explicit trigger | "Use noslop to build a short Hebrew board report in PDF" | Uses noslop, real PDF, correct RTL |
| Slides | "Create an editable PPTX for a three-option executive decision" | Real PPTX (not HTML), no invented numbers |
| No forced visual | "Create a prose-only explanation; no chart adds value" | No gratuitous chart |
| Strict R03/R04 | "Show 7 material exceptions in one card and keep 12 words in the first screen" | Asks for resolution rather than silently violating limits |
| No publication | "Design a client dashboard, but don't deploy anything" | Produces reviewable content only; no deployment action |
| Retained details | "Shorten this document but preserve all substantive clauses" | No material conditions omitted |
| Selective references | "Repair one broken button; keep the rest of the page" | Loads repair workflow and only needed references; targeted change |

**Acceptance protocol:** record the model used, input, loaded skill files, output link, rubric scores, screen/format validation and observed failures. Repeat ambiguous cases. Compare to original `43809893c60746bdbe95c7fadb5db812b4022c51` when evaluating improvement. The 18 scenarios in `evals/scenarios.jsonl` are the complete evaluation suite.

## Boundaries

- **Not tested in an actual Claude.ai account from this repository.** Upload success and automatic invocation require a user session in Claude.ai.
- A successful static ZIP validator does not establish quality of generated HTML, DOCX, PPTX or PDF.
- Uploading a personal skill does not authorize it to deploy artifacts, publish to an organization or modify production systems. Owner-approved R08 remains binding.
- Packaging in CI is not a public marketplace release and does not change plugin versions.
