# Five Years — anniversary campaign

**Status:** placeholder, opened 23 Aug 2026 · **Anchor date:** 16 December 2026 `[CONFIRM]`
**Supplied so far:** one badge / seal design, two colourways

---

## The date

First outlet opened **Banani, Dhaka, 16 December 2021**. Five years lands **16 December 2026** — just under four months out. The company was founded in Singapore earlier in 2021, so if the milestone is being counted from incorporation rather than from the Banani opening, the date moves. `[CONFIRM] which anniversary we're marking.`

Worth noting: 16 December is also **Bijoy Dibosh**. That is a national day with its own weight and its own tone, and a dessert brand's birthday sharing the date is a real consideration — it could be an asset or it could read badly. It needs a decision, not an accident.

---

## The supplied badge

A circular seal, two colourways — white ring with pink outline, and a solid pink fill version.

- **Character:** reads as **Air Maxi** — pink curls, cyan headphones, dark shades. `[CONFIRM]` the character ID, and confirm this artwork was produced from supplied character art rather than redrawn.
- **The "5":** a gold numeral held up over the head, hands gripping it. The gesture *is* the line — he's holding the number up.
- **Ring text:** **"5 YEARS. AND WE'RE ONLY GOING UP."**

### Why the line works

It puns on the brand name without announcing that it's punning — *Up* is doing double duty as trajectory and as WaffleUp. It's deadpan-adjacent, it's short, and it says something about the business rather than about the occasion. That's the difference between this and "Celebrating 5 wonderful years."

It is also **not attributed to the character**. The line sits in the ring, unspoken. That keeps it inside the rule that characters appear but don't speak until `brand/character-voices/` is approved.

### Two checks before this ships

1. **The pale blue disc behind the character** does not read as WaffleUp Cyan `#0BF9F6` — it looks like a muted powder blue. Brand cyan is electric. Worth pulling the source file and checking the actual value against `tokens/wup-tokens.json`.
2. **Outlines** should be Deep Cocoa `#450001`, never pure black. They look correct in the supplied render, but confirm in the file.

Neither is a rejection — both are five-minute checks on the source artwork.

---

## Where the artwork goes

Drop the supplied files into `campaigns/2026-12-five-years/assets/` as:

```
badge-5yr-white.png     the white-ring colourway
badge-5yr-pink.png      the solid pink colourway
badge-5yr.ai / .svg     vector source, if it exists
```

Vector matters here. This mark is going to end up on a box sticker, a Story frame, an X-banner and possibly a cup — it needs to scale, and it needs a version that survives at 200px.

---

## Strategic read — where this should go

*Not yet a plan. The angle, so the plan doesn't default to corporate.*

**The trap.** Anniversary campaigns almost always become about the company: milestones, thank-yous, a founder photo, "we are pleased to announce." That register is a hard fail for this brand — it's the corporate cousin of the luxury register, and it's just as off.

**The angle.** Five years is not WaffleUp's anniversary, it's the audience's. The kid who was 12 at the Banani opening is 17 now. Somebody's first WaffleUp was a school-day treat and is now a 1am habit. *That's* the story, and it's ownable — because nobody else in this market was selling a waffle on a stick in 2021.

**The founder story is finally usable at scale.** Salman brought waffles on a stick back from a US street truck into a market where a waffle was a luxury restaurant dessert sold in sets of four. Five years later it's the largest waffle chain in Bangladesh. That is *literally* "we're only going up," and it's the one moment in the calendar where telling it isn't self-indulgent.

**The Surprise Card is the obvious engine.** An anniversary is the single best excuse in the year for a **collectible season** — a numbered anniversary run, the badge on the card back, the rarest one dated 16.12.21. Scarcity of a *thing*, not of a price. That's exactly the allowed side of the value-language rule, and `programs/SURPRISE-CARD-GUIDELINE.md` already has the season mechanic built.

**Territory fit.** This sits mostly in *Collect the gang* (territory 5), with a strand of *No occasion required* inverted — for once there **is** an occasion.

---

## What I need before writing the campaign

1. Which date we're marking, and the Bijoy Dibosh decision
2. Scope — is this a week, a month, or a season?
3. Whether the Surprise Card anniversary run is on the table, and whether POS can carry a dated series
4. Whether Singapore runs it too, and on what date
5. Any budget or production constraint on physical (stickers, cups, box seals)

Give me those and this becomes a real brief with a shot list, a copy bank and a prompt set.
