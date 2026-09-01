# -*- coding: utf-8 -*-
"""Grade the two location photographs onto the WaffleUp palette.

Both plates arrive off-brand: the street is cool, dark and desaturated; the
outlet is bathed in a violet magenta that is hotter and bluer than WaffleUp
pink. A tritone gradient map pulls each onto the brand triad — deep cocoa in
the shadows, electric cyan through the mids, warm honey gold in the highlights
— then blends back toward the original so the photograph survives.
"""
import numpy as np
from PIL import Image, ImageFilter, ImageEnhance

CYAN = (11, 249, 246)
PINK = (255, 98, 155)
GOLD = (255, 213, 109)
COCOA = (69, 0, 1)


def gradient_map(im, stops, blend=0.75, contrast=1.15, sat=1.25):
    """Map luminance through colour stops, then blend back over the original."""
    src = im.convert("RGB")
    src = ImageEnhance.Contrast(src).enhance(contrast)
    a = np.asarray(src).astype(np.float32) / 255.0
    lum = (a[:, :, 0] * 0.2126 + a[:, :, 1] * 0.7152 + a[:, :, 2] * 0.0722)

    pos = np.array([s[0] for s in stops], np.float32)
    cols = np.array([s[1] for s in stops], np.float32) / 255.0
    mapped = np.stack([np.interp(lum, pos, cols[:, c]) for c in range(3)], axis=2)

    out = mapped * blend + a * (1.0 - blend)
    out = np.clip(out, 0, 1)
    res = Image.fromarray((out * 255).astype(np.uint8), "RGB")
    return ImageEnhance.Color(res).enhance(sat)


def street(path, size, blur=2.2):
    """Night street: cocoa shadows, cyan air, gold lamplight."""
    im = Image.open(path).convert("RGB")
    w, h = im.size
    cw = int(h * 9 / 16)
    x0 = int(w * 0.50) - cw // 2
    im = im.crop((max(0, x0), 0, max(0, x0) + cw, h))
    im = im.resize(size, Image.LANCZOS)
    im = im.filter(ImageFilter.GaussianBlur(blur))       # reads as depth of field
    im = gradient_map(im, [
        (0.00, COCOA),
        (0.09, (34, 22, 40)),
        (0.28, (16, 74, 96)),
        (0.52, (18, 165, 180)),
        (0.74, CYAN),
        (0.90, GOLD),
        (1.00, (255, 252, 240)),
    ], blend=0.66, contrast=1.26, sat=1.24)
    return im


def outlet(path, size, blur=1.0):
    """The shopfront: violet magenta pulled back to WaffleUp pink."""
    im = Image.open(path).convert("RGB")
    w, h = im.size
    cw = int(h * 9 / 16)
    x0 = int(w * 0.39) - cw // 2                          # keeps the sign, drops the watermark
    im = im.crop((max(0, x0), 0, max(0, x0) + cw, h))
    im = im.resize(size, Image.LANCZOS)
    im = im.filter(ImageFilter.GaussianBlur(blur))
    im = gradient_map(im, [
        (0.00, COCOA),
        (0.20, (92, 14, 60)),
        (0.45, PINK),
        (0.70, (255, 150, 190)),
        (0.86, GOLD),
        (1.00, (255, 253, 245)),
    ], blend=0.62, contrast=1.12, sat=1.22)
    return im


def grain(im, amount=7):
    a = np.asarray(im).astype(np.int16)
    n = np.random.default_rng(7).normal(0, amount, a.shape[:2])[:, :, None]
    return Image.fromarray(np.clip(a + n, 0, 255).astype(np.uint8), "RGB")
