#!/usr/bin/env python3
"""Static site build: stitches shared partials (nav, footer) into page templates.

Source of truth:
    src/pages/*.html      page templates, with include markers
    src/partials/*.html   shared fragments (nav, footer)

Output:
    public/*.html         generated — do not hand-edit, re-run this script instead

Include marker syntax (HTML comment, one per line):
    <!-- include: nav logo_href="index.html" home="index.html" -->
    <!-- include: footer -->

Any key="value" pairs after the partial name are substituted into that
partial wherever it contains the matching {{key}} token.

Run this after editing anything under src/, before committing:
    python3 build.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).parent
PAGES_DIR = ROOT / "src" / "pages"
PARTIALS_DIR = ROOT / "src" / "partials"
OUTPUT_DIR = ROOT / "public"

INCLUDE_RE = re.compile(
    r'<!--\s*include:\s*([a-zA-Z0-9_-]+)((?:\s+[a-zA-Z0-9_]+="[^"]*")*)\s*-->'
)
PARAM_RE = re.compile(r'([a-zA-Z0-9_]+)="([^"]*)"')


def load_partials():
    partials = {}
    for f in PARTIALS_DIR.glob("*.html"):
        partials[f.stem] = f.read_text(encoding="utf-8")
    return partials


def build():
    partials = load_partials()
    if not partials:
        raise SystemExit(f"No partials found in {PARTIALS_DIR}")

    pages = sorted(PAGES_DIR.glob("*.html"))
    if not pages:
        raise SystemExit(f"No page templates found in {PAGES_DIR}")

    OUTPUT_DIR.mkdir(exist_ok=True)

    for page in pages:
        content = page.read_text(encoding="utf-8")

        def replace(match):
            name = match.group(1)
            params_str = match.group(2)
            if name not in partials:
                raise ValueError(f"{page.name}: unknown include '{name}'")
            rendered = partials[name]
            for key, value in PARAM_RE.findall(params_str):
                rendered = rendered.replace("{{" + key + "}}", value)
            leftover = re.search(r"{{[a-zA-Z0-9_]+}}", rendered)
            if leftover:
                raise ValueError(
                    f"{page.name}: include '{name}' missing a value for {leftover.group(0)}"
                )
            return rendered.rstrip("\n")

        new_content = INCLUDE_RE.sub(replace, content)
        (OUTPUT_DIR / page.name).write_text(new_content, encoding="utf-8")

    print(f"Built {len(pages)} pages -> {OUTPUT_DIR}/")


if __name__ == "__main__":
    build()
