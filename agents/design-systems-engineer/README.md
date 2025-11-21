# Design Systems Engineer Agent

A specialized AI agent for building professional design systems that bridge design and development.

---

## What Does This Agent Do?

This agent helps you:

- 🎨 **Build design systems from scratch** - Complete design-to-code workflows
- 🧩 **Create component libraries** - Using shadcn/ui and Tailwind CSS
- 🎯 **Ensure design-code consistency** - Pixel-perfect implementation from Figma
- ♿ **Maintain accessibility standards** - WCAG AA compliance
- 📚 **Generate documentation** - Component APIs, usage guides, best practices
- 🔧 **Work with or without MCPs** - Flexible workflows for any setup

---

## When to Use This Agent

### Perfect For:

✅ **Client Projects**
- Building branded design systems for clients
- Translating brand guidelines into reusable components
- Creating professional component libraries
- Providing handoff documentation for client dev teams

✅ **Personal Projects**
- Establishing consistent UI patterns across your projects
- Building reusable component libraries for rapid prototyping
- Implementing professional-quality designs efficiently

### Use Cases:

- "I need to build a design system for a healthcare client with their brand colors"
- "Help me create a consistent component library for my SaaS product"
- "Translate this Figma design into a production-ready React component library"
- "Audit my existing components and consolidate them into a proper design system"
- "Set up shadcn/ui with custom design tokens for my project"

---

## How to Use This Agent

### Method 1: Task Tool (Recommended)

From any Claude Code session:

```
I need help building a design system. Can you use the design-systems-engineer agent
from agents/design-systems-engineer/AGENT.md?
```

Claude will read the agent instructions and operate with that expertise.

### Method 2: Direct Reference

```
Please read and follow the instructions in agents/design-systems-engineer/AGENT.md
while helping me build my design system.
```

### Method 3: Copy to Project

For long-term projects, copy the agent to your project's `.claude/` directory:

```bash
cp -r agents/design-systems-engineer /path/to/your/project/.claude/agents/
```

Then reference it in project context.

---

## What You'll Get

### Deliverables

When you work with this agent, you'll receive:

1. **Design Token System**
   - Configured `tailwind.config.js` with your brand tokens
   - Color palettes, typography scales, spacing systems
   - Documentation on token usage

2. **Component Library**
   - Production-ready React components with TypeScript
   - shadcn/ui components customized to your design system
   - Composite components built from primitives

3. **Documentation**
   - Component API reference
   - Usage guidelines and examples
   - Design-to-code mapping document
   - Contribution guidelines (for teams)

4. **Testing & Quality**
   - Accessibility compliance (WCAG AA)
   - Responsive design (mobile, tablet, desktop)
   - Type-safe TypeScript interfaces

5. **Showcase Page**
   - Interactive component gallery
   - Live examples with variants
   - Copy-paste code snippets

---

## Example Workflows

### Example 1: New Client Project

**You:** "I have a new client project. They have brand guidelines with specific colors and fonts. Help me build a design system."

**Agent will:**
1. Ask for brand guidelines (colors, fonts, logo, style)
2. Extract design tokens and create `tailwind.config.js`
3. Set up shadcn/ui with customized components
4. Build branded buttons, forms, cards, etc.
5. Create component showcase page
6. Provide handoff documentation

**Time:** 1-2 hours for core design system foundation

---

### Example 2: Personal Project UI Library

**You:** "I want to build a consistent design system for all my personal projects. Something modern and minimal."

**Agent will:**
1. Propose color palette and typography
2. Set up Tailwind with design tokens
3. Install essential shadcn/ui components
4. Customize for modern, minimal aesthetic
5. Create reusable patterns you can use across projects

**Time:** 30-60 minutes for essential components

---

### Example 3: Figma to Code Translation

**You:** "I have a Figma design. Help me translate it into a React component library."

**Agent will:**
1. Analyze Figma design tokens (if MCP available) or ask for specs
2. Extract colors, fonts, spacing, components
3. Create matching Tailwind config
4. Build components to match Figma pixel-perfectly
5. Ensure design-code consistency

**Time:** Varies by design complexity

---

## Prerequisites

### Required
- React project with TypeScript
- Tailwind CSS installed
- Node.js and npm/pnpm

### Optional (Enhances Experience)
- Figma MCP (for direct Figma integration)
- shadcn/ui MCP (for easier component installation)
- Storybook (for component documentation)

**Note:** This agent works effectively with or without MCPs!

---

## Tech Stack

This agent specializes in:

- **Framework:** React with TypeScript
- **Styling:** Tailwind CSS (utility-first)
- **Components:** shadcn/ui + Radix UI primitives
- **Design Tool:** Figma (optional)
- **Documentation:** Storybook (optional)
- **Testing:** React Testing Library, jest-axe

---

## MCP Setup (Optional)

See [MCP_SETUP.md](./MCP_SETUP.md) for instructions on installing:
- Figma MCP - Direct Figma file manipulation
- shadcn/ui MCP - Streamlined component installation

**The agent works without MCPs**, but they enhance the workflow.

---

## Common Questions

### Q: Can this agent work with Vue or Svelte?
**A:** This agent specializes in React. For other frameworks, you'd need a different agent or adjust the workflow.

### Q: What if I don't have Figma?
**A:** The agent can work without Figma by having you describe your design vision or provide brand guidelines. It will create design tokens and components based on your specifications.

### Q: Can I use this for existing projects?
**A:** Yes! The agent can audit existing components, identify inconsistencies, and help refactor into a proper design system.

### Q: Do I need to know Tailwind or shadcn/ui?
**A:** No. The agent will handle the technical implementation. You just need to describe what you want visually.

### Q: How long does it take to build a design system?
**A:** Depends on scope:
- **Basic foundation** (tokens + 5-10 components): 1-2 hours
- **Medium system** (tokens + 20-30 components + docs): 4-6 hours
- **Complete system** (everything + Storybook + tests): 1-2 days

### Q: Can this agent maintain my design system over time?
**A:** Yes! You can invoke it for updates, new components, audits, and ensuring design-code consistency.

---

## Tips for Best Results

1. **Be specific about your brand** - Share colors, fonts, personality, examples
2. **Prioritize components** - Start with what you need most (buttons, forms, etc.)
3. **Provide examples** - Show websites or apps with aesthetics you like
4. **Think in systems** - Consider how components relate and combine
5. **Iterate** - Start with foundation, then expand

---

## Agent Location

```
agents/design-systems-engineer/
├── AGENT.md              # Agent instructions (the brain)
├── README.md             # This file
├── MCP_SETUP.md          # MCP installation guide
├── examples/
│   ├── figma-to-code.md      # Example workflow
│   ├── client-project.md     # Client project example
│   └── personal-library.md   # Personal library example
└── templates/
    ├── tailwind.config.js    # Tailwind config template
    ├── component-template.tsx # Component template
    └── design-tokens.md      # Design token template
```

---

## Need Help?

If you encounter issues or have questions:

1. Check [MCP_SETUP.md](./MCP_SETUP.md) for MCP troubleshooting
2. Review examples in `examples/` directory
3. Ask Claude Code to invoke this agent and describe your issue

---

## Version

**Version:** 1.0.0
**Last Updated:** 2025-11-19
**Maintained By:** Pernell Toney

---

**Ready to build beautiful, consistent design systems?** Just ask Claude to use this agent!
