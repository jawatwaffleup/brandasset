# SQUARE IS THE NEW HEART — 15s Reel

**Built 24 Aug 2026** · **Render:** `output/2026-08-square-is-the-new-heart/square-is-the-new-heart-15s.mp4`
**Spec:** 1080×1920 · 30 fps · 15.00s · H.264 yuv420p · 4.6 MB · **no audio track**

---

## Strategic read

**Territory 4 — *square beats round*.** The primary tagline is already an engineering claim, not just a
slogan: the square packs flat, stacks, doesn't roll, doesn't crush. This cut states the claim as a
visual argument — round is the old world, square is what replaced it — and lets six products carry it
rather than one.

**70/30: this is a brand-heat post.** No CTA, no price, no channel claim. Judge it on saves and shares,
never on orders (`SOCIAL-ENGINE.md` §0 rule 1). The handle on the end card is identification, not a
call to action, so it carries no Chef's Table / delivery exposure.

**Rotation, not anchoring.** Six SKUs, one appearance each — Red Velvet, Tri-Chocolate,
Very Very Strawberry, Nutella, Fruity Bliss, Bangla Pizza. Nutella appears once, at the same weight as
everything else, per `CLAUDE.md` §8 rule 3.

---

## The cut

| # | In | Dur | Content | Move |
|---|---|---|---|---|
| 1 | 0.00 | 1.9 | `02-woas-red-velvet` — heart-shaped sprinkles beside square waffles | push in |
| 2 | 1.90 | 1.1 | **CARD, gold** — "ROUND IS / OVER." | scale settle |
| 3 | 3.00 | 1.8 | `03-woas-tri-chocolate` | push in |
| 4 | 4.80 | 1.8 | `09-very-very-strawberry` — plain square → round mirror | drift right |
| 5 | 6.60 | 1.7 | `01-woas-nutella` | push in |
| 6 | 8.30 | 1.7 | `10-fruity-bliss` | pull back |
| 7 | 10.00 | 1.7 | `11-bangla-pizza` | drift left |
| 8 | 11.70 | 3.3 | **END CARD, cyan** — supplied lockup → logo → handle | staged reveal |

**Shot 1 is the hook by design.** Heart-shaped sprinkles falling around two hard square waffles states
the whole argument in the first 1.5 seconds, before a word appears. Shot 4 restates it literally — a
bare square waffle on the left, its topped twin reflected in a round mirror on the right — and the
drift moves from one to the other.

**The bob.** Every product shot carries a ±0.4% sinusoidal vertical drift at 0.85 Hz, phase-offset per
shot. The house shots are of levitating product; without it, a static frame under a camera move reads
as a photograph rather than as a thing hanging in the air.

---

## What generated what

**Nothing was AI-generated.** Every pixel traces to a supplied file.

| Layer | Source |
|---|---|
| All six product shots | `assets/marketing/product-hero/` — real photographs |
| Tagline lockup | `assets/typography/Square (rgb).png` — supplied four-layer artwork, scaled only |
| Logo | `assets/logo/Waffle Up Logo - RBG.png` — supplied file, proportional scale only |
| "ROUND IS OVER." | Futura Extra Bold, caps, four-layer house treatment built in code |
| "@waffleup.online" | Bebas Neue, Deep Cocoa |
| Field colours | `tokens/wup-tokens.json` — exact hex, not sampled from artwork |

**Edits applied to the photographs:** a single unify pass — saturation ×1.08, contrast ×1.05 — plus the
9:16 crop window and Lanczos resample. Nothing structural: no relighting, no recolouring, no cutouts,
no regrading toward the packaging.

**Two colour decisions worth recording:**

1. `Square (rgb).png` is the **complete lockup**, not the single word — "SQUARE IS THE NEW HEART" in
   full. Setting the remainder in live type duplicates it. The asset name is misleading; the catalog
   entry should say so.
2. The lockup's "HEART" is brand pink `#FF629B`, so **the end card cannot be pink** — it disappears.
   It sits on cyan. The "ROUND IS OVER." card moved to gold so the two cards don't share a field.

**Kunaffle™ was cut from the lineup.** `05-woas-kunaffle` is shot on a **white** backdrop, which breaks
the photography rule that backdrops are brand colours, and it would have read as a hole in a run of
saturated fields. Not a product judgement — a backdrop one.

---

## Known limits

- **Silent by design.** `assets/marketing/audio/` has no verified commercial-rights record
  (`CLAUDE.md` §8 rule 7). Drop a cleared track under it before this goes anywhere public — the cut is
  built on a steady ~1.7s beat, so it will take a track cleanly.
- **Source resolution.** The hero photographs are ≤1200px on the long edge, so the render upscales
  ~1.6–1.75×. Clean at phone size; do not use this cut for anything larger than a phone screen.
- **Anniversary lockup not used.** The five-year badge in `campaigns/2026-12-five-years/` is still
  unconfirmed artwork — deliberately kept out.

---

## Copy bank — captions for this cut

Pick one. No CTA, per the 70/30 rule.

- Square is the new heart. Sorry, circles.
- Round had a good run.
- Four corners. No apologies.
- It doesn't roll away. That's the whole pitch.
- Bangla: গোল না, চারকোনা।

---

## Rebuilding

```bash
python "campaigns/2026-08-square-is-the-new-heart/build.py"
```

Deterministic — same inputs, same output. The cut is the `SHOTS` list at the bottom of the script;
durations, crop windows and moves are all data, so re-timing it is an edit to that table, not to the
renderer. Requires `Pillow` and `imageio-ffmpeg` (both already present).
