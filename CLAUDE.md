# CLAUDE.md — terrencemiquel.com

Project context for Claude Code. Read this before editing.

## What this is
The personal site of **Terrence Miquel** (note the spelling — the "L"). A hand-built
**static site**: plain HTML/CSS/vanilla JS, no framework, no build step. Deployed on
Cloudflare Pages from this repo. Every `git push` redeploys.

The site's job is a **validation destination**: people arrive from Terrence's social
content and the answer they should leave with is *"an introvert who tests what he's told —
business, relationships, faith — against reality, and keeps what survives."* The ideas are
the point, not the person. Keep it that way.

## Files
- `index.html` — the single-page homepage. Sections in order: hero → "What I'm Currently Testing" strip → Recent Observations → faith/creed band → What I'm building → pull quote → About + Journal → "See what survives" (email signup) → footer.
- `observation-N.html` — one detail page per observation. `observation-01.html` is the template/reference.
- `feed.xml` — RSS 2.0 feed. **This is the email trigger** (see Publishing).
- `img/terrence.jpg` — headshot. Currently used in the About section only (hero is text-first, no photo — intentional).
- `README.md` — deploy + workflow notes.

## Design system (all in the `:root` block of each HTML file)
Fonts: **Playfair Display** (display/headings), **Inter** (body), **Dancing Script** (script accents, logo, signature).

Dark palette (default) — cool/blue, matches Terrence's brand:
- `--bg #0A0A14` · `--bg-lift #12131F` · `--bg-card #101019` · `--line #232436`
- `--ink #F1F3F9` · `--ink-soft #AEB2C4` · `--ink-faint #7E8296`
- `--cream #9FB2F0` · `--cream-deep #7C93EC` — **note:** these vars are *named* "cream" for
  historical reasons but hold **light periwinkle blue** values. They're the quiet inline accent.
- `--brand #3957FF` — the primary brand blue. Used for the hero CTA and the signup band. This is the punch color.

Light theme exists via `[data-theme="light"]` and a toggle button. Keep both themes working when editing colors.

## Gotchas (we hit these — don't reintroduce them)
1. **Filled bands need explicit side padding.** `.capture` and `.creed` are full-width colored
   bands. Their inner container must use `padding: Y 28px`, NOT `padding: Y 0` — the shorthand
   zeroes out the horizontal gutter the `.wrap` class provides, and content jams against the edge.
2. `.step.kept` in `observation-*.html` used to break out of its container with
   `margin: 0 -100vw; padding: 0 100vw` to get a full-bleed background — but it's a direct child of
   `<article>` (no width constraint), so the breakout was never needed and was causing horizontal
   scroll on mobile (100vw renders wider than the visual viewport on some mobile browsers). Removed;
   `.step.kept { background: var(--bg-lift); }` alone is enough. `overflow-x: hidden` on `body`
   remains as a general safety net, not because anything specifically depends on it now.
3. **Cross-page links use `index.html`**, not `/`, so the site also works when opened as local files.
4. Nav currently has **5 items** (Observations / Current Tests / Building / Journal / About), with a
   mobile hamburger and a scroll-spy that highlights the active section. Don't add more nav items
   without reason. (Note: this bullet previously said "4 items ... Join the conversation" — that was
   stale; Journal and About were added and the signup section (now "See what survives")/Contact
   were moved out of the nav.)

## Publishing a new observation (the full loop)
1. Duplicate `observation-01.html` → `observation-N.html`. Update: `<title>`, the meta description,
   the OG/Twitter tags (`og:url`, `og:title`, `og:description`, `twitter:*`), the meta line
   (`Observation 0N`, category, date), the `.statement` headline, the byline read-time, the three
   spine steps (**What I was handed → The test → What survived**), the principle pull-quote, the soft
   product tie, and the foot-nav next/prev links.
2. In `index.html`, find the matching **"Coming soon"** card and convert it from
   `<div class="obs soon"> … Coming soon` to `<a href="observation-N.html" class="obs"> … Read the test →`
   (with the arrow SVG, matching card 1).
3. **In `feed.xml`, add a new `<item>` as the FIRST item** (copy the existing block; update title,
   link, guid, pubDate, description, and `content:encoded`). Skipping this means the post goes live
   but the email list never hears about it.
4. Commit + push.

## Voice (when drafting observations or copy)
- Structure every observation as **handed → tested → kept**, ending on the principle that held.
- Terrence's stance: tests faith against reality, *not religion*; a living, speaking God (relationship,
  not a closed book); the **text is the plumb line** he tests promptings against; nature-of-God /
  afterlife are carried by reason and trust, not predict-and-check.
- Tone: warm, direct, introvert-who-goes-deep. Minimal formatting. No hype.
- **Never fabricate a personal story.** Observation content must be true to what actually happened.
  If the real specifics aren't provided, draft the structure and flag the parts Terrence must fill in —
  don't invent anecdotes. The whole site's credibility rests on these being real tests.

## Email + deploy
- Email: `feed.xml` → **Kit** (Automate → RSS → add the feed). New posts become broadcasts.
- Deploy: push to this repo → Cloudflare Pages auto-builds (preset: None, no build command).
- Local preview: `python3 -m http.server 8000` then open `http://localhost:8000` (needed so
  root-relative paths like `/feed.xml` and the OG image URLs resolve correctly).
