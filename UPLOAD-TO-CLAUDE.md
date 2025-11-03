# Skills Ready for Claude.ai Upload

This document lists skills that have been bundled as ZIP files for upload to claude.ai.

## Skill Naming Requirements

Per [Claude.ai skill documentation](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview), skill names must:
- Contain **only lowercase letters, numbers, and hyphens**
- Not exceed 64 characters
- Avoid reserved words like "anthropic" and "claude"

## Available Skill Bundles

### 1. oracle-hcm-solution-architect
**File:** `oracle-hcm-solution-architect.zip` (21 KB)
**Description:** Expert Oracle HCM and Recruiting Cloud solution architect for creating visual diagrams, wireframes, workflows, and technical documentation with Mermaid.

**Contents:**
- SKILL.md (main skill instructions)
- README.md (user documentation)
- QUICK-REFERENCE.md (quick reference guide)
- CAPABILITIES-SHOWCASE.md (examples and capabilities)

**Use cases:**
- Creating Oracle HCM/Recruiting Cloud diagrams
- Documenting customizations and configurations
- Building user journey maps and workflows
- Technical architecture documentation

---

### 2. recruiting-materials
**File:** `recruiting-materials.zip` (38 KB)
**Description:** Generate professional hiring documents including phone screen scripts, interview guides, evaluation forms (1-10 rating scale), and reference check guides.

**Contents:**
- SKILL.md (main skill instructions)
- README.md (user documentation)
- references/question-banks.md (question library)
- templates/ (4 document templates)
- assets/ (3 reference assets)

**Use cases:**
- Creating phone screen scripts
- Generating interview guides
- Building evaluation forms
- Preparing reference check materials
- Batch generation for multiple candidates

---

## How to Upload to Claude.ai

1. **Go to Claude.ai** and log in to your account
2. **Navigate to Skills:**
   - Click on your profile
   - Select "Skills" or "Manage Skills"
3. **Upload the ZIP file:**
   - Click "Upload Custom Skill"
   - Select the `.zip` file
   - Confirm the upload
4. **Activate the skill:**
   - The skill will appear in your skills library
   - Toggle it on to use in conversations

## How to Use After Upload

Once uploaded, simply mention the task in your conversation:

**Oracle HCM Solution Architect:**
- "Create a sequence diagram for the requisition approval workflow"
- "Document the integration between ORC and HCM Core"
- "Build a user journey map for the candidate experience"

**Recruiting Materials:**
- "Generate interview materials for a Senior Developer position"
- "Create a phone screen script for this job description"
- "Build evaluation forms for 5 candidates based on their resumes"

## Notes

- These skills have proper YAML frontmatter for claude.ai compatibility
- All bundled resources (templates, references, assets) are included
- Skills can be updated by uploading a new version with the same name
- ZIP files do not include .DS_Store or other system files

## Version Control

These skills are maintained in the GitHub repository: `skills-agents`
- Source: `skills/oracle-hcm-solution-architect/`
- Source: `skills/recruiting-materials/`

To create updated bundles after making changes:
```bash
cd skills
zip -r ../oracle-hcm-solution-architect.zip oracle-hcm-solution-architect -x "*.DS_Store"
zip -r ../recruiting-materials.zip recruiting-materials -x "*.DS_Store"
```
