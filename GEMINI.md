# GEMINI.md — WaffleUp brand context for Google AI surfaces

**Version 1.0 · 23 August 2026**
Companion to `CLAUDE.md`. Where `CLAUDE.md` tells Claude how to *think* about WaffleUp marketing, this file tells any **Google** surface — Antigravity CLI, the Gemini app, Flow — what it is allowed to make.

**Read `programs/AI-PRODUCTION.md` first.** That is the pipeline. This file is the context payload the pipeline needs.

---

## 0. What this file is for, per surface

| Surface | How this file reaches it | What it's good for |
|---|---|---|
| **Antigravity CLI** | Auto-loaded from repo root — it keeps `GEMINI.md` compatibility from the retired Gemini CLI | Text: caption variants, prompt expansion, shot-list drafting |
| **Gemini app** (gemini.google.com) | **Paste §1 by hand** — it cannot see this repo | Stills, copy drafts, prompt rewriting |
| **Flow** (labs.google/flow) | **Paste §1 first, then one prompt per generation** | Video plates. The one that matters. |
| **Veo via API** | Injected as a prefix by whatever script calls it | Batch plate generation |

> **No Google surface generates the finished ad.** Every one of them makes a *plate*. The brand goes on afterwards, in CapCut. See `programs/AI-PRODUCTION.md` §6.

---

## 1. THE PASTE BLOCK

Paste this whole block as the first message in any Gemini or Flow session. It is deliberately self-contained — it assumes the model can see none of this repo.

```
You are generating background plates for WaffleUp, a Bangladeshi street-dessert
brand. Waffles on a stick, square, sold from outlets in Dhaka, Sylhet,
Chattogram and one in Singapore. Audience: 10-25, urban, style-aware, phone in
hand. The brand promise is "joy that travels."

REGISTER: street, loud, funny, fast. Never luxury. Never "artisanal,"
"indulgent," "premium," "curated," "treat yourself." The entire brand exists to
de-luxury the waffle.

YOU MAKE THE STAGE. YOU NEVER MAKE THE ACTORS.
Generate ONLY: backgrounds, sets, streets, rooftops, night city, skies,
colour-blocked studio backdrops, abstract texture (splash, drip, steam, crumb),
weather, motion plates.
NEVER generate: the WaffleUp logo, any WaffleUp cartoon character or mascot,
the waffle product itself, packaging artwork, or any text, lettering, signage
or brand mark of any kind. Those are all real supplied files, composited in
afterwards. A generated character is wrong in a new way every time.

PALETTE — NEVER WRITE A HEX CODE IN A PROMPT. Veo reads "#C5DBE4" as text to
print and renders it into the picture. Name colours in plain words instead:
  electric cyan · hot bubblegum pink · warm honey gold · deep cocoa brown
  pale ice blue (the studio surface)
Shadows and outlines are deep cocoa brown, never pure black. Roughly: one
colour dominates 60-75% of frame, a second takes 15-25%, a third is a 3-5%
accent. Exact hex values are matched afterwards, in the grade, not by the
generator.

LIGHT — always hard directional light, stark contrast, one crisp well-defined
shadow with a sharp edge. This is the brand persona, not a style option.
Never soft, diffuse, overcast, hazy or moody.

BACKDROPS are always saturated brand colour or a real environment. Never grey,
never beige, never neutral studio seamless.

FORMAT unless told otherwise: vertical 9:16, 30fps, clean and uncluttered.

WRITE PROMPTS AS CINEMATIC PROSE, not keyword lists. Every prompt states, in
this order: shot and camera move, lens, subject and environment, light
direction and hardness, palette in plain colour words, and what the frame
deliberately keeps empty.

PHRASE EXCLUSIONS POSITIVELY. Naming a thing tends to summon it.
  "no people"      ->  "completely deserted"
  "no signage"     ->  "bare unmarked concrete"
  "no soft light"  ->  "harsh direct sun, sharp-edged shadows"
  "no grey"        ->  "richly saturated colour"

RESERVE SPACE. If a character or product is being composited in later, say so:
"the right third of the frame is open and completely unobstructed." If a
generation fills that space, regenerate it. Do not mask it out.
```

### Measured targets — sampled from the house shots, not guessed

Pulled from `assets/marketing/product-hero/` on 23 Aug 2026. Use these numbers to write prompts **and** to judge what comes back.

| | Gold wall | Pale surface | Cyan wall |
|---|---|---|---|
| `01-woas-nutella` | `#F5D286` | `#C5DBE4` | — |
| `03-woas-tri-chocolate` | `#FDDF59` | `#FFE366` | — |
| `09-very-very-strawberry` | — | `#FEDF70` | `#BAF5FE` |

> **The pale surface is ice blue `#C5DBE4`, not mint green.** Asking a generator for "soft mint" returns a saturated jade floor that looks nothing like the house shots.

**The exposure signature — this is the part everyone gets wrong.**

| Measure | House shots | Reject if |
|---|---|---|
| Mean luminance | **184–208** / 255 | below ~150 |
| Pixels under 60 luma | **0–5%** | above ~10% |

The WaffleUp look is **hard light *and* bright**. "Hard directional light" on its own reads to Veo as *dramatic*, and dramatic means big black shadows — the opposite of this brand. Always pair the light direction with an explicit brightness instruction and an explicit limit on how much frame the shadow may occupy.

**Two traps found the hard way, 23 Aug 2026:**

- **A hex code in the prompt gets rendered as text in the frame.** Veo printed `C5DBE4` into the bottom-left corner of a plate. Colours go in as words; exact values are matched later in the grade.
- **Naming a shadow on an empty set makes Veo invent an object to cast it.** Asking for "a small contained shadow" on a bare surface returned a dark blurry prop sitting on the floor. On an empty plate, state the light direction and let the shadow follow — never name the shadow as a thing.

**Veo output defaults:** 24fps, and 720×1280 on the cheaper tiers. Brand spec is 30fps / 1080×1920, so conform in CapCut and generate finals at the highest tier. Veo also writes an audio track — mute or detach it; brand audio is chosen separately.

---

## 2. THERE IS NO NEGATIVE FIELD

**Neither Flow nor the Gemini app has a negative prompt box.** Flow takes plain English in one prompt box and nothing else. Any instruction written as "no X" is being fed straight into the prompt, where it works against you — naming a thing tends to summon it.

So **every exclusion is written into the prose, phrased as something that IS true about the frame.**

| Instead of excluding | Write into the prompt |
|---|---|
| product, waffle, dessert, food | "a bare, clean, completely empty surface — an unoccupied set photographed before anything was placed on it" |
| people, crowds | "completely deserted" |
| characters, mascots | *(say nothing — don't plant the idea)* |
| text, signage, logos, watermarks | "a plain unmarked wall" · "bare unmarked concrete" |
| props, clutter | "a clean uninterrupted surface" |
| soft light, diffuse, overcast | "harsh direct light, one crisp sharp-edged shadow" |
| grey, beige, neutral, muted | "richly saturated colour, high contrast" |
| texture noise, grain | "smooth flawless paint" |
| camera shake, handheld | "locked off, perfectly steady" |

**The reserved-space trick.** When a character or product is being composited in later, don't describe the absence — describe the emptiness as deliberate: *"the right third of the frame is open and completely unobstructed."* If a generation fills it, regenerate. Never mask it out.

> If a tool you're using later *does* have a negative field, this is the block for it: `people, cartoon characters, mascots, food, waffles, text, logos, watermarks, packaging, soft diffuse lighting, grey and beige tones, lens flare, camera shake, low contrast`. Flow is not that tool.

---

## 3. The six things every prompt states

Non-negotiable. A prompt missing any of these comes back off-brand.

1. **Aspect + duration** — `vertical 9:16 · 8s`
2. **Camera** — lens feel, the move, locked vs handheld
3. **Light** — some form of *hard directional light, stark contrast, crisp shadow*
4. **Palette** — named in **words, never hex** (§1). Hex gets printed into the frame as text. Grade to the exact value in CapCut afterwards.
5. **Exclusions** — folded into the prose as positive statements (§2). There is no negative field anywhere.
6. **Compositing note** — which supplied file layers in afterwards, and where the frame is being kept empty for it

Worked examples: `programs/AI-PRODUCTION.md` §5 and `campaigns/2026-08-bhoppu-intro/prompts.md`.

---

## 4. Hard fences — these do not bend

| Never | Because |
|---|---|
| Generate the **logo** | `assets/logo/` — the white signature wave through the letterforms cannot survive a generator |
| Generate a **character** | `assets/characters/` — one character per piece, supplied PNG, unmodified |
| Feed a **character PNG into an image-to-video tool** | That generates new poses from his artwork, which is redrawing him. Motion comes from moving the *layer* in CapCut, never regenerating the art |
| Use Flow's **Ingredients to Video** with a character, the product, the logo or packaging | Same rule, specific feature. Ingredients works by generating new renders from the reference. Allowed only with stills Flow itself generated |
| Generate the **product** in a hero or claim position | AI gets the grid, the stick and the crumb wrong, and it is the one thing this audience knows by heart. Use `assets/marketing/product-hero/` |
| Generate **packaging** | Use the real files in `assets/marketing/packaging/` |
| Colour-match to `assets/marketing/packaging/BD BOX A.jpg` | That artwork is off-palette. The packaging is the thing that's wrong, not the palette |
| Write the words **"free"** or **"discount"** — any language, any channel | `CLAUDE.md` §3. If the customer could work out the taka value from the words on screen, rewrite it |
| Put a character in first-person dialogue | `brand/character-voices/` is unapproved. Characters appear; they don't speak |
| Generate an implied claim | "fastest delivery," "best in Bangladesh," anything health or nutrition |
| Put a delivery CTA on Chef's Table content | Chef's Table has no delivery |

---

## 5. Credit budgeting

Google AI Pro is roughly **1,000 credits/month**, and a 10s Veo 3.1 clip at Quality runs about **125 credits** — call it **~10 Quality clips, ~50 Fast, or ~100 Lite per month**, with clips capped at 8s. `[CONFIRM]` these against the counter in your own Flow account before planning a batch; third-party figures move.

How to spend it, in priority order:

1. **Draft every plate at Lite first.** Composition, framing and reserved space are all judgeable at Lite. Cheap iteration.
2. **Promote only the keeper to Quality.** One regeneration, not five.
3. **Generate longer than you need and trim.** Tail is free once generated.
4. **Half the social engine needs no AI at all.** SOUND ON, NOT-SO-FACTS and CAUGHT CRISPY never touch a generator (`programs/SOCIAL-ENGINE.md` §7). Don't burn credits on formats that are cheaper and better on a phone.

A three-plate reel like `campaigns/2026-08-bhoppu-intro/` costs roughly 3 Lite drafts plus 3 Quality finals.

---

## 6. Handing work back

Plates come out of Flow into `output/<campaign-slug>/`, named to match the shot list — `plate-a.mp4`, `plate-b.mp4`. Then tell Claude which ones landed and which need a rewrite. Claude rewrites the prompt; it does not guess from the filename.
