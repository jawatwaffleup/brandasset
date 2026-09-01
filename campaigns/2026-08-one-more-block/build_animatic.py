# -*- coding: utf-8 -*-
"""Build the One More Block animatic — 1080x1920, 30fps, 20s.

The composite route from programs/AI-PRODUCTION.md 6: approved pose PNGs over
brand-colour fields, motion from moving the layer. No generated characters.
Cut to the ElevenLabs voice master.
"""
import math, os, subprocess, sys
import imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import grade

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
IMG = os.path.join(ROOT, "brand-guidelines", "img")
FONTS = os.path.join(ROOT, "assets", "fonts", "web")
OUT = os.path.join(ROOT, "output", "2026-09-one-more-block")
FRAMES = os.path.join(OUT, "frames")

W, H, FPS, DUR = 1080, 1920, 30, 20.0
CYAN, PINK, GOLD, COCOA, CREAM = (11, 249, 246), (255, 98, 155), (255, 213, 109), (69, 0, 1), (255, 248, 236)

# shot: (in, out, pose, plate, move, bob px, bob hz, caption)
SHOTS = [
    (0.00,  2.35, "pose-air-maxi-main",  "street", "in",    14, 2.0, "One more block. Come on — it's still open."),
    (2.35,  6.00, "pose-bhoppu-1",       "street", "right", 20, 1.2, "One more block? You said that four blocks ago."),
    (6.00,  9.40, "pose-air-maxi-4",     "street", "in",    12, 2.4, "And you're still going. That's the whole point."),
    (9.40, 15.10, "pose-bhoppu-main",    "street", "left",  18, 1.3, "There's a waffle at the end. Different reason. Same direction."),
    (15.10, 17.90, "pose-mr-waffle-main", "outlet", "hold",  0, 0.0, "You're both here. It worked."),
    (17.90, 20.00, None,                  "card",   "in",    0, 0.0, "Stay crispy."),
]

STREET_SRC = "D:/Waffleup Download/images.jpg"
OUTLET_SRC = "D:/Waffleup Download/MG_9939-1024x683.jpg"
OVER = 1.22                                   # oversize so the camera has room to move
PW, PH = int(W * OVER), int(H * OVER)

print("grading plates ...")
PLATES = {
    "street": grade.grain(grade.street(STREET_SRC, (PW, PH)), 7),
    "outlet": grade.grain(grade.outlet(OUTLET_SRC, (PW, PH)), 5),
}


def plate_window(name, move, k):
    """Crop a moving 1080x1920 window out of the oversized graded plate."""
    if name == "card":
        return Image.new("RGB", (W, H), PINK)
    src = PLATES[name]
    if move == "in":
        z = 1.0 + 0.16 * (1.0 - k)            # settle inward across the shot
    else:
        z = 1.10
    vw, vh = int(W * z), int(H * z)
    vw, vh = min(vw, src.width), min(vh, src.height)
    slack_x, slack_y = src.width - vw, src.height - vh
    fx = 0.5
    if move == "right":
        fx = 0.30 + 0.40 * k
    elif move == "left":
        fx = 0.70 - 0.40 * k
    x = int(slack_x * fx)
    y = int(slack_y * 0.55)
    win = src.crop((x, y, x + vw, y + vh))
    return win.resize((W, H), Image.LANCZOS)


font_cap = ImageFont.truetype(os.path.join(FONTS, "FuturaExtraBold.otf"), 46)
poses = {s[2]: Image.open(os.path.join(IMG, s[2] + ".png")).convert("RGBA")
         for s in SHOTS if s[2]}
logo = Image.open(os.path.join(ROOT, "assets", "logo", "Waffle Up Logo - RBG.png")).convert("RGBA")
logo.thumbnail((940, 940), Image.LANCZOS)


def wave_band(draw, y, colour, phase, amp=46, thick=300):
    """A signature-wave band across the frame, scrolled by phase."""
    pts = []
    for x in range(-40, W + 41, 20):
        pts.append((x, y + math.sin((x / 300.0) + phase) * amp))
    pts += [(W + 40, y + thick), (-40, y + thick)]
    draw.polygon(pts, fill=colour)


def shadow_of(im, w):
    """Flat cocoa shadow ellipse sized to the character."""
    s = Image.new("RGBA", (w, max(18, w // 5)), (0, 0, 0, 0))
    ImageDraw.Draw(s).ellipse([0, 0, w - 1, s.height - 1], fill=COCOA + (90,))
    return s.filter(__import__("PIL.ImageFilter", fromlist=["ImageFilter"]).GaussianBlur(10))


def caption(base, text):
    """Futura caps on a cream plate, bottom-aligned above the 400px safe margin."""
    d = ImageDraw.Draw(base)
    words, lines, cur = text.upper().split(), [], ""
    for wd in words:
        t = (cur + " " + wd).strip()
        if d.textlength(t, font=font_cap) > W - 260 and cur:
            lines.append(cur); cur = wd
        else:
            cur = t
    lines.append(cur)

    lh, pad = 60, 26
    box_h = len(lines) * lh + pad * 2
    bottom = H - 430
    top = bottom - box_h
    widest = max(d.textlength(ln, font=font_cap) for ln in lines)
    bw = widest + pad * 3
    x0 = (W - bw) / 2

    plate = Image.new("RGBA", (int(bw) + 14, box_h + 14), (0, 0, 0, 0))
    pd = ImageDraw.Draw(plate)
    pd.rounded_rectangle([7, 12, int(bw) + 6, box_h + 11], radius=26, fill=COCOA + (255,))
    pd.rounded_rectangle([7, 7, int(bw) + 6, box_h + 6], radius=26,
                         fill=CREAM + (255,), outline=COCOA + (255,), width=6)
    base.alpha_composite(plate, (int(x0) - 7, int(top) - 7))

    y = top + pad
    for ln in lines:
        tw = d.textlength(ln, font=font_cap)
        d.text(((W - tw) / 2, y), ln, font=font_cap, fill=COCOA + (255,))
        y += lh


def frame(n):
    t = n / float(FPS)
    sh = next(s for s in SHOTS if s[0] <= t < s[1]) if t < SHOTS[-1][1] else SHOTS[-1]
    t0, t1, pose, plate, move, bob, hz, cap = sh
    k = (t - t0) / max(0.001, (t1 - t0))

    base = plate_window(plate, move, k).convert("RGBA")

    if pose:
        art = poses[pose]
        target_h = int(H * 0.46)
        scale = target_h / art.height
        scale *= 1.0 + 0.05 * k
        a = art.resize((max(1, int(art.width * scale)), max(1, int(art.height * scale))), Image.LANCZOS)
        dy = int(math.sin(t * hz * 2 * math.pi) * bob) if bob else int(math.sin(t * 1.1) * 5)
        ground = int(H * 0.715)
        cx, cy = W // 2, ground - a.height // 2 + dy
        sd = shadow_of(a, int(a.width * 0.78))
        base.alpha_composite(sd, (cx - sd.width // 2, ground - sd.height // 2 + 10))
        base.alpha_composite(a, (cx - a.width // 2, cy - a.height // 2))
    elif plate == "card":
        lg = logo.copy()
        z = 1.0 + 0.05 * k
        lg = lg.resize((int(lg.width * z), int(lg.height * z)), Image.LANCZOS)
        base.alpha_composite(lg, ((W - lg.width) // 2, int(H * 0.42) - lg.height // 2))

    # vignette beds the flat artwork into the photograph
    vg = Image.new("L", (W, H), 0)
    ImageDraw.Draw(vg).ellipse([-int(W * 0.34), -int(H * 0.16),
                               int(W * 1.34), int(H * 1.16)], fill=255)
    vg = vg.filter(__import__("PIL.ImageFilter", fromlist=["ImageFilter"]).GaussianBlur(160))
    dark = Image.new("RGBA", (W, H), COCOA + (150,))
    base = Image.composite(base, Image.alpha_composite(base, dark), vg)

    caption(base, cap)
    return base.convert("RGB")


def main():
    os.makedirs(FRAMES, exist_ok=True)
    total = int(DUR * FPS)
    for n in range(total):
        frame(n).save(os.path.join(FRAMES, "f%04d.jpg" % n), quality=92)
        if n % 60 == 0:
            sys.stdout.write("  %d/%d\n" % (n, total)); sys.stdout.flush()

    exe = imageio_ffmpeg.get_ffmpeg_exe()
    out = os.path.join(OUT, "one-more-block-animatic.mp4")
    cmd = [exe, "-y", "-framerate", str(FPS), "-i", os.path.join(FRAMES, "f%04d.jpg"),
           "-i", os.path.join(OUT, "voice-master.mp3"),
           "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "21",
           "-c:a", "aac", "-b:a", "192k", "-shortest", out]
    r = subprocess.run(cmd, capture_output=True, text=True)
    print("encode:", "ok" if r.returncode == 0 else r.stderr[-700:])
    print(out, "%.1f MB" % (os.path.getsize(out) / 1e6) if os.path.exists(out) else "MISSING")


if __name__ == "__main__":
    main()
