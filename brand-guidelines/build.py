#!/usr/bin/env python
"""Build the WaffleUp Brand Guidelines PDF.

Prepares print-weight copies of the library artwork into `img/`, inlines the
licensed fonts into `fonts.css`, then renders `index.html` to PDF with headless
Chrome at 1440 x 810 px (16:9), matching the format of the previous brand book.

    python brand-guidelines/build.py            # images + fonts + PDF
    python brand-guidelines/build.py --no-pdf   # assets only

Requires: pillow, numpy, scipy, and Google Chrome.
"""

import base64
import os
import shutil
import subprocess
import sys
import tempfile

import numpy as np
from PIL import Image
from scipy import ndimage

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
IMG = os.path.join(HERE, "img")
PDF_OUT = os.path.join(ROOT, "WaffleUp Brand Guidelines.pdf")

CHROME_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "/usr/bin/google-chrome",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
]


def src(*parts):
    return os.path.join(ROOT, *parts)


def save(im, name, quality=84):
    """Write an image to img/, choosing PNG for transparency and JPEG for photos."""
    path = os.path.join(IMG, name)
    if im.mode == "RGBA":
        im.save(path, "PNG", optimize=True)
    else:
        im.convert("RGB").save(path, "JPEG", quality=quality, optimize=True, progressive=True)
    return path


def photo(source, name, size, crop=None, quality=84):
    im = Image.open(src(source))
    if im.mode == "CMYK":
        im = im.convert("RGB")
    im = im.convert("RGB")
    if crop:
        im = im.crop(crop)
    im.thumbnail((size, size), Image.LANCZOS)
    save(im, name + ".jpg", quality)


def trim(source, name, size):
    """Trim transparent margins and keep the alpha channel."""
    im = Image.open(src(source)).convert("RGBA")
    box = im.getbbox()
    if box:
        im = im.crop(box)
    im.thumbnail((size, size), Image.LANCZOS)
    save(im, name + ".png")


def scan(source, name, size, quality=86):
    """Crop a scanned reference sheet down to the drawing.

    The sheets are ruled paper, so a plain white-margin trim keeps the whole
    page — every column crosses the same ruling. Score columns and rows by ink
    density instead and keep only the band the linework actually occupies.
    """
    im = Image.open(src(source)).convert("RGB")
    a = np.asarray(im)
    ink = a.min(axis=2) < 150
    cols = ink.sum(axis=0).astype(float)
    rows = ink.sum(axis=1).astype(float)
    xs = np.where(cols > cols.max() * 0.10)[0]
    ys = np.where(rows > rows.max() * 0.10)[0]
    if len(xs) and len(ys):
        pad = int(min(im.size) * 0.02)
        im = im.crop((max(0, xs.min() - pad), max(0, ys.min() - pad),
                      min(im.width, xs.max() + pad), min(im.height, ys.max() + pad)))
    im.thumbnail((size, size), Image.LANCZOS)
    save(im, name + ".jpg", quality)


def cutout(source, name, size, thresh=243, work=1100):
    """Knock the white studio background off flat character artwork.

    Flood-fills white from the page edge, then drops the flat colour-swatch
    squares that sit beside several of the master drawings.
    """
    im = Image.open(src(source)).convert("RGB")
    im.thumbnail((work, work), Image.LANCZOS)
    a = np.asarray(im)

    nearwhite = (a >= thresh).all(axis=2)
    lab, _ = ndimage.label(nearwhite)
    edge = np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))
    ink = ~np.isin(lab, edge[edge != 0])

    parts, count = ndimage.label(ink)
    sizes = np.array(ndimage.sum(ink, parts, range(1, count + 1)))
    boxes = ndimage.find_objects(parts)
    biggest = sizes.max()

    keep = []
    for i, box in enumerate(boxes):
        if sizes[i] < biggest * 0.02:
            continue
        mask = parts[box] == i + 1
        px = a[box][mask]
        bins = (px // 48).astype(np.int32)
        _, counts = np.unique(bins[:, 0] * 10000 + bins[:, 1] * 100 + bins[:, 2], return_counts=True)
        h = box[0].stop - box[0].start
        w = box[1].stop - box[1].start
        flat = counts.max() / len(px) >= 0.9 and sizes[i] / float(h * w) >= 0.9
        if flat and sizes[i] < biggest * 0.7:
            continue  # colour-spec swatch, not artwork
        keep.append(i + 1)

    mask = np.isin(parts, keep)
    ys, xs = np.where(mask)
    out = np.dstack([a, (mask * 255).astype(np.uint8)])
    out = out[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
    im = Image.fromarray(out, "RGBA")
    im.thumbnail((size, size), Image.LANCZOS)
    save(im, name + ".png")


def pose(source, name, size=900, work=1400, tol=26):
    """Lift a character pose off its baked backdrop.

    The Aug 2026 pose sheets ship as A4 canvases with a flat white or grey
    field, a reference thumbnail pinned to the top-left corner, and (on the
    main poses) a four-square colour key. Flood-fill the field from the edge,
    then drop the thumbnail and the key so only the artwork survives.
    """
    im = Image.open(src(source)).convert("RGBA")
    im.thumbnail((work, work), Image.LANCZOS)
    a = np.asarray(im)
    rgb = a[:, :, :3].astype(np.int16)

    bg = a[:, :, 3] < 16
    # Seed from the dominant colours of the 1px border ring rather than the corner
    # pixels — one sheet has artwork running into a corner, which ate the drawing.
    ring = np.concatenate([a[0, :, :3], a[-1, :, :3], a[:, 0, :3], a[:, -1, :3]])
    keys, counts = np.unique(ring.astype(np.int32) @ np.array([65536, 256, 1]), return_counts=True)
    for key in keys[counts.argsort()[::-1][:2]]:
        if counts[list(keys).index(key)] < len(ring) * 0.05:
            continue
        colour = np.array([key >> 16, (key >> 8) & 255, key & 255], np.int16)
        bg |= np.abs(rgb - colour).sum(axis=2) < tol

    lab, _ = ndimage.label(bg)
    edge = np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))
    ink = ~np.isin(lab, edge[edge != 0])

    parts, count = ndimage.label(ink)
    sizes = np.array(ndimage.sum(ink, parts, range(1, count + 1)))
    boxes = ndimage.find_objects(parts)
    height, width = ink.shape
    biggest = sizes.max()

    keep = []
    for i, box in enumerate(boxes):
        if sizes[i] < biggest * 0.004:
            continue
        h = box[0].stop - box[0].start
        w = box[1].stop - box[1].start
        fill = sizes[i] / float(h * w)
        px = a[box][:, :, :3][parts[box] == i + 1]
        # Reference thumbnail, pinned to the top-left corner. On a grey sheet it
        # survives as a white card; on a white sheet the card itself flood-fills
        # away and only the miniature drawing inside it is left behind.
        white = ((px >= 232).all(axis=1)).mean()
        card = (box[0].start < height * 0.06 and box[1].start < width * 0.06
                and white > 0.20 and sizes[i] < biggest * 0.70)
        residue = (box[0].start < height * 0.06 and box[1].start < width * 0.12
                   and sizes[i] < biggest * 0.25)
        if card or residue:
            continue
        bins = (px // 48).astype(np.int32)
        _, counts = np.unique(bins[:, 0] * 10000 + bins[:, 1] * 100 + bins[:, 2], return_counts=True)
        if counts.max() / len(px) >= 0.9 and fill >= 0.85 and sizes[i] < biggest * 0.7:
            continue  # colour-key square, not artwork
        keep.append(i + 1)

    mask = np.isin(parts, keep)
    ys, xs = np.where(mask)
    out = np.dstack([a[:, :, :3], (mask * 255).astype(np.uint8)])
    out = out[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
    im = Image.fromarray(out, "RGBA")
    im.thumbnail((size, size), Image.LANCZOS)
    save(im, name + ".png")


# --------------------------------------------------------------------------
# Manifest
# --------------------------------------------------------------------------

BD = "assets/characters/bangladesh"

CHARACTERS = ["mr-waffle", "air-maxi", "bhoppu", "picchi", "stovy", "swirly", "tvy", "spacy", "icy"]
T_POSES = ["air-maxi", "bhoppu", "picchi", "swirly"]
MODELS_3D = {"mr-waffle": "3d/model-reference.jpg", "air-maxi": "3d/model-reference.jpg",
             "picchi": "3d/model-reference.jpg", "bhoppu": "2d/hero.png"}

WORDMARKS = ["Ashol", "Crispy", "Crunch", "Drizzle", "Everyday", "Halal-1", "Halal-2", "Love",
             "Obsessed", "Order Now", "Smile", "Square", "Sweet", "Waffle Love", "Waffleistic"]

# Merlulu is omitted — the printed card carries the superseded design.
SURPRISE_CARDS = ["Mr Waffle", "Air Maxi", "Bhoppu", "Picchi", "Stovy", "Swirly", "Tvy", "Spacy",
                  "Icy"]

PRODUCTS = ["01-woas-nutella", "02-woas-red-velvet", "03-woas-tri-chocolate", "04-woas-mad-mango",
            "05-woas-kunaffle", "06-death-by-nutella", "07-bananatella-and-nuts",
            "08-strawberry-banana-and-nutella", "09-very-very-strawberry", "10-fruity-bliss",
            "11-bangla-pizza", "choco-choco-cheese", "delivery-platform---cheese-drink",
            "hot-chocolate-new", "mango-drink"]

PACKAGING = ["BD BOX A.jpg", "BD BOX B.jpg", "BD BOX C.jpg", "BD Tray - Event.jpg",
             "BD Tray - Outlet.jpg", "Round Cup Design.png", "Round Cup Mockup.png",
             "SG Bag 25x14x30.jpg"]

EVENTS = ["WUP Event Backdrop 10ft x 8ft.png", "WUP Event Backdrop 8ft x 8ft.png",
          "WUP Event Sidedrop-1 10ft x 8ft.png", "WUP Event Sidedrop-2 10ft x 8ft.png",
          "WUP Event Table Front (11ft x 3ft).png", "WUP Event X Banner - Cheese Drink.png",
          "WUP Event X Banner - Kunaffle (limited edition).png",
          "WUP Event X Banner - Kunaffle (ramadan).png", "WUP Event X Banner - Nutella.png",
          "WUP Event X Banner - Trichocolate.png"]

EXTRAS = ["Mr Waffle-01.png", "Mr Waffle-02.png", "Spacy-02.png", "Stovy-02.png", "Tvy-01.png",
          "Scratch Card - Ice Cream.png"]

# The Aug 2026 pose batch (Sadbin Ahmed) — `Character poses/`. Folder spellings differ
# from the approved public names, so map them here rather than renaming the source.
POSE_DIR = "Character poses"
POSES = {
    "bhoppu":    ["Bhoppu 001", "Bhoppu 002", "Bhoppu 003", "Bhoppu 004"],
    "air-maxi":  ["Air maxi 001", "Air maxi 002", "Air maxi 003", "Air maxi 004"],
    "mr-waffle": ["Mr Waffle 001", "Mr Waffle 002", "Mr Waffle 003", "Mr Waffle 004", "Mr Waffle 005"],
    "picchi":    ["picchi 001", "picchi 002", "picchi 003", "picchi 004"],
    "swirly":    ["Swirly 001", "Swirly 002", "Swirly 003", "Swirly 004"],
    "merlulu":   ["Merlulu 001", "Merlulu 002", "Merlulu 003", "Merlulu 004"],
    "tvy":       ["TV 001", "TV 002", "TV 003", "TV 004"],
    "spacy":     ["Spacie 001", "Spacie 002", "Spacie 003", "Spacie 004"],
    "stovy":     ["Stovie 001", "Stovie 002", "Stovie 003 ", "Stovie 004"],
    "icy":       ["popsicle 001", "popsicle 002", "popsicle 003", "popsicle 004"],
}
POSE_MAIN = {
    "bhoppu": "Bhoopu Main Pose", "air-maxi": "Air maxi final", "mr-waffle": "mr waffle final",
    "picchi": "picchi final", "swirly": "swirly final", "spacy": "spacie final",
    "stovy": "stovie final", "icy": "popsicle final", "tvy": "TVy final",
}
# Merlulu's main pose sits in the top-level folder, not Mains/.
POSE_MAIN_FLAT = {"merlulu": "Merlulu Main"}

FONTS = {
    "Chum": ("assets/fonts/web/Chum.ttf", "truetype"),
    "FuturaXB": ("assets/fonts/web/FuturaExtraBold.otf", "opentype"),
    "GeneralSans": ("assets/fonts/web/GeneralSans-Variable.ttf", "truetype"),
    "BebasNeue": ("assets/fonts/web/BebasNeue.otf", "opentype"),
}


def slug(name):
    return name.lower().replace(" ", "-")


def build_images():
    os.makedirs(IMG, exist_ok=True)
    log = lambda s: sys.stdout.write(s + "\n") or sys.stdout.flush()

    log("marks")
    trim("assets/logo/Waffle Up Logo - RBG.png", "logo-rgb", 1400)
    trim("assets/logo/Waffle Up Logo - CMYK.png", "logo-cmyk", 800)
    for key, f in [("rgb", "Icon (rbg).png"), ("social", "Icon (rbg) - Social.png"),
                   ("cmyk", "Icon (cmyk).png"), ("red", "Icon (red).png"),
                   ("white", "Icon (white).png")]:
        trim("assets/icon/" + f, "icon-" + key, 520)
    for key, f in [("rgb", "Symbol (rbg).png"), ("cmyk", "Symbol (cmyk).png"),
                   ("button", "Brand-Icon--button.png")]:
        trim("assets/symbol/" + f, "symbol-" + key, 520)

    log("colour + pattern")
    for key, f in [("rgb", "Color Code - RGB.png"), ("cmyk", "Color Code - CMYK.png"),
                   ("pantone", "Color Code - Pantone.png")]:
        photo("assets/" + f, "color-" + key, 620)
    photo("assets/pattern/Brand-Pattern.jpg", "pattern", 2200, quality=88)

    log("typography")
    for name in WORDMARKS:
        trim("assets/typography/%s (rgb).png" % name, "wm-" + slug(name), 760)

    log("characters")
    photo(BD + "/lineup.png", "lineup", 2600, quality=88)
    for name in CHARACTERS:
        cutout(BD + "/%s/2d/hero.png" % name, "char-" + name, 820)
        photo(BD + "/%s/2d/expressions.png" % name, "expr-" + name, 1000)
    for name in T_POSES:
        scan(BD + "/%s/2d/t-pose-front.png" % name, "tpose-" + name, 1300)
    for name, rel in MODELS_3D.items():
        photo(BD + "/%s/%s" % (name, rel), "model-" + name, 1100)

    log("character poses (Aug 2026 batch)")
    for key, names in POSES.items():
        for n, f in enumerate(names, 1):
            pose("%s/%s.png" % (POSE_DIR, f), "pose-%s-%d" % (key, n), 900)
    for key, f in POSE_MAIN.items():
        pose("%s/Mains/%s.png" % (POSE_DIR, f), "pose-%s-main" % key, 1000)
    for key, f in POSE_MAIN_FLAT.items():
        pose("%s/%s.png" % (POSE_DIR, f), "pose-%s-main" % key, 1000)
    photo("%s/Mains/family.png" % POSE_DIR, "gang-banner", 2600, quality=88)

    log("surprise cards")
    for name in SURPRISE_CARDS:
        trim("assets/Surprise Cards/Character Cards/Character Card - %s.png" % name,
             "sc-" + slug(name), 480)
    for f in EXTRAS:
        trim("assets/marketing/surprise-card/" + f, "extra-" + slug(os.path.splitext(f)[0]), 560)
    photo("assets/marketing/audio/YTCover.png", "ytcover", 700)

    log("products, packaging, events")
    for f in PRODUCTS:
        photo("assets/marketing/product-hero/%s.jpg" % f, "prod-" + f, 620)
    for f in PACKAGING:
        photo("assets/marketing/packaging/" + f, "pack-" + slug(os.path.splitext(f)[0]), 880)
    for f in EVENTS:
        photo("assets/marketing/event/" + f, "ev-" + slug(os.path.splitext(f)[0]), 880)

    total = sum(os.path.getsize(os.path.join(IMG, f)) for f in os.listdir(IMG))
    log("img/ = %d files, %.1f MB" % (len(os.listdir(IMG)), total / 1e6))


def build_fonts():
    faces = []
    for family, (path, fmt) in FONTS.items():
        with open(src(path), "rb") as fh:
            data = base64.b64encode(fh.read()).decode("ascii")
        mime = "font/ttf" if fmt == "truetype" else "font/otf"
        weight = "200 700" if family == "GeneralSans" else "400"
        faces.append(
            '@font-face{font-family:"%s";src:url(data:%s;base64,%s) format("%s");'
            'font-weight:%s;font-style:normal;font-display:block}' % (family, mime, data, fmt, weight)
        )
    with open(os.path.join(HERE, "fonts.css"), "w", encoding="utf-8") as fh:
        fh.write("/* Generated by build.py — licensed WaffleUp faces, inlined for print. */\n")
        fh.write("\n".join(faces))
    print("fonts.css written")


def find_chrome():
    for path in CHROME_CANDIDATES:
        if os.path.exists(path):
            return path
    found = shutil.which("chrome") or shutil.which("google-chrome")
    if found:
        return found
    raise SystemExit("Chrome not found — install it or edit CHROME_CANDIDATES.")


def build_pdf():
    chrome = find_chrome()
    profile = tempfile.mkdtemp(prefix="wup-pdf-")
    url = "file:///" + os.path.join(HERE, "index.html").replace("\\", "/").replace(" ", "%20")
    cmd = [
        chrome, "--headless", "--disable-gpu", "--no-sandbox",
        "--no-pdf-header-footer", "--allow-file-access-from-files",
        "--run-all-compositor-stages-before-draw", "--virtual-time-budget=60000",
        "--user-data-dir=" + profile,
        "--print-to-pdf=" + PDF_OUT, url,
    ]
    print("rendering PDF …")
    result = subprocess.run(cmd, capture_output=True, text=True)
    shutil.rmtree(profile, ignore_errors=True)
    if not os.path.exists(PDF_OUT):
        print(result.stdout, result.stderr)
        raise SystemExit("Chrome did not produce a PDF.")
    print("%s — %.1f MB" % (PDF_OUT, os.path.getsize(PDF_OUT) / 1e6))


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--pdf-only" not in args:
        build_images()
        build_fonts()
    if "--no-pdf" not in args:
        build_pdf()
