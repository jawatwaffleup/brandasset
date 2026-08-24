# -*- coding: utf-8 -*-
"""
Plate acceptance test.

Measures a downloaded plate against the house exposure signature sampled from
assets/marketing/product-hero/ on 23 Aug 2026 (GEMINI.md §1). Both failed Veo
plates in output/2026-08-drop-test/ were caught by exactly these two numbers.

    python campaigns/2026-08-plate-library/check-plate.py <file> [<file> ...]

Accepts stills and video. Video is sampled at five points across its duration.
"""
import os
import subprocess
import sys
import tempfile

from PIL import Image
import imageio_ffmpeg

MEAN_LO, MEAN_HI = 184, 208   # house band
DARK_MAX = 5.0                # % of pixels under 60 luma

VIDEO_EXT = {'.mp4', '.mov', '.webm', '.mkv', '.m4v'}


def measure(im):
    im = im.convert('RGB')
    g = im.convert('L')
    px = list(g.getdata())
    n = float(len(px))
    mean = sum(px) / n
    dark = 100.0 * sum(1 for v in px if v < 60) / n
    # dominant colour, coarsely quantised, as a palette sanity check
    q = im.resize((64, 64), Image.LANCZOS).quantize(colors=5, method=Image.MEDIANCUT)
    pal = q.getpalette()
    top = sorted(q.getcolors(), reverse=True)[:3]
    doms = ['#%02X%02X%02X' % tuple(pal[i * 3:i * 3 + 3]) for _, i in top]
    return mean, dark, doms


def frames(path):
    ext = os.path.splitext(path)[1].lower()
    if ext not in VIDEO_EXT:
        yield Image.open(path)
        return
    ffm = imageio_ffmpeg.get_ffmpeg_exe()
    out = subprocess.run([ffm, '-i', path], capture_output=True, text=True).stderr
    dur = 5.0
    for line in out.splitlines():
        if 'Duration:' in line:
            hms = line.split('Duration:')[1].split(',')[0].strip()
            h, m, s = hms.split(':')
            dur = int(h) * 3600 + int(m) * 60 + float(s)
            break
    tmp = tempfile.mkdtemp()
    for i in range(5):
        t = dur * (i + 0.5) / 5.0
        p = os.path.join(tmp, 'f%d.png' % i)
        subprocess.run([ffm, '-y', '-ss', str(t), '-i', path, '-frames:v', '1', p],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if os.path.exists(p):
            yield Image.open(p)


def check(path):
    ms, ds, doms = [], [], []
    for im in frames(path):
        m, d, dm = measure(im)
        ms.append(m); ds.append(d); doms = dm
    if not ms:
        print('%s  COULD NOT READ' % path)
        return
    mean = sum(ms) / len(ms)
    dark = sum(ds) / len(ds)
    ok_m = MEAN_LO <= mean <= MEAN_HI
    ok_d = dark <= DARK_MAX
    verdict = 'PASS' if (ok_m and ok_d) else 'REJECT'
    print('\n%s  ->  %s' % (os.path.basename(path), verdict))
    print('  mean luminance  %6.1f   target %d-%d   %s'
          % (mean, MEAN_LO, MEAN_HI, 'ok' if ok_m else
             ('TOO DIM' if mean < MEAN_LO else 'TOO BRIGHT')))
    print('  pixels <60 luma %5.1f%%   target <=%.0f%%  %s'
          % (dark, DARK_MAX, 'ok' if ok_d else 'SHADOW EATING THE SET'))
    print('  dominant colours %s' % ', '.join(doms))
    if not ok_m and mean < MEAN_LO:
        print('  fix: the prompt asked for hard light without asking for BRIGHT.')
        print('       Add an explicit brightness line and cap the shadow area.')
    if not ok_d:
        print('  fix: bound how much frame the shadow may occupy, and never name')
        print('       a shadow as an object on an empty set.')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    for p in sys.argv[1:]:
        check(p)
