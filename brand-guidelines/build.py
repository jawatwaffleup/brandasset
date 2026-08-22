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


def cutout_field(source, name, size, crop, seeds, tol=100):
    """Lift flat artwork off a coloured field — used for the Merlulu sticker.

    Flood-fills the named background colours from the crop edge, then keeps the
    largest remaining blob and fills it, so the sticker's white keyline survives.
    """
    im = Image.open(src(source)).convert("RGB").crop(crop)
    a = np.asarray(im).astype(np.int16)
    bg = np.zeros(a.shape[:2], bool)
    for colour in seeds:
        bg |= np.abs(a - np.array(colour, np.int16).reshape(1, 1, 3)).sum(axis=2) < tol
    lab, _ = ndimage.label(bg)
    edge = np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))
    ink = ~np.isin(lab, edge[edge != 0])
    parts, count = ndimage.label(ink)
    sizes = np.array(ndimage.sum(ink, parts, range(1, count + 1)))
    mask = ndimage.binary_fill_holes(parts == int(sizes.argmax()) + 1)
    ys, xs = np.where(mask)
    out = np.dstack([np.asarray(im), (mask * 255).astype(np.uint8)])
    out = out[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
    im = Image.fromarray(out, "RGBA")
    im.thumbnail((size, size), Image.LANCZOS)
    save(im, name + ".png")


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


# --------------------------------------------------------------------------
# Manifest
# --------------------------------------------------------------------------

BD = "assets/characters/bangladesh"

CHARACTERS = ["mr-waffle", "air-maxi", "bhoppu", "picchi", "stovy", "swirly", "tvy", "spacy", "icy"]
CARD_ART = ["mr-waffle", "air-maxi", "bhoppu", "picchi", "stovy", "swirly"]
T_POSES = ["air-maxi", "bhoppu", "picchi", "swirly"]
MODELS_3D = {"mr-waffle": "3d/model-reference.jpg", "air-maxi": "3d/model-reference.jpg",
             "picchi": "3d/model-reference.jpg", "bhoppu": "2d/hero.png"}

WORDMARKS = ["Ashol", "Crispy", "Crunch", "Drizzle", "Everyday", "Halal-1", "Halal-2", "Love",
             "Obsessed", "Order Now", "Smile", "Square", "Sweet", "Waffle Love", "Waffleistic"]

SURPRISE_CARDS = ["Mr Waffle", "Air Maxi", "Bhoppu", "Picchi", "Stovy", "Swirly", "Tvy", "Spacy",
                  "Icy", "Merlulu"]

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
    for name in CARD_ART:
        trim(BD + "/%s/2d/card.png" % name, "cardart-" + name, 620)
    for name in T_POSES:
        photo(BD + "/%s/2d/t-pose-front.png" % name, "tpose-" + name, 900)
    for name, rel in MODELS_3D.items():
        photo(BD + "/%s/%s" % (name, rel), "model-" + name, 1100)
    cutout_field("assets/characters/singapore/merlulu/references/sg-sticker-sheet-full.jpg",
                 "char-merlulu", 820, crop=(10, 1310, 780, 2230),
                 seeds=[(241, 99, 155), (110, 204, 216), (247, 177, 205), (166, 224, 231)])
    photo("assets/characters/singapore/merlulu/references/sg-sticker-sheet-full.jpg",
          "sg-sheet", 1500, quality=86)

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
