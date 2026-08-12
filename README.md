<div align="center">

# WaffleUp Brand Kit

**One portable folder that makes every WaffleUp repo look, sound and behave like WaffleUp.**

`v1.7.0` · maintained by the AI & Automation team

</div>

---

## What this is

A drop-in kit for every WaffleUp codebase — POS, inventory, manufacturing, SOP apps, dashboards, mobile apps, internal sites. It carries the brand truth in three forms:

1. **For humans** — `brand/*.md`: what the brand is, how it sounds, what the rules are.
2. **For machines** — `tokens/*`: the same palette, type scale and shape language as JSON, CSS, SCSS, TS, Tailwind and Dart. No one retypes a hex code ever again.
3. **For AI agents** — `AGENTS.md` / `CLAUDE.md`: instructions Claude Code, Cursor, Copilot and friends read automatically so generated code is on-brand by default.

## Install into a repo

**Option A — git submodule (recommended, stays in sync)**

```bash
git submodule add https://github.com/<org>/waffleup-brand-kit .brand
cp .brand/AGENTS.md ./CLAUDE.md      # so Claude Code picks it up at repo root
```

**Option B — copy in**

```bash
cp -r waffleup-brand-kit ./.brand
cp ./.brand/AGENTS.md ./CLAUDE.md
```

Then wire up the tokens for your stack:

| Stack | Do this |
|---|---|
| Plain CSS / HTML | `<link rel="stylesheet" href=".brand/tokens/wup-tokens.css">` then `.brand/components/wup-components.css` |
| Tailwind | `presets: [require('./.brand/tokens/tailwind.wup.preset.js')]` in `tailwind.config.js` |
| React / Next / TS | `import { wup } from './.brand/tokens/wup-tokens'` |
| SCSS | `@use './.brand/tokens/wup-tokens' as wup;` |
| Flutter | `import 'package:.../.brand/tokens/wup_tokens.dart';` |
| Odoo module | link `wup-tokens.css` in your assets bundle; see `ODOO.md` |
| Anything else | read `tokens/wup-tokens.json` — it's the canonical source |

Open `components/preview.html` in a browser to see the whole system rendered.

## What's inside

```
waffleup-brand-kit/
├── AGENTS.md              ← rules for AI coding agents (copy to CLAUDE.md at repo root)
├── CLAUDE.md              ← identical copy, for Claude Code
├── ARCHITECTURE.md        ← the system spine: three registries, facts, views, build order
├── ODOO.md                ← how to apply this kit inside Odoo
├── brand/
│   ├── BRAND.md           ← the full brand truth: company, palette, type, menu, outlets
│   ├── VOICE.md           ← tone of voice + a microcopy bank you can paste from
│   ├── CHARACTERS.md      ← the Waffle Up Gang, and how to use them in software
│   └── LOGO-RULES.md      ← logo / symbol / icon usage, do's and don'ts
├── tokens/
│   ├── wup-tokens.json    ← CANONICAL. everything else is generated from this
│   ├── wup-tokens.css     ├ wup-tokens.scss
│   ├── wup-tokens.ts      ├ wup_tokens.dart
│   └── tailwind.wup.preset.js
├── components/
│   ├── wup-components.css ← sticker card, plaque button, wave divider, layered hero type
│   └── preview.html       ← open this to see it all
├── data/
│   ├── outlets.json       ← every outlet: ops codes, status, POS, BIN, hours, Foodpanda IDs
│   ├── menu.json          ← full catalogue, SKUs, both price books — POS-VERIFIED
│   └── CONVENTIONS.md     ← id / sku / channel / currency / date conventions + ingest rules
└── assets/
    ├── logo/ symbol/ icon/ pattern/ characters/ typography/ fonts/
    └── Color Code - RGB|CMYK|Pantone.png
```

## Building a system on top of this?

Read `ARCHITECTURE.md` first, then `data/CONVENTIONS.md`. The short version: three registries (outlets, items, people), then append-only facts that reference them, then disposable views. Two of the three registries already live in `data/`. Don't let a new module invent a fourth copy of any of them.

## Companion kit

`waffleup-marketing-kit/` sits alongside this one: occasions calendar, format specs, copy bank, campaign archive, the character-animation pipeline and the Surprise Card programme. This kit is *how the brand looks and sounds*; that one is *what to make and when*.

## The five rules, if you read nothing else

1. **Colours** come from tokens. Ink is `#450001`, never `#000000`.
2. **Ratio** 60–75% dominant colour, 15–25% secondary, 3–5% each accent.
3. **The logo always keeps its white signature wave.** Never solid letters, never recoloured.
4. **Shape language** is rounded, thick cocoa outline, hard offset shadow — sticker, not enterprise card.
5. **Voice is Jester** — plain functional labels, humour in empty states and success states, never in errors.

## And two data rules, since v1.6.0

6. **Prices come from `data/menu.json`, which comes from the POS.** Never from menu artwork — it has been stale by up to two revisions, and 12 prices in v1.5.0 were wrong because of it. Always state which price book.
7. **Use the ops team's outlet codes** (`WUP-FS-01`, `WUP-FC-03`, `WUP-CK-04`) and filter on `status`. Not every row in `outlets.json` is trading — Rampura is opening soon and two cloud kitchens are discontinued.

## Changing the kit

Edit `tokens/wup-tokens.json` first, then propagate to the other token files. Bump `VERSION`, note it in `CHANGELOG.md`, and let dependent repos pull the new submodule commit.

Source of truth for the underlying assets: the WaffleUp brand drive, `[WUP-01] Brand Assets`.
