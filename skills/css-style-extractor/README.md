# CSS Style Extractor

Extract and parse CSS stylesheets into comprehensive, standardized style guide documentation.

## Overview

This skill transforms raw CSS files (from websites, design systems, or codebases) into structured markdown style guides that document:
- Color palettes
- Typography systems
- Spacing scales
- Shadow/elevation systems
- Border radius patterns
- Animation/transition specifications
- Component styles

## Quick Start

### 1. Obtain CSS

Extract CSS from a reference website:
1. Right-click on website → Inspect
2. Navigate to Sources or Network tab
3. Find and copy stylesheet content (`.css` files)
4. Save to `data/inputs/css-extraction/[source-name]__[date].css`

**Example:**
```
data/inputs/css-extraction/stripe-dashboard__2025-11-14.css
```

### 2. Run the Skill

From the repository root:
```bash
cd data/inputs/css-extraction
python ../../../skills/css-style-extractor/extract_css_styles.py stripe-dashboard__2025-11-14.css
```

Or specify output directory:
```bash
python skills/css-style-extractor/extract_css_styles.py \
  data/inputs/css-extraction/stripe-dashboard__2025-11-14.css \
  data/outputs/css-extraction
```

### 3. Review Generated Style Guide

Output location:
```
data/outputs/css-extraction/Stripe-Dashboard-Style-Guide__2025-11-14.md
```

The style guide will contain:
- All extracted CSS variables
- Organized color palette
- Typography system
- Spacing, shadows, border radius
- Component style examples

### 4. Use with Pixel-Perfect Designer Agent

```
User: "Launch pixel-perfect-designer agent. Use the Stripe Dashboard style guide
to create my analytics dashboard."
```

The agent will read the style guide and apply the design system to your project.

## Usage Scenarios

### Scenario 1: Replicate Competitor Design
**Goal:** Extract and replicate a competitor's design system

```bash
# 1. Extract their CSS
python extract_css_styles.py data/inputs/css-extraction/competitor__2025-11-14.css

# 2. Review style guide
cat data/outputs/css-extraction/Competitor-Style-Guide__2025-11-14.md

# 3. Use with pixel-perfect-designer agent to apply to your project
```

---

### Scenario 2: Document Existing Design System
**Goal:** Generate documentation for your own design system

```bash
# 1. Export your compiled CSS
# Save as: data/inputs/css-extraction/company-design-system__2025-11-14.css

# 2. Extract style guide
python extract_css_styles.py data/inputs/css-extraction/company-design-system__2025-11-14.css

# 3. Share style guide with team
```

---

### Scenario 3: Compare Multiple Design Systems
**Goal:** Analyze and compare 3 different design approaches

```bash
# Extract from all 3 sources
python extract_css_styles.py data/inputs/css-extraction/option-a__2025-11-14.css
python extract_css_styles.py data/inputs/css-extraction/option-b__2025-11-14.css
python extract_css_styles.py data/inputs/css-extraction/option-c__2025-11-14.css

# Review outputs side-by-side
# Compare color palettes, typography, spacing systems
```

## File Naming Conventions

### Input Files
```
[source-name]__[YYYY-MM-DD].css
[source-name]__[YYYY-MM-DD].html (if contains <style> tags)

Examples:
  motherduck__2025-11-14.css
  stripe-dashboard__2025-11-14.css
  figma-export__2025-11-14.css
```

### Output Files
```
[Source-Name]-Style-Guide__[YYYY-MM-DD].md

Examples:
  Motherduck-Style-Guide__2025-11-14.md
  Stripe-Dashboard-Style-Guide__2025-11-14.md
```

## What Gets Extracted

### CSS Variables (Priority)
The script prioritizes CSS custom properties:
```css
:root {
  --color-primary: #3b82f6;
  --space-4: 1rem;
  --shadow-md: 0 4px 6px rgba(0,0,0,0.1);
}
```

### Hard-Coded Values (Secondary)
Recurring hard-coded values are identified and documented:
- Colors that appear 2+ times
- Common spacing values
- Shadow patterns

### Component Styles
Common component classes are extracted:
- Buttons (`.btn`, `.button`)
- Inputs (`.input`, `.form-control`)
- Cards (`.card`, `.panel`)
- Navigation (`.nav`, `.menu`)

## Integration with Pixel-Perfect Designer

This skill is a **companion to the pixel-perfect-designer agent**.

### Workflow:

1. **Extract Style (this skill)**
   ```
   CSS file → extract_css_styles.py → Style Guide MD
   ```

2. **Design with Agent**
   ```
   Style Guide → pixel-perfect-designer agent → New UI Components
   ```

This ensures:
- High-fidelity input (real CSS, not screenshots)
- Structured context (organized documentation)
- Consistent output (agent follows extracted system)

## Dependencies

### Required Python Libraries
```bash
pip install tinycss2
```

### Optional (for enhanced parsing)
```bash
pip install cssutils beautifulsoup4
```

Currently, the script uses regex parsing (no external dependencies), but can be enhanced with dedicated CSS parsers.

## Output Structure

Generated style guides follow this structure:

```markdown
# [Source Name] Design System Style Guide

## Overview
- Version, date, source info

## Color Palette
- Primary, secondary, accent colors
- Neutrals/grays
- Semantic colors (success, error, warning, info)

## Typography
- Font families
- Type scale (sizes)
- Font weights
- Line heights

## Spacing System
- Base unit
- Spacing scale

## Shadows (Elevation)
- Shadow definitions by level

## Border Radius
- Rounding scale

## Animations & Transitions
- Timing functions
- Durations

## Component Styles
- Buttons, inputs, cards, navigation examples

## Notes
- Usage guidelines
- Integration recommendations
```

## Limitations

### Can Extract:
- ✅ CSS variables and hard-coded values
- ✅ Color, typography, spacing patterns
- ✅ Component style examples
- ✅ Animation/transition properties

### Cannot Extract:
- ❌ JavaScript-generated styles (must be static CSS)
- ❌ Styles from screenshots/images
- ❌ Design intent or brand strategy
- ❌ Visual mockups (use pixel-perfect-designer for that)

## Troubleshooting

### Issue: "No CSS variables detected"
**Cause:** The CSS file doesn't use `:root` or custom properties

**Solution:**
- The script will still extract hard-coded values
- Consider manually creating variables for recurring values
- Use hard-coded color/spacing patterns as guide

---

### Issue: "Very few styles extracted"
**Cause:** CSS might be minified or using preprocessor syntax

**Solution:**
- Ensure CSS is compiled/processed
- Pretty-print minified CSS before processing
- Remove commented-out code

---

### Issue: "Component styles not detected"
**Cause:** Components use non-standard class names

**Solution:**
- The script looks for `.btn`, `.card`, `.input`, etc.
- Manually review CSS for other component patterns
- Edit generated style guide to add custom components

## Version History

- **v1.0** - Initial release, companion to pixel-perfect-designer agent

## Related Tools

**Agents:**
- `pixel-perfect-designer` - Uses extracted style guides to generate UI

**Skills:**
- `brand-guidelines` - May integrate extracted brand colors
- `how-to-guide-writer` - Can document design system usage

**External Tools:**
- Browser DevTools - Extract CSS from websites
- Super Design Extension - Advanced CSS extraction
- Twix CN - Generate custom themes

## Contributing

To improve the extraction logic:
1. Edit `extract_css_styles.py`
2. Enhance parsing for specific CSS patterns
3. Add new categorization rules
4. Improve output formatting

## Support

For issues or questions:
- Review `SKILL.md` for detailed documentation
- Check generated style guide for accuracy
- Manually edit style guide to add context or fix errors
