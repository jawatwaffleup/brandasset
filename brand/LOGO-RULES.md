# Logo, Symbol & Icon — usage rules

## The three marks

### 1. Logo (primary)
"WAFFLE" in cyan and "UP" in pink, each carrying the **white signature wave**, set on a **Waffle Gold rounded plaque with a Deep Cocoa outline**, ® top-right.

`assets/logo/`
- `Waffle Up Logo - RBG.png` / `.eps` — **screens, web, apps**
- `Waffle Up Logo - CMYK.png` / `.eps` — **print, packaging, signage**

### 2. Symbol
The **W monogram** in a Waffle Gold circle with cocoa outline. Used where the full logo won't fit or reads too wide.

`assets/symbol/` — `Symbol (rbg).png`, `Symbol (cmyk).png`, `Brand-Icon--button.png`

### 3. Icon
App icons, favicons, social avatars. Five variants:

`assets/icon/`

| File | Use on |
|---|---|
| `Icon (rbg).png` | white / light backgrounds — **default for screens** |
| `Icon (rbg) - Social.png` | social profile avatars (safe-area padded) |
| `Icon (white).png` | cyan, pink, cocoa or photographic backgrounds |
| `Icon (red).png` | single-colour applications where pink/red is required |
| `Icon (cmyk).png` | print |

---

## Do

- **Even spacing in all directions.** Clearspace on every side ≥ the height of the "W" in the wordmark. Nothing — text, image, edge, button — inside it.
- **The signature wave must always run through the letterforms.** It is the identity, not a decoration.
- **Maintain proper colourisation across every medium and channel.** Digital gets the RGB build, print gets CMYK.
- Scale proportionally only.
- Minimum sizes: logo ≥ 120px wide on screen (≥ 25mm print); icon ≥ 32px; below that use the symbol.

## Don't

Straight from the brand guideline's "don'ts" page:

- ✗ **Uneven spacing or cropped-out corners**
- ✗ **Solid coloured letters without the signature wave**
- ✗ **Single coloured letters without the signature wave**

Plus:

- ✗ Recolouring to non-brand colours
- ✗ Stretching, squashing, skewing or rotating
- ✗ Removing the gold plaque, the cocoa outline, or the ®
- ✗ Adding drop shadows, glows, gradients or strokes of your own
- ✗ Placing on a busy photo without a plaque or sufficient contrast
- ✗ Rebuilding it in CSS/SVG by hand — always use the supplied file
- ✗ AI-generating or "cleaning up" the mark

---

## In code

```html
<!-- Screens, light background -->
<img src=".brand/assets/logo/Waffle Up Logo - RBG.png"
     alt="Waffle Up" width="180" style="margin: var(--wup-space-5)">

<!-- On a coloured field -->
<div class="wup-field-pink" style="padding: var(--wup-space-6)">
  <img src=".brand/assets/icon/Icon (white).png" alt="Waffle Up" width="48">
</div>
```

Clearspace in CSS: `padding: calc(<logo-width> * 0.22)` around the mark is a safe approximation of the "height of the W" rule.

**Favicon / PWA icon:** use `Icon (rbg).png`, exported at 512 / 192 / 180 / 32 / 16 px. Don't letterbox it — the icon already has its own safe area.

---

## Brand pattern

The organic wave-blob field of cyan, pink and gold on white with scattered white dots. `assets/pattern/Brand-Pattern.jpg`; vector source on the drive at `Works by Sharara/Brand Pattern/Brand Pattern.ai`.

This is the layout device that makes a screen read as WaffleUp before anyone reads a word. Use it for:

- splash and login screens
- dashboard headers
- printed receipt headers and footers
- empty states behind a character
- section dividers (see `.wup-wave` in `components/wup-components.css`)

Keep it behind content, never under body text at full contrast — knock it back or confine it to a band.
