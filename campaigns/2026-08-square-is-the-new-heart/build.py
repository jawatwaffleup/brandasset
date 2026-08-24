# -*- coding: utf-8 -*-
"""
SQUARE IS THE NEW HEART - 15s Reel builder

Renders 1080x1920 @30fps from supplied brand assets only.
No AI generation, no CapCut. Frames are rendered in PIL and piped to ffmpeg.
"""
import os, math, subprocess
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter
import imageio_ffmpeg

ROOT  = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HERO  = os.path.join(ROOT, 'assets', 'marketing', 'product-hero')
TYPO  = os.path.join(ROOT, 'assets', 'typography')
LOGO  = os.path.join(ROOT, 'assets', 'logo', 'Waffle Up Logo - RBG.png')
FONTS = os.path.join(ROOT, 'assets', 'fonts', 'web')
OUT   = os.path.join(ROOT, 'output', '2026-08-square-is-the-new-heart')
os.makedirs(OUT, exist_ok=True)

W, H, FPS = 1080, 1920, 30

# tokens/wup-tokens.json - canonical
CYAN  = (0x0B, 0xF9, 0xF6)
PINK  = (0xFF, 0x62, 0x9B)
GOLD  = (0xFF, 0xD5, 0x6D)
COCOA = (0x45, 0x00, 0x01)
WHITE = (255, 255, 255)

F_DISPLAY = os.path.join(FONTS, 'FuturaExtraBold.otf')


def ease(t):
    t = max(0.0, min(1.0, t))
    return t * t * (3 - 2 * t)


def lerp(a, b, t):
    return a + (b - a) * t


# ---------------------------------------------------------------- product
_cache = {}


def load_hero(name):
    if name not in _cache:
        im = Image.open(os.path.join(HERO, name + '.jpg')).convert('RGB')
        # unify pass only: mild saturation + contrast. Nothing structural.
        im = ImageEnhance.Color(im).enhance(1.08)
        im = ImageEnhance.Contrast(im).enhance(1.05)
        _cache[name] = im
    return _cache[name]


def window(im, s, cxf, cyf):
    """Crop a 9:16 window covering fraction s of the largest fitting box,
    centred on (cxf, cyf) as fractions of the source, resized to 1080x1920."""
    sw, sh = im.size
    bw = min(sw, sh * 9.0 / 16.0)
    bh = bw * 16.0 / 9.0
    if bh > sh:
        bh = sh
        bw = bh * 9.0 / 16.0
    w, h = bw * s, bh * s
    x = cxf * sw - w / 2.0
    y = cyf * sh - h / 2.0
    x = max(0.0, min(sw - w, x))
    y = max(0.0, min(sh - h, y))
    box = (int(round(x)), int(round(y)), int(round(x + w)), int(round(y + h)))
    return im.crop(box).resize((W, H), Image.LANCZOS)


def shot_product(sh, t):
    im = load_hero(sh['src'])
    p = ease(t / sh['dur'])
    s  = lerp(sh['s0'],  sh['s1'],  p)
    cx = lerp(sh['cx0'], sh['cx1'], p)
    cy = lerp(sh['cy0'], sh['cy1'], p)
    # the levitation bob - keeps the frozen-in-air house look alive in motion
    cy += math.sin(2 * math.pi * (t + sh.get('phase', 0.0)) * 0.85) * 0.004
    return window(im, s, cx, cy)


# ------------------------------------------------------------- typography
def fit_font(path, text, target_w, hi=400):
    lo = 10
    while lo < hi:
        mid = (lo + hi + 1) // 2
        f = ImageFont.truetype(path, mid)
        bb = f.getbbox(text)
        if bb[2] - bb[0] <= target_w:
            lo = mid
        else:
            hi = mid - 1
    return ImageFont.truetype(path, lo)


def display_text(base, text, font, cy, fill, outline, stroke=14,
                 shadow=COCOA, shadow_off=(9, 13), blur=7):
    """House four-layer treatment: drop shadow -> outline -> text."""
    d0 = ImageDraw.Draw(base)
    bb = d0.textbbox((0, 0), text, font=font, stroke_width=stroke)
    tw, th = bb[2] - bb[0], bb[3] - bb[1]
    x = (W - tw) / 2.0 - bb[0]
    y = cy - th / 2.0 - bb[1]
    sl = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(sl).text((x + shadow_off[0], y + shadow_off[1]), text, font=font,
                            fill=shadow + (255,), stroke_width=stroke,
                            stroke_fill=shadow + (255,))
    base.alpha_composite(sl.filter(ImageFilter.GaussianBlur(blur)))
    ImageDraw.Draw(base).text((x, y), text, font=font, fill=fill + (255,),
                              stroke_width=stroke, stroke_fill=outline + (255,))
    return th


def shot_card_round(sh, t):
    # gold field: the end card takes cyan, so these two do not sit on the same colour
    img = Image.new('RGBA', (W, H), GOLD + (255,))
    f = fit_font(F_DISPLAY, 'ROUND IS', int(W * 0.78))
    display_text(img, 'ROUND IS', f, H * 0.455 - f.size * 0.54, COCOA, WHITE)
    display_text(img, 'OVER.',    f, H * 0.455 + f.size * 0.54, COCOA, WHITE)
    k = lerp(1.06, 1.0, ease(min(1.0, t / 0.35)))
    if k > 1.0:
        nw, nh = int(W * k), int(H * k)
        img = img.resize((nw, nh), Image.LANCZOS).crop(
            ((nw - W) // 2, (nh - H) // 2, (nw - W) // 2 + W, (nh - H) // 2 + H))
    return img.convert('RGB')


_sq = None
_logo = None


def _fade(layer, a):
    out = layer.copy()
    alpha = out.getchannel('A').point(lambda v: int(v * a))
    out.putalpha(alpha)
    return out


def shot_endcard(sh, t):
    global _sq, _logo
    if _sq is None:
        s = Image.open(os.path.join(TYPO, 'Square (rgb).png')).convert('RGBA')
        _sq = s.crop(s.getbbox())
        l = Image.open(LOGO).convert('RGBA')
        _logo = l.crop(l.getbbox())

    # cyan field: the lockup's "HEART" is brand pink and would vanish on pink
    img = Image.new('RGBA', (W, H), CYAN + (255,))

    # 1. the tagline - supplied artwork carries the whole lockup and the
    #    four-layer treatment. Never rebuilt, never re-set in live type.
    k = ease(min(1.0, t / 0.55))
    tw = int(W * 0.88 * lerp(0.90, 1.0, k))
    sq = _sq.resize((tw, int(_sq.height * tw / _sq.width)), Image.LANCZOS)
    sq_top = int(H * 0.40) - sq.height // 2
    img.alpha_composite(sq, ((W - sq.width) // 2, sq_top))

    # 2. logo - supplied file, never rebuilt, inside the bottom safe margin
    if t > 0.85:
        a = ease(min(1.0, (t - 0.85) / 0.45))
        lw = int(W * 0.50)
        lg = _logo.resize((lw, int(_logo.height * lw / _logo.width)), Image.LANCZOS)
        lay = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        top = sq_top + sq.height + 150
        lay.alpha_composite(lg, ((W - lg.width) // 2, top))
        img.alpha_composite(_fade(lay, a))

        # 3. the handle. Not a CTA - no channel claim, so it is safe anywhere.
        if t > 1.35:
            a2 = ease(min(1.0, (t - 1.35) / 0.4))
            fh = ImageFont.truetype(os.path.join(FONTS, 'BebasNeue.otf'), 68)
            lay2 = Image.new('RGBA', (W, H), (0, 0, 0, 0))
            d = ImageDraw.Draw(lay2)
            txt = '@waffleup.online'
            bb = d.textbbox((0, 0), txt, font=fh)
            d.text(((W - (bb[2] - bb[0])) / 2 - bb[0], top + lg.height + 46),
                   txt, font=fh, fill=COCOA + (255,))
            img.alpha_composite(_fade(lay2, a2))

    return img.convert('RGB')


# -------------------------------------------------------------- the cut
SHOTS = [
    dict(kind='p', src='02-woas-red-velvet',      dur=1.9, s0=1.00, s1=0.90,
         cx0=.47, cx1=.47, cy0=.48, cy1=.48, phase=0.0),
    dict(kind='card_round',                        dur=1.1),
    dict(kind='p', src='03-woas-tri-chocolate',   dur=1.8, s0=1.00, s1=0.89,
         cx0=.50, cx1=.50, cy0=.50, cy1=.50, phase=0.3),
    dict(kind='p', src='09-very-very-strawberry', dur=1.8, s0=0.95, s1=0.95,
         cx0=.30, cx1=.63, cy0=.52, cy1=.52, phase=0.6),
    dict(kind='p', src='01-woas-nutella',         dur=1.7, s0=1.00, s1=0.90,
         cx0=.50, cx1=.50, cy0=.50, cy1=.50, phase=0.9),
    dict(kind='p', src='10-fruity-bliss',         dur=1.7, s0=0.92, s1=1.00,
         cx0=.50, cx1=.50, cy0=.50, cy1=.50, phase=1.2),
    dict(kind='p', src='11-bangla-pizza',         dur=1.7, s0=0.95, s1=0.95,
         cx0=.62, cx1=.40, cy0=.50, cy1=.50, phase=1.5),
    dict(kind='endcard',                           dur=3.3),
]

TOTAL = sum(s['dur'] for s in SHOTS)
NF = int(round(TOTAL * FPS))
print('total %.2fs  %d frames' % (TOTAL, NF))

bounds, acc = [], 0.0
for s in SHOTS:
    bounds.append((acc, acc + s['dur'], s))
    acc += s['dur']


def render(i):
    t = i / float(FPS)
    for a, b, s in bounds:
        if a <= t < b or (b >= TOTAL - 1e-9 and t >= a):
            local = t - a
            if s['kind'] == 'p':
                return shot_product(s, local)
            if s['kind'] == 'card_round':
                return shot_card_round(s, local)
            return shot_endcard(s, local)
    return shot_endcard(bounds[-1][2], bounds[-1][2]['dur'])


if __name__ == '__main__':
    ffm = imageio_ffmpeg.get_ffmpeg_exe()
    dst = os.path.join(OUT, 'square-is-the-new-heart-15s.mp4')
    proc = subprocess.Popen(
        [ffm, '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24',
         '-s', '%dx%d' % (W, H), '-r', str(FPS), '-i', '-', '-an',
         '-c:v', 'libx264', '-profile:v', 'high', '-pix_fmt', 'yuv420p',
         '-crf', '18', '-preset', 'slow', '-movflags', '+faststart', dst],
        stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    lum = []
    for i in range(NF):
        fr = render(i)
        if i % 15 == 0:
            g = fr.convert('L')
            lum.append(sum(g.getdata()) / float(W * H))
        proc.stdin.write(fr.tobytes())
    proc.stdin.close()
    proc.wait()

    print('wrote', dst)
    print('mean luminance, sampled: %.1f  (house band 184-208)' % (sum(lum) / len(lum)))
