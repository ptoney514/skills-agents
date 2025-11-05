# Recruiting Evaluation Skill - Installation Guide

**Version**: 2.2
**Updated**: November 4, 2025

## ✅ What's Ready

Your `recruiting-evaluation-skill` folder now contains:

```
recruiting-evaluation-skill/
├── SKILL.md                          ✅ Main skill file with proper YAML frontmatter
├── EVALUATION_METHODOLOGY.md         ✅ Complete methodology reference
├── SCREEN_AND_RANK_EXAMPLE.md        ✅ Example output format
├── SQLITE_ARCHITECTURE.md            ✅ Database schema and API docs
├── recruiting_database.py            🐍 SQLite database wrapper
├── excel_exporter.py                 🐍 Excel export functions
├── test_database.py                  🧪 Database validation script
├── templates/                        📁 Templates for new job folders
│   ├── job_description_template.txt  ✅ Job description template
│   └── HOW_TO_USE_template.md       ✅ Job-specific guide template
├── CANDIDATE_EVALUATION_TEMPLATE.md  📋 Legacy template (reference)
├── CACHING_INSTRUCTIONS.md           📋 Legacy caching docs (reference)
└── README.md                         📖 Human-readable documentation
```

---

## 📦 Requirements

### Python Dependencies

For **Claude Code** users (local terminal use):

```bash
# SQLite is built into Python (no install needed)

# Optional: Excel export functionality
pip install openpyxl
```

If you don't install `openpyxl`, the skill will still work but Excel exports will be disabled.

### For claude.ai Users

No installation needed! All functionality works in the web/desktop app.

---

## 🚀 How to Use This Skill

### Option 1: Claude.ai (Upload as ZIP)

1. **Create a ZIP file**:
   ```bash
   cd /Users/pernelltoney/Documents
   zip -r recruiting-evaluation-skill.zip recruiting-evaluation-skill/
   ```

2. **Upload to Claude.ai**:
   - Go to Claude.ai Settings > Features
   - Look for "Custom Skills" section
   - Upload the `recruiting-evaluation-skill.zip` file
   - Available on Pro, Max, Team, and Enterprise plans

3. **Use it**:
   Just start a conversation like:
   ```
   "Evaluate these 5 candidates for Senior Software Engineer.
   Here's the JD: [paste]
   Resumes attached: [upload files]"
   ```

---

### Option 2: Claude Code (Filesystem)

1. **Copy to Claude Code skills directory**:
   ```bash
   # Create skills directory if it doesn't exist
   mkdir -p ~/.claude/skills
   
   # Copy your skill
   cp -r /Users/pernelltoney/Documents/recruiting-evaluation-skill ~/.claude/skills/
   ```

2. **Use it**:
   ```bash
   claude code "Evaluate all resumes in ./candidates/ 
   against job_description.txt and create a report"
   ```

---

### Option 3: Claude API (If using programmatically)

1. **Upload via API**:
   ```bash
   # You'll need to use the /v1/skills endpoints
   # See: https://docs.claude.com/en/api/skills-guide
   ```

2. **Reference in API calls**:
   ```python
   response = client.messages.create(
       model="claude-sonnet-4-5-20250929",
       skills=["recruiting-evaluation"],
       # ... rest of your API call
   )
   ```

---

## 🎯 What Changed (The Fix)

### ❌ Before (Missing frontmatter):
```markdown
# Recruiting Evaluation Skill

## Overview
...
```

### ✅ After (Proper format):
```markdown
---
name: recruiting-evaluation
description: Evaluate job candidates using evidence-based scoring...
---

# Recruiting Evaluation Skill

## Overview
...
```

The **YAML frontmatter** at the top is what tells Claude:
- **name**: The skill identifier (must be lowercase with hyphens)
- **description**: What it does AND when to use it (helps Claude decide to trigger it)

---

## 📝 Quick Test

To verify it works:

1. **If using Claude.ai**: After uploading, ask:
   ```
   "Do you have access to the recruiting-evaluation skill?"
   ```

2. **If using Claude Code**: Run:
   ```bash
   claude code "list available skills"
   ```

---

## 🔧 Customization

If you need to adjust thresholds or weights:

1. Edit `SKILL.md`
2. Find the formulas section
3. Modify the values:
   ```markdown
   Overall Score = (Q × 0.40) + (E × 0.40) + (R × 0.20)
   
   # Change to:
   Overall Score = (Q × 0.30) + (E × 0.50) + (R × 0.20)
   ```
4. Re-zip and re-upload (or just save if using Claude Code)

---

## 🧪 Testing the Database System

For **Claude Code** users, test the SQLite database:

```bash
cd ~/.claude/skills/recruiting-evaluation-skill
python3 test_database.py
```

This will:
- Create a test database
- Add sample candidates and evaluations
- Test queries, notes, and shortlists
- Export to Excel (if openpyxl available)
- Verify all functionality works

---

## ✅ Next Steps

1. **Test it** with a real job description and resumes
2. **Validate** the scoring makes sense for your organization
3. **Calibrate** thresholds based on your hiring standards
4. **Use SQLite features** for persistent candidate tracking (Claude Code only)
5. **Share** with your recruiting team (API/Teams only)

Your skill is now ready to use! 🎉

---

## 🆕 What's New

### v2.2 (Latest)
- ✅ **Automatic folder initialization** - Claude sets up new job folders with templates
- ✅ **Job description template** - Pre-formatted template with optimal fields for evaluation
- ✅ **Job-specific guide** - Each job folder gets a customized HOW_TO_USE.md
- ✅ **Streamlined onboarding** - Just create folder, say "evaluate resumes", confirm initialization

### v2.1
- ✅ **SQLite database support** - Persistent candidate tracking across evaluation rounds
- ✅ **Stage management** - Move candidates through hiring funnel
- ✅ **Notes system** - Add interview feedback, phone screen notes, etc.
- ✅ **Query capabilities** - Filter candidates by score, stage, date
- ✅ **Historical tracking** - Full audit trail of evaluations and decisions
- ✅ **Excel exports** - Generate reports on demand from database

See [SQLITE_ARCHITECTURE.md](SQLITE_ARCHITECTURE.md) for complete details.
