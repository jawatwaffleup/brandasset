# AI Production Pipeline — Gemini / Veo

**Version 1.0 · 23 August 2026**
How to produce WaffleUp content using the Google AI Pro subscription plus this brand folder. Applies to every format in `programs/SOCIAL-ENGINE.md`.

---

## 0. The shape of the whole thing

**Flow never sees the assets, and it doesn't need to.** The finished video is a sandwich, and Flow only makes the bottom slice.

| Layer | Who makes it | Where it comes from |
|---|---|---|
| **Top** — logo, hero word, end card | Nobody. Supplied files. | `assets/logo/` · `assets/typography/` |
| **Middle** — the product, the character | Nobody. Real photos and supplied art. | `assets/marketing/product-hero/` · `assets/characters/` |
| **Bottom** — the room it all sits in | **Flow** | generated from a prompt |
| **The assembly** | **CapCut** | you, ten minutes |

### One shot, traced end to end

Take THE DROP — a Nutella waffle floating against a gold-and-mint backdrop.

1. **Flow** generates an *empty* backdrop: two-tone colour block, hard key light from upper left, one crisp shadow, slow push in, 8s. No product in it. There is no waffle anywhere in that generation. → `plate.mp4`
2. **Cut out** the real waffle from `assets/marketing/product-hero/01-woas-nutella.jpg`. → `product.png`
3. **CapCut**: `plate.mp4` as the base, `product.png` as an overlay. Keyframe a slow 6px float, duplicate-blur-darken a shadow underneath it.
4. **Overlay** `assets/typography/Waffleistic (rgb).png` — the four-layer treatment is already built into that file.
5. **End card** from `assets/logo/`. Export 1080×1920, 30fps.

Flow made the room. Everything the audience recognises as WaffleUp was a real file the whole time.

### Why this is the feature, not the workaround

A composited PNG is pixel-perfect in **every frame, forever**. A generated waffle is wrong in a **new way every time** — and the grid, the stick and the crumb are the one thing this audience knows by heart. Same for the logo's signature wave, same for every character.

### Reference images — what may go in

> **Amended 31 Aug 2026 (Jawat).** The Merlulu poses `001`–`004` were generated with ChatGPT from the approved main pose, and they hold the line weight, the palette and the silhouette. **AI may now pose an approved character from reference.** The rule it replaces — *never AI a character* — is retired.

Flow has **Ingredients to Video** (up to three reference images) and **Frames to Video** (a start and end frame it animates between). Both are now in play for characters, on conditions.

| Image input | Verdict |
|---|---|
| A **generated** backdrop still as a start frame | ✅ Fine |
| Frames to Video between two **generated** stills | ✅ Fine |
| A **character identity sheet** — two or three approved poses of one character | ✅ Fine, and required |
| A single character PNG as the only reference | ⚠ Weak — identity drifts. Give it three angles. |
| A **photograph** of real packaging, defocused, as background dressing | ⚠ Fine, but see the palette note below |
| A product photo, to generate the product in hero position | ❌ Never — use the real shot |
| The logo, as reference or as something to render | ❌ Never — composite the file |

**Conditions on character generation:**

1. **Approved characters only, from approved reference.** A generator may re-pose one of the ten. It may not invent an eleventh, restyle one, or change a costume.
2. **Three angles minimum** in the identity sheet, and **the same sheet on every shot** for that character across a piece.
3. **Clips of 3–4 seconds.** Design drifts *inside* a clip — the mark, the medallion and any lettering go first.
4. **Check the last frame, not the first.** If the last frame is off-model, the clip is off-model.
5. **Grade back to the palette afterwards.** Generators run warm and desaturate the cyan.
6. **Anything a generation gets wrong, composite instead.** The fallback in §6 has not gone away — it is now the repair, not the default.

**The packaging palette trap.** The real boxes print in a hotter magenta and mint green than the brand palette. Feed a box photo as reference and the model pulls the whole frame that way, and the printed characters on the panels are superseded designs. Keep any box defocused, and grade back. The **branded stick** is the safe brand cue — clean, on-palette, nothing to drift.

---

## 1. The toolchain

| Tool | What it's for | Where |
|---|---|---|
| **Flow** | Video plates. Veo under the hood, with camera controls, clip extension, Frames and Ingredients modes. **The main tool.** | labs.google/flow |
| **Gemini app** | Quick stills, copy drafting, caption variants | gemini.google.com |
| **CapCut** | Compositing, camera moves on stills, text, export. No cost. | desktop app |
| **Claude Code** | Writes the prompts, the shot lists and the copy. Holds the brand rules. | this repo |

**Brand context for the Google side lives in `GEMINI.md`** at the repo root — the paste block, the positive-phrasing conversion table and the hard fences. Paste it in before the first prompt of any session.

### Two corrections to earlier versions of this doc

- **Whisk no longer exists separately.** Whisk, ImageFX and the original Flow were merged into one Flow workspace in February 2026. Everything routes through Flow now.
- **Gemini CLI is not a route to video, and for individual accounts it is retired.** Google stopped serving Gemini CLI and the Code Assist IDE extensions for individual, AI Pro and AI Ultra tiers on **18 June 2026**, pointing users at **Antigravity CLI** instead. Neither CLI has ever generated video — they are coding agents. Video is Flow and Google Vids. Antigravity CLI does read `GEMINI.md`, so the context file works there if you want it for text drafting.

### Credits `[CONFIRM] against your own Flow counter`

Google AI Pro is roughly **1,000 credits/month**; a 10s Veo 3.1 clip at Quality costs about **125 credits**. That is ~10 Quality, ~50 Fast or ~100 Lite clips a month, capped at 8s per clip. **Draft at Lite, promote only the keeper to Quality.** Third-party figures move — check the counter before planning a batch.

---

## 2. The golden rule

> **AI makes the stage, and may pose the actors. It never makes the props that carry the brand mark.**

| AI generates | Never AI — use the supplied file |
|---|---|
| Backgrounds, sets, rooftops, streets | **The logo, symbol and icon** — `assets/logo/` |
| Night city, motion plates, weather | **The product in hero position** — `assets/marketing/product-hero/` |
| Abstract texture: splash, drip, steam | **Packaging artwork** — `assets/marketing/packaging/` |
| Colour-blocked studio backdrops | **Any lettering, wordmark or signage** |
| **Approved characters, re-posed from reference** *(amended 31 Aug 2026)* | |

The line moved, and it moved for a reason: a re-posed character can be checked against the reference and regenerated until it is right. **The logo cannot** — the signature wave through the letterforms is the thing generators reliably destroy, and a broken mark is worse than no mark. Same for the product: the grid, the stick and the crumb are what this audience knows by heart.

When a generated character does come back wrong, the composite route in §6 is the repair.

**Also never generate:** implied claims — "fastest delivery", "best in Bangladesh", health or nutrition claims.

---

## 3. How this folder feeds the pipeline

| Step | Pull from |
|---|---|
| Writing the prompt | `tokens/wup-tokens.json` — exact hex values |
| Generating the plate | *(nothing — the folder never goes into a generator)* |
| Compositing the character | `assets/characters/bangladesh/<name>/2d/hero.png` |
| Product cut-out | `assets/marketing/product-hero/` — 15 real shots |
| Hero words | `assets/typography/` — 15 pre-set word-marks, four-layer treatment already built |
| End card | `assets/logo/` · `assets/icon/` for small sizes |
| Background device | `assets/pattern/Brand-Pattern.jpg` |
| Caption voice | `brand/character-voices/` *(draft — no first-person until approved)* |

---

## 4. Converting prompts for Veo

Veo wants **cinematic prose**, not keyword lists. Rewrite accordingly.

**⚠ Correction to v1.0 of this doc.** It claimed Flow has a negative prompt field. **It does not.** Flow takes plain English in a single prompt box — no negative field, no keywords, no weighting. Neither does the Gemini app. Anything written as "no X" lands inside the prompt, where it tends to summon the very thing it names.

**So every exclusion is phrased positively, in both tools, always.** Say what IS true about the frame.

| Don't write | Write instead |
|---|---|
| "no people" | "completely deserted" |
| "no product, no waffle, no food" | "a bare, clean, completely empty surface — an unoccupied set photographed before anything was placed on it" |
| "no text, no signage" | "bare unmarked concrete" · "a plain unmarked wall" |
| "no soft lighting" | "harsh direct sunlight, sharp-edged shadows" |
| "no grey palette" | "richly saturated colour, high contrast" |
| "no clutter on the ledge" | "a clean empty ledge surface" |
| "no camera shake" | "locked off, perfectly steady" |
| "no cartoon characters" | *(say nothing — don't plant the idea)* |

The full conversion table lives in `GEMINI.md` §2.

---

## 5. The three Bhoppu plates, rewritten for Flow

Vertical 9:16 throughout. Generate the longest clip Flow allows and trim — extra tail is free once generated.

### Plate A — the hook

```
A camera cranes smoothly upward along the face of a weathered concrete rooftop
parapet in a South Asian city, cresting the top edge so open sky fills the
frame. Late golden-hour sunlight rakes hard across the rough concrete from the
left, casting one sharp-edged shadow. The sky burns saturated cyan, fading to
warm gold at the horizon. The rooftop is completely deserted — bare unmarked
concrete. Shot on a 24mm lens, low angle, continuous upward movement, high
contrast, richly saturated, crisp and clean. Vertical 9:16.
```

### Plate B — the reveal

```
A locked-off camera at parapet height on a South Asian city rooftop, pushing in
very slowly. The flat top of a concrete ledge runs across the lower third of
frame, clean and completely bare. Behind it a golden-hour skyline of rooftops
and water tanks falls gently out of focus. Harsh direct sunlight from the left
throws sharp crisp shadows across the ledge. Saturated cyan sky, warm gold
light, deep cocoa-brown shadows. The right third of the frame is open and
completely unobstructed. Shot on 35mm, eye level, high contrast. Vertical 9:16.
```

> The right-third instruction is **reserving Bhoppu's seat**. If a generation fills it, regenerate — don't mask it out.

### Plate C — the view / the walk

```
A camera tracks smoothly sideways to the right along a rooftop parapet at
walking pace, the near concrete ledge sliding past quickly while the distant
city skyline drifts slowly behind it — strong depth separation between
foreground and background. A loose plastic sheet flutters in the wind at the
edge of frame. Low golden sun from the left casts long sharp shadows across the
rooftops. Saturated cyan sky fading to gold at the horizon, deep cocoa shadows.
The rooftop is deserted, bare unmarked concrete. Shot on 35mm, eye level,
smooth steady tracking, high contrast. Vertical 9:16.
```

---

## 6. Compositing in CapCut

**Making a character "walk" without generating them:**

1. Import the plate. Set project to **1080×1920, 30fps**.
2. Add `bhoppu/2d/hero.png` as an overlay. Position centre-right, scale to read at phone size.
3. **The bob** — keyframe the overlay's Y position: 2–4px up and down, roughly two cycles per second. Add 1–2° rotation on the same rhythm.
4. **The shadow** — duplicate the PNG, fill black, flatten, blur, drop opacity to ~30%, place under his feet, bob it in sync.
5. Background slides, he bobs → he's walking.

> **Amended 31 Aug 2026.** Feeding character reference into an image-to-video tool is now allowed — see §0 for the conditions. The layer-bob technique above has not gone away: it is still the most reliable way to move a character, it costs nothing, and it is exactly on-model in every frame. **Use it whenever a shot doesn't need the character to do anything a flat overlay can't do.** Reach for generation when the shot needs a walk cycle, a head turn or a real interaction with the scene.

**Camera moves on stills** (if you generate images rather than video):

| Move | How |
|---|---|
| Crane up | Scale ~130%, keyframe Y position upward |
| Slow push | Scale 100% → 110% over the shot |
| Lateral drift | Generate **16:9 wide**, crop a 9:16 window, slide the crop sideways |

For real parallax, mask the foreground off the background as two layers and slide the front faster.

**Text:** Futura Extra Bold caps, cocoa `#450001` drop shadow plus white outline. Inside safe margins — 250px top, 400px bottom. For a full hero word, use the supplied artwork in `assets/typography/` rather than rebuilding the four-layer effect.

---

## 7. Mapping to the social engine

| Format | Route |
|---|---|
| **THE DROP** | Generate colour-blocked studio backdrop → composite real product photo |
| **SOUND ON** | ❌ **No AI.** Real macro footage, real audio. Phone + quiet room. |
| **ON THE MOVE** | Generate street plate → composite real hand + product, or just film it |
| **NOT-SO-FACTS** | ❌ No AI needed. Typography on brand pattern. |
| **GANG SIGHTING** | Generate the character in the environment from an identity sheet, or generate the environment with empty space and composite |
| **CAUGHT CRISPY** | ❌ No AI. Customer's own content. |
| **THE LATE SHIFT** | Generate night city plate → composite product |
| **ORDER UP** | Generate clean backdrop → composite real product |

**Half the engine needs no AI at all.** That's by design — SOUND ON, NOT-SO-FACTS and CAUGHT CRISPY are the cheapest and most reliable formats you run, and none of them touch a generator.

---

## 8. Guardrails

Every rule in `CLAUDE.md` §3 and §6 still applies, whichever tool is generating:

- Never **"free"** or **"discount"** — in any language, any channel
- Characters: approved characters only, posed from an approved identity sheet; **no first-person speech** until voices are approved
- Ink is `#450001`, never pure black
- Hard light, brand-colour backdrops, 30fps
- No Foodpanda/Pathao CTA on Chef's Table content
- Audience starts at 10
- Music: cleared royalty-free only — `assets/marketing/audio/` has no verified rights record
