<!-- Original SKILL.md section 7; unchanged. Source commit 43809893c60746bdbe95c7fadb5db812b4022c51. -->

## 7. Style kit

Start every page from this. Add only what the page needs.

- **Fonts:** serif for the title and section headings, like Claude's greeting. Sans for everything else.
- **Sizes:** only 5. 40px big numbers, 32px title, 22px section headings, 16px text, 13px labels.
- **Charts:** inline SVG or Chart.js. The bar or line that matters in clay, the rest in gray.
- **Icons:** simple line icons drawn in SVG, in gray or clay. Never emoji.
- **Nothing spills out of its box.** You can't see the page you build, so use layouts that can't break. No grid with more than 6 columns: a week of 10 days becomes a list or a timeline that wraps. Never a pill, a tag or `white-space: nowrap` inside a box narrower than 200px. A number in a tile fits on one line at every width ("$400", with "was $200" as its tag, never "$200 → $400"). Every box grows with its content. Picture it at 1440px and at 400px wide: if any text could overflow, overlap or wrap mid-number, change the layout.

```css
:root {
  --bg: #fff; --soft: #f9f9f9; --card: #fff;
  --text: rgba(0,0,0,.9); --text-2: rgba(0,0,0,.6); --text-3: rgba(0,0,0,.47);
  --line: rgba(0,0,0,.12); --shadow: 0 4px 20px rgba(0,0,0,.075);
  --clay: #d97757; --clay-strong: #c6613f;
  --good: #006c10; --good-bg: rgba(16,161,34,.14);
  --bad: #a42528; --bad-bg: rgba(220,60,61,.12);
  --watch: #794c02; --watch-bg: rgba(251,179,21,.16);
  --serif: Georgia, "Times New Roman", serif;
  --sans: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {
  --bg: #151515; --soft: #0b0b0b; --card: #1f1f1f;
  --text: rgba(255,255,255,.93); --text-2: rgba(255,255,255,.57); --text-3: rgba(255,255,255,.4);
  --line: rgba(255,255,255,.12); --shadow: none;
  --good: #53c556; --bad: #f17778; --watch: #e49c06; color-scheme: dark; } }
/* repeat the dark values under :root[data-theme="dark"] */
body { margin: 0; background: var(--bg); color: var(--text); font: 16px/1.55 var(--sans); }
h1, h2 { font-family: var(--serif); font-weight: 400; margin: 0; text-wrap: balance; }
h1 { font-size: 32px; line-height: 1.2; } h2 { font-size: 22px; line-height: 1.3; }
.meta { font-size: 13px; color: var(--text-2); border-bottom: 1px solid var(--line); padding: 12px 0; }
.card { background: var(--card); border: 1px solid var(--line); border-radius: 14px; box-shadow: var(--shadow); padding: 20px; }
.num { font-size: 40px; font-weight: 500; line-height: 1; }
.pill { display: inline-block; border-radius: 999px; padding: 2px 10px; font-size: 13px; font-weight: 500; }
.good { color: var(--good); background: var(--good-bg); } .bad { color: var(--bad); background: var(--bad-bg); } .watch { color: var(--watch); background: var(--watch-bg); }
button { font: 500 16px var(--sans); border-radius: 10px; padding: 10px 16px; cursor: pointer; background: var(--card); color: var(--text); border: 1px solid var(--line); }
button.main { background: var(--clay-strong); color: #fff; border: 0; }
input, select, textarea { font: 16px var(--sans); background: var(--card); color: var(--text); border: 1px solid var(--line); border-radius: 10px; padding: 10px 12px; }
```
