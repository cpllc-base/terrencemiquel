# terrencemiquel.com — static site

Static HTML/CSS/JS with a tiny local build step: shared nav/footer live once in `src/partials/`
and get stitched into every page by `build.py`. The output in `public/` is what actually deploys —
plain static files, nothing runs on the server.

## Files
- `src/pages/*.html` — edit these. One file per page.
- `src/partials/nav.html`, `src/partials/footer.html` — the shared header/footer, included on
  every page.
- `build.py` — run this after editing anything in `src/`, before committing.
- `public/*.html` — **generated.** Don't hand-edit; the next build overwrites it.
- `public/feed.xml`, `public/img/` — not templated, edited directly in `public/`.

## Editing a page
1. Edit the file under `src/pages/`.
2. `python3 build.py` — regenerates everything in `public/`.
3. `git add . && git commit -m "..." && git push`.

## Deploy (Cloudflare Pages, free)
1. Put this repo on GitHub (e.g. `github.com/cpllc-base/terrencemiquel`).
2. Cloudflare dashboard → **Workers & Pages → Create → Pages → Connect to Git** → pick the repo.
3. Build settings: **Framework preset = None**, **Build command = (blank)**, **Output directory = `public`**. Deploy.
   (The build already happened locally before you pushed — Cloudflare just serves the `public/`
   folder as-is.)
4. **Custom domain:** Pages project → Custom domains → add `terrencemiquel.com`. If your DNS is already on Cloudflare it wires automatically; otherwise add the CNAME it shows you. HTTPS is automatic.

Every `git push` redeploys. That push is your publish button.

*(Even simpler alternative: GitHub Pages — repo Settings → Pages → deploy from `main`. Cloudflare gives better performance and leaves room to add dynamic pieces later.)*

## Add a new observation
1. Duplicate `src/pages/observation-01.html` → `src/pages/observation-N.html`.
2. Edit the headline, the meta line, the three steps (handed → tested → kept), the principle, and the foot-nav prev/next links.
3. In `src/pages/index.html`, add a new card to the observations grid linking to `observation-N.html`.
4. **Add it to the feed** (this is what emails the list). In `public/feed.xml` (not templated — edit directly), copy the existing `<item>…</item>` block, paste it as the NEW FIRST item, and update the title, link, guid, pubDate, description, and content.
5. `python3 build.py`, then `git add . && git commit -m "Add observation N" && git push`. Live in ~1 minute.

## Email the list automatically (RSS → Kit)
The site emits an RSS feed at `https://terrencemiquel.com/feed.xml`. That's the trigger.
1. In Kit: **Automate → RSS → + Add feed**, paste the feed URL.
2. Choose **single email per post** (or a **weekly digest** of recent posts).
3. Turn **"Send automatically"** ON for hands-off (goes out ~30 min after Kit picks up the post), or leave it OFF to review each draft before sending.
4. Set the from-address and pick recipients (all subscribers, or a tag).

Notes:
- Kit's native RSS auto-send may require the **Creator plan** (paid, but starts low). List hosting itself is free to 10,000 subscribers.
- Staying strictly free? Two options that use the same feed: send each observation as a manual **Broadcast**, or bridge **RSS → Kit with Zapier/Make**.
- A Kit signup form is embedded in the "See what survives" block so the list actually fills — that's the rented→owned conversion point.

## Photos
Your headshot is already wired into both slots (hero + About) at `img/terrence.jpg`. To swap it later, replace that file with a same-name JPG (square works best) — no code changes needed.

## Later (optional, not needed to launch)
If duplicating an HTML file per post ever gets old, graduate to **Astro** or **Eleventy**: same static output, but observations become Markdown files and the layout is one shared template. Only worth it once your publishing cadence justifies it.
