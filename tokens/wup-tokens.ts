/**
 * WaffleUp Design Tokens — TypeScript  ·  v1.0.0
 * Generated from tokens/wup-tokens.json. Do not hand-edit; edit the JSON.
 */

export const wup = {
  color: {
    cyan: '#0BF9F6',
    pink: '#FF629B',
    gold: '#FFD56D',
    cocoa: '#450001',   // ink — never use #000
    white: '#FFFFFF',
    print: { cyan: '#70CBD3', pink: '#F0629A', gold: '#FFD76D', cocoa: '#3F1212' },
    pantone: { cyan: '3255 C', pink: '212 C', gold: '1215 C', cocoa: '4975 C' },
    cyanScale:  { 100: '#DFFEFD', 300: '#8DFCFA', 500: '#0BF9F6', 700: '#06B5B3' },
    pinkScale:  { 100: '#FFE7EF', 300: '#FFA7C6', 500: '#FF629B', 700: '#D93C74' },
    goldScale:  { 100: '#FFF6E2', 300: '#FFE6A8', 500: '#FFD56D', 700: '#E0AE38' },
    cocoaScale: { 300: '#A56A6B', 500: '#6B1A1B', 900: '#450001' },
  },
  semantic: {
    bg: '#FFFFFF', bgAlt: '#DFFEFD', surface: '#FFFFFF',
    text: '#450001', textMuted: '#A56A6B', textInvert: '#FFFFFF',
    border: '#450001', accent: '#FF629B', accentAlt: '#0BF9F6', highlight: '#FFD56D',
    success: '#1FBF6B', warning: '#E0AE38', danger: '#D93C74', info: '#06B5B3',
  },
  font: {
    display:   '"CHUM", "Futura PT", Futura, system-ui, sans-serif',
    headline:  '"Futura PT Extra Bold", Futura, "General Sans", system-ui, sans-serif',
    condensed: '"Bebas Neue", Oswald, Impact, sans-serif',
    body:      '"General Sans", Inter, -apple-system, "Segoe UI", Roboto, sans-serif',
    bangla:    '"Noto Sans Bengali", "Hind Siliguri", "General Sans", sans-serif',
    size: { xs: '0.75rem', sm: '0.875rem', base: '1rem', lg: '1.25rem', xl: '1.75rem', '2xl': '2.5rem', hero: '4rem' },
  },
  radius: { sm: '8px', md: '16px', lg: '28px', pill: '999px' },
  stroke: { default: '3px', large: '5px' },
  shadow: {
    sticker: '0 4px 0 #450001',
    card:    '0 6px 0 #450001',
    soft:    '0 8px 24px rgba(69,0,1,0.12)',
  },
  space: { 1: '4px', 2: '8px', 3: '12px', 4: '16px', 5: '24px', 6: '32px', 7: '48px', 8: '64px' },
  motion: { dur: '180ms', ease: 'cubic-bezier(0.34, 1.36, 0.64, 1)' },
  touch: { minTarget: '48px' },
  /** 60-75% dominant / 15-25% secondary / 3-5% each accent */
  colorRatio: { dominant: [60, 75], secondary: [15, 25], accent: [3, 5] },
} as const;

export type WupBrandColor = 'cyan' | 'pink' | 'gold' | 'cocoa' | 'white';

/** Correct text colour to place on a brand field. */
export function onColor(bg: WupBrandColor): string {
  return bg === 'pink' || bg === 'cocoa' ? wup.color.white : wup.color.cocoa;
}

/** Format money the WaffleUp way: whole taka, no decimals. */
export function bdt(amount: number, symbol = false): string {
  const n = Math.round(amount).toLocaleString('en-BD');
  return symbol ? `৳${n}` : `BDT ${n}`;
}

export default wup;
