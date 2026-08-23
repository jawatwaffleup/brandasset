# WaffleUp — Brand System Reference

**Purpose of this file.** Single source of truth for every internal tool built in this project folder (POS, inventory, manufacturing, opening/closing SOPs, dashboards). Anything I build should read from here so all WaffleUp software looks and sounds like WaffleUp.

Last verified: 11 Aug 2026 · Sources: `[WUP-01] Brand Assets`, `Waffle Up Brand Book V.1.pdf`, `WUP Brand Guideline_1.pdf` (Lamiya, 2023), `WaffleUp Profile — Edited 7 Feb 2024.pdf`, waffleup.global

---

## 1. Company

| | |
|---|---|
| Legal entity | Waffle Up Global PTE Ltd. |
| Registered | 33A Pagoda Street, Singapore 059192 |
| BD address | Road 11, House 67/C, Block E, Banani, Dhaka-1213 |
| Founded | 2021 (Singapore) · 1st outlet Banani, Dhaka — **16 Dec 2021** |
| Founder story | Mohammad Salman saw a streetside waffle truck in the USA; brought "waffles on a stick" to Dhaka, where waffles were a luxury restaurant dessert sold in sets of four |
| Category | QSR / food-tech startup — largest & fastest-growing waffle chain in Bangladesh |
| Scale (2023–24 profile) | 12 outlets + 3 cloud kitchens · ~8,000 waffles/day · ~38,000 orders/month · 100+ team · BDT 180M revenue (2023) |
| Scale (verified Aug 2026) | **15 trading sites**: 8 standard outlets · 4 Chef's Table · 2 cloud kitchens live · 1 Singapore. Foodpanda alone: 8,809 delivered orders and BDT 4.5M GMV in Jul 2026, AOV 511. |
| Handles | @waffleup.online (IG / FB / TikTok) · waffleup.global |
| Orders | +880 1958 095887 (WhatsApp) |

### Purpose, mission, vision
- **Purpose** — Redefine waffles as a delectable street food dessert.
- **Mission** — *Offering innovative, delicious and premium products in a joyful, welcoming environment that brings people together and creates memories.*
- **Vision — the three R's:** **Reimagine** (the consumer experience, fusion products) → **Redefine** (waffles as street food; products and *procedures*) → **Revolutionize** (processes, for global scalability).

> The vision explicitly names **procedures and processes**, not just product. Ops automation work is on-brand vision work, not back-office overhead — frame internal tools that way.

### Value pillars
Brand guideline: **Quality · Joy · Community · Innovation**
Company profile: **Quality · Speed · Access · Innovation**
Use the union in internal tooling copy: *Quality, Speed, Joy, Access, Community, Innovation.*

### Audience
Primary 10–25, upper class; secondary 26–35, upper-middle. Urban and prime hubs.

### Taglines / signature lines
- **SQUARE IS THE NEW HEART** (primary tagline)
- *Ashol WaffleUp Chinun* (আসল ওয়াফলআপ চিনুন) — Bangla authenticity line on menus
- *Every Waffle Day* · *For immediate consumption* (packaging)
- Typography set: Waffleistic, Sweeeet, Obsessed, Drizzled with Love, Waffle Love, Crispy, Crunch Up, Smile, Order Now, Everyday, Ashol, Halal

---

## 2. Voice & tone

**Archetype: the Jester.** Casual · friendly · humorous.

- Lighthearted, irreverent, unexpected. Puns, jokes and wordplay are explicitly encouraged.
- Product copy is sensory and a little over the top — "Death by Nutella… RIP.", "a fusion of fresh banana, nutella, maple syrup and nuts to party with your taste buds."
- Bangla/English code-switching is on-brand (*Ashol WaffleUp Chinun*, *Bangla Pizza*).
- Never corporate-stiff, never apologetic, never luxury-precious — the whole brand exists to de-luxury the waffle.

**Applying Jester to internal tools:** keep labels plain and functional (staff need speed), but let empty states, confirmations, streaks and success messages carry the humour. A closing checklist that says "Shutter down. Go home, legend." is on-brand. A stock alert that says "Nutella is running dry 😬" is on-brand. Error and compliance messaging stays clear and literal.

---

## 3. Colour

### Current palette (authoritative — `[WUP-01-04] Color Code`)

| Role | RGB / Digital | CMYK-safe (print) | Pantone | Name |
|---|---|---|---|---|
| **Primary — Cyan** | `#0BF9F6` | `#70CBD3` (C53 M0 Y15 K0) | 3255 C | WaffleUp Cyan |
| **Primary — Pink** | `#FF629B` | `#F0629A` (C0 M77 Y7 K0) | 212 C | WaffleUp Pink |
| **Secondary — Yellow** | `#FFD56D` | `#FFD76D` (C0 M15 Y68 K0) | 1215 C | Waffle Gold |
| **Secondary — Deep Cocoa** | `#450001` | `#3F1212` (C47 M85 Y76 K71) | 4975 C | Cocoa / ink |

Neutrals: pure **white `#FFFFFF`** is a real part of the system (the signature wave, logo outlines, card surfaces). Deep Cocoa `#450001` is the **text/ink colour — do not use pure black**.

*Legacy note:* the 2022 Brand Book V.1 lists `#6DCBD8 / #F0639A / #FFD66D / #3E1312`. Those are superseded by the table above; treat old-file colours as the print-CMYK line.

### Usage ratio (from the brand guideline)
**60–75%** dominant colour · **15–25%** secondary · **3–5%** each for up to two accents.
In practice: pick cyan *or* pink as the field, the other as the counterpoint, yellow as the highlight, cocoa as ink.

### Photo & video colour rules
- Backdrops must follow the brand colour codes — no off-brand backgrounds.
- **Hard light, stark contrast** — that's the brand persona.
- Video: triadic colour grading with `#6DCBD8` and `#F0639A` dominating; 30 fps.

---

## 4. Logo, symbol, icon

**Logo** — "WAFFLE" in cyan with the white **signature wave** running through it, "UP" in pink with the wave, all inside a **Waffle Gold rounded plaque with a Deep Cocoa outline**, ® mark top-right. Files: `[WUP-01-01] Logo/Waffle Up Logo - RBG.png|.eps` (digital) and `- CMYK` (print).

**Brand symbol** — the **W** monogram in a Waffle Gold circle with cocoa outline. Files: `[WUP-01-02] Symbol`.

**Icon** — app/social mark, 6 variants: `rbg`, `rbg-Social`, `cmyk`, `red`, `white` (.ai + .png) in `[WUP-01-03] Icon`. **Use `Icon (white)` on coloured fields and `Icon (rbg)` on white.**

### Do
- Even spacing in all directions (clearspace).
- The **signature wave must always be present** inside the letterforms.
- Correct colourisation maintained across every medium and channel.

### Don't
- Uneven spacing or cropped-out corners.
- Solid-coloured letters without the signature wave.
- Single-coloured letters without the signature wave.
- (Implied) Don't recolour, stretch, rotate, or drop the ® / plaque.

**Brand pattern** — organic flowing wave-blobs of cyan, pink and gold on white, with scattered white dots/bubbles. This wave-blob divide (cyan top / pink bottom, or diagonal) is *the* WaffleUp layout device. Use it for headers, splash screens, receipt headers, login screens.

---

## 5. Typography

Font files: `[WUP-01-05] Fonts` — `01 chum` · `02 futura` · `03 ultra` · `04 bebas-neue` · `05 puffin-display` · `06 general-sans`

| Role | Typeface | Notes |
|---|---|---|
| Display / hero | **CHUM** | The chunky rounded lowercase-look display face — "brand identity", "archetype & tone", section headers |
| Headline / product names | **Futura Extra Bold** | Set in caps, often with cocoa drop shadow + white outline |
| Condensed / labels | **Bebas Neue** | Caps, tight, for tickers, prices, small caps labels |
| Also licensed | Ultra, Puffin Display, General Sans | General Sans is the practical UI/body face for screens |

**Layered text effect (from the guideline):** every hero word is built in four layers — **Background → Drop Shadow → Outline → Text**. Reproduce with `text-shadow` / `-webkit-text-stroke` in web UIs.

**For software UI (my recommendation, consistent with the above):**
- UI/body: **General Sans** (already licensed; falls back cleanly to system sans)
- Numbers in POS/dashboards: General Sans tabular figures or Bebas Neue for large KPI numerals
- Reserve CHUM and Futura Extra Bold for headers, splash screens, printed receipts and staff-facing celebration moments — not for dense data.

---

## 6. Characters — "The Waffle Up Gang"

**Created by founder Mohammad Salman**, then formalised into polished vector art and animation rigs with outside (likely freelance) help — the website's "renowned French-Australian artist" line describes that later stage. **Bangladesh has exactly nine canonical characters:** Mr Waffle, Air Maxi, Bhoppu, Picchi, Stovy, Swirly, Tvy, Spacy and Icy.

| # | Character | What it is | Approved Surprise Card description |
|---|---|---|---|
| 1 | **Bhoppu** | Cyan bear in a pink tracksuit, dumbbell + waffle | He has a knack for finding those elevated spots where waffles seem extra flavourful. Some say it's his natural zest for life; others think there's a secret ingredient. |
| 2 | **Air Maxi** | Pink-curled kid, headphones, "AIR MAX" varsity jacket | The beat of the street! With his paw on the pulse of the latest trends, he's the go-to guy for all things trendy in the city. |
| 3 | **Picchi** | Small freckled kid in a cyan W-onesie | With a flair for vibrant colors and a head full of curly dreams, Picchi dances through life, sprinkling joy everywhere. Believing every day is a celebration waiting to happen, Picchi spreads happiness with every step. |
| 4 | **Swirly** | Candy-swirl striped bear, tongue out | While wild colors meet wildlife flavors, don't be fooled by Swirly's zany appearance; there's nothing more serious than our commitment to satisfy those late-night waffle whims. Dare to taste the swirl? |
| 5 | **Mr Waffle** | An actual waffle square in sunglasses and hi-tops | The original trendsetter of the waffle world! With a drizzle of style and a splash of sass, he's here to prove that breakfast can be the highlight of any day. “Stay crispy, stay cool!” |
| 6 | **Icy** | A melting popsicle on a WaffleUp stick | Swirling with cool colors and bursting with dynamic energy, Icy knows how to make a splash! Always the life of the party, Icy turns any ordinary day into a refreshing adventure. |
| 7 | **Tvy** | Cyan television with antennae and a pixel grin | Retro vibes and crispy delights! Tvy is here to rewind you back to the golden era while you munch on our cosmic waffles. No breakfast? No worries! We're open till late at night. |
| 8 | **Stovy** | The WaffleUp waffle oven itself | The mastermind behind every crispy edge and fluffy center. When waffles need an upgrade, Stovy turns up the heat! Some say his technique is unparalleled; others believe he whispers to the batter. |
| 9 | **Spacy** | Kid in a pink-and-cyan space helmet, floating | From the Milky Waffle Way, Spacy brings you the cosmic delight of crispy edges and fluffy centers. Dive into a galactic treat with us, open till late night! |

**Singapore variant: Merlulu** — a pink-maned Merlion with a gold W medallion. Singapore therefore has ten characters: the Bangladesh nine plus Merlulu. Its approved Surprise Card description is: “Boldly be playful, Merlulu loves making worlds together. Just like a lion and a fish! No wonder she's a fan of Waffle Up's bold flavors with a smooth twist.” On the SG sticker sheets, and as a tenth Surprise Card character in Batch 11 (May 26).

Several characters are *objects*, not people — Stovy is the oven, Icy is the popsicle and Mr Waffle is the waffle. That maps unusually well onto software modules: Stovy for manufacturing, Icy for beverages and Mr Waffle for the waffle SKUs.

Only four supplied printable 3D models exist in this kit: **Mr Waffle, Air Maxi, Bhoppu and Picchi**. They are stored as `.stl` files in their market/character folders; 2D T-pose artwork is not a 3D model. Full roster, usage rules and asset map: `brand/CHARACTERS.md`. Art: `assets/characters/{bangladesh,singapore}/`.

---


## 7. Product catalogue (POS-verified, Aug 2026)

Prices in BDT, **read from the till, not from menu artwork**. Standard prices come from the GiantSoft item-wise sales export; Chef's Table prices are effective net-per-unit from the ZAB July 2026 export. Menu artwork has been stale by up to two price revisions — treat it as a design record, not a price book.

Chef's Table runs **+16% to +33%** above standard on the same SKU, and the gap is not uniform. POS must support **per-channel price books**.

### Waffle on a Stick
| Item | Standard | Chef's Table | CT premium |
|---|---|---|---|
| Nutella | 185 | 215 | +16% |
| Red Velvet | 175 | 215 | +23% |
| Tri-Chocolate | 200 | 250 | +25% |
| Mad Mango | 225 | 270 | +20% |
| **Kunaffle™** *(Limited Edition)* | 280 | 350 | +25% |

### Waffles (square / tray)
| Item | Standard | Chef's Table |
|---|---|---|
| Fruity Bliss | 250 | 300 |
| Very Very Strawberry | 200 | 250 |
| Strawberry, Banana & Nutella | 185 | 230 |
| Bananatela & Nuts | 160 | 200 |
| Death by Nutella | 190 | 230 |
| Bangla Pizza *(savoury; older menus)* | — | — |

### Beverages
| Item | Standard | Chef's Table |
|---|---|---|
| Strawberry Cheese | 380 | 380 |
| Strawberry Mango Cheese | 350 | — |
| Strawberry Milk Shake | 380 | 380 |
| Mango Cheese | 285 | 340 |
| Choco Choco Cheese | 320 | 380 |
| Oreo Cream Shake | 285 | 285 |
| Hot Chocolate | 320 | ~334 |
| Crack Drink *(in POS; no description or artwork — confirm status)* | 380 | — |
| Water 500 ml | 20 | — |

### Zero-Guilt Dessert
| Item | Standard | Chef's Table |
|---|---|---|
| Crunchy Chia Pudding | 380 | 464 |

### Combo
| Item | Standard |
|---|---|
| Waffle Madness (1:4) — 2× Nutella WOAS, 1× Mad Mango WOAS, 1× Tri-Chocolate WOAS | 720 |

### Add-ons
| Item | Standard | Chef's Table |
|---|---|---|
| Ice cream (vanilla · chocolate · strawberry · mango) | 135 | 135 |
| Whipped cream | 120 | 120 |
| Extra nuts | 80 | 80 |
| Extra Nutella | 120 | **109** ⚠ |

> ⚠ Extra Nutella is the only SKU priced *lower* at Chef's Table than standard. Every other CT price is higher. Almost certainly a CT item-master error, not a decision.

**What actually sells.** Nutella and Tri-Chocolate are roughly **two-thirds of all units** on delivery and two-thirds of Chef's Table revenue. The rest of the range shares the remaining third. Any tool that treats the catalogue as flat — equal shelf space, equal forecasting weight, equal stock priority — is modelling a business that doesn't exist.

**Loyalty — the Surprise Card.** One card per **BDT 500** spent. Two types from the same envelope: a **character card** (collectible; bio on the front, colour-in line art on the back) and a rarer **scratch card** (instant win — free item or merch). Every card carries a unique serial, e.g. `FLL-9525656492`. A **batch** is the production unit: **297 cards — 270 character + 27 scratch (9.09% scratch)**. Twelve **print runs** to date, each ~27,000 character + ~3,500 scratch, i.e. roughly 100 batches per run. Tracked in Excel. *(Corrected 23 Aug 2026 — this line previously called a print run a "batch", a ~100× discrepancy. `batch_id` means 297 cards everywhere, including the Surprise Card engine.)*

Measured 2026 performance: **38,556 distributed** (Feb–May), **2,839 redeemed** (Jan–Aug), a **3–4% redemption rate** — with a 2–3× spread between the best outlet (Sylhet) and the worst (Bashundhara). At the till it appears as two zero-value complimentary categories: `SURPRISE CARD` for issue and `SURPRISE CARD ITEM` (`SI …`) for redemption. **Any POS or loyalty module must preserve that issue/redeem distinction** — it is the only thing making the programme measurable today. Full detail in `waffleup-marketing-kit/programs/SURPRISE-CARD.md`.

---

## 8. Outlets & channels

**15 trading sites** across four models. This visual brand library does not maintain an operational outlet register.

| Type | Count | POS | Delivery | Price book |
|---|---|---|---|---|
| Standard outlet | 8 | GiantSoft | Foodpanda · Pathao · Foodi · BuyHereNow | standard |
| Chef's Table | 4 | ZAB (Chef's Table's own) | **none** | chefs_table |
| Cloud kitchen | 2 live | Foodpanda only | Foodpanda | standard |
| International | 1 | unknown | unknown | unknown |

**Standard outlets** (`WUP-FS-01…08`): Banani (1st, 16 Dec 2021) · Dhanmondi (flagship) · Gulshan 1 · Bailey Road · Bashundhara R/A · Uttara · Sylhet Zindabazar · Chattogram
**Chef's Table** (`WUP-FC-01…04`): Gulshan 2 · Dhanmondi · Courtside United City (100ft) · Sylhet
**Cloud kitchens** (`WUP-CK-…`): Mirpur · Mohammadpur live. **Rampura is *opening soon*, not open.** FP Bashundhara and FP Uttara are discontinued.
**International:** Singapore — CQ @ Clarke Quay · Dubai, Thailand, Indonesia coming soon

**Delivery partners:** Foodpanda · Pathao · Foodi · Buy Here Now (historically also Munchies, HungryNaki) — plus WaffleUp's own delivery all over Dhaka. Coverage: Gulshan, Banani, Baridhara, Bashundhara, Uttara, Dhanmondi, Bailey Road, Mirpur, Mohammadpur, Sylhet.

**Outlet models:** *Quick dispatch window / drive-in* — compact 180–250 sq ft, serves through a window; walk-in, takeaway, sit-in-car or drive-by. Also events catering (corporate, concerts, schools, universities, weddings).

### Four things every ops tool must handle

1. **Outlets differ by type.** Each type needs its own SOP checklist, price book and stock list. Don't hardcode one outlet shape.
2. **Foodpanda is not a cloud-kitchen thing.** Every standard outlet has a Foodpanda storefront. Cloud kitchens are just the two sites that have nothing *but* delivery. Cloud-kitchen commission also runs ~4 points higher (31.6% vs 27.6%).
3. **Chef's Table has no delivery at all.** Never surface a delivery flow, a delivery SLA or a "find us on Foodpanda" link for a CT location.
4. **Banani trades under a different legal entity and BIN.** `CLOUD` / `003596326-0101` versus `WAFFLE UP LIMITED` / `005242361-0101` for every other site. Any consolidated revenue, VAT or invoicing view must carry `legal_entity` and split on it.

### POS reality

| System | Where | Note |
|---|---|---|
| **GiantSoft** (Giant POS) | 8 standard outlets | Original system, and current. Exports are filename-stamped with a .NET tick — no outlet, no date inside the file. |
| **Otomatic** | historic | Used for a period between the two GiantSoft eras. Any trend line crossing that switch compares two different definitions of a sale. Nobody has recorded when each outlet switched. |
| **ZAB Framework** (Orange Solutions) | 4 Chef's Table outlets | Chef's Table's own system. Detail export duplicates item-line pages — aggregate by invoice sub-total or overstate CT by ~29%. Identify the shop by invoice prefix (`DO01`/`DO04`/`DO05`/`DO13`), never the item code. |
| **Foodpanda merchant portal** | all except CT | A *channel* report, not a POS. Foodpanda GMV cannot be added to POS revenue — the same sale is in both. |

> **There is currently no single source that gives a correct company revenue number.** Building one is the first real job for any new system. See `waffleup-marketing-kit/data/POS-AND-REPORTING.md`.

---

## 9. Rules for anything I build in this project

1. **Colour** — use the tokens in `tokens/wup-tokens.css`. Respect the 60–75 / 15–25 / 3–5 ratio. Ink is `#450001`, never `#000000`.
2. **Logo** — always the wave version, always with clearspace, never recoloured, never solid-letter.
3. **Type** — General Sans for data, CHUM / Futura Extra Bold for headers and celebration moments only.
4. **Shape language** — rounded corners, thick cocoa outlines, sticker/plaque cards, the wave-blob divider. Nothing flat-grey-enterprise.
5. **Voice** — functional labels, Jester microcopy. Puns allowed in empty states, success states and staff nudges; never in errors or compliance text.
6. **Characters** — one per outlet / per achievement; use the line-art versions as icons.
7. **Bilingual** — Bangla is a first-class language for staff-facing tools (outlet teams), English for management dashboards. Design for both.
8. **Multi-outlet by default** — every schema carries `outlet_id`, `outlet_type`, `channel` (dine-in / takeaway / Foodpanda / Pathao / event) and `price_book`.
9. **Currency** — BDT, no decimals, format `BDT 250` or `৳250`.

---

## 10. Where the assets live

```
[WUP] Waffle Up-...-1-0NN/[WUP] Waffle Up/
├── [WUP-01] Brand Assets/
│   ├── [WUP-01-01] Logo          logo, RGB + CMYK, .eps + .png
│   ├── [WUP-01-02] Symbol        W monogram
│   ├── [WUP-01-03] Icon          6 icon variants, .ai + .png
│   ├── [WUP-01-04] Color Code    RGB / CMYK / Pantone swatch sheets
│   ├── [WUP-01-05] Fonts         chum, futura, ultra, bebas-neue, puffin-display, general-sans
│   ├── [WUP-01-06] Typography    30 pre-set word-marks (rgb + cmyk)
│   ├── Works by Rokib/           per-outlet signage, packaging, menus, murals, Brand Book V.1
│   └── Works by Sharara/         brand pattern, characters, logo, menu templates, Figma file
├── Menu/                          dated menu artwork (latest: 2026.04.01 CT, 2026.04.21 Event)
├── [WUP-02] Digital · [WUP-03] Print
├── Animation (Tasnim)/            3D character rigs, poses, .moho files
├── Characters 3D (China)/
├── Event Materials · Merch · Social Media Posts · Video Contents · WUPxStickOn
└── Index.xlsx                     asset index
```

**Marketing assets, occasions calendar, format specs, copy bank and the animation pipeline live in `waffleup-marketing-kit/`.**

Google-Takeout split: the same tree is spread across parts `-001` to `-018`. To find a file, search all 18 parts.
