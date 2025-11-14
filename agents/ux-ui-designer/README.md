# UX/UI Designer

Expert in polished visual design, design systems, component libraries, user experience patterns, accessibility (WCAG), responsive design, and creating high-fidelity mockups for web and mobile applications.

## Overview

This agent provides **polished, production-ready design expertise** for web and mobile applications. Unlike agents that create lo-fi wireframes for MVP speed, this agent focuses on **high-fidelity design**, design systems, component libraries, and visual polish suitable for production implementation.

## Core Capabilities

### User Experience (UX) Design
- User research interpretation and persona definition
- User journey mapping from awareness to retention
- Information architecture (sitemaps, navigation)
- Task flows and interaction design
- Empty states, loading states, error handling

### Visual Design (UI)
- **Visual Hierarchy:** Size, color, contrast, spacing to guide attention
- **Typography:** Type scales, font pairing, line height, optimal readability
- **Color Theory:** Primary/secondary colors, semantic colors, WCAG-compliant contrast
- **Spacing System:** Consistent 4px-based scale
- **Layout & Grid:** 12/8/4-column responsive grids

### Design Systems & Component Libraries
- **Buttons:** Primary/Secondary/Tertiary with states (hover, active, disabled, loading)
- **Forms:** Text inputs, selects, checkboxes, radio buttons, inline validation
- **Cards:** Consistent containers for related content
- **Modals & Dialogs:** Overlays with focus traps
- **Navigation:** Top nav, sidebar, breadcrumbs, tabs
- **Feedback:** Toasts, alerts, progress indicators, empty states
- **Data Display:** Tables, lists, stats/metrics

### Responsive Design
- **Breakpoints:** Mobile (320-767px), Tablet (768-1023px), Desktop (1024+)
- **Responsive Patterns:** Hamburger menus, stacked layouts, responsive typography
- **Touch Targets:** Minimum 44x44px (iOS), 48x48px (Android)

### Accessibility (WCAG 2.1 AA)
- **Contrast:** 4.5:1 for normal text, 3:1 for large text and UI components
- **Keyboard Navigation:** All interactive elements accessible via Tab/Enter/Esc
- **Focus Indicators:** Visible 2px outlines
- **Alt Text:** Descriptive for images, alt="" for decorative
- **Semantic HTML:** Proper elements and ARIA labels

### Design Tools & Deliverables
- **Tools:** Figma (preferred), Sketch, Adobe XD, Excalidraw, Miro
- **Deliverables:** High-fidelity mockups, interactive prototypes, design system documentation, responsive variants, icon libraries, asset exports

## When to Use This Agent

✅ **Use this agent when:**
- Creating high-fidelity, production-ready mockups
- Building design systems with component libraries
- Designing reusable UI components (buttons, forms, cards, modals)
- Mapping complete user journeys with polished screen designs
- Ensuring accessibility compliance (WCAG 2.1 AA)
- Designing responsive layouts (desktop, tablet, mobile)
- Improving visual hierarchy, spacing, and typography
- Conducting design critiques and reviews
- Applying brand guidelines to product UI

❌ **Don't use this agent for:**
- Lo-fi wireframes for MVP speed (use **Product & Growth Lead 0→1**)
- Product requirements (use **Product Manager**)
- Technical architecture (use **Technical Architect**)
- Growth experiments and analytics (use **Product Operations**)
- Code implementation (use development agents)

## Example Use Cases

### 1. High-Fidelity Dashboard Design

**Task:** "Design a dashboard showing key metrics (MRR, active users, churn rate) with filters and date range selection."

**Output includes:**
- High-fidelity desktop mockup (1440px width)
- Responsive mobile variant (375px width)
- Design system: Colors (Primary Blue 600, Neutrals Gray 900-100), Typography (Inter, type scale), Spacing (4px base unit)
- Component specs: Metric cards (large number, label, trend indicator), filters (dropdown, multi-select), date picker
- Interactive Figma prototype with working filters
- Accessibility notes: Contrast ratios (4.5:1 text, 3:1 UI components), keyboard navigation (Tab through filters)
- Developer handoff: Measurements, CSS color variables, SVG icon exports

### 2. Build a Design System

**Task:** "Create a design system for our SaaS product. Brand color is blue (#2563EB)."

**Output includes:**
- **Color Palette:**
  - Primary: #2563EB (Blue 600)
  - Secondary: #7C3AED (Purple 600)
  - Semantic: Success (#10B981 Green), Warning (#F59E0B Amber), Error (#EF4444 Red)
  - Neutrals: Gray 900/700/500/300/100, White
- **Typography:** Inter font, type scale (H1: 48px, H2: 32px, H3: 24px, H4: 20px, Body: 16px, Small: 14px), line heights
- **Spacing:** 4px base, scale (4/8/12/16/24/32/48/64/96/128)
- **Components:**
  - Buttons: Primary (filled), Secondary (outlined), Tertiary (ghost), sizes (Small 32px, Medium 40px, Large 48px), states (default, hover, active, disabled, loading)
  - Inputs: Text, select, checkbox, radio, validation states
  - Cards, Modals, Navigation, Alerts
- **Figma Component Library:** Reusable components with variants
- **Design Tokens:** JSON/CSS variables for dev handoff

### 3. Mobile Onboarding Flow

**Task:** "Design a 3-step onboarding flow for our iOS app. Users select interests, connect calendar, enable notifications."

**Output includes:**
- High-fidelity iOS mockups (375x812px, iPhone 13)
- 4 screens: Welcome + 3 onboarding steps
- Progress indicator (1 of 3, 2 of 3, 3 of 3) at top
- Skip button (top-right, low emphasis) for each step
- Primary CTA button (bottom, 48px height, thumb-friendly zone)
- Friendly illustrations for each step (interests, calendar, notifications)
- Interactive Figma prototype with smooth screen transitions
- Accessibility: Text contrast 4.5:1, touch targets 44x44px minimum, VoiceOver labels

## Design System Example

### Color Palette
```
Primary: #2563EB (Blue 600) - CTAs, links, focus states
Secondary: #7C3AED (Purple 600) - Secondary actions
Success: #10B981 (Green 500) - Positive feedback
Warning: #F59E0B (Amber 500) - Caution states
Error: #EF4444 (Red 500) - Errors, destructive actions
Info: #3B82F6 (Blue 500) - Informational messages

Neutrals:
- Gray 900: #111827 (headings)
- Gray 700: #374151 (body text)
- Gray 500: #6B7280 (secondary text)
- Gray 300: #D1D5DB (borders)
- Gray 100: #F3F4F6 (backgrounds)
- White: #FFFFFF
```

### Typography
```
Font: Inter (Google Fonts)

H1: 48px, weight 700, line-height 1.2 (hero headings)
H2: 32px, weight 700, line-height 1.2 (section headings)
H3: 24px, weight 600, line-height 1.3 (subsections)
H4: 20px, weight 600, line-height 1.4
Body: 16px, weight 400, line-height 1.6 (optimal readability)
Small: 14px, weight 400, line-height 1.5 (secondary info)
```

### Spacing System
```
Base: 4px

Scale:
- 4px (xs)
- 8px (sm)
- 12px (md)
- 16px (lg)
- 24px (xl)
- 32px (2xl)
- 48px (3xl)
- 64px (4xl)
- 96px (5xl)
- 128px (6xl)
```

## Accessibility Checklist

- [ ] Color contrast meets WCAG 2.1 AA (4.5:1 normal text, 3:1 large text/UI)
- [ ] All interactive elements keyboard accessible (Tab, Enter, Esc)
- [ ] Visible focus indicators (2px solid outline, high contrast)
- [ ] Images have descriptive alt text (or alt="" for decorative)
- [ ] Form inputs have associated labels
- [ ] Error messages are clear and actionable
- [ ] Don't rely on color alone to convey information (use icons, labels)
- [ ] Touch targets minimum 44x44px (iOS), 48x48px (Android)
- [ ] Test with screen reader (VoiceOver, NVDA)
- [ ] Test keyboard navigation without mouse

## Responsive Breakpoints

```
Mobile: 320-767px (4-column grid, 16px gutters)
Tablet: 768-1023px (8-column grid, 16px gutters)
Desktop: 1024-1439px (12-column grid, 24px gutters)
Large Desktop: 1440px+ (12-column grid, max 1440px width, centered)
```

## Best Practices

### User-Centered Design
- Design for user needs, not aesthetics alone
- Test designs with real users early and often
- Iterate based on feedback and data

### Consistency
- Use design system components consistently
- Maintain visual language across product
- Follow platform conventions (iOS HIG, Material Design, Web standards)

### Simplicity
- Remove unnecessary elements (minimalism)
- Prioritize clarity over cleverness
- Use familiar patterns when possible

### Accessibility
- Design for all users, including disabilities
- Test with keyboard, screen readers, zoom
- Don't sacrifice accessibility for aesthetics

### Collaboration
- Involve developers early to understand constraints
- Share work-in-progress for feedback
- Document design decisions and rationale

## How to Invoke

**In Claude Code:**
```
I need polished, production-ready mockups for our dashboard.

Launch a UX/UI Designer agent using the prompt from:
agents/ux-ui-designer/AGENT.md
```

**Direct reference:**
```
Please read agents/ux-ui-designer/AGENT.md and create a design system
with typography, colors, and core components for our SaaS product.
```

## Configuration

- **Model:** Sonnet (recommended for balanced speed/quality)
  - Use Opus for complex design systems or large component libraries
  - Use Haiku for simple component specs or quick critiques
- **Thoroughness:** Polished (default), or specify "concept" for quick explorations
- **Output:** Figma links (preferred), detailed descriptions, Mermaid diagrams for user flows

## Related Agents

**Use together with:**
- **Product Manager** - Provides product requirements and user flows
- **Product & Growth Lead 0→1** - For lo-fi wireframes (MVP speed)
- **Technical Architect** - For understanding technical constraints
- **UX Site Reviewer** (existing agent) - For auditing and improving existing designs

**UX/UI Designer role:**
- Receives requirements from Product Manager → Designs polished mockups → Hands off to developers
- Receives lo-fi wireframes from Product & Growth Lead 0→1 → Polishes for production

## Tips for Best Results

1. **Provide context:** Product stage, target users, brand guidelines
2. **Share examples:** Competitor designs, inspiration, existing designs to improve
3. **Define scope:** Specific screens/flows or full design system
4. **Clarify output:** "Figma mockups" vs. "Detailed descriptions" vs. "Interactive prototype"
5. **Include constraints:** Timeline, technical limitations, accessibility requirements

## Key Concepts

- **WCAG 2.1:** Web Content Accessibility Guidelines (A, AA, AAA levels)
- **ARIA:** Accessible Rich Internet Applications (semantic attributes)
- **Figma Variants:** Component properties for states/sizes (hover, active, disabled, small/medium/large)
- **Design Tokens:** Variables for colors, spacing, typography (sync design + code)
- **Progressive Disclosure:** Show advanced options only when needed
- **Mobile-First:** Start with mobile constraints, enhance for desktop

## Version History

- **1.0.0** (2025-11-05) - Initial version with UX, UI, design systems, accessibility

---

**Questions?**
- See [AGENT.md](./AGENT.md) for complete agent instructions
- See [agents/README.md](../README.md) for general agent guidance
