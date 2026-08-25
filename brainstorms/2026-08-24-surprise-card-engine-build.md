# Surprise Card Engine — Build Grill / Discovery Notes

Date: 24 Aug 2026 · Goal: settle every decision needed to build the Surprise Card engine
into the WaffleUp admin panel (`waffleupadmin`), then build it.

**Method:** grill-me. One question at a time, each with a recommended answer. Every answer is
checkpointed here before the next question is asked. This file is the source of truth, not the
conversation.

**Distinct from** `2026-08-24-surprise-card-engine-grill.md`, which closed the *programme* design
(and produced `programs/SURPRISE-CARD-GUIDELINE.md` v2.0). This session closes the *build*.

## Inputs read before starting

- `Brand_Assets/programs/SURPRISE-CARD-GUIDELINE.md` v2.0 — Part B §11–§16 read in full
- `Brand_Assets/brainstorms/2026-08-24-surprise-card-engine-grill.md` (prior programme grill)
- `Brand_Assets/data/characters.json` — 10 characters, ids kebab-case
  (`mr-waffle`, `air-maxi`, `bhoppu`, `picchi`, `stovy`, `swirly`, `tvy`, `spacy`, `icy`, `merlulu`)
- `waffleupadmin`: `BUILD_STATUS.md`, `package.json`, `docs/implementation-plans/18`, `/19`,
  `lib/navigation/module-registry.ts`, `lib/config/feature-flags.ts`,
  `supabase/migrations/*` (15 applied, latest `202608190001`), `components/ui/*`

## What the codebase already answers (not asked)

| Question | Answer found in repo |
|---|---|
| Stack | Next.js 16 / React 19 / TypeScript / Supabase Postgres / zod. Modular monolith, ADR 0001 |
| Migration convention | `supabase/migrations/YYYYMMDDNNNN_name.sql`; RLS on every public table; every function pins `search_path`; CI fails if either regresses |
| Module home | `loyalty` module exists as a **planned** stub (`app/(app)/loyalty/page.tsx`), registry sections already include *Members · Points ledger · Tiers and rules · Rewards catalogue · Character cards* |
| Unfinished surfaces | Must sit behind a server-authoritative feature flag, off by default (`lib/config/feature-flags.ts`) |
| Existing plans covering this | Plan 18 (members + card registry), Plan 19 (ledger, rewards, redemption, POS sync) — both marked *Blocked*, on Plans 05/06 |
| Verification gate | `npm run check` = tokens + brand + env + repo scan + lint + typecheck + test + build |
| Character roster data | `Brand_Assets/data/characters.json`, with printed card bios (spec §12.1 says do not rewrite) |

## Summary / key decisions

**Session outcome:** 13 questions, 13 answered, 0 stalled. Two answers changed the design rather than
confirming it (Q6b, Q10). Build proceeds as `docs/implementation-plans/26-surprise-card-engine.md`.

**The four decisions that reshaped the guideline:**

1. **The entitlement mechanic (Q6b/Q7).** The right to a card comes from the *transaction against a
   phone number*, not from possessing a printed card. The printed number says *which* card; the
   entitlement says the customer *earned* one. Guideline v2.0 has no such concept — it is the largest
   addition in this build, and it closes the serial-guessing hole by construction.
2. **One card per BDT 500, not one per transaction (Q8).** Resolves a real contradiction between §1,
   §7.3 and `cap_cards_per_transaction`. The more expensive reading, chosen deliberately.
3. **The account holder is the payer, and is an adult (Q10).** Minors are an exception path, not a
   user class. Shrinks the child-data surface to a single derived flag.
4. **Customers share Supabase Auth with staff, separated by a service-role-only audience marker (Q4)** —
   because the existing `on_auth_user_created` trigger would otherwise file every customer in the
   staff registry.

**Settled without asking** (answered from the repository, recorded so the reasoning is not lost):

| Decision | Basis |
|---|---|
| Tables in `public`, snake_case, RLS on every one, `search_path` pinned on every function | CI fails if either invariant regresses (`202608190001`) |
| Module home is `loyalty`; its registry sections already name Members, Points ledger, Rewards catalogue, Character cards | `lib/navigation/module-registry.ts:109` |
| §14 owner column → existing roles: Jawat = `system_owner`, Ops = `operations_manager`, Marketing = `marketing_manager`, Finance = `finance_head` | `202608150001_foundation.sql:338`. **No `legal` role exists** — Legal-owned parameters fall to `system_owner`, flagged below |
| New permission keys needed — only `loyalty.read` exists today | `202608180007_module_catalogue_prd_ia.sql:31` |
| Config changes are permission-gated and fully audited, with no approval workflow | §14 asks for "logged with who made it and when", nothing more |
| Every batch records its RNG seed | Makes a generated batch **recomputable by anyone auditing it** — a fairness proof, not just a log line |
| Points are integers throughout; BDT is `numeric`, never float | Invariant 2 requires exact ledger arithmetic |
| Redemption Points are the existing `outlets` registry plus a flag | Avoids a second, drifting location registry |
| Scratch cards are generated with their reward mix and register for 0 points; the operational redemption chain is untouched | §17.2 keeps the chain deliberately; only its WhatsApp step is a later fix (Phase 7) |
| Merch catalogue ships **empty** | §5.1's prices are `[DECISION NEEDED]` illustrations; seeding them would turn an illustration into a price |

**Build sequence agreed (Q14):** plan 26 → migration + RLS → engine service layer with the §11.2
reference table as a test fixture → admin screens → public site. Report at each stage.

## Q&A log

### Q14 — Build sequence and completeness backstop
- **Captured:** plan doc first, then straight through in dependency order, reporting at each stage.
- **Backstop asked:** anything untouched — scratch cards, delivery orders, economics? **"Nothing — go
  build."** Smaller build details are mine to judge.

---

## Open flags (pending input)

| # | Item | Owner | Blocks |
|---|---|---|---|
| 1 | ✅ **Legacy serial files — RECEIVED 24 Aug 2026.** 17 workbooks, batches 1-13, 305,564 importable cards. Importer written and dry-run clean. Three new questions came out of them: see F4-F6 | Jawat | Closed; replaced by F4-F6 |
| 2 | **SMS provider + per-message cost** for phone OTP | Ops | Turning on `loyalty.customer_otp`. Public self-registration stays closed until then |
| 3 | **Legal sign-off** on consent, retention and minor policy | Legal / Jawat | Switching the public site on |
| 4 | **§1 of the guideline must be reworded** — "one Surprise Card" now contradicts the engine (Q8) | Jawat / Marketing | Nothing technical; the document is simply wrong until edited |
| 5 | **Merch point prices, production costs, MRP** | Ops / Finance | The catalogue stays empty and redemption stays flagged off |
| 6 | **Redemption Point list**, and coverage for delivery-only customers | Ops | Which outlets carry the flag |
| 7 | **Item-level COGS** for the scratch reward mix (§18 item 1) | Finance | The 15–25% saving, not the build |
| 8 | **Occasion artwork** — which character carries each of the four editions | Jawat + Sadbin Ahmed | The first occasion edition |
| 8b | ✅ **Pronouns — closed 24 Aug 2026.** All ten confirmed; Swirly she/her, Tvy and Icy it/its. Schema widened to admit `it` | Jawat | Closed |
| 9 | **No `legal` role exists** in the roles table; Legal-owned parameters currently fall to `system_owner` | Jawat | Nothing today; worth correcting when Legal gets a login |
| 10 | **Nothing is deployed and no domain is bought** — the public site needs a host and `waffleup.global` DNS | Jawat | Anyone outside the office seeing this. Plan 04 territory |
| 11 | ⚠ `waffle_up_surprise_card_engine_claude_brief.md` v1.0 — referenced by the guideline, in neither repo. Carried from the prior grill; **downgraded to a note** now that Q1 settled the build as greenfield | Jawat | Nothing |

## Deltas the guideline owes this session

`programs/SURPRISE-CARD-GUIDELINE.md` v2.0 does not yet contain these, and the engine is now ahead of it:

1. **§1 / §2** — the tiered earning rule (one card per BDT 500, capped), replacing "one Surprise Card".
2. **§11 / §12 / §13** — the `card_entitlements` table, and §13.1's ladder rewritten to check an
   entitlement before a serial.
3. **§13.3** — invariants **13** (an entitlement is consumed exactly once) and **14** (a registration
   requires an open entitlement for that phone).
4. **§13.4** — reconciliation becomes three-way: qualifying transactions vs entitlements issued vs
   cards registered, with the issuing staff id attached.
5. **§12.5** — the minor fields reframed as an exception path; the account holder is the payer.
6. **§14** — new parameters: `entitlement_source_staff_app_enabled`, and the confirmation that
   entitlements never expire.

### Q1 — Build from scratch, or integrate an existing engine?
- **Asked:** Part B says it "assumes the existing Surprise Card engine". Is that real running software, or a document?
- **Captured:** **Build it all here.** There is no deployed system to integrate with. Every table in
  §12 gets created inside `waffleupadmin`/Supabase — including the ones Part B treats as
  pre-existing (`cards`, `batches`, serials, scratch redemption, fraud controls, liability). Part B's
  "additions to the existing schema" are therefore read as **one coherent new schema**, not a patch.
- **Consequence:** the engine is greenfield. No legacy schema constrains naming, so it follows this
  repo's conventions (snake_case tables in `public`, RLS on everything, `search_path` pinned).
- **Flags:** the missing `waffle_up_surprise_card_engine_claude_brief.md` no longer blocks the build —
  it is now only of historical interest. Downgraded from blocker to note.

### Q2 — Which surfaces ship in this build?
- **Asked:** engine + admin only, or also the customer-facing site?
- **Captured:** **Engine + admin + public site, all in this repo.** The customer-facing pages
  (account, register a card, collection scoreboard, merch shop) are built here as an
  **unauthenticated route group** in the same Next.js app, alongside the §15 admin screens.
- **Consequences accepted:**
  - The app now has two audiences. Staff routes stay permission-gated; customer routes are public
    and must never reach a staff table. This is an **RLS boundary question, not a routing one.**
  - Needs customer authentication (Q3), minor/guardian consent UI (§9.1), and public brand design —
    the admin design system is an internal tool, not a consumer surface.
  - Registration exists on **both** channels from day one, matching `registrations.channel`
    (`web` / `staff_assisted`). Both must call one single registration path, never two copies of
    the §13.1 validation ladder.
- **Flags:** public-site visual design — reuse admin tokens, or a separate consumer skin? → raised in Q7.

### Q3 — How does a customer prove their phone number?
- **Asked:** every cap in §14 is *per phone*, so an unverified phone makes them advisory.
- **Captured:** **Phone OTP through Supabase Auth, behind a feature flag that ships OFF.**
  Built now, dormant until an SMS vendor is contracted. Follows the repo's existing rule that any
  outward-reaching surface is flag-gated and off by default (`lib/config/feature-flags.ts`).
- **New flag to add:** `loyalty.customer_otp` — risk `outbound`; precondition: a contracted SMS
  provider, a sending identity, and an owner accountable for message cost and delivery.
- **Behaviour while the flag is off:** public registration is closed and says so plainly; the
  **staff-assisted channel still works**, so the entire loop is exercisable at a counter from day one.
- **Flags:** SMS vendor + per-message cost for Bangladesh → Ops. WhatsApp OTP was offered as a
  cheaper alternative and not chosen; it stays available as a later swap because the flag isolates
  the channel.

### Q4 — Customer identity vs staff identity (⚠ found in the schema, not asked in the abstract)
- **Found:** `supabase/migrations/202608150001_foundation.sql:200` — trigger `on_auth_user_created`
  fires on **every** `auth.users` insert and writes a staff `public.profiles` row. Customers signing
  up through Supabase Auth would each land in the staff registry.
- **Verified fail-closed:** `has_permission` and `has_scoped_permission` both require a
  `user_role_assignments` row joined to an **active** profile, so a customer could never pass a
  permission check. The damage is **registry contamination, not privilege escalation.**
- **Captured — decision:** **Shared Supabase Auth, audience-gated trigger.**
  - Customers authenticate through Supabase Auth, so OTP issuance, hashing, rate-limiting and
    session rotation stay Supabase's responsibility rather than hand-rolled.
  - `handle_new_user()` is amended to create a staff profile **only** when the new user is not
    marked `audience = 'customer'`.
  - The marker lives in **`raw_app_meta_data`, which is service-role-writable only** — never in
    `raw_user_meta_data`, which a client can set on itself. Getting this backwards would let anyone
    signing up suppress their own profile row, or worse, claim staff audience.
  - Customers get a `loyalty_customers` row keyed to `auth_user_id`; they never get a `profiles` row.
- **Non-negotiable that ships with it:** RLS tests proving a customer session reads **nothing**
  staff-side — employees, compensation, outlets, audit, platform_* — and that a customer cannot read
  another customer's collection, ledger or phone number.
- **Note:** this modifies a Plan 01 security-critical object, so it is called out in the plan doc and
  in `BUILD_STATUS.md` rather than buried in a migration.

### Q5 — How much ships in this build?
- **Asked:** §17 has nine phases; some are blocked outside this repo.
- **Captured:** **everything that is not blocked, in one build.**

| Ships live | Ships as schema + screens, acting surface flag-gated | Not built |
|---|---|---|
| Full §12 schema **including `trades`** — nothing is ever retrofitted | Merch redemption: PIN issue, stock reservation, collection (needs prices, costs, Redemption Point list) | Card transfer *behaviour* (schema only, §12.14) |
| All §11 algorithms: generation, point draw, two-stage draw, cap normalisation, duplicate conversion | POS reconciliation ingest (needs Plans 05/06 sales data) | Scratch redemption moved out of WhatsApp (Phase 7) |
| All 12 §13.3 invariants, enforced **in the database** | Anomaly detection auto-run (rules built; scheduled run needs `jobs.worker`) | |
| Registration on both channels, duplicate conversion, milestones, append-only ledger | | |
| Every §15 admin screen | | |
| Public account + register + collection loop | | |

- **Rationale for schema-complete-now:** §12.1a is explicit that retrofitting `card_designs` into a
  live `cards` table means re-keying every card ever issued and is "the most expensive thing on this
  spec to add late". The same argument applies to `trades` and to the merch tables.
- **Flags:** merch `point_price` values and production costs → Ops/Finance. Until they land, the
  catalogue ships **empty**, not seeded with the §5.1 illustrative numbers — those are `[DECISION
  NEEDED]` ratios, and seeding them would turn an illustration into a price.

### Q6a — Do we hold the legacy serial numbers?
- **Asked:** Phase 0 registers ~38,556 already-printed cards; nothing in the workspace holds those numbers.
- **Captured (Jawat):** *"those are in files.. we know which number represents what.. But I don't have
  access to that now.. I can share that later.. keep this open.. ask me later for the file.. I think
  this won't stop you from building anything."*
- **Consequence:** the files exist and map number → card. Build the **importer and its contracts now**,
  run it against real data later. Legacy import must be hashed and idempotent (Plan 18 task 5), so
  importing the same file twice cannot double-issue.
- **⚠ OPEN — ask Jawat for the legacy serial files before Phase 0 goes live.** Until they land, the
  legacy pool has no rows and legacy registration has nothing to validate against. Does not block
  building.

### Q6b — Serial format for new print runs → ⚠ answered with a different mechanic entirely
- **Asked:** what should a printed card serial look like, given guessable serials are a fraud hole?
- **Captured (Jawat), verbatim:** *"When a customer buys.. they are giving number.. at orders above
  500 tk, automatically the profile with that number gets a card issued, but which card it's
  unknown.. so when the customer enter the number from his profile, the card is displayed. But one
  cannot try to redeem a card by randomly entering any number as that profile won't have a card
  issued in the first place. This way the problem of serial number type gets solved ig."*
- **What this changes — this is not a small answer.** The entitlement moves from **the printed card**
  to **the phone number on the transaction**:

| Guideline v2.0 assumed | Jawat's mechanic |
|---|---|
| Customer tears a sealed pack, types the printed serial | Customer gives a phone number at the till; the card is issued to that profile automatically |
| §13.1 step 1 validates *"card serial exists"* | There is no serial to type. The check becomes *"does this profile hold an unopened card?"* |
| Guessing a valid serial is the fraud hole | **The hole closes by construction** — an unearned profile simply holds no card |
| Reveal happens when the customer types the number | Reveal happens when the customer opens their profile |

- **Why the fraud argument is genuinely stronger:** serial-guessing, serial-sharing and
  "found a card on the floor" all disappear. The card cannot be detached from the person who earned it.
- **What it costs:** the engine must **learn that a qualifying transaction happened**, in near-real
  time, keyed to a phone number. That is a POS dependency, and POS ingestion is Plans 05/06 — not built.
  Resolved in Q7.
- **Also unresolved:** whether a physical card is still handed over, and if so how the physical object
  and the digital record stay the same card. Resolved in Q7.

### Q7 — Physical card, and how the engine learns a transaction happened
- **Captured (a):** **Both — entitlement + printed number.** The customer still receives a physical
  sealed pack. They type the number from **their own** pack, and it registers **only if their profile
  holds an unredeemed entitlement** earned by a ≥BDT 500 transaction.
  - The printed number says **which** card. The entitlement says they **earned** one.
  - Serial-guessing dies: a guessed number is useless without an entitlement.
  - A found or resold card is worthless to a stranger.
  - **No per-card step is added at the counter** — §13.7's objection is respected.
- **Captured (b):** **Staff app now, POS later.** One issuance path, with the source recorded.
  Staff issue against a phone number today; POS ingestion writes through the *same* path behind a
  flag when Plans 05/06 land. §13.4 then reconciles the two sources against each other.
- **New concept this introduces — `card_entitlements`.** It is not in guideline v2.0 and must be
  designed here:
  - Keyed on **phone number, not customer_id** — at the till the customer may have no account yet.
    It binds to a `loyalty_customers` row when one appears, and an entitlement earned before signup
    is still waiting for them.
  - `source` ∈ `staff_app` / `pos_import` / `delivery_order`, plus outlet, txn reference, txn amount,
    issued_at, issuing staff.
  - `status` ∈ `open` / `consumed` / `voided`, with `consumed_by_registration_id`.
  - **Invariant 13:** an entitlement is consumed exactly once, and a registration consumes exactly
    one. (Extends §13.3, which stops at 12.)
  - **Invariant 14:** a registration binds a card to the customer **only** if an open entitlement
    exists for their phone. This is the new §13.1 step 1.
- **§13.4 gets stronger, not weaker:** entitlements issued vs cards registered vs qualifying POS
  transactions is now a **three-way** reconciliation, and staff-issued entitlements carry the issuing
  staff id — so the "farming nets out to zero" limitation the guideline admits is now detectable.

### Q8 — Cards per transaction (⚠ resolves a contradiction inside guideline v2.0)
- **The contradiction:** §1 [CONFIRMED] says ≥BDT 500 earns *"one Surprise Card"*, but §14 ships
  `cap_cards_per_transaction = 10` (a cap that controls nothing if the answer is always one), and
  §7.3 costs a batch as *"297 cards represents BDT 148,500 of qualifying spend"* — exactly 297 × 500.
- **Captured:** **one card per BDT 500 tier** — `min(floor(amount / earning_threshold_bdt),
  cap_cards_per_transaction)`. A BDT 2,400 transaction earns **four**.
- **Why this is the right reading:** it is the arithmetic §7.3 already uses, it gives
  `cap_cards_per_transaction` a job, it rewards a larger basket, and it removes the incentive to split
  one bill into several transactions.
- **Cost consequence, stated plainly:** programme cost becomes a **fixed proportion of qualifying
  spend** rather than a proportion of qualifying *transactions*. The 3.0% ceiling in §7.4 is measured
  against the same base either way, so the ceiling still holds — but this is the more expensive of the
  two readings and the ceiling monitor matters more because of it.
- **⚠ Guideline edit required:** §1 must be reworded from "one Surprise Card" to the tiered rule, or
  the document contradicts the engine. → owner Jawat/Marketing.

### Q9 — Does an unconsumed entitlement expire?
- **Captured:** **never expires.** The customer is holding a real physical card; refusing it later
  would break §2's promise that no card in a customer's hand is ever worthless.
- **How the liability stays honest:** unconsumed entitlements are reported as an **"unopened cards"**
  line — quantity issued, quantity outstanding, and the expected point value at the §11.2 mean of
  11.59 points per card. Bounded by what was actually issued, so it can never surprise anyone.
- **Distinction to keep straight:** *entitlements* never expire; *issued points* still follow
  `point_inactivity_expiry_months = 12` with the 30-day notice floor. Two different clocks, and the
  second one only starts once points exist.

### Q10 — Minor protection (⚠ Jawat corrected the framing)
- **Captured (Jawat), verbatim:** *"The minor is not buying.. the person who is buying has a phone
  number.. So, an adult is buying the minor.. and the card is being assigned against the number of
  the adult."*
- **Why this matters:** the guideline's §12.5 fields (`year_of_birth`, `is_minor`, `guardian_phone`,
  `guardian_consent_at`) read as though children hold accounts. They do not. **The account holder is
  the payer.** The child collects the physical cards; the adult holds the account, the points and the
  redemption.
- **What that changes:**

| Assumed | Actual |
|---|---|
| Minors are a normal user class needing a consent flow | Minors are an **exception path**, not the default |
| Consent UI is on the main signup road | The main road is an adult giving their own number at the till |
| Heavy child-data collection | **Year of birth is collected for one purpose only** — applying the threshold |

- **Decision:** build to the guideline defaults, with the framing corrected.
  - Accounts are **adult accounts by default**. Signup declares year of birth; `is_minor` is derived
    at `minor_age_threshold = 16`.
  - A self-declared under-16 does not get a free-standing account: it requires a guardian phone and a
    recorded consent timestamp. The §12.5 fields stay in the schema and are exercised only here.
  - No marketing to minors, and a minor never appears on any public-facing display.
  - **An entitlement earned against a phone belongs to that phone's holder** — so a card bought by an
    adult for a child sits in the adult's account, which is what already happens in the shop.
- **Gate, recorded not assumed:** Legal sign-off on the consent, retention and minor policy is a
  **precondition of switching the public site on** — logged the same way Plan 04 logs the unperformed
  restore rehearsal, not quietly waved through. → Legal / Jawat.

### Q11 — Customer-facing language
- **Captured:** **English now, Bangla-ready.** Every user-facing string lives in one translation layer
  from day one, so adding Bangla is a content job and not a rewrite.
- **Rationale:** matches the brand's existing voice — all ten card bios in `data/characters.json` are
  English, and §12.1 forbids rewriting them.
- **Flags:** a Bangla writer, when the time comes → Marketing. Character bios would need a voice-
  preserving translation, not a literal one.

### Q12 — Where the implementation plan lives
- **Captured:** **new `docs/implementation-plans/26-surprise-card-engine.md`, superseding Plans 18 and
  19**, which get a status change and a pointer to 26.
- **Why:** 18 and 19 predate the guideline and predate the entitlement mechanic entirely. Leaving all
  three live would mean three documents describing the same tables and disagreeing. 26 becomes the
  single authority; 18/19 stay readable as history.
- **Carried forward from 18/19 rather than discarded** — these were right and stay binding:
  consent versioning · no silent destructive member merge · hashed idempotent legacy import ·
  deterministic idempotency keys on every ledger entry · refunds as reversals, never deletion ·
  database-level atomic reserve/redeem · balance rebuildable from the ledger · separate permission
  and audit for bulk export · campaign triggers stay off until consent exists.

### Q13 — The public site's look and home
- **Captured:** **same Next.js app, new unauthenticated route group, consumer skin over the same
  generated brand tokens.** One deployment, one database, one auth.
- **Explicitly not reused:** the admin shell's dense data-table look. It is an internal tool; the
  reveal moment is the product.
- **What that obliges:** the consumer routes must meet the same accessibility bar the admin panel
  already holds (`npm run test:a11y`, 53 checks, axe at WCAG 2.2 AA, zero violations) — a public
  surface cannot be the weaker one.
- **Flag:** a public route group in a staff app means the **RLS boundary is the only thing** between
  an anonymous visitor and staff data. Q4's tests are not optional.

---

## Findings from building it

Three things surfaced while implementing the specification. All three are in the
guideline, not in the code.

### F1 — `batch_point_cap = 3160` binds far more often than "occasionally"

Section 11.4 says frequent normalisation means the cap is set too low for the band.
Measured over 1,500 seeded batches at the standard configuration:

| | |
|---|---|
| Uncapped batch total | mean **3,128**, standard deviation **69** |
| The cap, 3,160 | sits **0.46 standard deviations** above the mean |
| Batches needing normalisation | **31%** — roughly one box in three |
| Median reductions when it bites | **41** single-point trims (worst case 185) |
| Effective value per card | drops from **11.586** to **11.532** |

So the published 11.59 average is not quite what ships: about half a percent is
trimmed off by the ceiling. Not a bug — the ceiling is doing its job — but "one
box in three gets trimmed" is a different operational picture from what section
11.4 implies, and the drift means the odds table is very slightly optimistic.

| Cap | Batches normalised | Effective value per card |
|---|---|---|
| 3,160 *(standard)* | 30.9% | 11.532 |
| 3,200 | 14.3% | 11.565 |
| 3,250 | 4.3% | 11.581 |
| **3,300** | **0.9%** | **11.585** |

**Not changed.** `batch_point_cap` is Finance-owned in section 14, so the standard
value ships as specified and the admin panel reports the normalisation rate.
→ **Finance to decide** whether to lift it to ~3,300.

### F2 — Section 11.3's cautionary example is wrong

> *"a weight of 0.033 yields 1 in 92, not 1 in 30"*

Against the **nine** ordinary characters the same paragraph specifies, a weight of
0.033 yields **1 in 274**. The figure 1 in 92 is what three ordinary characters
would give. The formula itself and the 0.3103 result are both correct — only the
warning is miscalculated, and it is exactly the sentence someone would reach for
when sanity-checking a weight. → Jawat / Marketing.

### F3 — Three characters had no confirmed pronouns · ✅ RESOLVED by Jawat, 24 Aug 2026

Raised because Swirly, Tvy and Icy could not be sourced from any canon file and
shipped as they/them rather than being guessed. Jawat supplied the full table:

| Character | Pronoun | Source |
|---|---|---|
| Mr Waffle | he/him | Card bio |
| Air Maxi | he/him | Card bio ("his paw") |
| Bhoppu | he/him | Card bio |
| Stovy | he/him | Card bio |
| Merlulu | he/him | Jawat, 24 Aug 2026 — resolved. Card bio and all canon files updated; next print batch carries "he" |
| Picchi | she/her | Jawat, 23 Aug 2026 |
| Spacy | she/her | Jawat, 23 Aug 2026 — consistent with Picchi |
| **Swirly** | **she/her** | Jawat, 23 Aug 2026 |
| **Tvy** | **it/its** | Jawat — it's a television |
| **Icy** | **it/its** | Jawat — it's a popsicle |

**This did not fit the schema.** The `pronouns` column admitted only
`he` / `she` / `they`, so seeding Tvy and Icy would have failed the check
constraint and taken the whole migration with it. The column now admits
**four** values. `they` remains the default for a character whose pronouns have
not been decided — a guess ends up printed on a card.

Two of the cast being objects rather than people is a real distinction the data
model now carries, not an oversight to tidy away later.

**Also confirmed in the same message:** Merlulu is **universal** from 24 Aug 2026,
no longer Singapore-only. `data/characters.json` already has all ten at
`market: global` and CHARACTER-BIBLE.md line 151 already records the restriction
as void, so nothing needed changing — and the engine has no market concept at
all, so the roster is simply one roster.

---

## What was built (24 Aug 2026)

Plan: `waffleupadmin/docs/implementation-plans/26-surprise-card-engine.md`. Plans 18 and 19 are
marked superseded, with the constraints they established carried forward explicitly.

| Layer | Delivered |
|---|---|
| **Migration** `202608240001` | 26 `loyalty_*` tables, 3 public views, 21 functions, 14 invariants enforced in the database. RLS on every table, `search_path` pinned on every function |
| **Engine** `lib/loyalty/` | Seeded reproducible generation, the point draw, the two-stage character/design draw, cap normalisation, serials with a check character, the section 16 report definitions |
| **Database functions** | The registration ladder, entitlement issue, duplicate conversion, milestone evaluation, ledger append — all atomic, all server-side |
| **Admin** `/loyalty` | Dashboard · characters and designs · batches · entitlements · customers · review queue · reconciliation · merchandise · configuration |
| **Customer** `/surprise` | The Gang, register a card with the reveal, collection scoreboard, shop — behind `loyalty.public_site`, which ships off |
| **Tests** | 69 loyalty unit tests; 203 in the suite; 62 accessibility checks including the public layout |

### Verification actually run

`npm run check` passes end to end — tokens, brand images, environment contract, credential scan,
ESLint, TypeScript, 203 unit tests, production build. `npm run test:a11y` passes 62 checks in real
Chromium with zero axe violations at any impact level.

**⚠ The migration has not been executed against any database.** There are no local Postgres
credentials on this machine and Docker is not installed, so it could not be run here. CI builds a
throwaway Supabase stack and applies every migration in order, so that is the first place it will
run. Two defects were caught by reading rather than by running, and both are fixed:

1. `is_minor` was written as a **generated column using `now()`**. Postgres requires a generation
   expression to be immutable and would have rejected the migration outright. Minority is now
   derived on demand by `loyalty_is_minor()` — which is also the correct behaviour, since a stored
   flag would say "was a minor at signup" and go wrong on a birthday.
2. The `/surprise` routes were **prerendered as static**, which bakes the feature flag into the build.
   Turning `loyalty.public_site` on would have changed nothing and the flag would have looked broken.
   The route group is now `force-dynamic`, matching the precedent already set by `/design-system`.

### Decisions taken inside the build, worth knowing

- **No `point_balance` column.** The guideline calls it "derived from the ledger, never
  authoritative"; a column that must never be trusted is one that will eventually be believed.
  Balances come from a view that sums the ledger.
- **Collection is a table, not the JSON blob the guideline specifies.** It gives invariant 9 —
  a conversion cannot grant a character already held — as a primary key rather than as application logic.
- **No self-update policy on a customer's own row.** Row level security cannot restrict *columns*, so
  a self-update policy would also let a customer set their own `duplicate_credits` or lift their own
  suspension. Customers change their profile through a function that touches two columns.
- **The public site reads two views through the anon role, never a table and never the service role.**
- **Merch catalogue ships empty**, deliberately. Section 5.1's ladder is ratios marked
  `[DECISION NEEDED]`, and seeding it would turn an illustration into a price.


### F4 — Batch 12 is a copy of batch 11 ⚠ NEEDS A DECISION

`WUP Surprise Card - Batch 12 (Jul 26).xlsx` contains **the same 33,500 serials** as
`Batch 11 (May 26)` — identical values, identical `MAY-` prefix — while its summary sheet reads
"SURPRISE CARD BATCH-12 JULY". Every other pair of files across all 13 batches is disjoint; this is
the only collision in 340,064 cells, so it is not a systemic numbering problem.

Two possibilities, and they need very different responses:

| If | Then |
|---|---|
| Batch 12 was never regenerated and **never printed** | Harmless. The file is a working copy. Batch 12 needs real serials before it goes to print |
| Batch 12 **was printed with batch 11's numbers** | **Duplicate physical cards are in circulation.** Two customers can hold the same number, and the engine treats it as one card — first to register wins, second is told "someone's already claimed this one" while holding a genuine card |

The importer takes batch 11 and logs all 33,500 of batch 12's rows as duplicates rather than
failing. Nothing is lost either way, and the question stays visible instead of becoming a constraint
violation at 3am. → **Jawat.**

### F5 — 1,000 scratch cards whose prize was never written down

Batch 9, column 13: 1,000 serials under a **blank heading cell**, with the first serial sitting where
the reward name should be. The cards are real and someone is holding them; what they win is not
recorded anywhere in the workbook. Not imported — a guess here hands out the wrong prize. → **Jawat.**

### F6 — 300 cards that do not say what they are

`WUP_Batch_13_Matcha_Launch.xlsx` has four sheets named only by channel — Flagship, CT, 3rd Party,
Event — each a bare list of card numbers with no indication whether they are character or scratch
cards. 300 cards, none overlapping ORDER_1. Not imported. → **Jawat.**

### F7 — Section 17.1 understates the legacy liability by about 6.8x

The guideline estimates ~38,556 legacy cards worth about BDT 405,000. The workbooks hold **305,564
printed cards**; registering all of them would mint **2,782,620 points ≈ BDT 2.78 million**.

Printed is not the same as held — a large share was never distributed, and the true figure in
customers' pockets is unknown. **The exposure does not change**: the legacy pool caps actual minting
at 50,000 points, **1.8%** of the theoretical maximum, and cards past the pool still complete a
collection while minting nothing.

But the pool is doing far more work than §17.1 credits it with. That section reads as though it
bounds a BDT 405,000 risk; it is really bounding one nearly seven times larger. Worth restating in
the guideline so nobody later raises `legacy_point_pool` thinking they are relaxing a small cap.

### F8 — Character serials only exist from batch 5

Batches 1, 2, 3, 4, 4.1 and 5.1 recorded **scratch cards only**. Roughly 15,400 character cards from
that era were printed with numbers nobody wrote down. They can never be registered, and no amount of
engineering changes that — worth knowing before anyone promises retro-activation covers "every card
you have ever had".

### F9 — Merlulu has been in print since batch 10

Merlulu appears in batches 10, 11, 12 and 13 — in circulation since March 2025. The engine seeds him
`is_print_ready = false` and `roster_state = 'locked'` per the guideline, which is right for
*generation* (the redesign artwork is not approved) but means a customer holding a real Merlulu card
sees a locked silhouette. All of those cards import as `merlulu_first_ed`, so the first-edition story
is intact. **Whether Merlulu should be `live` on the site given how long he has been in packs is
Jawat's call.**
