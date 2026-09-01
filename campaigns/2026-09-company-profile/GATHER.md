# Gather list — WaffleUp Company Profile 2026

Everything that is not a photograph. Facts to verify, documents to collect, assets already in hand.

**Rule for the whole project:** nothing goes into the profile unverified. Anything still open at draft stage is written as `[CONFIRM]` in the copy deck, and `[CONFIRM]` never survives to a signed-off page. Never invent a price, an outlet, an opening date, an award or a statistic.

---

## 1. What we already have — no gathering needed

Confirmed present in this library and usable as-is.

| Asset | Where | Use in the profile |
|---|---|---|
| Logo — RGB + CMYK, .eps + .png | `assets/logo/` | Cover, footers. Supplied file only, never rebuilt |
| Symbol, 6 icon variants | `assets/symbol/`, `assets/icon/` | Section marks, contact page |
| Brand pattern (wave-blob) | `assets/pattern/` | Section dividers, cover |
| Colour tokens — RGB / CMYK / Pantone | `tokens/wup-tokens.json` | Identity page, and the whole document's palette |
| Six licensed font families | `assets/fonts/` | CHUM, Futura Extra Bold, Bebas Neue, General Sans |
| 15 pre-set word-marks, full four-layer treatment | `assets/typography/` | Section titles. Use the artwork, don't rebuild the effect |
| **15 product-hero shots** | `assets/marketing/product-hero/` | Range pages. Covers all 5 Waffle-on-a-Stick and all 6 waffles |
| Packaging flats — BD boxes A/B/C, trays, cups, SG bag | `assets/marketing/packaging/` | Packaging page, alongside real photography |
| Event artwork — backdrops, sidedrops, table front, 5 X-banners | `assets/marketing/event/` | Events page |
| **10 character card designs** | `assets/Surprise Cards/Character Cards/` | The Gang and Surprise Card sections |
| Character art — 2d hero, expressions, poses, T-poses | `assets/characters/`, `Character poses/` | The Gang section |
| Character canon | `brand/CHARACTER-BIBLE.md`, `data/characters.json` | Copy for the Gang pages |
| Owned audio — Sweet Night Bites 30s / 60s / 1.5min | `assets/marketing/audio/` | Profile video — **rights unverified, see §7** |
| Founder story, purpose, mission, vision, three R's | 2024 profile + `brand/BRAND.md` | Carry over near-verbatim |
| Product descriptions in brand voice | 2024 profile | Reuse; extend to the SKUs it never covered |
| 16:9 HTML→PDF build pipeline | `brand-guidelines/build.py` | The build route |

**Not usable as-is:**
- `docs/brand-guides/waffleup-profile-2024.pdf` is a **git-lfs pointer file, 134 bytes** — the content is not actually in the working tree. The real file is the 200 MB copy at the repo root. Worth cleaning up so the reference in `docs/` resolves.
- `assets/marketing/packaging/BD BOX A.jpg` is off-palette. Usable as a record of the artwork, not as a colour reference.

---

## 2. Numbers — the 2026 "In Numbers" page

The 2024 page reads **12 · 8,000 · 100+ · 2 · 38,000 · 180 mln**. Every one of those needs to be re-cut for 2026.

| Figure | 2024 profile said | Status | Owner |
|---|---|---|---|
| Trading sites | 12 outlets + 3 cloud kitchens | **Wrong.** Now 15 sites: 8 standard, 4 Chef's Table, 2 cloud kitchens live, 1 Singapore | Ops |
| Waffles per day | 8,000 | Still the working figure — **re-measure over a recent 30-day window** | Ops |
| Team members | 100+ | Verify current headcount | HR |
| Cities | 2 major cities in BD | **Wrong.** Dhaka, Sylhet and Chattogram = 3, plus Singapore | Ops |
| Orders per month | 38,000 | Verify. Foodpanda alone did 8,809 delivered orders in Jul 2026 | Ops / Finance |
| **Revenue** | BDT 180 mln (2023) | ⚠ **See the warning below** | Finance |
| Years trading | "24 months since inception" | Now **five years** as of 16 Dec 2026 — a timeline, not a duration | — |
| Countries | — | New figure worth adding: BD + SG live, three in pipeline | — |

### ⚠ The revenue warning — read before anyone types a number

`brand/BRAND.md` records that **there is currently no single source that produces a correct company revenue figure.** Three reasons, all live:

1. Standard outlets run **GiantSoft**, Chef's Table runs **ZAB**, and the ZAB detail export duplicates item-line pages — aggregating it naively **overstates Chef's Table by roughly 29%**.
2. **Foodpanda's merchant portal is a channel report, not a POS.** Its GMV cannot be added to POS revenue — the same sale appears in both. Adding them double-counts.
3. An **Otomatic** era sits between two GiantSoft eras, and nobody recorded when each outlet switched. Any multi-year trend line crosses two different definitions of a sale.

**Recommendation: do not print a revenue figure in this profile until that reconciliation is done.** Printing an unreconciled number in a document that goes to investors and franchise prospects is the single highest-risk line in the project.

Safer figures that are defensible today and read just as well: **waffles per day · orders per month · trading sites · cities · team size · Surprise Cards distributed · years trading.** If a financial figure is genuinely required for the audience, print an audited or accountant-signed figure with its period labelled — never an internal export.

---

## 3. The estate register

There is no operational outlet register in this folder, and the map page and outlet-models pages both need one. Build it once, use it everywhere.

Per site, collect: **name · model · full address · opening date · floor area · seating/standing capacity · delivery platforms live · price book · legal entity · Google Business listing URL.**

Known list to verify and complete:

- **Standard (8):** Banani (1st, 16 Dec 2021) · Dhanmondi (flagship) · Gulshan 1 · Bailey Road · Bashundhara R/A · Uttara · Sylhet Zindabazar · Chattogram
- **Chef's Table (4):** Gulshan 2 · Dhanmondi · Courtside United City (100ft) · Sylhet — **no delivery at any of them**
- **Cloud kitchens:** Mirpur and Mohammadpur **live**. **Rampura is opening soon, not open** — do not list it as trading. FP Bashundhara and FP Uttara are discontinued and must not appear
- **International:** Singapore — CQ @ Clarke Quay

**Also needed:** opening dates for every site, for the timeline page. Right now only Banani's is documented.

**Retire from all copy:** the 2024 claim of *"outlets in UAE and Egypt soon to be launched."* Egypt is not in the current pipeline. The live pipeline is **Dubai, Thailand, Indonesia** — and each of those needs a status word chosen deliberately: *signed*, *in negotiation*, or *exploring*. "Coming soon" against a market with no signed agreement is the kind of line a due-diligence reader checks.

---

## 4. Press, awards and certification

### Press
The 2024 profile prints five bare URLs. For each: **confirm the link is live, capture publication name, article title, author, date, and a high-resolution screen capture of the piece as published.**

- The Business Standard — *WaffleUp: Square is the new heart*
- The Prestige — *A quick-bite trendsetter*
- The Financial Express — *Waffle Up: a bistro trendsetter*
- Showcase — *Rewriting the law of waffles*
- The Daily Star / Shout — *A waffle worth the fuss*

Then: **anything published since Feb 2024.** Two and a half years of coverage is missing from the deck. Also check for TV, radio, podcast and creator coverage — the old page is print-only.

**Permission:** confirm whether mastheads and article excerpts can be reproduced. Most publications allow a linked citation; reproducing layout and masthead is a separate question. Keep quotes short and attributed.

### Awards
| Award | What is needed |
|---|---|
| Best Retail Startup Brand | Issuing body, year, certificate, photograph of the plaque |
| Best Loyalty Campaign Program | Issuing body, year, certificate, photograph |
| Best Dessert Shop — Dhaka North City Corporation | Year, certificate |

All three currently appear as claims with no attribution. In a profile, an award without an issuing body and a year is weaker than no award.

### Certification
- **Halal** — certifying body, certificate number, issue and expiry dates, scope (which sites, which products), current certificate scan. It is on pack, so it must be current and it must be right. State it; never embellish it.
- Food-safety / hygiene licences, BSTI or equivalent, city trade licences — whatever a franchise or corporate reader will ask for.

---

## 5. Partners and clients

The 2024 page is a logo grid split GLOBAL / LOCAL with no names extractable from the file. Rebuild from scratch:

- The actual list, split into **suppliers · delivery platforms · corporate clients · event clients · technology partners**
- **Vector logo files** for each — a profile with pixelated partner logos looks worse than one with no partner page
- **Written permission to reproduce each mark.** Several suppliers restrict use of their branding by customers. This applies with particular care to any ingredient brand named in a product
- For corporate and event clients, confirm they are willing to be named at all

---

## 6. Corporate, legal and people

**Corporate**
- Confirm the entity structure for print: **Waffle Up Global PTE Ltd** (Singapore, 33A Pagoda Street 059192), **WAFFLE UP LIMITED** (BD), and the separate entity operating Banani under a different BIN. The audience is business-first, so this **does** belong in the document — decide how much detail
- Registration numbers, incorporation dates
- Current registered BD address. `brand/BRAND.md` and the 2024 profile give **two different Banani addresses** — Road 11 House 67/C Block E, versus Plot 07 Road 17 Rupsha Tower. Resolve which is the registered office and which is the outlet
- **Franchise model terms — now required** (audience confirmed business-first, 1 Sep 2026): investment range, footprint per model, fit-out cost, support package, territory rights, term. This is the content the "Partner with us" close is made of, and none of it exists in this folder today

**People**
- Founder bio — Mohammad Salman. Name, title, short bio, and confirm the story wording is how he wants it told in 2026
- Leadership team — names, titles, one-line bios, and consent to be named
- Current headcount, and a gender/role split if the Culture page uses one
- Anything the employer brand wants said: training, progression, staff numbers grown from within

**Singapore**
- CQ @ Clarke Quay — full address, opening date, model, menu differences, price book
- Which platforms it trades on (Grab is named in the channel map — confirm live)
- Who owns SG content approval

---

## 7. Loose ends worth closing before the build

| Item | Why it matters | Owner |
|---|---|---|
| **Crack Drink** — in POS at BDT 380, no description, no artwork | It is either a live SKU that needs shooting and listing, or a dead item that should be off the till. It cannot be both | Ops |
| **Extra Nutella priced 109 at Chef's Table vs 120 standard** | The only SKU cheaper at CT. Almost certainly an item-master error. Doesn't hit the profile directly, but it will hit any pricing table printed from POS | Ops |
| **Audio rights** — `assets/marketing/audio/` | No verified commercial-rights record. Cannot go in a public profile video without human sign-off. If rights are unclear, budget for a cleared track | Legal / Marketing |
| ~~Value pillars conflict~~ | **Resolved 1 Sep 2026** — the profile prints **Quality · Speed · Access · Innovation** | ✅ |
| **"Premium" in the Mission** | Sits against the de-luxury rule. `PLAN.md` §5b | Jawat |
| **Which box artwork is in production** | Determines whether the packaging page shows on-palette packaging | Ops / Design |
| **Menu artwork currency** | Runs up to two price revisions stale. Any menu board photographed or price printed must be checked against the live price book for that channel | Ops |
| **`docs/brand-guides/waffleup-profile-2024.pdf` is an unresolved LFS pointer** | The reference in `docs/` doesn't open | — |

---

## 8. Graphics to build (not gathered — made)

Not photography, but they are page-blocking and someone has to make them.

1. **Estate map** — Bangladesh with all sites plotted, coded by model, plus a Singapore inset
2. **Timeline 2021 → 2026** — needs every opening date from §3
3. **The reward loop diagram** — POS ↔ Cards ↔ Points ↔ Orders
4. **Outlet-model comparison** — four models, footprint, service style, delivery, side by side
5. **Channel diagram** — own delivery, four delivery partners, dine-in, events
6. **Product form as proof** — the stick / the square / the box as an explanatory graphic, not a photograph
7. **Org or entity structure** — **in scope**, now that the audience is business-first
8. **Franchise model at a glance** — the four outlet models against footprint, investment band and support, for the "Partner with us" page

All seven use brand colour, cocoa ink `#450001` (never black), rounded corners and thick cocoa outlines. Nothing flat-grey-enterprise.

---

## 9. Suggested owners

| Area | Owner |
|---|---|
| Estate register, opening dates, outlet facts, Crack Drink | Ops |
| Revenue reconciliation, orders, AOV | Finance |
| Headcount, leadership bios, Culture input | HR |
| Awards, halal, licences, partner mark permissions, releases | Legal / Admin |
| Press capture and new coverage | Marketing |
| Singapore facts and shoot brief | SG lead |
| Structure, copy, shot direction, build | Marketing / Claude |
| Audience call, pillars, mission, final sign-off | Jawat |
