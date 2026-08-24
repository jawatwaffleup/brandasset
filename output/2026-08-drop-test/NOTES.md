# DROP backdrop plate — test 1

**Generated:** 23 Aug 2026, Flow · **File:** `plate-gold-mint.mp4` · **Verdict: reject, do not composite**

## What came back

720x1280 · 24fps · 8.00s · h264 · has an audio track

| Measure | This plate | House target | |
|---|---|---|---|
| Gold wall (lit) | `#E0B647` | `#F5D286` | dull ochre, too dark |
| Pale surface (lit) | `#B0DCA9` | `#C5DBE4` | green, should be ice blue |
| Mean luminance | **113** | 184-208 | far too dim |
| Pixels under 60 luma | **35%** | 0-5% | a third of frame is near-black |

## Why it failed

1. **The shadow ate the set.** A hard diagonal wedge cuts across both wall and floor, leaving only a thin lit strip of surface. There is nowhere to place a product that isn't in darkness.
2. **It reads as window light, not studio light.** Sun through a doorway. The house look is a clean studio key with one small contained product shadow.
3. **The floor is green.** The prompt said "soft mint green"; the actual house surface is pale ice blue `#C5DBE4`.
4. **The light animates.** The shadow wedge swings noticeably across the 8s. A static composited product would sit under a shadow that changes direction beneath it.

## Prompt faults (all three are prompt-side, not Veo-side)

- Asked for "hard directional light" with no brightness instruction -> Veo read *hard* as *dramatic* and went moody.
- Never bounded how much frame the shadow could occupy.
- Named the wrong colour for the surface.

Fixes folded into `GEMINI.md` §1 "Measured targets" and the v2 prompt below.

---

# Test 2 — `plate-v2-gold-iceblue.mp4`

**Verdict: reject.** But the v1 fix worked — the failure moved somewhere new.

| Measure | v1 | v2 | Target | |
|---|---|---|---|---|
| Dark pixels (<60 luma) | 35% | **2%** | 0-5% | ✅ fixed |
| Mean luminance | 113 | 159 | 184-208 | still dim |
| Surface colour | `#B0DCA9` green | `#7CB6C3` blue | `#C5DBE4` | ✅ right hue, too saturated |
| Wall, upper left | — | `#C5831C` | `#F5D286` | uneven |
| Wall, upper right | — | `#E4BB41` | `#F5D286` | 30-point swing across the wall |

## New failures

1. **`C5DBE4` is printed into the frame**, bottom left, every frame. Veo read the hex code in the prompt as text to render. **Never put a hex value in a prompt again** — see `GEMINI.md` §1.
2. **A dark blurry object sits on the surface**, right of centre. Caused by "a single small crisp-edged shadow falls to the lower right" — on an empty set, naming a shadow makes Veo invent something to cast it.
3. **Horizon too high.** Wall/surface boundary at ~48% of frame height; the house shots sit at ~57%. Less gold field to place a product against.
4. **Uneven wall.** Bright on the right, ochre on the left, plus corner vignetting. The house look is flat and even.
5. **Reads as water.** The hard teal line at the junction plus the receding blue makes the surface look like a pool rather than a seamless.

## Standing lessons

- Colours go into prompts as **words**, never hex. Grade to exact values in CapCut.
- On an empty plate, **never name a shadow**. State light direction only.
- Specify **even** lighting explicitly, corner to corner — "bright" alone still gives vignetting.

## The bigger question

Two generations spent on a backdrop that already exists as 15 finished photographs. THE DROP is the **worst** format to buy plates for: flat colour, exact tone and an empty frame are the three things generators are weakest at, and it is the one format where the finished asset is already in the folder. A slow push on the existing still in CapCut gets most of the motion for zero credits and zero brand risk.

**Spend Veo credits on what the folder does not contain** — street plates, night city, motion, weather, texture.
