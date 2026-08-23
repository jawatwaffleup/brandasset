# AI Production Pipeline — Gemini / Veo

**Version 1.0 · 23 August 2026**
How to produce WaffleUp content using the Google AI Pro subscription plus this brand folder. Applies to every format in `programs/SOCIAL-ENGINE.md`.

---

## 1. The toolchain

| Tool | What it's for | Where |
|---|---|---|
| **Flow** | Video plates. Veo under the hood, with camera controls, negative prompt field, clip extension. **The main tool.** | labs.google/flow |
| **Gemini app** | Quick stills, copy drafting, caption variants | gemini.google.com |
| **Whisk** | Fast image riffing from references — good for mood, not for final plates | labs.google/whisk |
| **CapCut** | Compositing, camera moves on stills, text, export. Free. | desktop app |

> **[CONFIRM]** Generation quotas on Google AI Pro. Check your limits in Flow before planning a big batch — don't assume unlimited.

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

**The negative-prompt problem.** Flow has a negative prompt field. The Gemini app doesn't. So:

- **In Flow** — put exclusions in the negative field
- **In the Gemini app** — phrase every exclusion *positively*, because naming a thing tends to summon it

| Don't write | Write instead |
|---|---|
| "no people" | "completely deserted" |
| "no text, no signage" | "bare unmarked concrete" |
| "no soft lighting" | "harsh direct sunlight, sharp-edged shadows" |
| "no grey palette" | "richly saturated colour" |
| "no clutter on the ledge" | "a clean empty ledge surface" |

**Standard negative field** (paste into Flow every time):

```
people, human figures, crowds, cartoon characters, mascots, animals, text,
letters, words, signage, logos, watermarks, brand marks, soft diffuse
lighting, overcast sky, grey and beige tones, lens flare, drone shot,
camera shake, time lapse
```

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
