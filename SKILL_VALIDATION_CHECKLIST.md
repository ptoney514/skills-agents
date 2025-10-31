# Skill Validation Checklist

Based on Anthropic's official skill validation requirements from [Claude Code Skills Documentation](https://docs.claude.com/en/docs/claude-code/skills.md).

## Validation Requirements

### 1. SKILL.md Format

- [ ] YAML frontmatter starts on line 1 with `---`
- [ ] YAML frontmatter closes with `---`
- [ ] Markdown content follows closing `---`
- [ ] Uses spaces only (no tabs in YAML)
- [ ] Correct YAML indentation

### 2. Required Frontmatter Fields

#### `name` field
- [ ] Present and non-empty
- [ ] Maximum 64 characters
- [ ] Lowercase letters, numbers, and hyphens only
- [ ] No spaces, underscores, or special characters
- [ ] Does not contain reserved words: "anthropic", "claude"

#### `description` field
- [ ] Present and non-empty
- [ ] Maximum 1024 characters
- [ ] No XML tags
- [ ] Does not contain reserved words: "anthropic", "claude"
- [ ] Contains WHAT the skill does
- [ ] Contains WHEN to use it (trigger context)
- [ ] Includes specific, concrete terms users would mention
- [ ] Avoids vague descriptions like "helps with documents"

#### `allowed-tools` field (optional)
- [ ] If present, uses valid tool names
- [ ] Appropriate tool restrictions for skill purpose

### 3. Description Quality

The description should answer:
- **What**: Clear statement of capabilities and functions
- **When**: Contextual triggers and usage scenarios
- **Specificity**: Concrete file types, operations, use cases

**Anti-patterns to avoid:**
- Generic phrases ("helps with", "works with")
- Missing trigger context
- Vague functionality descriptions
- No specific file types or operation names

### 4. File Organization

- [ ] Skill directory follows naming convention: `skill-name/`
- [ ] SKILL.md is at root of skill directory
- [ ] Supporting files use relative paths with forward slashes
- [ ] No hardcoded absolute paths
- [ ] Optional directories properly structured:
  - `scripts/` for helper scripts
  - `templates/` for template files
  - Additional .md files for reference documentation

### 5. Content Structure

- [ ] Instructions are procedural (step-by-step) not conceptual
- [ ] Includes concrete examples of usage
- [ ] Main instructions under 5,000 tokens
- [ ] Supporting files loaded on-demand
- [ ] Clear workflow/process defined

### 6. Best Practices

- [ ] Single, focused purpose (not trying to do too much)
- [ ] Dependencies documented in description or instructions
- [ ] Version history maintained (if applicable)
- [ ] Tested with actual use cases
- [ ] README.md provides user-facing documentation

## Validation Process

For each skill:

1. **Automated checks**:
   - YAML syntax validation
   - Character count verification
   - Field presence validation
   - Naming convention compliance

2. **Manual review**:
   - Description quality assessment
   - Trigger context clarity
   - Example completeness
   - Procedural guidance quality

3. **Testing**:
   - Skill activates in appropriate contexts
   - Claude can execute the skill successfully
   - Supporting files load correctly
   - Output meets expectations

## Skills to Validate

| Skill Name | Location | Status | Notes |
|------------|----------|--------|-------|
| position-review-skill | skills/position-review-skill/ | ✅ Passed | Fixed: name field changed to `position-review-processor` |
| how-to-guide-writer | skills/how-to-guide-writer.skill/ | ✅ Passed | All checks passed |
| sop-writer | skills/sop-writer/ | ✅ Passed | All checks passed |
| recruiting-materials | skills/recruiting-materials/ | ✅ Passed | All checks passed |
| skill-creator | skills/skill-creator/ | ⚠️ Warning | Contains 'Claude' in description (intentional - skill is about creating skills for Claude) |
| canvas-design | skills/canvas-design/ | ✅ Passed | All checks passed |
| recruiting-evaluation | skills/recruiting-evaluation/ | ✅ Passed | All checks passed |
| brand-guidelines | skills/brand-guidelines/ | ⚠️ Warning | Contains 'Anthropic' in description (intentional - skill is about Anthropic brand guidelines) |

**Validation Date**: 2025-10-31
**Validation Result**: ✅ All 8 skills passed validation (6 fully passed, 2 with acceptable warnings)

## Status Legend

- ⏳ Pending - Not yet validated
- ✅ Passed - Meets all requirements
- ⚠️ Warning - Meets requirements but has improvement opportunities
- ❌ Failed - Does not meet requirements, needs fixes

## Validation Script

```bash
# Run this script to validate all skills
./scripts/validate-skills.sh
```

## Common Issues Found

This section will be populated as we validate each skill.

### Issue Categories

1. **Frontmatter formatting**
2. **Name validation**
3. **Description quality**
4. **File organization**
5. **Content structure**

## Remediation Plan

For any skills that don't pass validation:

1. Document specific violations
2. Create fix for each violation
3. Re-test after fixes
4. Update skill version number
5. Document changes in version history

## References

- [Claude Code Skills Documentation](https://docs.claude.com/en/docs/claude-code/skills.md)
- [Agent Skills Overview](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)
- Repository: [CLAUDE.md](./CLAUDE.md)
