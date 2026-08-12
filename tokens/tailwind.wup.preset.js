/**
 * WaffleUp Tailwind preset  ·  v1.0.0
 * tailwind.config.js →  presets: [require('./.brand/tokens/tailwind.wup.preset.js')]
 */
module.exports = {
  theme: {
    extend: {
      colors: {
        wup: {
          cyan:  { DEFAULT: '#0BF9F6', 100: '#DFFEFD', 300: '#8DFCFA', 500: '#0BF9F6', 700: '#06B5B3', print: '#70CBD3' },
          pink:  { DEFAULT: '#FF629B', 100: '#FFE7EF', 300: '#FFA7C6', 500: '#FF629B', 700: '#D93C74', print: '#F0629A' },
          gold:  { DEFAULT: '#FFD56D', 100: '#FFF6E2', 300: '#FFE6A8', 500: '#FFD56D', 700: '#E0AE38', print: '#FFD76D' },
          cocoa: { DEFAULT: '#450001', 300: '#A56A6B', 500: '#6B1A1B', 900: '#450001', print: '#3F1212' },
        },
        // semantic aliases
        ink: '#450001',
        'ink-muted': '#A56A6B',
      },
      fontFamily: {
        display:   ['CHUM', 'Futura PT', 'Futura', 'system-ui', 'sans-serif'],
        headline:  ['Futura PT Extra Bold', 'Futura', 'General Sans', 'system-ui', 'sans-serif'],
        condensed: ['Bebas Neue', 'Oswald', 'Impact', 'sans-serif'],
        sans:      ['General Sans', 'Inter', '-apple-system', 'Segoe UI', 'Roboto', 'sans-serif'],
        bangla:    ['Noto Sans Bengali', 'Hind Siliguri', 'General Sans', 'sans-serif'],
      },
      fontSize: { hero: ['4rem', { lineHeight: '0.95' }] },
      borderRadius: { wup: '16px', 'wup-lg': '28px', 'wup-sm': '8px' },
      borderWidth: { wup: '3px', 'wup-lg': '5px' },
      boxShadow: {
        sticker: '0 4px 0 #450001',
        'wup-card': '0 6px 0 #450001',
        'wup-soft': '0 8px 24px rgba(69,0,1,0.12)',
      },
      minHeight: { touch: '48px' },
      minWidth:  { touch: '48px' },
      transitionTimingFunction: { wup: 'cubic-bezier(0.34, 1.36, 0.64, 1)' },
    },
  },
};
