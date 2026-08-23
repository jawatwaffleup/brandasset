# Surprise Card — Utilisation Guideline

**Version 1.0 · 23 August 2026 · Owner: Marketing**
**Companion to:** `waffle_up_surprise_card_engine_claude_brief.md` v1.0 (24 Jun 2026)

---

## 0. What this document is

The engine brief is a **fulfilment and control system**: it generates codes, tracks cards, validates redemptions, prevents fraud and reports liability. It is well designed and this document does not repeat it.

This document covers the half the brief does not: **the demand side.** What makes a customer want the next card. Right now the programme has an excellent gearbox and no engine.

Read the two together:

| Question | Document |
|---|---|
| How does a card get made, tracked, validated, audited? | Engine brief |
| Why does a customer come back to get another one? | **This document** |

Everything here is written to be buildable. Section 11 gives the schema deltas the admin panel needs on top of the brief's existing tables.

Following the engine brief's own convention, content is tagged **[CONFIRMED]**, **[RECOMMENDED]**, **[ASSUMPTION]** or **[DECISION NEEDED]**.

---

## 1. Diagnosis — the number everyone is reading wrong

**[CONFIRMED]** `brand/BRAND.md` reports a **3–4% redemption rate** (2,839 redemptions against 38,556 cards distributed) and treats it as a problem.

It isn't. That metric divides redemptions by *every card printed* — but **character cards are not redeemable by design.** The engine brief states they *"usually do not provide direct redeemable food rewards."*

Run the arithmetic against only the cards that *can* be redeemed:

**[CONFIRMED]** A batch is **297 cards — 270 character + 27 scratch, 9.09% scratch.**

The available data supports two readings, and it cannot currently distinguish between them:

| Reading | Assumption | Scratch distributed | Redemptions | Rate |
|---|---|---|---|---|
| **A** | 38,556 is the complete distribution; redemptions ran against it | ~3,505 | 2,839 | **~81%** |
| **B** | Distribution continued at the Feb–May rate (9,639/mo) across Jan–Aug | ~7,006 | 2,839 | **~40%** |

**[ASSUMPTION]** The truth is somewhere between. The recorded periods don't align — distribution is logged Feb–May, redemption Jan–Aug — so the honest answer is **scratch redemption sits somewhere between 40% and 81%**, and the current record-keeping cannot narrow it further. Use **60%** as the central planning figure until the engine measures it properly.

*(Correction to v1.0 of this document, which quoted 65–81%. That range compared a four-month distribution total against an eight-month redemption total. Fixing the mismatch widens the range downward.)*

### The actual finding

Even at the pessimistic end, this holds:

> **Scratch cards work.** 40–81% redemption on a physical, manually validated paper coupon requiring a store visit is a good-to-excellent result. Whatever is wrong with this programme, it is not the scratch card.
>
> **The problem is that 91% of everything you print does nothing.** 270 of every 297 cards are character cards with no reward, no completion payoff, no trade route and no way for the customer to track progress.

You are not running an underperforming loyalty programme. You are running a working one at **9% of its printed volume**, and giving away the other 91% as a nice piece of paper.

**Note for `brand/BRAND.md`:** that file records "~27,000 character + ~3,500 scratch per batch." Now confirmed incorrect — those figures describe a **print run** of roughly 100 batches, not a batch. The file should be corrected so `batch_id` means one thing across the business.

### Why the character card currently cannot drive repeat custom

**[CONFIRMED]** Nine characters. **[CONFIRMED]** 270 character cards per 297-card batch, drawn randomly.

That makes set completion a coupon-collector problem. Expected cards needed to collect all nine:

```
E = (9 × H₉) / P(character card)
  = (9 × 2.829) / 0.909
  = 28.0 cards
```

| At current design | |
|---|---|
| Cards needed to complete the set | **~28** |
| Qualifying spend at BDT 500/card | **~BDT 14,000** |
| Elapsed time at weekly repeat | **~6.5 months** |
| Reward on completion | **None** |
| Customer's ability to see progress | **None** |

A 28-visit, BDT 14,000, six-month game with no prize and no scoreboard. Nobody is playing it, because nobody has been told it exists or given a reason to finish.

**Everything below fixes that without a single taka of discount.**

---

## 2. Design principles

These constrain every recommendation that follows.

1. **Never discount.** [CONFIRMED constraint from Jawat: *"we dont give discounts — that would be against our brand image."*] Give things; never cut price. A free add-on is a gift. A percentage off is a different brand.
2. **Preserve controlled randomness.** The engine brief is right to protect this. The customer must always feel lucky. Internally the ratios are fixed and costed.
3. **Give the game an ending the customer can reach.** A goal that takes 28 visits is not a goal.
4. **Make progress visible.** An invisible collection is not a collection.
5. **Prefer prizes that cannot be bought.** Unbuyable beats free-food, because it creates status, and status is what gets posted.

---

## 3. The core change — Seasons

**[RECOMMENDED]** Stop printing all nine characters into every batch. Print **three characters per season, three seasons a year.**

This is a printing decision. It changes no schema, costs nothing extra, and it converts an unwinnable lottery into a winnable six-visit game that resets three times a year.

### The seasons

The nine characters group cleanly on their own source material — these aren't arbitrary splits, they're the groupings already implicit in the approved bios:

| Season | Name | Characters | The thread |
|---|---|---|---|
| 1 | **The Street** | Air Maxi · Bhoppu · Picchi | The three human characters. Trends, energy, movement. |
| 2 | **The Originals** | Mr Waffle · Stovy · Icy | The three *object* characters — the waffle, the oven, the popsicle. The product itself. |
| 3 | **The Late Shift** | Swirly · Tvy · Spacy | All three bios explicitly reference late night. This is the brand's core occasion, cast as characters. |

**[DECISION NEEDED]** Season order and calendar placement. The Late Shift is the strongest and I'd hold it for the year-end slot rather than open with it.

### What this does to the math

| | Current (all 9) | Seasons (3 at a time) |
|---|---|---|
| Cards to complete | ~28 | **~6** |
| Qualifying spend | ~BDT 14,000 | **~BDT 3,025** |
| Time at weekly repeat | ~6.5 months | **~6 weeks** |
| Completions per year (max) | 0–1 | **3, plus an annual meta-set** |
| Feels | Impossible | Nearly done |

```
E = (3 × H₃) / 0.909 = (3 × 1.833) / 0.909 = 6.05 cards
```

Six visits is inside a weekly buyer's natural rhythm and — critically — is a **reachable stretch for the monthly "treat buyer"**, which is the segment where frequency growth actually lives.

### The annual meta-set

Collect all three season trios across the year → **the Full Gang**, all nine. This gives the habit buyer a twelve-month arc sitting above the six-week arc, without making the six-week arc any harder.

---

## 4. The reward ladder, and what it costs

All non-discount. All gifts, not price cuts. **All deliberately low-value** — see §4.4.

| Tier | Trigger | Reward | Est. true cost |
|---|---|---|---|
| **Instant** | Scratch card | Existing scratch rewards — keep exactly as they are, they work | ~BDT 66 avg |
| **Season trio** | 3/3 of a season | **Foil season badge card** (unbuyable, never in a batch) **+** an add-on that comes with it — ice cream or whipped cream | ~BDT 60 |
| **Full Gang** | 9/9 across the year | **Collector's folder** — a printed wallet that holds all nine, with the season badges | ~BDT 40 |
| **Status** | Full Gang holders | Early access to the next Kunaffle™ / limited-edition drop, before public release | ~0 |
| **Recognition** | Full Gang holders | Named on a Wall of Fame at their home outlet, and on social | ~0 |

### 4.1 The badge card and the folder

The **foil badge** is a card that is never in a batch and cannot be won randomly. It is the only object that proves you finished a season. It's the cheapest status object available to you, and it makes a trio worth completing before the free add-on is even considered.

The **collector's folder** does the same job at the top of the ladder, and it does something extra: it makes the collection *displayable*. A folder that shows nine slots with three filled is a permanent, physical progress bar sitting in the customer's bag. That is the single cheapest way to keep the game visible between visits.

**[DECISION NEEDED]** Print cost and minimum order for the foil badge and the folder. Both are standard print jobs — expect low unit cost at volume, but confirm before committing.

### 4.2 The figurine is dropped

**[DECISION MADE — 23 Aug 2026]** The 3D-printed character figurine proposed in v1.0 is **withdrawn.** Two reasons, both good:

1. **Cost and operational risk.** Per-unit print cost, lead time, fulfilment and the fact that only four of nine models exist made it the one item on the ladder with an unbounded cost tail.
2. **It was the item that created the compliance profile.** A high-value prize behind a randomised, spend-gated mechanic aimed at an audience starting at age 10 is the exact shape regulators look at. Removing it materially improves the position — see §15.

The `.stl` models remain a genuine unused asset and are worth revisiting later as **merchandise sold at retail** or as event/PR objects — just not as the prize inside a randomised collection game.

### 4.3 Reward economics — the batch

**[CONFIRMED]** Batch = 297 cards, 27 of them scratch. The scratch reward mix in the engine brief §3.14 maps to quantities summing to exactly 27, which validates the reading:

| Reward | Qty | Menu price (std) | Menu value |
|---|---|---|---|
| Tri-Chocolate WOAS | 3 | 200 | 600 |
| Nutella WOAS | 2 | 185 | 370 |
| Whipped cream | 5 | 120 | 600 |
| Ice cream | 5 | 135 | 675 |
| Kunaffle™ | 2 | 280 | 560 |
| Oreo Cream Shake | 2 | 285 | 570 |
| Hot Chocolate | 3 | 320 | 960 |
| Choco Choco Cheese | 5 | 320 | 1,600 |
| **Total** | **27** | | **BDT 5,935** |

Average scratch reward: **BDT 220 at menu price.**

**The critical distinction:** menu price is revenue foregone, not cost incurred. A free ice cream costs you the ice cream, not BDT 135.

**[CONFIRMED 23 Aug 2026]** Food COGS runs **30–45%, varying by product.** A single blended figure is still pending. Everything below is therefore modelled as a **range**, and the range is wide enough to change decisions — so treat the low end as optimistic.

| Per batch of 297 | |
|---|---|
| Qualifying spend the batch represents (297 × 500) | BDT 148,500 |
| Scratch reward menu value | BDT 5,935 — **4.0%** of qualifying spend |
| True cost @ 30% COGS, 60% redemption | BDT 1,068 — **0.72%** |
| True cost @ 45% COGS, 60% redemption | BDT 1,602 — **1.08%** |

### 4.4 Reward economics — the month

**[ASSUMPTION]** Current volume from `brand/BRAND.md`: 38,556 cards over Feb–May = **9,639 cards/month ≈ 32.5 batches/month.**

| Monthly, at current volume | |
|---|---|
| Qualifying revenue generating cards | ~BDT 4,819,500 |
| Scratch reward menu value issued | ~BDT 192,900 |

True cost at 60% redemption, across the confirmed COGS range:

| COGS | Monthly true cost | vs BDT 35,000 budget |
|---|---|---|
| 30% | ~BDT 34,700 | **on budget** |
| 35% | ~BDT 40,500 | 16% over |
| 40% | ~BDT 46,300 | 32% over |
| 45% | ~BDT 52,100 | **49% over** |

> **The BDT 35,000 budget is coherent — but only at the very bottom of the COGS range.**
>
> It was almost certainly built assuming ~30% COGS and ~60% redemption, and at those inputs it is accurate to within 1%. At a blended 37.5% it is running roughly **24% over**. The budget isn't wrong so much as **fragile**: it has no tolerance for the product mix drifting toward higher-COGS items.
>
> *(This supersedes the flag in v1.0 of this document, which claimed a ~BDT 64,000 run-rate. That calculation priced rewards at menu value rather than COGS and overstated cost by roughly 3×. The corrected answer is that the budget is broadly sound at low COGS and tight at high COGS.)*

### 4.4a Re-weight the reward mix — the cheapest saving available

**[RECOMMENDED]** Because COGS varies by product but the *customer* judges the gift by its **menu price**, the reward mix has a free optimisation in it:

> Choose scratch rewards where **menu price is high relative to COGS**. Maximum perceived generosity per taka of real cost.

The current mix is not obviously optimised for this. Beverages typically carry lower COGS than food, while Nutella-heavy items carry high COGS because the ingredient is imported. On that logic:

| Likely efficient (high menu, lower COGS) | Likely expensive (high COGS) |
|---|---|
| Hot Chocolate (320), Choco Choco Cheese (320), Oreo Shake (285) | Kunaffle™ (280), Nutella WOAS (185) |

A Hot Chocolate "feels like" a BDT 320 gift. If its COGS is 25%, it costs you BDT 80. A Kunaffle feels like BDT 280 and at 45% COGS costs BDT 126 — **less perceived value for more real cost.**

**[DECISION NEEDED]** Item-level COGS. With it, the mix can be re-weighted to hold the headline menu value at ~BDT 5,935 per batch — so the programme feels exactly as generous — while cutting true cost. Early estimate suggests **15–25% off reward cost with no change to customer experience.** This is the single cheapest saving in the programme and needs no customer-facing change at all.

### 4.5 The recommended budget

**[RECOMMENDED]** Stop budgeting a flat BDT figure. Card volume scales with sales, so a fixed number goes stale every time the business grows. **Budget as a percentage of qualifying revenue** — the spend that actually generates cards.

Adding the new completion rewards at ~BDT 60 per season completion (badge ~20 + add-on at COGS ~40):

Theoretical maximum completions = cards ÷ 6 = **~1,606/month**. Realistically only a fraction of holders will register and finish:

| Uptake (of theoretical max) | Completions/mo | Cost/mo | % of qualifying rev |
|---|---|---|---|
| 10% | 161 | ~BDT 9,700 | 0.20% |
| 25% | 402 | ~BDT 24,100 | 0.50% |
| 50% | 803 | ~BDT 48,200 | 1.00% |

**The recommended structure:**

| Line | Monthly (current volume) | % of qualifying revenue |
|---|---|---|
| Scratch rewards (existing, unchanged) | BDT 34,700–52,100 | 0.72–1.08% |
| Season completion rewards (new) | BDT 10,000–48,000 | 0.20–1.00% |
| Card printing | **[DECISION NEEDED — with ops lead]** | — |
| **Recommended operating ceiling** | **~BDT 120,000** | **2.5%** |

**Why 2.5% and not 2.0%:** at the top of the confirmed COGS range (45%) combined with strong completion uptake, rewards alone reach ~2.08%. A 2.0% ceiling would bind in exactly the scenario where the mechanic is working best. Set it at 2.5%, then tighten once actual COGS is confirmed — a ceiling you have to breach in year one teaches the organisation to ignore ceilings.

**Two rules that make this budget behave:**

1. **Express and review it as a rate.** At 2.0% of qualifying revenue it self-scales with the business and never needs a manual reset.
2. **If you breach the ceiling, raise it — don't cut the reward.** A breach means completions are running hot, which means the frequency mechanic is working. Cutting rewards at that exact moment would kill the thing you just proved. Check the starred metric in §12 first: if registered collectors are visiting more often than everyone else, the spend is buying what it was meant to buy.

---

### 4.6 How the rewards must be worded

**[CONFIRMED 23 Aug 2026 — binding, all customer-facing surfaces]** Jawat: *"we never use terms like free or discount."*

WaffleUp may give value away. It must **never name it, quantify it, or label it.** The words "free" and "discount" are banned outright — in cards, POS screens, social, staff scripts, Bangla and English alike.

| ✗ Never | ✓ Instead |
|---|---|
| "Get a FREE ice cream!" | "Ice cream comes with it." |
| "Worth BDT 135!" | *(say nothing — never quantify)* |
| "Collect 3 and save!" | "Collect 3. See what happens." |
| "Special discount for collectors" | "Collectors get first look." |

This applies to internal staff scripts too — if a staff member says "you get a free ice cream", the customer hears a giveaway, and the brand becomes cheap. Train the phrasing, not just the process.

**Test:** if the customer could work out the taka value from the words on screen, rewrite it. Full rule in `CLAUDE.md` §3.

---

## 5. Registration — the single highest-leverage addition

**[RECOMMENDED]** Let a customer **register** a character card without redeeming anything, without staff involvement, and without a POS transaction.

Print a **QR code** on every card. Scanning it opens WhatsApp (or a lightweight web page) and registers that serial to the customer's phone number.

This is the most important recommendation in this document, for four reasons:

1. **It creates the scoreboard.** The customer instantly sees *"Air Maxi ✓ · Bhoppu ✓ · Picchi ✗ — one more to finish The Street."* Principle 4, solved.
2. **It costs the outlet nothing.** Zero POS steps, zero staff time, zero queue impact. It works during the Thursday rush.
3. **It gives you the customer.** Phone number, collection state, visit cadence — the `customers` table in the engine brief finally has a way to populate itself. Today you have no idea who your repeat customers are.
4. **It turns 91% of your print run from inert paper into a tracked engagement event.**

**Critically: registration is not redemption.** Keep them as separate events with separate tables, separate metrics and separate fraud rules. Registration is low-risk (it grants nothing), so it needs almost no validation. Redemption stays exactly as controlled as the engine brief specifies.

### Customer-facing copy [RECOMMENDED]

Brand voice, Jester register, per `brand/VOICE.md`:

- On-card: **"Scan me. I'm keeping score."**
- Registration confirmation: **"Bhoppu's in. Two down, one to go."**
- Set complete: **"The Street is yours. Come collect what's coming to you."**
- Near-miss nudge: **"You're one Picchi away. Just saying."**
- Duplicate registered: **"Another Bhoppu. He does that. Trade him."**

---

## 6. Trading

**[RECOMMENDED]** Duplicates are currently dead weight. In every collectible programme that works, duplicates are the *engine* — they force collectors to find each other.

Trading serves three of your goals at once: it accelerates set completion (raising redemption), it creates social behaviour you don't have to pay for, and it costs nothing.

**Phase 1 — physical, launch with the season.** A **Swap Wall** at each outlet: a pegboard where a customer pins a duplicate and takes one. Unmanaged, unpoliced, zero staff cost. Low-value items, so shrink doesn't matter.

**Phase 2 — digital, once registration has volume.** Registered collectors can flag duplicates and see who nearby has what they need. Transfer of a serial from one `customer_id` to another, logged.

**[ASSUMPTION]** Phase 1 needs an outlet-level test before rollout — the window-format outlets (180–250 sq ft) may not have wall space. Test at a Chef's Table or a larger standard outlet first.

---

## 7. Fix the redemption friction

**[CONFIRMED]** Current redemption is 10 POS steps, then hole-punch, photograph, send to a WhatsApp group, staple to bill and KOT, ship to HQ, and a CCTV spot-check.

That is a serious, well-designed fraud control. It is also a **structural disincentive for staff to encourage redemption during the exact hours you're busiest.** A 65–81% redemption rate is being achieved *despite* it, which suggests customer demand is strong enough to survive the friction — but staff will never proactively promote it.

**[RECOMMENDED]** Keep every fraud control. Change only the mechanics of capture:

| Step today | Change | Keeps fraud control? |
|---|---|---|
| Staff types serial number | **Scan the QR** | Yes — stronger; eliminates typos |
| Photo sent to WhatsApp group | **Photo uploaded in the staff app at redemption** | Yes — better; auto-linked to the redemption record |
| Card + bill + KOT stapled, shipped to HQ | Keep physical shipping, but **HQ reconciles against the app record** rather than hunting a WhatsApp thread | Yes |
| Hole punch | **Keep unchanged** | Yes |
| Physical card required | **Keep unchanged** | Yes |

The WhatsApp group is the weakest link in the current chain — it is unsearchable, unstructured, and has no link to the POS record. Moving that one step into the engine is the highest-value operational fix.

---

## 8. Playing to the two segments

**[CONFIRMED]** Repeat behaviour is not uniform: habit buyers repeat weekly (a thin daily layer exists), treat buyers repeat monthly or once in 2–3 months.

The same card does a different job for each.

| | **Habit buyer** (weekly+) | **Treat buyer** (monthly / 2–3 months) |
|---|---|---|
| Their barrier | No reason *today* | The occasion doesn't come round often |
| What the card must do | Give today a purpose | Shorten the gap between occasions |
| Season trio at ~6 visits | 6 weeks — comfortably achievable | 6 months — **too slow, they'll miss the season** |
| Play | The Full Gang annual arc, the Swap Wall, status | **Expiry-dated season with a visible deadline.** "The Street leaves in 3 weeks." Scarcity converts a 3-month gap into a 6-week one |

**[RECOMMENDED]** The treat buyer is where the frequency growth is, and **seasonal expiry is the lever** — not more content. A season that ends creates the deadline their occasion currently lacks.

**[DECISION NEEDED]** Season expiry policy. Season length must exceed expected completion time (~6 visits) for a habit buyer but pressure a treat buyer. A **4-month season with cards expiring at season end** is the starting recommendation, but it must be checked against actual visit-gap distribution before committing.

---

## 9. Content and social

This is where the programme feeds the standing "be active on social media" objective. The Surprise Card generates content you do not have to invent.

**[RECOMMENDED]** Always-on beats:

| Beat | Cadence | Format |
|---|---|---|
| Season launch | 3×/year | The three characters revealed. Hero art already exists in `assets/characters/` |
| "Who's missing?" | Weekly | Poll/sticker — which one can't you find? Free engagement, zero production |
| Completion posts | Ongoing | Repost customer set-completion photos. **This is the UGC flywheel** — the prize is the content |
| Figurine reveal | 3×/year | The unbuyable object. Highest-value asset you'll have |
| Swap Wall | Ongoing | Film it. Kids trading is inherently watchable |
| Near-miss | Ongoing | "3,000 people are one card away from The Street." Real scarcity, real drama |

**Rule:** every one of these is content *about a customer*, not about a product. That is what makes it postable, and it's what a purely product-led feed can't do.

**Character constraint reminder:** per `CLAUDE.md`, characters may appear visually using supplied artwork only — never AI-generated, never redrawn — and **must not speak in first person** until `brand/character-voices/` is written and approved. A season launch is a strong argument for finally defining three character voices at a time.

---

## 10. What NOT to do

Explicitly ruled out, so nobody proposes them later:

- ✗ **Any discount, ever.** No %-off, no BOGO, no happy hour, no weekday offer, no creator discount codes.
- ✗ **Points as a public cash-like currency** — the engine brief is right to hold this back. Keep points internal for liability only until legally reviewed.
- ✗ **Making the set easier by raising the character-card ratio.** That devalues scratch, which is the part that works.
- ✗ **Lowering the BDT 500 threshold.** It is currently just under Foodpanda's AOV of 511, which is close to optimal — nearly every delivery order earns exactly one card. Lowering it destroys the scarcity for no volume gain.
- ✗ **Guaranteeing the set.** Controlled randomness is the psychology. Trading is the pressure valve, not a guaranteed drop.

---

## 11. Engine spec — deltas to the brief's schema

These are the additions the admin panel needs **on top of** the tables already specified in the engine brief (§7). Everything else in the brief stands.

### 11.1 New table — `characters`

| Field | Example | Notes |
|---|---|---|
| `character_id` | `bhoppu` | Use the stable identifiers from `data/characters.json` |
| `character_name` | Bhoppu | |
| `market` | BD / SG | Merlulu is **SG only** |
| `season_id` | `S1_STREET` | |
| `description` | *(approved bio)* | Source: `data/characters.json` — do not rewrite |
| `art_path` | `assets/characters/…` | |
| `has_3d_model` | Yes / No | Only 4 of 9 today |

### 11.2 New table — `seasons`

| Field | Example |
|---|---|
| `season_id` | `S1_STREET` |
| `season_name` | The Street |
| `market` | BD |
| `character_ids` | `air-maxi, bhoppu, picchi` |
| `starts_at` / `ends_at` | date |
| `cards_expire_at` | date |
| `completion_reward_id` | `BADGE_S1 + ADDON_FREE` |
| `status` | Upcoming / Active / Closed |

### 11.3 New table — `registrations`

**Distinct from `redemptions`.** A registration grants nothing and therefore needs minimal validation.

| Field | Example |
|---|---|
| `registration_id` | UUID |
| `card_id` | UUID |
| `customer_id` | UUID |
| `phone_number` | +880… |
| `registered_at` | timestamp |
| `channel` | QR / WhatsApp / staff-assisted |
| `is_duplicate_for_customer` | Yes / No — drives the trade prompt |

### 11.4 New table — `set_completions`

| Field | Example |
|---|---|
| `completion_id` | UUID |
| `customer_id` | UUID |
| `season_id` | `S1_STREET` (or `FULL_GANG_2026`) |
| `completed_at` | timestamp |
| `reward_id` | `BADGE_S1` |
| `fulfilled_at` / `fulfilled_by` / `outlet_id` | |
| `status` | Pending / Fulfilled / Expired |

### 11.5 Additions to existing tables

| Table | Add | Why |
|---|---|---|
| `cards` | `season_id` | Season membership |
| `cards` | `qr_url` | Scan-to-register |
| `cards` | `registered_at`, `registered_by_customer_id` | Registration is a lifecycle state |
| `cards` | new status **`Registered`** | Sits between `Distributed` and `Redeemed`; a character card may end its life here |
| `customers` | `collection_state` (JSON) | Which characters held, per season |
| `customers` | `sets_completed` | |
| `customers` | `first_registered_at`, `last_seen_at` | Enables the repeat-rate metric in §12 |
| `rewards` | `is_discount` = **always No** | Enforce the brand rule in the schema itself |

### 11.6 Trading (Phase 2 — build later, design the table now)

`trades`: `trade_id`, `card_id`, `from_customer_id`, `to_customer_id`, `traded_at`, `outlet_id`, `status`. A trade is a transfer of a serial between customers — it must be logged, because an untracked transfer looks identical to fraud.

---

## 12. Metrics — retire the 3–4%

**[RECOMMENDED]** Stop reporting redemptions ÷ all cards. It measures nothing and it makes a healthy programme look broken.

| Metric | Definition | Why |
|---|---|---|
| **Scratch redemption rate** | Redeemed ÷ scratch distributed, **same period** | The real redemption number. Current data gives 40–81% because the periods don't align; plan at 60% and let the engine settle it |
| **Character registration rate** | Registered ÷ character cards distributed | The new headline metric. Today it is 0% |
| **Set completion rate** | Customers completing a season ÷ customers holding ≥1 card of it | Is the game winnable? |
| **Median cards to completion** | Actual vs the ~6 model | Validates or kills the season sizing |
| ⭐ **Repeat rate: registered vs unregistered** | Visit frequency of registered collectors vs everyone else | **The one that proves the programme works.** If collectors don't visit more often, the mechanic has failed, and no other metric matters |
| **Cards per customer** | Distribution, not average | Reveals the daily-superfan segment |
| **Outstanding liability** | Per the engine brief §10 | Unchanged — keep it |

The starred metric is the business case. Instrument it first.

---

## 13. Rollout sequence

Ordered by dependency and by value-per-unit-of-effort.

| Phase | Ship | Depends on |
|---|---|---|
| **0 — now, zero build** | Print the season's three characters as a tick-box strip on the back of every card alongside the colour-in art. Costs nothing, and it alone creates visible progress | Next print run |
| **1** | Seasons: restructure the print run to 3 characters. Launch Season 1 | Season calendar decision |
| **2** | QR + registration. `registrations` table, WhatsApp or web endpoint | Phase 1 |
| **3** | Season badge card + free add-on fulfilment. `set_completions` | Phase 2 |
| **4** | Swap Wall, physical, piloted at one large outlet | Phase 1 |
| **5** | Redemption friction fixes — QR scan at POS, in-app photo | Engine build |
| **6** | Full Gang collector's folder | Print-cost decision |
| **7** | Digital trading | Registration volume |

**Phase 0 is free and should not wait for the engine.** A checklist printed on the back of a card you're already printing is the highest return-per-taka action available in this entire document.

---

## 14. Open decisions

Carried forward for Jawat / the team. Per the engine brief's rule, these are **not** answered here.

1. **Season calendar** — order, start dates, length. Recommendation: 4 months, Late Shift held for year-end.
2. **Season expiry** — do cards die at season end? Recommendation: yes, it's the treat-buyer lever. Needs checking against real visit-gap data.
3. ~~Figurine economics~~ — **RESOLVED 23 Aug 2026. Withdrawn.** See §4.2. Replaced by the collector's folder. Remaining question is print cost and MOQ for the foil badge and the folder.
4. ~~"Batch" definition~~ — **RESOLVED 23 Aug 2026. A batch is 297 cards, 9.09% scratch.** `brand/BRAND.md`'s "~27,000 + ~3,500 per batch" describes a print run of ~100 batches and should be corrected in that file.
5. ~~Reward budget~~ — **RESOLVED 23 Aug 2026.** The BDT 35,000/month figure is coherent on a COGS basis at ~60% redemption. See §4.4. **Superseded by** the rate-based budget in §4.5: a **2.0% of qualifying revenue** operating ceiling. Remaining input needed: **actual food COGS %**, currently assumed at 30%.
5a. **Card printing cost** — not yet in any budget line. Needed to complete §4.5.
6. **Singapore** — Merlulu makes ten characters. Does SG run a fourth season, or a different structure? Do not mix the rosters.
7. **Character voices** — a season launch is the natural moment to define three at a time. Currently blocked; `brand/character-voices/` is empty.
8. **Free add-on vs free item** — confirm the no-discount boundary covers gifts. This document assumes a gift is not a discount.

---

## 15. Compliance flags

Raised for review, not resolved here. The engine brief's §18 cautions all still apply, plus:

**⚠ Under-18 exposure — risk materially reduced, but still worth a look.** The audience on file is **primary 10–25**. The mechanic is a randomised collectible obtained through a monetary spend threshold, with scarcity pressure. That general shape is what regulators in several markets have moved against, and Singapore-entity IP positioning raises the stakes if the programme scales internationally.

**[UPDATED 23 Aug 2026]** Dropping the figurine (§4.2) removes the sharpest edge of this. What remains is a low-value ladder — a foil card, a printed folder, a free scoop of ice cream — attached to cards given away free with a purchase the customer was already making. That is a materially different thing from a paid loot box, and the entire reward ladder now sits under BDT 70 of true cost per item.

It still deserves a considered view before the scarcity is marketed hard, but this is now a routine promotional-compliance check rather than a structural question about the mechanic.

**[DECISION NEEDED]** Legal review covering: promotional compliance, T&Cs, expiry and redemption terms, delivery-platform policy alignment, customer data privacy for phone-number registration, and minors' participation.

---

## Appendix — key numbers at a glance

| | |
|---|---|
| Earning threshold | BDT 500/transaction (480 subtotal on delivery portals) [CONFIRMED] |
| Batch | 270 character + 27 scratch = 297 (**9.09% scratch**) [CONFIRMED 23 Aug 2026] |
| Characters, Bangladesh | 9 [CONFIRMED] |
| Characters, Singapore | 10 (the nine + Merlulu) [CONFIRMED] |
| Cards to complete all nine, current design | ~28 (~BDT 14,000, ~6.5 months) |
| Cards to complete a 3-character season | **~6 (~BDT 3,025, ~6 weeks)** |
| Scratch redemption rate | 40–81% [derived]; **plan at 60%** |
| Character card engagement rate | **0% — nothing is currently measurable** |
| Scratch reward menu value per batch | BDT 5,935 (avg BDT 220) |
| True reward cost per batch @30% COGS, 60% redemption | BDT 1,068 — **0.72%** of qualifying spend |
| Current monthly reward cost (modelled) | ~BDT 34,700 vs BDT 35,000 budgeted — **coherent** |
| **Recommended budget basis** | **2.0% of qualifying revenue** (~BDT 96,000/mo at current volume) |
| Food COGS | **30–45%, varies by product [CONFIRMED]**; blended point figure pending |
| Franchising | Expected ~Aug 2027; all outlets currently owned [CONFIRMED] |
| Value language | **Never say "free" or "discount"** [CONFIRMED — see §4.6] |
| Typical repeat cycle | Weekly (habit) · monthly to 2–3 months (treat) [CONFIRMED] |
| Peak days | Thu/Fri/Sat BD; local weekend elsewhere [CONFIRMED] |
| Capacity at peak | Headroom exists [CONFIRMED] |
