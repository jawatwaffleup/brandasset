# The Waffle Up Gang

The characters are WaffleUp-owned brand artwork. Use supplied files only: do not redraw, recolour, restyle, or generate a new pose.

## Bangladesh — the canonical nine

**There are ten canonical characters, universally** — the nine below plus Merlulu. The folder names are the stable identifiers used by this kit; `bangladesh/` and `singapore/` are **historical folder names**, not market restrictions. *(Roster unified 24 Aug 2026 — see `brand/CHARACTER-BIBLE.md`.)*

| Character | Identifier | Approved Surprise Card description | Included art |
|---|---|---|---|
| Mr Waffle | `mr-waffle` | The original trendsetter of the waffle world! With a drizzle of style and a splash of sass, he's here to prove that breakfast can be the highlight of any day. “Stay crispy, stay cool!” | 2D art + 3D model |
| Air Maxi | `air-maxi` | The beat of the street! With his paw on the pulse of the latest trends, he's the go-to guy for all things trendy in the city. | 2D art + 3D model |
| Bhoppu | `bhoppu` | He has a knack for finding those elevated spots where waffles seem extra flavourful. Some say it's his natural zest for life; others think there's a secret ingredient. | 2D art + 3D model |
| Picchi | `picchi` | With a flair for vibrant colors and a head full of curly dreams, Picchi dances through life, sprinkling joy everywhere. Believing every day is a celebration waiting to happen, Picchi spreads happiness with every step. | 2D art + 3D model |
| Stovy | `stovy` | The mastermind behind every crispy edge and fluffy center. When waffles need an upgrade, Stovy turns up the heat! Some say his technique is unparalleled; others believe he whispers to the batter. | 2D art |
| Swirly | `swirly` | While wild colors meet wildlife flavors, don't be fooled by Swirly's zany appearance; there's nothing more serious than our commitment to satisfy those late-night waffle whims. Dare to taste the swirl? | 2D art |
| Tvy | `tvy` | Retro vibes and crispy delights! Tvy is here to rewind you back to the golden era while you munch on our cosmic waffles. No breakfast? No worries! We're open till late at night. | 2D art |
| Spacy | `spacy` | From the Milky Waffle Way, Spacy brings you the cosmic delight of crispy edges and fluffy centers. Dive into a galactic treat with us, open till late night! | 2D art |
| Icy | `icy` | Swirling with cool colors and bursting with dynamic energy, Icy knows how to make a splash! Always the life of the party, Icy turns any ordinary day into a refreshing adventure. | 2D art |

`assets/characters/bangladesh/lineup.png` is the group reference.

## Merlulu — the tenth character

Merlulu joins the nine above, making the **ten-character universal roster**. **Approved Surprise Card description:** Boldly be playful, Merlulu loves making worlds together. Just like a lion and a fish! No wonder he's a fan of Waffle Up's bold flavors with a smooth twist. **Pronouns: he/him**, confirmed by Jawat 24 Aug 2026 — the next Surprise Card print batch carries "he" and the redesigned Merlulu look. **The "never with the Bangladesh nine" rule is void** as of 24 Aug 2026: Merlulu appears anywhere the other nine do.

The descriptions above are transcribed from `assets/Surprise Cards/Character Cards/`; `data/characters.json` is the machine-readable source of truth.

## Asset structure

```text
assets/characters/
├── bangladesh/
│   ├── lineup.png
│   └── {mr-waffle,air-maxi,bhoppu,picchi,stovy,swirly,tvy,spacy,icy}/
│       ├── 2d/                 hero, expression, card and available T-pose art
│       └── 3d/model.stl        only Mr Waffle, Air Maxi, Bhoppu and Picchi
├── singapore/merlulu/
│   ├── print/character-card.eps
│   └── references/             SG sticker-sheet source and preview art
```

This is the complete character library. There are no legacy duplicate character folders or secondary characters in the kit.

## 3D models

Only four printable 3D models are included. They are source `.stl` files and need suitable 3D software or a slicer; they are not browser-viewable images.

| Character | Model path | Reference image |
|---|---|---|
| Mr Waffle | `bangladesh/mr-waffle/3d/model.stl` | `model-reference.jpg` |
| Air Maxi | `bangladesh/air-maxi/3d/model.stl` | `model-reference.jpg` |
| Bhoppu | `bangladesh/bhoppu/3d/model.stl` | use the 2D hero image |
| Picchi | `bangladesh/picchi/3d/model.stl` | `model-reference.jpg` |

T-pose artwork in the 2D folders is animation reference art. It does not mean a printable 3D model exists.

## Source-name aliases

The Takeout source uses inconsistent spellings. This kit standardises the public names requested above: `Stovie` → **Stovy**, `TV`/`Tvy` → **Tvy**, and `Spacie`/`Spacy` → **Spacy**. File names inside the legacy folders are unchanged; use the new character folders for normal work.

## Usage rules

- Use one character per screen or campaign piece, full-colour and unmodified.
- Use characters for positive moments, achievements and product storytelling—not errors, payroll, discipline or dense data views.
- **Character treatments are no longer market-specific** (changed 24 Aug 2026). Market-specific rules still apply to **pricing, outlets and delivery CTAs** — see `CLAUDE.md` §2.
- If a pose is unavailable, request approved artwork. Do not fabricate one.
