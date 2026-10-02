"""Builds site/index.html from content.py. Run from anywhere:

    python3 websites/college-conversations/build/build.py

It also downloads each video's thumbnail once into site/img/yt/ (16:9 WebP),
so the page never hotlinks YouTube images.
"""
import html, json, os, sys, urllib.request, io
from pathlib import Path

HERE = Path(__file__).resolve().parent
SITE = HERE.parent / "docs"
sys.path.insert(0, str(HERE))
import content as C  # noqa: E402

e = html.escape


def thumbs():
    from PIL import Image
    out = SITE / "img" / "yt"
    out.mkdir(parents=True, exist_ok=True)
    for key, (vid, _, _) in C.VIDEOS.items():
        dest = out / f"{vid}-640.webp"
        if dest.exists():
            continue
        data = None
        for q in ("maxresdefault", "sddefault", "hqdefault"):
            try:
                with urllib.request.urlopen(f"https://i.ytimg.com/vi/{vid}/{q}.jpg", timeout=20) as r:
                    data = r.read()
                im = Image.open(io.BytesIO(data)).convert("RGB")
                if q != "maxresdefault":  # 4:3 frames carry letterbox bars: crop to 16:9
                    h = round(im.width * 9 / 16)
                    top = (im.height - h) // 2
                    im = im.crop((0, top, im.width, top + h))
                break
            except Exception:
                data = None
        if data is None:
            raise SystemExit(f"no thumbnail for {key} {vid}")
        for w in (640, 960):
            if w > im.width and w != 640:
                continue
            im.resize((w, round(w * 9 / 16)), Image.LANCZOS).save(out / f"{vid}-{w}.webp", quality=78, method=6)
        print("thumb", key, vid, q)


# ---------------------------------------------------------------- icons
ICON_PATHS = {
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "out": '<path d="M7 17 17 7M9 7h8v8"/>',
    "play": '<path d="M8 5.5v13l11-6.5z" fill="currentColor" stroke="none"/>',
    "search": '<circle cx="11" cy="11" r="7"/><path d="m20 20-3.6-3.6"/>',
    "check": '<path d="m5 12.5 4.5 4.5L19 7.5"/>',
    "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
    "close": '<path d="M6 6l12 12M18 6 6 18"/>',
    "pause": '<path d="M9 6v12M15 6v12"/>',
    "reset": '<path d="M4 12a8 8 0 1 0 2.4-5.7M4 4v5h5"/>',
    "plus": '<path d="M12 5v14M5 12h14"/>',
    "minus": '<path d="M5 12h14"/>',
    "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>',
}


def icon(name, cls="icon"):
    """One shared sprite (see sprite()); each use is a tiny <use> reference."""
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><use href="#i-{name}"/></svg>')


def sprite():
    syms = "".join(f'<symbol id="i-{k}" viewBox="0 0 24 24">{v}</symbol>' for k, v in ICON_PATHS.items())
    return f'<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">{syms}</svg>'


# The College Conversations mark: a mortarboard worn at a slight tilt on a
# conversation bubble with CC inside. Bubble and letter colours come from CSS
# custom properties so one SVG works on cream (navy bubble) and on navy
# (cream bubble). Each copy gets its own gradient id.
LOGO_SVG = (
    '<svg class="{cls}" viewBox="0 0 64 64" aria-hidden="true" focusable="false">'
    '<defs><linearGradient id="{gid}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFD067"/><stop offset="1" stop-color="#F5B335"/></linearGradient></defs>'
    '<path d="M14 26h36a10 10 0 0 1 10 10v10a10 10 0 0 1-10 10H28l-11 7.5 2.2-7.5H14A10 10 0 0 1 4 46V36a10 10 0 0 1 10-10z" fill="var(--logo-bubble, #0B1F3A)"/>'
    '<path d="M26.9 36.2A7 7 0 1 0 26.9 45.8M44.9 36.2A7 7 0 1 0 44.9 45.8" fill="none" stroke="var(--logo-ink, #F6F1E7)" stroke-width="4.2" stroke-linecap="round"/>'
    '<g transform="rotate(-9 32 18)">'
    '<path d="M19.5 15.5v9.2c3.2 2.6 7.6 3.9 12.5 3.9s9.3-1.3 12.5-3.9v-9.2z" fill="#C98A1E"/>'
    '<path d="M5 13.2v2.6L32 26.4l27-10.6v-2.6L32 23.8z" fill="#D9982A"/>'
    '<path d="M32 2.6 59 13.2 32 23.8 5 13.2z" fill="url(#{gid})"/>'
    '<path d="M32 13.2 55.5 14.6" stroke="#A9741A" stroke-width="1.3" stroke-linecap="round"/>'
    '<ellipse cx="32" cy="13.2" rx="2.3" ry="1.3" fill="#A9741A"/></g>'
    '<path d="M55.3 10.6V23" stroke="#F5B335" stroke-width="1.6" stroke-linecap="round"/>'
    '<path d="M53.8 22.6h3l1.3 8.4h-5.6z" fill="#F5B335"/><circle cx="55.3" cy="22.6" r="1.7" fill="#F5B335"/></svg>')


class _Logo:
    n = 0

    def format(self, cls):
        _Logo.n += 1
        return LOGO_SVG.replace("{cls}", cls).replace("{gid}", f"capg{_Logo.n}")


CAP = LOGO = _Logo()

GHOST = ('<svg class="{cls}" viewBox="0 0 150 140" aria-hidden="true" focusable="false">'
         '<g transform="translate(8,0)" fill="none" stroke="currentColor" stroke-width="1.2">'
         '<g transform="rotate(-12 60 43)"><path d="M43 52 L45.5 74 Q61 84 77.5 74 L80 52"/>'
         '<path d="M60 14 L114 43 L60 66 L6 43 Z"/><circle cx="60" cy="42" r="4.2"/></g>'
         '<path d="M7.2 54.2 C 4.5 63 3 72 3.2 80"/><circle cx="3.4" cy="87.5" r="6.4"/></g></svg>')


def yt(key):
    return C.VIDEOS[key]


def watch_url(key):
    return f"https://www.youtube.com/watch?v={yt(key)[0]}"


def video_link(key, cls="vlink"):
    vid, title, dur = yt(key)
    return (f'<a class="{cls}" href="{watch_url(key)}" data-video="{vid}" data-title="{e(title)}">'
            f'<span class="vlink__play">{icon("play")}</span><span class="vlink__text">Watch Dr. Fedor: '
            f'<span class="vlink__title">{e(title)}</span> <span class="vlink__dur">{dur}</span></span></a>')


def slug(s):
    return "".join(c.lower() if c.isalnum() else "-" for c in s).strip("-").replace("--", "-")


# ---------------------------------------------------------------- sections
def header():
    nav = [("#roadmap", "Roadmap"), ("#library", "Library"), ("#tools", "Tools"),
           ("#decoder", "Decoder"), ("#videos", "Videos"), ("#about", "About")]
    links = "".join(f'<a href="{h}">{t}</a>' for h, t in nav)
    mlinks = "".join(f'<a href="{h}">{t}</a>' for h, t in nav)
    return f'''
<a class="skip-link" href="#main">Skip to content</a>
<div class="progress" aria-hidden="true"><span></span></div>
<header class="site-header">
  <div class="container bar">
    <a class="brand" href="#top" aria-label="College Conversations with Dr. Janice Fedor, home">
      {CAP.format(cls="brand__mark")}
      <span class="brand__text"><span class="brand__name">College <em>Conversations</em></span><span class="brand__by">with Dr. Janice Fedor</span></span>
    </a>
    <nav class="nav" aria-label="Main">{links}</nav>
    <a class="btn btn--gold btn--sm header-cta" href="{C.SUBSCRIBE}" rel="noopener">Subscribe on YouTube</a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="mobile-nav" aria-label="Open menu">{icon("menu", "icon icon--open")}{icon("close", "icon icon--close")}</button>
  </div>
  <div class="container mobile-nav" id="mobile-nav" hidden>
    <nav aria-label="Mobile">{mlinks}</nav>
    <a class="btn btn--gold" href="{C.SUBSCRIBE}" rel="noopener">Subscribe on YouTube {icon("arrow", "icon arrow")}</a>
  </div>
</header>'''


def hero():
    chips = "".join(f'<a class="qchip" href="#library" data-q="{e(q)}">{e(q)}</a>'
                    for q in ["FAFSA", "Scholarships", "Credit hours", "Internships", "Mental health", "Free textbooks"])
    n = len(C.RESOURCES)
    return f'''
<section class="hero" id="top">
  <div class="container">
    <div class="hero__card">
      <div class="hero__bg" aria-hidden="true"><span class="hero__glow"></span><span class="hero__ring hero__ring--1"></span><span class="hero__ring hero__ring--2"></span></div>
      <div class="hero__copy">
        <p class="pill" data-reveal><span class="pill__dot"></span>Free resource library, every link checked {C.CHECKED}</p>
        <h1 class="hero__title" data-split>College doesn't come with instructions. <em class="hero__accent">Here they are.<svg class="hero__swash" data-reveal viewBox="0 0 420 26" preserveAspectRatio="none" aria-hidden="true" focusable="false"><path pathLength="1" d="M4 18 C 90 6, 200 4, 416 12" fill="none" stroke="currentColor" stroke-width="5" stroke-linecap="round"/></svg></em></h1>
        <p class="hero__lede">The forms, tools, deadlines and straight answers you need from senior year to your first job, gathered by Dr. Janice Fedor after two decades as a professor, advisor and administrator.</p>
        <form class="finder" role="search" action="#library" data-reveal style="--i:4">
          <label class="visually-hidden" for="hero-q">Search {n} resources</label>
          {icon("search", "icon finder__icon")}
          <input id="hero-q" name="q" type="search" placeholder="What do you need?" autocomplete="off">
          <button class="btn btn--gold finder__btn" type="submit"><span class="finder__btn-text">Find it</span> {icon("arrow", "icon arrow")}</button>
        </form>
        <div class="qchips" data-reveal style="--i:5"><span class="qchips__label">Popular:</span>{chips}</div>
      </div>
      <div class="hero__visual" data-reveal>
        <div class="arch">
          <span class="arch__line" aria-hidden="true"></span>
          <div class="arch__photo"><img src="img/fedor-profile-1100.webp" srcset="img/fedor-profile-700.webp 700w, img/fedor-profile-1100.webp 1100w" sizes="(min-width: 56rem) 400px, 68vw" width="1100" height="1375" alt="Dr. Janice Fedor smiling in her office" fetchpriority="high"></div>
          <p class="hero__tag"><span class="hero__tag-k">Your guide</span>Dr. Janice Fedor</p>
          <p class="hero__creds" aria-hidden="true">Professor<span></span>Advisor<span></span>Administrator</p>
        </div>
      </div>
    </div>
    <ul class="catalog" role="list" data-stagger>
      <li><a class="ccard" href="#videos">
        <span class="ccard__call"><span>No. 01</span><span>Videos</span></span>
        <span class="ccard__num">51K+</span>
        <span class="ccard__label">views on her credit hour explainer</span>
        <span class="ccard__stamp" aria-hidden="true">Most<br>watched</span>
        <span class="ccard__go">Watch it {icon("arrow", "icon")}</span>
      </a></li>
      <li><a class="ccard" href="#library">
        <span class="ccard__call"><span>No. 02</span><span>Library</span></span>
        <span class="ccard__num">{n}</span>
        <span class="ccard__label">tools and official links, every one opened and checked</span>
        <span class="ccard__stamp" aria-hidden="true">Checked<br>{C.CHECKED.split()[0][:3]} {C.CHECKED.split()[1]}</span>
        <span class="ccard__go">Browse them {icon("arrow", "icon")}</span>
      </a></li>
      <li><a class="ccard" href="#roadmap">
        <span class="ccard__call"><span>No. 03</span><span>Roadmap</span></span>
        <span class="ccard__num">6</span>
        <span class="ccard__label">stages, from senior year of high school to your first job</span>
        <span class="ccard__stamp" aria-hidden="true">In<br>order</span>
        <span class="ccard__go">Start the checklist {icon("arrow", "icon")}</span>
      </a></li>
    </ul>
  </div>
</section>'''


def marquee():
    items = "".join(f'<li>{e(t)}</li><li class="sep" aria-hidden="true">{icon("plus", "icon")}</li>' for t in C.MARQUEE)
    return f'''
<section class="ticker" aria-label="Topics this library explains">
  <div class="ticker__row">
    <div class="marquee"><div class="marquee__track"><ul>{items}</ul><ul aria-hidden="true">{items}</ul></div></div>
    <button class="ticker__pause" type="button" aria-pressed="false" aria-label="Pause the moving topics">{icon("pause", "icon")}</button>
  </div>
</section>'''


def paths():
    tiles = []
    for i, (stage_id, lib_stage, title, sub) in enumerate(C.PATHS):
        st = next(s for s in C.ROADMAP if s["id"] == stage_id)
        tiles.append(f'''<a class="path path--{i}" href="#stage-{stage_id}" data-stage="{lib_stage}">
      <span class="path__n">{st["n"]}</span>
      <span class="path__title">{e(title)}</span>
      <span class="path__sub">{e(sub)}</span>
      <span class="path__go">Show me {icon("arrow", "icon arrow")}</span>
    </a>''')
    return f'''
<section class="section paths-sec" aria-labelledby="paths-h">
  <div class="container">
    <div class="section-head section-head--split">
      <div class="stack stack--xs">
        <p class="eyebrow">Start here</p>
        <h2 class="h2" id="paths-h" data-split>Where are you right now? <span class="soft">Start there.</span></h2>
      </div>
      <p class="lede" data-reveal>Pick the stage you're in. You'll jump straight to the checklist for it, and the library will narrow to what matters for that stage.</p>
    </div>
    <div class="paths" data-stagger>{"".join(tiles)}
      <a class="path path--help" href="#faq">
        <span class="path__n">{icon("plus", "icon")}</span>
        <span class="path__title">I'm helping a student</span>
        <span class="path__sub">Parents, counselors and mentors: start with the questions families ask most.</span>
        <span class="path__go">Show me {icon("arrow", "icon arrow")}</span>
      </a>
    </div>
  </div>
</section>'''


def roadmap():
    total = sum(len(s["items"]) for s in C.ROADMAP)
    stages = []
    for s in C.ROADMAP:
        items = []
        for j, (text, link) in enumerate(s["items"]):
            cid = f'{s["id"]}-{j}'
            if link is None:
                extra = ""
            elif link[0] == "video":
                extra = video_link(link[1])
            else:
                extra = f'<a class="xlink" href="{link[2]}" target="_blank" rel="noopener">{e(link[1])}{icon("out", "icon")}<span class="visually-hidden"> (opens in a new tab)</span></a>'
            items.append(f'''<li class="task">
          <input type="checkbox" id="t-{cid}" data-task="{cid}">
          <label for="t-{cid}"><span class="task__box" aria-hidden="true">{icon("check", "icon")}</span><span class="task__text">{e(text)}</span></label>
          {f'<div class="task__link">{extra}</div>' if extra else ''}
        </li>''')
        stages.append(f'''<li class="stage" id="stage-{s["id"]}" data-stage-id="{s["id"]}">
      <div class="stage__node" aria-hidden="true"><span>{s["n"]}</span></div>
      <div class="stage__card" data-reveal>
        <div class="stage__head">
          <div><p class="stage__when">{e(s["when"])}</p><h3 class="stage__title">{e(s["title"])}</h3></div>
          <p class="stage__count" data-stage-count="{s["id"]}"><span>0</span> of {len(s["items"])}</p>
        </div>
        <ul class="tasks" role="list">{"".join(items)}</ul>
      </div>
    </li>''')
    return f'''
<section class="section section--sand roadmap-sec" id="roadmap" aria-labelledby="roadmap-h">
  <div class="container roadmap">
    <div class="roadmap__side">
      <div class="roadmap__sticky">
        <p class="eyebrow">The roadmap</p>
        <h2 class="h2" id="roadmap-h" data-split>Senior year to first job, <span class="soft">in the order it happens.</span></h2>
        <p class="lede" data-reveal>Thirty-five things that decide how college goes, almost every one linked to the tool or explainer that gets it done. Tick them off as you go; your progress stays on this device.</p>
        <div class="meter" data-reveal>
          <svg class="meter__ring" viewBox="0 0 120 120" aria-hidden="true"><circle cx="60" cy="60" r="52" class="meter__track"/><circle cx="60" cy="60" r="52" class="meter__fill" pathLength="100"/></svg>
          <div class="meter__text"><p class="meter__num"><span data-done>0</span><span class="meter__of">/{total}</span></p><p class="meter__label">done</p></div>
          <p class="visually-hidden" aria-live="polite" data-meter-live></p>
        </div>
        <button class="btn btn--ghost btn--sm reset" type="button" data-reset>{icon("reset", "icon")} Reset my checklist</button>
      </div>
    </div>
    <ol class="stages" role="list">
      <span class="stages__rail" aria-hidden="true"><span class="stages__fill"></span></span>
      {"".join(stages)}
    </ol>
  </div>
</section>'''.replace("Thirty-five", number_word(total))


def number_word(n):
    words = {30: "Thirty", 31: "Thirty-one", 32: "Thirty-two", 33: "Thirty-three", 34: "Thirty-four",
             35: "Thirty-five", 36: "Thirty-six", 37: "Thirty-seven", 38: "Thirty-eight"}
    return words.get(n, str(n))


def library():
    cats = []
    index = []
    for cid, name, blurb in C.CATEGORIES:
        rs = sorted((r for r in C.RESOURCES if r["cat"] == cid), key=lambda r: r["price"] != "Government")
        cards = []
        for r in rs:
            dom = r["url"].split("/")[2].replace("www.", "")
            v = r["video"]
            vhtml = f'<div class="res__video">{video_link(v, "vlink vlink--sm")}</div>' if v else ""
            gov = " res--gov" if r["price"] == "Government" else ""
            search = " ".join([r["name"], r["org"], r["desc"], name, dom]).lower()
            cards.append(f'''<li class="res{gov}" data-stages="{" ".join(r["stages"])}">
          <a class="res__link" href="{r["url"]}" target="_blank" rel="noopener">
            <span class="res__top"><span class="res__price">{e(r["price"])}</span><span class="res__dom">{e(dom)}</span></span>
            <span class="res__name">{e(r["name"])}{icon("out", "icon res__out")}</span>
{"" if r["org"] == r["name"] else f'            <span class="res__org">{e(r["org"])}</span>'}
            <span class="res__desc">{e(r["desc"])}</span>
            <span class="visually-hidden"> (opens in a new tab)</span>
          </a>{vhtml}
        </li>''')
        cats.append(f'''<section class="cat" id="cat-{cid}" data-cat="{cid}" aria-labelledby="cat-{cid}-h">
        <div class="cat__head"><h3 class="cat__title" id="cat-{cid}-h">{e(name)}</h3><p class="cat__blurb">{e(blurb)}</p></div>
        <ul class="res-grid" role="list" id="grid-{cid}">{"".join(cards)}</ul>
        <button class="more" type="button" aria-controls="grid-{cid}" aria-expanded="false" hidden>Show all {len(rs)} in {e(name.lower())}</button>
      </section>''')
        index.append(f'<li><a href="#cat-{cid}" data-index="{cid}"><span>{e(name)}</span><span class="n" data-index-count="{cid}">{len(rs)}</span></a></li>')
    stages = "".join(f'<button type="button" class="seg__btn" data-filter-stage="{k}" aria-pressed="false">{v}</button>' for k, v in C.STAGES.items())
    n = len(C.RESOURCES)
    return f'''
<section class="section library-sec" id="library" aria-labelledby="library-h">
  <div class="container">
    <div class="section-head section-head--split">
      <div class="stack stack--xs">
        <p class="eyebrow">The library</p>
        <h2 class="h2" id="library-h" data-split>{n} resources, almost all free. <span class="soft">No ads. No sign-up.</span></h2>
      </div>
      <p class="lede" data-reveal>Official government tools first, then the best free ones from nonprofits, universities and companies. Every link was opened and checked in {C.CHECKED}.</p>
    </div>
    <div class="libbar" data-reveal>
      <label class="search"><span class="visually-hidden">Search the library</span>{icon("search", "icon")}
        <input id="lib-q" type="search" placeholder="Search: loans, jobs, 988" autocomplete="off"></label>
      <div class="seg" role="group" aria-label="Filter by stage"><button type="button" class="seg__btn" data-filter-stage="all" aria-pressed="true">Everything</button>{stages}</div>
      <p class="libbar__count" aria-live="polite"><span data-lib-count>{n}</span> resources</p>
    </div>
    <div class="library">
      <nav class="lib-index" aria-label="Library categories"><p class="lib-index__head">Categories</p><ul role="list">{"".join(index)}</ul></nav>
      <div class="lib-main">
        {"".join(cats)}
        <div class="empty" hidden>
          <p class="empty__title">Nothing matches that yet.</p>
          <p>Try a broader word, like <button type="button" class="linkish" data-q="aid">aid</button>, <button type="button" class="linkish" data-q="writing">writing</button> or <button type="button" class="linkish" data-q="jobs">jobs</button>. Or ask Dr. Fedor in the comments on <a href="{C.CHANNEL}" rel="noopener">YouTube</a>.</p>
        </div>
      </div>
    </div>
  </div>
</section>'''


def tools():
    credit_opts = "".join(f'<option value="{v}"{" selected" if v == 120 else ""}>{t}</option>'
                          for v, t in [(60, "Associate (60)"), (120, "Bachelor's (120)")])
    grades = [("A", 4.0), ("A-", 3.7), ("B+", 3.3), ("B", 3.0), ("B-", 2.7), ("C+", 2.3), ("C", 2.0), ("C-", 1.7), ("D+", 1.3), ("D", 1.0), ("F", 0.0)]
    grade_opts = '<option value="" selected>Grade</option>' + "".join(f'<option value="{p}">{g}</option>' for g, p in grades)
    return f'''
<section class="section section--inverse tools-sec" id="tools" aria-labelledby="tools-h">
  <div class="container">
    <div class="section-head section-head--split">
      <div class="stack stack--xs">
        <p class="eyebrow">Tools</p>
        <h2 class="h2" id="tools-h" data-split>Do the math <span class="soft">before you register.</span></h2>
      </div>
      <p class="lede" data-reveal>The two numbers that shape every semester: how much work your schedule really is, and what it does to your GPA.</p>
    </div>
    <div class="tabs" data-reveal>
      <div class="tabs__list" role="tablist" aria-label="Calculators">
        <button class="tabs__tab" role="tab" id="tab-credit" aria-controls="panel-credit" aria-selected="true">Credit hour calculator</button>
        <button class="tabs__tab" role="tab" id="tab-gpa" aria-controls="panel-gpa" aria-selected="false" tabindex="-1">GPA calculator</button>
      </div>

      <div class="panel calc" role="tabpanel" id="panel-credit" aria-labelledby="tab-credit">
        <div class="calc__inputs">
          <div class="field field--range">
            <label for="credits">Credits this semester</label>
            <output class="calc__big" for="credits" id="credits-out">15</output>
            <input id="credits" type="range" min="1" max="21" step="1" value="15" aria-describedby="credits-hint">
            <div class="range-scale" aria-hidden="true"><span>1</span><span>6</span><span>12</span><span>15</span><span>21</span></div>
            <p class="hint" id="credits-hint">Most classes are 3 credits, so 15 credits is usually five classes.</p>
          </div>
          <div class="field-row">
            <div class="field"><label for="degree">Degree (credits)</label><select id="degree">{credit_opts}</select></div>
            <div class="field"><label for="earned">Credits already earned</label><input id="earned" type="number" inputmode="numeric" min="0" max="200" value="0"></div>
          </div>
        </div>
        <div class="calc__out" aria-live="polite">
          <div class="calc__status"><span class="status" data-status>Full-time</span><span class="calc__classes" data-classes>about 5 classes</span></div>
          <div class="week">
            <div class="week__row"><span class="week__label">In class</span><span class="week__bar"><span class="week__fill week__fill--class" data-bar="class"></span></span><span class="week__val" data-val="class">15 hrs</span></div>
            <div class="week__row"><span class="week__label">Outside class</span><span class="week__bar"><span class="week__fill week__fill--out" data-bar="out"></span></span><span class="week__val" data-val="out">30 hrs</span></div>
            <div class="week__row week__row--total"><span class="week__label">Every week</span><span class="week__bar"><span class="week__fill week__fill--total" data-bar="total"></span><span class="week__mark" title="A 40-hour work week"></span></span><span class="week__val" data-val="total">45 hrs</span></div>
            <p class="week__legend"><span class="week__legend-mark" aria-hidden="true"></span> The dashed line is a 40-hour work week.</p>
          </div>
          <p class="calc__finish" data-finish>At 15 credits a term, you finish in <strong>8 semesters</strong>, about <strong>4 years</strong>.</p>
          <p class="calc__note">Based on the federal definition of a credit hour: an hour of class and at least two hours of work outside it each week, over about 15 weeks. Full-time is usually 12 credits or more, but your school sets the rules. {video_link("credit", "vlink vlink--inv")}</p>
        </div>
      </div>

      <div class="panel gpa" role="tabpanel" id="panel-gpa" aria-labelledby="tab-gpa" hidden>
        <div class="gpa__table">
          <div class="gpa__head" aria-hidden="true"><span>Course</span><span>Credits</span><span>Grade</span><span></span></div>
          <ol class="gpa__rows" role="list" data-gpa-rows></ol>
          <template id="gpa-row"><li class="gpa__row">
            <input class="gpa__name" type="text" aria-label="Course name (optional)" placeholder="Course name (optional)">
            <select class="gpa__cr" aria-label="Credits"><option>1</option><option>2</option><option selected>3</option><option>4</option><option>5</option></select>
            <select class="gpa__gr" aria-label="Grade">{grade_opts}</select>
            <button class="gpa__del" type="button" aria-label="Remove this course">{icon("minus", "icon")}</button>
          </li></template>
          <button class="btn btn--ghost btn--sm" type="button" data-gpa-add>{icon("plus", "icon")} Add a course</button>
          <details class="gpa__prior">
            <summary>Add my GPA so far</summary>
            <div class="field-row">
              <div class="field"><label for="prior-gpa">Current GPA</label><input id="prior-gpa" type="number" inputmode="decimal" min="0" max="4" step="0.01" placeholder="3.20"></div>
              <div class="field"><label for="prior-cr">Credits it covers</label><input id="prior-cr" type="number" inputmode="numeric" min="0" max="250" placeholder="30"></div>
            </div>
          </details>
        </div>
        <div class="gpa__out" aria-live="polite">
          <p class="gpa__label">Semester GPA</p>
          <p class="gpa__num" data-gpa>0.00</p>
          <div class="gpa__dial" aria-hidden="true"><span data-gpa-dial></span></div>
          <p class="gpa__meta" data-gpa-meta>0 credits</p>
          <p class="gpa__cum" data-gpa-cum hidden></p>
          <p class="calc__note">Uses the common 4.0 scale (A = 4.0, B = 3.0, with plus and minus steps). Some schools use A+ or different values; check your catalog.</p>
        </div>
      </div>
    </div>
  </div>
</section>'''


def decoder():
    letters = sorted({t[0][0].upper() for t in C.TERMS})
    cards = []
    for term, d, v in sorted(C.TERMS, key=lambda t: t[0].lower()):
        vh = f'<p class="term__video">{video_link(v, "vlink vlink--sm")}</p>' if v else ""
        cards.append(f'''<li class="term">
        <h3 class="term__name">{e(term)}</h3>
        <p class="term__def">{e(d)}</p>{vh}
      </li>''')
    return f'''
<section class="section decoder-sec" id="decoder" aria-labelledby="decoder-h">
  <div class="container">
    <div class="section-head section-head--split">
      <div class="stack stack--xs">
        <p class="eyebrow">The decoder</p>
        <h2 class="h2" id="decoder-h" data-split>The words nobody explains <span class="soft">at orientation.</span></h2>
      </div>
      <div class="stack stack--xs">
        <p class="lede" data-reveal>{len(C.TERMS)} terms, in plain English. Where Dr. Fedor has a video on one, it's linked.</p>
        <label class="search search--sm" data-reveal><span class="visually-hidden">Search the decoder</span>{icon("search", "icon")}<input id="term-q" type="search" placeholder="Look up a term" autocomplete="off"></label>
      </div>
    </div>
    <ul class="terms" role="list" id="terms-grid" data-stagger>{"".join(cards)}</ul>
    <div class="more-wrap"><button class="more" type="button" aria-controls="terms-grid" aria-expanded="false" hidden>Show all {len(C.TERMS)} terms</button></div>
    <p class="empty terms-empty" hidden>No term matches that. <a href="{C.CHANNEL}" rel="noopener">Ask it on YouTube</a> and it may become the next video.</p>
  </div>
</section>'''


def vcard(key, feature=False):
    vid, title, dur = yt(key)
    w = 960 if feature else 640
    src = f"img/yt/{vid}-{w}.webp" if (SITE / "img" / "yt" / f"{vid}-{w}.webp").exists() else f"img/yt/{vid}-640.webp"
    sizes = "(min-width: 56rem) 45vw, 100vw" if feature else "(min-width: 56rem) 24vw, (min-width: 36rem) 45vw, 100vw"
    return f'''<article class="vcard{' vcard--feature' if feature else ''}">
      <a class="vcard__thumb" href="https://www.youtube.com/watch?v={vid}" data-video="{vid}" data-title="{e(title)}" aria-label="Play {e(title)} ({dur})">
        <img src="{src}" alt="" width="{w}" height="{round(w*9/16)}" loading="lazy" decoding="async" sizes="{sizes}">
        <span class="vcard__play">{icon("play")}</span>
        <span class="vcard__dur">{dur}</span>
      </a>
      <h3 class="vcard__title"><a href="https://www.youtube.com/watch?v={vid}" rel="noopener">{e(title)}</a></h3>
    </article>'''


def videos():
    tabs, panels = [], []
    for i, (sid, name, keys) in enumerate(C.SHELVES):
        sel = i == 0
        ti = "" if sel else ' tabindex="-1"'
        tabs.append(f'<button class="chip" role="tab" id="vtab-{sid}" aria-controls="vpanel-{sid}" aria-selected="{str(sel).lower()}"{ti}>{e(name)}</button>')
        grid = "".join(vcard(k) for k in keys)
        panels.append(f'<div class="vgrid" role="tabpanel" id="vpanel-{sid}" aria-labelledby="vtab-{sid}"{"" if sel else " hidden"}>{grid}</div>')
    fvid, ftitle, fdur = yt("credit")
    return f'''
<section class="section section--sand videos-sec" id="videos" aria-labelledby="videos-h">
  <div class="container">
    <div class="feature">
      <div class="feature__copy stack">
        <p class="eyebrow">Watch</p>
        <h2 class="h2" id="videos-h" data-split>The four-minute video <span class="soft">with more than 51,000 views.</span></h2>
        <p class="lede" data-reveal>Understanding Credit Hours is the most-watched video on the channel, and the fastest way to understand your whole schedule. Start there, then pick a topic.</p>
        <div class="cluster" data-reveal><a class="btn btn--navy" href="{C.SUBSCRIBE}" rel="noopener">Subscribe for new videos {icon("arrow", "icon arrow")}</a><a class="link-arrow" href="{C.CHANNEL}/videos" rel="noopener">All videos <span>{icon("arrow", "icon")}</span></a></div>
      </div>
      <div class="feature__video" data-reveal>{vcard("credit", feature=True)}</div>
    </div>
    <div class="shelf">
      <div class="chips" role="tablist" aria-label="Video topics">{"".join(tabs)}</div>
      {"".join(panels)}
    </div>
  </div>
</section>'''


def about():
    return f'''
<section class="section about-sec" id="about" aria-labelledby="about-h">
  <div class="container">
    <div class="section-head section-head--split">
      <div class="stack stack--xs">
        <p class="eyebrow">Who made this</p>
        <h2 class="h2" id="about-h" data-split>Real college advice <span class="soft">from a real college professor.</span></h2>
      </div>
      <p class="lede" data-reveal>Twenty years on every side of the desk: the classroom, the advising office and the meetings where the rules get made.</p>
    </div>
    <div class="about-row" data-stagger>
      <div class="acard acard--navy">
        {CAP.format(cls="acard__mark")}
        <p class="acard__lead">Most students don't struggle because they aren't smart enough. They struggle because nobody told them how the system works.</p>
        <p class="acard__body">Dr. Janice Fedor has spent two decades in higher education as a professor, an advisor and an administrator. In 2021 she started <strong>College Conversations</strong> to explain the parts of college nobody explains: credit hours, degree plans, financial aid and the unwritten rules. This library is the same idea, in one place.</p>
        <a class="link-arrow acard__link" href="{C.CHANNEL}" rel="noopener">Visit the channel <span>{icon("arrow", "icon")}</span></a>
      </div>
      <div class="acard acard--photo">
        <div class="acard__glow" aria-hidden="true"></div>
        <img src="img/fedor-think-845.webp" srcset="img/fedor-think-480.webp 480w, img/fedor-think-845.webp 845w" sizes="(min-width: 64rem) 28vw, (min-width: 40rem) 45vw, 90vw" width="845" height="1385" alt="Dr. Janice Fedor in glasses, one finger raised as she makes a point" loading="lazy" decoding="async">
        <p class="acard__chip">Professor, advisor, administrator</p>
      </div>
      <div class="acard acard--stat">
        <p class="acard__big"><span data-count="350" data-suffix="K+">350K+</span></p>
        <p class="acard__biglabel">views across the channel</p>
        <dl class="acard__rows">
          <div><dt>Years in higher education</dt><dd><span data-count="20">20</span></dd></div>
          <div><dt>Subscribers</dt><dd><span data-count="5400" data-suffix="+">5,400+</span></dd></div>
          <div><dt>Views on one credit hour video</dt><dd><span data-count="51" data-suffix="K+">51K+</span></dd></div>
          <div><dt>Explaining college since</dt><dd>2021</dd></div>
        </dl>
        <p class="acard__src">From YouTube Studio, {C.CHECKED}.</p>
      </div>
    </div>
  </div>
</section>'''


def faq():
    items = "".join(f'''<details{" open" if i == 0 else ""}><summary><span>{e(q)}</span><span class="faq__icon" aria-hidden="true">{icon("plus", "icon")}</span></summary><div class="answer"><p>{e(a)}</p></div></details>'''
                    for i, (q, a) in enumerate(C.FAQ))
    return f'''
<section class="section section--surface faq-sec" id="faq" aria-labelledby="faq-h">
  <div class="container faq-wrap">
    <div class="faq-side">
      <div class="stack">
        <p class="eyebrow">Questions</p>
        <h2 class="h2" id="faq-h" data-split>What students and families <span class="soft">ask most.</span></h2>
      </div>
      <figure class="faq-photo" data-reveal>
        <span class="faq-photo__light" aria-hidden="true"></span>
        <img src="img/fedor-faq-920.webp" srcset="img/fedor-faq-480.webp 480w, img/fedor-faq-920.webp 920w" sizes="(min-width: 56rem) 24rem, 80vw" width="920" height="1150" alt="Dr. Janice Fedor smiling and pointing up toward the questions" loading="lazy" decoding="async">
      </figure>
    </div>
    <div class="faq" data-stagger>{items}</div>
  </div>
</section>'''


def cta():
    return f'''
<section class="section cta-sec" aria-labelledby="cta-h">
  <div class="container">
    <div class="cta">
      <div class="cta__rings" aria-hidden="true"><span></span><span></span><span></span></div>
      {CAP.format(cls="cta__mark")}
      <h2 class="h2 cta__title" id="cta-h" data-split>Get the next explainer <span class="soft">first.</span></h2>
      <p class="cta__lede" data-reveal>Straight answers about how college actually works, from someone who has worked inside it for twenty years. Free, on YouTube.</p>
      <div class="cluster cta__actions" data-reveal>
        <a class="btn btn--gold" href="{C.SUBSCRIBE}" rel="noopener">Subscribe on YouTube {icon("arrow", "icon arrow")}</a>
        <a class="btn btn--ghost-inv" href="{watch_url("credit")}" rel="noopener">{icon("play", "icon")} Watch the credit hour video</a>
      </div>
    </div>
  </div>
</section>'''


def footer():
    cats = "".join(f'<li><a href="#cat-{c}">{e(n)}</a></li>' for c, n, _ in C.CATEGORIES[:6])
    return f'''
<footer class="site-footer">
  <div class="container">
    <div class="crisis"><span class="crisis__icon">{icon("phone", "icon")}</span><p><strong>In crisis or thinking about suicide?</strong> Call or text <a href="tel:988">988</a>, any time, free. Or text HOME to <a href="sms:741741?&body=HOME">741741</a>.</p></div>
    <div class="footer-grid">
      <div class="stack stack--xs footer-brand">
        <a class="brand brand--inv" href="#top">{CAP.format(cls="brand__mark")}<span class="brand__text"><span class="brand__name">College <em>Conversations</em></span><span class="brand__by">with Dr. Janice Fedor</span></span></a>
        <p class="small">A free, independent library of everything high school seniors, graduates and college students need, gathered by a professor who has spent twenty years inside higher education.</p>
      </div>
      <nav aria-label="Library categories"><p class="footer-h">Library</p><ul role="list">{cats}</ul></nav>
      <nav aria-label="On this page"><p class="footer-h">On this page</p><ul role="list">
        <li><a href="#roadmap">The roadmap</a></li><li><a href="#tools">Credit hour calculator</a></li><li><a href="#tools">GPA calculator</a></li><li><a href="#decoder">The decoder</a></li><li><a href="#videos">Videos</a></li><li><a href="#faq">Questions</a></li></ul></nav>
      <nav aria-label="Elsewhere"><p class="footer-h">Watch</p><ul role="list">
        <li><a href="{C.CHANNEL}" rel="noopener">YouTube channel</a></li><li><a href="{C.SUBSCRIBE}" rel="noopener">Subscribe</a></li><li><a href="{watch_url("credit")}" rel="noopener">Understanding Credit Hours</a></li></ul></nav>
    </div>
    <div class="footer-base">
      <p class="small">&copy; <span data-year>2026</span> Dr. Janice Fedor, College Conversations.</p>
      <p class="small footer-note">Links go to outside sites we don't control. Deadlines, amounts and rules change, so confirm anything important with your school's financial aid office or registrar. Links checked {C.CHECKED}.</p>
    </div>
  </div>
</footer>
<dialog class="player" aria-label="Video player">
  <div class="player__box">
    <div class="player__bar"><p class="player__title" data-player-title></p><button class="player__close" type="button" aria-label="Close video">{icon("close", "icon")}</button></div>
    <div class="player__frame" data-player-frame></div>
  </div>
</dialog>'''


def page():
    n = len(C.RESOURCES)
    desc = (f"{n} checked resources, almost all free, for high school seniors, graduates and college students: FAFSA and aid, scholarships, "
            "study tools, careers and mental health, plus a senior-year-to-first-job checklist, a credit hour calculator "
            "and plain-English explainers from Dr. Janice Fedor.")
    ld = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "WebSite", "name": "College Conversations Resource Library", "url": C.SITE_URL, "description": desc,
             "inLanguage": "en-US", "publisher": {"@id": "#fedor"}},
            {"@type": "Person", "@id": "#fedor", "name": "Dr. Janice Fedor", "jobTitle": "Professor",
             "description": "College professor, advisor and administrator with two decades in higher education.",
             "sameAs": [C.CHANNEL]},
            {"@type": "FAQPage", "mainEntity": [
                {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in C.FAQ]},
        ],
    }
    body = "".join([sprite(), header(), '<main id="main">', hero(), marquee(), paths(), roadmap(), library(), tools(),
                    decoder(), videos(), about(), faq(), cta(), "</main>", footer()])
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>College Resource Library | Dr. Janice Fedor, College Conversations</title>
<meta name="description" content="{e(desc)}">
<meta name="theme-color" content="#0B1F3A">
<meta property="og:type" content="website">
<link rel="canonical" href="{C.SITE_URL}">
<meta property="og:url" content="{C.SITE_URL}">
<meta property="og:site_name" content="College Conversations">
<meta property="og:title" content="College doesn’t come with instructions. Here they are.">
<meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="{C.SITE_URL}og.png">
<meta property="og:image:alt" content="College Conversations with Dr. Janice Fedor: a free college resource library">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{C.SITE_URL}og.png">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="icon" href="favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="preload" href="fonts/Fraunces-SemiBold.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="fonts/Inter-Regular.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="img/fedor-profile-1100.webp" as="image" imagesrcset="img/fedor-profile-700.webp 700w, img/fedor-profile-1100.webp 1100w" imagesizes="(min-width: 56rem) 400px, 68vw">
<link rel="preload" href="fonts/Fraunces-Italic-SemiBold.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="css/app.css">
<script>document.documentElement.classList.add('js')</script>
<script type="application/ld+json">{json.dumps(ld)}</script>
</head>
<body>
{body}
<script src="js/motion.js" defer></script>
<script src="js/app.js" defer></script>
</body>
</html>
'''


def bundle_css():
    """tokens + base + site -> css/app.css, comments and whitespace stripped."""
    import re
    src = "\n".join((SITE / "css" / f).read_text(encoding="utf-8") for f in ("tokens.css", "base.css", "site.css"))
    src = re.sub(r"/\*.*?\*/", "", src, flags=re.S)
    src = re.sub(r"\s+", " ", src)
    src = re.sub(r"\s*([{};,>])\s*", r"\1", src)
    src = src.replace(";}", "}")
    (SITE / "css" / "app.css").write_text(src.strip() + "\n", encoding="utf-8")


def minify_html(doc):
    import re
    return re.sub(r">\s+<", "> <", doc)


def stamp(doc):
    """Append a content hash to local CSS/JS so browsers never run stale files."""
    import hashlib, re
    def v(m):
        path = SITE / m.group(2)
        h = hashlib.md5(path.read_bytes()).hexdigest()[:8] if path.exists() else "0"
        return f'{m.group(1)}="{m.group(2)}?v={h}"'
    return re.sub(r'(href|src)="((?:css|js)/[^"?]+)"', v, doc)


def curly(doc):
    import re
    parts = re.split(r"(<script.*?</script>|<[^>]+>)", doc, flags=re.S)
    q = re.compile(r"(?<=[A-Za-z])(?:'|&#x27;)(?=[A-Za-z])")
    return "".join(p if p.startswith("<") else q.sub("\u2019", p) for p in parts)


if __name__ == "__main__":
    thumbs()
    bundle_css()
    (SITE / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f'  <url><loc>{C.SITE_URL}</loc><lastmod>{__import__("datetime").date.today().isoformat()}</lastmod></url>\n</urlset>\n', encoding="utf-8")
    (SITE / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {C.SITE_URL}sitemap.xml\n", encoding="utf-8")
    (SITE / "CNAME").write_text(C.SITE_URL.split("/")[2] + "\n", encoding="utf-8")
    (SITE / "index.html").write_text(stamp(minify_html(curly(page()))), encoding="utf-8")
    print("wrote", SITE / "index.html", "resources:", len(C.RESOURCES), "tasks:", sum(len(s['items']) for s in C.ROADMAP), "terms:", len(C.TERMS))
