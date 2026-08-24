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

### Yes, Flow accepts images — and that's the trap

Flow has **Ingredients to Video** (upload up to three reference images for characters, objects or style) and **Frames to Video** (a start and end frame it animates between). So you *can* technically drop Bhoppu into Flow.

**Don't.** Ingredients to Video works by generating *new poses* from the reference — which is redrawing him, the exact thing the character rules forbid. It will come back with four fingers, a wrong tracksuit and a dumbbell that changes shape mid-shot.

| Flow image input | Verdict |
|---|---|
| A **generated** backdrop still as a start frame, to animate it | ✅ Fine — no brand art involved |
| Frames to Video between two **generated** stills, for a controlled move | ✅ Fine |
| A character PNG as an "ingredient" | ❌ Never |
| A product photo as an "ingredient" | ❌ Never |
| The logo, or packaging artwork, as a style reference | ❌ Never |

Motion for supplied art comes from **moving the layer in CapCut**, never from regenerating the art. §6 has the technique.

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

> **AI makes the stage. It never makes the actors.**

| AI generates | Never AI — use the supplied file |
|---|---|
| Backgrounds, sets, rooftops, streets | **The logo** — `assets/logo/` |
| Night city, motion plates, weather | **Any character** — `assets/characters/` |
| Abstract texture: splash, drip, steam | **The product in hero position** — `assets/marketing/product-hero/` |
| Colour-blocked studio backdrops | **Packaging artwork** — `assets/marketing/packaging/` |

This isn't a limitation to work around — it's what keeps the brand exact. A composited PNG is pixel-perfect in every frame, forever. A generated character is wrong in a new way every time.

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

> ⚠ **Never feed a character PNG into Veo, Flow, Whisk or any image-to-video tool.** That generates new poses from his artwork, which is redrawing him — the same hard rule as generating him from scratch. Motion comes from moving the *layer*, never regenerating the art.

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
| **GANG SIGHTING** | Generate environment with empty space → composite character PNG |
| **CAUGHT CRISPY** | ❌ No AI. Customer's own content. |
| **THE LATE SHIFT** | Generate night city plate → composite product |
| **ORDER UP** | Generate clean backdrop → composite real product |

**Half the engine needs no AI at all.** That's by design — SOUND ON, NOT-SO-FACTS and CAUGHT CRISPY are the cheapest and most reliable formats you run, and none of them touch a generator.

---

## 8. Guardrails

Every rule in `CLAUDE.md` §3 and §6 still applies, whichever tool is generating:

- Never **"free"** or **"discount"** — in any language, any channel
- Characters: supplied art only, **no first-person speech** until voices are approved
- Ink is `#450001`, never pure black
- Hard light, brand-colour backdrops, 30fps
- No Foodpanda/Pathao CTA on Chef's Table content
- Audience starts at 10
- Music: cleared royalty-free only — `assets/marketing/audio/` has no verified rights record
