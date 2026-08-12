# WaffleUp — Voice & Microcopy

## The archetype

**Jester.** Casual · friendly · humorous.

From the brand guideline: *"Jester brands frequently employ humor and wit in their messaging to engage their audience. Waffle Up Ltd. should therefore concentrate on developing messages that are lighthearted, irreverent, and unexpected. Puns, jokes, and wordplay are all effective ways for brands that fit the Jester archetype."*

The whole company exists to take waffles down from the luxury-hotel dessert trolley and put them on a stick on the street. The voice does the same job: never precious, never corporate.

## Voice in three lines

- **We're funny, not silly.** The joke never gets in the way of the information.
- **We're warm, not soft.** Direct, quick, no hedging.
- **We're Bangladeshi and global at once.** Bangla and English mix freely — *Ashol WaffleUp Chinun*, *Bangla Pizza*, *Square is the new heart*.

## Where humour goes — and where it doesn't

| Context | Register | Why |
|---|---|---|
| Field labels, table headers, buttons | **Literal.** "Closing stock", "Submit count" | Staff are mid-shift, scanning |
| Errors, validation, compliance, money | **Literal.** "Count can't be negative." | Never make someone decode a joke while something is broken |
| Empty states | **Playful.** "Nothing here yet. Suspiciously clean." | Nobody's blocked; it's a free moment |
| Success / completion | **Playful.** "Shutter down. Go home, legend." | Reward the person |
| Nudges, streaks, reminders | **Playful.** | Motivation, not instruction |
| Onboarding, first-run | **Playful.** | Sets the tone |
| Loading | **Light.** "Warming the iron…" | Short, never annoying on repeat |

**Rule of thumb:** if the user is stuck, stressed, or handling money — be plain. If they're fine or they've just won — be funny.

## Paste-ready microcopy bank

**Empty states**
- "Nothing here yet. Suspiciously clean."
- "No orders yet today. The calm before the crunch."
- "No wastage logged. Either a perfect day or a forgotten form."
- "No items match that. Even the search is stumped."

**Success**
- "Shutter down. Go home, legend." *(closing checklist complete)*
- "Open for business. Go get 'em." *(opening checklist complete)*
- "Counted. Every last stick." *(stock count submitted)*
- "Saved. Crisp." *(generic save)*
- "Sent. Off it goes."

**Streaks / nudges**
- "7 days, zero missed checklists. Somebody's on a roll."
- "Two items below par. Worth a look before the evening rush."
- "Closing checklist is still open. The iron's cooled down, has it?"

**Loading**
- "Warming the iron…"
- "Stacking the squares…"
- "Counting sticks…"

**Confirmations**
- "Delete this count? It won't come back."  *(literal — destructive)*
- "Submit closing stock for {outlet}? You can't edit after this."

**Errors — always literal**
- "Count can't be negative."
- "Couldn't save. You're offline — we'll retry automatically."
- "This item isn't on {outlet}'s stock list."
- "Photo required before submitting."

**Never write**
- ~~"Oops! Something went wrong :("~~ — say what went wrong and what happens next
- ~~"Please kindly be informed that…"~~ — corporate stiffness
- ~~"Indulge in our premium artisanal experience"~~ — luxury register, wrong brand
- Jokes inside an error, a legal notice, or anything about someone's pay

## Signature lines & assets

| Line | Use |
|---|---|
| **SQUARE IS THE NEW HEART** | Primary tagline. Splash screens, printed material |
| **Ashol WaffleUp Chinun** (আসল ওয়াফলআপ চিনুন) | Bangla authenticity line, used on menus |
| Every Waffle Day | Packaging |
| For immediate consumption | Packaging — deadpan, very on-brand |

Pre-set word-marks available as artwork in `assets/typography/`: Waffleistic · Sweeeet · Obsessed · Drizzled with Love · Waffle Love · Crispy · Crunch Up · Smile · Order Now · Everyday · Ashol · Halal · Square · Love · Drizzle.

Use these images rather than trying to reproduce the effect in CSS when you need a hero word with the full four-layer treatment.

## Bangla

Staff-facing tools are bilingual. Bangla is not a translation afterthought — outlet teams may work in it primarily.

- Keep Bangla strings short; the display faces don't carry Bangla, so use `--wup-font-bangla` (Noto Sans Bengali / Hind Siliguri).
- Humour translates badly. In Bangla, prefer warm-and-plain over pun-based. A direct "হয়ে গেছে!" beats a laboured wordplay.
- Numbers and currency stay in Western numerals with `BDT` / `৳`.
