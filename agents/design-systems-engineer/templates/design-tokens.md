# Design Tokens

Design tokens are the visual design atoms of the design system. They are named entities that store visual design attributes.

---

## Color Tokens

### Primary Colors

Used for primary actions, links, and brand identity.

| Token | Value | Usage |
|-------|-------|-------|
| `primary-50` | `#...` | Lightest shade, backgrounds |
| `primary-100` | `#...` | Very light, hover states |
| `primary-200` | `#...` | Light, disabled states |
| `primary-300` | `#...` | Light medium |
| `primary-400` | `#...` | Medium light |
| `primary-500` | `#...` | **Base primary color** |
| `primary-600` | `#...` | Medium dark, hover states |
| `primary-700` | `#...` | Dark |
| `primary-800` | `#...` | Very dark |
| `primary-900` | `#...` | Darkest shade |

**Examples:**
- Buttons (primary variant)
- Links
- Selected states
- Focus indicators

---

### Secondary Colors

Used for secondary actions and complementary elements.

| Token | Value | Usage |
|-------|-------|-------|
| `secondary-500` | `#...` | **Base secondary color** |

**Examples:**
- Secondary buttons
- Alternative CTAs
- Supporting UI elements

---

### Semantic Colors

Colors with specific meanings.

#### Success
| Token | Value | Usage |
|-------|-------|-------|
| `success-500` | `#...` | Success states, confirmations |

#### Warning
| Token | Value | Usage |
|-------|-------|-------|
| `warning-500` | `#...` | Warnings, caution states |

#### Error/Destructive
| Token | Value | Usage |
|-------|-------|-------|
| `destructive-500` | `#...` | Errors, destructive actions |

#### Info
| Token | Value | Usage |
|-------|-------|-------|
| `info-500` | `#...` | Informational messages |

---

### Neutral Colors

Used for text, backgrounds, borders.

| Token | Value | Usage |
|-------|-------|-------|
| `neutral-50` | `#...` | Lightest background |
| `neutral-100` | `#...` | Card backgrounds |
| `neutral-200` | `#...` | Borders, dividers |
| `neutral-300` | `#...` | Disabled text |
| `neutral-400` | `#...` | Placeholder text |
| `neutral-500` | `#...` | Secondary text |
| `neutral-600` | `#...` | Body text |
| `neutral-700` | `#...` | Headings |
| `neutral-800` | `#...` | Primary text |
| `neutral-900` | `#...` | Darkest text |

---

## Typography Tokens

### Font Families

| Token | Value | Usage |
|-------|-------|-------|
| `font-sans` | `Inter, system-ui, sans-serif` | Body text, UI elements |
| `font-heading` | `Poppins, sans-serif` | Headings, titles |
| `font-mono` | `JetBrains Mono, monospace` | Code, monospace text |

---

### Font Sizes

| Token | Pixels | Rem | Line Height | Usage |
|-------|--------|-----|-------------|-------|
| `text-xs` | 12px | 0.75rem | 1rem | Fine print, labels |
| `text-sm` | 14px | 0.875rem | 1.25rem | Small text, captions |
| `text-base` | 16px | 1rem | 1.5rem | **Body text default** |
| `text-lg` | 18px | 1.125rem | 1.75rem | Large body text |
| `text-xl` | 20px | 1.25rem | 1.75rem | Small headings |
| `text-2xl` | 24px | 1.5rem | 2rem | H3 headings |
| `text-3xl` | 30px | 1.875rem | 2.25rem | H2 headings |
| `text-4xl` | 36px | 2.25rem | 2.5rem | H1 headings |
| `text-5xl` | 48px | 3rem | 1 | Hero text, display |

---

### Font Weights

| Token | Value | Usage |
|-------|-------|-------|
| `font-normal` | 400 | Body text |
| `font-medium` | 500 | Emphasized text |
| `font-semibold` | 600 | Subheadings |
| `font-bold` | 700 | Headings |
| `font-extrabold` | 800 | Display text |

---

## Spacing Tokens

Based on 4px scale for consistency.

| Token | Pixels | Rem | Usage |
|-------|--------|-----|-------|
| `spacing-1` | 4px | 0.25rem | Tight spacing |
| `spacing-2` | 8px | 0.5rem | Small gaps |
| `spacing-3` | 12px | 0.75rem | Medium small gaps |
| `spacing-4` | 16px | 1rem | **Base spacing** |
| `spacing-5` | 20px | 1.25rem | Medium gaps |
| `spacing-6` | 24px | 1.5rem | Large gaps |
| `spacing-8` | 32px | 2rem | Section spacing |
| `spacing-10` | 40px | 2.5rem | Large section spacing |
| `spacing-12` | 48px | 3rem | Very large spacing |
| `spacing-16` | 64px | 4rem | Page sections |

---

## Border Radius Tokens

| Token | Value | Usage |
|-------|-------|-------|
| `rounded-sm` | 0.25rem (4px) | Small elements, badges |
| `rounded` | 0.5rem (8px) | **Default radius** |
| `rounded-md` | 0.5rem (8px) | Buttons, inputs |
| `rounded-lg` | 0.75rem (12px) | Cards, modals |
| `rounded-xl` | 1rem (16px) | Large cards |
| `rounded-2xl` | 1.5rem (24px) | Hero sections |
| `rounded-full` | 9999px | Circles, pills |

---

## Shadow Tokens

Elevation system for depth.

| Token | Value | Usage |
|-------|-------|-------|
| `shadow-sm` | `0 1px 2px 0 rgb(0 0 0 / 0.05)` | Subtle elevation |
| `shadow` | `0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1)` | **Default shadow** |
| `shadow-md` | `0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1)` | Cards, dropdowns |
| `shadow-lg` | `0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1)` | Modals, popovers |
| `shadow-xl` | `0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1)` | Large modals |
| `shadow-2xl` | `0 25px 50px -12px rgb(0 0 0 / 0.25)` | Hero sections |

---

## Breakpoint Tokens

Responsive design breakpoints.

| Token | Value | Devices |
|-------|-------|---------|
| `sm` | 640px | Mobile landscape, small tablets |
| `md` | 768px | Tablets |
| `lg` | 1024px | Laptops, desktops |
| `xl` | 1280px | Large desktops |
| `2xl` | 1536px | Extra large screens |

---

## Animation Tokens

### Duration

| Token | Value | Usage |
|-------|-------|-------|
| `duration-75` | 75ms | Instant feedback |
| `duration-100` | 100ms | Quick transitions |
| `duration-150` | 150ms | Micro-interactions |
| `duration-200` | 200ms | **Default duration** |
| `duration-300` | 300ms | Moderate animations |
| `duration-500` | 500ms | Slow animations |

### Easing

| Token | Value | Usage |
|-------|-------|-------|
| `ease-linear` | `linear` | Constant speed |
| `ease-in` | `cubic-bezier(0.4, 0, 1, 1)` | Accelerating |
| `ease-out` | `cubic-bezier(0, 0, 0.2, 1)` | Decelerating |
| `ease-in-out` | `cubic-bezier(0.4, 0, 0.2, 1)` | **Default easing** |

---

## Z-Index Tokens

Layering system.

| Token | Value | Usage |
|-------|-------|-------|
| `z-0` | 0 | Base layer |
| `z-10` | 10 | Dropdowns |
| `z-20` | 20 | Sticky headers |
| `z-30` | 30 | Modals |
| `z-40` | 40 | Popovers |
| `z-50` | 50 | Tooltips |
| `z-999` | 999 | Always on top |

---

## Usage Guidelines

### Do's ✅
- Use design tokens for all visual properties
- Reference tokens by name, not raw values
- Update tokens centrally, not in components
- Document semantic meaning of each token

### Don'ts ❌
- Don't hardcode colors, sizes, or spacing values
- Don't create one-off custom values
- Don't use tokens for semantic purposes that don't match their intent
- Don't override token values in components

---

## Example Token Usage

### ✅ Good
```tsx
<button className="bg-primary text-primary-foreground px-4 py-2 rounded-md">
  Click me
</button>
```

### ❌ Bad
```tsx
<button style={{ backgroundColor: '#FF6B35', color: 'white', padding: '8px 16px', borderRadius: '6px' }}>
  Click me
</button>
```

---

**Design tokens ensure consistency across your entire design system!**
