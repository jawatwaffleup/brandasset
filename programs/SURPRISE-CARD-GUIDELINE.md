# The WaffleUp Surprise Card

### Programme design and engine specification

**24 August 2026 · revised 26 and 27 August 2026 · Waffle Up Global PTE Ltd.**
**Owner: Mohammad Jawat · Prepared by: Marketing**

---

## How to read this document

| Part | For | Contains |
|---|---|---|
| **A — The Programme** | The office | What the Surprise Card is, how a customer plays it, what it gives away, what it costs, and what we will never do |
| **B — The Engine** | Whoever builds the admin panel | Data model, algorithms, invariants, validation rules, configuration, reports |
| **C — Delivery** | Everyone | Rollout order, open items, the evidence the design rests on |

Statements are tagged **[CONFIRMED]** (decided), **[RECOMMENDED]** (proposed, not yet signed off), **[ASSUMPTION]** (our best figure, unverified) or **[DECISION NEEDED]** (blocked on someone).

**Nothing in Part B is hardcoded.** Every number ships at a standard value and is editable from the admin panel. The full parameter list is §14.

---
---

# PART A — THE PROGRAMME

---

## 1. What the Surprise Card is

**[CONFIRMED]** A customer who spends **BDT 500 or more** in a single transaction receives one Surprise Card, in a **sealed yellow WaffleUp pack**. The card number is not visible until the pack is torn open.

Three kinds of card come out of that pack:

| | Rate | What it is |
|---|---|---|
| **Character card** | ~90.8% | One of the Waffle Up Gang. Collectible, carries points, colour-in back |
| **Scratch card** | **9.09%** | An instant win — a food item, claimed at any outlet |
| **The Golden Waffle** | **1 in 1,000** | The rarest thing we print. §4.3 |

**[CONFIRMED]** A batch is **297 cards: 27 scratch, the rest character**, with Golden Waffles seeded across the print run at one per thousand cards.

### The problem this design solves

The scratch card already works. Between 40% and 81% of scratch cards get redeemed — an excellent result for a paper coupon that requires a physical store visit.

**The character card does nothing.** Nine of every ten cards we print have no reward, no completion payoff, no way for the customer to see progress, and no reason to keep them. We are running a working loyalty programme at 9% of its printed volume and giving away the other 91% as a nice piece of paper.

Worse, the collection cannot realistically be finished. Drawing all ten characters at random takes about **40 cards — BDT 20,000 of spending across ten months** — with no prize at the end and no scoreboard. Nobody plays a game they cannot win.

**Everything below turns the other 91% into the programme.**

---

## 2. How a customer plays it

```
1. Spends BDT 500+           →  gets a sealed yellow pack
2. Tears it open             →  a card, with a unique number
3. Logs in at waffleup.global   (same account as the merch shop)
4. Enters the card number    →  the card registers to them
                             →  POINTS ARE REVEALED
                             →  their collection updates
5. Three duplicates          →  swap for any character they're missing
6. Points reach a merch item →  redeems, picks a Redemption Point
7. Gets an SMS: PIN, product, outlet
8. Collects in person        →  staff check the PIN
```

### Three loops, running at three speeds

This is the heart of the design. A customer always has something close and something far away.

| Loop | Speed | What it is |
|---|---|---|
| **The reveal** | Every single card | Points revealed at registration, 5–18. A small win, every time |
| **Points → merchandise** | First reward on the **first card** | The fast loop. Something real in hand almost immediately |
| **The Full Gang** | **~16 cards, ~4 months** | The long goal. All ten characters |

**[CONFIRMED]** On top of those, four **limited-edition cards a year**, tied to real occasions — §3.2.

### Why it works now when it didn't before

1. **The collection is finishable.** Three duplicates swap for a character you're missing, which collapses the long tail — 40 cards becomes 16.
2. **Progress is visible.** The account is the scoreboard. Before this, a customer had no way of knowing what they held.
3. **Every card is worth something.** A duplicate still awards points *and* counts toward a swap. **No card in a customer's hand is ever worthless.**

---

## 3. The cast, and the collection

### 3.1 All ten, always

**[CONFIRMED]** Every character is in circulation at all times. There is no rotation and no seasonal roster.

**Priority order**, from `brand/CHARACTER-BIBLE.md`:

**Bhoppu · Air Maxi · Mr Waffle · Picchi · Swirly · Merlulu · Spacy · Stovy · Tvy · Icy**

**All ten are equally common. [CONFIRMED 27 Aug 2026 — Jawat]** The print run carries Merlulu at the same quantity as everyone else, so his `rarity_weight` is **1.0** and he arrives about **1 in 10** — not the 1 in 30 this section specified until 27 August 2026.

> **Merlulu is not precious, he is unique.** His point value is set at the same level as Air Maxi's — a good card, not a jackpot. What makes him worth having is that he completes the Gang, and that he is the Merlion: Singapore is where Waffle Up Global was founded, and that story tells itself whether or not the card is scarce. **[CONFIRMED]**

> **What changed, and what did not.** Scarcity was doing less work than it looked. Re-modelled at 40,000 trials (§11.5), the standard three-duplicate conversion rule finishes the Gang in a **median of 16 cards either way** — 15.8 mean at 1 in 30, 15.5 at equal weight. Conversion absorbs the difference almost entirely. Scarcity only bites without conversion, where the mean falls from 39.8 cards to 29.4. **The chase was never really about how rare Merlulu was; it was about the swap rule.** What the change does cost is this design pillar and the published-odds line, and it raises the expected mint per character card from 11.59 to **11.71**, which forced `batch_point_cap` up with it — see §7.5 and §11.2.

### Merlulu ships with everyone else

**[CONFIRMED 26 Aug 2026]** Merlulu goes to print on the **base design** — the artwork we already have. He is `live` and in card generation from launch, and **the Full Gang is ten from day one.** No locked slot, no phased reveal, nothing on the critical path.

The cards already in circulation carry the old art and read "she". New print runs read "he", and the old ones are never reprinted — which makes them a genuine First Edition acquired for nothing (§12.1a). That is a content beat, not a problem to solve.

The **roster state** mechanism stays in the engine — `hidden`, `locked`, `live`, set independently of print readiness — because it is how any *future* character gets introduced, and a locked slot is a better hook than an absent one. It is simply not needed for Merlulu. A locked character does not count toward the Full Gang target.

### The milestones

**[CONFIRMED]**

| Milestone | Reward |
|---|---|
| **Half the Gang** — any 5 of 10 | **+50 points** |
| **The Full Gang** — all 10 | **+200 points** + the collector's folder |
| **The Year's Four** — all four occasion editions in a calendar year | **+200 points**, repeatable every year |

Completing the Gang takes about 16 cards and earns roughly **435 points** all in — a T-shirt with change, or most of the way to a hoodie. It is a four-month goal for a weekly customer, and a genuine year's project for a monthly one.

### 3.2 Occasions, not seasons

**[CONFIRMED]** Four times a year we release a **limited-edition design of an existing character** — not a new character, and not a rotation of the roster.

| Occasion | When |
|---|---|
| **Pohela Boishakh** | 14 April |
| **Eid ul-Fitr** | moves |
| **Eid ul-Adha** | moves |
| **Victory Day** | 16 December — also the Banani anniversary |

**How it works:** during the window, a proportion of character cards carry the special edition artwork instead of the standard. When the window closes the design is **retired and never reprinted.** A customer who has it, has it.

**Why this and not seasons:**

- **The occasion is real.** We are joining something the country already observes, not inventing a reason for a card to be special.
- **It doesn't touch the base collection.** Any Bhoppu completes Bhoppu — see the rule in §12.1a. Occasion editions are a second, optional layer for the completionist.
- **It gives collectors a permanent chase.** Once someone has all ten, the editions are what keeps them collecting.
- **Marketing gets a calendar that already exists**, four moments a year, each with genuine cultural weight.

### 3.3 What expires

**[CONFIRMED]** Almost nothing, and that is deliberate.

| | Expires? |
|---|---|
| Registering a card | **Never.** Any card, any time |
| Points, once awarded | **Never**, unless the account is completely inactive for 12 months — and then only with 30 days' notice |
| Progress toward any milestone | **Never** |
| An occasion edition | **Never expires once held.** It simply stops being printed |
| **A scratch card's food reward** | **`scratch_validity_days` — 180.** The one real expiry in the programme |

**The scratch card is the exception, and it always was.** A scratch card is a coupon for a food item, and a coupon that never lapses is an open-ended kitchen liability. Batch 9's cards were printed December 2025 and Ops report them out of use by August 2026, which is where the 180-day standard comes from — **[DECISION NEEDED]** for Ops to confirm.

> This does not weaken anything above it. **A character card and the points on it never expire**, which is enforced by a constraint rather than by convention: only a scratch card may carry an expiry at all (invariant 15). And an expiry is never a message we send — the card says what it says, and nothing in §8's language changes.

> The urgency in this programme comes from **supply, not deadlines.** The Eid card stops being made. Nothing a customer already holds is ever taken away from them, and no message we send ever threatens to.
>
> ✓ *"The Eid card stops printing on the 12th."*
> ✗ *"Your progress dies in 3 weeks."*

---

## 4. Points

### 4.1 What earns points

**[CONFIRMED]**

| Event | Points |
|---|---|
| Registering a character card — **duplicates included** | **5–18**, revealed at registration |
| Half the Gang — 5 of 10 | **+50** |
| The Full Gang — all 10 | **+200** |
| The Year's Four — all occasion editions in a year | **+200** |
| Finding a Golden Waffle | **+100** |
| Scratch card | **0** — it already paid out in food |

### 4.2 Why the points vary

Every card awards a random amount between 5 and 18, revealed when the customer registers it. That reveal is a small win on every card, and it is what makes opening the site worth doing rather than a chore.

**The odds are weighted by character, but every character can roll every number.** Bhoppu trends high; Icy trends low; an Icy still rolls a perfect 18 about once in 45. Nobody ever holds a worthless card, and *"an 18 on an Icy"* is a better story than a guaranteed-high Bhoppu.

| Character | Average | Chance of an 18 |
|---|---|---|
| Bhoppu | 13.8 | 16.1% |
| Air Maxi | 13.4 | 13.9% |
| **Merlulu** | **13.4** | 13.9% |
| Mr Waffle | 12.9 | 11.7% |
| Picchi | 12.3 | 9.8% |
| Swirly | 11.8 | 8.0% |
| Spacy | 10.7 | 5.0% |
| Stovy | 10.1 | 3.9% |
| Tvy | 9.6 | 2.9% |
| Icy | 9.2 | 2.2% |
| **Average per card** | **11.6** | |

**Merlulu sits at Air Maxi's level deliberately** — his scarcity is the reward, not his point value.

The weighting is one dial in the admin panel. **Turning it up or down does not change what the programme costs** — the roster average holds steady at every setting. The maths is in §11.2.

### 4.3 The rare finds

**[CONFIRMED]**

| | Rate | What you get |
|---|---|---|
| **The reveal** | Every card | 5–18 points |
| **Scratch card** | 1 in 11 | A food item |
| **Merlulu** | **~1 in 10** | Completes the Gang. Air Maxi's point value. *No longer a standing rare — see §3.1* |
| **The Golden Waffle** | **~1 in 1,000** | **+100 points** — double any milestone, roughly nine ordinary cards in one find |

**The Golden Waffle is the rarest object we print** — about ten found a month across the whole business. It is precious because of what it is, not only what it pays. **[RECOMMENDED]** every find is worth a post: the customer, the card, the reaction.

**[RECOMMENDED]** Golden Waffle holders also get first look at the next limited edition before it goes public. Costs nothing, and status is what gets shared.

---

## 5. Rewards and merchandise

### 5.1 The merchandise ladder

**[CONFIRMED]** Points buy WaffleUp merchandise. Every item is also genuinely sold in the shop at a real price. Costs below are actuals from the vendor list, August 2026.

> ### One rule sets the whole ladder
> **A point costs one taka to produce, so an item's point price is simply its production cost in taka.**
> No conversion table, no judgement call per item, and a new product prices itself the moment a vendor quotes it.

| Item | Points | ~Cards | Production cost | Suggested shop price | Vendor |
|---|---|---|---|---|---|
| **Sticker** — character or page | **10** | **~1** | 5.50 | 30 | Bijoy |
| Pen & box | 35 | ~3 | 35 *(box included)* | 100 | Bijoy |
| Pop socket — 10 designs | 40 | ~3 | 37 | 100 | Case Corner |
| Calendar | 65 | ~6 | 50 + 15 box | 170 | Monir |
| **Notebook** — 3 designs | **95** | **~8** | 95 *(wrapping included)* | 250 | Bijoy / Asha |
| Socks — kids, 2 colours | 140 | ~12 | 90–100 + 40 box | 350 | Toco |
| Socks — adult, 2 colours | 175 | ~15 | 135 + 40 box | 450 | Toco |
| Water bottle | 195 | ~17 | 190 + 5 box | 500 | Customized & Crafts |
| Cap — mesh | 300 | ~26 | 235 + 62 box | 750 | Toco |
| Cap — all-over print | 310 | ~27 | 250 + 62 box | 800 | Toco |
| T-shirt — pink or black | 350 | ~30 | 350 | 900 | Gorur Ghash |
| Hoodie — pink or black | 580 | ~50 | 581 | 1,500 | Gorur Ghash |

**[CONFIRMED] Every item ships in its box.** Where a product has its own packaging on the vendor list, that cost is inside the point price above — so a cap arrives boxed, socks arrive in their tube, the calendar in its pink box. Pop socket wrapping is not used.

**The paper gift bag (BDT 35) is not part of this catalogue at all.** [CONFIRMED] It is reserved for goodies given to new employees and important guests, and it should never be costed into a point redemption or a shop sale.

> **Adding the boxes does not change what the programme costs.** Points are minted at a fixed rate per batch, and because a point price *is* the production cost, every point redeemed costs BDT 1.00 whatever it buys. The box raises the SKU's point price so the cost per point holds steady. What changes is how far a customer's points go — the cap moved from ~20 cards to ~26.

**[CONFIRMED 26 Aug 2026] Shop prices are not fixed — these are the launch values.** The column above runs at a consistent **~2.6× production cost, boxed**, a multiple validated by Jawat's own notebook figure of BDT 200–300 against a BDT 95 cost. We list at these and adjust once we see what the Dhaka market actually pays. The two caps at BDT 750–800 are the pair to watch.

> **Every price in this table is a field in the admin panel, not a number in the code.** So is every name, image, variant and stock figure. See **§15.1 — the no-deploy rule.** Nothing in this catalogue needs a developer to change.

**The sticker is the most important line in this table.** At 10 points it is reachable on a customer's *first card*. The industry evidence is blunt: people who redeem spend **3.1× more** than people who don't, and the first redemption is the moment someone stops holding a card and becomes a collector. A one-card entry point is the cheapest customer conversion available anywhere in this programme.

Completing the Full Gang earns about **435 points** — a T-shirt with change, or most of the way to a hoodie.

**Not in the catalogue:** the **collector's folder** (§5.2) does not yet exist and has no quote. It is a print job and should be quoted by Bijoy at Asha Printers, who already produce the cards.

**[CONFIRMED]** More products are coming. Adding one is a row in the admin panel — name, production cost, shop price, stock — and the point price follows from the cost automatically.

### 5.2 What cannot be bought

**[CONFIRMED]** The **collector's folder** is never in the shop, never has a price, and cannot be bought with points. It is earned by completing the Gang, and that is the entire reason it is worth having.

### 5.3 The catalogue is a living list

**[CONFIRMED]** The admin panel can add an item, take one off the list, or mark it out of stock at any time.

| State | Behaviour |
|---|---|
| **Available** | Listed and redeemable |
| **Out of stock** | **Still listed and still visible**, but not redeemable. Never hidden — someone is saving for it |
| **Retired** | Off the list, but still honoured for any PIN already issued |

**An item people are saving toward is never deleted, and a point price is never raised on someone already saving for it.**

---

## 6. Where things are collected

**[CONFIRMED]**

| | Rule |
|---|---|
| **Merchandise** | Collected in person at a **Redemption Point** — a named list of standard outlets, chosen for footfall and storage |
| Cloud kitchens | Not Redemption Points — there is no counter |
| Chef's Table | Not initially — handing over merchandise is wrong for that service |
| **Delivery of merchandise** | **Never as a paid delivery of a point redemption.** Either collected at a Redemption Point, or **sent along with a paid order** — §6.2. Merchandise *bought with money* delivers normally |
| **Scratch card food** | Claimable at **every** outlet, Chef's Table included |
| **Price book** | Every reward is valued at the **standard price book**, wherever it is claimed |

**Why redemption is in-person only.** This is not an inconvenience we are imposing — it is the most valuable part of the design. When a member comes in to collect a reward, they buy something else while they are there. The industry calls it the redemption halo, and one measured convenience chain got **one extra visit per member per month** out of it. Collection *is* the mechanic.

### 6.1 How collection works

**[CONFIRMED]**

1. Customer redeems online and chooses a Redemption Point.
2. **The item is reserved against their PIN immediately.** A customer arriving to find their item gone is the worst thing this programme can do, and it is entirely preventable.
3. They get an SMS in the same format as an order confirmation: **PIN, product, outlet.**
4. They collect. Staff check the PIN and the **last four digits of the registered phone number** — a PIN on its own can be sold.
5. PINs expire after 14 days and the stock goes back on the shelf.

### 6.2 The delivery-only customer

**[CONFIRMED 26 Aug 2026]** In-person collection stays the default, for the reason above — the visit *is* the mechanic, and it wins us counter customers we would otherwise never see. But someone who only ever orders from a cloud kitchen can earn points and never have a counter to reach, and that has to be answered.

**The answer: the reward rides along with a paid order.** At redemption the customer chooses *"send it with my next order"* instead of a Redemption Point. The item is reserved immediately, exactly as at a counter, and goes into the bag the next time they order.

| | |
|---|---|
| **Costs nothing** | The order was already being delivered. There is no delivery charge to pay, absorb or argue about |
| **Names no value** | No cash changes hands at the moment a reward arrives |
| **Still requires a purchase** | Which is the commercial point of collection in the first place — and it preserves the programme's own logic: **a reward arrives with a purchase the customer already chose to make** |
| **No new operation** | §13.6 already has the packer entering a card serial against the `order_id` at bag-seal. The order ticket simply also shows "reward to attach" |
| **Small items only** | Sticker · pen · pop socket · calendar · notebook. Apparel, caps, socks and bottles stay counter-only — they do not fit the bag, and colour-and-size handover needs a human |

**Two ideas considered and rejected.**

> **Cash on delivery for the shipping charge.** Rejected. A customer paying BDT 70 to receive their reward has just been told what the reward is worth — precisely what §8 exists to prevent — and a reward you pay for stops being a reward. It also puts COD reconciliation, refusals and returns onto an order with no sale value behind it.
>
> **Paying the delivery charge with points.** Rejected. "Delivery: 70 points" states a taka value the moment a customer knows what delivery costs, it spends the reward budget on logistics instead of on a product, and it deletes the redemption halo — the one thing that makes in-person collection commercially worth its friction.

**Still [DECISION NEEDED]:** the Redemption Point list itself, chosen for footfall, storage *and* coverage against the cloud-kitchen catchments. Ride-along is the backstop, not a substitute for a reachable counter.

---

## 7. What it costs

### 7.1 The scratch card

**[CONFIRMED]** 27 scratch cards per batch of 297:

| Reward | Qty | Menu price | Menu value |
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

**Menu price is revenue foregone, not money spent.** An ice cream given away costs us the ice cream, not BDT 135.

**[CONFIRMED 26 Aug 2026] Budget the reward mix at a flat 38% of selling price.** Item-level COGS is not to hand, so 38% of the standard-price-book menu price is the working figure across every reward.

| | Per batch |
|---|---|
| Menu value of the 27 scratch rewards | BDT 5,935 |
| **At 38% of selling price** | **BDT 2,255** |
| At 38%, planning at 60% redemption | **BDT 1,353** |

### 7.2 The saving the flat figure hides

Real COGS varies by item, and the customer judges a gift by its **menu price** — so there is an optimisation sitting in the reward mix: **pick rewards where menu price is high relative to what they actually cost us.** Illustratively: a Hot Chocolate that feels like a BDT 320 gift but costs BDT 80 to make is a better reward than a Kunaffle™ that feels like BDT 280 and costs BDT 126 — less perceived generosity for more real cost. *(Those two figures are plausible, not measured — which is exactly the problem.)*

> **A flat 38% cannot see this.** Under a flat assumption every item costs exactly 38% of its menu price by construction, so every possible reward mix looks equally efficient. **The saving is real in the kitchen; it is the assumption that is blind to it.**

**[DECISION NEEDED — still open]** Item-level COGS. It changes nothing the customer can see, and it lets us hold the headline menu value at BDT 5,935 per batch — so the programme feels exactly as generous — while cutting real cost by an estimated **15–25%**. 38% is a sound number to *budget* against. It is not a number to *design the reward mix* with.

### 7.3 Card printing

**[CONFIRMED]** Actual costs, August 2026, from Bijoy at Asha Printers:

| | Per card | Per 297-card batch |
|---|---|---|
| Character card | BDT 3.00 | 270 × 3.00 = 810.00 |
| Scratch card | BDT 3.40 | 27 × 3.40 = 91.80 |
| **Total** | | **BDT 901.80** — **0.61%** of qualifying spend |

At current volume that is about **BDT 29,300 a month.**

> **[CONFIRMED 26 Aug 2026] BDT 3.00 and 3.40 are the printed-and-sealed cost — the cover is inside them.** The vendor sheet backs this up: both card lines specify a 600gsm Swedish board card at 2″×3.5″ **and** a 2.5″×4″ cover in the same spec, with the separate "Surprise Card Cover" line (150gsm art paper, matte lamination) describing that cover rather than pricing an extra item.
>
> **This closes the flag.** The printing figure is a **total, not a floor.** §7.4 stands as written, and card printing sits comfortably inside its 0.65% ceiling.

**The one line still genuinely unpriced is the Surprise Card Box** — the outer carton the cards ship to outlets in, typed *Others* on the vendor sheet, not *Branding*. It is a logistics item: one box per few hundred cards, amortised at fractions of a taka per card, and it never touches a customer's hand. **[DECISION NEEDED]** — worth getting quoted for completeness, but it is not a material budget line and it does not hold up anything.

### 7.4 The whole programme

Each batch of 297 cards represents **BDT 148,500** of qualifying spend.

**The three cost lines, at face value:**

| | Per batch | % of qualifying spend |
|---|---|---|
| Points minted — 3,156 × BDT 1.00 | 3,156 | 2.13% |
| Scratch rewards at cost — 38% of BDT 5,935 menu | 2,255 | 1.52% |
| Card printing — cover included | 902 | 0.61% |

**What it actually costs depends on two behaviours:** how many of those points get registered and spent, and how many scratch cards get redeemed. Printing costs the same either way.

| Scenario | Giveaway | All-in | |
|---|---|---|---|
| **Realistic** — 40% register, 50% of those points spent, 60% of scratch redeemed | 1,984 · **1.34%** | 2,886 · **1.94%** | ← plan against this |
| Every point spent, 60% of scratch redeemed | 4,509 · 3.04% | 5,411 · 3.64% | |
| Every point spent, **81%** scratch — the highest rate ever observed here | 4,983 · 3.36% | 5,885 · **3.96%** | ← the real worst case |
| Theoretical maximum — every point, every scratch card | 5,411 · 3.64% | 6,313 · 4.25% | never occurred anywhere |

The 50% burn figure is not a guess. **About half of all loyalty rewards go unclaimed across every industry measured** — we are planning conservatively. The 60% scratch figure sits inside our own observed 40–81% band.

**[ASSUMPTION]** At current volume — about 9,639 cards a month, **BDT 4,819,500** of qualifying revenue:

| Scenario | Monthly, all-in |
|---|---|
| **Realistic** | **~BDT 94,000** |
| Every point spent, 60% scratch | ~BDT 176,000 |
| Every point spent, 81% scratch | ~BDT 191,000 |
| Theoretical maximum | ~BDT 205,000 |

### 7.5 The budget rule

**[RECOMMENDED]** Two ceilings, not one, because they behave differently. Printing is a fixed production cost that scales with cards whether or not anyone plays; the giveaway only costs money when a customer actually receives something.

> | | Ceiling |
> |---|---|
> | **Giveaway** — points + scratch rewards | **3.5% of qualifying revenue** |
> | **Card printing** | **0.65%** |
> | **All-in programme** | **4.15%** |

**The giveaway ceiling moved from 3.0% to 3.5%, and it is worth being explicit why.** 3.0% was set when the reward mix was modelled against a 30–45% COGS *range*. The confirmed working figure is a flat **38% of selling price** — dearer than the bottom of that range, applied to every item. So the old ceiling was breached on paper by arithmetic, not by anybody's behaviour. Per rule 2 below, **the response to a ceiling the design breaches is to reset the ceiling, not to shrink the reward.**

**[CONFIRMED]** Three rules that make this behave:

1. **Budget it as a rate, never as a fixed taka figure.** A fixed number goes stale every time the business grows. A rate scales itself.
2. **If we breach the ceiling, we raise it — we do not cut the reward.** A breach means people are completing collections, which means the mechanic is working. Cutting rewards at that exact moment kills the thing we just proved.
3. **We never devalue points already issued.** If costs need managing, the lever is the catalogue going forward — which items are listed and at what price. Never a balance someone already holds. Re-pricing issued points is how loyalty programmes lose people permanently.

**How much headroom 3.5% actually buys.** Quite a lot, and it is worth knowing the exact shape of it. Points are held to `batch_point_cap` — **3,300**, against an expected mint of ~3,164 — by the generator, so the only variable left is scratch redemption. **The giveaway ceiling cannot be breached unless scratch redemption passes ~90% while every single point issued is also spent.** The highest rate we have ever observed is 81%, and points burn at nearer 50% everywhere it has been measured. Realistic run-rate is 1.94% all-in — a little under half the ceiling, which is where a ceiling should sit.

**If that combination ever did arrive**, the lever exists and it is exact: **lower `batch_point_cap`.** Dropping it from 3,300 to **2,940** guarantees the 3.5% giveaway ceiling even at 100% scratch redemption and 100% point burn simultaneously, at a cost of about **0.8 points per card**. Because points are minted at print time, the ceiling is enforced by arithmetic rather than by watching a dashboard.

**The better first lever, though, is §7.2** — item-level COGS and a reward mix built on it recovers an estimated 15–25% of scratch cost with nothing the customer can see. Reach for that before touching anyone's points.

**Note on merchandise:** merchandise given away for points counts against the giveaway ceiling at production cost. Merchandise **sold** for money is a separate business line with its own margin and does not touch this budget.

---

## 8. How we talk about it

**[CONFIRMED]** **WaffleUp may give value away. It must never name it, quantify it, or label it.** The words "free" and "discount" are banned outright — cards, screens, social, staff scripts, Bangla and English alike.

| ✗ Never | ✓ Instead |
|---|---|
| "Get a FREE ice cream!" | "Ice cream comes with it." |
| "Worth BDT 135!" | *(say nothing)* |
| "Collect and save!" | "Collect the Gang. See what happens." |
| "Special discount for collectors" | "Collectors get first look." |
| "500 points = BDT 250 value" | *(never)* |

This applies to what staff say, not only what we print. If a staff member says "you get a free ice cream," the customer hears a giveaway and the brand becomes cheap.

### 8.1 Why merchandise can carry a price

**[CONFIRMED]** There is an apparent contradiction here worth resolving explicitly, because the whole merchandise plan depends on it.

> **The rule stops WaffleUp naming the value it gives away. It does not stop a product having a price.**
> The difference is **who does the arithmetic.**

| | |
|---|---|
| ✗ **Banned** — we state the value | "Redeem for a notebook — worth BDT 250!" |
| ✓ **Allowed** — the product has a price and the customer works it out | The notebook sits in the shop at BDT 250 with a price tag, like any product. Separately, collectors can unlock it. |

**The drive comes from the customer's own realisation, never from our boast.** That is the entire mechanism, and it is why this works where "worth BDT 250" would not.

**Four conditions:**

1. **The shop price must be real.** Genuinely sold at that price to paying customers. An invented price to make the reward look bigger is dishonest and legally exposed.
2. **Never state value at the moment of redemption.** No "worth", no "value", no "you saved".
3. **Point prices and taka prices never appear on the same screen for the same item.** The shop shows taka. The collection shows points. The customer connects them; we never draw the line.
4. **Never side by side** — no "BDT 250 or 400 points".

**The test:** if the customer could work out the taka value *from words WaffleUp wrote*, rewrite it.

---

## 9. What we will never do

**[CONFIRMED — binding.]** This programme is designed to be genuinely compelling. It is not designed to be compulsive, and the distinction is commercial as much as ethical: our primary audience starts at **age 10**, and we are a Singapore-registered company expanding into UAE, Thailand and Indonesia.

| We use | We never build |
|---|---|
| Random rewards — the reveal, the scratch, Merlulu, the Golden Waffle | Any purchase made *only* to buy a chance |
| Scarcity of a **thing** — an edition that stops printing | Countdown pressure toward a price |
| Visible progress — "7 of 10", the folder, the scoreboard | Streak-loss guilt, decaying balances, "you'll lose it" |
| Social proof, the Wall of Fame, near-miss content | Marketing messages aimed at minors |
| Collection, status, early access | Paid re-rolls, buying points, buying cards |

> ## The line we do not cross
>
> **A card only ever arrives with a purchase the customer already chose to make. No card is ever sold, and no chance is ever purchasable.**

This is not caution. It is the single fact that keeps this programme legal everywhere we operate and everywhere we plan to. Every country that has restricted this kind of mechanic has restricted **paid** randomness — Belgium and the Netherlands ban paid loot boxes outright, Brazil bans selling them to under-18s, the EU is moving the same way. **Because our cards come free with a purchase and are never sold, none of it applies to us.** Cross that line in any market, for any campaign, and the whole position collapses.

### 9.1 Protecting younger customers

**[CONFIRMED]**

- Registration asks for **year of birth.**
- Under 16, the account needs a **guardian's phone number**, and the guardian must confirm by SMS reply before the account activates.
- Accounts belonging to minors carry standing restrictions: **no marketing messages ever**, in-person collection only, and no appearance on any public leaderboard or Wall of Fame without separate consent.

### 9.2 Anti-scalping caps

**[CONFIRMED]** Not theoretical. **McDonald's Japan had to end a Pokémon card promotion early in August 2025** because people bought meals purely for the cards and threw the food away. They now cap purchases and block delivery apps at launch.

Our BDT 500 threshold is a natural brake — hoarding is expensive here in a way a Happy Meal is not. But a limited edition that stops printing is exactly the mechanic that produces this behaviour.

| Cap | Standard |
|---|---|
| Cards registered per phone per day | 10 |
| Cards registered per phone per month | 60 |
| Duplicate swaps per phone per month | 5 |
| Cards issued in a single transaction | 10 |
| Redemptions per phone per day | 2 |

**Hitting a cap queues an account for review. It never deletes anything.** A genuine superfan must not be punished for being one.

---

## 10. The two kinds of customer

**[CONFIRMED]** Repeat behaviour is not uniform. Habit buyers come weekly. Treat buyers come monthly, or once in two or three months.

| | **Habit buyer** | **Treat buyer** |
|---|---|---|
| Their barrier | No reason to come *today* | The occasion doesn't come round often |
| What the card must do | Give today a purpose | Shorten the gap |
| The Full Gang means | ~4 months — a real project | ~a year — the long arc |
| The lever | Milestones, the points ladder, the Golden Waffle | **The occasion window.** A card that stops printing |
| First redemption | The sticker is in reach on their **first card** | **A reward reachable on card one is why they come back at all** |

**The treat buyer is where frequency growth lives.** The two levers that reach them are the occasion window and a cheap first redemption — not more content.

---
---

# PART B — THE ENGINE

**For the team building this in the WaffleUp admin panel.**

This part assumes the existing Surprise Card engine — card generation, serial tracking, scratch redemption, fraud controls, liability reporting — and specifies what is added on top.

---

## 11. Core algorithms

### 11.1 Card generation

A batch is generated as a unit. **Point values are assigned at generation, not at registration.**

```
generate_batch(batch_size=297, scratch_ratio=0.0909,
               golden_rate=0.001, point_cap=3300, occasion_id=None):

    n_scratch   = round(batch_size * scratch_ratio)          # 27
    n_golden    = seeded_from_print_run(batch_size, golden_rate)   # usually 0, sometimes 1
    n_character = batch_size - n_scratch - n_golden

    cards = []
    for i in range(n_scratch):
        cards.append(Card(type='scratch', reward=next_from_reward_mix()))

    for i in range(n_golden):
        cards.append(Card(type='golden_waffle', point_value=golden_waffle_points))

    for i in range(n_character):
        character = draw_character()                          # see 11.3
        design    = draw_design(character, occasion_id)        # see 11.3
        value     = draw_point_value(character.point_rank(), design)
        cards.append(Card(type='character',
                          character_id=character.id,
                          design_id=design.id,
                          point_value=value))

    # HARD CONSTRAINT — not a report
    if sum(c.point_value for c in cards) > point_cap:
        normalise_down(cards, point_cap)                      # see 11.4

    assign_serials(cards)
    shuffle(cards)
    return cards
```

**Golden Waffles are seeded at print-run level, not per batch.** At one in a thousand, most batches contain none. Seeding across the run keeps the rate honest without forcing one into every batch.

**Why values are assigned at generation:**

| | |
|---|---|
| **Auditable** | Every card's value is fixed and provable before a single card ships |
| **No re-roll exploit** | There is nothing to retry and nothing to time |
| **Liability known at print time** | Not discovered afterwards |
| **The budget ceiling becomes arithmetic** | The cap is enforced by the generator, not by monitoring |

### 11.2 The point value draw

An exponential tilt over a discrete band. One parameter controls the whole weighting.

```
draw_point_value(point_rank, design):

    band   = design.point_band_override or point_band     # default 5..18
    LO, HI = band
    MID    = (LO + HI) / 2                                # 11.5
    HALF   = (HI - LO) / 2                                # 6.5
    s      = tier_skew_strength                           # 1.0

    w      = (10 - point_rank) / 9                        # 1.0 at rank 1 ... 0.0 at rank 10
    theta  = s * (2*w - 1)

    weights = [ exp(theta * (v - MID) / HALF) for v in LO..HI ]
    return weighted_random_choice(LO..HI, weights)
```

**`point_rank` is not `priority_rank`.** It defaults to it, but can be overridden per character. **Merlulu is priority rank 6 and point rank 2** — sixth in the fiction, Air Maxi's value in points.

> **Property to preserve if this is ever refactored: the unweighted roster mean is exactly `MID` at every value of `s`.** The tilt redistributes probability without changing the total, which is why the skew dial can be moved freely without re-costing the programme. Any replacement algorithm must keep this. **Treat the table below as a test fixture.**

**Reference output at `s = 1.0`:**

| point_rank | character | mean | P(=5) | P(=18) | P(≥15) |
|---|---|---|---|---|---|
| 1 | Bhoppu | 13.82 | 2.2% | 16.1% | 52.0% |
| 2 | Air Maxi | 13.36 | 2.9% | 13.9% | 46.8% |
| 2 | **Merlulu** *(override)* | 13.36 | 2.9% | 13.9% | 46.8% |
| 3 | Mr Waffle | 12.86 | 3.9% | 11.7% | 41.5% |
| 4 | Picchi | 12.33 | 5.0% | 9.8% | 36.2% |
| 5 | Swirly | 11.78 | 6.4% | 8.0% | 31.1% |
| 7 | Spacy | 10.67 | 9.8% | 5.0% | 21.7% |
| 8 | Stovy | 10.14 | 11.7% | 3.9% | 17.7% |
| 9 | Tvy | 9.64 | 13.9% | 2.9% | 14.1% |
| 10 | Icy | 9.18 | 16.1% | 2.2% | 11.2% |

**Expected value per character card: 11.71 points.** The roster is not ranks 1–10 once each — Merlulu carries point rank 2 as an override, so rank 2 appears twice and nothing sits at rank 6, which is why this sits above the 11.5 band midpoint. It was **11.59** while he was a 1-in-30 standing rare; equal print quantity gives that rank-2 value ten times the weight. The engine derives this figure rather than quoting it (`expectedPointsPerCharacterCard`), so it tracks `merlulu_rarity_weight` automatically.

At `s = 0` every character is identical. At `s = 2.5` Icy averages 7.07 and starts reading as a card nobody wants — hence the hard cap.

### 11.3 The two-stage draw

```
draw_character():
    pool = all characters where is_print_ready = true
    weighted by rarity_weight
    return weighted_random_choice(pool)

draw_design(character, occasion_id):
    if occasion_id and random() < occasion_edition_share:
        d = card_designs where character_id = character.id
            and occasion_id = occasion_id and is_print_ready = true
        if d: return d
    designs = card_designs where character_id = character.id
              and occasion_id is null
              and is_print_ready = true and is_retired = false
    return weighted_random_choice(designs, by rarity_weight)
```

**Character first, then design within that character.** Outside an occasion window stage two returns the character's standard design and is effectively a no-op.

**`rarity_weight` calibration.** **All ten characters ship at 1.0**, so stage one is a flat draw and every character is 1 in 10. The formula below is retained because it is what any *future* standing rare must be calibrated with — it is not currently in use.

For a target rate `r` against `n` ordinary characters at 1.0, `w = n·r / (1 − r)`. A 1-in-30 rate against nine ordinary characters is **9/29 = 0.3103**, which is what Merlulu carried until 27 August 2026. *(Getting this wrong is easy — a weight of 0.033 yields 1 in 274 against nine ordinary characters, not the 1 in 92 an earlier draft of this section claimed; 1 in 92 is what three ordinary characters would give. The formula and the 0.3103 result were always correct.)*

The `is_print_ready` gate stays in the draw as the mechanism for introducing future characters. **All ten current characters are print-ready**, Merlulu included.

### 11.4 Batch cap normalisation

If a generated batch exceeds `batch_point_cap`, reduce values rather than regenerate — regeneration would bias the distribution.

```
normalise_down(cards, cap):
    while sum(values) > cap:
        pick a random character card with value > band.LO
        decrement its value by 1
```

Log every normalisation. Frequent normalisation means the cap is set too low for the band.

> **⚠ `batch_point_cap` is a RATE, not a number — pro-rate it to the order.** 3,300 is the ceiling for **297 cards**, about 11.11 points a card. A real print order is nothing like 297: batch 11 was 33,500 cards. Applied flat, the generator would demand a 33,500-card run fit inside 3,300 points, drive every card to the band floor and then throw. The engine computes `ceil(cards × batch_point_cap ÷ batch_size)`. §7.5's promise that "the ceiling is enforced by arithmetic" only holds if the arithmetic knows how big the order is.

### 11.6 The printed card number

**[CONFIRMED 26 Aug 2026 — Jawat]** From **batch 14 onward** every card carries a number in one format:

```
B14F-7201647537
│ │ │ └────────── ten digits
│ │ └──────────── where the card is meant to be handed out
│ └────────────── the batch number
└──────────────── literally B, for batch
```

| Letter | Where the card goes |
|---|---|
| **F** | Flagship outlets |
| **C** | Chef's Table |
| **3** | Third party |
| **E** | Event |
| **G** | Gift |

**`3` rather than `T` for third party**, because Tvy exists and a card number gets read aloud across a counter more often than anyone expects.

This **formalises what batch 13 already did in its filing.** That workbook splits by channel in the sheet names — "Flagship - Character", "3rd Party - Scratch" — so the fact existed but lived in a spreadsheet. Now it is on the card, where a staff member can read it and a box can be checked against its label without consulting a summary.

> **The tenth digit is a check digit, not a random one.**
>
> Nine digits are random; the tenth is a **Luhn mod 10** check over the other nine — the same scheme every payment terminal implements. The printed format is unchanged and the space is still a billion per batch and type, so a 40,000-card order fills 0.004% of it.
>
> What it buys: a customer who mistypes one digit, or swaps two adjacent ones, is **told it is a typo** instead of being told we do not recognise their card. *"We don't recognise that number"* reads as an accusation when someone is holding a real card and simply fat-fingered it, and that is the single most common thing that will happen on the registration screen. It catches every single-digit error and every adjacent transposition except the 09/90 pair Luhn is known to miss.
>
> **The check digit shapes the message, never the verdict.** The register is the authority on whether a card exists, because a number keyed in through the import screen is a real card whether or not it carries our check digit.

**Batch numbers are 1–999 and never reused.** Reusing one is how batch 12 came to carry batch 11's serials, which is the worst data problem in the whole thirteen-batch history (§13.8). The panel offers the next free number and refuses one already recorded.

**Sub-batches have no format yet.** The history has 4.1, 5.1 and 5.2; `B14.1` would put a full stop in a card number. **[DECISION NEEDED]** — or simply take the next whole number, which costs nothing.

### 11.5 Duplicate conversion

**[CONFIRMED]** The mechanism that makes the collection finishable.

```
convert_duplicates(customer, target_character_id):
    require target_character_id NOT in customer.collection
    require target.roster_state = 'live'
    require customer.duplicate_credits >= duplicates_per_swap    # 3
    require customer under cap_swaps_per_phone_per_month

    customer.duplicate_credits -= duplicates_per_swap
    add target_character_id to customer.collection
    log to conversion_log
    re-evaluate milestones
```

A registration where `is_duplicate_for_customer = true` increments `duplicate_credits` by 1 — **in addition to** awarding its points. Duplicates do both jobs.

**Modelled outcome** (40,000 trials), re-run on 27 Aug 2026 at equal rarity alongside the original:

| Rule | Merlulu 1 in 30 (old)<br>Mean / Median | Merlulu 1 in 10 (current)<br>Mean / Median |
|---|---|---|
| No conversion | 39.8 / 32 | **29.4 / 27** |
| 8 duplicates → pick any | 21.7 / 24 | 20.6 / 20 |
| **3 duplicates → pick any** *(standard)* | 15.8 / 16 | **15.5 / 16** |
| 2 duplicates → pick any | 13.5 / 13 | 13.4 / 13 |

> **The standard rule barely moved, and that is the finding.** Dropping Merlulu from 1 in 30 to 1 in 10 changes the median at the standard three-duplicate rule **not at all** — 16 either way — because conversion already absorbs a missing character. Scarcity only bites in the *no conversion* row, which is the rule we do not use. **The chase is created by `duplicates_per_swap`, not by rarity.** That also means the swap rule is the lever to reach for if the Gang ever needs to feel harder, and rarity is not.

---

## 12. Data model

Additions to the existing schema. Existing tables and controls are unchanged.

### 12.1 `characters`

| Field | Type | Notes |
|---|---|---|
| `character_id` | string PK | `bhoppu`, `air_maxi` … — ids from `data/characters.json` |
| `character_name` | string | |
| `priority_rank` | int 1–10 | Importance in the fiction, from `CHARACTER-BIBLE.md` |
| `point_rank` | int 1–10 | **Drives the point skew. Defaults to `priority_rank`, overridable.** Merlulu: priority 6, point rank **2** |
| `is_standing_rare` | bool | **Nobody, since 27 Aug 2026.** Merlulu was the only one; the column stays for a future rare |
| `rarity_weight` | decimal | **All ten at 1.0** (= 1 in 10 each). Merlulu carried 0.3103 until 27 Aug 2026 |
| `is_print_ready` | bool | **Gates card generation.** All ten are `true` — Merlulu ships on the base design |
| `roster_state` | enum | **Gates website visibility, independently of print readiness.** `hidden` = absent · `locked` = silhouetted, uncollectable, does not count toward the Full Gang · `live`. **All ten are `live` at launch**; the states exist for introducing future characters |
| `pronouns` | enum | Picchi **she**, Merlulu **he** |
| `speaks` | bool | **Swirly is `false`.** Blocks any quoted line in generated copy |
| `description` | text | The printed card bio, from `data/characters.json`. **Not rewritten** |

### 12.1a `card_designs`

**[CONFIRMED]** A character has one or more card designs: the standard, plus occasion editions, poses and foils over time. **This table must exist from day one.** Retrofitting a variant system into a live `cards` table means re-keying every card ever issued, and it is the most expensive thing on this spec to add late.

| Field | Type | Notes |
|---|---|---|
| `design_id` | string PK | `bhoppu_standard`, `bhoppu_eid_2027`, `merlulu_first_ed` |
| `character_id` | FK | |
| `design_name` | string | "Bhoppu — Eid 2027" |
| `variant_type` | enum | `standard` / `occasion` / `pose` / `first_edition` / `foil` |
| `occasion_id` | FK nullable | Set for occasion editions |
| `art_path` | string | |
| `rarity_weight` | decimal | Share **within that character's** allocation |
| `point_band_override` | nullable | Normally null. Lets a rare foil carry a higher band without touching the character |
| `is_print_ready` | bool | |
| `is_retired` | bool | Never reprinted. **This is what makes a design genuinely scarce** |

`cards.design_id` replaces any direct art reference.

> ### The rule that keeps variants from breaking the game
>
> **Collection completion counts at CHARACTER level, never at design level.** Holding *any* Bhoppu completes Bhoppu.
>
> Occasion editions and other designs are a **second, optional collection layer** — "Bhoppu: 3 of 5 designs" — with no bearing on the Full Gang. If designs counted toward completion, sixteen cards would silently become fifty and the winnability argument in §2 collapses.

**Merlulu's pre-redesign card is already a variant.** Cards in circulation say "she"; future cards say "he", and the old ones are never reprinted. Log it as `merlulu_first_ed` with `is_retired = true` — a genuine First Edition acquired for free, and worth a content beat when the new one lands.

### 12.2 `occasions`

`occasion_id` (PK) · `occasion_name` ("Eid ul-Fitr 2027") · `starts_at` · `ends_at` · `edition_share` (proportion of character cards carrying the edition during the window) · `status` (upcoming / active / closed)

**No character is tied to an occasion.** [CONFIRMED] Which character carries an edition is chosen fresh each time, so the pairing stays a creative decision rather than a rule the schema enforces. An occasion may carry more than one character's edition.

When an occasion closes, every design carrying its `occasion_id` is set `is_retired = true` automatically.

### 12.3 `batches`

`batch_id` (PK) · **`batch_number`** (1–999, never reused — the number printed on every card in the order) · `occasion_id` (nullable) · `card_count` · `point_total` · `point_cap` · `assigned_outlet_id` · `serial_range_start` · `serial_range_end` · `status` (generated / printed / shipped / **activated**) · `activated_at` · `activated_by_staff_id` · **`duplicate_registration_allowed`** (§13.8)

**`batch_number` is not `batch_reference`.** The reference carries the month and the campaign — "Batch 5.1 GGxWUP Special (Jan 25)". The number is what goes on the card.

### 12.4 `cards` — added fields

| Field | Notes |
|---|---|
| `card_type` | `character` / `scratch` / `golden_waffle` |
| `batch_id` | |
| **`design_id`** | FK to `card_designs` |
| **`point_value`** | Assigned at generation, revealed at registration |
| **`distribution_type`** | `flagship` / `chefs_table` / `third_party` / `event` / `gift` — §11.6. Null for batches 1–12, which recorded no type, and derived from the sheet name for batch 13 |
| **`expires_at`** | **Scratch cards only.** A character card never expires and neither do its points — §3.3. Enforced by a constraint, not by convention |
| **`registration_count`** | Normally 0 or 1. Capped at 2, and only under §13.8 |
| `assigned_outlet_id` | For serial-range binding |
| `order_id` | Nullable. Set at packing for delivery orders |
| `registered_at`, `registered_by_customer_id` | |
| `status` | `generated → printed → shipped → distributed → registered → redeemed`, plus `expired` for a lapsed scratch card |

### 12.5 `customers`

`customer_id` (PK) · `phone_number` (unique) · `year_of_birth` · `is_minor` (derived) · `guardian_phone` · `guardian_consent_at` · `collection_state` (JSON, character level) · `design_state` (JSON, variant level — display only, never affects completion) · **`duplicate_credits`** (int) · `point_balance` (**derived from the ledger, never authoritative**) · `milestones_earned` · `first_registered_at` · `last_seen_at` · `review_flag`

### 12.6 `registrations`

`registration_id` (PK) · `card_id` · `customer_id` · `registered_at` · `channel` (web / staff_assisted) · `points_awarded` · `is_duplicate_for_customer` · `is_legacy`

### 12.7 `point_ledger` — the liability record

`entry_id` (PK) · `customer_id` · `delta` (signed int) · `reason` (`card_registration` / `milestone` / `golden_waffle` / `redemption` / `expiry` / `adjustment`) · `source_id` · `created_at` · `balance_after`

> **Append-only. Never updated, never deleted.** Balances are always derived by summing the ledger. This is what makes "we never devalue issued points" enforceable in code rather than a promise.

### 12.8 `conversion_log`

`conversion_id` (PK) · `customer_id` · `credits_spent` · `character_granted` · `created_at`

### 12.9 `milestones`

`milestone_id` (PK) · `name` · `type` (`collection_partial` / `collection_full` / `occasion_year`) · `threshold` · `point_reward` · `physical_reward_id` (nullable) · `is_repeatable` · `active`

Standard rows: Half the Gang (5, +50) · The Full Gang (10, +200, folder) · The Year's Four (4 occasion editions, +200, repeatable annually).

### 12.10 `merch_catalogue`

`sku_id` (PK) · `name` · `description` · `point_price` · `production_cost` · `mrp` · `vendor` · `status` (available / out_of_stock / retired) · `is_purchasable_with_cash` · `is_earned_only` · **`is_order_attachable`** (§6.2) · **`images[]`** (ordered, one primary) · **`sort_order`** · **`is_visible`**

- **`point_price` defaults to `production_cost` rounded to the nearest 5.** The panel pre-fills it on entry and allows an override — so adding a product is one quote, not a pricing decision.
- Collector's folder: `is_earned_only = true`, no `point_price`, no `mrp`.
- `point_price` is **versioned** — a price change never affects a PIN already issued.
- **A SKU with outstanding customer intent is never hard-deleted.** Retire it, or set `is_visible = false` to pull it from the shop without touching anyone's saved progress toward it.
- **Every field on this table is editable from the panel, images included.** See §15.1.

### 12.10a `merch_variants` — required, not optional

Almost every real item has variants the customer must choose between, and stock is held per variant, not per SKU.

`variant_id` (PK) · `sku_id` · `variant_name` · `variant_type` (`colour` / `size` / `design`) · `production_cost_override` (nullable) · `active`

| SKU | Variants |
|---|---|
| Notebook | 3 designs |
| Pop socket | **10 designs** |
| Sticker | page · character type 1 · character type 2 |
| Socks — kids | pink · teal *(different costs: 90 / 100)* |
| Socks — adult | pink · white |
| Cap | mesh · all-over print |
| T-shirt | pink · black — **× sizes** |
| Hoodie | pink · black — **× sizes** |

> **Apparel needs size, and size is where this goes wrong.** A redemption must reserve a specific *variant*, not a SKU. Reserving "T-shirt" and discovering at the counter that only XXL is left is the failure §6.1 exists to prevent. `merch_stock` is keyed on `variant_id`.

### 12.11 `merch_stock`

**`variant_id`** · **`location_id`** · `on_hand` · `reserved` · `reorder_threshold` (default 30%) · `updated_at`. `available = on_hand − reserved`. **Keyed on variant, never on SKU.**

**`location_id`, not `redemption_point_id`** — because §6.2 means a cloud kitchen holds attachable stock without ever being a counter. A location carries `is_redemption_point` and `is_attach_point` independently.

### 12.12 `merch_redemptions`

`redemption_id` (PK) · `customer_id` · `sku_id` · **`variant_id`** · `points_spent` · `pin` · `pin_expires_at` · **`fulfilment_method`** (`counter` / `order_attach`) · **`location_id`** · **`attached_order_id`** (nullable) · `stock_reserved` (bool) · `status` (pending / **awaiting_attach** / collected / expired / cancelled) · `collected_at` · `collected_by_staff_id`

- `counter` reservations hold for `pin_expiry_days` — 14.
- **`order_attach` reservations hold for `pin_expiry_days_order_attach` — 60.** You cannot require someone to place an order inside a fortnight.
- **On lapse, stock is released and the points go back to the ledger**, reason `reservation_lapsed`. Nothing a customer holds is ever taken away, and that includes a reward they have not managed to collect yet.

### 12.13 `pos_reconciliation`

`period` · `outlet_id` · `channel` (dine_in / takeaway / delivery) · `qualifying_txn_count` · `cards_issued_count` · `cards_registered_count` · `issue_rate` · `variance` · `flagged` (bool)

### 12.14 `trades` — build last

`trade_id` (PK) · `card_id` · `from_customer_id` · `to_customer_id` · `traded_at` · `status`. **Specified now so the schema does not need retrofitting.** Deprioritised.

### 12.15 One field to remove

The existing `rewards.is_discount` flag is always "No" and therefore controls nothing. Replace it with a **validation rule that rejects reward names and POS strings containing the banned words in §8** — that is where the real control belongs.

---

## 13. Rules and invariants

### 13.1 Registration validation

In order. Any failure stops the process.

```
1.  Card serial exists                          else "We don't recognise that number"
2.  Card's batch status = 'activated'           else "That card isn't in circulation yet"
3.  Card not already registered                 else "Someone's already claimed this one"
4.  Customer account exists and is active       else register / confirm guardian
5.  Customer under daily cap                    else queue for review, friendly hold
6.  Customer under monthly cap                  else queue for review
7.  If is_legacy and legacy pool exhausted      → collection credit, 0 points
8.  Award points, write ledger entry
9.  If character already held                   → duplicate_credits += 1
    else                                        → add to collection_state
10. Always                                      → add design to design_state
11. Re-evaluate milestones (see 13.2)
```

**Step 7:** a legacy card is never *refused*. Once the pool is empty it still counts toward the collection; it just stops minting points.

**Step 9:** a duplicate awards **both** its points and a conversion credit.

### 13.2 Milestone evaluation

```
held = count(collection_state where roster_state = 'live')

if held >= 5  and 'half_gang' not earned      → award +50
if held == count(all live characters)          → award +200 + folder
if all of this year's occasion editions held   → award +200  (repeatable per year)
```

**Uses the live roster, not a hardcoded 10.** All ten are `live` at launch, so the Full Gang target is ten from day one. The indirection exists for future characters: a `locked` character is displayed but excluded from the target, and when one goes live the target grows — but **a milestone already awarded is never revoked** (invariant 3).

### 13.3 Hard invariants

The engine must enforce these, not merely report on them.

| # | Invariant |
|---|---|
| **1** | A card can be registered exactly once, ever — **except under §13.8**, where a serial printed twice may register twice, by two different people, and never more |
| **2** | `sum(point_ledger.delta)` for a customer **always equals** their balance. Balances are never written directly |
| **3** | A ledger entry is never updated or deleted; a milestone once awarded is never revoked |
| **4** | `batch.point_total ≤ batch.point_cap` at generation, where the cap is pro-rated to the size of the order (§11.4) |
| **5** | A card in a non-activated batch cannot register |
| **6** | `merch_stock.reserved ≤ on_hand` at all times |
| **7** | A redemption cannot be created without a successful stock reservation |
| **8** | `points_spent` equals the SKU's point price **at the moment of redemption**, not the current one |
| **9** | A duplicate conversion cannot grant a character the customer already holds, or one that is not `live` |
| **10** | No card record may have a sale price field. **Cards are never sold** |
| **11** | `cards_registered ≤ cards_issued` per outlet per period |
| **12** | ⭐ `cards_registered ≤ qualifying_txn_count` per outlet per period |
| **13** | An entitlement is consumed exactly once |
| **14** | An entitlement never expires |
| **15** | **A scratch card may carry an expiry; a character card may not.** Enforced by a constraint, because §3.3 is a promise to customers |

### 13.8 The duplicate serials — batches 11 and 12

**[CONFIRMED 26 Aug 2026 — Kaushik could not confirm, so the engine assumes the worse case]**

`Batch 12 (Jul 26)` contains **the same 33,500 serials** as `Batch 11 (May 26)` — identical values, identical `MAY-` prefix — while its summary sheet reads "SURPRISE CARD BATCH-12 JULY". It is the only collision in 340,064 cells across all thirteen workbooks, so it is not a systemic numbering problem. Ops cannot confirm whether batch 12 was a filing error or was genuinely printed with batch 11's numbers.

**If it was printed, two customers are holding the same number.** Under invariant 1 as originally written, the first to register wins and the second is told *"someone's already claimed this one"* while holding a genuine card. That is the wrong answer to give someone whose card is real.

So the invariant is relaxed **by exactly one, in one place, under four conditions that must all hold:**

| | |
|---|---|
| `unique (card_id, customer_id)` | One person can never register a serial twice |
| `cards.registration_count ≤ 2` | No serial can ever register more than twice |
| `batches.duplicate_registration_allowed` | And only on a batch flagged as printed twice |
| `allow_duplicate_serial_registration` | And only while Ops leave the master switch on |

The first two are **schema constraints, not function logic**, so the property that actually matters — nobody can farm points by re-registering a card — holds even if the registration function is wrong.

**Every second registration queues for review.** Not because it is suspicious, but because **the count of them is the only evidence that will ever exist** about how many duplicate physical cards actually reached customers. The workbooks cannot answer it; the register can.

**The master switch is in Configuration**, so it can be turned off everywhere at once without anyone hunting for affected batches under pressure.

### 13.4 ⭐ POS reconciliation — the primary integrity control

The POS already knows how many qualifying transactions happened. That is how many cards should exist. Comparing the two closes the largest remaining hole **without adding a single step at the counter.**

```
Per outlet, per channel, per period:

  qualifying_txn_count    from POS      — transactions ≥ BDT 500 (≥ 480 subtotal on portals)
  cards_issued_count      from engine   — cards in activated batches assigned to that outlet
  cards_registered_count  from engine   — registrations against that outlet's serial ranges

  issue_rate = cards_issued_count / qualifying_txn_count
  variance   = qualifying_txn_count - cards_issued_count
```

| Check | Meaning | Action |
|---|---|---|
| `cards_registered > qualifying_txn_count` | **More cards registered than customers earned.** Arithmetic proof of farming | **Flag, freeze the serial range, investigate** |
| `cards_registered > cards_issued` | Registrations against cards never handed out | Flag |
| `issue_rate` well below 1.0 | **Staff are not handing cards out** | Management issue, not fraud |
| `issue_rate` above 1.0 | Over-issuing | Flag |

> ⭐ **`issue_rate` should be reported as a per-outlet staff KPI.** It closes the fraud hole *and* it fixes the separate problem that staff currently have no reason to promote the programme — it gives them a number they are measured on.

**One honest limitation.** This is a *count* reconciliation, not a card-level one. If a staff member farms 20 cards while the outlet also fails to hand 20 to real customers, the totals net to zero and the variance is invisible. **POS reconciliation is therefore the primary detection, and the anomaly rules below catch what nets out.**

### 13.5 Anomaly detection

Run continuously. Every hit **queues for review; nothing is auto-deleted.**

| Signal | Threshold |
|---|---|
| Sequential serials registering together | 3+ consecutive serials, same account, within an hour |
| Many cards, few phone numbers | > 20 cards across < 3 numbers in a day at one outlet |
| Registration clustering | > 10 registrations from one outlet's range within 5 minutes |
| Geographic mismatch | Card registering from an outlet's range with no order history there |
| Staff account correlation | Registrations concentrated in one staff member's activated batches |
| Conversion velocity | > 5 duplicate swaps per phone per month |
| Redemption velocity | > 2 redemptions per phone per day |

### 13.6 Delivery cards

**[CONFIRMED]** The card serial is **scanned or entered against the `order_id` when the bag is sealed.** About three seconds per order, and it does three things: proves the card went out, ties the serial to a real customer order, and lets a "my card was missing" complaint be answered from the record instead of argued about.

POS reconciliation runs per channel, so the delivery issue rate is visible separately from in-store.

### 13.7 Batch activation

An outlet marks a box **activated** when it opens it — **one tap in the staff app, once per box, not per card.** Cards in a non-activated box cannot register at all, and the activating staff member is on record.

This is the deliberate middle path. Activating each card at the till would be stronger, but it adds a step at the counter during the busiest hours — the same friction that already stops staff promoting the programme.

---

## 14. Configuration

**[CONFIRMED]** Everything here is editable from the admin panel. Every change is logged with who made it and when.

| Parameter | Standard | Safe range | Who changes it |
|---|---|---|---|
| `earning_threshold_bdt` | 500 | 400–800 | Jawat |
| `batch_size` | 297 | 100–500 | Ops |
| `scratch_ratio` | 0.0909 | 0.05–0.15 | Jawat |
| `golden_waffle_rate` | **0.001** (1 in 1,000) | 0.0002–0.005 | Jawat |
| `golden_waffle_points` | **100** | 50–500 | Jawat |
| `point_band` | **5–18** | 1–50 | Jawat |
| `tier_skew_strength` | **1.0** | 0–1.5 (hard cap 2.5) | Jawat |
| `merlulu_rarity_weight` | **1.0** (1 in 10) | 0.1–1.0 | Marketing |
| **`duplicates_per_swap`** | **3** | 2–8 | Jawat |
| `milestone_half_gang` | 50 | 25–100 | Marketing |
| `milestone_full_gang` | 200 | 100–500 | Marketing |
| `milestone_occasion_year` | 200 | 100–500 | Marketing |
| `occasion_edition_share` | 0.30 | 0.1–0.6 | Marketing |
| `occasions_per_year` | 4 | 2–6 | Marketing |
| `batch_point_cap` | **3300** | derived from the ceiling | Finance |
| `point_to_cost_bdt` | **1.00** | 0.50–2.00 | Finance |
| `card_cost_character_bdt` | **3.00** | actual — cover included | Ops |
| `card_cost_scratch_bdt` | **3.40** | actual — cover included | Ops |
| **`scratch_cogs_pct`** | **38** *(of selling price)* | 25–50 | Finance |
| **`scratch_redemption_planning_pct`** | **60** | 40–85 | Finance |
| `giveaway_ceiling_pct` *(points + scratch)* | **3.5** | 1.5–5.0 | Jawat |
| `printing_ceiling_pct` | **0.65** | 0.4–1.5 | Finance |
| **`all_in_ceiling_pct`** | **4.15** | derived | Finance |
| `legacy_point_pool` | **50000** | 0–200,000 | Jawat |
| `point_inactivity_expiry_months` | 12 | 6–24 | Jawat |
| `point_expiry_notice_days` | 30 | **never below 30** | fixed floor |
| `pin_expiry_days` *(counter)* | 14 | 3–30 | Ops |
| **`pin_expiry_days_order_attach`** | **60** | 14–90 | Ops |
| **`scratch_validity_days`** | **180** | 30–730 | Ops |
| **`allow_duplicate_serial_registration`** | **On** | on / off | Jawat |
| **`serial_check_digit_required`** | **On** | on / off | Jawat |
| **`scratch_cogs_pct`** | **38** *(of selling price)* | 25–50 | Finance |
| **`scratch_redemption_planning_pct`** | **60** | 40–85 | Finance |
| **`card_cost_character_bdt`** | **3.00** | actual — cover included | Ops |
| **`card_cost_scratch_bdt`** | **3.40** | actual — cover included | Ops |
| `minor_age_threshold` | 16 | 13–18 | Legal |
| `cap_cards_per_phone_per_day` | 10 | 3–50 | Ops |
| `cap_cards_per_phone_per_month` | 60 | 20–200 | Ops |
| `cap_swaps_per_phone_per_month` | 5 | 2–15 | Ops |
| `cap_cards_per_transaction` | 10 | 3–20 | Ops |
| `cap_redemptions_per_phone_per_day` | 2 | 1–5 | Ops |
| `stock_reorder_threshold_pct` | 30 | 10–50 | Ops |

**Two things are not configurable, ever:**

- **Cards may never be sold.** No price field exists for a card, in any table.
- **Issued point balances may never be reduced or re-priced.**

---

## 15. Admin panel screens

| Screen | Does |
|---|---|
| **Dashboard** | Cards issued · registration rate · point burn · **outstanding liability** · giveaway and all-in spend as % of qualifying revenue against the **3.5% / 4.15%** ceilings |
| **Characters** | Priority rank, **point rank**, rarity weight, print-ready, **roster state (hidden/locked/live)**, `speaks`, pronouns |
| **Card designs** | **Add a pose, occasion edition or foil for any character.** Set rarity within that character, upload art, mark print-ready, retire. **New cards are a data change, not a code change** |
| **Occasions** | Create an occasion, set the window and edition share, attach designs. Closing it auto-retires its designs |
| **Batches** | **Generate a print order** — batch number, then per distribution type a character count and a quantity for each scratch product. **Previews before it commits**: per-character counts, scratch share against 9.09%, point total against the ceiling, values trimmed. **Exports the printer's workbook** — Summary, Character Card, Scratch Card, laid out exactly as the previous thirteen. **Imports a batch from the same layout.** Assign to outlets, track activation |
| **Milestones** | Thresholds, point rewards, physical rewards, repeatability |
| **Merchandise** | Add/edit/retire SKUs and variants · point price, production cost, MRP · **upload, replace and reorder product images** · name, description, sort order, visibility · per-location stock, reorder alerts |
| **Redemptions** | Pending PINs, reservations, collection confirmation, expiries · **order-attach queue** — which rewards are waiting to ride along with an order |
| **Customers** | Collection state, duplicate credits, ledger, caps, review flags, guardian consent |
| **POS reconciliation** | Per outlet, per channel: qualifying transactions vs cards issued vs registered. **Issue rate league table** |
| **Review queue** | Anomaly hits and cap breaches awaiting a human decision |
| **Configuration** | Everything in §14, with change history |
| **Reports** | §16 |

### 15.1 ⭐ The no-deploy rule

**[CONFIRMED 26 Aug 2026]** Everything a customer sees is **data, not code.** Nothing in the list below may require a developer, a code change or a release.

| Editable from the panel |
|---|
| Add a product · edit it · pull it from the shop · retire it |
| Point price · production cost · shop price — each independently of the others |
| Product name, description, sort order, and whether it is listed at all |
| **Product images** — upload, replace, reorder, set the primary |
| Variants, and stock per variant per location |
| Characters, card designs, occasions, milestones |
| Every parameter in §14 |

Three consequences for whoever builds this:

1. **Images are uploads, not repository files.** A product photo goes to object storage through the panel and is referenced by URL. If adding a new product needs a code change to show its picture, the panel is not finished.
2. **Prices are expected to move.** The §5.1 column is a launch position, not a decision — so the price field must be first-class, versioned, and safe to change while customers are mid-save (invariant 8: a PIN already issued keeps its price).
3. **Editable is not the same as untraceable.** Every price and configuration change is logged with who made it and when.

---

## 16. Reports

| Report | Definition | Why it exists |
|---|---|---|
| **Scratch redemption rate** | Redeemed ÷ scratch distributed, **same period** | The real redemption number. Never divide by all cards |
| **Character registration rate** | Registered ÷ character cards distributed | The headline number. Today it is 0% |
| **Point burn rate** | Points spent ÷ points issued | Benchmark ~50%. Drives the liability provision |
| **Outstanding liability** | Unspent points × cost per point × expected burn | **Belongs on the balance sheet** |
| **First-redemption time** | Median days, first registration → first redemption | The habit-formation number. The 25-point item exists to move it |
| **Collection completion rate** | Customers reaching 5/10 and 10/10 | Is the game winnable? |
| **Median cards to completion** | Actual, against the ~16 model | Validates or kills the conversion rate |
| **Conversion usage** | Swaps per completing customer | If it is near zero, `duplicates_per_swap` is too high |
| ⭐ **Incremental lift** | Visit frequency and spend of registered collectors **vs a matched non-registered group** | **The one that proves the programme works** |
| **Occasion edition capture** | Share of collectors holding each edition | Are the four moments landing? |
| **Card issue rate** | Per outlet, per channel | Fraud signal *and* staff KPI |
| **Cards per customer** | Distribution, not average | Finds superfans, flags farming |
| **Review queue volume** | Open flags by type and age | Fraud early warning |

> **The starred report is the business case. Build it first, and build the control group with it.** A redemption rate on its own only tells you people like presents. What matters is whether collectors visit more often than comparable customers who aren't collecting.

**Retire the "3–4% redemption rate."** It divides redemptions by every card printed, including character cards that were never redeemable by design. It measures nothing and makes a healthy programme look broken.

---
---

# PART C — DELIVERY

---

## 17. Rollout

| Phase | Ship | Needs |
|---|---|---|
| **0** | ⭐ **Retro-activation.** Launch accounts and the merch shop. Let the **~38,556 cards already in customers' hands** register against the numbers already printed on them | Account build. **No card redesign, no reprint** |
| **1** | Duplicate conversion, milestones, the collection scoreboard | Phase 0 |
| **2** | Redemption Points live — PIN fulfilment, stock reservation | Merch stock |
| **2b** | **Order-attach fulfilment** (§6.2) — small items ride along with a paid order | Phase 2 + the bag-seal step |
| **3** | POS reconciliation and the issue-rate report | POS integration |
| **4** | Batch activation, serial-range binding, anomaly detection | Engine |
| **5** | First occasion edition | Artwork + print run |
| **6** | Golden Waffle seeded into the print run; odds published | Print run |
| **7** | Scratch redemption capture moved out of WhatsApp into the staff app | Engine |
| **8 · later** | Card transfer between accounts | Registration volume |

> **Phase 0 is the highest-return action available.** It builds the customer database and the scoreboard **before** anything is reprinted, tests the whole flow at real volume, and gives us a launch story that costs nothing: *the cards you already have just started counting.*

### 17.1 The legacy pool

**[CONFIRMED]** Retro-activation carries a liability. If every one of the ~35,000 legacy character cards were registered at the standard band, it would mint about **BDT 405,000** of points at once. Bounded as follows:

| | |
|---|---|
| Legacy point pool | **50,000 points**, set in the admin panel |
| Released | First come, first served |
| While the pool has points | Legacy card → collection credit **and** points |
| Once it is empty | Legacy card → **collection credit, no points** |
| **Maximum exposure** | **BDT 50,000, known in advance** |

**Nobody's collection is ever refused,** and the pool creates honest urgency at launch that costs nothing to communicate.

### 17.2 A note on the scratch redemption chain

**[CONFIRMED]** Scratch redemption today is ten POS steps, then hole-punch, photograph, send to a WhatsApp group, staple to bill and KOT, ship to HQ, plus a CCTV check. That is a well-designed fraud control and every part of it should be kept.

But it is also why staff will never proactively encourage redemption during the busiest hours. **The WhatsApp group is the weakest link** — unsearchable, unstructured, and not linked to the POS record. Moving that one step into the staff app, so the photo attaches automatically to the redemption record and HQ reconciles against the system instead of a chat thread, is the highest-value operational fix available. Everything else stays exactly as it is.

---

## 18. Open items

### Needs a decision

| # | Item | Owner |
|---|---|---|
| 1 | **Item-level COGS** for the scratch reward mix. Budgeted at a flat 38% of selling price, which is enough to plan against — but the real numbers are still worth an estimated 15–25% off reward cost with nothing the customer can see (§7.2) | Finance |
| 2 | **Collector's folder** — does not exist and has no quote. Print job, should go to Bijoy at Asha Printers | Ops |
| 3 | **Redemption Point list** — footfall, storage, *and* coverage against the cloud-kitchen catchments (§6.2) | Ops |
| 4 | **Merchandise ownership** — who holds stock, who reorders, working capital. Now also: which locations hold order-attach stock | Ops |
| 5 | **Occasion editions** — which character carries each of the four. Not fixed, chosen per occasion. **Artwork: Junaid** | Jawat + Junaid |
| 6 | **Surprise Card Box** — the outer shipping carton is unpriced on Bijoy's sheet. A rounding item, not a budget line (§7.3). Worth getting on the next quote | Ops / Bijoy |
| 7 | **Sub-batch numbering** — the history has 4.1, 5.1 and 5.2, and `B14.1` would put a full stop in a card number (§11.6). Either a format, or a standing rule to take the next whole number | Ops |

### Closed

| Item | |
|---|---|
| ~~Merlulu's rarity contradicting his print run~~ | ✅ **27 Aug 2026, Jawat.** The print run carries him at the **same quantity as everyone else**, so `rarity_weight` is **1.0**, he is **1 in 10**, and `is_standing_rare` is off. §3.1's standing-rare pillar is deleted, not softened. **The earlier estimate that this would drop the Full Gang from ~16 cards to ~13 was wrong** — re-modelled at 40,000 trials the standard three-duplicate rule gives a median of **16 either way** (§11.5). Conversion, not scarcity, is what makes the Gang finishable |
| ~~`batch_point_cap` binding too often~~ | ✅ **27 Aug 2026.** Raised **3,160 → 3,300**, as this item proposed. It stopped being optional: equal-weight Merlulu lifts expected mint to ~3,164, *above* the old cap, which trimmed **51.6%** of measured batches against 2.4% at 3,300. Per §7.5 rule 2, the response to a ceiling the design breaches is to raise the ceiling. **Finance owns the number and can move it back from the panel** — but the Merlulu weight must move back with it |
| ~~Merchandise packaging~~ | ✅ **24 Aug 2026.** Every item ships in its box; costs are inside the point prices in §5.1. The gift bag is excluded from the catalogue |
| ~~Surprise Card Cover unpriced~~ | ✅ **26 Aug 2026.** The cover is inside the BDT 3.00 / 3.40 card price. **Printing is a total, not a floor** |
| ~~Shop prices~~ | ✅ **26 Aug 2026.** Launch at the ~2.6× column in §5.1 and adjust from the panel thereafter (§15.1). Not a fixed decision — a starting position |
| ~~Item-level COGS blocking the budget~~ | ✅ **26 Aug 2026.** Budgeting at a flat 38% of selling price. Giveaway ceiling reset to 3.5% as a consequence (§7.5). The optimisation stays open as item 1 |
| ~~Delivery-only redemption~~ | ✅ **26 Aug 2026.** Order-attach (§6.2). Cash-on-delivery and points-for-delivery both considered and rejected |
| ~~Merlulu's artwork~~ | ✅ **26 Aug 2026.** Shipping on the base design. All ten live from launch, **the Full Gang is ten from day one**, nothing on the critical path |
| ~~The 300 Matcha-launch cards of unknown type~~ | ✅ **26 Aug 2026, Jawat.** All 300 are **scratch cards** and all carry the new **Matcha** product. Four sheets named only by channel; the parser refused to guess and the answer resolved it |
| ~~Batch 9's unnamed column~~ | ✅ **26 Aug 2026, Salman via Jawat.** 1,000 serials under a blank heading, believed to be socks but unconfirmed — so the reward is recorded as **"Socks Maybe"**, which says out loud that we do not know. Ops report the batch out of use, so those cards import **already lapsed**: no liability, and nobody can be handed the wrong thing on the strength of a guess |
| ~~Batch 12 duplicating batch 11~~ | ✅ **26 Aug 2026.** Kaushik could not confirm it either way, so the engine assumes the worse case and allows a **second registration on those serials only**, by a different person, with a master switch to stop it everywhere. §13.8 |
| ~~The card number format~~ | ✅ **26 Aug 2026, Jawat.** `B14F-7201647537` from batch 14 onward, five distribution types. §11.6 |

### Needs someone outside the company

**7 · Legal review.** Points change what this programme legally is. Counsel should be asked:

> - ✅ **ANSWERED — Jawat, 24 Aug 2026: a points balance redeemable for merchandise does NOT constitute regulated stored value or e-money under Bangladesh law.** No registration, reporting or ring-fencing obligation follows. *(Bangladesh only. Singapore's Payment Services Act treats stored-value facilities separately and must be answered independently before any Singapore launch. And "not regulated" does not mean "not a liability" — unspent points remain an accounting provision, per §16.)*
> - Our position is that the programme falls outside loot-box and gambling rules because **cards are never sold and no chance is ever purchasable** (§9). Confirm this holds in Bangladesh, and flag where it would not in Singapore, UAE, Thailand or Indonesia.
> - Is the guardian-consent flow in §9.1 sufficient for under-16 participation, including holding a minor's phone number and a guardian's?
> - Are the promotional terms compliant — odds disclosure, expiry, the anti-scalping caps, and refusal or review of a flagged account?
> - Does any of this conflict with Foodpanda or Pathao platform policy where cards are issued on delivery orders?
> - Confirm that publishing the odds (§19) creates no additional obligation we would not otherwise have.

**8 · Singapore.** Bangladesh launches first. CQ @ Clarke Quay is a single site and cannot produce meaningful data on its own. Before any Singapore launch: an SGD earning threshold, the SG price book for liability, an SG print run and customs, an SG merchandise catalogue, and a separate legal review. **Bangladesh CTAs must never appear on Singapore content.**

**9 · Franchising, from ~Aug 2027.** **[RECOMMENDED] principle: the entity that issued the card funds the reward.** Every card carries its issuing outlet, so a franchisee fulfilling a reward against a company-issued card is reimbursed at production cost, netted monthly between entities. The same applies to the Chef's Table price-book difference, which stops being an internal transfer the moment outlets are separately owned. *Owner: Jawat + finance.*

### Housekeeping

- `brand/CHARACTER-BIBLE.md` is still marked DRAFT. Everything in §3 depends on it.
- `brand/BRAND.md` records "~27,000 character + ~3,500 scratch per batch" — those figures describe a print run of about 100 batches, not a batch. Correct it so `batch_id` means one thing across the business.
- `CLAUDE.md` §10 says character card art exists for 6 of 9. **All ten exist.** Correct it.
- **`CLAUDE.md` §5 needs a carve-out** for the colour-in card back: line art derived from supplied character artwork is permitted **for the Surprise Card back only**, must be produced by the original character artist, must be approved by Jawat, and is then stored in `assets/` as a supplied asset in its own right. Every other derivative stays banned, and AI generation of any character remains banned absolutely.

---

## 19. The evidence this rests on

Researched 24 August 2026.

**Collecting-by-code programmes are a mature, proven pattern.** Enter a unique code from a pack into an account, accumulate points, redeem for branded merchandise. The standard controls in that category — unique single-use codes, per-member usage limits, granular tracking — are the ones specified in §13.

**In-person redemption genuinely drives visits.** Members returning to collect a reward buy other things while they are there; the industry calls it the redemption halo. One measured convenience chain got **one extra visit per member per month** from it. Brands with physical locations also see *higher* redemption than online-only ones, because staff can explain it.

**Rewards must be reachable in weeks, not months.** This is stated explicitly as a condition for in-person redemption producing incremental visits, and it is why the merchandise ladder starts at 10 points — about **one card** — rather than making a customer wait for the full collection.

**Planning benchmarks used in §7:**

| | |
|---|---|
| Redeemers vs non-redeemers | **Redeemers spend 3.1×** |
| Healthy programme | 20–30% of active members redeem in a period |
| Average breakage | **~50% of rewards go unclaimed** |
| The KPI that matters | Incremental lift against a **matched** non-member group |

**The compliance position.** Every country that has restricted this kind of mechanic has restricted **paid** randomness. Belgium and the Netherlands ban paid loot boxes as gambling. PEGI applies a minimum 16 rating to paid random items. Brazil's 2025 law prohibits selling them to under-18s from March 2026. The US FTC required parental consent for under-16 purchases and accurate odds disclosure. The EU's Digital Fairness Act is expected to go further. **Our cards come free with a purchase the customer already chose to make and are never sold, which places us outside all of it.**

**[RECOMMENDED] Publish the odds anyway.** Scratch 9.09% · every character ~1 in 10 · Golden Waffle ~1 in 1,000. Doing it voluntarily costs nothing, builds trust, makes the chase legible, is good content in itself, and puts us ahead of where regulation is clearly heading.

**A warning worth taking seriously.** **McDonald's Japan ended a Pokémon Happy Meal promotion early in August 2025** because customers bought meals purely for the cards and discarded the food. Resale and hoarding drove it. They now cap purchases per group and block delivery apps for the first three days of a card promotion. Our BDT 500 threshold makes hoarding far more expensive than a Happy Meal — but a limited edition that stops printing is exactly the mechanic that produces this behaviour, which is why the caps in §9.2 are mandatory and not advisory.

**Sources:** [Open Loyalty](https://www.openloyalty.io/product/code-scanning) · [Rivo](https://www.rivo.io/blog/points-program-redemption-rate) · [Voucherify](https://www.voucherify.io/glossary/loyalty-breakage) · [Exchange Solutions](https://exchangesolutions.com/glossary/redemption/) · [Paytronix](https://www.paytronix.com/blog/effectiveness-of-loyalty-programs) · [Restaurant Business](https://www.restaurantbusinessonline.com/marketing/demand-mcdonalds-pokemon-cards-goes-through-roof) · [Attack of the Fanboy](https://attackofthefanboy.com/news/mcdonalds-caps-new-pokemon-happy-meal-at-six-per-group-and-blocks-delivery-apps-for-three-days-after-past-promo-sold-out-in-24-hours/) · [Yahoo](https://www.yahoo.com/news/articles/mcdonalds-ends-pokemon-promo-early-173000472.html) · [Promise Legal](https://blog.promise.legal/loot-box-laws-game-developers/) · [Lexology](https://www.lexology.com/library/detail.aspx?g=6779705d-3000-4825-92c4-7c5b8a901ada)

---

## Appendix — the numbers on one page

| | |
|---|---|
| Earning threshold | **BDT 500** per transaction (480 subtotal on delivery portals) |
| Batch | **297 cards** — 27 scratch, the rest character |
| **Card number** | **`B14F-7201647537`** from batch 14 — batch, type letter (F·C·3·E·G), ten digits, the last a Luhn check |
| Characters | **All 10, always in circulation** |
| Merlulu | **~1 in 10 cards** · rarity weight **1.0** · point rank **2** · no longer a standing rare |
| Golden Waffle | **~1 in 1,000 cards** · **+100 points** |
| Point band | **5–18**, weighted by character, average per card **11.71** |
| Skew strength | **1.0** (0–1.5, hard cap 2.5) |
| **Duplicate swap** | **3 duplicates → any character you're missing** |
| To complete all 10 | **~16 cards · ~BDT 7,900 · ~4 months weekly** |
| Milestones | 5/10 = **+50** · 10/10 = **+200** + folder · all four editions = **+200**/year |
| Occasions | **4 a year** — Pohela Boishakh · both Eids · Victory Day |
| 1 point | **BDT 1.00 production cost.** An item's point price **is** its production cost in taka |
| Shop price | ~**2.6× production cost** [recommended] |
| Batch point cap | **3,300** per 297 cards — **pro-rated to the order**, enforced by the generator |
| What expires | **Nothing a customer holds**, and no points, ever. A scratch card's food reward lapses at 180 days — the one real expiry |
| Card printing | **BDT 3.00 character · BDT 3.40 scratch, cover included** = BDT 902/batch = **0.61%** |
| **Giveaway ceiling** (points + scratch) | **3.5% of qualifying revenue** |
| **All-in programme ceiling** | **4.15%** |
| Realistic all-in cost | **1.94%** of qualifying revenue ≈ **BDT 94,000/month** |
| Legacy pool | **50,000 points** — maximum exposure BDT 50,000 |
| Cheapest merch item | **Sticker, 10 points (~1 card)** |
| Redemption | **In person at a Redemption Point** · small items may **ride along with a paid order** (§6.2) |
| Scratch redemption rate | 40–81%; **plan at 60%** |
| Scratch reward value per batch | BDT 5,935 menu · **BDT 2,255 at cost** (average BDT 220 menu) |
| Food COGS | **38% of selling price** — flat working figure |
| Benchmark: redeemers vs non | **3.1× spend** |
| Benchmark: breakage | ~50% |
| Possession proof | **The sealed yellow pack** |
| Primary integrity control | **POS reconciliation** — qualifying transactions vs cards registered |
| Value language | Never "free", never "discount", never state what a gift is worth |
| **The line we do not cross** | **No card is ever sold. No chance is ever purchasable** |
