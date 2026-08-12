# Should WaffleUp build on Odoo?

Written Aug 2026 for the WaffleUp AI & Automation team. This is an engineering opinion, not a procurement decision.

## The honest answer: partly

**Odoo is a strong fit for the back office. It's a weak fit for the outlet counter.**

Odoo Community Edition (v19 is current) is free and open source under LGPL, self-hosted, and already ships the exact modules you'd otherwise spend a year rebuilding: **Inventory, Manufacturing (MRP), Purchase, Accounting basics, Employees, Attendance, Recruitment, Helpdesk-adjacent tooling**. Crucially it gives you the thing you actually said you want — **one unified database** with a shared model for products, partners, locations and employees, plus a real ORM, permissions, audit trail and reporting layer.

The problem is the POS. Reviews consistently flag that in Community Edition, **kitchen order tickets, floor plans and table management are limited, and there's no robust offline POS or official IoT-box support** for printers, cash drawers and scanners. Those aren't nice-to-haves in a QSR with a dispatch window and unreliable wifi. And you already have three POS systems in the field (GiantSoft at the 8 standard outlets, ZAB at the 4 Chef's Table sites, Foodpanda at the cloud kitchens) that aren't going away next quarter — plus Otomatic in the history, which breaks any trend line crossing the switch.

## Recommended shape

> The layered view — three registries, facts, views — is in `ARCHITECTURE.md`. This file is about where Odoo sits within it: the back-office consumer, not the spine.

```
        Giantsoft        ZAB        Foodpanda POS
        (outlets)     (Chef's Table)  (cloud kitchens)
             │             │              │
             └─────────────┴──────────────┘
                           │  nightly / hourly sales import
                           ▼
              ┌──────────────────────────┐
              │   Odoo Community (self-  │
              │   hosted)                │
              │  Inventory · MRP ·       │
              │  Purchase · Employees ·  │
              │  Attendance · Reporting  │
              └──────────────────────────┘
                     ▲            ▲
        Odoo REST/JSON-RPC        │
                     │            │
      ┌──────────────┴───┐   ┌────┴─────────────┐
      │ WaffleUp Ops app │   │ Management       │
      │ (phone-first)    │   │ dashboard (web)  │
      │ open/close SOPs  │   │ branded          │
      │ stock counts     │   └──────────────────┘
      │ wastage photos   │
      └──────────────────┘
```

**Odoo is the database and the back office. Your own branded apps are the interface staff actually touch.** That split lets you:

- stop rebuilding inventory/MRP/HR from scratch
- keep total design control where the brand shows
- avoid fighting Odoo's POS limitations
- swap the fragmented POS systems out later without redoing everything

## What to do in what order

1. **Don't start with Odoo.** Start with the opening/closing SOP app and wastage capture — small, phone-first, immediate relief, and it forces you to define outlets, items and shifts properly. Ship it standalone with a plain Postgres schema following `data/CONVENTIONS.md`. Seed `outlet` from `data/outlets.json` and `item` from `data/menu.json`; both are now POS-verified, and the ops team's outlet codes (`WUP-FS-01` …) are already printed on things — adopt them rather than inventing new IDs.
2. **Stand up Odoo Community in parallel**, with Inventory + Purchase only, and load your item master and BOMs. Run it alongside the Excel sheets for one full cycle.
3. **Point the SOP/stock app at Odoo** via JSON-RPC once the item master is trustworthy. Your app becomes Odoo's mobile front end for the things Odoo's own UI is bad at.
4. **Then MRP** for the commissary — batch production of waffle bases and sauces, distribution to outlets.
5. **Then sales ingestion** — nightly imports from GiantSoft/ZAB/Foodpanda into Odoo so stock depletion is automatic and margin reporting becomes real. Three things will bite, all documented in `waffleup-marketing-kit/data/POS-AND-REPORTING.md`: the ZAB detail export **duplicates item-line pages** (aggregate by invoice sub-total or overstate Chef's Table by 29%); item names differ across all three systems, so ingestion must go through an alias table and never a name match; and Foodpanda overlaps GiantSoft, so summing them double-counts. Reconcile every import against the source report's own printed total — that check is the only thing that catches a silently-broken parser.
6. **Then HR/attendance** — fingerprint device → Odoo Attendance, then payroll.
7. **Only consider Odoo POS last**, and only for new outlets, only after you've validated it handles a dispatch window offline.

## Costs and cautions

- **Community is genuinely free**, but self-hosting isn't: budget for a VPS, backups, monitoring and someone who can do a version upgrade. Odoo Online/Enterprise starts around **$31/user/month**, which for 100+ team members is not casual money — that's the main reason to stay on Community.
- **Enterprise-only features** you'll notice missing: full accounting, some POS/IoT bits, studio (drag-drop customisation), official support. The OCA (Odoo Community Association) and third-party modules fill many gaps — vet them for the version you're on.
- **Version upgrades between major releases are real work** if you've written custom modules. Keep customisation in your own modules, never fork core.
- **Odoo's UI is not brandable in any deep sense.** You can restyle it with `tokens/wup-tokens.css` in an assets bundle and swap the logo, and it'll look tidy — but it will never look like WaffleUp. That's precisely why staff-facing screens belong in your own apps.

## Branding an Odoo instance with this kit

Minimum viable, worth doing for the back office:

1. Custom module `wup_brand`, add to `web.assets_backend`:
   ```python
   # __manifest__.py
   'assets': {
       'web.assets_backend': [
           'wup_brand/static/src/css/wup-tokens.css',
           'wup_brand/static/src/css/wup-odoo-overrides.css',
       ],
   }
   ```
2. Copy `tokens/wup-tokens.css` in; write overrides mapping Odoo's variables to ours (`$o-brand-primary: #FF629B`, `$o-brand-odoo: #450001`).
3. Replace the company logo with `assets/logo/Waffle Up Logo - RBG.png` and the favicon with `assets/icon/Icon (rbg).png` in Settings → Companies.
4. Set company address to the Banani office, currency BDT, language en_US + bn_BD, timezone Asia/Dhaka.
5. Report templates (invoices, picking slips, labels) — use the **CMYK/print** token variants, not the digital ones.

## Alternatives worth 30 minutes of consideration

| Option | Verdict |
|---|---|
| **Odoo Community, self-hosted** | Best fit for back office. Recommended. |
| **ERPNext / Frappe** | Also free, arguably nicer developer experience, strong manufacturing. Smaller module ecosystem. A legitimate second choice — worth a spike. |
| **Build everything custom** | Full brand control, but you'd spend a year rebuilding inventory and MRP badly. Only do this for the staff-facing layer. |
| **Odoo Enterprise / Odoo Online** | Fastest start, but per-user pricing over 100+ staff is the wrong shape for a QSR. |
| **Stay on Excel + point tools** | The status quo. Fine for one more quarter, not for 16+ locations. |

---

**Sources:** [Odoo Community Edition: Features, Limits & Cost (2026)](https://theledgerlabs.com/odoo-community-edition-guide/) · [Odoo POS Software Review (2026)](https://www.posusa.com/odoo-pos-review/) · [Odoo Community Edition POS features & required modules](https://www.farishtatech.com/odoo-community-edition-pos-point-of-sale-features-required-modules/) · [Odoo Download 2026 guide](https://www.codegenes.net/blog/odoo-download/)
