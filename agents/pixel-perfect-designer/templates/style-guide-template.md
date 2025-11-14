# [Project Name] Design System Style Guide

**Version:** 1.0
**Last Updated:** [Date]
**Created By:** Pixel-Perfect Designer Agent

---

## Overview

### Design Philosophy
[Brief description of the design approach, principles, and goals]

### Target Audience
[Who this design is for - end users, context, industry]

### Use Cases
[Primary scenarios where this design system will be applied]

---

## Color Palette

### Primary Colors
```css
--color-primary: #[HEX];
--color-primary-light: #[HEX];
--color-primary-dark: #[HEX];
```

**Usage:** [When to use primary colors - CTAs, key actions, brand moments]

### Secondary Colors
```css
--color-secondary: #[HEX];
--color-secondary-light: #[HEX];
--color-secondary-dark: #[HEX];
```

**Usage:** [When to use secondary colors]

### Accent Colors
```css
--color-accent-1: #[HEX];
--color-accent-2: #[HEX];
```

**Usage:** [Highlights, badges, special states]

### Neutrals
```css
--color-gray-50: #[HEX];   /* Lightest */
--color-gray-100: #[HEX];
--color-gray-200: #[HEX];
--color-gray-300: #[HEX];
--color-gray-400: #[HEX];
--color-gray-500: #[HEX];  /* Base */
--color-gray-600: #[HEX];
--color-gray-700: #[HEX];
--color-gray-800: #[HEX];
--color-gray-900: #[HEX];  /* Darkest */
```

**Usage:** [Text, borders, backgrounds, subtle UI elements]

### Semantic Colors
```css
--color-success: #[HEX];
--color-warning: #[HEX];
--color-error: #[HEX];
--color-info: #[HEX];
```

**Usage:** [Success messages, warnings, errors, informational states]

### Backgrounds
```css
--bg-primary: #[HEX];
--bg-secondary: #[HEX];
--bg-tertiary: #[HEX];
```

---

## Typography

### Font Families
```css
--font-primary: '[Font Name]', sans-serif;
--font-secondary: '[Font Name]', serif;
--font-mono: '[Font Name]', monospace;
```

**Primary Font:** [Usage - UI text, body copy]
**Secondary Font:** [Usage - headings, emphasis]
**Monospace Font:** [Usage - code, technical content]

### Type Scale
```css
--text-xs: 0.75rem;    /* 12px */
--text-sm: 0.875rem;   /* 14px */
--text-base: 1rem;     /* 16px */
--text-lg: 1.125rem;   /* 18px */
--text-xl: 1.25rem;    /* 20px */
--text-2xl: 1.5rem;    /* 24px */
--text-3xl: 1.875rem;  /* 30px */
--text-4xl: 2.25rem;   /* 36px */
--text-5xl: 3rem;      /* 48px */
```

### Font Weights
```css
--font-light: 300;
--font-normal: 400;
--font-medium: 500;
--font-semibold: 600;
--font-bold: 700;
```

### Line Heights
```css
--leading-tight: 1.25;
--leading-normal: 1.5;
--leading-relaxed: 1.75;
--leading-loose: 2;
```

### Typography Usage

**H1 - Page Title**
- Font: `var(--font-secondary)`
- Size: `var(--text-4xl)`
- Weight: `var(--font-bold)`
- Line Height: `var(--leading-tight)`

**H2 - Section Heading**
- Font: `var(--font-secondary)`
- Size: `var(--text-3xl)`
- Weight: `var(--font-semibold)`
- Line Height: `var(--leading-tight)`

**H3 - Subsection Heading**
- Font: `var(--font-secondary)`
- Size: `var(--text-2xl)`
- Weight: `var(--font-semibold)`
- Line Height: `var(--leading-normal)`

**Body Text**
- Font: `var(--font-primary)`
- Size: `var(--text-base)`
- Weight: `var(--font-normal)`
- Line Height: `var(--leading-relaxed)`

**Small Text / Captions**
- Font: `var(--font-primary)`
- Size: `var(--text-sm)`
- Weight: `var(--font-normal)`
- Line Height: `var(--leading-normal)`

---

## Spacing System

### Base Unit
**Base:** 4px (0.25rem)

### Spacing Scale
```css
--space-0: 0;
--space-1: 0.25rem;   /* 4px */
--space-2: 0.5rem;    /* 8px */
--space-3: 0.75rem;   /* 12px */
--space-4: 1rem;      /* 16px */
--space-5: 1.25rem;   /* 20px */
--space-6: 1.5rem;    /* 24px */
--space-8: 2rem;      /* 32px */
--space-10: 2.5rem;   /* 40px */
--space-12: 3rem;     /* 48px */
--space-16: 4rem;     /* 64px */
--space-20: 5rem;     /* 80px */
--space-24: 6rem;     /* 96px */
```

### Usage Guidelines
- **Tight spacing:** Components within a card (space-2 to space-4)
- **Medium spacing:** Between related groups (space-6 to space-8)
- **Loose spacing:** Between major sections (space-12 to space-16)

---

## Shadows (Elevation System)

```css
--shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
--shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
--shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
--shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
--shadow-2xl: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
```

**Usage:**
- **sm:** Subtle cards, input focus states
- **md:** Standard cards, dropdowns
- **lg:** Modals, popovers, elevated cards
- **xl:** High-priority modals, overlays
- **2xl:** Dramatic elevation (rarely used)

---

## Border Radius

```css
--radius-none: 0;
--radius-sm: 0.125rem;   /* 2px */
--radius-md: 0.25rem;    /* 4px */
--radius-lg: 0.5rem;     /* 8px */
--radius-xl: 0.75rem;    /* 12px */
--radius-2xl: 1rem;      /* 16px */
--radius-full: 9999px;   /* Fully rounded (pills, circles) */
```

**Usage:**
- **Buttons:** `var(--radius-md)` to `var(--radius-lg)`
- **Cards:** `var(--radius-lg)` to `var(--radius-xl)`
- **Input fields:** `var(--radius-md)`
- **Avatars/Badges:** `var(--radius-full)`

---

## Component Styles

### Buttons

#### Primary Button
```css
.btn-primary {
  background: var(--color-primary);
  color: white;
  padding: var(--space-3) var(--space-6);
  border-radius: var(--radius-md);
  font-weight: var(--font-semibold);
  box-shadow: var(--shadow-sm);
}

.btn-primary:hover {
  background: var(--color-primary-dark);
  box-shadow: var(--shadow-md);
}
```

#### Secondary Button
```css
.btn-secondary {
  background: transparent;
  color: var(--color-primary);
  border: 1px solid var(--color-primary);
  padding: var(--space-3) var(--space-6);
  border-radius: var(--radius-md);
  font-weight: var(--font-semibold);
}

.btn-secondary:hover {
  background: var(--color-primary-light);
}
```

### Form Inputs

```css
.input {
  border: 1px solid var(--color-gray-300);
  padding: var(--space-3) var(--space-4);
  border-radius: var(--radius-md);
  font-size: var(--text-base);
  background: white;
}

.input:focus {
  border-color: var(--color-primary);
  box-shadow: 0 0 0 3px rgba([PRIMARY_RGB], 0.1);
  outline: none;
}
```

### Cards

```css
.card {
  background: white;
  border-radius: var(--radius-lg);
  padding: var(--space-6);
  box-shadow: var(--shadow-md);
}

.card:hover {
  box-shadow: var(--shadow-lg);
  transform: translateY(-2px);
}
```

### Navigation

```css
.nav-link {
  color: var(--color-gray-700);
  padding: var(--space-2) var(--space-4);
  font-weight: var(--font-medium);
  border-radius: var(--radius-md);
}

.nav-link:hover {
  background: var(--color-gray-100);
  color: var(--color-primary);
}

.nav-link.active {
  background: var(--color-primary);
  color: white;
}
```

---

## Animations

### Timing Functions
```css
--ease-in: cubic-bezier(0.4, 0, 1, 1);
--ease-out: cubic-bezier(0, 0, 0.2, 1);
--ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);
```

### Durations
```css
--duration-fast: 150ms;
--duration-normal: 250ms;
--duration-slow: 350ms;
```

### Standard Transitions
```css
--transition-colors: color var(--duration-normal) var(--ease-in-out),
                     background-color var(--duration-normal) var(--ease-in-out);
--transition-shadow: box-shadow var(--duration-normal) var(--ease-out);
--transition-transform: transform var(--duration-normal) var(--ease-out);
```

**See animation-spec.md for detailed micro-interaction specifications**

---

## Responsive Breakpoints

```css
--breakpoint-sm: 640px;   /* Mobile landscape */
--breakpoint-md: 768px;   /* Tablet */
--breakpoint-lg: 1024px;  /* Desktop */
--breakpoint-xl: 1280px;  /* Large desktop */
--breakpoint-2xl: 1536px; /* Extra large */
```

---

## Accessibility Guidelines

### Color Contrast
- **Normal text:** Minimum 4.5:1 contrast ratio
- **Large text (18px+):** Minimum 3:1 contrast ratio
- **Interactive elements:** Minimum 3:1 contrast against background

### Focus States
- All interactive elements must have visible focus indicators
- Use `box-shadow` or `outline` with `var(--color-primary)` at 10% opacity

### ARIA Labels
- Provide `aria-label` for icon-only buttons
- Use semantic HTML elements where possible
- Ensure forms have proper labels and error messaging

---

## Design Tokens (CSS Variables)

```css
:root {
  /* Colors */
  --color-primary: [VALUE];
  --color-secondary: [VALUE];

  /* Typography */
  --font-primary: [VALUE];
  --text-base: [VALUE];

  /* Spacing */
  --space-4: [VALUE];

  /* Shadows */
  --shadow-md: [VALUE];

  /* Border Radius */
  --radius-lg: [VALUE];

  /* Animations */
  --duration-normal: [VALUE];
}
```

---

## Usage Notes

### For Designers
- Reference this guide when creating new screens or components
- Maintain consistency by using defined tokens
- Propose updates to this guide through version control

### For Developers
- Implement design tokens as CSS variables or framework config (Tailwind, etc.)
- Build reusable components that match these specifications
- Report deviations or edge cases for design review

### For the Agent
- This style guide guards all future design behavior
- Always reference these specifications when generating new UI
- Maintain consistency across all components and pages

---

## Version Control

**v1.0** - [Date] - Initial style guide created from reference page
[Add subsequent versions here with change notes]

---

**Generated by:** Pixel-Perfect Designer Agent
**Framework:** Flow Engineering Methodology
**Contact:** [Project owner contact if applicable]
