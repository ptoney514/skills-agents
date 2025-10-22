# Skills-Agents Workspace

A clean, organized workspace for Claude Code skills and automation workflows.

## 📁 Structure

```
skills-agents/
├── skills/                      # Your custom Claude Code skills
│   └── position-review-skill/  # Example skill
├── data/
│   ├── inputs/                 # Source files (organized by task)
│   │   └── position-review/
│   └── outputs/                # Generated results
│       └── position-review/
└── scripts/                    # Helper scripts
    ├── setup.sh
    ├── sync-skills.sh
    └── view-structure.sh
```

## 🚀 Quick Start

### View Your Structure
```bash
./scripts/view-structure.sh
```

### Add a New Skill
```bash
# 1. Create the skill folder
mkdir skills/my-new-skill

# 2. Add your SKILL.md and scripts
# ...

# 3. Sync to Claude Code
./scripts/sync-skills.sh
```

### Typical Workflow

1. **Add input files** to `data/inputs/[task-name]/`
2. **Navigate to the input directory**
   ```bash
   cd data/inputs/position-review
   ```
3. **Start Claude Code**
   ```bash
   claude-code
   ```
4. **Process your files** - Claude will use the appropriate skill
5. **Get results** from `data/outputs/[task-name]/`

## 🔧 Scripts

- **setup.sh** - Initial workspace setup
- **sync-skills.sh** - Sync skills to `~/.claude/skills/`
- **view-structure.sh** - Display folder structure

## 🔗 How It Works

Skills are stored in `skills/` and symlinked to `~/.claude/skills/` so Claude Code can find them:

```
~/.claude/skills/position-review-skill
    ↓ (symlink)
~/Projects/skills-agents/skills/position-review-skill
```

This allows you to:
- Edit skills in one organized location
- Keep everything version-controlled
- Easily back up your entire workspace
- Share skills across projects

## 📝 Best Practices

- **Date-stamp input files**: `file__2025-10-21.xlsx`
- **Keep inputs and outputs separate**: Use the data/ structure
- **One skill per task type**: Keep skills focused
- **Archive old files**: Move to `data/outputs/[task]/archive/`

## 🎯 Example: Position Review Workflow

```bash
# Save Oracle export with date
mv ~/Downloads/orc-requisitions.xlsx \
   data/inputs/position-review/orc-requisitions__$(date +%Y-%m-%d).xlsx

# Process it
cd data/inputs/position-review
claude-code

# In Claude Code:
"Process the latest orc-requisitions file and save to ../../outputs/position-review/"

# Result appears in:
# data/outputs/position-review/Position_Review_Meetings_[DATE].xlsx
```

## 🔄 Maintenance

```bash
# View structure
./scripts/view-structure.sh

# Sync skills after changes
./scripts/sync-skills.sh

# Clean old files (30+ days)
find data/inputs -name "*.xlsx" -mtime +30 -delete
```

## 📊 Adding More Skills

As your automation needs grow, add new skills:

```bash
# Create skill
mkdir skills/budget-analysis-skill

# Add SKILL.md and scripts
# ...

# Create data folders
mkdir -p data/inputs/budget
mkdir -p data/outputs/budget

# Sync to Claude Code
./scripts/sync-skills.sh
```

Now you can work on budget analysis in `data/inputs/budget/` and Claude will automatically use the right skill!

---

**Time saved per week**: ~45 minutes per automated task ✅
