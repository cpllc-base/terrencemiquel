# terrencemiquel.com — static site

Two files, no build step. Deploy as-is.

## Files
- `index.html` — the homepage
- `observation-01.html` — first observation ("People don't buy products")

## Deploy (Cloudflare Pages, free)
1. Put these files in a Git repo (e.g. `github.com/cpllc-base/terrencemiquel`):
   ```
   git init
   git add .
   git commit -m "Initial site"
   git remote add origin <your-repo-url>
   git push -u origin main
   ```
2. Cloudflare dashboard → **Workers & Pages → Create → Pages → Connect to Git** → pick the repo.
3. Build settings: **Framework preset = None**, **Build command = (blank)**, **Output directory = /** (root). Deploy.
4. **Custom domain:** Pages project → Custom domains → add `terrencemiquel.com`. If your DNS is already on Cloudflare it wires automatically; otherwise add the CNAME it shows you. HTTPS is automatic.

Every `git push` redeploys. That push is your publish button.

*(Even simpler alternative: GitHub Pages — repo Settings → Pages → deploy from `main`. Cloudflare gives better performance and leaves room to add dynamic pieces later.)*

## Add a new observation
1. Duplicate `observation-01.html` → `observation-02.html`.
2. Edit the headline, the meta line, the three steps (handed → tested → kept), the principle, and the "next" link.
3. In `index.html`, find the matching **"Coming soon"** card and turn it into a link:
   - change `<div class="obs soon"> … <span class="read">Coming soon</span>`
   - to `<a href="observation-02.html" class="obs"> … <span class="read">Read the test →</span></a>`
4. **Add it to the feed** (this is what emails the list). In `feed.xml`, copy the existing `<item>…</item>` block, paste it as the NEW FIRST item, and update the title, link, guid, pubDate, description, and content.
5. `git add . && git commit -m "Add observation 2" && git push`. Live in ~1 minute.

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
