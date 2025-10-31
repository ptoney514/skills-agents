# UX Site Reviewer

Automated website UX auditor that captures screenshots, analyzes navigation, and identifies user experience friction points.

## What It Does

This agent performs comprehensive UX audits by:

1. **Capturing screenshots** using Playwright (desktop, tablet, mobile)
2. **Mapping site structure** and navigation patterns
3. **Analyzing user flows** for friction points
4. **Identifying issues** with button density, navigation, and information architecture
5. **Providing recommendations** with low-fidelity wireframe mockups

## When to Use

- You have a marketing site with UX issues (confusing navigation, too many buttons)
- You need an objective assessment before a redesign
- Users complain about not finding what they need
- You want to compare your site's UX to competitors
- You need a professional audit report for clients/stakeholders

## Quick Start

### 1. Install Playwright

```bash
npm install -D @playwright/test
npx playwright install chromium
```

### 2. Launch the Agent

In Claude Code, say:

```
I need a UX audit of https://mysite.com. Please use the ux-site-reviewer
agent from ~/Documents/Projects/skills-agents/agents/ux-site-reviewer/AGENT.md

Focus on:
- Homepage, about, and contact pages
- Navigation structure
- Top 5 friction points
```

### 3. Review the Report

The agent will deliver:
- Screenshot library organized by viewport
- Site structure map
- Prioritized findings (Critical, High, Medium, Low)
- Recommendations with low-fidelity wireframes
- Quick wins for immediate implementation

## Example Audits

### Example 1: "Too Many Buttons" Problem

**Your request:**
```
Our homepage has way too many buttons and links. Users don't know where to click.
Please audit https://example.com/home and propose a cleaner navigation.
```

**What you'll get:**
- Button/link count analysis (e.g., "42 clickable elements found - 3x industry average")
- Heatmap showing density issues
- Recommendation: "Reduce to 1 primary CTA, 2 secondary, move rest to footer"
- Low-fidelity wireframe showing simplified layout
- Implementation priority: "Quick win - high impact, low effort"

### Example 2: User Flow Analysis

**Your request:**
```
Users are abandoning our signup flow. Please analyze the journey from
homepage → signup → confirmation and identify friction points.
```

**What you'll get:**
- Flow diagram showing all steps
- Analysis: "5 clicks, 2 page loads, 12 form fields - 60% typical abandonment rate"
- Friction points identified:
  - "Step 2: Asking for phone number too early"
  - "Step 3: No progress indicator"
  - "Step 4: Error messages unclear"
- Recommendations with wireframes for each issue
- Proposed simplified flow (3 steps instead of 5)

### Example 3: Navigation Audit

**Your request:**
```
Our site navigation is confusing. We have a mega menu with 15 items and
users can't find key pages. Please audit and propose improvements.
```

**What you'll get:**
- Current navigation structure analysis
- Issue: "15 menu items exceeds cognitive load limit (7±2)"
- Issue: "Menu labels unclear ('Solutions' vs 'Products' vs 'Services')"
- Issue: "No visual hierarchy in mega menu"
- Proposed structure (7 items, grouped logically)
- Before/after wireframes
- Implementation effort: "Medium - requires information architecture work"

## Output Structure

```
ux-audit/
├── screenshots/
│   ├── desktop/
│   ├── tablet/
│   └── mobile/
├── scripts/
│   ├── capture-screenshots.js
│   └── analyze-navigation.js
├── reports/
│   └── ux-audit-report-2025-10-31.md
└── mockups/
    └── proposed-navigation.txt
```

## Typical Audit Report Sections

1. **Executive Summary**: Overall score, critical issues count, quick wins
2. **Site Structure**: Page map, navigation tree
3. **Findings by Page**: Issues organized by page and severity
4. **User Flow Analysis**: Key journeys mapped with friction points
5. **Recommendations**: Prioritized list with mockups
6. **Quick Wins**: High-impact, low-effort improvements to do first

## Scope

### Best For
- Marketing sites and landing pages
- Traditional multi-page websites (HTML/JS)
- Small business sites (5-50 pages)
- Content-focused sites with clear navigation

### Not For
- Heavy JavaScript SPAs (complex interaction testing)
- Mobile apps (iOS/Android) - use separate mobile agents
- Backend functionality or API testing
- Full WCAG accessibility audits (basic checks only)

## Configuration Options

**Thoroughness levels:**
- `quick`: Homepage + 2-3 key pages, top issues only (~30 min)
- `medium`: 5-8 pages, full 4-phase audit (~2 hours)
- `comprehensive`: Entire site, all flows, detailed mockups (~4+ hours)

**Focus areas:**
- Navigation structure
- Button/link density
- User flows (signup, checkout, contact)
- Mobile responsiveness
- Basic accessibility

## Tips for Best Results

1. **Be specific about pages**: List the exact pages you want audited
2. **Describe the problem**: "Users complain about X" gives context
3. **Define key user goals**: What should users be able to accomplish?
4. **Provide access**: Ensure site is publicly accessible or on localhost
5. **Share analytics**: "Users abandon at step 3" helps prioritize

## Follow-Up Actions

After receiving your audit:

1. **Review quick wins**: Implement high-impact, low-effort items first
2. **Validate findings**: Test hypotheses with real users if possible
3. **Prioritize by impact**: Focus on issues affecting key user goals
4. **Request detailed mockups**: If you need high-fidelity designs, use the [ui-ux-designer](../ui-ux-designer/AGENT.md) agent
5. **Schedule follow-up audit**: Re-audit after implementing changes to measure improvement

## Related Agents

- **[ui-ux-designer](../ui-ux-designer/AGENT.md)**: Use after the audit to create high-fidelity designs for recommendations
- **[design-review-specialist](../design-review-specialist/AGENT.md)**: For focused design critiques of specific components
- **[react-stack-reviewer](../react-stack-reviewer/AGENT.md)**: For reviewing implementation code of UX improvements

## Real-World Use Cases

### Use Case 1: Pre-Redesign Assessment
**Scenario**: You're planning a site redesign and need to document current issues.

**Request**: "Audit our current site at https://old.site.com. We're redesigning and need to understand what's not working."

**Outcome**: Comprehensive documentation of current state, prioritized list of issues to address in redesign, screenshot archive for reference.

### Use Case 2: Conversion Optimization
**Scenario**: Your signup conversion rate is low and you don't know why.

**Request**: "Analyze our signup flow from https://app.com/signup. Users drop off at 60% rate."

**Outcome**: Detailed flow analysis showing exactly where users are dropping off, specific friction points identified, recommendations with A/B test ideas.

### Use Case 3: Client Deliverable
**Scenario**: You're a consultant and need to deliver a professional UX audit to a client.

**Request**: "Full audit of client site https://client.com. Need professional report with executive summary and prioritized recommendations."

**Outcome**: Publication-ready audit report with screenshots, findings organized by severity, ROI estimates for each recommendation.

### Use Case 4: Competitive Analysis
**Scenario**: You want to understand how your site compares to competitors.

**Request**: "Audit our site and compare navigation structure to competitors at competitor1.com and competitor2.com."

**Outcome**: Comparative analysis showing where you're behind/ahead, specific areas to improve based on competitive benchmarks.

## Sample Wireframe Output

The agent creates low-fidelity mockups like this:

```
Current Homepage (42 clickable elements):
┌─────────────────────────────────────────────────┐
│ Logo  [Products▼] [Solutions▼] [Resources▼]    │
│       [About] [Blog] [Contact] [Login] [Signup] │
├─────────────────────────────────────────────────┤
│                                                 │
│  Headline with 5 inline text links              │
│                                                 │
│  [CTA 1] [CTA 2] [CTA 3] [CTA 4]                │
│  [Learn More] [Watch Demo] [Get Started]        │
│                                                 │
│  ← 15 product cards, each with 3 buttons →     │
│                                                 │
└─────────────────────────────────────────────────┘
ISSUE: Choice overload, unclear primary action

Proposed Simplification (12 clickable elements):
┌─────────────────────────────────────────────────┐
│ Logo  Products  Solutions  Resources  [Login]   │
├─────────────────────────────────────────────────┤
│                                                 │
│  Clear Headline                                 │
│  Supporting text without inline links           │
│                                                 │
│  [Primary CTA - Get Started]                    │
│  [Secondary - Learn More]                       │
│                                                 │
│  ← 3 key product cards, single "View" link →   │
│                                                 │
│  [All Products →]                               │
│                                                 │
└─────────────────────────────────────────────────┘
IMPROVEMENT: Single clear primary action, reduced choice
```

## Frequently Asked Questions

**Q: How long does an audit take?**
A: Quick audit (3-5 pages): 30-60 minutes. Full audit (10+ pages): 2-4 hours.

**Q: Can it audit authenticated pages?**
A: Yes, but you'll need to provide login credentials or session cookies for Playwright.

**Q: Does it work on localhost?**
A: Yes! Great for auditing sites before launch.

**Q: What if my site is built with React/Next.js?**
A: Works fine. The agent captures the rendered output, not the code itself.

**Q: Can it audit mobile apps?**
A: No, this agent is for websites only. Mobile apps need a separate mobile-specific agent.

**Q: How detailed are the wireframes?**
A: Low-fidelity (ASCII or simple HTML). For high-fidelity mockups, use the [ui-ux-designer](../ui-ux-designer/AGENT.md) agent.

**Q: Does it provide accessibility scores?**
A: Basic checks only (contrast, touch targets, labels). For full WCAG audit, use a specialized accessibility agent.

## Version History

- **1.0.0** (2025-10-31)
  - Initial release
  - Playwright automation for screenshots
  - 4-phase audit methodology
  - Low-fidelity wireframe mockups
  - Support for marketing sites and traditional web

## Contributing

Found a way to improve this agent?

1. Edit [AGENT.md](./AGENT.md)
2. Test your changes on a real site audit
3. Update version number and this README
4. Commit with descriptive message: `git commit -m "Improve ux-site-reviewer: [what you changed]"`
5. Push to GitHub

## License

Part of the skills-agents repository. Free to use and modify for your projects.
