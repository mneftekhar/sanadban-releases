"""Builds everything public about SanadBan from site/content.json, site/changelog.json and the GitHub releases.

Writes:  docs/index.html (Persian), docs/en/index.html (English), docs/style.css, docs/sitemap.xml, docs/robots.txt,
         docs/404.html, docs/<indexnow key>.txt, README.md, CHANGELOG.md, guides/*.md, site/releases.json (cache)
Run:     python site/build.py            (GITHUB_TOKEN is used when set; without network the cache is used)
Only the Python standard library is needed. Prints the files that changed; in GitHub Actions also sets changed=true|false.
"""
import datetime as dt
import html
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE, DOCS, GUIDES = ROOT / "site", ROOT / "docs", ROOT / "guides"
C = json.loads((SITE / "content.json").read_text(encoding="utf-8"))
CURATED = json.loads((SITE / "changelog.json").read_text(encoding="utf-8"))["releases"]
BASE = C["site"]["url"].rstrip("/") + "/"
REPO = C["site"]["repo"]
LANGS = ("fa", "en")
FA_DIGITS = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")
KINDS = ("added", "changed", "fixed", "removed")
changed_files = []


# ---------------------------------------------------------------- small helpers
def t(obj, lang):
    return obj[lang] if isinstance(obj, dict) else obj

def num(s, lang):
    return str(s).translate(FA_DIGITS) if lang == "fa" else str(s)

def esc(s):
    return html.escape(str(s), quote=True)

def inline_html(s):
    """**bold**, `code`, [text](url) -> HTML (input is plain text, escaped first)."""
    s = esc(s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", lambda m: f'<a href="{m.group(2)}" rel="noopener">{m.group(1)}</a>', s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"`(.+?)`", r'<code dir="ltr">\1</code>', s)
    return s

def plain(s):
    return re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s).replace("**", "").replace("`", "")

def write(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    old = path.read_text(encoding="utf-8") if path.exists() else None
    if old != text:
        path.write_text(text, encoding="utf-8")
        changed_files.append(str(path.relative_to(ROOT)))

def jalali(d: dt.date):
    """Gregorian -> Jalali (the standard arithmetic algorithm)."""
    gy, gm, gd = d.year, d.month, d.day
    g_d_m = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    gy2 = gy + 1 if gm > 2 else gy
    days = 355666 + (365 * gy) + ((gy2 + 3) // 4) - ((gy2 + 99) // 100) + ((gy2 + 399) // 400) + gd + g_d_m[gm - 1]
    jy = -1595 + (33 * (days // 12053)); days %= 12053
    jy += 4 * (days // 1461); days %= 1461
    if days > 365:
        jy += (days - 1) // 365; days = (days - 1) % 365
    jm = 1 + days // 31 if days < 186 else 7 + (days - 186) // 30
    jd = 1 + (days % 31 if days < 186 else (days - 186) % 30)
    return jy, jm, jd

FA_MONTHS = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"]

def nice_date(iso, lang):
    d = dt.date.fromisoformat(iso[:10])
    if lang == "fa":
        y, m, dd = jalali(d)
        return f"{num(dd, 'fa')} {FA_MONTHS[m - 1]} {num(y, 'fa')}"
    return d.strftime("%-d %B %Y")


# ---------------------------------------------------------------- releases
def fetch_releases():
    cache = SITE / "releases.json"
    url = f"https://api.github.com/repos/{REPO}/releases?per_page=100"
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json", "User-Agent": "sanadban-site"})
    if os.environ.get("GITHUB_TOKEN"):
        req.add_header("Authorization", "Bearer " + os.environ["GITHUB_TOKEN"])
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            data = json.load(r)
        slim = [{
            "tag": x["tag_name"], "date": (x.get("published_at") or x["created_at"])[:10], "body": x.get("body") or "",
            "url": x["html_url"], "draft": x.get("draft"), "prerelease": x.get("prerelease"),
            "assets": [{"name": a["name"], "size": a["size"], "url": a["browser_download_url"]} for a in x.get("assets", [])],
        } for x in data if not x.get("draft")]
        write(cache, json.dumps(slim, ensure_ascii=False, indent=1) + "\n")
        return slim
    except Exception as e:  # offline or rate-limited: use the last good copy
        print("GitHub releases not reachable, using the cache:", e, file=sys.stderr)
        return json.loads(cache.read_text(encoding="utf-8")) if cache.exists() else []

KIND_WORDS = {
    "added": ("added", "افزوده شد", "افزوده"), "changed": ("changed", "تغییر کرد", "تغییر"),
    "fixed": ("fixed", "رفع شد", "رفع"), "removed": ("removed", "حذف شد", "حذف"),
}
KIND_RE = re.compile(r"^\s*[-*+]?\s*(" + "|".join(w for ws in KIND_WORDS.values() for w in ws) + r")\s*[:：]\s*(.+?)\s*$", re.I)
PERSIAN = re.compile(r"[؀-ۿ]")

def parse_notes(body):
    """Release notes as published by release.ps1 (-NotesEn, blank line, -NotesFa). Recognised lines:
       'Summary sentence.'  '- Added: ...'  '- Changed: ...'  '- Fixed: ...'  '- Removed: ...'
       and in Persian 'افزوده شد:' 'تغییر کرد:' 'رفع شد:' 'حذف شد:'. Any other text becomes the summary."""
    out = {"summary": {"fa": "", "en": ""}, **{k: {"fa": [], "en": []} for k in KINDS}}
    for raw in body.replace("\r", "").split("\n"):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        lang = "fa" if PERSIAN.search(line) else "en"
        m = KIND_RE.match(line)
        if m:
            word = m.group(1).lower()
            kind = next(k for k, ws in KIND_WORDS.items() if word in ws)
            out[kind][lang].append(m.group(2))
        else:
            parts = [p.strip() for p in line.split(" / ")] if " / " in line else [line]
            for p in parts:
                pl = "fa" if PERSIAN.search(p) else "en"
                out["summary"][pl] = (out["summary"][pl] + " " + p.lstrip("-* ")).strip()
    rel = {"summary": {}, **{k: [] for k in KINDS}}
    for l in LANGS:
        rel["summary"][l] = out["summary"][l] or out["summary"]["en" if l == "fa" else "fa"]
    for k in KINDS:
        fa, en = out[k]["fa"], out[k]["en"]
        for i in range(max(len(fa), len(en))):
            e = en[i] if i < len(en) else fa[i]
            f = fa[i] if i < len(fa) else e
            rel[k].append({"fa": f, "en": e})
    return rel

def vkey(v):
    return tuple(int(x) if x.isdigit() else 0 for x in re.split(r"[.\-+]", v))

def releases():
    pub = fetch_releases()
    curated = {r["version"]: r for r in CURATED}
    out = []
    for p in pub:
        v = p["tag"].lstrip("v")
        win = next((a for a in p["assets"] if a["name"].endswith("-win.zip")), None)
        if v in curated:
            r = dict(curated[v])
        else:
            r = {"version": v, "codename": None, **parse_notes(p["body"])}
        r.update(date=r.get("date") or p["date"], url=p["url"], download=win, prerelease=p.get("prerelease"))
        out.append(r)
    if not pub:  # nothing from GitHub and no cache: still show the curated history
        out = [dict(r, url=f"https://github.com/{REPO}/releases/tag/v{r['version']}", download=None) for r in CURATED]
    out.sort(key=lambda r: vkey(r["version"]), reverse=True)
    return out


# ---------------------------------------------------------------- the website
def page(lang, rels):
    L = lambda o: t(o, lang)
    other = "en" if lang == "fa" else "fa"
    pre = "" if lang == "fa" else "../"               # path back to docs/
    here = BASE if lang == "fa" else BASE + "en/"
    there = BASE + "en/" if lang == "fa" else BASE
    latest = next((r for r in rels if not r.get("prerelease")), rels[0] if rels else None)
    ver = latest["version"] if latest else ""
    dl = latest["download"]["url"] if latest and latest.get("download") else f"https://github.com/{REPO}/releases/latest"
    size_mb = latest["download"]["size"] / 1048576 if latest and latest.get("download") else 0
    size = (num(f"{size_mb:.0f}", lang) + (" مگابایت" if lang == "fa" else " MB")) if size_mb else ""
    fine = L(C["ui"]["fine"]).replace("{version}", num(ver, lang)).replace("{size}", size)
    if not size:
        fine = re.sub(r"\s*\(\)", "", fine)

    # ---- structured data for search engines
    ld = [{
        "@context": "https://schema.org", "@type": "SoftwareApplication",
        "name": C["name"][lang], "alternateName": [n for n in C["alternate_names"] if n != C["name"][lang]],
        "description": L(C["description"]), "url": here, "inLanguage": lang,
        "applicationCategory": "SecurityApplication", "applicationSubCategory": "VPN client",
        "operatingSystem": "Windows 10, Windows 11", "processorRequirements": "x64, ARM64",
        "softwareRequirements": ".NET 10 Desktop Runtime", "softwareVersion": ver,
        "datePublished": latest["date"] if latest else None, "downloadUrl": dl,
        "releaseNotes": BASE + ("" if lang == "fa" else "en/") + "#changes",
        "screenshot": BASE + f"assets/home-{lang}.webp",
        "author": {"@type": "Person", "name": L(C["site"]["author"]), "url": f"https://github.com/{C['site']['github_user']}"},
        "image": BASE + "assets/icon-512.png",
    }, {
        "@context": "https://schema.org", "@type": "FAQPage", "inLanguage": lang,
        "mainEntity": [{"@type": "Question", "name": plain(L(q["q"])),
                        "acceptedAnswer": {"@type": "Answer", "text": plain(L(q["a"]))}}
                       for q in C["faq"]["items"] + C["help"]["items"]],
    }, {
        "@context": "https://schema.org", "@type": "WebSite", "name": C["name"][lang],
        "alternateName": C["alternate_names"], "url": here, "inLanguage": lang,
    }]
    ld_json = json.dumps(ld, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")

    verify = ""
    if C["site"].get("google_site_verification"):
        verify += f'<meta name="google-site-verification" content="{esc(C["site"]["google_site_verification"])}">\n'
    if C["site"].get("bing_site_verification"):
        verify += f'<meta name="msvalidate.01" content="{esc(C["site"]["bing_site_verification"])}">\n'

    nav_links = "".join(f'<a href="#{n["id"]}">{esc(L(n))}</a>' for n in C["nav"])
    lang_switch = (f'<div class="lang" role="group" aria-label="Language / زبان">'
                   + (f'<span lang="fa">فارسی</span><a href="{pre}en/" lang="en" hreflang="en" data-go="en">English</a>' if lang == "fa"
                      else f'<a href="{pre}" lang="fa" hreflang="fa" data-go="fa">فارسی</a><span lang="en">English</span>')
                   + "</div>")

    clauses = "".join(f'<div class="clause"><dt>{esc(L(i["term"]))}</dt><dd>{inline_html(L(i["text"]))}</dd></div>'
                      for i in C["features"]["items"])
    pages = C["screens"]["pages"]
    tabs = "".join(
        f'<button type="button" role="tab" id="tab-{p["id"]}" aria-selected="{"true" if k == 0 else "false"}" tabindex="{0 if k == 0 else -1}" '
        f'data-id="{p["id"]}" data-what="{esc(L(p["what"]))}" data-alt="{esc(L(p["name"]))}">{esc(L(p["name"]))}</button>'
        for k, p in enumerate(pages))
    first = pages[0]
    steps = "".join(f"<li><span>{inline_html(L(s).replace('{version}', ver))}</span></li>" for s in C["install"]["steps"])
    def qa(items):
        return "".join(f"<details><summary>{esc(L(i['q']))}</summary><p>{inline_html(L(i['a']))}</p></details>" for i in items)
    road = "".join(f'<li class="{i["state"]}"><span class="st">{esc(L(C["roadmap"]["states"][i["state"]]))}</span><span>{inline_html(i[lang])}</span></li>'
                   for i in C["roadmap"]["items"])

    timeline = ""
    for r in rels:
        items = ""
        for k in KINDS:
            for it in r.get(k, []):
                items += f'<li><span class="kind k-{k}">{esc(L(C["changes"]["kinds"][k]))}</span><span>{inline_html(it[lang])}</span></li>'
        code = f'<br>{esc(r["codename"][lang])}' if r.get("codename") else ""
        timeline += (f'<article class="rel"><div><div class="ver"><a href="{esc(r["url"])}">{num(r["version"], lang)}</a></div>'
                     f'<div class="when"><time datetime="{r["date"]}">{nice_date(r["date"], lang)}</time>{code}</div></div>'
                     f'<div><p class="sum">{inline_html(r["summary"][lang])}</p>' + (f"<ul>{items}</ul>" if items else "") + "</div></article>")

    signed = esc(L(C["ui"]["signed"]))
    seal_font = '"Vazirmatn", sans-serif' if lang == "fa" else '"Space Grotesk", sans-serif'
    word = 'سند<b>بان</b>' if lang == "fa" else 'Sanad<b>Ban</b>'
    wclass = "word-fa" if lang == "fa" else "word"
    dl_attr = f'href="{esc(dl)}"'

    return f"""<!DOCTYPE html>
<html lang="{lang}" dir="{'rtl' if lang == 'fa' else 'ltr'}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(L(C['title']))}</title>
<meta name="description" content="{esc(L(C['description']))}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="author" content="{esc(L(C['site']['author']))}">
<link rel="canonical" href="{here}">
<link rel="alternate" hreflang="fa" href="{BASE}">
<link rel="alternate" hreflang="en" href="{BASE}en/">
<link rel="alternate" hreflang="x-default" href="{BASE}">
<link rel="alternate" type="application/atom+xml" title="SanadBan releases" href="https://github.com/{REPO}/releases.atom">
<meta name="theme-color" content="#0F4C5C">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{esc(C['name'][lang])}">
<meta property="og:title" content="{esc(L(C['title']))}">
<meta property="og:description" content="{esc(L(C['description']))}">
<meta property="og:url" content="{here}">
<meta property="og:image" content="{BASE}assets/social.png">
<meta property="og:image:width" content="1280"><meta property="og:image:height" content="640">
<meta property="og:locale" content="{'fa_IR' if lang == 'fa' else 'en_US'}">
<meta property="og:locale:alternate" content="{'en_US' if lang == 'fa' else 'fa_IR'}">
<meta name="twitter:card" content="summary_large_image">
{verify}<link rel="icon" href="{pre}assets/logo.svg" type="image/svg+xml">
<link rel="icon" href="{pre}assets/favicon-64.png" type="image/png">
<link rel="apple-touch-icon" href="{pre}assets/icon-512.png">
<link rel="preload" href="{pre}fonts/Vazirmatn-Regular.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{pre}style.css">
<script type="application/ld+json">{ld_json}</script>
<script>
/* Persian for visitors from Iran, English elsewhere. A language chosen on this site always wins. Crawlers are never
   redirected, so each language keeps its own address in search results. */
(function () {{
  var here = "{lang}", other = "{pre}{'en/' if lang == 'fa' else ''}", d = document.documentElement;
  if (/bot|crawl|spider|slurp|duckduck|bingpreview|yandex|baidu|lighthouse|preview|facebookexternalhit|telegram|whatsapp/i.test(navigator.userAgent)) return;
  var get = function (s, k) {{ try {{ return window[s].getItem(k); }} catch (e) {{ return null; }} }};
  var put = function (s, k, v) {{ try {{ window[s].setItem(k, v); }} catch (e) {{}} }};
  var go = function (l) {{ if (l && l !== here) location.replace(other + location.hash); }};
  var chosen = get("localStorage", "sb-lang") || get("sessionStorage", "sb-geo");
  if (chosen) {{ go(chosen); return; }}
  d.className = "pending"; setTimeout(function () {{ d.className = ""; }}, 1300);
  var done = false;
  function decide(cc) {{
    if (done || !cc) return; done = true;
    var l = String(cc).toUpperCase() === "IR" ? "fa" : "en";
    put("sessionStorage", "sb-geo", l);
    if (l !== here) go(l); else d.className = "";
  }}
  function ask(url, pick) {{
    var c = window.AbortController ? new AbortController() : null;
    if (c) setTimeout(function () {{ c.abort(); }}, 2500);
    fetch(url, c ? {{ signal: c.signal }} : {{}}).then(function (r) {{ return r.ok ? r.text() : ""; }}).then(pick).then(decide).catch(function () {{}});
  }}
  ask("https://www.cloudflare.com/cdn-cgi/trace", function (s) {{ var m = /(?:^|\\n)loc=([A-Z]{{2}})/.exec(s); return m && m[1]; }});
  ask("https://api.country.is/", function (s) {{ try {{ return JSON.parse(s).country; }} catch (e) {{ return null; }} }});
  ask("https://get.geojs.io/v1/ip/country.json", function (s) {{ try {{ return JSON.parse(s).country; }} catch (e) {{ return null; }} }});
}})();
</script>
</head>
<body>
<a class="skip" href="#main">{esc(L(C['ui']['skip']))}</a>

<header class="wrap bar">
  <a class="mark" href="{pre}{'' if lang == 'fa' else 'en/'}" aria-label="{esc(C['name'][lang])}">
    <img src="{pre}assets/logo.svg" alt="" width="40" height="40">
    <span class="{wclass}">{word}</span>
  </a>
  <nav class="nav" aria-label="{esc(L(C['ui']['menu']))}">{nav_links}</nav>
  <span class="spacer"></span>
  <details class="menu"><summary>{esc(L(C['ui']['menu']))}</summary><nav class="drop" aria-label="{esc(L(C['ui']['menu']))}">{nav_links}</nav></details>
  {lang_switch}
  <a class="btn get" {dl_attr}>{esc(L(C['ui']['download']))}</a>
</header>

<main id="main">
<section class="hero">
  <div class="wrap">
    <div>
      <h1>{esc(L(C['hero']['h1']))}</h1>
      <p class="lead">{esc(L(C['hero']['lead']))}</p>
      <div class="cta">
        <a class="btn" {dl_attr}>
          <svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M3 5.5 10 4.5v7H3zm0 13 7 1v-7H3zm8 1.1L21 21v-8.5H11zM11 4.4 21 3v8.5H11z"/></svg>
          {esc(L(C['ui']['download_windows']))}
        </a>
        <a href="#changes">{esc(L(C['ui']['see_changes']))}</a>
      </div>
      <p class="fine">{esc(fine)}</p>
    </div>
    <div class="stage">
      <svg class="rosette" viewBox="-200 -200 400 400" aria-hidden="true"></svg>
      <div class="window">
        <video class="js-video" src="{pre}assets/connect-{lang}.mp4" width="1000" height="612" muted loop playsinline preload="metadata"
               poster="{pre}assets/home-{lang}.webp" aria-label="{esc(L(C['ui']['connect_video']))}"></video>
      </div>
      <svg class="seal" viewBox="0 0 120 120" role="img" aria-label="{signed}">
        <circle cx="60" cy="60" r="56" fill="#E09F3E"/>
        <circle cx="60" cy="60" r="51" fill="none" stroke="#FFF6E8" stroke-width="1.2" stroke-dasharray="1.5 3"/>
        <circle cx="60" cy="60" r="45" fill="none" stroke="#FFF6E8" stroke-width=".8"/>
        <g transform="translate(44.5 27) scale(.26)">
          <path d="M60 6 L104 22 V58 C104 86 84 105 60 114 C36 105 16 86 16 58 V22 Z" fill="#FFF6E8"/>
          <path d="M44 34 H68 L80 46 V82 a4 4 0 0 1 -4 4 H44 a4 4 0 0 1 -4 -4 V38 a4 4 0 0 1 4 -4 Z" fill="#B8761F"/>
        </g>
        <text x="60" y="82" text-anchor="middle" style="font:700 15px {seal_font};fill:#FFF6E8">{signed}</text>
      </svg>
    </div>
  </div>
</section>

<section class="does" id="features" aria-labelledby="features-h">
  <div class="wrap">
    <h2 id="features-h">{esc(L(C['features']['title']))}</h2>
    <p class="lead" style="margin-bottom:2.5rem">{esc(L(C['hero']['about']))}</p>
    <dl class="clauses">{clauses}</dl>
  </div>
</section>

<section class="split" aria-labelledby="split-h">
  <div class="wrap">
    <div>
      <h2 id="split-h">{esc(L(C['split']['title']))}</h2>
      <p class="lead">{esc(L(C['split']['lead']))}</p>
    </div>
    <div class="lanes" role="img" aria-label="{esc(L(C['split']['label']))}">
      <div class="pc">
        <svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round" d="M3 5h18v11H3zM8 20h8M12 16v4"/></svg>
        <span class="node">{esc(L(C['split']['pc']))}</span>
      </div>
      <div class="lane vpn"><img class="shield" src="{pre}assets/logo.svg" alt=""></div>
      <div class="node reg">{esc(L(C['split']['reg']))}<small>{esc(L(C['split']['reg_via']))}</small></div>
      <div class="lane"></div>
      <div class="node">{esc(L(C['split']['other']))}<small>{esc(L(C['split']['other_via']))}</small></div>
    </div>
  </div>
</section>

<section class="inside" id="screens" aria-labelledby="screens-h">
  <div class="wrap">
    <h2 id="screens-h">{esc(L(C['screens']['title']))}</h2>
    <div class="viewer">
      <div class="tabs" role="tablist" aria-orientation="vertical">{tabs}</div>
      <div class="shot" role="tabpanel" aria-labelledby="tab-{first['id']}">
        <figure>
          <div class="window"><img class="js-shot" src="{pre}assets/{first['id']}-{lang}.webp" alt="{esc(L(first['name']))}" width="1600" height="978" loading="lazy"></div>
          <figcaption><span class="what js-what">{esc(L(first['what']))}</span><span class="blurred">{esc(L(C['ui']['blurred']))}</span></figcaption>
        </figure>
      </div>
    </div>
  </div>
</section>

<section class="install" id="install" aria-labelledby="install-h">
  <div class="wrap">
    <div>
      <h2 id="install-h">{esc(L(C['install']['title']))}</h2>
      <p class="lead" style="margin-top:1rem">{esc(L(C['install']['lead']))}</p>
      <p class="cta"><a class="btn" {dl_attr}>{esc(L(C['ui']['download_windows']))}</a></p>
    </div>
    <div>
      <ol class="steps">{steps}</ol>
      <p class="needs">{inline_html(L(C['install']['needs']))}</p>
    </div>
  </div>
</section>

<section class="help" id="help" aria-labelledby="help-h">
  <div class="wrap twin">
    <div>
      <h2 id="help-h">{esc(L(C['help']['title']))}</h2>
      <p class="lead" style="margin-top:1rem">{esc(L(C['help']['lead']))}</p>
      <div class="qa">{qa(C['help']['items'])}</div>
    </div>
    <div id="faq">
      <h2>{esc(L(C['faq']['title']))}</h2>
      <div class="qa">{qa(C['faq']['items'])}</div>
    </div>
  </div>
</section>

<section class="roadmap" id="roadmap" aria-labelledby="roadmap-h">
  <div class="wrap">
    <h2 id="roadmap-h">{esc(L(C['roadmap']['title']))}</h2>
    <p class="lead" style="margin-top:1rem">{esc(L(C['roadmap']['lead']))}</p>
    <ol class="road">{road}</ol>
  </div>
</section>

<section class="changes" id="changes" aria-labelledby="changes-h">
  <div class="wrap">
    <h2 id="changes-h">{esc(L(C['changes']['title']))}</h2>
    <div class="timeline">{timeline}</div>
    <p class="more"><a href="https://github.com/{REPO}/blob/main/CHANGELOG.md">{esc(L(C['ui']['full_changelog']))}</a></p>
  </div>
</section>
</main>

<footer>
  <div class="wrap">
    <div>
      <h3>{esc(L(C['developer']['title']))}</h3>
      <p>{esc(L(C['developer']['text']))}</p>
      <div class="links">
        <a href="https://github.com/{REPO}">GitHub</a>
        <a href="https://github.com/{REPO}/releases">{esc(L(C['ui']['all_releases']))}</a>
        <a href="https://github.com/{REPO}/blob/main/CHANGELOG.md">{esc(L(C['nav'][-1]))}</a>
      </div>
    </div>
    <div>
      <h3>{esc(L(C['privacy']['title']))}</h3>
      <p>{esc(L(C['privacy']['text']))}</p>
      <p class="independent">{esc(L(C['independent']))}</p>
    </div>
    <p class="small">© {esc(L(C['site']['author']))}. {esc(L(C['developer']['fonts']))}</p>
  </div>
</footer>

<script>
(function () {{
  var $ = function (s) {{ return document.querySelector(s); }};
  var reduce = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;
  /* the language switch remembers the choice */
  document.querySelectorAll("[data-go]").forEach(function (a) {{
    a.addEventListener("click", function () {{ try {{ localStorage.setItem("sb-lang", a.getAttribute("data-go")); }} catch (e) {{}} }});
  }});
  /* close the narrow-screen menu after a choice */
  document.querySelectorAll(".menu a").forEach(function (a) {{ a.addEventListener("click", function () {{ $(".menu").open = false; }}); }});
  /* the recording */
  var v = $(".js-video");
  if (reduce) v.controls = true; else {{ v.autoplay = true; var p = v.play(); if (p && p.catch) p.catch(function () {{ v.controls = true; }}); }}
  /* the pages of the app */
  var tabs = [].slice.call(document.querySelectorAll(".tabs button")), cur = 0, pre = "{pre}", lang = "{lang}";
  function show(i, focus) {{
    cur = i; var b = tabs[i];
    $(".js-shot").src = pre + "assets/" + b.dataset.id + "-" + lang + ".webp";
    $(".js-shot").alt = b.dataset.alt; $(".js-what").textContent = b.dataset.what;
    $(".shot").setAttribute("aria-labelledby", b.id);
    tabs.forEach(function (x, j) {{ x.setAttribute("aria-selected", j === i); x.tabIndex = j === i ? 0 : -1; }});
    if (focus) b.focus();
  }}
  tabs.forEach(function (b, i) {{ b.addEventListener("click", function () {{ show(i, true); }}); }});
  $(".tabs").addEventListener("keydown", function (e) {{
    var n = tabs.length, f = lang === "fa" ? ["ArrowDown", "ArrowLeft"] : ["ArrowDown", "ArrowRight"], k = e.key, i = cur;
    if (f.indexOf(k) >= 0) i = (i + 1) % n; else if (k.indexOf("Arrow") === 0) i = (i + n - 1) % n;
    else if (k === "Home") i = 0; else if (k === "End") i = n - 1; else return;
    e.preventDefault(); show(i, true);
  }});
  /* the fine line pattern of official papers, drawn once */
  var svg = $(".rosette"), NS = "http://www.w3.org/2000/svg";
  function gcd(a, b) {{ return b ? gcd(b, a % b) : a; }}
  [[150, 52, 66, 0], [150, 39, 48, .35], [118, 31, 52, .9], [176, 44, 30, .2]].forEach(function (L, k) {{
    var R = L[0], r = L[1], dd = L[2], ph = L[3], pts = [], n = 2600;
    for (var i = 0; i <= n; i++) {{
      var a = i / n * Math.PI * 2 * (r / gcd(R, r));
      pts.push((i ? "L" : "M") + ((R - r) * Math.cos(a + ph) + dd * Math.cos((R - r) / r * a + ph)).toFixed(1) + " " + ((R - r) * Math.sin(a + ph) - dd * Math.sin((R - r) / r * a + ph)).toFixed(1));
    }}
    var p = document.createElementNS(NS, "path"); p.setAttribute("d", pts.join(""));
    if (k === 2) p.style.stroke = "#D9C49C";
    svg.appendChild(p);
    if (!reduce && p.getTotalLength) {{
      var len = p.getTotalLength(); p.style.strokeDasharray = len; p.style.strokeDashoffset = len; p.getBoundingClientRect();
      p.style.transition = "stroke-dashoffset " + (2.6 + k * .5) + "s cubic-bezier(.4,0,.2,1) " + (k * .15) + "s";
      requestAnimationFrame(function () {{ p.style.strokeDashoffset = 0; }});
    }}
  }});
}})();
</script>
</body>
</html>
"""


# ---------------------------------------------------------------- GitHub pages (README, guides, changelog)
GUIDE_PAGES = [  # (file, nav id or None, title)
    ("features", "features"), ("screenshots", "screens"), ("install", "install"),
    ("troubleshooting", "help"), ("faq", "faq"), ("updates", None), ("privacy", None), ("roadmap", "roadmap"),
]

def menu(from_root):
    p = "" if from_root else "../"
    g = "guides/" if from_root else ""
    links = [f'<a href="{p}README.md">خانه · Home</a>']
    for n in C["nav"]:
        target = f"{p}CHANGELOG.md" if n["page"] == "changelog" else f"{g}{n['page']}.md"
        links.append(f'<a href="{target}">{n["fa"]} · {n["en"]}</a>')
    links.insert(-1, f'<a href="{g}updates.md">به‌روزرسانی · Updates</a>')
    links.insert(-1, f'<a href="{g}privacy.md">حریم خصوصی · Privacy</a>')
    links.append(f'<a href="{BASE}">وب‌سایت · Website</a>')
    return '<p align="center">\n  ' + " &nbsp;|&nbsp;\n  ".join(links) + "\n</p>"

def md_page(title, fa_body, en_body, from_root=False):
    note = f"<!-- {C['ui']['generated']['en']} -->\n"
    return (note + menu(from_root) + "\n\n"
            + f'<div dir="rtl">\n\n# {title["fa"]}\n\n{fa_body.strip()}\n\n<a href="#english">English ↓</a>\n\n</div>\n\n---\n\n'
            + f'<a id="english"></a>\n\n# {title["en"]}\n\n{en_body.strip()}\n')

def md_list(items, lang):
    return "\n".join(f"- {i[lang] if isinstance(i, dict) and lang in i else t(i, lang)}" for i in items)

def md_qa(items, lang):
    return "\n\n".join(f"### {i['q'][lang]}\n\n{i['a'][lang]}" for i in items)

def md_shots(lang):
    rows = []
    for p in C["screens"]["pages"]:
        rows.append(f"### {p['name'][lang]}\n\n{p['what'][lang]}\n\n"
                    f'<img src="../docs/assets/{p["id"]}-{lang}.webp" width="820" alt="{p["name"][lang]}">')
    return C["ui"]["blurred"][lang] + "\n\n" + "\n\n".join(rows) + (
        f'\n\n<details><summary>{C["ui"]["tour"][lang]}</summary>\n\n<img src="../docs/assets/tour-{lang}.gif" width="820" alt="">\n\n</details>')

def changelog_md(rels):
    body = {}
    for lang in LANGS:
        parts = [C["changes"]["intro"][lang]]
        for r in rels:
            v = num(r["version"], lang)
            head = f"## [{v}]({r['url']}) — {nice_date(r['date'], lang)}" + (f" ({r['codename'][lang]})" if r.get("codename") else "")
            block = [head, "", r["summary"][lang]]
            for k in KINDS:
                if r.get(k):
                    block += ["", f"**{C['changes']['kinds'][k][lang]}**", ""] + [f"- {i[lang]}" for i in r[k]]
            parts.append("\n".join(block))
        body[lang] = "\n\n".join(parts)
    return md_page({"fa": "تاریخچهٔ تغییرات", "en": "Changelog"}, body["fa"], body["en"], from_root=True)

def readme(rels):
    latest = next((r for r in rels if not r.get("prerelease")), rels[0] if rels else None)
    ver = latest["version"] if latest else ""
    dl = latest["download"]["url"] if latest and latest.get("download") else f"https://github.com/{REPO}/releases/latest"
    def block(lang):
        L = lambda o: t(o, lang)
        lat = (f"**{C['ui']['latest'][lang]}: [{num(ver, lang)}]({latest['url']})** — {C['ui']['released'][lang]} {nice_date(latest['date'], lang)} · "
               f"[{C['ui']['download_windows'][lang]}]({dl})\n\n> {latest['summary'][lang]}") if latest else ""
        feats = "\n".join(f"- **{i['term'][lang]}.** {i['text'][lang]}" for i in C["features"]["items"])
        steps = "\n".join(f"{n}. {s[lang].replace('{version}', ver)}" for n, s in enumerate(C["install"]["steps"], 1))
        return f"""{L(C['hero']['about'])}

{lat}

<p align="center"><img src="docs/assets/connect-{lang}.gif" width="760" alt="{L(C['ui']['connect_video'])}"></p>

## {L(C['features']['title'])}

{feats}

## {L(C['install']['title'])}

{steps}

{L(C['install']['needs'])}

## {L(C['developer']['title'])}

{L(C['developer']['text'])} {L(C['developer']['source'])}

{L(C['independent'])}"""
    head = f"""<!-- {C['ui']['generated']['en']} -->
<p align="center"><img src="docs/assets/logo.svg" width="88" alt="SanadBan"></p>

<h1 align="center">سندبان · SanadBan</h1>

<p align="center">{C['tagline']['fa']}<br>{C['tagline']['en']}</p>

<p align="center">
  <a href="https://github.com/{REPO}/releases/latest"><img alt="Latest release" src="https://img.shields.io/github/v/release/{REPO}?label=release&color=0F4C5C"></a>
  <img alt="Windows 10 and 11, x64 and ARM64" src="https://img.shields.io/badge/Windows%2010%20%2F%2011-x64%20%7C%20ARM64-0F4C5C">
  <a href="{BASE}"><img alt="Website" src="https://img.shields.io/badge/website-{'mneftekhar.github.io'}-E09F3E"></a>
</p>

{menu(True)}
"""
    admin = f"""<details>
<summary>For administrators: what each release contains, and how this page is built</summary>

| File | Purpose |
|---|---|
| `SanadBan-<version>-win.zip` | The one download for a first install, on any Windows PC (x64 or ARM64). |
| `SanadBan-<version>-win-x64.zip`, `SanadBan-<version>-win-arm64.zip` | The update packages; an installed copy takes the one for its own processor. |
| `manifest.json`, `manifest.json.sig` | The signed list of update packages (ECDSA P-256, SHA-256) with each package's SHA-256 and size. |

The website, this README, the pages in `guides/` and `CHANGELOG.md` are generated by `site/build.py` from
`site/content.json`, `site/changelog.json` and the published releases. The workflow `.github/workflows/site.yml` runs
it on every release, on every change under `site/`, and once a day, then deploys the website and notifies search
engines (IndexNow). Release notes become changelog entries when written like this:

```
One-sentence summary.
- Added: ...
- Changed: ...
- Fixed: ...
- Removed: ...

خلاصه در یک جمله.
- افزوده شد: ...
- تغییر کرد: ...
- رفع شد: ...
- حذف شد: ...
```
</details>
"""
    return (head + f'\n<div dir="rtl">\n\n## {C["name"]["fa"]} چیست؟\n\n' + block("fa") + '\n\n<a href="#english">English ↓</a>\n\n</div>\n\n---\n\n'
            + '<a id="english"></a>\n\n## What is SanadBan?\n\n' + block("en") + "\n\n" + admin)

def guides():
    by = lambda key: (lambda lang: md_qa(C[key]["items"], lang))
    pages = {
        "features": (C["features"]["title"], lambda l: C["hero"]["about"][l] + "\n\n" + "\n\n".join(
            f"### {i['term'][l]}\n\n{i['text'][l]}" for i in C["features"]["items"])
            + f"\n\n## {C['split']['title'][l]}\n\n{C['split']['lead'][l]}"),
        "screenshots": (C["screens"]["title"], md_shots),
        "install": (C["install"]["title"], lambda l: C["install"]["lead"][l] + "\n\n" + "\n".join(
            f"{n}. {s[l].replace('{version}', '<version>' if l == 'en' else '<نسخه>')}" for n, s in enumerate(C["install"]["steps"], 1))
            + "\n\n" + C["install"]["needs"][l] + f"\n\n[{C['ui']['download_windows'][l]}](https://github.com/{REPO}/releases/latest)"),
        "troubleshooting": (C["help"]["title"], lambda l: C["help"]["lead"][l] + "\n\n" + md_qa(C["help"]["items"], l)),
        "faq": (C["faq"]["title"], by("faq")),
        "updates": (C["updates"]["title"], lambda l: md_list(C["updates"]["items"], l)),
        "privacy": (C["privacy"]["title"], lambda l: C["privacy"]["text"][l] + "\n\n" + C["independent"][l]),
        "roadmap": (C["roadmap"]["title"], lambda l: C["roadmap"]["lead"][l] + "\n\n" + "\n".join(
            f"- **{C['roadmap']['states'][i['state']][l]}:** {i[l]}" for i in C["roadmap"]["items"])),
    }
    for name, (title, body) in pages.items():
        write(GUIDES / f"{name}.md", md_page(title, body("fa"), body("en")))


# ---------------------------------------------------------------- search-engine files
def seo_files():
    today = dt.date.today().isoformat()
    sm = DOCS / "sitemap.xml"
    old = sm.read_text(encoding="utf-8") if sm.exists() else ""
    page_changed = any(f.startswith("docs/index.html") or f.startswith("docs/en/") for f in changed_files)
    m = re.search(r"<lastmod>([\d-]+)</lastmod>", old)
    lastmod = today if page_changed or not m else m.group(1)
    alt = (f'<xhtml:link rel="alternate" hreflang="fa" href="{BASE}"/>'
           f'<xhtml:link rel="alternate" hreflang="en" href="{BASE}en/"/>'
           f'<xhtml:link rel="alternate" hreflang="x-default" href="{BASE}"/>')
    write(sm, f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <url><loc>{BASE}</loc><lastmod>{lastmod}</lastmod>{alt}</url>
  <url><loc>{BASE}en/</loc><lastmod>{lastmod}</lastmod>{alt}</url>
</urlset>
""")
    write(DOCS / "robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {BASE}sitemap.xml\n")
    key = C["site"]["indexnow_key"]
    write(DOCS / f"{key}.txt", key + "\n")
    write(DOCS / "404.html", f"""<!DOCTYPE html><html lang="fa" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex"><title>سندبان | SanadBan</title><link rel="stylesheet" href="{BASE}style.css"></head>
<body><main class="wrap" style="padding-block:5rem"><h1>این صفحه پیدا نشد.</h1><p class="lead" style="margin-top:1rem"><a href="{BASE}">بازگشت به صفحهٔ اصلی سندبان</a></p>
<p class="lead" lang="en" dir="ltr" style="margin-top:2rem">This page does not exist. <a href="{BASE}en/">Go to the SanadBan home page</a>.</p></main></body></html>
""")


def main():
    rels = releases()
    write(DOCS / "style.css", (SITE / "style.css").read_text(encoding="utf-8"))
    write(DOCS / "index.html", page("fa", rels))
    write(DOCS / "en" / "index.html", page("en", rels))
    write(ROOT / "README.md", readme(rels))
    write(ROOT / "CHANGELOG.md", changelog_md(rels))
    guides()
    seo_files()
    print("\n".join(changed_files) if changed_files else "nothing changed")
    if os.environ.get("GITHUB_OUTPUT"):
        site_changed = any(f.startswith("docs/") for f in changed_files)
        with open(os.environ["GITHUB_OUTPUT"], "a") as fh:
            fh.write(f"changed={'true' if changed_files else 'false'}\nsite_changed={'true' if site_changed else 'false'}\n")


if __name__ == "__main__":
    main()
