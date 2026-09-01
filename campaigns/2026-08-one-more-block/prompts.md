# One More Block — generation prompts

**Route: image-to-video with character references.** Approved by Jawat 31 Aug 2026; the canon in
`programs/AI-PRODUCTION.md` §0/§2/§6, `CLAUDE.md` §5 and the brand book now say the same thing.

---

## 1. The pipeline, in order

| # | Step | Tool | Notes |
|---|---|---|---|
| 1 | **Voices** | ElevenLabs | ✅ done. This is the master clock — everything cuts to it. |
| 2 | **Reference kit** | — | ✅ done, in `refs/`. Same identity sheet on every shot for that character. |
| 3 | **Generate each shot** | Higgsfield / Flow / Kling | 3–4s per clip, draft quality, 2–3 takes each. |
| 4 | **Cull on the last frame** | eye | Design drifts *inside* a clip. If the last frame is off-model, bin it. |
| 5 | **Promote keepers** | same tool | Re-run only the ones you're keeping at full quality. |
| 6 | **Assemble to the audio** | CapCut | Audio on the timeline first, picture cut to it. |
| 7 | **Grade to palette** | CapCut | Pull back from the warm/magenta drift. Cocoa for shadows, never black. |
| 8 | **Composite the fixed bits** | CapCut | Logo, end card, captions. These are never generated. |

**Where the money goes:** step 3 at draft, step 5 for keepers only. Don't generate anything at
full quality until you've seen it move.

---

## 2. Audio — no, don't attach it

**Do not feed the ElevenLabs track into the video generator.** Two separate reasons:

- **Image-to-video tools don't take audio as a driver.** There's nothing for it to do. It either
  ignores the file or refuses it.
- **Veo 3.x generates its own audio** — ambience, footsteps, sometimes speech. That will fight
  your track. **Mute or discard every generated audio stream** and keep only ElevenLabs.

Audio's job is step 6, not step 3. Lay it down first and cut picture to it; the timings in
`shotlist.md` are the audio and they are the master.

**On lip sync:** you don't need it. At phone size, in a 20-second reel, the cut and the caption do
the attribution work — the audience knows who's talking because of who's on screen. The prompts
below say *"talking as he walks"* so the mouth is active for roughly the right length, and that's
enough. If you later want real sync, it's a separate lip-sync pass run on the finished clip, after
the edit — not something the video generator does.

---

## 3. What changed in the prompts

Every character shot now carries two locked blocks, verbatim, because consistency is the thing
that breaks:

- **A design lock** — the character's exact colours and parts, spelled out, so the model has
  something to hold onto besides the reference image.
- **A palette lock** — the four brand colours named in words, stated as holding steady across
  the shot.

Both are phrased as **what IS true**, never as "don't change X" — naming a fault tends to summon
it (`GEMINI.md` §2).

---

## 4. Shots

Vertical 9:16, 30fps. Generate 4s, trim to the audio.

---

### SHOT 1 · 0.0 – 3.2 · Air Maxi leads
**Attach:** `ref-air-maxi-identity.jpg` · `ref-style.jpg` · `ref-box-blurred.jpg`

```
A flat-colour cartoon character in bold vector style walks briskly toward camera
down a narrow deserted South Asian side street at night, talking as he walks and
glancing forward, chin up, arms swinging, energetic and confident. The camera
tracks smoothly backward ahead of him, holding him centre-right of frame.

His design, proportions, outline weight and colours are identical to the
reference images and stay identical in every frame: a hot pink curl mass with
long upright ears, a warm honey gold face and hands, cyan headphones worn under
the ears, a deep cocoa brown varsity jacket with gold lettering, hot pink
joggers, chunky pink and white sneakers, and a gold brush tail. Flat vector
fills with thick deep cocoa brown outlines throughout — the same jacket, the
same headphones, the same shoes from the first frame to the last.

Wet asphalt reflects a single hard overhead lamp and a cyan neon spill from a
shuttered shopfront, both from the upper left, throwing one crisp sharp-edged
shadow. Deep in the far background, well out of focus, a warm-lit food counter
with an indistinct branded box on it.

The palette holds steady across the whole shot: saturated electric cyan, hot
bubblegum pink, warm honey gold, and deep cocoa brown for every outline and
shadow. Shot on 35mm, eye level, high contrast, richly saturated. Vertical 9:16.
```

---

### SHOT 2 · 3.2 – 7.3 · Bhoppu trails
**Attach:** `ref-bhoppu-identity.jpg` · `ref-style.jpg`

```
A flat-colour cartoon character in bold vector style trudges heavily along a
deserted South Asian side street at night, talking as he walks, leaning back to
counterweight his belly, shoulders rolling, visibly out of breath. The camera
pushes in very slowly at chest height.

His design, proportions, outline weight and colours are identical to the
reference images and stay identical in every frame: a large round electric cyan
bear, a hot pink tracksuit jacket with a warm honey gold W on the chest, a gold
headband, hot pink shorts patterned with small gold triangles, and gold-cream
shoes. Flat vector fills with thick deep cocoa brown outlines throughout — the
same tracksuit, the same headband, the same shoes from the first frame to the
last.

A low kerb and wet asphalt run across the lower third; behind him shuttered
storefronts and overhead cables fall out of focus. Hard directional light from a
single overhead lamp at upper left casts one sharp shadow beneath him.

The palette holds steady across the whole shot: saturated electric cyan, hot
bubblegum pink, warm honey gold, and deep cocoa brown for every outline and
shadow. Shot on 35mm, eye level, very slow push in, high contrast. Vertical 9:16.
```

---

### SHOT 3 · 7.3 – 9.8 · Air Maxi looks back
**Attach:** `ref-air-maxi-identity.jpg` · `ref-style.jpg`

```
A flat-colour cartoon character in bold vector style walks away from camera down
a deserted South Asian side street at night, then turns his head back over his
shoulder and grins, talking, still walking. The camera drifts slowly backward
with him.

His design, proportions, outline weight and colours are identical to the
reference images and stay identical in every frame, including through the head
turn: a hot pink curl mass with long upright ears, a warm honey gold face, cyan
headphones worn under the ears, a deep cocoa brown varsity jacket with gold
lettering, hot pink joggers, chunky pink and white sneakers, and a gold brush
tail. Flat vector fills with thick deep cocoa brown outlines throughout.

The street narrows into the distance, lit by a receding line of hard overhead
lamps each throwing one sharp shadow.

The palette holds steady across the whole shot: saturated electric cyan neon far
down the street, hot bubblegum pink, warm honey gold lamplight, and deep cocoa
brown for every outline and shadow. Shot on 28mm, slightly low angle, smooth
continuous movement, high contrast. Vertical 9:16.
```

> The head turn is the whole shot and the hardest thing here. If the face won't hold through it,
> split: generate the walk-away, generate a separate 2s turn, cut between them.

---

### SHOT 4 · 9.8 – 14.4 · Bhoppu and the reason
**Attach:** `ref-bhoppu-identity.jpg` · `ref-style.jpg` · `ref-stick.jpg`

```
A flat-colour cartoon character in bold vector style walks along a deserted South
Asian side street at night holding up a square waffle on a flat wooden stick,
talking and looking at it happily as he walks. The camera tracks alongside him at
walking pace, the near kerb sliding past quickly while the background drifts
slowly behind — strong depth separation.

His design, proportions, outline weight and colours are identical to the
reference images and stay identical in every frame: a large round electric cyan
bear, a hot pink tracksuit jacket with a warm honey gold W on the chest, a gold
headband, hot pink shorts patterned with small gold triangles, and gold-cream
shoes. Flat vector fills with thick deep cocoa brown outlines throughout.

The waffle is square with a deep even grid, warm honey gold, on a plain flat
wooden stick — the same shape and the same grid in every frame.

Hard directional lamplight from the upper left, one crisp shadow. The palette
holds steady across the whole shot: saturated electric cyan, hot bubblegum pink,
warm honey gold, and deep cocoa brown for every outline and shadow. Shot on 35mm,
eye level, smooth steady tracking, high contrast. Vertical 9:16.
```

> If the waffle comes back round, soggy or with a wrong grid, generate his hand empty and
> composite a real one from `assets/marketing/product-hero/`. The product is the one thing this
> audience knows by heart.

---

### SHOT 5 · 15.0 – 17.4 · Mr Waffle, still
**Attach:** `ref-mr-waffle-identity.jpg` · `ref-style.jpg` · `ref-box-blurred.jpg`

```
A flat-colour cartoon character in bold vector style hovers motionless just above
the ground in front of a brightly lit open serving hatch on a deserted street at
night, speaking two short calm lines. He floats, perfectly still, with only the
faintest drift — his feet hang clear of the ground and stay clear.

His design, proportions, outline weight and colours are identical to the
reference images and stay identical in every frame: a square warm honey gold
waffle grid body with one bite missing from the top corner, a hot pink glaze
dripping over the top edge, round dark sunglasses, electric cyan arms and legs,
and hot pink and white sneakers. Flat vector fills with thick deep cocoa brown
outlines throughout.

Warm honey gold light floods from the hatch and spills across the ground in one
hard-edged pool beneath him. On the counter behind, well out of focus, an
indistinct branded box. The camera is locked off and absolutely still.

The palette holds steady across the whole shot: saturated electric cyan night air
at the edges, hot bubblegum pink, warm honey gold light pool, and deep cocoa
brown for every outline and shadow. Shot on 50mm, eye level, high contrast.
Vertical 9:16.
```

> **He must not bob or walk.** Everything before this shot moves; this one stops dead. That
> contrast is the joke landing. If the model gives him a walk cycle, regenerate.

---

### SHOT 6 · 17.4 – 19.6 · the crunch
**Attach:** `ref-stick.jpg`

```
Extreme close-up, locked off, of a square waffle on a flat wooden stick held
against a flat richly saturated hot bubblegum pink surface, lit by hard
directional light from the left throwing one crisp sharp-edged shadow. A slow
lateral drift across the frame. The waffle is warm honey gold with a deep even
grid, the same shape in every frame. Deep cocoa brown outlines and shadow.
Vertical 9:16.
```

End card cuts in at ~18.2s. **Composited, not generated** — `assets/logo/Waffle Up Logo - RBG.png`
over a flat pink field, with the crunch landing on the cut.

---

## 5. The reference kit — `refs/`

| File | What it locks | Attach to |
|---|---|---|
| `ref-air-maxi-identity.jpg` | Face, ears, tail, jacket — three angles | 1, 3 |
| `ref-bhoppu-identity.jpg` | Mass, headband, tracksuit — three angles | 2, 4 |
| `ref-mr-waffle-identity.jpg` | Grid, shades, bite, drip — three angles | 5 |
| `ref-style.jpg` | Line weight, outline colour, flat-fill language | every character shot |
| `ref-stick.jpg` | The real branded stick, photographed | 4, 6 |
| `ref-box-blurred.jpg` | Real boxes defocused behind the product | 1, 5 |
| `ref-box-sharp.jpg` | The real box in focus | only if a box must read |

**The packaging palette trap.** The real box art prints hotter magenta and mint green than the
brand palette, and its printed characters are superseded designs. Keep any box defocused, and
grade back afterwards. **`ref-stick.jpg` is the safe brand cue** — clean, on-palette, nothing to
drift.

**Never ask for the logo.** The signature wave through the letterforms is what generators destroy.
Keep it small and genuinely out of focus, or leave the space clean and composite the real file.

---

## 6. Fallback

Any shot that won't hold reverts to the old route: generate the street **empty** with the
character's space reserved, composite the approved PNG in CapCut, and bob the layer 2–4px.
`programs/AI-PRODUCTION.md` §6 has the technique. Shot 5 falls back most easily — Mr Waffle
doesn't move anyway.
