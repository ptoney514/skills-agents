# ARCHIVED: Canvas Design Skill

**Archived Date:** 2025-11-14
**Reason:** Replaced by `pixel-perfect-designer` agent

## Why This Was Archived

The `canvas-design` skill has been consolidated into the new **`pixel-perfect-designer`** agent, which provides:
- More structured design methodology (Flow Engineering)
- Better integration with CSS extraction for high-fidelity replication
- Comprehensive templates for style guides and design systems
- Support for both quick wireframes and detailed design systems
- Systematic approach to achieving pixel-perfect results

## Migration Path

If you previously used `canvas-design`, use `pixel-perfect-designer` instead:

### Old Usage:
```
User: "Create a poster/design/visual art for [purpose]"
→ canvas-design skill activated
```

### New Usage:
```
User: "Launch pixel-perfect-designer agent to create [design/wireframe/system]"
→ pixel-perfect-designer agent provides more structured, comprehensive approach
```

## What pixel-perfect-designer Adds

1. **Structured Methodology**
   - Flow Engineering: 4-step process
   - Lo-fi mode: ASCII wireframes for rapid iteration
   - Hi-fi mode: Complete design systems with style guides

2. **CSS Integration**
   - Extract styles from reference websites
   - Works with `css-style-extractor` skill
   - Achieves 100% fidelity to existing designs

3. **Comprehensive Outputs**
   - Style guides (color, typography, spacing, shadows)
   - Animation specifications
   - Component libraries
   - Framework-agnostic code

4. **Versatility**
   - React web apps
   - iOS designs
   - Print wireframes
   - Static sites
   - Design systems

## Accessing Archived Skill

This skill is preserved for reference but is no longer maintained. To use it:

1. Review `SKILL.md` for original instructions
2. Consider migrating to `pixel-perfect-designer` for active projects
3. For legacy workflows, the skill can still be invoked manually (though symlinks may need to be recreated)

## Key Difference

**canvas-design** focused on creating individual visual artifacts (posters, designs).

**pixel-perfect-designer** focuses on creating systematic, reusable design systems with pixel-perfect fidelity, though it can also handle individual designs within a structured workflow.

---

**Replacement Agent:** [agents/pixel-perfect-designer/AGENT.md](../../../agents/pixel-perfect-designer/AGENT.md)
