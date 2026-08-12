# WaffleUp — instructions for AI coding agents

You are building software for **WaffleUp**, a waffle QSR chain (Waffle Up Global PTE Ltd., Singapore; largest waffle chain in Bangladesh). Everything you produce here is customer-facing in spirit even when it's an internal tool — outlet staff, managers and the founders all see it. Off-brand output is a defect, same as a failing test.

Read `.brand/brand/BRAND.md` before designing anything. Import tokens from `.brand/tokens/`. Never hardcode a colour, font or radius.

---

## 1. Non-negotiables

**Colour**
- Use tokens only: `--wup-cyan #0BF9F6` · `--wup-pink #FF629B` · `--wup-gold #FFD56D` · `--wup-cocoa #450001` · white.
- **Text/border ink is `#450001`. Never `#000000`, never grey `#333`.**
- Ratio per screen: one dominant colour 60–75%, secondary 15–25%, accents 3–5% each. Don't paint everything cyan.
- On cyan and gold, text is cocoa. On pink and cocoa, text is white.
- Print/CMYK contexts (receipts, labels, packaging artwork) use the `-print` variants.

**Type**
- Body, data, tables, forms → **General Sans** (`--wup-font-body`).
- Headers, splash, celebration, printed receipts → **CHUM** or **Futura Extra Bold**.
- Big numerals, tickers, price rails → **Bebas Neue**.
- Never set dense operational data in a display face.
- Numbers in POS/stock views get `font-variant-numeric: tabular-nums`.

**Shape**
- Rounded corners (`--wup-radius` 16px default), **thick cocoa outline** (`3px`), **hard offset shadow** (`0 6px 0 var(--wup-cocoa)`) — sticker, not Material card.
- Buttons are pill-shaped plaques that press down on `:active`.
- Section breaks use the wave (`.wup-wave`) or a wave-blob colour split, not a 1px grey line.

**Logo**
- Only from `.brand/assets/logo/`. The white signature wave through the letterforms is mandatory.
- Never recolour, stretch, rotate, crop corners, remove the ®, or render solid/single-coloured letters.
- On coloured backgrounds use `assets/icon/Icon (white).png`; on white use `Icon (rbg).png`.

**Voice**
- Archetype: **Jester** — casual, friendly, humorous, puns welcome.
- **Labels, field names and error/compliance text: plain, literal, fast to scan.** Staff are mid-shift.
- **Empty states, success states, streaks, nudges: let it be funny.** See `brand/VOICE.md` for a paste-ready bank.
- Currency `BDT 250` or `৳250`, whole numbers, no decimals.

---

## 2. Domain rules — get these right or the tool is wrong

WaffleUp is **not** a single-shop business. Every schema, API and screen must carry:

| Field | Values |
|---|---|
| `outlet_id` | see `data/outlets.json`. Use the ops codes — `WUP-FS-01`, `WUP-FC-03`, `WUP-CK-04`. Do not invent a parallel scheme |
| `outlet_type` | `outlet` · `chefs_table` · `cloud_kitchen` · `event_cart` |
| `channel` | `dine_in` · `takeaway` · `foodpanda` · `pathao` · `foodi` · `buyherenow` · `wup_delivery` · `event` |
| `price_book` | `standard` · `chefs_table` · `event` — **prices genuinely differ**, e.g. Kunaffle 280 vs 350, Tri-Chocolate 200 vs 250. Chef's Table runs +16% to +33%, non-uniformly |
| `legal_entity` | `waffle_up_limited` · `cloud` — Banani trades under a separate entity and BIN. Consolidated revenue and VAT must split on this |

Other facts that bite:
- **Prices come from the POS, never from menu artwork.** `data/menu.json` is POS-verified as of Aug 2026. Menu JPGs on the drive were stale by up to two revisions — 12 prices in the previous version of this kit were wrong because they were read off artwork.
- **Cloud kitchens have no walk-in.** No dine-in flows, no table numbers, Foodpanda-only channel. They also pay ~4 points more Foodpanda commission (31.6% vs 27.6%) — margin logic must not assume one rate.
- **Foodpanda is not a cloud-kitchen thing.** Every standard outlet has a Foodpanda storefront too. Cloud kitchens are just the two sites with nothing else.
- **Chef's Table is a co-brand** with its own menu artwork, its own price book, its own POS — and **no delivery at all**. Never surface a delivery flow or SLA for a CT site.
- **Rampura is not open.** `WUP-CK-05` is `opening_soon`; `WUP-CK-01` and `WUP-CK-02` are discontinued. Filter on `status`, don't assume every row in `outlets.json` is trading.
- **POS is fragmented today:** GiantSoft (8 standard outlets), ZAB (4 Chef's Table), Foodpanda (cloud kitchens, and a channel everywhere else), plus **Otomatic** historically — trend lines break across that switch. Anything new must ingest and reconcile heterogeneous sources, not assume one system.
- **Never join on an item name.** Four systems spell the same waffle four ways; in the CT data the typo `Red Velvel` outsells the correct spelling 9:1. Go through an alias table; unmapped codes go to a human, never to a fuzzy match.
- **Never add Foodpanda revenue to POS revenue.** Same sale, two views. There is currently no single source of correct company revenue.
- **Inventory currently lives in noisy Excel.** Migration paths and import tolerance matter more than a pretty schema.
- **Loyalty:** Surprise Card issued on every **BDT 500** purchase. At the till it is two zero-value complimentary categories — `SURPRISE CARD` (issue) and `SURPRISE CARD ITEM` (redeem). Model them as `complimentary_qty`, not as a discount; collapsing them destroys the only measurement the programme has. Measured redemption is 3–4%.
- Timezone **Asia/Dhaka**. Dates ISO `YYYY-MM-DD`.
- Staff-facing screens: **Bangla + English**. Management dashboards: English. Never hardcode user-visible strings — use an i18n layer from day one.

---

## 3. How to build here

**Building a system, not a screen? Read `ARCHITECTURE.md` first.** Three registries — outlets, items, people — then append-only facts that reference them, then disposable views. Two registries already live in `data/`. If your module is about to hold its own list of outlets, items or staff, stop: reference the registry instead. And adopt existing identifiers rather than minting new ones — outlet codes and employee IDs both already exist in the business, and both were invented wrongly in this kit before anyone checked.


- **Phone-first for staff tools.** Opening/closing checklists, wastage logging, stock counts happen on a phone, one-handed, sometimes with wet hands. Big tap targets (min 48px), thumb-reachable primary actions, works on a cheap Android in a bright shopfront.
- **Camera-first data entry is a first-class feature**, not a nice-to-have. Memos, receipts and wastage are captured as photos today. Design capture → extract → confirm → commit flows, always with a human confirm step.
- **Offline tolerant.** Outlet wifi is not a given. Queue writes, sync later, show sync state honestly.
- **One unified data model** across POS, inventory, manufacturing, HR/attendance, support. Don't build a silo; give every module a shared `outlet`, `item`, `employee`, `event` vocabulary.
- Accessibility: 4.5:1 contrast minimum. Cyan and gold need cocoa text, not white — check it.

---

## 4. Checklist before you call it done

- [ ] No hardcoded hex, font-family, or radius — all from tokens
- [ ] No `#000` anywhere; ink is `#450001`
- [ ] One dominant colour per screen, ratio respected
- [ ] Logo from `assets/`, wave intact, correct variant for the background
- [ ] Body copy in General Sans; display faces only in headers/celebrations
- [ ] Sticker shape language: rounded, cocoa outline, offset shadow
- [ ] `outlet_id`, `outlet_type`, `channel`, `price_book`, `legal_entity` present in every relevant model
- [ ] Any price shown is traceable to `data/menu.json` and labelled with its price book
- [ ] Outlet lists filter on `status` — closed and not-yet-open sites excluded
- [ ] Any ingest reconciles its parsed total against the source report's own printed total
- [ ] Staff strings translatable; BDT formatted without decimals
- [ ] Tap targets ≥48px; usable one-handed
- [ ] Contrast checked
- [ ] Microcopy: literal in errors, playful in empty/success states
