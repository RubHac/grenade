# Web implementation — Level 2 workflow (R01, R06, R08)

Use this workflow **only when the user requests an actual website/web app** (not merely because a report or slide deck has visual content). Read the relevant content workflow as well.

## Build
- Preserve the selected reader goal and its required detail. Use HTML/CSS/JS or a suitable framework according to the user's explicit technology preference and available tools.
- For a new app where no stack is imposed, the original preferred stack remains: Vite, React, TypeScript, Tailwind CSS, shadcn/ui, Recharts, Motion and lucide-react. Do not add unnecessary dependencies.
- Use Claude's design language by default, or the exact requested user/enterprise visual identity (R06). Consult [Style kit](../references/style-kit.md) and [Accessibility/RTL](../references/accessibility.md).
- Keep animations purposeful and respect reduced motion. Charts show units and exact values on hover or tap. Interactive cards, forms and buttons must perform meaningful actions.
- Where tooling permits, run locally and inspect at 1440px and 400px; correct overflow, empty hero bands, broken controls and keyboard issues.
- For substantive facts, use [Content integrity](../references/content-integrity.md). Before handoff, run [Quality checks](../references/quality-checks.md).

## Hard publication gate
**Never create a public deployment or share a live URL without the user's explicit approval and joint selection of the authentication/security mechanism.** GitHub and Vercel are possible destinations, **not mandatory defaults**. A private repo plus a passcode is not automatically adequate security. Read [Deployment and security](../references/deployment-security.md) only when deployment has been requested for discussion; act only after approval. Otherwise deliver working source or a private draft for review.

Retain R03's structural limits and R04's first-screen word range. If these conflict with keeping essential data, request direction; never suppress essential information to fit them.
