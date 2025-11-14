# Visual Design Principles for Job Aids

This guide provides best practices for creating visually effective job aids that are easy to scan and use at point of need.

## Core Design Principles

### 1. Visual Hierarchy

**Purpose:** Guide the eye to the most important information first.

**Techniques:**
- **Size:** Larger text for critical information
- **Weight:** Bold for emphasis, regular for details
- **Color:** High-contrast for critical items, muted for supporting info
- **Position:** Top and left positions draw attention first
- **Grouping:** Related items close together with white space around groups

**Example Hierarchy:**
```
LARGE, BOLD TITLE (Most Important)
  Medium, Bold Subheading (Secondary)
    Regular body text (Supporting detail)
      Small text for notes (Least important)
```

### 2. White Space

**Purpose:** Reduce cognitive load and improve scannability.

**Guidelines:**
- Leave 20-30% of page as white space
- Create margins around edges (minimum 0.5" for print)
- Add space between distinct sections
- Don't try to fit too much on one page
- Empty space makes content feel less overwhelming

**Poor:** Cramming everything with no breathing room  
**Good:** Clear separation between sections with generous spacing

### 3. Consistency

**Purpose:** Build pattern recognition for faster comprehension.

**Apply Consistently:**
- Font families (1-2 max)
- Heading styles (H1, H2, H3)
- Color coding (same color = same type of info)
- Icon usage
- Spacing and alignment
- Bullet styles

**Example Color Coding:**
- 🔴 Red = Warnings, errors, don't do this
- 🟢 Green = Success, go ahead, approved
- 🟡 Yellow = Caution, review required
- 🔵 Blue = Information, FYI

### 4. Scannability

**Purpose:** Users should find info in under 30 seconds.

**Techniques:**
- Use descriptive headings that answer questions
- Start with most important info (inverted pyramid)
- Break text into short chunks (3-5 lines max per paragraph)
- Use bullets for lists, not long paragraphs
- Bold key terms that users will scan for
- Use tables for structured comparisons
- Add visual breaks (dividers, icons)

**Test:** Can someone get the key info by reading only the bolded text?

### 5. Visual Elements

**Purpose:** Accelerate understanding through visuals.

**Effective Use:**
- **Icons:** Quick visual recognition (⚠️ warning, ✅ success, ❌ avoid)
- **Color:** Categorize or show severity
- **Shapes:** Flowchart symbols for process steps
- **Borders/Boxes:** Group related information
- **Arrows:** Show direction or flow
- **Highlighting:** Draw attention to critical info

**Don't Overdo It:** Too many visual elements = visual clutter

## Typography Best Practices

### Font Selection

**Print Job Aids:**
- **Headings:** Arial, Helvetica, Calibri (sans-serif)
- **Body:** Georgia, Times New Roman (serif) OR same sans-serif as headings
- **Monospace:** Courier for code/technical data

**Digital Job Aids:**
- Stick to system fonts for universal rendering
- Sans-serif works best on screens
- Avoid decorative fonts entirely

### Font Sizing

**Minimum Sizes:**
- Body text: 11pt (print), 14px (digital)
- Headings: 16-24pt (print), 20-32px (digital)
- Fine print: 9pt minimum (for version info, footnotes)

**Line Height:**
- Set to 1.4-1.6x font size for readability
- More space between lines = easier to scan

**Line Length:**
- Ideal: 50-75 characters per line
- Too long = hard to track across page
- Too short = choppy reading experience

### Emphasis Techniques

**Recommended:**
- **Bold** for key terms and actions
- *Italic* for emphasis or technical terms (use sparingly)
- `Monospace` for system inputs, code, exact text

**Avoid:**
- UPPERCASE for entire sentences (only for short warnings)
- Underline (confusing with hyperlinks)
- Multiple types of emphasis together (bold + italic + underline)

## Color Usage

### Color Psychology

- **Red:** Danger, stop, error, critical
- **Orange:** Warning, caution
- **Yellow:** Attention needed, review
- **Green:** Success, go, approved, safe
- **Blue:** Information, neutral, professional
- **Gray:** Secondary info, disabled, unavailable
- **Purple:** Special status, premium
- **Black:** Text, formal, serious

### Accessibility

**Contrast Requirements:**
- Text: 4.5:1 contrast ratio minimum (WCAG AA)
- Large text: 3:1 contrast ratio minimum
- Test on a grayscale printer - text should still be readable

**Color Blindness Considerations:**
- Never use color alone to convey information
- Add icons, patterns, or labels alongside color
- Avoid red/green combinations as sole differentiators
- Test with colorblind simulation tools

**Examples:**
- ❌ Poor: "Green means approved, red means rejected" (color only)
- ✅ Good: "🟢 ✓ Approved" and "🔴 ✗ Rejected" (color + icon + text)

### Color Limitations

**Print Considerations:**
- Many users will print in black & white
- Test how your colors render in grayscale
- Use patterns or icons to differentiate when color is removed

**Recommendation:**
- Limit to 3-4 colors maximum per job aid
- Use shades/tints of the same color family

## Layout and Composition

### Grid System

**Benefits of Grids:**
- Consistent alignment
- Professional appearance
- Easier to scan
- Predictable layout

**Common Grids:**
- Single column (simple, linear reading)
- Two column (compare/contrast, before/after)
- Three column (tables, comparisons)

### Alignment

**Rules:**
- Pick left-aligned, centered, or right-aligned and stick with it
- Left-aligned is most scannable for text-heavy content
- Centered works for titles and callouts
- Right-aligned rarely used (maybe for dates or numbers)

**Avoid:**
- Mixing alignment styles within the same section
- Centered body paragraphs (hard to read)

### Balance

**Symmetrical Balance:**
- Same visual weight on both sides
- Formal, stable, traditional
- Good for: Policy documents, formal procedures

**Asymmetrical Balance:**
- Different but balanced visual weight
- Dynamic, modern, interesting
- Good for: Flowcharts, infographics, creative job aids

### Proximity

**Group related items together:**
- Items that belong together should be close
- Unrelated items should have more space between
- Creates visual relationships without explicit labels

## Flowchart Design

### Standard Flowchart Symbols

```
┌─────────┐
│Rectangle│ = Process/Action Step
└─────────┘

    ╱─────╲
   ╱Diamond╲ = Decision Point
   ╲       ╱
    ╲─────╱

┌───────────┐
│   Oval    │ = Start/End Point
└───────────┘

────────────→ = Flow Direction/Arrow

┌──────────────┐
│ Parallelogram│ = Input/Output (Data)
└──────────────┘

      ___
     /   \
    |Delay| = Delay/Wait
     \___/
```

### Flowchart Best Practices

**Flow Direction:**
- Top to bottom (most common)
- Left to right (also common)
- Avoid diagonal flows
- Never flow upward (confusing)

**Decision Points:**
- Always have exactly 2 or 3 exits
- Label each path (YES/NO, APPROVED/REJECTED)
- Use consistent exit positions (YES usually right or down)

**Keep It Simple:**
- Maximum 10-15 shapes per flowchart
- Break complex flows into multiple diagrams
- Use sub-process symbols for detailed sub-flows

**Text in Shapes:**
- Start with action verb in rectangles ("Review", "Submit")
- Use questions in diamonds ("Approved?", "Complete?")
- Keep text to 3-5 words per shape

## One-Page Design Strategy

**When space is limited:**

1. **Start with core content** - what MUST be included?
2. **Cut ruthlessly** - remove anything not essential
3. **Condense** - use tables instead of paragraphs
4. **Abbreviate** - if universally understood
5. **Reduce font size** - but not below minimums
6. **Use landscape** - more horizontal room for tables/charts
7. **Consider two-sided** - front and back counts as "one page"
8. **Link to details** - QR code or short URL to full documentation

**Example Priorities:**
- Must have: Critical steps, key contact, safety warnings
- Nice to have: Examples, tips, troubleshooting
- Can link to: Full procedures, background info, training

## Checklist Design

**Visual Treatment:**
- Large checkboxes (☐) or check marks (✓)
- Number steps if sequence matters
- Use bold for action items
- Regular text for context or notes

**Structure:**
- Group related items under headers
- Use indentation for sub-tasks
- Add brief clarifications in lighter text

**Example:**
```
☐ **Contact hiring manager** (Get approval before posting)
☐ **Prepare job description** 
  ☐ Include salary range
  ☐ List required qualifications
☐ **Submit requisition in myHR**
☐ **Notify recruiter** (hr.recruiting@example.com)
```

## Table Design

**Effective Tables:**
- Bold header row
- Alternate row shading (light gray every other row)
- Align numbers right, text left
- Keep columns narrow enough to scan
- Use vertical lines sparingly (or not at all)

**Poor Table:**
```
Messy, no alignment, hard to scan
```

**Good Table:**
```
| Column 1 | Column 2      | Column 3    |
|----------|---------------|-------------|
| Item A   | Description 1 | $1,000      |
| Item B   | Description 2 | $2,500      |
```

## Icons and Symbols

**Effective Icon Use:**
- Use universally recognized symbols
- Keep icon style consistent (all line art OR all solid)
- Size icons consistently
- Don't overuse - 3-5 different icons max per page

**Universal Icons:**
- ✅ Check mark = complete, approved, yes
- ❌ X mark = error, no, don't do this
- ⚠️ Triangle warning = caution
- 💡 Light bulb = tip, idea
- 📧 Envelope = email contact
- 📞 Phone = call contact
- 🔗 Chain link = hyperlink
- ℹ️ Info = additional information
- ⏱️ Clock = time-sensitive
- 👤 Person = user, employee

**Avoid:**
- Obscure symbols only you understand
- Too many different icon styles
- Icons without accompanying text

## Testing Your Design

### Usability Checklist

Test with real users:

- [ ] Can they find the key information in under 30 seconds?
- [ ] Do they understand the visual hierarchy?
- [ ] Are the steps clear and actionable?
- [ ] Is text readable from normal viewing distance?
- [ ] Does it work in black and white?
- [ ] Can it fit on one page without compromising readability?
- [ ] Is it obvious where to start?
- [ ] Are decision points clear?
- [ ] Is the language appropriate for the audience?
- [ ] Would they use this over asking someone?

### A/B Testing

**Create two versions:**
- Version A: Text-heavy with paragraphs
- Version B: Visual with tables, icons, bullets

**Measure:**
- Time to find information
- Task completion rate
- User preference
- Error rate

**Result:** Version B almost always wins for job aids

## Common Design Mistakes

❌ **Too much text** - Job aids should be scannable, not novel-length  
✅ Use bullets, tables, and visuals instead

❌ **Tiny fonts** - Trying to cram too much in  
✅ Cut content or use two pages

❌ **Random colors** - Using color without purpose  
✅ Use color strategically and consistently

❌ **No visual breaks** - One big wall of text  
✅ Add headings, spacing, dividers

❌ **Inconsistent formatting** - Different styles everywhere  
✅ Pick a pattern and stick to it

❌ **Too many fonts** - Different fonts for variety  
✅ Use 1-2 font families maximum

❌ **Cluttered layout** - No white space  
✅ Remove elements until it feels breathable

❌ **Poor contrast** - Light gray text on white  
✅ Use high contrast (black or dark gray on white)

## Tools and Resources

**Design Tools:**
- **Canva** - Templates for visual job aids
- **Lucidchart** - Professional flowcharts and diagrams
- **Microsoft Visio** - Advanced diagramming
- **Google Drawings** - Free, collaborative diagrams
- **Miro** - Whiteboard for process mapping

**Accessibility Testing:**
- **WebAIM Contrast Checker** - Test color contrast
- **Colorblind Simulator** - See how colorblind users see it
- **WAVE Tool** - Accessibility evaluation

**Typography Resources:**
- **Google Fonts** - Free, web-safe fonts
- **Font Squirrel** - Commercial-use free fonts

## Quick Reference: Design Do's and Don'ts

| **Do** | **Don't** |
|--------|-----------|
| ✅ Use white space generously | ❌ Cram every inch with content |
| ✅ Keep it to 1-2 pages | ❌ Create multi-page job aids |
| ✅ Use clear headings | ❌ Use vague labels like "Info" |
| ✅ Bold key actions | ❌ Bold entire paragraphs |
| ✅ Use consistent colors | ❌ Rainbow of random colors |
| ✅ Test in black & white | ❌ Rely solely on color |
| ✅ Use standard symbols | ❌ Create custom icons users won't know |
| ✅ Left-align text | ❌ Center body text |
| ✅ Use tables for data | ❌ Use paragraphs for lists |
| ✅ Number sequential steps | ❌ Bullet sequential steps |
