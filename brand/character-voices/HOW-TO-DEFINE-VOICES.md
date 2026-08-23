# How to Define the WaffleUp Character Voices

**A workshop guide · 23 August 2026**
Produces the approved per-character files this folder is reserved for. See `README.md` for the required output structure.

> **Nothing in this file is approved.** The Mr Waffle draft in §5 is a worked example showing the shape of the output — it is a proposal for you to accept, edit or reject, not a decision. Until a character file is signed off, characters may appear visually but **must not speak in first person**.

---

## 1. The problem you're actually solving

You have ten characters, several people writing copy, and AI tools in the loop. Without written voices, three things happen — reliably, and within about a month:

1. **Drift.** Bhoppu sounds different in March than in June, because a different person wrote him.
2. **Collapse.** Every character converges on the same generic "fun mascot" voice, and the cast becomes one character wearing nine costumes.
3. **Contamination.** An AI tool, given no constraint, fills the gap with the average of every cartoon mascot on the internet.

Collapse is the dangerous one, and it's the one nobody notices happening.

### The insight that makes this work

> **Consistency comes from contrast.** You cannot define these voices one at a time in isolation. A voice is only distinct relative to the others.

If you define Bhoppu alone, you'll write "energetic and fun." If you define Bhoppu *next to Picchi and Icy*, you'll discover all three are energetic and fun — and you'll be forced to make the actual decision about what separates them. That decision is the deliverable.

**So: never define one character in a sitting. Define three, side by side.**

---

## 2. Two layers of "voice"

| Layer | What it is | Needed when |
|---|---|---|
| **Written voice** | Personality, vocabulary, rhythm, what they'd never say | **Now.** Unblocks captions, cards, in-app copy |
| **Spoken voice** | Actual audio — casting, accent, pitch, delivery | Only if you do voiced video |

This guide covers **written voice**, which is the blocker today. §9 covers what changes if you later add audio — the decisions are different and much more expensive to reverse, so don't make them casually as a side effect of this workshop.

---

## 3. Start with the anchor, not the season

**Define Mr Waffle first, on his own, before anything else.**

He's the flagship — an actual waffle in sunglasses, "the original trendsetter." Every other voice will be defined by how it differs from his. Fix the tuning fork first, then tune the rest against it.

**Then work in threes, matched to Surprise Card seasons** (see `programs/SURPRISE-CARD-GUIDELINE.md` §3), so voice definition arrives exactly when that season's content needs it:

| Order | Set | Characters |
|---|---|---|
| 0 | **The anchor** | Mr Waffle |
| 1 | Season 1 — The Street | Air Maxi · Bhoppu · Picchi |
| 2 | Season 2 — The Originals | Stovy · Icy *(Mr Waffle already done)* |
| 3 | Season 3 — The Late Shift | Swirly · Tvy · Spacy |
| 4 | Singapore only | Merlulu |

That's four short sessions instead of one impossible one. **Merlulu is Singapore-only** and must never be written as part of the Bangladesh nine.

---

## 4. The differentiation map

Before writing a single line, plot the characters against each other. This is the whole workshop in one exercise.

Two axes: **Energy** (calm → hyper) and **Warmth** (dry/cool → warm/earnest).

```
                        HYPER
                          │
         Air Maxi ●       │       ● Bhoppu
                          │       ● Picchi
          Swirly ●        │       ● Icy
                          │
   DRY ───────────────────┼─────────────────── WARM
                          │
             Tvy ●        │       ● Stovy
       Mr Waffle ●        │       ● Spacy
                          │
                        CALM
```

**[DRAFT placement — this is my read of the approved bios, and it is exactly what the workshop should argue about.]**

### The collisions you must resolve

The map immediately shows where the cast is at risk of collapsing. These are your real decisions:

| Collision | The question to answer |
|---|---|
| **Bhoppu · Picchi · Icy** all sit hyper-and-warm | Three "fun energetic" characters is two too many. What separates them? My read: Bhoppu is **physical** (a bear with a dumbbell), Picchi is **innocent** (a small kid, pure delight), Icy is **social** (the life of the party). Different *sources* of the same energy. |
| **Mr Waffle · Tvy** both sit calm-and-dry | Both are deadpan. Separation: Mr Waffle is **effortlessly current**; Tvy is **deliberately retro**. Same dryness, opposite relationship to time. |
| **Air Maxi vs Mr Waffle** | Both "cool." The cleanest distinction in the whole cast: **Mr Waffle set the trend. Air Maxi follows it — expertly, first, but he follows.** Originator vs early adopter. |

Resolve those three and the cast holds together. Leave them unresolved and it collapses within a quarter, no matter how good the individual files are.

---

## 5. Worked example — Mr Waffle

**⚠ DRAFT FOR APPROVAL — not usable until signed off.**

Built strictly from the approved Surprise Card bio in `data/characters.json`, and nothing else:

> *"The original trendsetter of the waffle world! With a drizzle of style and a splash of sass, he's here to prove that breakfast can be the highlight of any day. 'Stay crispy, stay cool!'"*

---

### 1. Voice in one sentence
Mr Waffle is the one who was here first and has never once needed to mention it.

### 2. Personality and energy
Calm, dry, quietly amused. **Low energy by design** — he's the still point the rest of the cast moves around. His confidence is structural, not performed: he never oversells, never shouts, never chases. Sass, in his case, means a raised eyebrow, not a punchline.

**Energy: 2/5. Warmth: 2/5.**

### 3. Vocabulary, catchphrases, language mix
- Short sentences. Often just one.
- Understatement as the default setting.
- Never uses intensifiers — no "super", "so", "totally", "literally".
- **Catchphrase (approved, from the bio):** *"Stay crispy, stay cool."* Use sparingly — a catchphrase used every time stops being one.
- **Language:** English-led. Occasional Bangla, always dry and short, never a laboured pun. Per `brand/VOICE.md`, Bangla humour should be warm-and-plain rather than wordplay.

### 4. What he may and may not say

**May:** observe, understate, approve minimally, notice things before others do.
**May not:** hype, beg, exclaim, use more than one exclamation mark in a month, explain a joke, be self-deprecating about the brand, or chase a trend. **He does not follow. He is followed.**

### 5. Example lines *(draft)*

| Situation | Line |
|---|---|
| Greeting | "You came. Good call." |
| New flavour lands | "It's new. It's fine. It's very fine." |
| Late at night | "Still here. Where else." |
| Someone completes a card set | "All nine. Took you long enough." |
| Queue is long | "They know something." |
| Generic sign-off | "Stay crispy." |

### 6. Market
Bangladesh and Singapore. No restriction.

---

**Notice what's doing the work.** It's not the personality adjectives — it's the *prohibitions*. "Never uses intensifiers" and "one exclamation mark a month" are testable rules a new writer can follow on day one. "Confident and cool" is not.

**Write more prohibitions than permissions.** They're what actually holds a voice together.

---

## 6. The template

Copy this per character. Filename = the stable identifier from `data/characters.json` (`mr-waffle.md`, `air-maxi.md`, …).

```markdown
# {Character Name} — Voice

**Status:** Draft / Approved · **Approved by:** · **Date:**

## 1. Voice in one sentence

## 2. Personality and energy
Energy: _/5 · Warmth: _/5

## 3. Vocabulary, catchphrases, language mix
- Sentence length and rhythm:
- Words they always reach for:
- Words they never use:
- Catchphrase (only if one exists in the approved bio):
- English/Bangla mix:

## 4. What they may and may not say
**May:**
**May not:**

## 5. Example lines
| Situation | Line |
|---|---|
| Greeting | |
| New flavour lands | |
| Late at night | |
| Someone completes a card set | |
| Queue is long | |
| Generic sign-off | |

## 6. Market restrictions

## 7. How they differ from the nearest character
{The most important section. Name the character they're closest to and state the separation in one line.}
```

Section 7 isn't in the original README's list, and it's the one I'd insist on. It's what stops collapse.

---

## 7. Run the session — 90 minutes, three characters

**Before:** print the three approved bios from `data/characters.json` and the hero art from `assets/characters/`. Nothing else. **Do not read old captions** — you'll reproduce accidents.

| Time | Step |
|---|---|
| 0–10 | Read the three bios aloud. Only the approved text. |
| 10–25 | Plot all three on the energy/warmth map. Argue. **Collisions are the point** — if two land on the same spot, you've found your real work. |
| 25–55 | **The audition.** Write the same six situations (§6 table) for all three characters, side by side, in one pass. Same room, same sitting. |
| 55–70 | Read each row across, not down. Three lines for "late at night" — could you tell who's who with the names removed? **If not, the voices aren't distinct yet.** Rewrite until you can. |
| 70–85 | Write the prohibitions. Aim for more "may not" than "may". |
| 85–90 | Fill §7 for each — how they differ from their nearest neighbour. |

**Room:** 2–4 people maximum, including whoever writes the most copy day to day. That person must be in the room — they'll be the one holding the line afterwards.

---

## 8. The consistency test

Once a file is approved, any line can be checked in about ten seconds:

1. **The blind test.** Remove the character's name. Can someone in the team still identify them? If not, it's generic.
2. **The swap test.** Would this line work in another character's mouth? If yes, it's not in voice yet.
3. **The prohibition test.** Does it break any "may not"? Automatic fail, however good it sounds.
4. **The brand test.** Does it break `brand/VOICE.md` or the value-language rule in `CLAUDE.md` §3? **No character may say "free" or "discount"** — the character voice sits *inside* the brand voice, never outside it.

Test 2 catches most failures. It's the fastest and the most reliable.

---

## 9. If you later add spoken voice

Different decisions, much more expensive to reverse — a cast voice sticks for years and re-recording a back catalogue isn't realistic. Don't decide these as a side effect of this workshop.

- **Accent and language.** Bangladeshi English? Bangla-first? This is a positioning decision, not a casting one.
- **Human or processed.** Objects like Stovy, Tvy and Icy could carry processed voices; the human-ish characters shouldn't.
- **Consistency risk.** AI voice generation drifts between sessions and versions. If you go that route, lock a specific model and version per character and record it in the character file, or you'll get a different Bhoppu in six months.
- **Rights.** A human voice actor needs a contract covering AI training and reuse, explicitly. Get that right before the first session, not after.

**Recommendation: don't.** Written voice unblocks everything you currently need. Spoken voice is a real commitment and there's no content in `programs/SOCIAL-ENGINE.md` that requires it today.

---

## 10. What to do with the output

1. One file per character in this folder, named by stable identifier.
2. Mark **Status: Approved** with a name and date. Unapproved files must not be used.
3. Tell me they exist — I'll wire them into `CLAUDE.md` so characters can speak in first person, which unblocks GANG SIGHTING in the social engine and gives Surprise Card seasons a voice.
4. **Review at each season launch**, not continuously. Voices should be stable; if one keeps needing edits, the file isn't specific enough yet — usually it's short on prohibitions.

---

## Quick reference

| | |
|---|---|
| Define first | **Mr Waffle** — the anchor everything else is tuned against |
| Then | Three at a time, matched to Surprise Card seasons |
| Never | Define a character alone, or write dialogue before a file is approved |
| The key exercise | The audition — same six situations, three characters, side by side |
| The key test | The swap test — would this line work in another mouth? |
| The key content | Prohibitions. More "may not" than "may" |
| Hard boundary | Character voice sits inside brand voice. Never "free", never "discount" |
| Singapore | Merlulu only. Never one of the Bangladesh nine |
