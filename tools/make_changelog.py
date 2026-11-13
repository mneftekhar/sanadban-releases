"""Writes CHANGELOG.md from docs/changelog.json (the one place the changelog is edited).
Usage: python tools/make_changelog.py"""
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
data = json.loads((root / "docs" / "changelog.json").read_text(encoding="utf-8"))
FA_DIGITS = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")
KINDS = [("added", "Added", "افزوده شد"), ("changed", "Changed", "تغییر کرد"),
         ("fixed", "Fixed", "رفع شد"), ("removed", "Removed", "حذف شد")]
REPO = "https://github.com/mneftekhar/sanadban-releases/releases/tag/v"

out = ["# Changelog / تاریخچهٔ تغییرات", "",
       "Every published version of SanadBan. Installed copies update themselves; the newest download is on the",
       "[releases page](https://github.com/mneftekhar/sanadban-releases/releases/latest).", "",
       '<div dir="rtl">', "",
       "همهٔ نسخه‌های منتشرشدهٔ سندبان. نسخه‌های نصب‌شده خودشان به‌روز می‌شوند؛ تازه‌ترین فایل در",
       "[صفحهٔ انتشارها](https://github.com/mneftekhar/sanadban-releases/releases/latest) است.", "", "</div>", ""]
for r in data["releases"]:
    v, d = r["version"], r["date"]
    out += ["---", "", f"## [{v}]({REPO}{v}) — {d} ({r['codename']['en']})", "", r["summary"]["en"], ""]
    for key, en, _ in KINDS:
        if r[key]:
            out += [f"### {en}", ""] + [f"- {i['en']}" for i in r[key]] + [""]
    out += ['<div dir="rtl">', "", f"### نسخهٔ {v.translate(FA_DIGITS)} ({r['codename']['fa']})", "", r["summary"]["fa"], ""]
    for key, _, fa in KINDS:
        if r[key]:
            out += [f"#### {fa}", ""] + [f"- {i['fa']}" for i in r[key]] + [""]
    out += ["</div>", ""]
(root / "CHANGELOG.md").write_text("\n".join(out), encoding="utf-8")
print("CHANGELOG.md written:", len(data["releases"]), "releases")
