# Website and deployment — Level 2 workflow

## 8. The web version

Use this when they ask for a website, the web version, or to put the page on GitHub or Vercel. Everything above still applies. This version adds free, open-source libraries that make the page feel like an app, and a link only the reader can open.

**The stack.** Vite, React, TypeScript, Tailwind CSS and shadcn/ui (cards, tabs, buttons, badges, tooltips, dialogs). Charts with Recharts, through shadcn's chart component. Motion for movement. Icons from lucide-react. Nothing paid, no API keys.

**Same look.** Put the style kit into the shadcn theme: clay as the primary color, the serif for titles, the same 5 text sizes, the same dark mode. It must still look like Claude.

**What the libraries are for.** Only what helps the reader:

- Charts show the exact value on hover or tap.
- Big numbers count up once, when the page opens.
- Sections fade in once, in 200 to 400 ms. Nothing loops, nothing bounces. Respect "reduce motion".
- Rows and cards open smoothly to show reference detail.
- Tabs, steps and slides switch with a short slide.
- A light and dark switch in the corner.

**You can see the page now.** Run it, open it in a browser at 1440px and 400px wide, and look at the screenshots. Fix anything that spills, overlaps or looks empty, then look again. Read the first screen as the reader before you ship.

**Private by default.** Business pages are not for the whole internet:

1. Check `gh auth status` and `vercel whoami`. If either is signed out, start the sign-in (`gh auth login --web`, `vercel login`) and tell the person which button to click in the browser.
2. Push the code to a new private GitHub repo.
3. Deploy it to Vercel. Add a passcode gate: a `middleware.js` at the root (Vercel Routing Middleware) that shows a passcode screen in the same Claude look until the passcode is right, then sets a cookie. Keep the passcode in a Vercel environment variable, never in the code. Send `X-Robots-Tag: noindex` so search engines skip it.
4. Check it from outside: locked without the passcode, open with it.

End with 3 lines: the link, the passcode, the repo. Nothing else.

The source security and hosting rules above are retained unchanged. Review their adequacy with the owner in Phase 3. Also load applicable design rules, style kit, and final checks at their relevant stages.
