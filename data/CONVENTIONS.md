# Data conventions

Shared vocabulary across every WaffleUp repo. If two modules disagree on these, the unified database can never be built. Adopt them from the first commit.

## Identifiers

**`outlet_id`** — see `outlets.json`. **Use the ops team's existing codes.** They already exist, they are already printed on things, and inventing a parallel scheme guarantees two systems that can never be joined.

| Prefix | Meaning | Example |
|---|---|---|
| `WUP-FS-NN` | standard outlet (*full service*) | `WUP-FS-01` Banani |
| `WUP-FC-NN` | Chef's Table (*food court / co-brand*) | `WUP-FC-03` CT Courtside |
| `WUP-CK-NN` | cloud kitchen | `WUP-CK-03` FP Mirpur |
| `WUP-EV-NN` | event cart | — *(not yet used by ops; ours to define)* |
| country code | international | `SG-CQ` Clarke Quay |

> Earlier versions of this file proposed `WUP-` / `CT-` / `CK-` prefixes. That scheme was invented here before anyone had read the ops register. It is superseded — the `WUP-FS-` / `WUP-FC-` / `WUP-CK-` codes above are what the business actually uses. Numbers are **not** reassigned when a site closes: `WUP-CK-01` and `WUP-CK-02` are discontinued and stay retired so historic reports still resolve.

**External keys** — every outlet may carry identifiers owned by someone else. Store them, never derive from them.

| Key | Owner | Note |
|---|---|---|
| `foodpanda_store_id` | Foodpanda | 4-char code, e.g. `b41r` Dhanmondi |
| `zab_invoice_prefix` | Chef's Table | `DO01` / `DO04` / `DO05` / `DO13`. **Not** the item code — ZAB's item-code format changed mid-2026 and dropped the shop |
| `bin` | NBR | `005242361-0101` for all sites except Banani, which is `003596326-0101` |
| `legal_entity` | — | `WAFFLE UP LIMITED` or `CLOUD`. Banani is the exception. Consolidated revenue and VAT must split on this |

**`sku`** — `CAT-XXX`, three-letter category + three-letter item.

| Category | Meaning |
|---|---|
| `WOS` | Waffle on a Stick |
| `WAF` | Waffles |
| `BEV` | Beverages |
| `ZGD` | Zero-Guilt Dessert |
| `ADD` | Add-ons |
| `ING` | Ingredients (raw) |
| `PKG` | Packaging consumables |
| `EQP` | Equipment |

**`employee_id`** — **the existing numeric staff ID**, stored as a string: `'110'`, `'494'`, `'422'`.

Do not mint a new one. This ID already exists and already joins three otherwise-disconnected systems:

| System | Where it appears |
|---|---|
| Fingerprint attendance device | `WUP Attendance (…).xlsx` — keyed `ID, NAME`, with `LATE / EARLY LEFT / OVERTIME / DAY OFF / LEAVE / ABSENT / SLOT` |
| HR roster | `WUP HR LIVE (Sep–Dec 25)` — daily roster per branch, plus an ID ↔ name table |
| GiantSoft POS | the `User Id` on each transaction line (visible today on Surprise Card redemptions) |
| Document filing | `HR 2024-25/Employee Profile/` — folders named `101`, `102`, … |

Verified: of the 8 IDs present in both the Jan-2024 attendance export and the Dec-2025 roster, 8 of 8 resolve to the same person across a 23-month gap.

> Earlier versions of this file proposed `WUP-EMP-{n}` and said it "must map to the fingerprint device ID". That was backwards — it would have minted a parallel key alongside a working one. Superseded. **Adopt identifiers, don't mint them**; today the only registry that genuinely needs new IDs is items.

Two open questions to settle before this is load-bearing — see `ARCHITECTURE.md`:

- The ID space is **sparse and blocked** (101–199, then 401–450, extending past 567) with frequent gaps. Do the blocks mean something, and are numbers ever reused? If reused, add a surrogate key.
- Is the POS `User Id` provably the same number? Cross-check against a GiantSoft user/cashier list export before relying on the join.

## Enums

```
outlet_type  : outlet | chefs_table | cloud_kitchen | event_cart
channel      : dine_in | takeaway | foodpanda | pathao | foodi | buyherenow | wup_delivery | event
price_book   : standard | chefs_table | event
pos_system   : giantsoft | otomatic | zab | foodpanda | wup   ← today's reality is fragmented
                 giantsoft  8 standard outlets, current
                 otomatic   historic only; trend lines break across the switch
                 zab        4 Chef's Table outlets (Chef's Table's own system)
                 foodpanda  cloud kitchens; also a *channel* for every other outlet
outlet_status: open | opening_soon | discontinued
legal_entity : waffle_up_limited | cloud
slot         : A | B | C          ← as emitted by the attendance device; do NOT rename at source
shift        : opening | mid | closing   ← human-facing labels; map from slot in a lookup,
                                            the A/B/C ↔ opening/mid/closing mapping is UNCONFIRMED
uom          : g | kg | ml | l | pcs | pack | box
```

## Formats

| Thing | Rule |
|---|---|
| Currency | BDT, **whole numbers, no decimals**. Display `BDT 250` or `৳250` |
| Date | ISO `YYYY-MM-DD` |
| Timestamp | ISO 8601 with offset, e.g. `2026-08-11T21:30:00+06:00` |
| Timezone | `Asia/Dhaka` everywhere. Store UTC, display Dhaka |
| Business day | Closing counts belong to the day the shift **started**, not the calendar date at 1am |
| Locale | `en-BD` and `bn-BD` |
| Phone | E.164, `+8801XXXXXXXXX` |
| Weights | grams and millilitres in storage; friendly units at display time |

## Core entity sketch

Deliberately minimal — the shared spine every module hangs off.

```
outlet      (outlet_id, name, type, city, country, price_book, pos_system, timezone, status,
             legal_entity, bin, foodpanda_store_id, zab_invoice_prefix, opened_on)
item_alias  (source_system, source_code, source_name, sku)   ← REQUIRED, see below
item        (sku, category, name_en, name_bn, uom, is_sellable, is_stockable)
price       (sku, price_book, channel?, amount, valid_from, valid_to)
recipe      (sku, component_sku, qty, uom)          ← BOM; drives stock depletion
stock       (outlet_id, sku, qty, uom, as_of)
par_level   (outlet_id, sku, min_qty, reorder_qty)
count       (count_id, outlet_id, shift, counted_by, counted_at, lines[])
wastage     (wastage_id, outlet_id, sku, qty, reason, photo_url, logged_by, logged_at)
checklist   (checklist_id, outlet_type, shift, version, tasks[])
completion  (completion_id, checklist_id, outlet_id, employee_id, started_at, completed_at, evidence[])
order       (order_id, outlet_id, channel, price_book, placed_at, lines[], total, source_pos)
employee    (employee_id, full_name, known_as, role, status, joined_on, left_on, phone)
                                          ← NO outlet_id. Staff rotate; see assignment.
                                          ← NO salary, NID, bank details. Those live in HR, not here.
assignment  (assignment_id, employee_id, outlet_id, work_date, slot, is_cashier)
attendance  (employee_id, outlet_id, work_date, in_at, out_at, late_min, overtime_min, source)
document    (doc_id, type, outlet_id, photo_url, extracted_json, confirmed_by, confirmed_at)
```

## Rules that keep the data clean

1. **Every operational row carries `outlet_id`.** No exceptions, no "default outlet".
2. **Never store a price on an order line without its `price_book` and `channel`.** Chef's Table and Foodpanda genuinely differ; reconciliation dies without this.
3. **Photos are evidence, not data.** `document.photo_url` is kept; `extracted_json` is what OCR/vision produced; `confirmed_by` is who checked it. A human confirms before it commits — always.
4. **Stock moves are append-only.** Never update a quantity in place; write a movement and derive the balance. Excel's biggest failure mode is silent overwrite.
5. **Soft-delete only.** Nothing operational is hard-deleted; wastage and counts are audit trail.
6. **IDs are strings, not integers.** They get printed, scanned and typed by humans.
7. **`null` means unknown, `0` means zero.** Excel conflates these; the new system must not.
8. **Never join on an item *name*.** Four systems spell the same waffle four ways and two of them are inconsistent with themselves — `Red Velvel` (the typo) outsells `Red Velvet` 9:1 in the Chef's Table data. Every ingest goes through `item_alias`; unmapped codes go to a reject queue for a human, never to a fuzzy match.
9. **Never add Foodpanda revenue to POS revenue.** The same sale is in both. Foodpanda is a channel view, not a separate till.
10. **Never put a mutable relationship in a registry column.** Assignment, price and stock all change over time, so each is a fact with a date, not a field on a row. `employee.outlet_id` is the classic version of this mistake — 27 of the 45 staff IDs seen in 2026 POS data worked at more than one outlet in the same period.
11. **Reconcile every parsed report against its own printed total before using a single figure from it.** This is not paranoia: a parser silently dropped half a month of Chef's Table data when ZAB changed its item-code format mid-file, and produced a confident wrong answer. The check is one line and it is the only thing that catches this class of bug.

## Personal data

The employee registry holds **identity**, not the employment file. Name, role, status, joining date and work phone are operational — a stock-count app legitimately needs to know who counted. Salary, NID and passport numbers, bank details, contracts, medical and disciplinary records are **not**, and must not be joined into an ops database because one module happened to need a name.

Practical rules:

- Registry tables may be read broadly. Anything in an HR system is read by named people only.
- Never copy credentials into an operational sheet or repo. The `WUP Outlet Dashboard` currently stores bKash portal, ISP, router and CCTV passwords for 15 sites in plaintext in a shared Drive file — that is the pattern to avoid, and to unwind.
- Customer phone numbers appear in the Surprise Card redemption logs. Treat them as personal data: keep them out of dashboards and exports that don't need them.

## Loyalty at the till

The Surprise Card appears in the POS as two zero-value complimentary categories, and the distinction is the whole programme:

```
SURPRISE CARD        issue      one card per BDT 500 spent
SURPRISE CARD ITEM   redeem     prize SKUs, prefixed "SI "
```

Model them as `complimentary_qty` on the order line, not as a discount and not as a BDT 0 sale. Collapsing the two into one "free item" flag destroys the only measurement the programme has. Note that `SI Crunchy Chia Pudding` currently has **no product code** in GiantSoft — it will fall out of any code-keyed report until ops fixes it.

## Export file naming

Reports arrive from three systems with no useful filenames — GiantSoft stamps a .NET tick (`639220220886550000.csv`) with no outlet and no date anywhere inside the file. Rename on download, always:

```
{system}_{outlet-or-ALL}_{report-type}_{YYYYMMDD}-{YYYYMMDD}.csv

giantsoft_WUP-FS-01_item-sales_20260701-20260731.csv
zab_ALL_sales-detail_20260701-20260731.csv
foodpanda_ALL_orders_20260701-20260731.csv
```

## Migrating off the Excel sheets

The current inventory workbooks are the source of truth until replaced. When importing:

- Treat every sheet as untrusted: log rejects, don't silently coerce.
- Map free-text item names to `sku` through an explicit alias table, and keep it — the aliases will keep arriving.
- Preserve the original row in `raw_import` so any mapping mistake is recoverable.
- Import history read-only; run the new system in parallel for at least one full cycle before cutting over.
