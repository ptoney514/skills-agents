# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a skills-agents workspace for organizing and developing Claude Code custom skills. Skills are automation workflows that process data files (typically Excel/CSV exports) and generate formatted reports.

## Architecture Overview

### Symlink-Based Skill System

Skills live in `skills/` but are accessed by Claude Code via symlinks in `~/.claude/skills/`:

```
~/.claude/skills/position-review-skill  →  ~/Projects/skills-agents/skills/position-review-skill
```

**Why this matters:**
- Skills are edited here but auto-detected by Claude Code globally
- Multiple projects can reference the same skill library
- Version control stays in one place (this repo)

### Data Flow Pattern

All skills follow this input/output pattern:

```
data/inputs/[task-name]/        ← Source files (e.g., Oracle exports)
        ↓
skills/[task-name]-skill/       ← Processing logic
        ↓
data/outputs/[task-name]/       ← Generated reports
```

**Critical:** When a skill runs from a working directory like `data/inputs/position-review/`, output paths are typically relative: `../../outputs/position-review/`

## Key Commands

### View workspace structure
```bash
./scripts/view-structure.sh
```

### Sync skills to Claude Code after changes
```bash
./scripts/sync-skills.sh
```
**When to run:** After creating/modifying any skill, or if `~/.claude/skills/` symlinks are broken.

### Run a skill directly (for testing)
```bash
cd data/inputs/position-review
python ../../../skills/position-review-skill/process_positions.py input-file.xlsx
```

## Skill Development Workflow

### Anatomy of a Skill

Each skill directory must contain:
- **SKILL.md** - Skill metadata and instructions (required by Claude Code)
- **Processing script(s)** - Python/bash/etc. that does the actual work
- **README.md** - User-facing documentation

### Creating a New Skill

1. **Create skill structure:**
   ```bash
   mkdir skills/new-skill
   # Add SKILL.md, processing scripts, README.md
   ```

2. **Create data directories:**
   ```bash
   mkdir -p data/inputs/new-skill data/outputs/new-skill
   ```

3. **Sync to Claude Code:**
   ```bash
   ./scripts/sync-skills.sh
   ```

4. **Test the skill:**
   ```bash
   cd data/inputs/new-skill
   # Place test file here
   claude-code
   # Ask Claude to process using the skill
   ```

### SKILL.md Front Matter

Must include YAML front matter:
```yaml
---
name: Skill Display Name
description: What the skill does and when to use it (1-2 sentences)
---
```

Claude Code uses `description` to auto-select the skill based on user requests and file context.

## Existing Skills

### position-review-skill

**Purpose:** Processes Oracle Cloud Recruiting exports for weekly position review meetings.

**Key processing logic:**
- Filters positions with blank "Approved Date" AND excludes "_ORA_DELETED" requisitions
- Parses "Person Being Replaced" from comments using regex patterns
- Maps 12 Oracle columns to meeting format
- Flags data quality issues (missing salary, unclear justification)
- Generates: `Position_Review_Meetings_MM-DD-YYYY.xlsx`

**Placeholder fields:** Recruiter, Hiring Manager, Campus (awaiting second CSV integration)

**Dependencies:** pandas, openpyxl

## File Naming Conventions

**Input files:** Include date stamps for tracking history
```bash
orc-requisitions__2025-10-21.xlsx
budget-data__2025-Q4.xlsx
```

**Output files:** Auto-generated with dates by skills
```bash
Position_Review_Meetings_10-21-2025.xlsx
```

## .gitignore Strategy

- Data files (`*.xlsx`, `*.csv`) are ignored
- Directory structure is preserved with `.gitkeep` files
- Skills and scripts are version controlled

This allows sharing skills without exposing sensitive institutional data.

## Testing Skills

When testing a skill, always:

1. Navigate to the appropriate input directory: `cd data/inputs/[task-name]/`
2. Verify test files are present
3. Check that relative paths in the skill match this directory structure
4. Review generated data quality reports before accepting output

## Common Patterns

### Date-stamping inputs
```bash
mv ~/Downloads/export.xlsx data/inputs/task/export__$(date +%Y-%m-%d).xlsx
```

### Processing workflow
```bash
cd data/inputs/position-review
claude-code
# Say: "Process the latest file and save to ../../outputs/position-review/"
```

### Archiving old outputs
```bash
mkdir data/outputs/position-review/archive
mv data/outputs/position-review/*2024*.xlsx data/outputs/position-review/archive/
```
