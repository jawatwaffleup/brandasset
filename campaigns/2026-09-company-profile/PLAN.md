# WaffleUp Company Profile 2026 — production plan

**Status:** planning. Nothing shot, nothing written, nothing designed.
**Supersedes:** `WaffleUp Profile - Edited 7th Feb 2024.pdf` (20 pages, 16:9 landscape).
**Owner:** Jawat · **Drafted:** 1 Sep 2026

---

## 1. The strategic read

I extracted and read the whole 2024 profile. It is a decent document with four structural problems, and none of them are design problems.

**a) It describes a business that no longer exists.** Every hard number is 2023-vintage and at least three are now wrong: *12 outlets* (now 15 trading sites across four models), *3 cloud kitchens* (2 live), *"24 months since inception"* (now 57), *"outlets in UAE and Egypt soon to be launched"* (Egypt is gone from the plan entirely; the live pipeline is Dubai, Thailand, Indonesia). If a franchise prospect or a landlord reads the 2024 deck and then talks to us, the Egypt line alone costs credibility. **The old profile is now a liability document, not just a stale one.**

**b) It contains no photograph of the actual business.** Not one outlet. Not one cart. Not one kitchen. Not one team member. Not one customer. The entire visual load is carried by studio product shots and character art. For a consumer post that is fine. For a document whose readers are franchise partners, investors, mall leasing managers, corporate clients and journalists, the missing proof *is* the document. **This is the single biggest gap and the reason this project starts with a shoot.**

**c) It is three documents wearing one cover.** Franchise-pitch content (outlet models, impact numbers), consumer content (Jester product copy — *RIP*, *party with your taste buds*), and employer-brand content (Culture) sit side by side with no hierarchy. Nobody is fully served.

**d) It leaves the strongest asset on the floor.** The Waffle Up Gang gets a single title page — no characters shown, no explanation. The Surprise Card does not appear at all. Ten pieces of owned character IP plus a running loyalty programme with 38,556 cards distributed is the part of WaffleUp a competitor cannot copy by buying a waffle iron. **In a business document, the owned IP and the reward loop are the differentiator that isn't a waffle.**

### What I am proposing

Rebuild it as a **business-first profile** — a document that makes WaffleUp look like a company you would put a lease, a franchise fee or an investment behind. Consumer storytelling already has social; the profile has a different job. The brand voice stays Jester in the product pages and goes plain-and-confident everywhere a number or a claim appears.

Target: **32–40 pages, 16:9 landscape**, matching the old profile's format and — usefully — the format the `brand-guidelines/build.py` pipeline already renders at 1440×810. That pipeline produced the 63-page Brand Guidelines PDF from HTML. It is the obvious build route here: version-controlled, reproducible, and the numbers can be corrected without reopening a design file.

> **Decided by Jawat, 1 Sep 2026: business-first.** Primary reader is franchise, investor, landlord and corporate B2B. The consumer story stays on social. See §6 for what that settles in the shoot.

---

## 2. What carries over, what dies, what is new

| From the 2024 profile | Verdict |
|---|---|
| Cover · one-line positioning | Keep, restate |
| **Our story** (Salman, the US waffle truck, sets of four) | **Keep almost verbatim — it is the best page in the deck** |
| First outlet — Banani, 16 Dec 2021 | Keep, upgrade with a real photograph of the site |
| Impact paragraph | **Rewrite.** Contains the Egypt/UAE error |
| In Numbers (12 / 8,000 / 100+ / 2 / 38,000 / 180mln) | **Rewrite with 2026 figures.** See the revenue warning in `GATHER.md` §2 |
| Purpose · Mission · Vision (three R's) | Keep. Mission wording needs one decision — see §5 |
| Value pillars | **Resolve first.** Two source documents disagree — see §5 |
| Product list (2 pages, partial range) | **Rebuild.** Old list is missing Tri-Chocolate, Kunaffle™, Mad Mango, the whole beverage range and Zero-Guilt |
| "the waffle up gang" title page | **Expand to a real section.** Ten characters, named, with the IP story |
| Outlet models ×4 | **Keep the structure, rebuild with real photography.** Currently text-only |
| Making headlines (5 raw URLs) | **Rebuild.** Raw URLs on a page is not a press section — needs clippings, mastheads, dates |
| Clients and Partners (logo grid) | **Rebuild.** Needs a verified list and permission to use the marks |
| The word grid (Unique Shape / Hard to Forget / …) | **Cut or rebuild.** Nine adjectives with no proof behind any of them |
| Culture | Keep the copy, add faces. Currently a culture page with no people on it |
| Best Dessert Shop — Dhaka North City Corporation | Keep, plus the two awards it is missing |
| Contact page | Keep, fix (the handle renders doubled in the source file) |

**New sections the 2024 profile does not have at all:**

1. **Timeline 2021 → 2026** — five years is now a story worth drawing.
2. **Where we are** — a map of the estate. Fifteen sites reads as a chain; a paragraph reads as a claim.
3. **The insight** — *dessert used to be an occasion you travelled to; when it finally travelled to you it arrived soggy.* The stick is a handle, the square packs flat, the box is worth filming. This is one page and it is the strongest page you can add, because it explains why the product is shaped the way it is.
4. **The Surprise Card** — the loyalty engine, with its real numbers.
5. **The Waffle Up Gang** — ten owned characters as an IP asset.
6. **Operations & tech** — POS, per-channel price books, the food-tech framing the Vision already claims.
7. **Supply & quality** — halal, ingredients, hygiene. Non-negotiable for any B2B reader.
8. **Expansion & partnership** — the forward-looking close the old deck ends without.

---

## 3. Proposed structure

**Part 0 — Open**
1. Cover
2. What we are, in one line
3. Contents

**Part 1 — The company**
4. Our story
5. Where it started — Banani, 16 Dec 2021
6. Five years — timeline 2021→2026
7. Purpose · Mission · Vision
8. Value pillars
9. In numbers — 2026
10. Where we are — the estate map

**Part 2 — The proposition**
11. The insight — joy that travels
12. Product form as proof — the stick, the square, the box
13. What makes us different (rebuilt, one proof per claim)
14. Range — Waffle on a Stick
15. Range — Waffles
16. Range — Beverages & Zero-Guilt
17. Packaging

**Part 3 — The brand engine**
18. Identity at a glance — logo, colour, type
19. The Waffle Up Gang — ten owned characters
20. The Surprise Card — the reward loop
21. Content, social & audio

**Part 4 — The business**
22. Outlet models ×4
23. Estate & channels — own delivery, delivery partners
24. Events & catering
25. Operations & technology
26. Supply, quality & certification

**Part 5 — People & proof**
27. Culture
28. Team & leadership
29. Awards & certifications
30. Making headlines
31. Partners & clients

**Part 6 — Forward**
32. Singapore & the expansion pipeline
33. Partner with us
34. Contact

---

## 4. Workflow

| Phase | What happens | Blocked by |
|---|---|---|
| **0 · Decide** | Audience call (§6), value pillars, mission wording, format | Jawat |
| **1 · Gather** | Facts verified, documents collected, existing assets audited — `GATHER.md` | Ops, Finance, Legal, SG |
| **2 · Capture** | The shoot — `CAPTURE-BRIEF.md` | Phase 0 audience call |
| **3 · Write** | Copy deck, page by page, `[CONFIRM]` on anything unverified | Phase 1 |
| **4 · Build** | HTML → PDF via the `build.py` route, 1440×810 | Phases 2 + 3 |
| **5 · Sign-off** | Founder read, legal read on claims/certifications, print proof | — |

Phases 1 and 2 run in parallel. Phase 3 can start on the narrative pages (story, insight, vision) before the shoot finishes.

---

## 5. Brand decisions this document forces

**a) The value pillars conflict — RESOLVED.** The brand guideline says **Quality · Joy · Community · Innovation**. The 2024 profile says **Quality · Speed · Access · Innovation**. Both are in the library and they are not the same promise — *Speed and Access* is an operations argument, *Joy and Community* is a brand argument.

> **Decided by Jawat, 1 Sep 2026: the profile prints Quality · Speed · Access · Innovation.** Joy and Community are carried by the Culture and Gang sections rather than sitting as pillars. This decision is scoped to the company profile; it does not overwrite the brand guideline's set for other uses.

**b) "Premium" is in the Mission.** *"Offering innovative, delicious and premium products…"* — and the marketing rule in `CLAUDE.md` is that WaffleUp never sells itself in the luxury register, because the entire brand exists to de-luxury the waffle. In a *company* profile "premium" reads as premium ingredients, which is defensible and different from premium positioning. Options: print the mission as-is and let the ingredient meaning carry it, or amend to *"innovative, delicious, honestly-made products."* Recommendation: **print it as-is** — a mission statement is an asset, not copy, and rewriting it for one document puts two versions into circulation.

**c) One hard rule that applies to the whole document.** The value-language rule holds here as much as in an ad: **no "free", no "discount", no "% off"** anywhere in the profile, including in the description of the Surprise Card. The internal channel map describes the card as *"unlock free items"* — that phrasing must not reach this document. Write it as *rewards, surprises, what the card unlocks*.

---

## 6. Audience — decided

**Business-first.** Confirmed by Jawat, 1 Sep 2026. Primary reader: **franchise, investor, landlord and corporate B2B.** Secondary: press.

Rationale: the consumer story is already told daily across three channels with a real content engine behind it. The business story is currently being told by a document that says we are opening in Egypt.

What this settles:

- **Weight** goes to estate, operations, team and certification. Product and characters are still present and still strong, but they are evidence rather than the point.
- **Leadership portraits are P1**, not optional. A business profile with inconsistent or missing exec portraits reads as rushed.
- **Customer and street coverage drops to P2** — with one exception: CUS-01, someone walking with a waffle on a stick, stays P1 because it is the literal picture of the insight page.
- **Full operations coverage stays in** — kitchen, cloud kitchen, packing, POS and price-book story.
- **Voice** stays Jester on the product and Gang pages, and goes plain-and-confident on every page carrying a number, a claim or a certification.

---

## 7. Files in this campaign

- `PLAN.md` — this document
- `CAPTURE-BRIEF.md` — every photograph and clip to be captured, by location, with specs
- `GATHER.md` — every fact, document, logo and existing asset to be collected, with owners
