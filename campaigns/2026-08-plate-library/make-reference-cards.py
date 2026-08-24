# -*- coding: utf-8 -*-
"""
Palette reference cards for Krea / Seedream style-reference slots.

These exist so the palette can be locked WITHOUT putting a hex code in the
prompt (Veo printed "C5DBE4" into a frame, 23 Aug 2026) and WITHOUT uploading
any product, logo, character or packaging file as a reference.

Flat brand colour only. No text, no marks, no product, no gradient.
"""
import os
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'reference')
os.makedirs(OUT, exist_ok=True)

S = 1024

# tokens/wup-tokens.json — canonical. Ice blue is the measured house surface
# (GEMINI.md §1), not a token; it is the pale seamless in the hero shots.
CYAN   = (0x0B, 0xF9, 0xF6)
PINK   = (0xFF, 0x62, 0x9B)
GOLD   = (0xFF, 0xD5, 0x6D)
COCOA  = (0x45, 0x00, 0x01)
ICE    = (0xC5, 0xDB, 0xE4)

CARDS = {
    # dominant, secondary(large block), accent A, accent B
    'ref-palette-street-day':  (CYAN,  GOLD, PINK,  COCOA),
    'ref-palette-studio-gold': (GOLD,  ICE,  COCOA, PINK),
    'ref-palette-night':       (COCOA, CYAN, PINK,  GOLD),
}


def card(dominant, secondary, accent_a, accent_b):
    """One dominant field, one large secondary block, two small accents.
    Blocks not bands — a banded reference tends to produce a banded picture."""
    im = Image.new('RGB', (S, S), dominant)
    d = ImageDraw.Draw(im)
    # secondary ~22% of area, off-centre so it reads as palette not composition
    d.rectangle([int(S * 0.06), int(S * 0.60), int(S * 0.62), int(S * 0.94)],
                fill=secondary)
    # accents ~4% each
    d.rectangle([int(S * 0.70), int(S * 0.10), int(S * 0.94), int(S * 0.32)],
                fill=accent_a)
    d.rectangle([int(S * 0.70), int(S * 0.40), int(S * 0.94), int(S * 0.56)],
                fill=accent_b)
    return im


if __name__ == '__main__':
    for name, cols in CARDS.items():
        im = card(*cols)
        p = os.path.join(OUT, name + '.png')
        im.save(p)
        g = im.convert('L')
        px = list(g.getdata())
        mean = sum(px) / float(len(px))
        dark = 100.0 * sum(1 for v in px if v < 60) / len(px)
        print('%-26s mean luma %5.1f   dark %4.1f%%' % (name, mean, dark))
