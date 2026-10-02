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
| `site/` | The finished static site. Upload this folder to any host. |
| `site/css/tokens.css` | Every colour, size, space and motion value. The only file with raw values. |
| `design/` | Logo drafts (A was chosen, refined in `logo-v2`), OG image and icon sources, her YouTube avatar. |
| `qa/` | Audit script, capture script and review screenshots. |

## Editing

```bash
python3 build/build.py
```

Then open `site/index.html` through a local server (the preview config is in
`.claude/launch.json`, port 4200). CSS and JS links get a content hash on every build, so
browsers never show stale styles.

## Truth rules

- Every resource link was opened and checked in September 2026. Re-check before launch and
  every few months: `.gov` pages move.
- Every video is a public upload on @collegeconversations. Never link the 22 unlisted ones.
- Channel numbers (350K+ views, 5,400+ subscribers, 51K+ on Understanding Credit Hours) come
  from YouTube Studio, September 2026.

## Before launch (Hector's call)

1. Pick the domain and host (Netlify, Vercel or Cloudflare Pages all serve `site/` as-is).
2. Once the domain exists, add a canonical URL, `og:url`, absolute `og:image` URL and a
   `sitemap.xml`, and add a `Sitemap:` line to `robots.txt`.
3. Show Dr. Fedor the new logo before it goes anywhere public; it's a new mark, not yet on
   the channel.
