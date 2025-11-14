# ARCHIVED: UX/UI Designer Agent

**Archived Date:** 2025-11-14
**Reason:** Replaced by `pixel-perfect-designer` agent

## Why This Was Archived

The `ux-ui-designer` agent has been consolidated into the new **`pixel-perfect-designer`** agent, which provides:
- More comprehensive design methodology (Flow Engineering)
- Both lo-fi (ASCII wireframes) and hi-fi (detailed design systems) modes
- Integration with CSS extraction workflow
- Systematic approach to achieving pixel-perfect results
- Better documentation and templates

## Migration Path

If you previously used `ux-ui-designer`, use `pixel-perfect-designer` instead:

### Old Usage:
```
Launch ux-ui-designer agent to design [feature]
```

### New Usage:
```
Launch pixel-perfect-designer agent in hi-fi mode to design [feature]
```

## What pixel-perfect-designer Adds

1. **Flow Engineering Methodology**
   - Step 1: Layout Design (ASCII wireframes)
   - Step 2: Scene Design (Theme/Style)
   - Step 3: Animation Design (Micro-interactions)
   - Step 4: Scaling Components

2. **CSS Extraction Integration**
   - Works with `css-style-extractor` skill
   - Achieves 100% fidelity from reference sites

3. **Comprehensive Templates**
   - Style guide templates
   - Animation spec templates
   - Component manifest templates

4. **Framework-Agnostic**
   - React, iOS, print wireframes, static sites
   - Output format adapts to project needs

## Accessing Archived Agent

This agent is preserved for reference but is no longer maintained. To use it:

1. Review `AGENT.md` for original instructions
2. Consider migrating to `pixel-perfect-designer` for active projects
3. For legacy projects, the agent can still be invoked manually

---

**Replacement Agent:** [agents/pixel-perfect-designer/AGENT.md](../../pixel-perfect-designer/AGENT.md)
