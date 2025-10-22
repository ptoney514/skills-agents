---
name: sop-writer
description: Create, update, or review Standard Operating Procedures (SOPs), work instructions, process documentation, and procedural guides. Use when users request help writing SOPs, documenting processes, creating procedure manuals, standardizing workflows, or need guidance on operational documentation.
---

# SOP Writer

Create clear, actionable Standard Operating Procedures that ensure consistent execution of business processes.

## When to Use This Skill

Use this skill when users request:
- Creation of new SOPs or process documentation
- Updates or improvements to existing SOPs
- Reviews of SOP drafts for completeness and clarity
- Conversion of informal processes into formal documentation
- Standardization of procedures across teams
- Work instructions, runbooks, or procedural guides

## Core Workflow

### 1. Understand the Process

Before writing, gather key information:

**Ask clarifying questions:**
- What is the process being documented?
- Who will use this SOP? (experience level matters)
- What is the desired outcome of the process?
- How often is this process performed?
- What are the critical quality/safety requirements?
- Are there existing documents or materials to reference?

**Understand the scope:**
- Where does the process start and end?
- What triggers the process?
- What are the dependencies?
- What should explicitly NOT be included?

### 2. Choose the Appropriate Format

Select template based on complexity and audience:

**Basic SOP Template** (`assets/basic-sop-template.md`)
- **Use for:** Complex processes requiring detailed documentation
- **Includes:** Full structure with all sections
- **Best for:** Regulated environments, critical processes, training purposes
- **Typical length:** 3-10 pages

**Quick Reference Template** (`assets/quick-reference-template.md`)
- **Use for:** Simple, frequently-performed tasks
- **Includes:** Streamlined steps with minimal overhead
- **Best for:** Experienced users, routine operations
- **Typical length:** 1-2 pages

**Technical Procedure Template** (`assets/technical-procedure-template.md`)
- **Use for:** IT operations, software deployments, technical maintenance
- **Includes:** Commands, code blocks, verification steps, rollback procedures
- **Best for:** DevOps, system administration, technical teams
- **Typical length:** 2-5 pages

### 3. Write Clear, Actionable Steps

Follow these principles when writing procedure steps:

**Action-Oriented Language:**
- Start each step with an action verb (Click, Select, Enter, Review, Verify)
- Be specific: "Click the **Save** button" not "Save the file"
- One action per step when possible

**Decision Points:**
- Make branching logic explicit with IF/THEN statements
- Provide clear criteria for decisions
- Example: "IF error code is 404, THEN contact IT support. OTHERWISE, continue to Step 5."

**Expected Outcomes:**
- State what should happen after each major step
- Include verification steps
- Example: "Expected Result: The status indicator turns green and displays 'Connected'"

**Warnings and Notes:**
- Use **WARNING** for critical safety or data loss risks
- Use **NOTE** for helpful additional information
- Use **TIP** for efficiency improvements

### 4. Include Supporting Elements

**Prerequisites Section:**
- Required training, certifications, or knowledge
- Tools, systems, or software needed
- Materials or documents required
- Access permissions or credentials

**Troubleshooting Section:**
- Common problems and their solutions
- When to escalate
- Contact information for support

**Quality Checks:**
- Verification points throughout the process
- Final quality assurance checklist
- Success criteria

### 5. Review for Quality

A high-quality SOP should:
- Be executable by someone unfamiliar with the process
- Use clear, unambiguous language
- Include all necessary information without assumptions
- Have numbered sequential steps
- Define all technical terms and acronyms
- Include decision criteria (not just "if needed")
- Have a logical flow from start to finish

## Best Practices Reference

For detailed guidance on SOP writing best practices, see `references/sop-best-practices.md`. Key topics include:
- Writing style guidelines
- Formatting standards  
- Common mistakes to avoid
- Quality metrics for SOPs

## Output Format

Always create SOPs as markdown (.md) files. Use proper formatting:
- **Bold** for UI elements, buttons, field names
- *Italics* for emphasis
- `Monospace` for commands, code, system inputs
- Numbered lists for sequential steps
- Bullet points for non-sequential items
- Tables for roles, definitions, troubleshooting

## Examples of Good vs. Poor Steps

❌ **Poor:** "Configure the settings properly"
✅ **Good:** "Set the timeout value to 30 seconds and enable auto-retry"

❌ **Poor:** "If needed, adjust the parameters"
✅ **Good:** "IF the upload fails with error code 408, THEN increase the timeout to 60 seconds"

❌ **Poor:** "Make sure everything is correct"
✅ **Good:** "Verify all three status indicators are green before proceeding"

## Revision and Maintenance

Always include:
- Version number
- Effective date
- Revision history table
- Document owner
- Approval authority

When updating existing SOPs:
- Increment version number appropriately (major vs minor changes)
- Document what changed in the revision history
- Update the "Last Revised" date
- Consider if users need retraining

## Deliverable

Create the SOP as a complete, ready-to-use document. Don't just provide an outline - write the full content including:
- All sections properly filled in
- Actual step-by-step procedures
- Complete troubleshooting guidance
- Proper formatting and structure

The SOP should be immediately usable by the target audience with no additional work required.
