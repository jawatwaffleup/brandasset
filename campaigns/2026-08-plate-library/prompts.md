# Plate library — Krea prompt set

**Written 24 Aug 2026** · For generating on **krea.ai in the browser**, free tier.
Companion to `programs/AI-PRODUCTION.md` and `GEMINI.md`.

Five plates covering the environments this folder **does not** contain. Nothing here generates a
waffle, a character, the logo or packaging — those layer in afterwards from supplied files.

---

## 1. The reference-image answer

**Attach exactly one file: a palette card from `reference/`. Nothing else.**

| File | Palette | Use on |
|---|---|---|
| `reference/ref-palette-street-day.png` | cyan dominant · gold · pink · cocoa | Plates 1, 3, 4 |
| `reference/ref-palette-night.png` | cocoa dominant · cyan · pink · gold | Plate 2 |
| `reference/ref-palette-studio-gold.png` | gold dominant · ice blue · cocoa · pink | Plate 5 |

These are flat brand colour, built straight from `tokens/wup-tokens.json`. They exist to solve a
specific documented failure: **a hex code written into a prompt gets rendered into the picture as
text** (Veo printed `C5DBE4` into a frame on 23 Aug 2026). A style reference locks the palette
without a hex ever appearing in the prompt. `ref-palette-studio-gold` also measures mean luma 201 —
inside the house band — so it carries the exposure, not just the colour.

Regenerate them any time with `python campaigns/2026-08-plate-library/make-reference-cards.py`.

### Set the strength to 0.35, not the 0.5 default

⚠️ A flat swatch pushed too hard makes the model paint literal colour blocks. **The tell is
hard-edged rectangles appearing in the picture** — a pink square floating on a wall, a gold band
across the sky. If you see that, drop the strength. If the colour drifts off-brand instead, raise it
toward 0.5. It should never need to go past that.

### Never attach these

| Never upload as a reference | Why |
|---|---|
| Anything from `assets/marketing/product-hero/` | A style reference generates *new* product. AI gets the grid, the stick and the crumb wrong, and it is the one thing this audience knows by heart |
| Any file from `assets/characters/` | Generating new poses from supplied artwork is redrawing the character — the same hard rule as generating one from scratch |
| `assets/logo/`, `assets/icon/`, `assets/symbol/` | The white signature wave through the letterforms does not survive a generator |
| `assets/marketing/packaging/` | Real files only — and `BD BOX A.jpg` is off-palette, so it would poison the colour too |
| `assets/typography/` | The four-layer treatment is built artwork; it composites, it never regenerates |

This is `GEMINI.md` §4 and it does not bend for a different tool. **AI makes the stage. It never
makes the actors.**

---

## 2. Which model

| Job | Model | Why |
|---|---|---|
| **Drafting** — composition, framing, reserved space | **Krea 2 Large** | Takes a style reference with a real **strength** slider, and `creativity: raw` **turns prompt expansion off**. That matters: expansion rewrites your prompt and can quietly reintroduce the things you fenced out. Capped at 1K, which is fine for judging a layout |
| **The keeper** | **Seedream 4** | Goes to 4096px. Generate at **1440 × 2560** and you get ~1.33× headroom over 1080×1920, so a push-in crops into real pixels instead of upscaling |
| **Video, once there's balance** | **Seedance 2.5** | 9:16, 1080p, 4–30s. Its own guide wants hard negatives in a constraints tail — the opposite of the still models below |

**Generate stills, not video.** Roughly 240 compute units for one Seedance clip against a handful for
a still, and `programs/AI-PRODUCTION.md` §6 already establishes camera-moves-on-stills as a route.
The renderer in `campaigns/2026-08-square-is-the-new-heart/build.py` does push, pull and drift on any
still with brand-correct easing — hand me a plate and it becomes a moving shot with no generation
spend at all.

### Settings

```
Model        Krea 2 Large  (draft)   /   Seedream 4  (final)
Aspect       9:16                    /   width 1440 · height 2560
Resolution   1K
Creativity   raw            ← Krea 2 only. Do not leave this on "low"
Style ref    one palette card, strength 0.35
```

⚠️ **"Vertical 9:16" in the prompt text does not set the aspect ratio.** The v1 plate came back
1364×768 — 16:9 landscape — because the UI control was left on its default. The prompt line is a
composition hint to the model; **the dropdown is what actually crops the canvas.** Set it every time.

⚠️ **These are still-image models.** v1 came back as a 24fps 5.88s clip, which means a video model
was picked. Video models don't take the palette card the same way, cost roughly 3× a still, and give
you less resolution. Pick from the *image* tab.

### There is no negative prompt box

Neither Krea 2 Large nor Seedream 4 exposes a negative field. **Every exclusion below is already
written into the prose as something that IS true about the frame** — "completely deserted" rather
than "no people". Don't add "no X" lines; naming a thing tends to summon it.

*(This is the opposite of Seedance 2.5, which explicitly wants hard negatives. Per-engine, not
universal — `GEMINI.md` §2 currently states it as universal and needs amending.)*

---

## 3. The plates

### 3.0 The register rule — learned the hard way, 24 Aug 2026

**v1 of Plate 1 came back a beautiful documentary photograph of a real Dhaka street.** Structure was
perfect — deserted, straight down the length, shutters both sides, power lines, dry tarmac. Palette
was a total miss: dominant colours `#606358`, `#3C3934`, `#A19683`. Grey and mud. Mean luma 128,
19% of frame under 60 luma.

**The cause was the prompt's register, not its colour words.** "A narrow South Asian city street …
35mm … deep focus … power lines" is a *photojournalism* brief, and a photoreal model knows exactly
what a real Dhaka street looks like: weathered, dusty, hazy, grey-brown. Every realism cue outvoted
every colour word. Real streets are not cyan, so asking for a real street gets you a real street.

**The fix is to state that the street is art-directed.** It was freshly painted for a shoot. It was
swept. The air is clear because a crew waited for it. Say that, or realism wins again:

| Add to every plate | Kills |
|---|---|
| "a hyper-saturated commercial advertising photograph, art-directed and colour-graded" | the documentary default |
| "freshly repainted, new, smooth and flawless — painted this morning" | rust, weathering, faded patches |
| "the air is perfectly clear", "the sky holds its colour, never white, never hazy" | haze blowing the sky out and crushing contrast |
| "the sun is nearly overhead, shadows short and confined to a narrow strip" | the shadow band eating a fifth of the frame |

**And the grade cannot save a drab plate.** Tested on the v1 file: a hard brand grade moved the
numbers (dark 20% → 2.8%) but posterised the picture, banded the shutters and threw cyan blotches
across the road. A grade moves an *already saturated* image onto an exact hex. It cannot manufacture
colour that was never photographed. `GEMINI.md` §1 says exact values are matched afterwards in the
grade — true, but only if the generation came back saturated in the first place. Amend it to say so.

---

### Plate 1 — Daylight street · for ON THE MOVE

Reference `ref-palette-street-day.png` @ 0.35 · **set aspect to 9:16 in the UI**

```
A hyper-saturated commercial advertising photograph, art-directed and colour-graded
— not documentary, not photojournalism.

A narrow city street built as a film set, photographed straight down its length. The
roller shutters lining both sides have been freshly repainted for the shoot in flat,
vivid, poster-like colour — brilliant electric cyan down the left side, warm honey
gold down the right. The paint is new, smooth and flawless, with no rust and no
faded patches; every surface looks painted this morning. The road is swept spotless.
A few clean power lines cross overhead. The street is completely deserted, empty from
the foreground all the way to the far end.

The air is perfectly clear and the sky is a deep, rich, saturated cyan that holds its
colour all the way down to the horizon — bright and clean, never white, never hazy.

The whole frame is bright, high-key and evenly exposed corner to corner, with colour
so saturated it looks printed. Hard direct sunlight from high and slightly left; the
sun is nearly overhead, so shadows are short and confined to a narrow strip covering
well under a tenth of the picture. The darkest tones are a deep cocoa brown.

Shot on a 35mm lens, eye level, straight on, deep focus. Vertical 9:16.
```

> **Composites in:** a real hand holding a real waffle, filmed or cut from a shoot, entering from the
> lower right. The lower right sixth is deliberately clean.

---

### Plate 2 — Night street · for THE LATE SHIFT

Reference `ref-palette-night.png` @ 0.35

```
A hyper-saturated commercial advertising photograph, art-directed and colour-graded
— not documentary, not photojournalism.

A narrow city street at night, built as a film set, photographed straight down its
length. Plain signboards line both sides — smooth blank panels glowing brilliant
electric cyan and hot bubblegum pink, completely unmarked, lighting the street like
practical lamps. Strings of warm honey gold bulbs cross overhead. The road surface
is freshly wet and mirrors the coloured light in long sharp streaks. Every surface
is clean and newly painted. The air is perfectly clear, with no haze and no smoke.
The street is completely deserted, bare wet tarmac, unobstructed to the far end.

The frame is bright for a night scene and evenly readable corner to corner — the
glowing panels do the lighting and there is visible detail everywhere. The
darkest areas are a deep cocoa brown rather than black. Richly saturated, high
contrast, crisp and clean.

Shot on a 35mm lens, eye level, straight on, deep focus. Vertical 9:16.
```

> **Composites in:** real product, lower third. **Night plates use the adjusted acceptance band in
> §4** — the daylight numbers will fail every night plate by design.

---

### Plate 3 — Rooftop, seat reserved · for GANG SIGHTING

Reference `ref-palette-street-day.png` @ 0.35

```
A hyper-saturated commercial advertising photograph, art-directed and colour-graded
— not documentary, not photojournalism.

A flat concrete rooftop in a city, dressed as a film set, in late golden-hour sun,
photographed from parapet height. A low concrete ledge runs across the lower third
of the frame, its top surface swept clean, bare and completely uninterrupted. Behind
it a skyline of rooftops and water tanks falls gently out of focus beneath a deep,
rich, saturated cyan sky that warms to honey gold at the horizon and holds its colour
throughout — never white, never hazy. The air is perfectly clear. The rooftop is
completely deserted — plain unmarked concrete, clean and newly finished.

The right third of the frame is open, empty and completely unobstructed, from the
ledge up to the top edge of the picture.

The whole frame is bright and evenly exposed, high-key, richly saturated. Hard low
sun from the left throws sharp-edged shadows that stay small and cover well under
a fifth of the picture. Darkest tones are a deep cocoa brown.

Shot on a 35mm lens, eye level, deep focus. Vertical 9:16.
```

> **Composites in:** one character PNG from `assets/characters/bangladesh/<name>/2d/hero.png`, into
> the reserved right third. **If a generation fills that space, regenerate it — never mask it out.**
> Character appears; character does not speak.

---

### Plate 4 — After the rain · weather

Reference `ref-palette-street-day.png` @ 0.35

```
A hyper-saturated commercial advertising photograph, art-directed and colour-graded
— not documentary, not photojournalism.

A narrow city street built as a film set, immediately after heavy rain, in a bright
break of hard afternoon sun. Standing water sheets across the tarmac and mirrors the
buildings above it. Shutters and walls line both sides, freshly repainted for the
shoot in flat, vivid, poster-like colour — hot bubblegum pink and brilliant electric
cyan, new smooth paint with no rust and no faded patches. A few last drops fall
through the light. The air is washed perfectly clear and the sky holds a deep
saturated cyan, never white, never hazy. The street is completely deserted, the water
surface clean and unbroken.

Bright and evenly exposed corner to corner, richly saturated, high contrast, crisp
and clean. Hard direct sun from the upper right throws sharp-edged reflections,
and shadows stay small, covering well under a fifth of the frame. Darkest tones
are a deep cocoa brown.

Shot on a 35mm lens, low angle close to the water, deep focus. Vertical 9:16.
```

> **Composites in:** product or hand, upper centre. Also the best transition plate in the set — the
> reflections cut cleanly to anything.

---

### Plate 5 — Pour texture · transitions and overlays

Reference `ref-palette-studio-gold.png` @ 0.35

```
A hyper-saturated commercial advertising photograph, art-directed and colour-graded
— not documentary, not photojournalism.

Extreme close-up of a thick ribbon of glossy molten chocolate pouring and folding
through the air against a flat, freshly painted, flawless background wall in vivid
warm honey gold.
The ribbon twists and catches the light, and a few droplets break away and hang
suspended. Nothing else is in the picture — no vessel, no surface beneath, no
object the pour lands on. Just the ribbon against clean flat colour.

Bright and evenly exposed, richly saturated, high contrast, crisp and clean. Hard
direct light from the upper left picks out sharp specular highlights along the
chocolate. Shadows are small and tight. Darkest tones are a deep cocoa brown.

Shot on a 100mm macro lens, straight on, shallow depth of field on the pour only.
Vertical 9:16.
```

> **Composites in:** nothing. This is a transition wipe and an overlay element. Abstract texture —
> pour, drip, splash, steam, crumb — is explicitly on the allowed list (`CLAUDE.md` §6).

---

## 4. Accept or reject — run the numbers, don't eyeball it

```bash
python campaigns/2026-08-plate-library/check-plate.py output/plates/plate-1.png
```

| | Daylight plates (1, 3, 4, 5) | Night plate (2) |
|---|---|---|
| Mean luminance | **184–208** | **95–140** |
| Pixels under 60 luma | **≤ 5%** | **≤ 35%** |

Both rejected Veo plates in `output/2026-08-drop-test/` fail this test automatically, which is what
it was built against. The script prints the specific prompt fault when it rejects.

**The failure mode to expect:** "hard directional light" on its own reads to every generator as
*dramatic*, and dramatic means big black shadows — the exact opposite of this brand. That is why each
prompt above pairs the light direction with an explicit brightness instruction **and** a cap on how
much frame the shadow may occupy. If a plate comes back dim, that pairing is what got dropped.

**Never name a shadow as a thing on an empty set.** Asking for "a small crisp shadow" on a bare
surface makes the model invent an object to cast it — that is where the dark blurry prop in
`plate-v2` came from. State the light direction and let the shadow follow.

---

## 5. Credits, honestly

Free tier is **100 compute units/day**, web app only — the API and MCP path bills a separate balance
that the free plan does not fund, which is why generation from here returns `INSUFFICIENT_BALANCE`.

Extrapolating from the Pro plan's own figures (20,000 units ≈ 257 Nano Banana 2 images ≈ 83 Seedance
2.0 videos), that is roughly **78 units for a premium still and ~240 for a video clip**. So one
premium still a day, or several on the cheaper models — and **no video at all** on free.
`[CONFIRM]` against the cost the website shows before you hit generate; these are extrapolations, not
published numbers.

**Also: the free tier carries no commercial licence.** Anything generated on it is for testing the
look, not for posting to @waffleup.online. Basic at $9/mo is the floor for publishable work; Pro at
$35 ($21 annual) is the floor for video.

---

## 6. Handing back

Drop downloads into `output/plates/` named to match — `plate-1-street-day.png`, `plate-2-night.png`.
Run `check-plate.py` over them. Then tell me which passed, and I'll cut them into a reel with the
renderer — camera move, grade to exact token values, typography and end card, exported at
1080×1920/30fps. I rewrite the prompt for anything that failed; I don't guess from the filename.
