# WaffleUp systems architecture

How the pieces fit, and the order to build them in so each one makes the next cheaper rather than more expensive.

This is the *shape* of the system. `data/CONVENTIONS.md` is the vocabulary. `waffleup-marketing-kit/ROADMAP.md` is the schedule. Read this one first.

---

## The one idea

**Three registries, then facts, then views.**

```
        ┌──────────────── REGISTRIES ─────────────────┐
        │   PLACES          THINGS         PEOPLE     │   mutable, small,
        │   outlet          item           employee   │   one row per real
        │   15 rows         ~30 rows       ~200 rows  │   thing in the world
        └──────┬───────────────┬──────────────┬───────┘
               │               │              │
        ┌──────┴───────────────┴──────────────┴───────┐
        │                  FACTS                       │  append-only, large,
        │  sale · attendance · count · wastage ·       │  every row points at
        │  redemption · assignment · movement          │  all three registries
        └──────────────────────┬───────────────────────┘
                               │
        ┌──────────────────────┴───────────────────────┐
        │                  VIEWS                        │  derived, disposable,
        │  revenue · margin · stock · SOP compliance ·  │  rebuild any time
        │  loyalty · staff performance                  │
        └───────────────────────────────────────────────┘
```

Everything WaffleUp is trying to build — POS reconciliation, inventory, SOP checklists, wastage, the Surprise Card service, dashboards, eventually Odoo — is either a registry, a fact writer, or a view. Nothing else.

**The failure mode this prevents:** each new module inventing its own copy of "outlet", "item" and "employee". That is exactly how the business ended up with four spellings of the same waffle and two incompatible outlet-numbering schemes. Once two modules disagree on what a person is, no report can ever join them.

---

## Status of the three registries

Two are essentially done. One isn't, and it is the smallest of the three.

### PLACES — done ✅

`data/outlets.json` v2.0.0. 15 trading sites, ops codes (`WUP-FS-01`, `WUP-FC-03`, `WUP-CK-04`), status, POS, hours, BIN, legal entity, Foodpanda store IDs.

### THINGS — mostly done ⚠️

`data/menu.json` v2.0.0. POS-verified prices, both price books. **Missing: the alias table.** Each SKU needs its GiantSoft product code, its four ZAB item codes and its Foodpanda display string attached. That's Phase 1 of the roadmap and it's a ~30-row CSV.

Note that items are the one registry where WaffleUp must **mint** its own IDs — no system currently holds a company-wide product code. Places and people already have IDs; items don't.

### PEOPLE — exists, undocumented ⚠️

This was the surprise. There is already a **stable, company-wide numeric employee ID**, and it is the single most valuable identifier in the business because it appears in three otherwise-disconnected systems:

| System | Where the ID appears | Evidence |
|---|---|---|
| **Fingerprint attendance** | `WUP Attendance (…).xlsx`, keyed `ID, NAME`, with `LATE / EARLY LEFT / OVERTIME / DAY OFF / LEAVE / ABSENT / SLOT` | Jan 2024 export, IDs 101–199 and 401–450 |
| **HR roster** | `WUP HR LIVE (Sep–Dec 25)` — daily roster per branch plus an ID ↔ name table | Dec 2025, IDs extending to 567 |
| **GiantSoft POS** | `User Id` on every Surprise Card redemption row | 2026, 45 distinct staff, IDs to 666 |
| **Document filing** | `HR 2024-25/Employee Profile/` has folders literally named `101`, `102` | — |

Cross-checked: of the 8 IDs present in both the Jan-2024 attendance export and the Dec-2025 roster, **8 of 8 resolve to the same person** across a 23-month gap. POS user `494` — 199 redemptions — is the same `494` in the roster.

So the people registry does not need designing. It needs *writing down*. Two tables, seeded from files that already exist.

> **Consequence: `data/CONVENTIONS.md` v1 was wrong to propose `WUP-EMP-{n}`.** Minting a parallel employee ID would have thrown away a live join across attendance, HR and the POS. Corrected there. The rule generalises: **adopt identifiers, don't mint them** — mint only where none exists, which today is items alone.

---

## Five rules that keep this gradual

### 1. Adopt IDs, don't mint them

Before designing an identifier, search the business for one. Outlets had codes. People had codes. Both were invented independently inside this kit before anyone looked, and both had to be corrected. Only mint when a genuine search finds nothing.

### 2. Assignment is a fact, not an attribute

Do **not** write `employee.outlet_id`. Staff rotate constantly — 27 of the 45 staff IDs in the 2026 POS data appear at more than one outlet in the same period, and the HR roster is maintained *daily per branch* precisely because of it.

```
✗  employee (employee_id, name, outlet_id, shift)
✓  employee   (employee_id, name, role, status, joined_on)
   assignment (employee_id, outlet_id, work_date, slot, is_cashier)
```

The same reasoning applies to price (`price` is a fact with `valid_from`, not a column on `item`) and to stock (a movement, never an updated quantity). **Anything that changes over time is a row, not a field.** This is the single most expensive mistake to make early and the cheapest to avoid.

### 3. External identifiers are aliases, never keys

Foodpanda store IDs, ZAB invoice prefixes, GiantSoft product codes, bKash merchant IDs — all of these belong to somebody else and all of them will change. Store them beside your key; never join on them, and never let one become the primary key.

### 4. Facts are append-only; registries are mutable

You correct a person's name in place. You never edit a shift that happened, a count that was taken, or a sale that was rung. Corrections are new rows. This is what makes the system auditable, and it's the opposite of how the current Excel workbooks behave.

### 5. Reconcile on ingest, loudly

Every import checks its parsed total against the source report's own printed total and refuses to load on mismatch. This is not theoretical: building the July analysis, a parser silently dropped half the Chef's Table month when ZAB changed its item-code format mid-file and produced a confident, entirely wrong answer. One reconciliation line catches that class of bug; nothing else does.

---

## Build order, and why

Each step is useful alone and unlocks the next. The dependency is real, not aesthetic.

```
0    Secure what's exposed          credentials out of a shared sheet
     │
0.5  PEOPLE registry               ~1 week   ── unlocks every staff-attributed fact
     │
1    THINGS alias table            2–3 wks   ── unlocks every cross-system comparison
     │
2    Sales ingestion + revenue     3–4 wks   ── needs 1; better with 0.5 (who rang it)
     │
3    Surprise Card redemption      4–6 wks   ── needs 0.5 (who redeemed) + 1 (which prize)
     │
4    SOP / wastage / stock counts  ── needs 0.5 (who counted) + 1 (what was counted)
     │
5    Marketing reads the numbers   ── needs 2
     │
6    HR proper: payroll, leave     ── needs 0.5, and only 0.5
     │
7    Odoo back office / MRP        ── needs 1, 2, 4. See ODOO.md
```

**Why people come before things.** Not because people matter more, but because the people registry is a week and the things registry is three, and *every* fact table in steps 2–4 wants an `employee_id` column. Adding that column later means backfilling every row you wrote without it — and you can't backfill who did something after the fact.

**Why full HR comes near the end.** Payroll, leave balances, increments, contracts and salary certificates are a genuine project, and *nothing* in steps 1–5 needs any of it. Splitting the registry out from HR is what lets the useful 5% ship in a week instead of waiting a quarter behind the other 95%.

---

## The people registry, in full

This is the whole of step 0.5. Two tables.

```sql
employee (
  employee_id     text primary key,   -- the EXISTING numeric ID: '110', '494'
  full_name       text not null,
  known_as        text,               -- rosters use short names; POS uses these
  role            text,
  status          text,               -- active | inactive | left
  joined_on       date,
  left_on         date,
  phone           text
)

assignment (
  assignment_id   text primary key,
  employee_id     text references employee,
  outlet_id       text references outlet,
  work_date       date not null,
  slot            text,               -- 'A' | 'B' | 'C', as the attendance device records
  is_cashier      boolean default false
)
```

**Seed it from** `WUP HR LIVE` (roster + ID↔name) and the attendance exports (ID↔name, and the ID space). **Reconcile against** the GiantSoft user/cashier list so POS `User Id` is provably the same key.

**Deliberately excluded from this registry:** salary, NID and passport numbers, bank details, contracts, medical or disciplinary records. Those belong in an HR system with real access control and a named owner — not in a database that a stock-count app connects to. Step 0.5 stores *identity*, not *employment file*.

### Two things to settle while building it

- **The ID space is sparse and blocked** — 101–199, then 401–450, extending to 567 and beyond. Gaps are frequent. Find out whether the blocks mean something (head office vs outlet, cohort, contract type) and whether numbers are ever reused. If they are reused, the ID is not a safe primary key and needs a surrogate.
- **`SLOT` is recorded as A / B / C** by the attendance device. `data/CONVENTIONS.md` v1 guessed `opening | mid | closing`. Use the letters the device emits and map them to human names in a lookup — don't rename data at the source.

---

## What every module owes the spine

A module is ready to ship when it can answer all four:

1. Which registry rows does it reference? (It must reference, not copy.)
2. Which facts does it write, and are they append-only?
3. What does it do with an identifier it doesn't recognise? (Reject queue for a human — never a fuzzy match, never silent creation.)
4. How does it reconcile on ingest, and what does it do when reconciliation fails?

If a module can't name the registry rows it depends on, it is about to create its own. That's the moment to stop.

---

## Where this leaves Odoo

Unchanged from `ODOO.md`, and this architecture is why the recommendation holds: Odoo is a strong back office and a weak outlet counter. The three registries and the facts layer are **yours** regardless of what software sits on top. Build the spine outside Odoo, keep it in plain Postgres following `data/CONVENTIONS.md`, and let Odoo consume it for inventory, MRP and accounting.

That way the fragmented POS estate can be replaced, or Odoo can be replaced, without touching the layer that actually holds the business's meaning.

---

## Related

- `data/CONVENTIONS.md` — identifiers, enums, formats, entity sketch, ingest rules
- `data/outlets.json` · `data/menu.json` — two of the three registries, live
- `ODOO.md` — where Odoo fits and where it doesn't
- `waffleup-marketing-kit/ROADMAP.md` — the phased schedule
- `waffleup-marketing-kit/data/POS-AND-REPORTING.md` — what each source system emits
- `waffleup-marketing-kit/data/DATA-REQUESTS.md` — what's still needed to proceed
