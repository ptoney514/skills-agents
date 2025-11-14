---
name: css-style-extractor
description: Extract and parse CSS stylesheets into standardized, comprehensive style guide documentation. Use when you have CSS files from reference websites or design systems that need to be transformed into structured design system documentation with color palettes, typography, spacing, shadows, and component styles.
---

# CSS Style Extractor

Transform raw CSS stylesheets into comprehensive, structured style guide documentation that can be used for design system reference, brand alignment, or integration with AI design agents.

## When to Use This Skill

Use this skill when users request:
- Extracting style systems from website CSS
- Converting raw stylesheets into design documentation
- Creating style guides from existing code
- Documenting design tokens from CSS variables
- Analyzing and organizing design patterns from CSS
- Preparing CSS context for AI design agents
- Batch processing multiple CSS files into unified style guides

## Input Requirements

The skill processes CSS in various formats:

### Accepted Input Formats

1. **CSS Files** (`.css`)
   - Standard CSS files with selectors and rules
   - CSS with CSS variables (`:root { --color-primary: ... }`)
   - Component-specific stylesheets
   - Framework CSS (Bootstrap, Tailwind, etc.)

2. **Inline Styles** (HTML with `<style>` tags)
   - Full HTML documents
   - Extracted `<style>` sections

3. **CSS-in-JS** (if extracted to plain CSS)
   - Styled-components exports
   - Emotion stylesheets
   - Any CSS-in-JS converted to standard CSS

4. **Preprocessor Output** (compiled to CSS)
   - SCSS/SASS compiled output
   - LESS compiled output
   - PostCSS processed files

### Data Flow

```
data/inputs/css-extraction/
  ├── reference-site.css
  ├── extracted-styles.html
  └── design-system.css
        ↓
  [Processing Script]
        ↓
data/outputs/css-extraction/
  └── [Site-Name]-Style-Guide-[Date].md
```

## Core Workflow

### 1. Collect CSS Source Material

**From Website Inspection:**
1. Navigate to reference website
2. Right-click → Inspect Element
3. Go to Sources or Network tab
4. Find stylesheet files (`.css`)
5. Copy CSS content
6. Save as `.css` file in `data/inputs/css-extraction/`

**From `<style>` Tags:**
1. Right-click → View Page Source
2. Copy `<style>...</style>` content
3. Save as `.html` or `.css` file

**From Design Tools:**
1. Export CSS from Figma, Sketch, or design tools
2. Save exported file to input directory

**File Naming Convention:**
```
[source-name]__[date].css
Examples:
  motherduck__2025-11-14.css
  stripe-dashboard__2025-11-14.html
  company-design-system__2025-11-14.css
```

### 2. Parse and Categorize CSS

The processing script analyzes CSS and categorizes into:

#### A. Color System
- **CSS Variables:** Extract all `--color-*`, `--bg-*`, `--text-*` variables
- **Hex/RGB/HSL Values:** Identify recurring color values
- **Semantic Naming:** Group by purpose (primary, secondary, success, error, etc.)
- **Neutral Scales:** Detect gray scales (50, 100, 200, ..., 900)

**Example Extraction:**
```css
/* Input CSS */
:root {
  --color-primary: #3b82f6;
  --color-primary-dark: #2563eb;
  --gray-100: #f3f4f6;
}

/* Extracted to Style Guide */
### Primary Colors
- Primary: #3b82f6
- Primary Dark: #2563eb

### Neutrals
- Gray 100: #f3f4f6
```

#### B. Typography System
- **Font Families:** Extract all `font-family` declarations
- **Font Sizes:** Identify type scale (xs, sm, base, lg, xl, 2xl, etc.)
- **Font Weights:** Extract weights (light, normal, medium, semibold, bold)
- **Line Heights:** Document leading values (tight, normal, relaxed, loose)

**Example Extraction:**
```css
/* Input CSS */
--font-primary: 'Inter', sans-serif;
--text-base: 1rem;
--text-lg: 1.125rem;
--font-semibold: 600;

/* Extracted to Style Guide */
### Typography
**Font Family:** Inter, sans-serif
**Type Scale:**
- Base: 1rem (16px)
- Large: 1.125rem (18px)

**Weights:**
- Semibold: 600
```

#### C. Spacing System
- **CSS Variables:** Extract `--space-*`, `--gap-*`, `--padding-*`, `--margin-*`
- **Common Values:** Identify recurring spacing (4px, 8px, 16px, 24px, etc.)
- **Base Unit:** Detect base spacing unit (typically 4px or 8px)

#### D. Shadows (Elevation)
- **Box Shadows:** Extract all `box-shadow` values
- **Named Shadows:** Identify `--shadow-sm`, `--shadow-md`, etc.
- **Elevation Levels:** Categorize by intensity (subtle to dramatic)

**Example Extraction:**
```css
/* Input CSS */
--shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
--shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);

/* Extracted to Style Guide */
### Shadows
- Small: `0 1px 2px 0 rgba(0, 0, 0, 0.05)`
- Medium: `0 4px 6px -1px rgba(0, 0, 0, 0.1)`
```

#### E. Border Radius
- **Rounding Scale:** Extract `border-radius` values
- **Named Variables:** `--radius-sm`, `--radius-md`, etc.
- **Special Values:** `border-radius: 9999px` (fully rounded)

#### F. Component Styles
- **Buttons:** Extract button classes (`.btn`, `.btn-primary`, etc.)
- **Forms:** Input, textarea, select styles
- **Cards:** Card container styles
- **Navigation:** Nav, link, menu styles

**Example Extraction:**
```css
/* Input CSS */
.btn-primary {
  background: var(--color-primary);
  padding: 0.75rem 1.5rem;
  border-radius: 0.25rem;
  font-weight: 600;
}

/* Extracted to Style Guide */
### Buttons
**Primary Button:**
- Background: var(--color-primary)
- Padding: 0.75rem 1.5rem
- Border Radius: 0.25rem
- Font Weight: 600
```

#### G. Animations
- **Transitions:** Extract `transition` properties
- **Timing Functions:** `ease-in`, `ease-out`, cubic-bezier values
- **Durations:** Standard animation durations (150ms, 250ms, etc.)
- **Keyframe Animations:** Document `@keyframes` if present

### 3. Generate Structured Style Guide

The output follows the standardized template from the pixel-perfect-designer agent:

**Required Sections:**
1. **Overview** - Source website, extraction date, purpose
2. **Color Palette** - Primary, secondary, neutrals, semantic colors
3. **Typography** - Fonts, scale, weights, line heights
4. **Spacing System** - Base unit, scale, usage guidelines
5. **Shadows** - Elevation levels with use cases
6. **Border Radius** - Rounding scale
7. **Component Styles** - Key UI component patterns
8. **Animations** - Transitions, timing, easing functions

**Output File Naming:**
```
[Source-Name]-Style-Guide__[Date].md

Examples:
  MotherDuck-Style-Guide__2025-11-14.md
  Stripe-Dashboard-Style-Guide__2025-11-14.md
```

### 4. Quality Assurance

The skill performs quality checks:

**Completeness Check:**
- ✅ All CSS variables documented
- ✅ Recurring color values identified
- ✅ Font families and scales extracted
- ✅ Spacing patterns documented
- ✅ Component styles categorized

**Accuracy Check:**
- ✅ CSS syntax is valid in code snippets
- ✅ Variable references are correct
- ✅ Units are preserved (px, rem, em, %)
- ✅ Color formats are consistent

**Usability Check:**
- ✅ Style guide is readable and organized
- ✅ Usage notes provided for each category
- ✅ Code snippets are properly formatted
- ✅ Examples are clear and actionable

### 5. Flagging Issues and Gaps

The skill flags potential issues:

**Missing Information:**
- ⚠️ No CSS variables detected (all hard-coded values)
- ⚠️ Inconsistent color usage (many one-off values)
- ⚠️ No clear spacing system
- ⚠️ Limited component documentation

**Inconsistencies:**
- ⚠️ Multiple font families with no clear hierarchy
- ⚠️ Spacing values that don't follow a scale
- ⚠️ Shadow values with no pattern

**Recommendations:**
- 💡 Suggest consolidating colors into variables
- 💡 Recommend establishing spacing scale
- 💡 Propose standardizing component patterns

## Processing Script Requirements

The Python processing script (`extract_css_styles.py`) must:

### Input Handling
- Accept file path argument for CSS/HTML file
- Read and parse CSS content
- Handle CSS variables (`:root` declarations)
- Parse standard CSS selectors and rules

### Parsing Logic
- Use CSS parser library (e.g., `tinycss2`, `cssutils`, or regex)
- Extract color values (hex, rgb, rgba, hsl, hsla)
- Identify font-related properties
- Extract spacing values
- Parse shadow and border-radius declarations
- Categorize component-specific styles

### Output Generation
- Generate markdown using template structure
- Organize extracted data into appropriate sections
- Format code snippets with syntax highlighting
- Include usage notes and recommendations
- Add metadata (source, date, version)

### Error Handling
- Graceful handling of malformed CSS
- Warning messages for parsing issues
- Fallback for unrecognized patterns
- Logging of skipped/problematic selectors

## Dependencies

**Required Python Libraries:**
```bash
pip install tinycss2 markdown beautifulsoup4
```

**Optional (for enhanced parsing):**
- `cssutils` - Advanced CSS parsing
- `cssselect` - CSS selector matching
- `Pillow` - If generating color swatches

## Usage Examples

### Example 1: Extract from Website CSS

**User Request:**
> "I inspected motherduck.com and copied their CSS. Can you extract the style guide?"

**Workflow:**
1. User saves CSS to `data/inputs/css-extraction/motherduck__2025-11-14.css`
2. User runs skill: "Process the MotherDuck CSS and create a style guide"
3. Skill processes CSS and outputs `data/outputs/css-extraction/MotherDuck-Style-Guide__2025-11-14.md`
4. User reviews style guide and provides to pixel-perfect-designer agent

---

### Example 2: Batch Process Multiple Design Systems

**User Request:**
> "I have CSS files from 3 competitor sites I want to analyze and compare"

**Workflow:**
1. User saves files:
   - `competitor-a__2025-11-14.css`
   - `competitor-b__2025-11-14.css`
   - `competitor-c__2025-11-14.css`
2. User requests batch processing
3. Skill processes all files and generates 3 separate style guides
4. User compares color palettes, typography, spacing systems across competitors

---

### Example 3: Document Existing Design System

**User Request:**
> "We have a design system in CSS but no documentation. Extract the style guide from our codebase."

**Workflow:**
1. User exports compiled CSS from design system
2. Saves as `company-design-system__2025-11-14.css`
3. Skill processes and generates comprehensive documentation
4. User shares style guide with design and development teams

## Integration with Pixel-Perfect Designer Agent

The css-style-extractor skill is a **companion to the pixel-perfect-designer agent**. Typical workflow:

### Step 1: Extract Style (This Skill)
```
User: "Extract styles from Stripe's dashboard CSS"
→ Skill processes CSS
→ Outputs: Stripe-Dashboard-Style-Guide__2025-11-14.md
```

### Step 2: Use in Design Agent
```
User: "Launch pixel-perfect-designer agent in hi-fi mode.
Use the Stripe Dashboard style guide to create my analytics dashboard."
→ Agent reads style guide
→ Applies Stripe's design system to new project
→ Maintains pixel-perfect fidelity
```

This workflow ensures:
- **High-fidelity input** (real CSS, not screenshots)
- **Structured context** (organized style guide)
- **Consistent output** (agent follows extracted system)

## Output Template Reference

The skill uses the style guide template from:
```
agents/pixel-perfect-designer/templates/style-guide-template.md
```

This ensures consistency between:
- Extracted style guides (from this skill)
- Custom-created style guides (from pixel-perfect-designer agent)
- All design system documentation

## Best Practices

### For Users

1. **Provide Clean CSS:**
   - Use compiled/processed CSS (not raw SCSS with errors)
   - Remove commented-out code if possible
   - Ensure valid CSS syntax

2. **Name Files Descriptively:**
   - Include source name and date
   - Use consistent naming convention
   - Avoid special characters

3. **Review Generated Style Guides:**
   - Check for accuracy
   - Add context or usage notes if needed
   - Flag any misinterpretations

### For the Skill (Processing Logic)

1. **Prioritize CSS Variables:**
   - CSS variables indicate intentional design system
   - Hard-coded values may be one-offs
   - Group variables by prefix (`--color-*`, `--space-*`)

2. **Detect Patterns:**
   - Recurring values likely indicate system
   - One-off values may be exceptions
   - Scales (like 50, 100, 200) indicate thoughtful design

3. **Provide Context:**
   - Not just "what" but "when to use"
   - Examples of component usage
   - Recommendations for application

## Limitations

**This skill can:**
- ✅ Extract explicit CSS rules and variables
- ✅ Identify patterns in color, spacing, typography
- ✅ Generate structured documentation
- ✅ Organize styles into categories

**This skill cannot:**
- ❌ Understand design intent without context
- ❌ Generate visual mockups (use pixel-perfect-designer for that)
- ❌ Parse JavaScript-generated styles (must be static CSS)
- ❌ Extract styles from screenshots or images
- ❌ Interpret brand strategy or design philosophy

## Success Criteria

A successful extraction produces:
- ✅ Complete, well-organized style guide
- ✅ All major design tokens documented
- ✅ Reusable code snippets
- ✅ Clear usage guidelines
- ✅ Ready for integration with design agents or teams
- ✅ Accurate representation of source styles

## Related Tools

**Agents:**
- **pixel-perfect-designer** - Uses extracted style guides to generate UI
- **Product Designer / UX-UI Designer** - May reference style guides for design decisions

**Skills:**
- **brand-guidelines** - May integrate with extracted brand colors/typography
- **how-to-guide-writer** - Can document how to use the extracted design system

**External Tools:**
- **Browser DevTools** - Extract CSS from websites
- **Super Design Extension** - Advanced CSS extraction and style cloning
- **Twix CN** - Generate custom themes (alternative to extraction)

## Version History

- **v1.0** - Initial skill creation, companion to pixel-perfect-designer agent
