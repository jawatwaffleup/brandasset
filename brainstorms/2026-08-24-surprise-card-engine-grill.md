# Surprise Card Engine — Grill Session / Discovery Notes

Date: 24 Aug 2026 · Goal: close every loophole in the Surprise Card programme and rebuild
`programs/SURPRISE-CARD-GUIDELINE.md` v1.0 against `brand/CHARACTER-BIBLE.md` (24 Aug 2026).

**Method:** one question at a time, each with a recommended answer. Every answer checkpointed here
before the next question is asked. This file is the source of truth, not the conversation.

**Inputs read before starting:**
- `programs/SURPRISE-CARD-GUIDELINE.md` v1.0 (23 Aug 2026)
- `brand/CHARACTER-BIBLE.md` (24 Aug 2026, DRAFT)
- `CLAUDE.md` §3 value-language rule, §5 character rules
- ⚠ `waffle_up_surprise_card_engine_claude_brief.md` v1.0 (24 Jun 2026) is **referenced but not
  present in this repo.** All statements about the engine's existing tables and fraud controls are
  quoted second-hand from the guideline. **Flag: get the engine brief into the repo.**

---

## Summary / key decisions

**Outcome:** 23 loopholes logged before the session, 9 more found during it. **24 closed, 8 carried
with named owners.** v1.0 is superseded by `programs/SURPRISE-CARD-GUIDELINE.md` v2.0.

**The twelve decisions that shaped v2.0:**
1. Seasons 3×3 regrouped from the Character Bible; **Merlulu becomes a standing rare** (Q1)
2. **A points economy** — reverses v1.0's ban on public points (Q1)
3. **The anchor-price principle** — real MRP, brand never states value (Q2)
4. Flat earning + completion bonus, so completing beats farming (Q3)
5. **3.0% giveaway ceiling**, 1 pt = BDT 1.00 production cost (Q4, Q6)
6. Account + card-number registration, **in-store-only redemption** (Q5)
7. **Tier-skewed 5–18 point band**, cost-invariant to the skew dial (Q6)
8. **Only the season badge expires** — resolves v1.0's hard contradiction (Q7)
9. Card bios stay; only Merlulu she→he (Q8)
10. **Named Redemption Points**, always the standard price book (Q9)
11. Swap Wall dropped, transfer deprioritised; **Bangladesh first** (Q10)
12. **No card redesign** — the sealed pack is the possession proof; **retro-activate the ~38,556
    cards already in the market**, bounded by a 50,000-point legacy pool (Q11, Q12)

**The Hook Charter** (Q3) is the boundary the whole thing is built inside, and §16.5 shows it is also
what keeps the programme outside every loot box regime found.

---

## Loopholes found in the pre-grill read

Numbered so answers can reference them. Status updated as the session resolves them.

### Structural / logical
| # | Loophole | Status |
|---|---|---|
| L1 | **Season expiry and the Full Gang meta-set are mutually exclusive.** §8 recommends cards expire at season end; §3 rewards holding all 9 "across the year". You cannot physically hold a card that expired. v1.0 contains both. | OPEN |
| L2 | Seasons designed as 3×3 for nine characters. Roster is now **ten**. Merlulu is orphaned. | OPEN |
| L3 | The season groupings ("human / object / late-night") were derived from the **printed card bios**, which the Bible demotes to "a historical record of what's printed" and says were over-read. The "Late Shift" thread in particular does not survive the Bible. | OPEN |
| L4 | **Full Gang is defined as 9/9.** Now ambiguous: 9 or 10? | OPEN |

### Print / art
| # | Loophole | Status |
|---|---|---|
| L5 | **Merlulu is unprintable today.** Head option not approved (Bible §6.3), redesign exists only as WhatsApp JPEGs, no `.ai` master, no T-pose. Yet the Bible states the next print batch carries the redesign. Direct contradiction. | OPEN |
| L6 | **The next print run would reprint wrong bios.** §11.1 says `description` comes from `data/characters.json`, "do not rewrite". The Bible says five of those readings describe the wrong character. | OPEN |
| L7 | Card art exists for only 6 of 10 characters (`docs/ASSET-CATALOG` / CLAUDE.md §10). Phase 0 (tick-box strip + colour-in back) assumes card backs exist for the season's three. | OPEN |
| L8 | The colour-in line art on the card back is a **derivative of supplied artwork**, which CLAUDE.md §5 forbids ("no redraws, no restyles"). No named exception for the card back. | OPEN |

### Voice / brand
| # | Loophole | Status |
|---|---|---|
| L9 | **Swirly never speaks** and never appears with a speech bubble. If the card format carries a first-person bio or catchphrase, Swirly's card breaks canon. Mr Waffle's printed card already has a spoken catchphrase against an R2-D2 reference (Bible §6.5). | OPEN |
| L10 | Registration/QR reply copy in §5 is written in a character-adjacent voice. Characters "must not speak in first person until voices are approved" (CLAUDE.md §5). Needs an explicit system-voice vs character-voice rule. | OPEN |
| L11 | Pronoun drift: Picchi is **she** and Merlulu **he** in the Bible. Cards in circulation may say otherwise → two variants of the same character in the wild. Problem or collectible? | OPEN |

### Fraud / integrity — the "no loophole left" core
| # | Loophole | Status |
|---|---|---|
| L12 | **"Registration grants nothing so it needs almost no validation" (§5) is false the moment the season badge exists.** Registration becomes the trigger for a reward, so it inherits the full fraud surface. This is the single biggest hole in v1.0. | OPEN |
| L13 | **Registration and the Swap Wall are in direct conflict.** A registered card is spent. Pin it on the Swap Wall and the next holder gets nothing — or the serial re-registers and one card counts twice. | OPEN |
| L14 | QR is printed at production time → an entire undistributed batch can be scanned before it leaves the box (staff-side farming). No "activated on sale" step exists. | OPEN |
| L15 | A QR is a photograph. Nothing stops a card being registered from a picture posted on social, or a Swap Wall photo. | OPEN |
| L16 | No cap on cards or completions per phone number. Nothing stops farming/resale. | OPEN |
| L17 | Delivery: who puts the card in the box, and what stops skimming between kitchen and rider? | OPEN |
| L18 | Season expiry vs. a customer sitting at 2/3 when the season closes. No grace window defined → customer-anger surface. | OPEN |

### Commercial
| # | Loophole | Status |
|---|---|---|
| L19 | **Which price book governs a redemption?** Chef's Table runs +16–33%. Scratch rewards are costed at standard menu price. A scratch card redeemed at Chef's Table leaks value and misstates liability. Not addressed anywhere in v1.0. | OPEN |
| L20 | **Singapore has no threshold.** BDT 500 doesn't exist there. No SGD threshold, no SG price book, no SG print run, no SG season calendar. §14.6 asks a stale question (a fourth season) and misses the real one. | OPEN |
| L21 | **Franchising ~Aug 2027.** Who funds a reward when a franchisee redeems a card issued by a company outlet? Liability transfer is undefined. | OPEN |
| L22 | `rewards.is_discount = always No` is a dead field. The real control is a wording check on reward names and POS strings. | OPEN |
| L23 | Uniform character distribution is assumed. Priority order is now confirmed (Bhoppu → Icy) — no rarity tier is exploited, and §10 only forbids *raising the character ratio*, not adding a rare. | OPEN |

---

## Q&A log

### Q1 — Season architecture given ten characters

- **Asked:** With 10 characters and the card bios demoted to a historical artefact, how should seasons
  be shaped? Recommended 3×3 regrouped off the Bible's relationship web, with Merlulu held out as a
  standing chase card.
- **Captured — Jawat:** *"Go with your recommended version, but things should be flexible.. like we
  might be able to change the frequency or other things from the admin dashboard we are preparing.."*

**DECIDED — season architecture (resolves L2, L3, L4):**

| Season | Name | Characters | Priority ranks | Why |
|---|---|---|---|---|
| S1 | **The Big and the Small** | Bhoppu · Picchi · Swirly | 1 · 4 · 5 | Bhoppu+Picchi is the Bible's "classic duo"; Swirly is the chaos. Only trio with complete assets. Warmest opener. |
| S2 | **Go Further** | Air Maxi · Spacy · Icy | 2 · 7 · 10 | Ambition, exploration, travel. Spacy landing one season after Picchi turns the future-self link into a reveal. |
| S3 | **Hold the Line** | Mr Waffle · Stovy · Tvy | 3 · 8 · 9 | Tvy↔Stovy — the pairing the Bible calls "completely unexploited". Mascot anchors the year-end slot. |
| — | **Merlulu** | standing rare, all year, never in a season | 6 | Solves the art block (L5); makes Full Gang a genuine chase. |

- Full Gang = **9 season characters + Merlulu = 10**. The Gang is nine; finding Merlulu makes it ten.
- Season completion math unchanged: ~6 cards, ~BDT 3,025, ~6 weeks. Each season carries a top-4 anchor.
- Every season deliberately mixes strong and thin asset coverage rather than stacking the four
  expression-sheet-less characters (Icy/Spacy/Stovy/Tvy) into one weak season.

**NEW REQUIREMENT — nothing in the guideline may be hardcoded.**
The guideline ships a **standard/default configuration**, and every number in it is a dashboard-editable
parameter with a documented safe range and a named owner for changes. Season count, season length,
character count per season, scratch ratio and reward mix are all config, not doctrine.

**NEW SCOPE — a points economy. This is net-new and reverses a v1.0 decision.**
Jawat: *"How the point assignment would work to the character cards, redeem ways, that each point
converts to, redeem percentage tracking, adding merchandise items, setting up their price and
production cost, how much we would be willing to give away through points on what amount of sale etc,
create the engine guideline with a standard version, and keep scope to change those."*

Requirements extracted:
1. Point assignment rules — what a character card is worth, what a scratch card is worth
2. Redemption paths — what points can be exchanged for
3. Conversion — what one point converts to
4. Redemption-percentage tracking (points issued vs points burned)
5. A merchandise catalogue — items, retail price, production cost, stock
6. A giveaway ceiling expressed against sales volume
7. All of it configurable, shipped with a standard default

> ⚠ **This directly reverses v1.0 §10**, which ruled out points as a public currency: *"the engine brief
> is right to hold this back. Keep points internal for liability only until legally reviewed."*
> Jawat's call, taken and proceeding. Consequence: §10 must be rewritten, and the legal review in §15
> now has to cover a stored-value currency, not just a promotional collectible. **New flag → L24.**

- **Flags:** L24 — points become a stored-value liability; legal review scope widens. Owner: Jawat + legal.
- **Flags:** L25 — "merchandise price AND production cost" implies merch may also be *sold*. If the same
  SKU is both sold at retail and priced in points, the customer can derive an exact taka-per-point rate.
  Collides with `CLAUDE.md` §3. Raised as Q2.

### Q2 — Points vs. the value-language rule

- **Asked:** Any point-priced item with a known retail price publishes the taka-per-point rate.
  Recommended points buy only unbuyable things.
- **Captured — Jawat, refining the recommendation:** *"suppose we are willing to give a notebook after
  a customer finishes 6-8 above 500 purchase. In our end, the notebook cost us 80tk to produce. It is
  how we value it. But in customer mind - they dont get a value to assume for it. That is a opportunity
  wasted. Instead, we market/sell that notebook at 200-300 tk mrp.. so when a customer finds out that
  he can get such a notebook of such price by redeeming this character cards, I think it would create
  more drive for them."*

**DECIDED — the anchor-price principle. This supersedes my Option A and refines `CLAUDE.md` §3.**

The value-language rule bans WaffleUp from **naming, quantifying or labelling the value it gives away**.
It does not ban a product from **having a price**. Those are different acts, and the difference is who
does the arithmetic:

| | |
|---|---|
| ✗ **Banned** — the brand states the value | "Redeem for a notebook — worth BDT 250!" · "BDT 250 value" · "you saved" |
| ✓ **Allowed** — the product carries a price and the customer infers | The notebook sits in the WaffleUp shop at BDT 250 with a price tag, like any product. Separately, collectors can unlock it. |

**The drive comes from the customer's own inference, never from the brand's boast.** That is the whole
mechanism, and it is why this works where "worth BDT 250" would not.

**Four binding conditions that keep it clean:**
1. **The MRP must be real.** The item is genuinely sold at that price to paying customers. A phantom
   "RRP" invented to inflate perceived value is both a brand risk and a consumer-protection exposure.
2. **WaffleUp never states value in the redemption context.** No "worth", no "value", no "you saved".
   The price tag does the work; the copy stays silent.
3. **Point prices and taka prices never share a surface for the same item.** The shelf shows BDT. The
   collector view shows points. The customer connects them. The brand never draws the line.
4. **Never a side-by-side comparison** — no "BDT 250 or 400 points".

**Consequences to carry into the guideline:**
- **Merchandise becomes a real retail line, not a prize cupboard.** Inventory, SKUs, stock at outlet,
  POS lines, reorder points. This is new operational scope and it is not currently budgeted. **→ L26**
- The admin dashboard needs **both** numbers per SKU — production cost (for the giveaway ceiling and
  liability) and MRP (for the anchor). Jawat asked for exactly this and the reason is now on record.
- Worked example on his numbers: notebook at BDT 80 production, MRP 200–300, earned at ~6–8 cards
  (~BDT 3,000–4,000 qualifying spend) = **2.0–2.7% of qualifying spend at 100% uptake.** At a realistic
  25% completion uptake it is ~0.67%, which sits comfortably under the 2.5% ceiling — but it **binds at
  high uptake**, i.e. exactly when the mechanic is working. Ceiling needs restating against points. **→ L27**
- v1.0 §10's ban on public points is formally withdrawn (see L24).

- **Flags:** L26 — merch retail line is unbudgeted ops scope (stock, SKUs, reorder). Owner: ops lead.
- **Flags:** L27 — 2.5% ceiling must be recomputed with points included. Blocked on item-level COGS.

### Q3 — Point earning structure, and the "hook"

- **Asked:** What earns points, and how do we stop points cannibalising the collection game?
- **Captured — Jawat:** Confirmed flat-points-plus-completion-bonus. Then: *"keep rare big win
  opportunity.. It would attract more people... create hook the way most addictive games do.. just in
  our own version. We are only giving the cards, if we cannot hook people to it, none would actually
  value it.. And no serious addiction can ever be created with such mild implementation.. but you
  should do in depth research on how we can ensure that children & people get hooked and ensure repeat
  customers.. at the end out target is to sell the street desert to more people or more amount. And
  with creating merchandise product presence and building connection of people to the brand."*

**DECIDED — earning structure (standard config, all dashboard-editable):**

| Event | Standard | Range |
|---|---|---|
| Character card registered (duplicates included) | **10 pts** | 5–25 |
| Season complete (3/3) | **+50 pts** | 25–100 |
| Full Gang (10/10, incl. Merlulu) | **+200 pts** | 100–500 |
| Scratch card | **0 pts** — it already paid out in food | fixed |

Farming 6 random cards = 60 pts. Completing a season = 80 pts. **Completing is strictly better, and the
maths does the persuading** — no copy has to argue for it.

**DECIDED — three rarity tiers. This is the hook Jawat is asking for.**

| Tier | What | Standard rate | Wins |
|---|---|---|---|
| **Common** | Character card | ~91% of cards | Points + set progress |
| **Frequent small win** | Scratch card | ~9.09% (27/297) | Food, as today. Unchanged — it works |
| **Rare chase** | **Merlulu** | ~1 in 30 cards | Large point bonus + completes the Gang + status |
| **Ultra-rare** | **The Golden Waffle** | ~1 in 5,000–10,000 | The big win — see below |

**The Golden Waffle.** A third card type, a handful issued a year, announced publicly every single time
it is found. It wins a bundle that is deliberately **unbuyable and story-shaped, never cash-shaped**:
- **A year of waffles** — one a week for a year. High perceived value, low true cost, spread across 52
  weeks, and the prize *is* 52 repeat visits. The single most efficient prize in the programme.
- **The 3D-printed figurine of their chosen character.** The `.stl` assets exist and are unused. Dropped
  in v1.0 §4.2 as a *ladder* item because of the per-unit cost tail — as a handful-per-year ultra-rare
  that tail disappears entirely, and it becomes the most photographed object the brand owns.
- **Wall of Fame at their home outlet, and on social.** Zero cost, maximum status.

Every find is a content beat that WaffleUp does not have to invent. **→ this is the answer to "if we
cannot hook people to it, none would actually value it."** Scarcity of a *thing* is permitted by the
value-language rule; scarcity of a *price* is not.

---

**THE HOOK CHARTER — boundaries I am designing to, stated so nothing drifts later.**

Raised with Jawat, 24 Aug 2026. The commercial argument, not only the ethical one: the audience on file
starts at **age 10**, randomised chase mechanics aimed at minors are what regulators have actually moved
against, `SURPRISE-CARD-GUIDELINE` §15 already flags it, and Waffle Up Global is a **Singapore-registered
entity expanding into UAE, Thailand and Indonesia**. That is the wrong risk profile to test.

Designing for **anticipation, scarcity and status** — not compulsion. Concretely:

| Permitted — and used hard | Not built |
|---|---|
| Variable-ratio reward (the scratch card, the chase, the Golden Waffle) | Any purchase made *solely* to buy a chance |
| Scarcity of a thing — season ends, limited edition, ultra-rare | Countdown-to-a-price urgency (already banned by §4.6) |
| Visible progress — "2 of 3", the folder, the scoreboard | Streak-loss guilt, decaying balances, "you'll lose it" |
| Social proof, trading, Wall of Fame, near-miss content | Push messaging engineered at minors |
| Collection completion, status tiers, early access | Paid re-rolls, paid conversion, buying points or cards |

**The bright line — and it is also the legal one:** *a card only ever arrives with a purchase the
customer chose to make. No card is ever sold, and no chance is ever purchasable.* That is the
distinction between a promotional collectible and a loot box, and the entire compliance position rests
on it. **It must never be crossed, in any market, for any campaign.** **→ L28, binding.**

Additional guards to spec:
- Under-16 registration requires a parent/guardian phone number and consent. **→ L29**
- Season deadlines attach to the season, never to the person ("The Street ends in 3 weeks", never "your
  progress dies in 3 weeks").
- Points never expire silently — notice period, dashboard-configurable, minimum 30 days.

- **Flags:** L28 — "no chance is ever purchasable" is the load-bearing compliance line. Owner: Jawat + legal.
- **Flags:** L29 — under-16 consent flow. Owner: legal + engine build.
- **DELIVERABLE REQUESTED:** in-depth research on what makes collectible programmes drive repeat
  purchase (Pokémon, Panini, Happy Meal, Monopoly) **and** what regulators have done about them.
  Jawat asked for this explicitly. To run after the grill; will inform §s on hook design and compliance.

### Q4 — Giveaway ceiling and the point rate

- **Asked:** What total giveaway ceiling, as % of qualifying revenue?
- **Captured — Jawat:** Selected **3.0% ceiling, 1 pt = BDT 0.80 production cost.**

**DECIDED — the point economy standard config (resolves L27):**

| Parameter | Standard | Note |
|---|---|---|
| 1 point | **BDT 0.80 production cost** (≈ BDT 2.50 MRP) | dashboard-editable |
| Notebook (worked example) | **100 pts** · BDT 80 cost · BDT 250 MRP | ~6–8 cards, ~BDT 3,000–4,000 spend |
| **Total giveaway ceiling** | **3.0% of qualifying revenue** | up from v1.0's 2.5% — points are new spend |

Modelled monthly at 9,639 cards / BDT 4,819,500 qualifying revenue:

| Scenario | All-in cost |
|---|---|
| Realistic (40% registration, 70% burn) | ~1.4% |
| Everything registers and everything burns | ~2.7% |
| **Ceiling** | **3.0%** |

**Three rules that make the ceiling behave:**
1. **Express and review it as a rate,** never a flat taka figure — it self-scales as the business grows.
2. **If you breach it, raise it — never claw back.** A breach means the mechanic is working.
3. ⭐ **Never devalue points already issued.** The lever is the *catalogue going forward* — which items are
   listed, at what point price — never the balance a customer already holds. Re-pricing issued points is
   the cardinal sin of loyalty programmes and it is a trust and liability event, not a cost saving.
   **→ binding, L30.**

- **Flags:** L30 — "never devalue issued points" must be enforced in the schema: point prices are
  versioned per catalogue entry, balances are immutable. Owner: engine build.

### Q5 — Registration integrity, and Jawat's account-based redemption design

- **Asked:** A printed QR is registerable from a photo. How does a card prove possession?
- **Captured — Jawat proposed a fuller architecture instead:**

> *"what if we add a customer login option as well.. - maybe to the same place where they can buy our
> merchandise products as well.. Suppose a customer has collected a card, he can log in to our website..
> there is a unique number in each card.. he enters the card number and the card gets registered to
> him..(only cards already distributed would work),, After each card registration - the point he would
> get might be a bit variable.. (there would be range for each cards - superior cards gets more value -
> (you know the order).. But all these calculation should abide by the set threshold.. they can opt to
> redeem when they get a merchandise equivalent point in their profile.. There would be fixed few
> outlets from where they would be able to redeem.. and the way they get order confirmation msg, they
> would also get redeem msgs.. eg, after they confirm a notebook or a water bottle redeem with their
> points - they choose which outlet they would be collecting from..then they get a msg with a pin,
> product name, and redeem outlet name in their phone.. they go to the outlet, show the PIN, and collect
> the product.. It might increase the number of people coming to outlets as well. so i was thinking not
> to keep any delivery option in point redeem. however, there would be delivery option in case of
> products they buy with their money. This is a very rough plan.. validate it against existing
> examples.. would such thing work?"*

**Design as proposed — the eight moving parts:**
1. Customer account on the WaffleUp website, same place as the merch store
2. Unique number on each card, entered manually to register
3. Only already-distributed cards can register
4. Variable points per card, ranged; higher-priority characters worth more
5. All within the 3.0% threshold
6. Redeem once the balance reaches a merch item's point price
7. A small fixed set of redemption outlets
8. SMS with PIN + product + outlet → collect in person. **No delivery on point redemptions** (footfall
   is the point); delivery stays available for cash purchases.

**Status: validating against real programmes before I commit it to the guideline.** Research requested
by Jawat and pending — findings and verdict recorded below in Q5a.

**Open concerns flagged on first read, to be tested by the research:**
- **C1 — the photo attack is not closed.** A card number printed in the open is still readable in a
  photograph. His design and my PIN proposal are complementary, not alternatives: **open serial for
  HQ/ops reconciliation + hidden code under latex for registration.** That is the Coke-under-the-cap
  pattern. Recommend merging them.
- **C2 — "only distributed cards work" implies batch-level activation.** Outlets mark a batch as issued
  when they open it. Much lighter than per-card POS activation and it kills the undistributed-box attack.
- **C3 — variable points by character rank creates junk cards.** If Icy is designated low-value and is no
  rarer than Bhoppu, the bottom of the roster becomes visibly worthless and the set feels unfair.
  In collectibles, value follows **scarcity**, not designation. Counter-proposal in Q5a.
- **C4 — cloud kitchens have no counter.** Two of the 15 sites are cloud kitchens and delivery-only
  customers may have no reachable redemption outlet. Redemption-outlet selection needs care or a
  segment of customers can earn but never redeem.
- **C5 — stock reservation is missing.** If a PIN is issued but the item is gone when the customer
  arrives, that is the single worst experience the programme can produce. Reserving stock against the
  PIN at the moment of redemption is mandatory, not optional.
- **C6 — PIN resale.** A PIN alone is bearer-instrument. Bind it to the registered phone number and
  have staff confirm the last 4 digits.
- **C7 — scope.** "Login + merch store" is an e-commerce build. Not currently budgeted anywhere.

### Q5a — Research: does Jawat's design work? Validation against real programmes

Requested by Jawat, 24 Aug 2026. Sources listed at the end of this section.

**VERDICT: Yes. It is the standard architecture for this exact problem, and the evidence supports all
four of his instincts. Five corrections and two additions below.**

#### What the evidence confirms

**1 · Code-on-pack → account → points → merchandise is a mature, proven pattern.**
It is a productised category (Open Loyalty "code scanning"; long-running FMCG pack-code programmes;
Ghost Lifestyle rewards). The documented standard controls are precisely the ones this design needs:
**unique single-use codes, usage limits per member, granular usage tracking.** Jawat independently
arrived at the industry-standard shape.

**2 · In-store-only redemption is evidence-backed, not just intuition.**
- The **"redemption halo"**: members returning to redeem make *additional purchases* on that visit.
  Redemption is itself a traffic driver, separate from the reward's value.
- **Thorntons (convenience, Paytronix): one extra visit per member per month**, described as adding
  substantial money to the bottom line.
- Brands with physical locations see **higher** redemption, because staff can explain the options.
- ⇒ **Jawat's "no delivery on point redemption" call is correct and I withdraw any hesitation.**

**3 · Redemption thresholds must be reachable in weeks, not months.**
Explicitly called out as a condition for in-store redemption driving incremental visits. This
independently validates the 6-week season and the ~100-point notebook. The old 28-card / 6.5-month
design was failing a documented rule.

**4 · Real planning numbers, replacing our guesses:**

| Benchmark | Figure | What it means here |
|---|---|---|
| Redeemers vs non-redeemers | **Redeemers spend 3.1×** | The business case for the whole programme |
| Healthy programme | **20–30% of active members redeem in a period** | Our 25% uptake assumption is right on benchmark |
| Average breakage | **~50% of rewards go unredeemed** | We modelled 70% burn — we are **conservative**, good |
| The KPI that counts | **Incremental lift vs a matched non-member group** | Sharpens the ⭐ metric: not "do collectors visit more" but "do they visit more *than a matched control*" |

**5 · The compliance position is stronger than §15 assumed. This is the most important finding.**
Every regime found targets **PAID** randomness, not free-with-purchase:
- **Belgium & Netherlands** — banned **paid** loot boxes as illegal gambling.
- **PEGI** — minimum **16 rating** for **paid** random items (loot boxes, card packs, gacha, prize wheels).
- **Brazil** — 2025 law prohibiting loot box **sales** to under-18s, effective March 2026.
- **US FTC (Cognosphere)** — parental consent for under-16 **purchases**; disclose accurate probabilities.
- **EU Digital Fairness Act** — expected to move against loot boxes in games accessible to minors.

⇒ **WaffleUp's cards arrive with a purchase the customer already chose to make and are never sold.
That places the programme outside the loot box definition in every jurisdiction found.** The bright line
in the Hook Charter (**L28**) is not a cautious preference — it is the single fact that keeps this
programme legal as it scales into new markets. It must be written into the guideline as immovable.

> **Adopt voluntarily:** the FTC settlement required **disclosing accurate probabilities for rare chase
> rewards.** Publishing the odds (scratch ~9.09%, Merlulu ~1 in 30, Golden Waffle ~1 in 5,000–10,000)
> costs nothing, builds trust, is great content in its own right, and future-proofs against the direction
> every regulator is moving. **→ new recommendation, R1.**

#### ⚠ 6 · The failure mode of success — and it is a real one

**McDonald's Japan ended its Pokémon Happy Meal promotion early (Aug 2025)** because customers bought
meals purely for the cards and **discarded the food**, with resale markets and hoarding driving it.
McDonald's now runs **purchase caps (six per group) and blocks delivery apps for the first three days**
of a card promotion.

Read across to WaffleUp:
- The BDT 500 threshold is a natural brake — hoarding is expensive here in a way a Happy Meal is not.
- But a **Golden Waffle** chase is exactly the mechanic that produces this behaviour.
- ⇒ **Anti-scalping caps are mandatory, not optional.** Cap cards registered per phone per day and per
  season; cap completions per phone per season; flag sequential-serial registration. **→ resolves L16.**
- ⇒ Never let a single transaction issue an unbounded number of cards.

#### Corrections to the proposed design

| # | Correction | Why |
|---|---|---|
| C1 | **Merge the card number with the hidden PIN.** Open serial printed for HQ/ops reconciliation; **registration code under a latex scratch panel.** | An open number is readable in a photograph. This is the under-the-cap pattern and it is what "unique single-use code" means in practice. |
| C2 | **Batch-level activation.** Outlet marks a batch issued on opening; only cards in issued batches can register. | Delivers Jawat's "only distributed cards work" without adding a POS step. |
| C3 | **Do not scale points by character rank.** See Q6. | Designating Icy low-value creates junk cards and makes the set feel unfair. Value should follow scarcity, not rank. |
| C4 | **Redemption-outlet coverage.** 2 of 15 sites are cloud kitchens with no counter. | A delivery-only customer must not be able to earn but never redeem. |
| C5 | **Reserve stock against the PIN at redemption.** | A PIN issued for an item that is gone on arrival is the worst experience the programme can produce. |
| C6 | **Bind the PIN to the registered phone number**; staff confirm last 4 digits. | An unbound PIN is a bearer instrument and will be resold. |
| C7 | **Login + merch store is an e-commerce build** — unbudgeted scope. | Flag to ops/tech before it is assumed. |

**Sources:**
[Open Loyalty — Code Scanning](https://www.openloyalty.io/product/code-scanning) ·
[Rivo — Points Program Redemption Rate benchmarks](https://www.rivo.io/blog/points-program-redemption-rate) ·
[Voucherify — Loyalty breakage](https://www.voucherify.io/glossary/loyalty-breakage) ·
[Exchange Solutions — Redemption glossary](https://exchangesolutions.com/glossary/redemption/) ·
[Paytronix — Effectiveness of loyalty programs](https://www.paytronix.com/blog/effectiveness-of-loyalty-programs) ·
[Restaurant Business — Demand for McDonald's Pokémon cards](https://www.restaurantbusinessonline.com/marketing/demand-mcdonalds-pokemon-cards-goes-through-roof) ·
[Attack of the Fanboy — McDonald's caps Pokémon Happy Meals, blocks delivery apps](https://attackofthefanboy.com/news/mcdonalds-caps-new-pokemon-happy-meal-at-six-per-group-and-blocks-delivery-apps-for-three-days-after-past-promo-sold-out-in-24-hours/) ·
[Yahoo/People — McDonald's ends Pokémon promo early over discarded food](https://www.yahoo.com/news/articles/mcdonalds-ends-pokemon-promo-early-173000472.html) ·
[Promise Legal — Loot box laws by jurisdiction 2025](https://blog.promise.legal/loot-box-laws-game-developers/) ·
[Programming Insider — Loot boxes, regulation, where the line sits in 2026](https://programminginsider.com/loot-boxes-regulation-and-where-the-line-sits-in-2026/) ·
[Lexology — Regulation of loot boxes: a global perspective](https://www.lexology.com/library/detail.aspx?g=6779705d-3000-4825-92c4-7c5b8a901ada)

### Q6 — Point value per card: the tier-skewed random band

- **Asked:** Should points scale with character rank? Recommended a flat random band instead.
- **Captured — Jawat:** *"go with your recommended one. but increase uncertainty even more.. make it
  5-18.. and if possible create an algorithm that would make the tier wise variation as well.. like the
  probability of bhoppu card getting 15 would be more than the probability of icy card getting 15. but
  both can get that."*

**DECIDED — tier-skewed random point band. Resolves C3 better than either of my options.**

Full overlap of outcomes, tier-skewed probability. Every character can roll any value in the band; the
hero characters simply trend high. **No card is ever worthless, and a lucky Icy is better content than a
guaranteed-high Bhoppu.**

#### The algorithm — exponential tilt over a discrete band

```
band            = 5 .. 18            (dashboard-editable)
MID  = 11.5,  HALF = 6.5
w_c             = (10 - priority_rank_c) / 9      # 1.0 = Bhoppu ... 0.0 = Icy
theta_c         = s * (2*w_c - 1)                 # s = tier_skew_strength
weight_c(v)     = exp( theta_c * (v - MID) / HALF )   for v in band
P_c(v)          = weight_c(v) / sum(weight_c)
```

One parameter, `s`, controls the whole thing. **s = 0** → every character identical. **s = 2.5** → strongly
tiered. **Standard config: s = 1.0.**

⭐ **The property that makes this safe to ship: the roster-wide mean is exactly 11.50 at every value of
`s`.** The tilt redistributes probability without changing the total. Jawat can turn tiering up or down
from the dashboard and **the programme's cost does not move.** The dial is free.

#### Standard config (s = 1.0) — modelled, not estimated

| Character | Rank | Mean pts | P(rolls 5) | P(rolls 18) | P(≥15) |
|---|---|---|---|---|---|
| Bhoppu | 1 | **13.82** | 2.2% | 16.1% | 52.0% |
| Air Maxi | 2 | 13.36 | 2.9% | 13.9% | 46.8% |
| Mr Waffle | 3 | 12.86 | 3.9% | 11.7% | 41.5% |
| Picchi | 4 | 12.33 | 5.0% | 9.8% | 36.2% |
| Swirly | 5 | 11.78 | 6.4% | 8.0% | 31.1% |
| Merlulu | 6 | 11.22 | 8.0% | 6.4% | 26.2% |
| Spacy | 7 | 10.67 | 9.8% | 5.0% | 21.7% |
| Stovy | 8 | 10.14 | 11.7% | 3.9% | 17.7% |
| Tvy | 9 | 9.64 | 13.9% | 2.9% | 14.1% |
| Icy | 10 | **9.18** | 16.1% | 2.2% | 11.2% |
| | | **avg 11.50** | | | |

An Icy still rolls a perfect 18 roughly **1 time in 45** — and a Bhoppu rolls a 5 exactly as often. The
tier is felt as luck, not as a rule. Alternative strengths modelled: s=0.6 → spread 2.9 · s=1.5 → 6.5 ·
s=2.5 → 8.9 (at 2.5 Icy averages 7.07 and it starts reading as the junk card — **recommended dashboard
range 0–1.5, hard cap 2.5**).

#### ⭐ Roll at generation, never at registration

The value is **assigned deterministically when the card is generated** (seeded hash of serial + secret),
stored on the card record, and merely *revealed* at registration. Four things this buys:
1. **Auditable** — every card's value is fixed and provable before a single card ships.
2. **No re-roll exploit** — nothing to retry, nothing to time.
3. **Liability is known at print time**, not discovered later.
4. ⭐ **The budget ceiling becomes arithmetic, not monitoring.** The generator assigns tier-skewed values
   and then normalises so the **batch total lands on a configured cap.** This is the direct answer to
   Jawat's *"all these calculation should abide by the set threshold."*

#### Revised economics — the band changes the rate

Band 5–18 has mean 11.5, not 10, so issuance rises ~15%. Repricing to hold Jawat's stated intent
(notebook at 6–8 cards) gives **cleaner numbers than before**:

| Parameter | Revised standard | Was |
|---|---|---|
| 1 point | **BDT 1.00 production cost** (≈ BDT 3.00 MRP) | BDT 0.80 |
| Notebook | **80 pts** · BDT 80 cost · BDT 250 MRP | 100 pts |
| Cards to earn the notebook | **~7** (6–8 as Jawat specified) ✓ | ~6–8 |
| **Batch point cap** | **3,100 pts per 297-card batch** | new |

Check against the 3.0% ceiling, per batch of 297 (BDT 148,500 qualifying spend):

| Line | BDT | % of qualifying spend |
|---|---|---|
| Points minted (270 char × 11.5, capped at 3,100) | 3,100 | **2.09%** |
| Scratch rewards at COGS | 1,068–1,602 | 0.72–1.08% |
| **Total if every point burns** | **4,168–4,702** | **2.81–3.17%** |
| **Realistic (40% registration, 50% burn — industry benchmark)** | ~1,900 | **~1.3%** |

Sits inside the 3.0% ceiling at realistic uptake with wide margin, and touches it only at 100%
registration **and** 100% burn **and** the top of the COGS range — a scenario the batch cap can simply
tighten. **The ceiling is now structurally enforced at print time.**

- **Flags:** L31 — batch point cap must be a hard constraint in the card generator, not a report.
  Owner: engine build.

### Q7 — Season expiry vs the Full Gang (L1, L18)

- **Asked:** v1.0 contains both "cards expire at season end" and "collect all nine across the year".
- **Captured — Jawat:** Selected **only the season badge is time-boxed.**

**DECIDED — resolves L1 and L18 completely.**

| Thing | Expires? |
|---|---|
| Registering a card | **Never.** A card can be registered at any time, forever |
| Points awarded | **Never** on the card. Balance expires only after **12 months of total account inactivity, with 30 days' notice** |
| Counts toward Full Gang | **Never expires** — the permanent twelve-month arc |
| Counts toward the **season badge** and its merch | **Only before the season closes** |

**The deadline attaches to the badge, never to the customer.** The treat-buyer still gets the pressure
(§8's lever survives); the habit-buyer still gets the annual arc; and **nothing a customer already holds
is ever taken away** — which removes the worst anger surface in v1.0 and is consistent with the "never
devalue issued points" rule (L30).

**Binding copy rule:**
- ✓ "The Street ends in 3 weeks."  ✗ "Your progress dies in 3 weeks."
- Scarcity attaches to the *thing*, never to the person. Consistent with `CLAUDE.md` §3 and the
  Hook Charter (L28).

### Q8 — What goes on the redesigned card (L6, L11)

- **Asked:** Should the bios be rewritten from the Bible before the next print run?
- **Captured — Jawat:** *"picchi is she, merlulu is he.. We are aware and we are changing the bio of
  merlulu from she to he... Otherwise, the current bios are fine.. these convey double meaning,
  essentially reflecting the same characters as I described earlier."*

**CORRECTION TO MY PREMISE.** The Bible §7's "five of them described the wrong character" refers to the
**voice files** in `brand/character-voices/`, which were written *from* the bios and over-read them —
**not to the bios themselves.** I conflated the two. The bios are intentionally double-meaning and are
consistent with the Bible's characters.

**DECIDED — resolves L6 and L11:**
- **Card bios stay exactly as printed.** `data/characters.json` remains authoritative for card text.
- **Only change: Merlulu's bio, she → he.**
- §11.1's `description` sourced from `data/characters.json`, "do not rewrite", **stands as written.**
- The Bible governs **who the characters are and how they behave in marketing**; the bios govern **what
  is printed on the card**. Both true, no conflict. The thing that was wrong was the voice files, and
  they have already been rewritten.
- No bio-approval blocker on the print run. ✓

**Consequence worth banking:** the Merlulu pronoun change creates a genuine **First Edition Merlulu** —
existing cards say "she", all future cards say "he", and the old ones are never reprinted. That is a real
scarce variant, acquired for free. Worth a content beat when the redesign lands, and worth logging as a
`card_variant` field in the schema so the two are distinguishable. **→ R2.**

**The new card face — confirmed contents:**
| Element | Status |
|---|---|
| Character art (supplied, unmodified) | unchanged |
| Printed bio | **unchanged**, except Merlulu she→he |
| Open serial | **new** — HQ/ops reconciliation |
| Registration code under latex scratch panel | **new** — the possession proof (C1) |
| Season tick-box strip | **new** — Phase 0, visible progress |
| Colour-in line art back | unchanged |

- **Flags:** L8 still open — the colour-in line art is a derivative of supplied artwork and `CLAUDE.md`
  §5 forbids redraws with no stated exception for the card back. Needs an explicit carve-out written
  into `CLAUDE.md`, naming who may produce it. Owner: Jawat.
- **Flags:** L5 still open — Merlulu's redesign has no approved head option and no `.ai` master. He is
  the standing rare, so he does not block Season 1, but he must be print-ready before the Full Gang can
  be completed by anyone. Owner: Jawat (head choice) + Sadbin Ahmed (masters).

### Q9 — Redemption network and price book (L19, C4)

- **Asked:** Where can points be redeemed, and which price book governs a redemption?
- **Captured — Jawat:** Selected **named Redemption Points, standard outlets only.**

**DECIDED:**

| | Rule |
|---|---|
| **Point redemption (merch)** | A **named subset of standard outlets** = "Redemption Points", chosen for footfall and stock space |
| Cloud kitchens | **Excluded** — no counter to collect from |
| Chef's Table | **Excluded initially** — handing over merchandise is off-register for that service format |
| Delivery on point redemption | **Never.** Footfall is the point (evidence: redemption halo, Thorntons +1 visit/member/month) |
| Merch stock | Ships **only** to Redemption Points — keeps inventory and reorder tractable |
| **Scratch food rewards** | Redeemable at **every** outlet, Chef's Table included |
| **Price book on any redemption** | **Always booked at the STANDARD price book.** Chef's Table absorbs the delta — an internal transfer today, since every outlet is company-owned |

**Resolves L19.** Also gives the engine an unambiguous valuation rule: liability is always standard-book,
so reward cost never varies by where it lands.

- **Flags:** L32 — **Redemption Point coverage must be checked against delivery-only customers.** A
  customer who only ever orders from a cloud kitchen can earn points and never reach a counter. Either
  every delivery zone must be within reach of a Redemption Point, or that segment needs a stated route.
  Owner: ops lead. **This is the one gap the chosen option leaves open.**
- **Flags:** L21 remains open — **at franchising (~Aug 2027) the Chef's Table delta stops being an
  internal transfer and becomes a real settlement between entities.** Same applies to a franchisee
  fulfilling a reward against a card issued by a company outlet. Needs a settlement rule before the
  first franchise signs. Owner: Jawat + finance.

### Q10 — Trading, and Singapore (L13, L20)

- **Asked:** The Swap Wall conflicts with registration; and does Singapore run this?
- **Captured — Jawat:** *"Your recommendation is fine. but card swap is not our priority.."* ·
  Singapore: **Bangladesh first, Singapore once proven.**

**DECIDED — trading (resolves L13):**
- **The physical Swap Wall pegboard is dropped.** It is structurally incompatible with account-based
  registration — a registered card's code is spent, so handing over the physical card transfers nothing.
- **In-app account-to-account transfer** is the correct mechanism and is **designed now, built last.**
  Set credit moves to the new owner; points already awarded stay with the registrant; every transfer is
  logged, because an untracked transfer is indistinguishable from fraud.
- **Deprioritised at Jawat's direction.** Moves to the last phase. The `trades` table is still specced
  now so the schema does not have to be retrofitted later.
- Duplicates are **not** dead weight in the meantime — they still award points (Q3/Q6). That removes the
  urgency the Swap Wall was invented to solve.

**DECIDED — Singapore (resolves L20):**
- **Bangladesh only** for Phases 0–7. CQ @ Clarke Quay is one site and cannot produce meaningful data.
- Singapore follows **after Season 1 closes.** Required before SG launch, none of it decided:
  SGD earning threshold · SG price book for liability · SG print run and import/customs ·
  SG merch catalogue and MRP · **separate legal review under Singapore promotional law.**
- v1.0 §14.6 ("does SG run a fourth season?") is **retired** — it was a question about the old
  nine/ten roster split, which the Bible voided.
- **Bangladesh CTAs must never appear on Singapore content** (`CLAUDE.md` §5) — unchanged.

**Also resolved during this question — L7 is closed.**
All **ten** character cards exist at `assets/Surprise Cards/Character Cards/` (Air Maxi, Bhoppu, Icy,
Merlulu, Mr Waffle, Picchi, Spacy, Stovy, Swirly, Tvy). **`CLAUDE.md` §10's "card 6/9" note is stale
and should be corrected.** Caveat: the existing Merlulu card is the **pre-redesign art and says "she"** —
it is the First Edition (R2) and needs reissue before he can be the standing rare.

### Q11 — Season calendar, and the card redesign (L14, L15, C1)

- **Asked:** Season calendar, and the merch catalogue.
- **Captured — Jawat:** Calendar recommendation accepted. Then a **material correction:**

> *"no redesign at phase zero.. we already have unique numbers printed on the cards.. and we provide the
> cards in a pack (yellow color pack with waffleup logo.. card number is not visible until someone opens
> (tears) the pack.. so the number is safe.."*

> *"lets go with your recommendation.. but we should always have option to add new sku or remove from
> the available list, or show out of stock.."*

**DECIDED — calendar:**

| When | What |
|---|---|
| Sep–Dec 2026 | Build: account + merch site, registration flow. **No card redesign.** |
| **Jan 2027** | **S1 — The Big and the Small** (Bhoppu · Picchi · Swirly) |
| **May 2027** | **S2 — Go Further** (Air Maxi · Spacy · Icy) |
| **Sep 2027** | **S3 — Hold the Line** (Mr Waffle · Stovy · Tvy) — lands on the 16 Dec Banani anniversary |
| All year | **Merlulu**, standing rare |

⚠ Franchising (~Aug 2027) lands mid-S2 → the settlement rule (L21) is needed **before** S2 closes.

**DECIDED — the sealed yellow pack is the possession proof. This removes the redesign from the critical path.**

Cards already ship in a **sealed yellow WaffleUp-branded pack**; the unique number is **not visible until
the pack is torn open.** The pack is doing the job I proposed a latex panel for.

| Loophole | Status under the sealed pack |
|---|---|
| **L15 — photo attack** | **CLOSED.** The number cannot be read without opening the pack. Residual: a customer who opens, photographs and posts a card *before* registering it. Mitigate with copy, not engineering — *"register it the moment you open it."* |
| **C1 — hidden PIN / latex panel** | **WITHDRAWN. Not needed.** The pack already provides possession proof. No redesign, no added print cost, faster launch. |
| **L14 — staff farming an undistributed box** | **STILL OPEN.** Staff can tear packs. The pack stops outsiders, not insiders. **Batch-level activation (C2) + outlet serial-range binding + anomaly detection remain required.** Carried into the guideline. |

**Consequence — a much stronger Phase 0 than v1.0 had.**
v1.0's Phase 0 was a printed tick-box strip. With no redesign, Phase 0 becomes far better:

> ⭐ **Retro-activate the cards already in the market.** ~38,556 cards are already in customers' drawers
> with unique numbers on them. Launch the account and let every one of them be registered. This builds
> the customer database and the scoreboard **before** Season 1 prints, tests the whole flow on real
> volume, and gives a genuine launch story — *the cards you already have just started counting.*

⚠ **But it carries a liability nobody has costed. New finding:**

| | |
|---|---|
| Legacy cards in market | ~38,556 |
| Character cards among them (91%) | ~35,000 |
| If all registered at the standard 5–18 band (avg 11.5) | **~403,000 pts = BDT 403,000** |
| At a realistic 10% legacy registration | ~40,300 pts = **BDT 40,300** |

The realistic figure is about one month's programme budget — acceptable. The tail risk is not.
**[DECISION NEEDED] → L33: cap the legacy pool.** Recommended: a **global legacy point pool** (e.g.
50,000 pts, dashboard-set), first-come, and legacy cards register for **set credit and Full Gang
regardless** even after the pool empties. Preserves the launch story with a hard-bounded cost.

**Note:** seasons still require a **new print run** (three characters per batch instead of ten) —
that is a *print plan change, not a card redesign*. The tick-box strip and QR can ride on that run,
or wait. Not on the critical path either way.

**DECIDED — merch catalogue:**

| SKU | Points | ~Cards |
|---|---|---|
| Sticker sheet / enamel pin | **25** | ~2 |
| Notebook | **80** | ~7 |
| Water bottle | **150** | ~13 |
| Tote | **200** | ~17 |
| Tee | **350** | ~30 |
| Character plush | **600** | ~52 |

- The cheap bottom rung is load-bearing: an early **first redemption** converts a card-holder into a
  collector, and **redeemers spend 3.1× more than non-redeemers.**
- All sold at real MRP in the shop — the anchor must be honest (Q2).
- **Season badge and collector's folder are NOT purchasable.** Earned only. No point price, no MRP.
- **Jawat's requirement:** the catalogue needs full lifecycle control — **add SKU, remove from the
  available list, and an explicit out-of-stock state** (visible but unredeemable, not deleted — deleting
  a SKU someone is saving for breaks the "never devalue" rule, L30). → schema in §11.

### Q12 — Legacy card liability (L33)

- **Captured — Jawat:** Selected **global legacy pool, set credit always.**

**DECIDED:** legacy pool **50,000 pts** (dashboard-set), released first-come. While the pool holds
points, a legacy card awards set credit **and** points. Once empty, legacy cards still register for
**set credit and Full Gang progress** — nobody's collection is ever refused. **Max exposure BDT 50,000,
known in advance.** Creates honest launch urgency at zero communication cost. **L33 resolved.**

---

## Open flags (pending input)

| # | Item | Owner |
|---|---|---|
| — | **`waffle_up_surprise_card_engine_claude_brief.md` is not in this repo.** Everything about existing tables and fraud controls is second-hand. Get it committed. | Jawat |
| L5 | Merlulu — approve one of four head options; commission `.ai` master, T-pose. He is the standing rare and blocks Full Gang completion. | Jawat + Sadbin Ahmed |
| L8 | Colour-in line art on the card back is a derivative; `CLAUDE.md` §5 forbids redraws with no carve-out. Needs an explicit exception naming who may produce it. | Jawat |
| L14 | Staff farming an opened box. Needs batch-level activation + outlet serial-range binding + anomaly detection. | Engine build |
| L17 | Delivery: who inserts the card, and what stops skimming between kitchen and rider? | Ops lead |
| L21 | Franchising (~Aug 2027, lands mid-S2): settlement when a franchisee fulfils a reward against a company-issued card; and the Chef's Table price-book delta stops being internal. | Jawat + finance |
| L24 | Points are now a stored-value liability. Legal review scope widens beyond promotional compliance. | Jawat + legal |
| L26 | Merchandise becomes a real retail line — stock, SKUs, reorder. Unbudgeted. | Ops lead |
| L29 | Under-16 registration consent flow. | Legal + engine build |
| L32 | Redemption Point coverage vs delivery-only customers (cloud kitchen zones). | Ops lead |
| — | **Item-level COGS** — still the single cheapest saving available (reward-mix re-weighting). Open since v1.0. | Finance |
| — | **Card printing cost** — never entered any budget line. | Ops lead |
| — | Golden Waffle: confirm the prize bundle and publish the odds (R1). | Jawat |
| — | `CLAUDE.md` §10 says "card 6/9" — stale, all ten exist. Correct it. | Marketing |
| — | `brand/BRAND.md` "~27,000 + ~3,500 per batch" — describes a print run of ~100 batches, not a batch. Correct it. | Marketing |
| — | `brand/CHARACTER-BIBLE.md` is still DRAFT, "Approved by: ______". | Jawat |

## Recommendations carried forward
- **R1** — Publish the odds voluntarily (scratch 9.09%, Merlulu ~1 in 30, Golden Waffle ~1 in 5,000–10,000). Free trust, good content, future-proofs against every regulator's direction of travel.
- **R2** — Log a `card_variant` field. The Merlulu she→he change creates a genuine First Edition.

---

## Loophole status — final reconciliation

**Supersedes the "OPEN" statuses in the pre-grill table above.** 23 loopholes were logged before the
session; 9 more were found during it. Result: **24 closed, 8 carried as owned flags.**

| # | Loophole | Status | Where |
|---|---|---|---|
| L1 | Season expiry vs Full Gang — mutually exclusive | **CLOSED** | §3, only the badge is time-boxed |
| L2 | Seasons built for 9, roster is 10 | **CLOSED** | §3, Merlulu standing rare |
| L3 | Groupings derived from demoted card bios | **CLOSED** | §3, regrouped from the Bible's relationship web |
| L4 | Full Gang = 9 or 10? | **CLOSED** | §3, 9 + Merlulu = 10 |
| L5 | Merlulu unprintable | **CARRIED** | Doesn't block S1; gates Full Gang. Owner: Jawat + Sadbin |
| L6 | Next print run reprints wrong bios | **CLOSED — premise was wrong.** Bios are correct; the *voice files* were the misread. Only Merlulu she→he | §14.1 |
| L7 | Card art only 6/10 | **CLOSED — false.** All ten exist. `CLAUDE.md` §10 is stale | §18.15 |
| L8 | Colour-in line art is a forbidden derivative | **CARRIED** | Needs a `CLAUDE.md` carve-out. Owner: Jawat |
| L9 | Swirly must not speak on a card | **CLOSED** | §7.3 system voice + `speaks` flag in schema |
| L10 | Character-voice copy on registration surfaces | **CLOSED** | §7.3 |
| L11 | Pronoun drift | **CLOSED** | §14.1; and it yields a First Edition variant |
| L12 | "Registration grants nothing" is false once points ride on it | **CLOSED** | §7.1 states it plainly; §9 gives it a full fraud surface |
| L13 | Swap Wall vs registration conflict | **CLOSED** | §14.9 — pegboard dropped, transfer replaces it |
| L14 | Staff farm an undistributed box | **CARRIED** | Batch activation + serial ranges + anomaly rules specced in §9.2. Owner: engine build |
| L15 | QR registerable from a photo | **CLOSED** | The sealed yellow pack already hides the number (§7.2) |
| L16 | No cap per phone | **CLOSED** | §9.3, five caps, evidence-driven |
| L17 | Delivery card skimming | **CARRIED** | §9.2 #5. Owner: ops |
| L18 | No grace when a season closes mid-collection | **CLOSED** | §3 — nothing is ever taken away |
| L19 | Which price book governs a redemption | **CLOSED** | §8 — always standard book |
| L20 | Singapore undefined | **CLOSED** | §18 — BD first, SG prerequisites listed |
| L21 | Franchising liability transfer | **CARRIED** | §8, needed before S2 closes. Owner: Jawat + finance |
| L22 | `is_discount` is a dead field | **CLOSED** | §14.8 — dropped, replaced by a wording lint |
| L23 | No rarity tier exploited | **CLOSED** | §6.1 — four tiers |
| L24 | Points = stored-value liability | **CARRIED** | §18.8 widened legal scope. Owner: Jawat + legal |
| L25 | Merch MRP publishes the exchange rate | **CLOSED** | §10.1 anchor-price principle |
| L26 | Merch retail is unbudgeted ops scope | **CARRIED** | §18.12. Owner: ops |
| L27 | 2.5% ceiling didn't contemplate points | **CLOSED** | §5.4 — 3.0%, enforced at print time |
| L28 | The bright line needs to be immovable | **CLOSED** | §6.3, and §16.5 proves why it matters |
| L29 | Under-16 consent | **CARRIED** | §18.7. Owner: legal + engine |
| L30 | Never devalue issued points | **CLOSED** | §5.4 rule 3 + append-only ledger (§14.4) |
| L31 | Batch point cap must be a constraint, not a report | **CLOSED** | §4.3, §14.8 `batches` |
| L32 | Delivery-only customers may never reach a counter | **CARRIED** | §8. Owner: ops |
| L33 | Legacy retro-activation liability | **CLOSED** | §13.1 — 50,000 pt pool, exposure known in advance |

**Every carried flag has a named owner and appears in `programs/SURPRISE-CARD-GUIDELINE.md` §18.**

## Deliverable
`programs/SURPRISE-CARD-GUIDELINE.md` **v2.0**, 24 Aug 2026 — supersedes v1.0 in full.

---

## Q13 — Closing the 8 carried flags

- **Captured — Jawat:** *"you can go with your recommendation.. and here, one card is issued at each
  more than 500 tk purchase.. so we know how many 500* orders were made from POS.. from the total number
  of cards, we can track how many should there be and how many there actually is."*

**⭐ NEW CONTROL — POS reconciliation. Jawat's addition, and it is stronger than what I had specced.**

The POS already knows the count of qualifying transactions per outlet per period. That is how many cards
*should* exist. Three quantities, three invariants:

```
qualifying_txn_count   from POS      -> how many cards SHOULD have been issued
cards_issued_count     from engine   -> how many actually left the box
cards_registered_count from engine   -> how many were registered from that outlet's serial ranges
```

| Invariant | Meaning | A breach means |
|---|---|---|
| **I1** `cards_registered ≤ cards_issued` | Cannot register a card that was never handed out | Data or fraud |
| **I2** `cards_issued ≈ qualifying_txn_count` | **The card issue rate** | Staff are not handing cards out |
| **I3** ⭐ `cards_registered ≤ qualifying_txn_count` | Hard ceiling per outlet per period | **Arithmetic proof of farming** |

**Two things this buys beyond fraud detection:**
1. **No new step at the counter.** It uses data both systems already hold.
2. ⭐ **The card issue rate becomes a staff KPI** — which solves the separate problem that staff currently
   have no reason to promote the programme. A manager can own a number.

**Honest limit:** it is a *count* reconciliation, not a card-level one. If a staff member farms 20 cards
while the outlet also fails to hand 20 to real customers, the totals net to zero. **So POS reconciliation
is the primary detection and the anomaly rules remain** for what nets out.

**Decisions taken on Jawat's instruction ("go with your recommendation"):**

| # | Flag | Resolution |
|---|---|---|
| 1 | Insider farming | Batch activation + serial-range binding + anomaly rules **+ POS reconciliation as primary detection** |
| 2 | Delivery skimming | Card serial logged against `order_id` at packing; POS reconciliation run per channel |
| 3 | Under-16 | Year of birth at registration; under 16 requires guardian phone + SMS confirmation; minor accounts carry no marketing, in-person collection only, no public leaderboard without separate consent |
| 4 | Colour-in line art | Named carve-out in `CLAUDE.md` §5 — Surprise Card back only, original artist only, Jawat-approved, then stored in `assets/` as a supplied asset. AI generation remains banned absolutely |
| 5 | Merch ops scope | Launch 6 SKUs, single supplier, stock held centrally with per-outlet allocation, reorder at 30%. **Point-redeemed merch counts against the 3.0% ceiling at production cost; merch sold for cash is a separate P&L line.** Owner: ops lead |
| 6 | Franchising settlement | **Principle: the entity that issued the card funds the reward.** Cards carry their issuing outlet; the fulfilling entity is reimbursed at production cost; monthly netting between entities |
| 7 | Merlulu | **He enters circulation only when print-ready.** Until then the collection shows a **locked tenth slot** and the Full Gang bonus is unclaimable. A locked mystery slot is a better hook than an absent one |
| 8 | Legal | Cannot be closed by decision. Scoped as a written brief in the spec's Open Items so counsel is not thinking from scratch |

**Deliverable changed:** Jawat wants **a clean document with no version history and no v1/v2 comparison** —
readable by his office as the plan, and precise enough to feed to an AI building the engine in the
WaffleUp admin panel. Rewriting `programs/SURPRISE-CARD-GUIDELINE.md` on that basis.

### Q14 — Merlulu reveal, and the stored-value question

- **Captured — Jawat, 24 Aug 2026:**
  1. *"On merlulu, your recommendation seems fine.. I'd just open up merlulu in the website's available
     gang members once his card is rolled out."*
  2. *"does a points balance redeemable for merchandise constitute stored value under Bangladesh law..
     — does not constitute regulated stored value or e-money."*

**DECIDED — Merlulu is revealed, not placeheld.**
The locked-tenth-slot idea is dropped. The website shows **nine characters and nothing else** until
Merlulu's card actually rolls out — no locked slot, no placeholder, no "coming soon". His arrival is then
a genuine reveal: the Gang has always been nine, and one day there is a tenth. **A content beat rather
than a gap in a grid.**

Schema consequence — **two flags, not one:**

| Flag | Gates |
|---|---|
| `is_print_ready` | Inclusion in card generation |
| `is_live_on_site` | Visibility on the website roster — flipped manually when the first batch containing him is activated, so **we time the reveal, not the print schedule** |

Full Gang logic now reads **`all characters where is_live_on_site = true`**, not a hardcoded 10. A bonus
already awarded is never revoked (invariant 3).

⭐ **And the real deadline turns out to be much softer than assumed.** The Full Gang needs characters from
all three seasons, so **nobody can complete it before S3 opens in Sep 2027.** Merlulu therefore has to be
ready before **September 2027**, not before Season 1. **He was never actually blocking the launch** —
there is a full year of runway. Corrected in §3 and §18.7.

**RESOLVED — the sharpest legal question.**
Points redeemable for merchandise **do not constitute regulated stored value or e-money in Bangladesh.**
No registration, reporting or ring-fencing obligation. Two caveats recorded in §18.8:
- **Bangladesh only.** Singapore's Payment Services Act treats stored-value facilities separately and
  needs its own answer before any SG launch.
- **"Not regulated" ≠ "not a liability."** Unspent points remain an accounting provision on the balance
  sheet regardless of regulatory status — the outstanding-liability report in §16 stands.

The other five legal questions in §18.8 remain open.

### Q15 — Locked slot restored, and card variants

- **Captured — Jawat:** *"your suggestion on locked slot of merlulu is better.. In future we might as
  well introduce different poses or versions of each character card, so keep the plan of adding cards
  option in the admin."*

**DECIDED — roster state is a three-way enum, not a boolean.**
`hidden` (absent from the site) · `locked` (silhouetted, uncollectable, visible) · `live`.
Merlulu is `locked` until his card rolls out. Nine characters alone reads as a complete set; nine plus a
locked tenth reads as an unanswered question. Set independently of `is_print_ready` so **we time the
reveal, not the print schedule.** A `locked` character does not count toward the Full Gang target.

**DECIDED — `card_designs` table, built now, used later.**
A character will eventually have several cards: poses, seasonal editions, foils, and the pre/post-redesign
Merlulu that already exists. **Retrofitting this into a live `cards` table means re-keying every card ever
issued** — the most expensive late addition on the whole spec. At launch each character has exactly one
design and nothing behaves differently.

- Two-stage draw: **character first, then design within that character.** Stage two is a no-op at launch.
- `cards.design_id` FK; `design.point_band_override` lets a rare foil carry a higher band without
  touching the character's own band.
- `is_retired` on a design is what makes a card genuinely scarce — never reprinted.
- Admin gets a **Card designs** screen: add a pose, set its rarity within that character, upload art,
  mark print-ready, retire an old design. **New cards become a data change, not a code change.**

> ⭐ **The rule that stops variants breaking the game: set completion counts at CHARACTER level, never at
> design level.** Any Bhoppu completes Bhoppu. Variants are a second, optional completionist layer
> (`customers.design_state`) with no bearing on the season badge or the Full Gang. If designs counted
> toward completion, six cards a season silently becomes eighteen and the winnability argument in §3
> collapses.

- **Merlulu's "she" card** is logged as `merlulu_first_ed`, `is_retired = true` — a genuine First Edition
  acquired for free.

### Q16 — Seasons rejected. The restructure.

- **Captured — Jawat:** *"I did not like this three character season thing from the beginning. I dont
  want to create a new rank thing.. any alternative? we can roll out all characters always.. collection
  wins, simple math.. new announcement every three month that new season is beginning, where each season
  is basically same thing, just different characters - feels off to me.. We might introduce season, but
  in different way.. occasion or sth else.."* · Golden Waffle: **100 points**.

**He is right.** "New season, same game, different faces" is a content calendar pretending to be a
mechanic. The seasons only ever existed to solve one arithmetic problem — all ten at random takes ~40
cards — and there is a better solution to that problem.

**DECIDED — seasons abolished. All ten characters in circulation permanently.**

**The fix is duplicate conversion.** Modelled over 40,000 trials, Merlulu at 1 in 30:

| Rule | Mean cards to all 10 | ~Spend | ~Time weekly |
|---|---|---|---|
| No conversion | 39.7 | BDT 19,900 | 10 months |
| 8 duplicates → pick any | 21.6 | BDT 10,800 | 5 months |
| **3 duplicates → pick any** ✅ | **15.7** | **BDT 7,900** | **~4 months** |
| 2 duplicates → pick any | 13.5 | BDT 6,700 | 3 months |

**Three loops replace the season calendar:**
1. **The reveal** — every card, 5–18 points
2. **Points → merch** — first item at ~2 cards. *This is the fast loop seasons were faking*
3. **The Full Gang** — ~16 cards, ~4 months

Milestones instead of season badges: **5/10 = +50 · 10/10 = +200 + folder · all four occasion editions
in a year = +200, repeatable.**

**DECIDED — occasions replace seasons, using the `card_designs` table built in Q15.**
Four a year — **Pohela Boishakh (14 Apr) · Eid ul-Fitr · Eid ul-Adha · Victory Day (16 Dec, also the
Banani anniversary).** An occasion brings a **limited-edition design of an existing character**, not a
new character. In-window only, then `is_retired` forever.

Why it beats seasons: the occasion is real so urgency isn't manufactured · it doesn't touch the base
collection (completion is character-level) · it gives collectors a permanent chase after the base ten ·
marketing gets a calendar that already exists.

**Also decided:**
- **Merlulu: point rank 2 (Air Maxi's value), priority rank 6.** *"not precious, it is unique, and
  completes the gang."* Requires `point_rank` decoupled from `priority_rank`.
- **Golden Waffle: 1 in 1,000, +100 points.** ~10 found/month, ~BDT 960/month, 0.02% of qualifying revenue.
- **Nothing a customer holds ever expires.** Urgency comes from **supply** (an edition stops printing),
  never from a deadline on the person.

**Two errors corrected during this pass:**
1. **`merlulu_rarity_weight` was wrong.** 0.033 yields **1 in 92**, not 1 in 30. Correct value with nine
   ordinary characters is **9/29 = 0.3103**. General formula now written into §11.3: `w = n·r/(1−r)`.
2. **The seasons were not cost-neutral** — S1 (ranks 1/4/5) minted 3,420 pts/batch vs S3 (3/8/9) at
   2,960, a 15% gap, and S1 breached the cap. Moot now that seasons are gone: with all ten always
   circulating every batch mints **3,156**, uniformly. Cap set at **3,160**.

**Deliverable rewritten in full** — patching would have left inconsistencies across §§1–4, 11–17 and the
appendix.

### Q17 — Real costs from the vendor list

**Source:** `D:\Waffleup Download\Merchandise and Vendor List (with price).xlsx` (Item Info + Vendor Info),
supplied by Jawat 24 Aug 2026. Merchandise proper = rows 2–27 (items 1–26, ending at Pen & Box);
rows 28+ are packaging, employee and event items.

**[CONFIRMED] Card printing** — Bijoy / Asha Printers:
- Character card **BDT 3.00** · Scratch card **BDT 3.40**
- Per 297-batch: 270×3.00 + 27×3.40 = **BDT 901.80 = 0.61%** of qualifying spend
- ~**BDT 29,300/month** at current volume
- ⚠ **Surprise Card Cover and Surprise Card Box are unpriced on the sheet** — printing figure is a floor.

**[CONFIRMED] Jawat's instructions on the catalogue:**
- Water bottle + its box priced as one (190 + 5 = 195), not separated
- Pop socket wrapping skipped
- **Every item ships in its box** — box costs folded into point prices
- **Paper gift bag (35) excluded from the catalogue entirely** — *"We provide the bag only when we offer
  goodies to new employees or any important guest"*
- More products coming

⭐ **THE PRICING RULE THAT FELL OUT OF THE REAL DATA:**
> **A point costs BDT 1.00 to produce, so an item's point price *is* its production cost in taka.**

No conversion table, no per-item judgement, and a new product prices itself the moment a vendor quotes
it. `merch_catalogue.point_price` pre-fills from `production_cost` rounded to the nearest 5, overridable.

| Item | Points | ~Cards | Cost (boxed) | MRP @2.6× |
|---|---|---|---|---|
| **Sticker** | **10** | **~1** | 5.50 | 30 |
| Pen & box | 35 | ~3 | 35 | 100 |
| Pop socket (10 designs) | 40 | ~3 | 37 | 100 |
| Calendar | 65 | ~6 | 50+15 | 170 |
| **Notebook** (3 designs) | **95** | **~8** | 95 | 250 |
| Socks — kids | 140 | ~12 | 90–100+40 | 350 |
| Socks — adult | 175 | ~15 | 135+40 | 450 |
| Water bottle | 195 | ~17 | 190+5 | 500 |
| Cap — mesh | 300 | ~26 | 235+62 | 750 |
| Cap — AOP | 310 | ~27 | 250+62 | 800 |
| T-shirt | 350 | ~30 | 350 | 900 |
| Hoodie | 580 | ~50 | 581 | 1,500 |

- **Notebook lands at ~8 cards** — inside Jawat's originally stated 6–8. The model holds against his own intuition.
- **MRP multiple is a consistent ~2.6×**, validated by his notebook figure (95 cost → 200–300 MRP).
- **The sticker at ~1 card is the most valuable line in the table** — first redemption is what converts a
  cardholder into a collector, and redeemers spend 3.1×.

⭐ **Adding the boxes does not change programme cost.** Points are minted at a fixed rate per batch, and
because point price = production cost, every point redeemed costs BDT 1.00 whatever it buys. The box
raises the SKU's point price so cost-per-point holds. **The giveaway ceiling is set by points minted, not
by what they are spent on.** Only reach changes — the cap moved from ~20 cards to ~26.

**Budget restructured into two ceilings** (they behave differently — printing costs money whether or not
anyone plays):

| | Ceiling |
|---|---|
| Giveaway (points + scratch) | **3.0%** |
| Card printing | **0.65%** |
| **All-in programme** | **3.75%** |

Realistic all-in run-rate: **1.75–2.11%** (~BDT 84,000–102,000/month).

**Schema addition — `merch_variants`, mandatory.** Pop sockets have 10 designs, notebooks 3, socks differ
in cost by colour (90 vs 100), and apparel is colour **× size**. **`merch_stock` is keyed on `variant_id`,
never `sku_id`** — reserving "T-shirt" and finding only XXL at the counter is exactly the failure §6.1
exists to prevent.

**[CONFIRMED] Occasions:** character is **not fixed** — chosen fresh per occasion, may be more than one.
**Artwork owner: Junaid.**

**Vendors on record:** Bijoy/Asha Printers (cards, notebooks, stickers, pen) · Monir/F. Rahman (bags,
calendar) · Toco (caps, socks) · Gorur Ghash (apparel) · Customized & Crafts (bottles) · Case Corner
(pop sockets).

---

## Session 3 — 26 Aug 2026 · six decisions from Jawat

### Q18 — Card printing: the cover is already in the price

**[CONFIRMED]** BDT 3.00 / 3.40 **include the sealed cover.** Verified against the vendor sheet: rows 57–58
(`Surprise Card (Scratch)` / `(Character)`) both specify *Card Size 2″×3.5″, 600gsm swedish board, matte spot
lamination* **and** *Cover Size 2.5″×4″* in the same spec. Row 59 `Surprise Card Cover` (150gsm art paper) is
the cover's **material spec, not a second charge**.

→ **BDT 901.80/batch = 0.61% is a total, not a floor.** Flag closed.

**"Box of what?"** — row 60, `Surprise Card Box`, typed **Others** (not Branding), Bijoy, no dimensions, no
price. Only sensible reading: **the outer carton a print run ships to an outlet in** — the box staff open and
mark activated (§13.7). Ops consumable, one per few hundred cards, fractions of a taka each, never touches a
customer. Left open for completeness; not a budget line.

### Q19 — Scratch COGS: 38% of selling price, flat

**[CONFIRMED]** No item-level COGS available. Budget the whole reward mix at **38% of the standard-price-book
menu price.**

| | Per batch |
|---|---|
| Menu value, 27 scratch rewards | 5,935 |
| At 38% | **2,255** |
| At 38%, 60% redemption (planning) | **1,353** |

⚠ **This broke the 3.0% giveaway ceiling on paper.** 38% flat is dearer than the 30% bottom of the old
modelled range, so:

| Scenario | Giveaway | All-in |
|---|---|---|
| Realistic — 40% reg × 50% burn, 60% scratch | 1,984 · 1.34% | 2,886 · **1.94%** |
| Every point spent, 60% scratch | 4,509 · 3.04% | 5,411 · 3.64% |
| Every point spent, 81% scratch *(top observed)* | 4,983 · 3.36% | 5,885 · **3.96%** |
| Theoretical max | 5,411 · 3.64% | 6,313 · 4.25% |

⭐ **Ceiling reset: giveaway 3.0% → 3.5%, all-in 3.75% → 4.15%.** Justified by the programme's own rule 2 —
*a breached ceiling means you reset the ceiling, not the reward.* The breach was arithmetic, not behaviour.
**At 3.5% the ceiling cannot be breached unless scratch redemption passes ~90% while every point is also
spent.** Observed max is 81%; burn runs ~50%. Realistic run-rate 1.94% ≈ **BDT 94,000/month**.

Lever if it ever happens: `batch_point_cap` 3,160 → **2,940** (≈0.8 points/card). Better first lever is still
item-level COGS.

⚠ **Consequence to hold onto:** a flat 38% makes every reward mix look equally efficient by construction, so
**it cannot see the §7.2 optimisation at all.** The 15–25% saving is real in the kitchen; the assumption is
blind to it. Open item 1 stays open, re-scoped: *38% is a number to budget with, not to design the mix with.*

### Q20 — Delivery-only customers

Jawat floated: deliver merch via the platform, customer covers the extra with **points** or **cash on
delivery** — explicitly "if not the right way, scrap it, use best practices."

**Both rejected.**
- **COD on a reward** → the customer pays BDT 70 and has just been *told what the reward is worth.* Exactly
  what §8 exists to prevent, and a reward you pay for stops being a reward. Plus COD reconciliation,
  refusals and returns on an order with no sale value.
- **Points for delivery** → "delivery: 70 points" states a taka value the moment they know what delivery
  costs; spends reward budget on logistics rather than product; deletes the redemption halo, which is the
  entire commercial reason in-person collection is worth its friction.

⭐ **Instead — the reward rides along with a paid order.** Customer picks *"send it with my next order"*;
item reserved immediately; goes in the bag next time they order.

Costs nothing (the van was going anyway) · names no value · **still requires a purchase** · reuses the
§13.6 bag-seal step exactly · **small items only** (sticker, pen, pop socket, calendar, notebook — apparel
and bottles need size/colour handover and don't fit the bag).

Schema deltas: `merch_stock.location_id` replaces `redemption_point_id` (a cloud kitchen holds attach stock
without being a counter; `is_redemption_point` / `is_attach_point` independent) · `merch_redemptions` gains
`fulfilment_method`, `attached_order_id`, status `awaiting_attach` · `merch_catalogue.is_order_attachable` ·
`pin_expiry_days_order_attach` = **60** (can't require an order inside a fortnight) · **on lapse, points
return to the ledger** (`reservation_lapsed`) — nothing a customer holds is taken away. Rollout **Phase 2b**.

Jawat reaffirmed the original position: outlet-only redemption *"would also increase our customer to some
extent"* — correct, and it's why ride-along is the backstop, not the default.

### Q21 — Merlulu ships on the base design

**[CONFIRMED]** *"no need to worry, we would proceed with base.. We have the design."*

`is_print_ready = true`, `roster_state = 'live'`, in generation from launch. **The Full Gang is ten from day
one.** Locked-slot mechanic stays in the engine for future characters but is no longer used. **Merlulu comes
off the critical path entirely** — was the only item blocking first completions ~4 months post-Phase 1.

Circulating cards still read "she" → `merlulu_first_ed`, `is_retired = true`. Genuine First Edition acquired
for nothing. Content beat, not a problem.

### Q22 — Shop prices: launch at the recommendation, editable thereafter

**[CONFIRMED]** Not fixed. List at the ~2.6× column and adjust once the Dhaka market answers. Status changed
from [DECISION NEEDED] to a launch position.

### Q23 — ⭐ The no-deploy rule (new §15.1)

**[CONFIRMED]** *"everything should be front end change friendly."* Everything a customer sees is **data, not
code**: add/edit/retire products · point price, production cost, MRP independently · name, description, sort
order, visibility · **product images — upload, replace, reorder, set primary** · variants and per-location
stock · characters, designs, occasions, milestones · every §14 parameter.

Three build consequences: **images are uploads to object storage, not repo files** (if a new product needs a
code change to show its picture, the panel isn't finished) · prices must be first-class and versioned, safe
to change while customers are mid-save (invariant 8) · **editable ≠ untraceable** — every change logged with
who and when.

### Housekeeping done this session

Stale references corrected after the sticker replaced the 25-point entry item: §2 "first reward in ~2 cards"
→ first card · §10 "reaches 25 points in two visits" → sticker on card one · §19 "ladder starts at 25 points"
→ 10 points · §3.1 "enough for a tee, most of the way to a plush" → T-shirt/hoodie (no plush in the
catalogue) · §15 dashboard ceiling 3.0% → 3.5%/4.15% · §13.2 Merlulu-locked note.
