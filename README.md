# College Conversations: Resource Library

A one-page website for Dr. Janice Fedor: every resource a high school graduate or college
student needs, a senior-year-to-first-job checklist, two calculators, a glossary and her videos.

Design: the "Warm Community" type from the Swipe Shelf (references in `Inspo Web/`:
WorkNook's rounded hero card with a glass search bar, Horizon Courts' navy card + photo +
stat card row, grey second halves in headlines), set in the channel's own navy `#0B1F3A`,
gold `#F5B335`, banner cream `#F6F1E7`, Fraunces and Inter.

## Folders

| Path | What it is |
|---|---|
| `build/content.py` | **All copy and data**: resources, roadmap, glossary, videos, FAQ. Edit here. |
| `build/build.py` | Generates `site/index.html` from content.py; downloads video thumbnails once. |
| `docs/` | The finished static site. GitHub Pages serves it from `main` /docs at collegeconversations.org. |
| `docs/css/tokens.css` | Every colour, size, space and motion value. The only file with raw values. |
| `design/` | Logo drafts (A was chosen, refined in `logo-v2`), OG image and icon sources, her YouTube avatar. |
| `qa/` | Audit script, capture script and review screenshots. |

## Editing

```bash
python3 build/build.py
```

Then open `docs/index.html` through a local server (the preview config is in
`.claude/launch.json`, port 4200). CSS and JS links get a content hash on every build, so
browsers never show stale styles.

## Truth rules

- Every resource link was opened and checked in September 2026. Re-check before launch and
  every few months: `.gov` pages move.
- Every video is a public upload on @collegeconversations. Never link the 22 unlisted ones.
- Channel numbers (350K+ views, 5,400+ subscribers, 51K+ on Understanding Credit Hours) come
  from YouTube Studio, September 2026.

## Publishing

The site is live at https://collegeconversations.org (GitHub Pages, repo
`hectorivangq/College-Conversations`, source `main` /docs, DNS at Squarespace).
To publish a change:

```bash
python3 build/build.py
git add -A && git commit -m "Describe the change" && git push
```

Pages redeploys in about a minute. Re-check links every few months (`.gov` pages move),
and show Dr. Fedor the new logo before it goes on the channel.
