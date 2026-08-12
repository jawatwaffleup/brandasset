# The Waffle Up Gang

## Where they came from

**The characters were created by the founder, Mohammad Salman, himself.** They were formalised later — the polished vector art, the rigs and the pose libraries were produced with outside help, likely freelance.

The website describes them as *"exclusive character designs by a renowned French-Australian artist"* and says they *"add a unique visual charm, reflecting the vibrant, fun essence of Waffle Up… This creative touch sets us apart and enhances our global brand appeal."* Treat that as the public-facing framing of the formalisation stage, not the origin.

**Why this matters practically:** founder-originated characters are almost certainly WaffleUp-owned, which removes the main legal question hanging over automating character content. Confirm the terms of the freelance work before building on the source files, but the outlook is good.

They are the brand's personality layer — the one thing no competitor can copy. Use them in internal tools too.

---

## The core nine

The canonical roster is the numbered set in `Animation (Tasnim)/3D Characters/` — these nine have full rigs: main pose, T-poses (front / back / profile), hoodie variants, four-plus extra poses, expression sheets, and Moho animation files. If a character has a number, it's official.

| # | Character | What it actually is | Personality | Art |
|---|---|---|---|---|
| 1 | **Bhoppu** | Big cyan **bear** in a pink-and-cocoa tracksuit, sweatband with a W, dumbbell in one paw and a waffle in the other | Food *and* fitness; enjoys the contrasts in everything | `hero/bhoppu.png` |
| 2 | **Air Maxi** | Bear-eared kid with **pink curly hair**, headphones, and a tan "AIR MAX" varsity jacket over pink cargos | Trendsetter. It takes one to know one | `hero/air-maxi.png` |
| 3 | **Picchi** | Small kid, **pink curly hair**, freckles, cyan W-onesie and pink sneakers | Very sweet; will share his waffles if you ask nicely | `hero/picchi.png` |
| 4 | **Swirly** | A **candy-swirl bear** — cyan and pink barber-pole stripes, mouth wide open, tongue out | Always twirling around trying to make you smile | `hero/swirly.png` |
| 5 | **Mr. Waffle** | An actual **waffle square** with round sunglasses, pink frosting-and-sprinkle drip on top, cyan arms, pink hi-tops, thumbs up | Romantic; found love in every bite | `hero/mr-waffle.png` |
| 6 | **Icy** | A **popsicle/ice-lolly** with a melting cyan-and-pink coat on a WaffleUp stick | The cold-drinks character | `hero/icy.png` |
| 7 | **TV** | A **cyan television set** with antennae, X-taped eyes and a pixel grin, giving a thumbs up | The prop/mascot; graffiti-pose variant exists | `hero/tv.png` |
| 8 | **Stovie** | The **waffle oven** itself — cyan WaffleUp-branded machine, open mouth-drawer with a waffle inside | Loves everything warm and ooey-gooey | `hero/stovie.png` |
| 9 | **Spacie** | Kid in a **pink-and-cyan space helmet**, floating, throwing a peace sign, W on the chest | The dreamer/explorer of the set | `hero/spacie.png` |

Group shot: `reference/waffle-up-gang-family.png` — all nine in one banner, the definitive lineup.

## Secondary — 2D card art only

These appear on the character cards but have **no 3D rig**, so poses can't be generated. Use as-is or not at all.

| Character | What it is | Note |
|---|---|---|
| **Bubbly** | Bear with a Nutella/caramel drip poured over its head | Signature item: Bananatela |
| **Sweety** | A **sundae glass** topped with pink "sweet" drip | Not a person — a dessert object |
| **Chachhu Sam** | Older gentleman: straw hat, moustache, pink curls, striped shirt | Fusion-food explorer; "Chachhu" = uncle. Bangla Pizza |
| **ZZZ** | A little house with a pink roof, door ajar | The "always sleeping" one from the brand guideline |
| **Lazy Squirrel** | Same swirl-striped body as Swirly | Likely an early or alternate name for Swirly — confirm with design before using |

Card art: `cards/*.png` — each is the character on a cyan / pink / gold plaque with its name in CHUM.

## Market variant — Singapore

The Singapore sticker sheets introduce **Merlulu** — a pink-maned Merlion with sunglasses and a gold W medallion, drawn in the same line style. The name is confirmed by the Surprise Card artwork: `Batch 11 (May 26)/Character Card/Character Card - Merlulu.eps`, where Merlulu joins the nine as a tenth collectible card. Not part of the BD roster. See `reference/sg-sticker-sheet-*.jpg`.

The SG sheets also run a **softer, more pastel palette** than the Bangladesh artwork — worth noting if you ever build anything market-specific.

---

## What's in this kit

```
assets/characters/
├── hero/          full-colour master render per character + T-pose fronts
├── expressions/   facial/expression sheets (line art, 3-5 expressions each)
├── cards/         2D character cards on coloured plaques
└── reference/     full gang lineup, first-draft lineup, SG sticker sheets
```

Not copied in (too large / source formats) — go to the drive for these:

- `Animation (Tasnim)/3D Characters/` — Moho rigs, T-poses back and profile, hoodie variants, Extra Poses 1–5, seasonal sets (Eid, Christmas, V-Day, 26th March, 16 December), `.psd` and `.ai` sources
- `Characters 3D (China)/` — **`.stl` 3D print models** and T-pose refs for Air Maxi, Bhoppu, Mr. Waffle, Picchi
- `Merch/WUP Character Sticker (BD|SG)/` — sticker sheet vectors
- `Event Materials/.../WUP Character Cutout/` — life-size standee artwork

## Using characters in software

**Do**

- **One character per outlet.** Gives each team an identity in a multi-outlet dashboard — "Banani's Mr. Waffle is on a 12-day streak." Mapping below.
- **Use them for achievement and completion moments** — closing checklist done, zero-wastage day, perfect stock count. Same place the Jester voice lives.
- **Use the expression sheets as state icons.** They're already line art, already single-colour: happy for a clean count, shocked for a stock-out, angry for an overdue checklist. Cheaper and more on-brand than a generic icon set.
- **Pair a character with its matching product.** Icy on beverages, Stovie on manufacturing/commissary, Mr. Waffle on the waffle SKUs. Object characters map to modules almost too neatly — use that.
- Keep them full-colour on cyan, pink, gold or white fields.

**Don't**

- **Don't recolour, restyle, redraw, or AI-generate new poses.** These are commissioned work. If a pose doesn't exist, ask design — there are already 40+ poses on the drive, so it probably does.
- Don't use characters in error states, financial screens, payroll, or anything disciplinary. A cartoon next to someone's salary reads as mockery.
- Don't crowd them into dense data views. One character per screen, maximum.
- Don't shrink below ~48px — the line weight collapses.
- Don't mix the BD and SG palettes in one layout.

## Suggested outlet ↔ character mapping

A starting point, not a mandate — pick with the outlet teams so they feel ownership. Mirrored in `data/outlets.json`.

| Outlet | `outlet_id` | Character | Why |
|---|---|---|---|
| Banani (first outlet) | `WUP-FS-01` | **Mr. Waffle** | The original; the waffle itself |
| Dhanmondi (flagship) | `WUP-FS-02` | **Bhoppu** | The biggest presence for the biggest store |
| Gulshan 1 | `WUP-FS-03` | **Air Maxi** | Trendsetter for the trend-forward area |
| Bailey Road | `WUP-FS-04` | **Picchi** | — |
| Bashundhara R/A | `WUP-FS-05` | **Swirly** | — |
| Uttara | `WUP-FS-06` | **Spacie** | — |
| Sylhet Zindabazar | `WUP-FS-07` | **Chachhu Sam** ⚠ | — |
| Chattogram | `WUP-FS-08` | **Bubbly** ⚠ | — |
| Chef's Table ×4 | `WUP-FC-01…04` | **TV** | The co-brand, the broadcast |
| Cloud kitchens | `WUP-CK-…` | **Stovie** | Pure production, no storefront |
| Beverages module | — | **Icy** | — |
| Singapore | `SG-CQ` | **Merlulu** | Market-specific |

> ⚠ **Chachhu Sam and Bubbly are not in the nine rigged characters.** The canonical roster with full Moho rigs is Bhoppu, Air Maxi, Picchi, Swirly, Mr. Waffle, Icy, TV, Stovie, Spacie — plus Merlulu for Singapore. Chachhu Sam and Bubbly exist as flat art only, so a screen or animation that needs a pose for Sylhet or Chattogram will find nothing. Either commission rigs for them, or reassign those two outlets to rigged characters. Flagged as an open question in `data/outlets.json`.

> **Two outlets have no site to brand.** `WUP-CK-05` Rampura is *opening soon* and `WUP-CK-01`/`WUP-CK-02` are discontinued — don't render a character card for a site that isn't trading. Filter on `status`.

## Drive filenames vs. proper names

The drive uses shortened spellings. Map them:

| Proper name | Appears on the drive as |
|---|---|
| Air Maxi | `Air maxi`, `Maxy`, `Air maxy` |
| Bhoppu | `Bhoopu`, `bopu` |
| Icy | `Popsicle`, `popsicle final` |
| Stovie | `Stovy`, `Stovie Wonders` |
| Spacie | `Spacy` |
| TV | `Tvy`, `TVy final` |
| Swirly | `Swirly Wirly` |
| Chachhu Sam | `Chacchu sam`, `Chachhu Sam` |
| Merlulu | on Surprise Card Batch 11 only |

Use the proper names in all software and copy.
