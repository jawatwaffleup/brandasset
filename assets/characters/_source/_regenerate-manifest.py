# -*- coding: utf-8 -*-
import json, re, collections

MAP = {"air maxi": "air-maxi", "bhoppu": "bhoppu", "popsicle": "icy",
       "mr waffle": "mr-waffle", "picchi": "picchi", "spacie": "spacy",
       "stovie": "stovy", "swirly": "swirly", "tv": "tvy", "tvy": "tvy",
       "merlion": "merlulu", "spacy": "spacy", "stovy": "stovy", "icy": "icy"}
DISPLAY = {"air-maxi": "Air Maxi", "bhoppu": "Bhoppu", "icy": "Icy",
           "mr-waffle": "Mr Waffle", "picchi": "Picchi", "spacy": "Spacy",
           "stovy": "Stovy", "swirly": "Swirly", "tvy": "Tvy", "merlulu": "Merlulu"}


def slug(t):
    b = t.rsplit('.', 1)[0].lower()
    b = re.sub(r'\s*cmyk\s*', ' ', b)
    b = re.sub(r'\s*t pose\s*', ' ', b)
    b = re.sub(r'\s*final\s*', ' ', b)
    b = re.sub(r'\s*\d+\s*$', '', b).strip()
    return MAP.get(b)


def num(t):
    m = re.search(r'(\d{3})', t)
    return m.group(1) if m else None


rows = []
for line in open('drive.tsv', encoding='utf-8'):
    line = line.rstrip('\n')
    if not line:
        continue
    g, t, i, s = line.split('\t')
    rows.append(dict(group=g, title=t, id=i, size=int(s), char=slug(t), pose=num(t)))


def mb(n):
    return "%.1f MB" % (n / 1048576.0)


tot = sum(r['size'] for r in rows)
by = collections.Counter()
byz = collections.Counter()
for r in rows:
    by[r['group']] += 1
    byz[r['group']] += r['size']

GN = {"root": "Root - type and campaign artwork",
      "chars": "Characters - vector masters, T-poses, Merlulu",
      "facial": "Facial expression sheets",
      "rgb": "Extra poses (RGB)",
      "cmyk": "Extra poses (CMYK, print)"}

json.dump({"source_folder": "https://drive.google.com/drive/folders/1B4OX3wWNuXCxgsRfoknhUtPM-wpOceqd",
           "folder_title": "WaffleUp_ jeremy", "indexed": "2026-08-24",
           "file_count": len(rows), "total_bytes": tot, "downloaded": [], "files": rows},
          open('manifest.json', 'w', encoding='utf-8'), indent=2)

L = []
A = L.append
A("# Drive source index — `WaffleUp_ jeremy`\n")
A("Designer working files for the Waffle Up Gang, held in Mohammad Salman's Drive and shared to Jawat.")
A("Owner of most of the artwork: **jeremy@jeremylord.com** (Jeremy Lord).\n")
A("- **Source:** https://drive.google.com/drive/folders/1B4OX3wWNuXCxgsRfoknhUtPM-wpOceqd")
A("- **Indexed:** 2026-08-24 · **%d files** · **%s** total" % (len(rows), mb(tot)))
A("- **Status:** indexed. Mirror with `import.py` once Drive for Desktop is mounted — section 5.\n")
A("> These are **editable masters** (PSD/AI). The delivery-ready PNGs already in")
A("> `assets/characters/bangladesh/` remain the files to composite with. Nothing here")
A("> changes CLAUDE.md §5 — supplied artwork only, no redraws, no AI-generated characters.\n")
A("---\n")
A("## 1. Designer naming → brand naming\n")
A("Jeremy's filenames are not the approved character names. This is the decode:\n")
A("| Drive filename stem | Brand name | Repo folder |")
A("|---|---|---|")
for k, v in [("Air maxi", "air-maxi"), ("Bhoppu", "bhoppu"), ("popsicle", "icy"),
             ("Mr Waffle", "mr-waffle"), ("picchi", "picchi"), ("Spacie", "spacy"),
             ("Stovie", "stovy"), ("Swirly", "swirly"), ("TV / TVy", "tvy"),
             ("merlion", "merlulu")]:
    loc = "singapore/merlulu" if v == "merlulu" else "bangladesh/" + v
    A("| `%s` | **%s** | `assets/characters/%s/` |" % (k, DISPLAY[v], loc))
A("")
A("`popsicle → Icy`, `Spacie → Spacy`, `Stovie → Stovy`, `TV → Tvy` and `merlion → Merlulu`")
A("are the five renames that will bite if anyone briefs straight off a raw filename.\n")
A("The `facials finals/` folder already uses the **brand** spellings (`Spacy.psd`, `Stovy.psd`),")
A("so it postdates the naming decision. Everything else still carries the working names.\n")
A("---\n")
A("## 2. What exists, per character\n")
A("| Character | Vector master | T-pose | Expression sheet | Poses (RGB) | Poses (CMYK) |")
A("|---|---|---|---|---|---|")
for c in ["air-maxi", "bhoppu", "icy", "mr-waffle", "picchi", "spacy", "stovy", "swirly", "tvy", "merlulu"]:
    sel = lambda g: [r for r in rows if r['char'] == c and r['group'] == g]
    ai = "yes" if any(r['title'].endswith('.ai') for r in sel('chars')) else "—"
    tp = "yes" if any('T pose' in r['title'] for r in sel('chars')) else "—"
    ex = "yes" if sel('facial') else "—"
    rp = sorted(set(r['pose'] for r in sel('rgb') if r['pose']))
    cp = sorted(set(r['pose'] for r in sel('cmyk') if r['pose']))
    rs = "%d (%s)" % (len(rp), ", ".join(rp)) if rp else "—"
    cs = "%d" % len(cp) if cp else "—"
    A("| **%s** | %s | %s | %s | %s | %s |" % (DISPLAY[c], ai, tp, ex, rs, cs))
A("")
A("**Mr Waffle is the only character with five poses (001–005).** Everyone else has four.\n")
A("**Merlulu has a vector master and one layered PSD, nothing else** — no T-pose, no expression")
A("sheet, no extra poses. If a Singapore brief needs her in any pose other than the one that")
A("exists, that artwork has to be commissioned. Worth knowing before promising SG content.\n")
A("---\n")
A("## 3. What this Drive closes in the repo\n")
A("Scanned against `assets/characters/` on 2026-08-24.\n")
import os
REPO = r"D:/Waffleup Office Works/brandasset/assets/characters/bangladesh"


def has(c, f):
    return os.path.exists(os.path.join(REPO, c, "2d", f))


def has3d(c):
    p = os.path.join(REPO, c, "3d")
    return os.path.isdir(p) and bool(os.listdir(p))


BD = ["air-maxi", "bhoppu", "icy", "mr-waffle", "picchi", "spacy", "stovy", "swirly", "tvy"]
A("| Character | hero | expressions | card | t-pose | 3d ref | pose variants |")
A("|---|---|---|---|---|---|---|")
for c in BD:
    n = len([r for r in rows if r['char'] == c and r['group'] == 'rgb'])
    A("| **%s** | %s | %s | %s | %s | %s | %s |" % (
        DISPLAY[c],
        "yes" if has(c, "hero.png") else "**missing**",
        "yes" if has(c, "expressions.png") else "**missing**",
        "yes" if has(c, "card.png") else "**missing**",
        "yes" if has(c, "t-pose-front.png") else "**missing — PSD in Drive**",
        "yes" if has3d(c) else "none",
        "none in repo — **%d PSDs in Drive**" % n))
A("")
miss_t = [DISPLAY[c] for c in BD if not has(c, "t-pose-front.png")]
miss_c = [DISPLAY[c] for c in BD if not has(c, "card.png")]
A("**The three concrete wins from mirroring this Drive:**\n")
A("1. **T-poses for %s.** The repo has a flat `t-pose-front.png` for only 4 of 9;" % ", ".join(miss_t))
A("   Drive has layered T-pose PSDs for all 9. These are the character scaling reference,")
A("   and the reason `family.ai` matters too.")
A("2. **37 pose variants that exist in this repo in no form at all.** Today a brief needing")
A("   a character in anything but the hero pose has to be refused under CLAUDE.md §5.")
A("   After mirroring there are 4–5 approved poses per character to composite from.")
A("3. **Character cards for %s**, completing the Surprise Card set." % ", ".join(miss_c))
A("")
A("---\n")
A("## 4. Full file index\n")
for g in ["root", "chars", "facial", "rgb", "cmyk"]:
    A("### %s\n" % GN[g])
    A("*%d files · %s*\n" % (by[g], mb(byz[g])))
    A("| File | Character | Size | Drive ID |")
    A("|---|---|---|---|")
    for r in sorted([x for x in rows if x['group'] == g], key=lambda x: ((x['char'] or ''), x['title'])):
        A("| `%s` | %s | %s | `%s` |" % (r['title'], DISPLAY.get(r['char'], '—'), mb(r['size']), r['id']))
    A("")
A("---\n")
A("## 5. Transfer — why this is an index and not a mirror\n")
A("Four routes were tested on 24 Aug 2026:\n")
A("| Route | Result |")
A("|---|---|")
A("| Anonymous `curl` on the file IDs | **Blocked.** Redirects to Google sign-in — the folder is shared to named accounts, not link-public. |")
A("| Google Drive for Desktop | **Not installed.** Only `C:` and `D:` are mounted. |")
A("| Claude in Chrome (authenticated session) | **No browser connected** to this account. |")
A("| Drive connector `download_file_content` | **Works, but returns base64 through the conversation** — roughly 0.7M tokens per MB round-trip. Fine for a few hundred KB, impossible for 2.7 GB. |")
A("")
A("### To mirror the bulk, pick one\n")
A("**A. Install Google Drive for Desktop** — chosen 24 Aug 2026. Also handles Jeremy's future")
A("updates without another round of this.\n")
A("```")
A("winget install --id Google.GoogleDrive -e")
A("```\n")
A("Sign in as jawat@waffleup.global, then in Drive on the web: *Shared with me* →")
A("**WaffleUp_ jeremy** → right-click → *Organise* → *Add shortcut to Drive* → *My Drive*.")
A("It mounts at `G:\\My Drive\\WaffleUp_ jeremy` (drive letter may differ). Then:\n")
A("```")
A("python assets/characters/_source/import.py \"G:/My Drive/WaffleUp_ jeremy\" --dry-run")
A("python assets/characters/_source/import.py \"G:/My Drive/WaffleUp_ jeremy\"")
A("```\n")
A("`import.py` matches on basename (so Drive's local folder layout does not matter), renames")
A("everything to brand names on the way in, and is safe to re-run — files already present at")
A("the right size are skipped. It pulls **72 files / 470 MB** and skips the CMYK print set;")
A("add `--cmyk` only when a printer actually needs it.\n")
A("**B. Download from the Drive web UI.** Right-click the folder → *Download*. Drive will zip it")
A("(expect several parts at this size). Unzip anywhere and point me at the path.\n")
A("Either way, this is the layout `import.py` writes — brand names, not Jeremy's:\n")
A("```")
A("assets/characters/_source/")
A("|-- MANIFEST.md         this file")
A("|-- manifest.json       machine-readable index (source of truth for import.py)")
A("|-- import.py           the importer")
A("|-- vector-masters/     10 .ai  - air-maxi.ai ... tvy.ai, family.ai")
A("|-- merlulu/            merlulu.ai + merlulu.psd (SG only)")
A("|-- t-poses/             9 .psd - <char>-t-pose.psd, the scaling reference")
A("|-- expressions/         9 .psd - <char>-expressions.psd")
A("|-- poses-rgb/<char>/   37 .psd - <char>-001.psd ... screen-ready pose variants")
A("|-- poses-cmyk/<char>/  37 .psd - print separations, gitignored, --cmyk only")
A("|-- typography/         type.ai, type-flat.ai")
A("|-- apparel/            wu-group-tee-redux.ai")
A("`-- reference/          expressions-sheet.jpg, waffle-revolution.jpg")
A("```\n")
A("### Size warning before any of this lands in git\n")
A("The full set is **%s**. The CMYK folder alone is **%s** — print separations that only a" % (mb(tot), mb(byz['cmyk'])))
A("printer needs. Recommended split:\n")
A("- **Track in git directly:** vector masters, typography, reference JPGs — about 9 MB.")
A("- **Track in git-lfs:** all layered PSDs (T-poses, Merlulu, expression sheets, RGB poses) — about %s." % mb(byz["chars"] + byz["facial"] + byz["rgb"]))
A("- **Do not commit:** `poses-cmyk/` — send it to the printer from Drive directly.\n")
A("`git-lfs 3.7.1` is installed and `.gitattributes` already routes one PDF through it.\n")
A("---\n")
A("## 6. Open questions for Jawat\n")
A("1. **`type.ai` / `type flat.ai`** (2.1 MB combined) — outlined type, almost certainly where the")
A("   Japanese WaffleUp wordmark lives. Nothing Japanese is text-indexed in Drive because it is")
A("   outlined artwork, so it cannot be read without the file itself.")
A("2. **`family.ai`** (2.0 MB) — the group lineup, and the only place the **character scaling and")
A("   height relationships** are defined. The repo currently has a flat `lineup.png` only.")
A("3. **`waffle revolution copy.jpg`** (1.0 MB, Aug 2024) — campaign artwork with no other context")
A("   anywhere in this repo. What was it for, and is it still live?")
A("4. **`WU group tee redux.ai`** (2.3 MB) — merch artwork. There is no apparel section in this")
A("   repo yet; if tees are an ongoing line it needs one.")
A("5. **Merlulu's missing poses** — confirm whether Singapore content is expected to run on a")
A("   single pose, or whether more artwork is coming.")

open('MANIFEST.md', 'w', encoding='utf-8').write("\n".join(L) + "\n")
print("%d files, %s" % (len(rows), mb(tot)))
for g in ["root", "chars", "facial", "rgb", "cmyk"]:
    print("  %-6s %3d  %s" % (g, by[g], mb(byz[g])))
print("unmapped:", [r['title'] for r in rows if not r['char']])
