# Changelog

## 1.7.0 — 2026-08-11
Added the missing layer: a system architecture, and the third registry.

**New — `ARCHITECTURE.md`**

The shape the kit had been implying but never stated: **three registries (places, things, people), then append-only facts, then disposable views.** Includes the status of each registry, five rules that keep the build gradual, a dependency-ordered build sequence with the reasoning for each edge, the full people-registry schema, and four questions every module must answer before it ships.

**The finding behind it**

WaffleUp already has a stable, company-wide numeric employee ID, and it appears in three otherwise-disconnected systems: the fingerprint attendance exports, the `WUP HR LIVE` roster, and the `User Id` stamped on GiantSoft transaction lines. Employee document folders are already named after it. Of the 8 IDs checkable in both the Jan-2024 attendance export and the Dec-2025 roster, **8 of 8 are the same person** — a live join across HR, attendance and the POS that nothing currently uses.

**Corrected — `data/CONVENTIONS.md`**

- **`employee_id` was wrong.** v1 proposed minting `WUP-EMP-{n}` and mapping it to the fingerprint ID. That is backwards: it would have created a parallel key alongside a working one. Now the existing numeric ID, stored as a string, with the evidence and two open questions (is the space reused? is it the device ID?) written down.
- **`employee` entity restructured.** No `outlet_id` — staff rotate, and 27 of 45 staff IDs in 2026 POS data worked at more than one outlet in the same period. Assignment is now its own dated fact table. No salary, NID or bank details either; the registry holds identity, not the employment file.
- Added `slot: A | B | C` as the attendance device actually emits it, with the note that the A/B/C ↔ opening/mid/closing mapping is unconfirmed. v1 had guessed the human labels and lost the source values.
- New rule 10: never put a mutable relationship in a registry column — assignment, price and stock are all facts with dates, not fields.
- New **Personal data** section: what may be read broadly, what may not, and the credentials pattern to unwind.

This is the second time a v1 identifier scheme invented inside the kit had to be replaced by one the business already used — outlets were the first. Hence the rule now stated in `ARCHITECTURE.md`: **adopt identifiers, don't mint them.** Items are the only registry that genuinely needs new IDs.

**`README.md`** — `ARCHITECTURE.md` added to the tree and a pointer for anyone building on the kit.

## 1.6.0 — 2026-08-11
The rest of the kit caught up with the data files. v1.1.0 (below) fixed `outlets.json` and `menu.json`; every other file was still quoting the old numbers.

**`brand/BRAND.md`**

- **Section 7 (product catalogue) repriced from the till.** Was headed "as of Aug 2025 outlet menu / Apr 2026 Chef's Table menu"; now POS-verified Aug 2026. Nutella 180→185, Tri-Chocolate 185→200, Kunaffle 260→280, Death by Nutella 185→190, Hot Chocolate 285→320, ice cream 95→135, whipped cream 80→120, extra nuts 60→80, extra Nutella 80→120. Added Water, Waffle Madness combo, Strawberry Milk Shake and Crack Drink; added a CT-premium column (+16% to +33%). Flagged Extra Nutella as the one SKU cheaper at Chef's Table than standard — likely an item-master error.
- Added: the range is not flat. Nutella and Tri-Chocolate are ~two-thirds of units. Tools that assume an even catalogue are modelling a business that doesn't exist.
- Surprise Card now carries measured performance and, more usefully for builders, how it appears at the till: two zero-value complimentary categories, `SURPRISE CARD` and `SURPRISE CARD ITEM`.
- **Section 8 (outlets) rewritten** around the real register: 15 trading sites, ops codes, a POS table including Otomatic, and four things every ops tool must handle — outlet types differ; Foodpanda is not a cloud-kitchen thing; Chef's Table has no delivery; Banani is a separate legal entity and BIN.
- Added a verified-scale row alongside the 2023–24 profile figures.

**`components/preview.html`**

- `PRODUCTS` repriced, `OUTLETS` rebuilt with real codes, live status and Foodpanda store IDs. The outlet table gained Status and Foodpanda columns and dims non-trading rows.
- Menu, outlets and Surprise Card sections rewritten to say where the numbers come from and what breaks if you ignore them.

**`data/CONVENTIONS.md`**

- **`outlet_id` scheme corrected.** The old `WUP-` / `CT-` / `CK-` prefixes were invented here before anyone read the ops register; superseded by `WUP-FS-` / `WUP-FC-` / `WUP-CK-`, which is what the business already prints on things. Retired numbers stay retired.
- Added external keys (`foodpanda_store_id`, `zab_invoice_prefix`, `bin`, `legal_entity`), `outlet_status` and `legal_entity` enums, `otomatic` in `pos_system`, and a required `item_alias` entity.
- Four new rules: never join on an item name; never add Foodpanda revenue to POS revenue; reconcile every parsed report against its own printed total; model Surprise Card issue and redemption separately.
- Added an export file-naming convention — GiantSoft ships tick-numbered files with no outlet or date inside them.

**`AGENTS.md` / `CLAUDE.md`** — price examples corrected; `legal_entity` added to the mandatory fields; the "facts that bite" list expanded with the delivery, commission, status and item-naming traps; four new checklist items.

**`brand/CHARACTERS.md`** — outlet mapping now carries the real `outlet_id`s, and flags that **Chachhu Sam and Bubbly are not among the nine rigged characters**, so Sylhet and Chattogram have no poses available.

**`ODOO.md`** — ingestion step now names the three traps that will break a naive import; the architecture diagram warns that a Foodpanda order at Dhanmondi is also in GiantSoft.

**`README.md`** — two data rules added to the "if you read nothing else" list.

## 1.1.0 — 2026-08-11
Data files rebuilt from operational records rather than brand assets.

- `data/outlets.json` → **2.0.0**. Rebuilt from the ops drive's WUP Outlet Dashboard and Outlet FAQ Details, plus the Foodpanda and ZAB exports. Real outlet codes, addresses, BINs, phones, verified hours, status. Rampura corrected to *opening soon*; Chattogram confirmed open; discontinued cloud kitchens retained for reconciliation; Foodpanda store IDs and ZAB shop prefixes recorded; Banani's separate legal entity and BIN flagged. Credentials from that sheet were deliberately not copied.
- `data/menu.json` → **2.0.0**. Prices now come from the GiantSoft and ZAB tills, not menu artwork. 12 prices corrected, 3 POS-only SKUs added, every item carries a `priceSource`.
- Rationale, working and remaining gaps: `waffleup-marketing-kit/data/BUSINESS-STATE.md`.

## 1.5.0 — 2026-08-11
`components/preview.html` restyled to match waffleup.global.

- **Left sidebar replaced with the site's own navigation**: a gold announcement strip above a sticky pink nav bar — logo left, uppercase menu right, white pill CTA — copied from the real site's structure.
- **Hover dropdowns.** Five top-level groups (Foundation · Personality · Product · UI system · Production) reveal their sub-sections on hover, each with a colour dot. Tap-to-open on touch devices; collapses to a hamburger below 900px.
- **Per-section background switching**, the site's signature scroll behaviour: 19 full-bleed colour blocks cycling white → cyan → pink → gold → mint → cocoa, with hard edges and wave dividers at key transitions. Text, muted text and code colours re-theme per band so contrast holds on every field.
- Added a scroll-progress bar and scroll-spy that highlights the active nav group.
- Fixed an `id="menu"` collision between the nav element and the menu section, which broke both the anchor link and the mobile toggle.

## 1.4.0 — 2026-08-11
`components/preview.html` rebuilt as a full living brand book.

- **The real brand fonts now render.** CHUM, Futura Extra Bold, Bebas Neue and General Sans extracted from `assets/fonts/*.zip` into `assets/fonts/web/` and loaded via `@font-face`. The preview no longer falls back to system type.
- Grew from 12 to **19 sections** with a sticky navigation sidebar: brand story · logo & marks · pattern · colour · typography · word-marks · the gang · expressions · character cards · voice · menu · outlets · Surprise Card · components · UI patterns · formats · audio · packaging & event · file map.
- **Interactive:** click any swatch to copy its hex; toggle the menu between the standard and Chef's Table price books; tick the checklist rows.
- Now shows real assets throughout — all 5 icon variants, 3 symbols, the brand pattern, a clearspace diagram, logo do/don't, 12 word-marks, 9 character heroes, 9 expression sheets, 10 character cards, 14 product photos, Surprise Card art, packaging shots, and an audio player for the house track.
- Added colour tint ramps, a type scale table, text-on-colour checks, an outlet table, and aspect-ratio boxes for every content format.

## 1.3.0 — 2026-08-11
Character origin corrected, on Jawat's account.

- **The characters were created by founder Mohammad Salman**, then formalised later with outside (likely freelance) production help. The website's "renowned French-Australian artist" line describes that formalisation stage, not the origin — it is public-facing framing, not provenance.
- Ownership outlook revised from a blocker to a likely non-issue: founder-originated characters are almost certainly WaffleUp-owned. The remaining question is narrower — what the animator agreements say about the `.moho` rig files specifically, as distinct from the characters.
- Plain-language explanation of what a rig and a `.moho` file are added to `waffleup-marketing-kit/formats/ANIMATION.md`.

## 1.2.0 — 2026-08-11
Full-drive sweep. Every remaining folder explored; findings folded in.

- **Merlulu named** — the Singapore Merlion character, confirmed by `Surprise Card/Batch 11 (May 26)/Character Card - Merlulu.eps`, where it joins the nine as a tenth collectible.
- **Drive filename ↔ proper name map added** to `brand/CHARACTERS.md` (Bhoopu/Bhoppu, Popsicle/Icy, Stovy/Stovie, Spacy/Spacie, Tvy/TV, Maxy/Air Maxi).
- **Surprise Card documented properly** in `brand/BRAND.md` and `data/menu.json`: two card types, unique serials, 12 batches, ~27,000 character + ~3,500 scratch per batch.
- Product photography pointer added to `data/menu.json`.
- Companion `waffleup-marketing-kit/` created and cross-linked.

## 1.1.0 — 2026-08-11
Character audit. The v1.0.0 roster was assembled from the brand-guideline text and a partial folder sample, and several entries were wrong.

- **Canonical roster established: nine rigged characters** — Bhoppu, Air Maxi, Picchi, Swirly, Mr. Waffle, Icy, TV, Stovie, Spacie — taken from the numbered set in `Animation (Tasnim)/3D Characters/`, each with main pose, T-poses, hoodie variant, extra poses and Moho rigs.
- **Corrections from inspecting the actual art:** Swirly is a candy-swirl striped bear (not a twirling girl); Stovie is the waffle *oven* (not a person); Sweety is a sundae glass; Icy is the popsicle (filed as "Popsicle" on the drive); Mr. Waffle is a waffle square in sunglasses; ZZZ (the "always sleeping" one) is drawn as a little house. Spacie and TV were missing entirely from v1.0.0.
- **Secondary tier documented:** Bubbly, Sweety, Chachhu Sam, ZZZ, Lazy Squirrel — 2D card art only, no rig, so no new poses are possible.
- **Singapore Merlion variant found** on the SG sticker sheets, with a softer pastel palette than the BD artwork.
- Assets restructured: `assets/characters/{hero,expressions,cards,reference}/` with clean kebab-case names. 13 hero renders, 9 expression sheets, 11 character cards, 6 reference sheets.
- Outlet ↔ character mapping corrected in `data/outlets.json`; product ↔ character mapping corrected in `data/menu.json`; `brand/BRAND.md` §6 and `components/preview.html` updated.

## 1.0.0 — 2026-08-11
Initial kit.

- Brand truth extracted from `Waffle Up Brand Book V.1` (2022), `WUP Brand Guideline` (Lamiya, 2023),
  `WaffleUp Profile` (Feb 2024), waffleup.global and the `[WUP-01] Brand Assets` drive.
- **Palette corrected.** The 2022 Brand Book values (`#6DCBD8 / #F0639A / #FFD66D / #3E1312`) are superseded
  by the `[WUP-01-04] Color Code` files (`#0BF9F6 / #FF629B / #FFD56D / #450001`), verified pixel-for-pixel
  against the master logo artwork. Old values retained as the print/CMYK line.
- Tokens published in 6 formats: JSON (canonical), CSS, SCSS, TS, Tailwind preset, Dart/Flutter.
- Components: sticker card, plaque button, layered hero type, wave divider, stat tile, pill, checklist row, input, empty state, pattern band.
- `AGENTS.md` / `CLAUDE.md` for AI coding agents.
- Data: `outlets.json` (16 locations), `menu.json` (24 SKUs, both price books), `CONVENTIONS.md`.
- `ODOO.md` — recommendation on Odoo Community for the back office.
- Assets copied in: logo (RGB+CMYK), 5 icon variants, symbol, brand pattern, 5 characters, 15 word-marks, 6 font packs.

### Known gaps
- No recipes / bill of materials per SKU — needed before inventory depletion can be automated.
- No ingredient master, packaging consumables, suppliers or par levels.
- Outlet hours, staffing and live status unconfirmed.
- Vector logo (SVG) not in the drive — only .eps and .png. Ask design for SVG exports.
