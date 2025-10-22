# Notion Formatting Guide for How-To Documentation

## Overview

This guide helps you format how-to guides in Notion for optimal user experience and clean PDF export.

---

## Markdown Basics

Notion supports standard markdown with some enhancements:

### Headers

```
# H1 - Main Title (use once at top)
## H2 - Major Sections
### H3 - Subsections
```

**Best practices:**
- Use H1 only for document title
- Use H2 for main steps or major sections
- Use H3 for sub-steps or detailed breakdowns
- Don't skip heading levels (H1 → H3)

---

## Text Formatting

| Format | Markdown | Shortcut (Mac) | Shortcut (Windows) |
|--------|----------|----------------|-------------------|
| **Bold** | `**text**` | Cmd + B | Ctrl + B |
| *Italic* | `*text*` | Cmd + I | Ctrl + I |
| ~~Strikethrough~~ | `~~text~~` | Cmd + Shift + S | Ctrl + Shift + S |
| `Code/Monospace` | \`text\` | Cmd + E | Ctrl + E |
| [Link](url) | `[text](url)` | Cmd + K | Ctrl + K |

**When to use each:**
- **Bold**: UI elements (buttons, menus, field names), emphasis
- *Italic*: Rarely needed; use sparingly for mild emphasis
- `Code`: System paths, file names, commands, exact text to type
- Links: Related guides, external resources

---

## Lists

### Numbered Lists (Sequential Steps)

```
1. First step
2. Second step
3. Third step
```

**Use for:** Any sequential process where order matters

**Tips:**
- Start action-oriented sentences with verbs
- Keep one main action per numbered item
- Use sub-bullets under numbered items for details

### Bulleted Lists (Non-Sequential Items)

```
- Item one
- Item two
- Item three
```

**Use for:** Prerequisites, checklists, feature lists, tips

---

## Callout Blocks

Callouts are Notion's superpower for how-to guides!

### Creating Callouts

1. Type `/callout` or click + → Callout
2. Choose an emoji icon
3. Change background color if desired
4. Add your content

### Standard Callout Types

**⚠️ Important/Warning** (Red or Yellow background)
- Critical information users must know
- Potential data loss or security risks
- Common mistakes that cause major problems

**💡 Tip** (Light blue or green background)
- Helpful shortcuts
- Efficiency improvements
- Pro user techniques

**📝 Note** (Gray or light background)
- Additional context
- Explanations of "why"
- Helpful but not critical information

**✅ Success Indicator** (Green background)
- What success looks like
- Expected outcomes
- Confirmation messages users should see

**❌ Avoid** (Red background)
- Common mistakes
- Things not to do
- Pitfalls to watch for

### Callout Best Practices

- Use 2-4 callouts per page maximum
- Don't nest callouts within callouts
- Keep callout text concise (2-3 sentences)
- Use emojis consistently across documents

---

## Tables

Tables are great for:
- Field definitions
- Required vs optional items
- Comparison charts
- Troubleshooting quick reference

### Creating Tables

1. Type `/table` or click + → Table
2. Add columns and rows as needed
3. Use header row for column titles

### Table Formatting Tips

```
| Field Name | Description | Required? |
|------------|-------------|-----------|
| **Email*** | User's email address | Yes |
| **Phone** | Contact number | No |
```

**Best practices:**
- Bold the column headers
- Keep tables simple (max 4-5 columns)
- Use asterisks (*) to indicate required fields
- Align text left for readability

---

## Dividers

Use dividers to create visual breaks between sections.

**How to add:** Type `---` or `/divider`

**When to use:**
- Between major sections
- Before and after important callouts
- To create "page breaks" for PDF export
- Before support/contact information

---

## Toggle Blocks

Toggles are collapsible sections - useful for optional or advanced content.

### Creating Toggles

1. Type `/toggle` or click + → Toggle list
2. Add title text
3. Add content inside the toggle

### When to Use Toggles

✅ **Good uses:**
- Advanced/optional steps
- Detailed explanations for interested users
- "Why this matters" sections
- FAQs (each question as a toggle)

❌ **Avoid for:**
- Required steps (users might miss them)
- Critical warnings
- Anything essential to task completion

**PDF Export Note:** Toggles export in the OPEN state, so plan your content accordingly!

---

## Emojis for Visual Scanning

Emojis help users scan documents quickly. Use them strategically:

### Recommended Emojis

- 🔹 Main section headers
- ✅ Success indicators, completed steps, verification checkboxes
- ⚠️ Warnings and important notices
- 💡 Tips and helpful hints
- 📝 Notes and additional information
- ❌ Things to avoid, errors, problems
- 🔴 Problems in troubleshooting guides
- 📧 Contact information
- 📞 Phone numbers
- 🎯 Goals or objectives
- ⏱️ Time estimates or deadlines
- 📊 Data or reports
- 🔐 Security or access related items
- 🖼️ When indicating screenshot placement

### Emoji Best Practices

- Use consistently across all documents
- Don't overuse (3-5 types per document max)
- Stick to common, universally understood emojis
- Test how they look in PDF export

---

## Code Blocks

For showing commands, code, or formatted text examples:

### Inline Code

Use backticks for short commands: `command here`

### Code Blocks

```
Type /code or click + → Code
Select language for syntax highlighting
```

**When to use:**
- Commands to copy/paste
- File paths
- Configuration examples
- Error messages (exact text)

---

## Columns (Multi-Column Layouts)

### Creating Columns

1. Add a block
2. Click the ⋮⋮ handle and drag left/right
3. Drop next to another block

### When to Use Columns

✅ **Good for:**
- Before/after comparisons
- Side-by-side screenshots
- Do's and Don'ts lists

⚠️ **PDF Export Warning:**
- Columns can break awkwardly in PDFs
- Keep column content short
- Test PDF export before finalizing
- Consider using tables instead for complex layouts

---

## Images & Screenshots

### Adding Images

1. Type `/image` or drag/drop image file
2. Resize by dragging corners
3. Add caption below if needed

### Screenshot Best Practices

**File format:**
- PNG for screenshots (better quality, transparency)
- JPG for photos (smaller file size)

**Resolution:**
- Capture at 1920x1080 (standard HD)
- Don't enlarge images beyond original size
- Notion auto-optimizes on upload

**Annotations:**
- Add arrows, boxes, or numbers BEFORE uploading
- Use consistent colors (red for attention, green for success)
- Don't over-annotate - show only what matters

**Captions:**
- Add brief descriptive captions when helpful
- Not needed if screenshot is obvious from context

**Placement:**
- Put screenshots IMMEDIATELY after the step they illustrate
- Don't separate screenshots from their related text

---

## Page Organization

### Table of Contents

Notion can auto-generate a table of contents:

1. Type `/toc` or `/table of contents`
2. It automatically links to all headers on the page

**Use for:** Longer guides (10+ pages)

### Breadcrumbs

Add navigation at the top:

```
Home > [Category] > [Current Guide]
```

### Related Links Section

At the bottom of guides, include:

```
## Related Guides
- [Link to related guide 1]
- [Link to related guide 2]
- [Link to related guide 3]
```

---

## PDF Export Optimization

### Before Exporting

- [ ] Check all screenshots display correctly
- [ ] Test that tables fit on page width
- [ ] Verify toggle blocks contain what you want visible
- [ ] Review heading hierarchy (H1, H2, H3)
- [ ] Check that dividers create appropriate breaks
- [ ] Remove any draft/internal comments

### Export Settings

**Recommended export settings:**
- Format: PDF
- Include content: All blocks
- Paper size: Letter or A4
- Scale: Fit to page width

### Post-Export Checks

- Open the PDF and spot-check:
  - Header hierarchy and bookmarks
  - Screenshot clarity
  - Table formatting
  - Page breaks in reasonable places
  - No cut-off content

---

## Notion-Specific Features That DON'T Export Well

Avoid or plan around these:

❌ **Databases** (inline or full-page)
- Exports as static table, loses filtering/sorting
- Consider taking screenshots of database views instead

❌ **Linked Databases**
- May not export at all
- Use simple tables instead

❌ **Synced Blocks**
- Only shows content once
- Plan accordingly

❌ **Embedded Content** (YouTube, Twitter, etc.)
- Shows as link only in PDF
- Include screenshot if visual is important

❌ **Comments**
- Don't export
- Resolve or incorporate before exporting

---

## Template Checklist

Use this checklist when creating new how-to guides:

- [ ] Document title with clear task name
- [ ] Audience clearly stated
- [ ] Purpose section (why this guide exists)
- [ ] Prerequisites listed
- [ ] Quick reference section for experienced users
- [ ] Detailed step-by-step with screenshots
- [ ] All UI elements in **bold**
- [ ] Callout blocks for tips, warnings, notes
- [ ] Troubleshooting section
- [ ] Support contact information
- [ ] Related resources
- [ ] Last updated date and version number
- [ ] Tested PDF export

---

## Accessibility Considerations

Make your guides accessible:

- ✅ Use descriptive link text (not "click here")
- ✅ Provide alt text for complex diagrams
- ✅ Use sufficient color contrast
- ✅ Maintain logical heading hierarchy
- ✅ Don't rely solely on color to convey information
- ✅ Keep sentences and paragraphs short
- ✅ Define acronyms on first use

---

## Style Consistency

### Document-Level Consistency

Within each guide, be consistent with:
- Bold formatting for UI elements
- Emoji usage for callouts
- Heading capitalization (Title Case or Sentence case)
- Screenshot size and placement
- Table formatting

### Organization-Level Consistency

Across all guides in your organization:
- Use the same templates
- Apply the same emoji conventions
- Follow the same naming conventions
- Maintain the same tone and voice
- Use consistent support contact information

---

## Common Formatting Mistakes

### ❌ Don't Do This

**Over-formatting:**
- Too many colors and font sizes
- Excessive bold and italic
- Emoji overload

**Inconsistent structure:**
- Mixing H2 and H3 without pattern
- Random screenshot placement
- Varying callout styles

**Poor spacing:**
- Walls of text without breaks
- Too many empty lines
- Cramped layouts

### ✅ Do This Instead

**Clean formatting:**
- Limited, purposeful formatting
- Bold for UI elements only
- Strategic emoji use

**Consistent structure:**
- Logical heading hierarchy
- Screenshots after relevant steps
- Standard callout types

**Good spacing:**
- Short paragraphs (2-4 lines)
- Appropriate white space
- Visual breathing room

---

## Version Control in Notion

**Version history:**
- Notion auto-saves version history
- Access via ... menu → Page history
- Can restore previous versions

**Best practices:**
- Add version number to document title
- Include "Last Updated" date at bottom
- Track major changes in a revision table
- Export to PDF with each version for archive

---

*Last Updated: October 2025*  
*For questions about Notion formatting, consult Notion's official help docs*
