# Recruiting Tracker - Installation Guide

**Version**: 3.0
**Updated**: November 4, 2025

---

## ✅ What's Included

Your `recruiting-tracker` skill package contains:

```
recruiting-tracker/
├── SKILL.md                          ✅ Main skill file (Claude reads this)
├── EVALUATION_METHODOLOGY.md         ✅ Complete two-stage framework
├── SCREEN_AND_RANK_EXAMPLE.md        ✅ Example Stage 1 output
├── SQLITE_ARCHITECTURE.md            ✅ Database schema and API docs
├── recruiting_database.py            🐍 SQLite database wrapper
├── excel_exporter.py                 🐍 Excel export functions
├── test_database.py                  🧪 Database validation script
├── templates/                        📁 Templates for new job folders
│   ├── job_description_template.txt  ✅ Job description template
│   └── HOW_TO_USE_template.md       ✅ Job-specific guide template
├── README.md                         📖 This file
├── INSTALLATION.md                   📖 Setup instructions
├── STATUS.md                         📖 What's ready and changelog
└── create-zip.sh                     🛠️ Helper script for creating ZIP
```

---

## 📦 Requirements

### For Claude Code Users (Local Terminal)

**Python Dependencies:**
```bash
# SQLite is built into Python (no install needed)

# Optional: Excel export functionality
pip install openpyxl
```

If you don't install `openpyxl`, the skill will still work but Excel exports will be disabled.

**System Requirements:**
- macOS, Linux, or Windows
- Python 3.7 or higher (usually pre-installed on Mac/Linux)
- ~10MB disk space per job folder (database + exports)

### For Claude.ai Users (Web/Desktop)

No installation needed! All core evaluation features work in the web/desktop app.

**Note:** SQLite database features require local file system (Claude Code only).

---

## 🚀 Installation

### Option 1: Claude Code (Recommended for Full Features)

#### Step 1: Copy Skill to Claude Directory

```bash
# Create skills directory if it doesn't exist
mkdir -p ~/.claude/skills

# Copy the skill
cp -r /path/to/recruiting-tracker ~/.claude/skills/

# Or create symlink for auto-updates from Git
ln -s /path/to/skills-agents/skills/recruiting-tracker ~/.claude/skills/recruiting-tracker
```

#### Step 2: Verify Installation

```bash
cd ~/.claude/skills/recruiting-tracker
ls -la
# You should see all skill files listed
```

#### Step 3: Test Database System (Optional)

```bash
cd ~/.claude/skills/recruiting-tracker
python3 test_database.py
```

This will:
- Create a test database
- Add sample candidates and evaluations
- Test queries, notes, and shortlists
- Export to Excel (if openpyxl installed)
- Verify all functionality works

#### Step 4: Start Using

```bash
mkdir ~/recruiting/test-job
cd ~/recruiting/test-job
claude-code
# Say: "Evaluate resumes in this folder"
# Claude will prompt to initialize - reply "yes"
```

---

### Option 2: Claude.ai (Upload as ZIP)

#### Step 1: Create ZIP File

```bash
cd /path/to/recruiting-tracker
./create-zip.sh

# Or manually:
zip -r recruiting-tracker.zip * -x "*.pyc" -x "__pycache__/*"
```

#### Step 2: Upload to Claude.ai

1. Go to https://claude.ai
2. Click Settings > Features
3. Find "Custom Skills" section
4. Upload `recruiting-tracker.zip`
5. Skill is now available globally in your Claude.ai account

**Note:** Custom skills are available on Pro, Max, Team, and Enterprise plans.

#### Step 3: Use It

Start a new conversation:
```
"Evaluate these 5 candidates for Senior Software Engineer.

Job Description:
[paste JD]

Resumes and cover letters attached."
[Upload files]
```

Claude will automatically use the recruiting-tracker skill and produce evaluation reports.

---

## 🧪 Testing

### Test 1: Database Functionality

```bash
cd ~/.claude/skills/recruiting-tracker
python3 test_database.py
```

**Expected output:**
```
============================================================
RECRUITING DATABASE TEST SUITE
============================================================

TEST 1: Database Creation
✅ Database created: test_recruiting.db

TEST 2: Job Creation
✅ Job created with ID: 1

TEST 3: Candidate Creation
✅ Created candidate: John Doe (ID: 1)
✅ Created candidate: Jane Smith (ID: 2)
✅ Created candidate: Bob Johnson (ID: 3)

[... continues through all tests ...]

✅ ALL TESTS PASSED!
```

### Test 2: Folder Initialization

```bash
mkdir ~/recruiting-test
cd ~/recruiting-test
claude-code
```

Say: **"Evaluate resumes in this folder"**

**Expected behavior:**
- Claude prompts: "This folder hasn't been set up yet. Initialize it?"
- Reply "yes"
- Claude creates job_description.txt, resumes/, recruiting.db, HOW_TO_USE.md

### Test 3: Single Candidate Evaluation

Create a test folder with one resume and cover letter:

```bash
mkdir ~/recruiting-test-single
cd ~/recruiting-test-single
# Add job_description.txt
# Add one resume and cover letter
claude-code
```

Say: **"Evaluate this candidate's resume and cover letter"**

**Expected output:**
- Detailed evaluation with Q/E/R breakdown
- Cover letter analysis
- Application Quality score with evidence
- Verification questions
- Star rating and recommendation

---

## 🔧 Customization

### Adjust Score Thresholds

Edit `SKILL.md` to change what qualifies as "Strong Candidate":

```markdown
# Current:
90-100 → Strong Candidate (⭐⭐⭐⭐⭐)
85-89  → Good Candidate (⭐⭐⭐⭐)

# Change to:
92-100 → Strong Candidate (⭐⭐⭐⭐⭐)
85-91  → Good Candidate (⭐⭐⭐⭐)
```

### Adjust Formula Weights

If your organization prioritizes interview performance even more:

```markdown
# Current Stage 2:
Final = (Resume × 25%) + (Interview × 50%) + (References × 25%)

# Change to:
Final = (Resume × 15%) + (Interview × 60%) + (References × 25%)
```

Always update both `SKILL.md` and `EVALUATION_METHODOLOGY.md` to keep them in sync.

---

## 🆕 What's New in v3.0

### Complete Recruiting Solution
- ✅ **Two-stage framework** - Resume screening + post-interview decisions
- ✅ **Cover letter analysis** - Application Quality component with evidence-based scoring
- ✅ **Verification questions** - Candidate-specific questions for phone screens
- ✅ **Stage 2 synthesis** - Combine resume + interview + references for final decisions

### From recruiting-evaluation-skill v2.x
- ✅ **SQLite database** - Persistent candidate tracking
- ✅ **Stage management** - Track candidates through hiring funnel
- ✅ **Notes system** - Add interview feedback and observations
- ✅ **Query capabilities** - Filter and search candidates
- ✅ **Historical tracking** - Full audit trail
- ✅ **Excel exports** - Professional reports
- ✅ **Folder initialization** - One-command setup with templates

### From recruiting-evaluation v1.x
- ✅ **Cover letter evaluation** - As part of Application Quality scoring
- ✅ **Candidate-specific verification questions** - For phone screens
- ✅ **Stage 2 post-interview evaluation** - Interview weighted at 50%
- ✅ **Final hiring recommendations** - STRONG HIRE / HIRE / DO NOT HIRE

### New in v3.0
- ✅ **Unified system** - One skill for entire hiring lifecycle
- ✅ **Renamed "recruiting-tracker"** - Clearer purpose
- ✅ **Flexible scaling** - Works for 1 candidate or 100+
- ✅ **Complete documentation** - Merged best practices from both predecessors

---

## 🎯 Migration from Previous Versions

### Migrating from recruiting-evaluation (v1.x)

**What's the same:**
- Stage 1 and Stage 2 methodology
- Cover letter analysis
- Verification questions

**What's new:**
- SQLite database for persistent tracking
- Excel exports
- Folder initialization
- Stage management commands

**What to update:**
- Use new skill name: `recruiting-tracker`
- Adopt folder-based workflow for multi-candidate evaluations
- Take advantage of database queries

### Migrating from recruiting-evaluation-skill (v2.x)

**What's the same:**
- SQLite database architecture
- Folder initialization
- Excel exports
- Stage management

**What's new:**
- Cover letter analysis
- Stage 2 post-interview evaluation
- Verification questions
- Application Quality component

**What to update:**
- Use new skill name: `recruiting-tracker`
- Provide cover letters when available
- Use Stage 2 for final hiring decisions

---

## ✅ Next Steps

1. **Install the skill** using one of the methods above
2. **Run test_database.py** to verify SQLite functionality (Claude Code only)
3. **Create a test job folder** and try the initialization workflow
4. **Evaluate real candidates** with resumes and cover letters
5. **Test Stage 2** with interview data for final decisions
6. **Validate** that outputs match your expectations
7. **Calibrate** thresholds based on your hiring outcomes

Your recruiting-tracker skill is ready to use! 🎉

---

## 💬 Support

- **Issues or bugs**: Modify SKILL.md to adjust behavior
- **Feature requests**: Add instructions to SKILL.md
- **Questions**: See full documentation in README.md and EVALUATION_METHODOLOGY.md

For technical database questions, see [SQLITE_ARCHITECTURE.md](SQLITE_ARCHITECTURE.md).
