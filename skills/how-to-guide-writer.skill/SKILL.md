---
name: how-to-guide-writer
description: Create user-friendly how-to guides, software tutorials, and end-user documentation. Use when users need help creating step-by-step guides for software applications, training materials, user manuals, or visual documentation with screenshots. Optimized for Notion and PDF export.
---

# How-To Guide Writer

Create clear, visual, user-friendly documentation that helps end-users successfully complete tasks in software applications.

## When to Use This Skill

Use this skill when users request:
- Software how-to guides or tutorials
- End-user training documentation
- Step-by-step system navigation guides
- User manuals for internal applications
- Quick reference guides for software tasks
- Process documentation with heavy UI/screenshot focus
- Documentation intended for Notion → PDF export

## How This Differs from SOPs

**How-To Guides:**
- Focus: Teaching users how to use software/systems
- Tone: Friendly, helpful, conversational
- Structure: Quick reference + detailed steps
- Visual: Heavy use of screenshots and callouts
- Audience: End-users of varying skill levels
- Purpose: Enable self-service and reduce support tickets

**SOPs (Standard Operating Procedures):**
- Focus: Standardizing business processes for compliance
- Tone: Formal, authoritative
- Structure: Formal sections with roles/approvals
- Visual: Screenshots used sparingly
- Audience: Employees performing regulated tasks
- Purpose: Ensure consistency and meet audit requirements

## Core Workflow

### 1. Understand the Task

Before writing, gather key information:

**Essential Questions:**
- What task or process are you documenting?
- What system/software is being used?
- Who is the target audience? (new users, experienced users, specific role)
- What is the user trying to accomplish?
- What are common pain points or confusion areas?
- Are there existing materials or screenshots available?

**Scope Definition:**
- Where does the user start (e.g., "Log in to myHR")?
- What is the successful end state?
- What prerequisites must be in place?
- What should NOT be included in this guide?

### 2. Choose the Appropriate Format

Select template based on task complexity and user needs:

**Software Navigation Guide** (`assets/software-navigation-template.md`)
- **Use for:** Multi-step processes in web applications or software
- **Includes:** Quick reference, detailed steps with screenshots, tips & FAQs
- **Best for:** Most end-user how-to guides
- **Typical length:** 5-15 pages
- **Example:** "How to Create a Job Requisition in myHR"

**Quick Reference Card** (`assets/quick-reference-card-template.md`)
- **Use for:** Simple, frequently-performed tasks
- **Includes:** Condensed steps, minimal explanations
- **Best for:** Experienced users who need a reminder
- **Typical length:** 1-2 pages
- **Example:** "Quick Reference: Submitting a Time-Off Request"

**Visual Tutorial Guide** (`assets/visual-tutorial-template.md`)
- **Use for:** Complex tasks requiring extensive visual guidance
- **Includes:** Screenshot for nearly every step, annotations
- **Best for:** New users or complex interfaces
- **Typical length:** 10-20 pages
- **Example:** "Complete Guide to Using the New Expense System"

**Troubleshooting Guide** (`assets/troubleshooting-template.md`)
- **Use for:** Problem-solving and error resolution
- **Includes:** Problem/solution pairs, decision trees
- **Best for:** Support teams and self-service knowledge base
- **Typical length:** 3-8 pages
- **Example:** "Troubleshooting Login Issues in Workday"

### 3. Write Clear, User-Friendly Steps

Follow these principles when writing steps:

**Action-Oriented Language:**
- Start each step with an action verb (Click, Select, Enter, Navigate to, Open)
- Be specific about UI elements: "Click the **Save and Close** button" not "Save your work"
- Use bold for all UI elements: buttons, tabs, menu items, field names
- One primary action per step

**Progressive Disclosure:**
- Start with a "Quick Reference" section (5-10 condensed steps)
- Follow with "Detailed Instructions" (full step-by-step with context)
- This serves both quick scanners and first-time users

**Visual Indicators:**
- Mark screenshot locations with: `[Screenshot: Description of what to show]`
- Use callout boxes for warnings, tips, and notes
- Include arrows or annotations in screenshots when helpful

**User Context:**
- Explain WHY when it helps understanding: "Click Continue to send the requisition to your recruiter for review"
- State expected outcomes: "You should see a green confirmation message"
- Anticipate confusion: "Don't see the Positions option? Contact HR at hr@example.com"

### 4. Structure Your Guide

**Standard How-To Guide Structure:**

1. **Title Section**
   - Clear, task-focused title
   - Audience indicator (e.g., "For Hiring Managers")
   - Brief purpose statement

2. **Purpose & Prerequisites**
   - What this guide helps you accomplish
   - What you need before starting (access, info, approvals)

3. **Quick Reference** (Steps Overview)
   - 5-10 condensed steps
   - Links to detailed sections
   - For users who've done this before

4. **Detailed Instructions**
   - Full step-by-step walkthrough
   - Screenshots with callouts
   - Sub-steps where needed
   - Expected results for major steps

5. **Tips, Reminders & FAQs**
   - Common questions answered
   - Helpful shortcuts or tips
   - Links to related guides

6. **Troubleshooting**
   - Common problems and solutions
   - When to contact support
   - Support contact information

7. **Related Resources** (Optional)
   - Links to related guides
   - Additional training materials

### 5. Visual Design Guidance

**Screenshot Best Practices:**
- Capture at consistent resolution (1920x1080 recommended)
- Crop to show only relevant interface areas
- Use annotations sparingly (arrows, boxes, numbers)
- Keep screenshots up-to-date with current UI
- Place screenshots immediately after the step they illustrate

**Notion-Specific Formatting:**
- Use callout blocks for warnings, notes, and tips
- Use toggle blocks for optional/advanced content
- Use dividers to separate major sections
- Use column layouts for side-by-side comparisons
- Use emojis strategically for visual scanning:
  - 🔹 for main headers
  - ⚠️ for important warnings
  - 💡 for tips
  - ✅ for success indicators
  - ❌ for things to avoid

**Callout Types:**
- ⚠️ **IMPORTANT:** Critical information users must know
- 💡 **TIP:** Shortcuts or efficiency improvements
- 📝 **NOTE:** Additional helpful context
- ✅ **SUCCESS:** What success looks like
- ❌ **AVOID:** Common mistakes to prevent

### 6. Quality Checklist

A high-quality how-to guide should:
- ✅ Have a clear, task-oriented title
- ✅ Include both quick reference and detailed steps
- ✅ Use bold formatting for all UI elements
- ✅ Mark screenshot placements clearly
- ✅ Anticipate common questions and confusion
- ✅ Provide specific, actionable steps
- ✅ Include troubleshooting for common issues
- ✅ Be scannable (headings, bold, short paragraphs)
- ✅ Maintain a friendly, helpful tone
- ✅ Include support contact information

## Notion → PDF Export Considerations

When creating guides for Notion export to PDF:

**Formatting That Works Well:**
- Headings (H1, H2, H3) - maintains hierarchy
- Bold and italic text - preserves emphasis
- Numbered and bulleted lists - exports cleanly
- Callout blocks - exports with background color
- Dividers - creates visual separation
- Tables - maintains structure
- Emojis - adds visual interest

**Formatting to Avoid:**
- Inline databases - may not export well
- Complex multi-column layouts - can break in PDF
- Embedded content - may lose interactivity
- Toggle blocks - exports in open state (plan accordingly)

**PDF Optimization Tips:**
- Keep pages to reasonable length (10-15 pages ideal)
- Test PDF export before finalizing
- Add page breaks intentionally with dividers
- Use consistent heading levels for auto table of contents

## Writing Style Guide

**Do:**
- ✅ Write in second person ("You will see..." or imperative "Click the button")
- ✅ Use active voice ("Select the option" not "The option should be selected")
- ✅ Keep sentences short and simple
- ✅ Use numbered lists for sequential steps
- ✅ Use bullet points for non-sequential items or lists of things
- ✅ Define acronyms on first use
- ✅ Be conversational but professional

**Don't:**
- ❌ Use vague terms like "simply," "just," or "easy"
- ❌ Assume knowledge ("As you know...")
- ❌ Skip "obvious" steps
- ❌ Use jargon without explanation
- ❌ Write long, complex sentences
- ❌ Use passive voice

## Examples of Good vs. Poor Steps

❌ **Poor:** "Go to the system and create a requisition"
✅ **Good:** "Navigate to **My Team** > **Positions**, then click the **3-dots menu** next to the position you want to fill"

❌ **Poor:** "Fill out the form properly"
✅ **Good:** "Complete the required fields marked with an asterisk (*): Business Unit, Position, Number of Openings, and Hiring Manager"

❌ **Poor:** "If you have problems, get help"
✅ **Good:** "If you don't see the **Positions** option, contact HR for support at hr@creighton.edu"

❌ **Poor:** "Make sure it's correct before continuing"
✅ **Good:** "Verify the following before clicking **Save and Close**: recruiter is selected, business justification is complete, and fund/org codes are correct"

## Version Control & Maintenance

**Document Metadata to Include:**
- Document title and version (e.g., "v1.2")
- Last updated date
- Document owner/maintainer
- Audience (who should use this)

**When Updating:**
- Note what changed in the document or file name
- Update all affected screenshots
- Test the entire process again
- Consider if users need notification of changes

**Maintenance Schedule:**
- Review quarterly for UI changes
- Update when process changes
- Refresh screenshots annually or when UI updates
- Collect user feedback and iterate

## Deliverable

Create the complete guide as a markdown file ready for Notion import. Include:
- All sections properly structured
- Screenshot placement markers (since actual screenshots will be added in Notion)
- Proper formatting with bold, bullets, and callouts
- Complete troubleshooting section
- All necessary metadata

The guide should be immediately usable and require only screenshot insertion to be complete.

## Additional Resources

See these files for templates and examples:
- `assets/software-navigation-template.md` - Full how-to guide structure
- `assets/quick-reference-card-template.md` - Condensed format
- `assets/visual-tutorial-template.md` - Screenshot-heavy format
- `assets/troubleshooting-template.md` - Problem/solution format
- `examples/job-requisition-guide.md` - Real-world example from uploaded PDF
- `references/notion-formatting-guide.md` - Notion-specific tips
- `references/screenshot-guidelines.md` - Visual documentation best practices
