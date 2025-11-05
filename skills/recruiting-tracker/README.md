# Recruiting Tracker - Complete Recruiting Management System

**Version**: 3.0
**Updated**: November 4, 2025
**For**: Claude (claude.ai) and Claude Code

---

## What This Skill Does

Recruiting Tracker is a complete end-to-end recruiting solution that handles everything from initial resume screening to final hiring decisions. It combines rigorous candidate evaluation with professional candidate management in a single, unified system.

**Core Capabilities:**

### Evaluation Features
- ⭐ **Two-Stage Framework** - Resume screening (Stage 1) + Post-interview decisions (Stage 2)
- 📝 **Cover Letter Analysis** - Evaluates application quality as part of candidate assessment
- 📊 **Objective Scoring** - Mathematical Q/E/R methodology (0-100 scale)
- ✅ **Strengths & Concerns** - Specific, actionable feedback for each candidate
- 🎯 **Verification Questions** - Candidate-specific questions for phone screens
- ⭐ **Star Ratings** - Visual 5-star system for quick assessment

### Management Features
- 💾 **SQLite Database** - Persistent candidate tracking across weeks/months
- 📈 **Stage Management** - Track candidates through: screened → phone_screen → interview → offer
- 📝 **Notes System** - Add feedback from phone screens, interviews, references
- 🔍 **Query Capabilities** - Filter by score, stage, date evaluated
- 📊 **Excel Exports** - Multiple professional report formats
- 📚 **Historical Tracking** - Full audit trail of evaluations and decisions
- 🚀 **Auto-Initialization** - One-command folder setup with templates

### Flexibility
- **Single Candidate Mode** - "Evaluate this one resume and cover letter"
- **Bulk Mode** - "Evaluate all 50 resumes in this folder"
- **Incremental** - "Add 10 new candidates without re-processing existing 40"
- **Long-term** - Manage recruiting campaigns over weeks/months

**Key Benefits:**
- ✅ **Complete Solution** - From resume to offer, all in one skill
- ✅ **Scalable** - Works for 1 candidate or 100+ candidates
- ✅ **Persistent** - Data survives across multiple sessions
- ✅ **Professional** - Executive-ready reports and exports
- ✅ **Legally Defensible** - EEOC-compliant, objective methodology

---

## Quick Start

### For Claude Code Users (Recommended for Full Features)

#### Step 1: Install the Skill

```bash
# Create skills directory if needed
mkdir -p ~/.claude/skills

# Copy or symlink the skill
cp -r /path/to/recruiting-tracker ~/.claude/skills/

# Or create symlink for auto-updates
ln -s /path/to/skills-agents/skills/recruiting-tracker ~/.claude/skills/recruiting-tracker
```

#### Step 2: Create a Job Folder

```bash
mkdir ~/recruiting/software-engineer
cd ~/recruiting/software-engineer
claude-code
```

Say: **"Evaluate resumes in this folder"**

Claude will prompt: **"This folder hasn't been set up yet. Initialize it?"**

Reply: **"yes"**

Claude creates:
- `job_description.txt` (template with instructions)
- `resumes/` folder (for resumes and cover letters)
- `recruiting.db` (SQLite database)
- `HOW_TO_USE.md` (job-specific guide)

#### Step 3: Fill in Job Details

1. Edit `job_description.txt` with job requirements (fields marked with * are required)
2. Drop candidate resumes and cover letters into `resumes/` folder

#### Step 4: Run Evaluation

```bash
claude-code
# Say: "Evaluate all resumes"
```

Claude will:
- Evaluate all candidates (including cover letter analysis)
- Store results in SQLite database
- Generate `candidate_scores.xlsx`
- Create Screen and Rank Report

---

### For Claude.ai Users (Web/Desktop)

1. **Create ZIP file**:
   ```bash
   cd /path/to/recruiting-tracker
   ./create-zip.sh
   ```

2. **Upload to Claude.ai**:
   - Go to Settings > Features > Custom Skills
   - Upload the ZIP file
   - Available on Pro, Max, Team, and Enterprise plans

3. **Use it**:
   ```
   "Evaluate these 5 candidates for Senior Software Engineer.
   Here's the JD: [paste]
   Resumes and cover letters attached: [upload files]"
   ```

Claude will automatically produce a Screen and Rank Report.

---

## What's Included

```
recruiting-tracker/
├── SKILL.md                          ✅ Main skill file (Claude reads this)
├── EVALUATION_METHODOLOGY.md         ✅ Complete mathematical framework
├── SCREEN_AND_RANK_EXAMPLE.md        ✅ Example output format
├── SQLITE_ARCHITECTURE.md            ✅ Database schema and implementation
├── recruiting_database.py            🐍 SQLite database wrapper class
├── excel_exporter.py                 🐍 Excel export functions
├── test_database.py                  🧪 Database validation script
├── templates/                        📁 Templates for new job folders
│   ├── job_description_template.txt  ✅ Job description template
│   └── HOW_TO_USE_template.md       ✅ Job-specific guide template
├── README.md                         📖 This file
├── INSTALLATION.md                   📖 Setup instructions
├── STATUS.md                         📖 What's ready and what changed
└── create-zip.sh                     🛠️ Helper script for creating ZIP
```

---

## Two-Stage Evaluation Framework

### Stage 1: Resume Screening

**Purpose:** Identify which candidates to interview

**Inputs:**
- Job description
- Candidate resume
- Cover letter (if provided)

**Scoring:**
```
Overall Score = (Qualifications × 40%) + (Experience × 40%) + (Risk Flags × 20%)
```

**Risk Flags includes:**
- Employment Gaps (25%)
- Job Hopping Patterns (25%)
- Skill Currency (25%)
- **Application Quality / Cover Letter (25%)**

**Output:**
- 0-100 score with star rating
- Key strengths (3-5 bullets)
- Key concerns (1-3 bullets)
- **Candidate-specific verification questions** for phone screen

**Decision Thresholds:**
- ⭐⭐⭐⭐⭐ (90-100) = Strong Candidate - Interview ASAP
- ⭐⭐⭐⭐ (85-89) = Good Candidate - Definitely interview
- ⭐⭐⭐ (70-84) = Potential Fit - Consider for phone screen
- ⭐⭐ or ⭐ (below 70) = Not a Match

### Stage 2: Post-Interview Decision

**Purpose:** Make final hire/no-hire recommendation

**Inputs:**
- Stage 1 resume score (from database or provided)
- Interview rating (1-10 scale or 0-100)
- Reference check feedback (2-3 references)

**Scoring:**
```
Final Score = (Resume × 25%) + (Interview × 50%) + (References × 25%)
```

**Output:**
- Final hiring recommendation: STRONG HIRE / HIRE / DO NOT HIRE
- Comparative analysis (if multiple candidates)
- Where interview contradicted or confirmed resume
- Reference check highlights
- Confidence level and rationale

**Key Principle:** Interview performance is weighted at 50% - the most important factor. A strong resume gets you to the interview, but interview performance determines if you get the offer.

---

## Using the Database System

### Your Folder Structure

```
job-folder/
├── job_description.txt
├── resumes/
│   ├── john_doe_resume.pdf
│   ├── john_doe_cover_letter.pdf
│   ├── jane_smith_resume.pdf
│   └── jane_smith_cover_letter.docx
├── recruiting.db                 ← SQLite database (source of truth)
├── candidate_scores.xlsx         ← Generated on demand
└── Screen_and_Rank_Report.md    ← Generated on demand
```

### Common Workflows

#### Initial Evaluation
```bash
cd ~/recruiting/software-engineer
claude-code
# Say: "Evaluate all resumes in this folder"

# Claude processes all resumes and cover letters
# Creates database, exports Excel, generates report
```

#### Add New Candidates (Weeks Later)
```bash
# Drop new resumes into resumes/ folder
claude-code
# Say: "Check for new resumes and evaluate them"

# Only new candidates are processed!
# Database and reports updated automatically
```

#### Query Candidates
```bash
claude-code
# Say: "Show me all candidates with 85+ scores who haven't been interviewed yet"
# Say: "Show me candidates in phone screen stage"
# Say: "Show me top 10 candidates"
```

#### Track Interview Progress
```bash
claude-code
# After phone screen:
"Add phone screen note for Jane Smith: Strong technical skills,
interested in mission-driven work, available next week"

"Move Jane Smith to interview stage"

# After interview:
"Add interview note for Jane Smith: Excellent cultural fit,
demonstrated leadership in examples, minor concern about relocation timeline"

"Move Jane Smith to final round stage"
```

#### Make Final Hiring Decision
```bash
claude-code
# Say: "Run Stage 2 evaluation for Jane Smith.
# Her interview rating was 9/10, references were excellent
# (former manager would rehire, praised leadership),
# and her Stage 1 score was 88"

# Claude calculates:
# Final = (88 × 0.25) + (90 × 0.50) + (95 × 0.25) = 90.75
# Recommendation: STRONG HIRE
```

#### Export Reports
```bash
claude-code
# Say: "Export all candidates to Excel"
# Say: "Generate comparison report for top 3 finalists"
# Say: "Show me evaluation history for Jane Smith"
```

---

## Cover Letter Analysis

One of the most powerful features is automatic cover letter evaluation.

### How It Works

Cover letters are scored as part of the **Application Quality** component (25% of Risk Flags, which is 20% of total score).

**Impact on Overall Score:**
- Exceptional cover letter: Can add **~1 point** to overall score
- Weak cover letter: Can subtract **~0.5 points** from overall score

### What Makes an Exceptional Cover Letter?

- **Deep Research**: References specific programs, initiatives, or values of the organization
- **Personalization**: Clearly tailored to this specific role, not a template
- **Fit Narrative**: Compellingly explains why this role is the right next step
- **Gap Addressing**: Proactively explains career transitions or gaps
- **Professional Writing**: Excellent grammar, structure, and tone

### Example Impact

Two candidates with identical qualifications and experience:
- **Candidate A**: Generic cover letter → Application Quality = 65 → Overall = 84.5
- **Candidate B**: Exceptional cover letter → Application Quality = 95 → Overall = 86.5

**Candidate B ranks higher** - the cover letter demonstrates:
- Better communication skills
- Genuine interest in the organization
- Research and attention to detail
- Proactive problem-solving (addressing potential concerns)

---

## Verification Questions

For each candidate evaluated in Stage 1, Claude generates 3-5 **candidate-specific verification questions** to ask during phone screens.

### Purpose

These questions:
- Address concerns or gaps identified in resume
- Verify key skills or experiences
- Clarify career transitions
- Validate claims that seem too good to be true

### Example

**Candidate**: John Doe, Software Engineer

**Generated Verification Questions:**
1. "You had a 6-month gap between TechCorp and StartupCo - can you tell me what you were working on during that time?"
2. "Your resume mentions leading a distributed systems project - can you walk me through your specific role and technical contributions?"
3. "I see you transitioned from data science to software engineering in 2022 - what prompted that change and how did you build up your engineering skills?"

These questions help you make the most of limited phone screen time.

---

## Database Features

### Persistent Tracking
- Keep candidate data across weeks/months of recruiting
- Add new candidates without re-evaluating existing ones
- Track how candidates progress through hiring stages

### Stage Management
Candidates move through these stages:
1. **new** - Just added, not yet evaluated
2. **screened** - Resume evaluated, scores assigned
3. **phone_screen** - Passed screening, scheduled for phone call
4. **interview** - Passed phone screen, invited for interview
5. **final_round** - Top candidates, final decision pending
6. **offer** - Offer extended
7. **rejected** - Not moving forward
8. **withdrawn** - Candidate withdrew

### Notes System
Add notes for:
- **phone_screen** - Feedback from initial call
- **interview** - In-person/video interview observations
- **reference_check** - Reference feedback
- **internal** - Hiring manager comments, team feedback
- **hiring_manager** - Specific hiring manager input

Each note is timestamped and can be tagged for filtering.

### Query Capabilities

Ask questions like:
- "Show me candidates with 85+ scores not yet interviewed"
- "How many candidates in each stage?"
- "Show evaluation history for John Doe"
- "Get all interview notes for Jane Smith"
- "Who are my top 5 candidates?"

### Excel Exports

Generate professional reports:
- **candidate_scores.xlsx** - All candidates with filters and conditional formatting
- **phone_screen_list.xlsx** - Candidates ready for phone screens
- **interview_candidates.xlsx** - Candidates scheduled for interviews
- **finalist_comparison.xlsx** - Side-by-side comparison of top candidates

---

## The Scoring System

### Stage 1: Resume Screening

```
Evala Overall Score = (Q × 40%) + (E × 40%) + (R × 20%)

Where:
  Q = Qualifications (must-haves, preferreds, education, certs)
  E = Experience (years, progression, industry, complexity)
  R = Risk Flags (gaps, hopping, currency, application quality)
```

**Risk Flags Breakdown:**
```
R = (Employment Gaps × 25%) + (Job Hopping × 25%) +
    (Skill Currency × 25%) + (Application Quality/Cover Letter × 25%)
```

**Star Ratings:**
- ⭐⭐⭐⭐⭐ (90-100) = Strong Candidate
- ⭐⭐⭐⭐ (85-89) = Good Candidate
- ⭐⭐⭐ (70-84) = Potential Fit
- ⭐⭐ (60-69) = Not a Match
- ⭐ (0-59) = Not a Match

### Stage 2: Final Hiring Decision

```
Final Score = (Resume × 25%) + (Interview × 50%) + (References × 25%)
```

**Interview performance is weighted at 50% - the most important factor.**

**Interpretation:**
- **90-100:** STRONG HIRE (Excellent across all dimensions)
- **80-89:** HIRE (Solid candidate, recommend offer)
- **70-79:** MARGINAL (Proceed with caution)
- **Below 70:** DO NOT HIRE

---

## Example Workflows

### Workflow 1: Quick Single Candidate Evaluation

```
User: "Evaluate this candidate for Senior Software Engineer"
[Provides JD, resume, cover letter]

Claude:
✅ Provides detailed evaluation with:
- Overall score and star rating
- Q/E/R breakdown
- Cover letter analysis
- Strengths and concerns
- 3-5 verification questions for phone screen
```

### Workflow 2: Bulk Screening for New Position

```
Day 1:
User creates folder: ~/recruiting/marketing-director
User: "Evaluate resumes in this folder"
Claude: "Initialize folder? (yes/no)"
User: "yes"
Claude creates structure with templates

User fills in job_description.txt
User adds 20 resumes + cover letters to resumes/ folder

User: "Evaluate all resumes"
Claude:
- Evaluates all 20 candidates
- Analyzes cover letters
- Stores in recruiting.db
- Exports candidate_scores.xlsx
- Generates Screen and Rank Report

Week 2:
User adds 5 more resumes
User: "Check for new resumes"
Claude: Only evaluates the 5 new ones, updates everything

Week 3:
User: "Show me candidates with 85+ scores not yet interviewed"
User: "Move top 5 to interview stage"
User: "Export interview candidates to Excel"

Week 4:
After interviews:
User: "Add interview note for John Doe: [feedback]"
User: "Run Stage 2 evaluation for finalists"
Claude: Provides final hiring recommendations
```

### Workflow 3: Comparing Finalists

```
User: "I've interviewed 3 candidates. Here are their details:

Jane Smith: Stage 1 score 88, interview rating 9/10, references excellent
John Doe: Stage 1 score 92, interview rating 7/10, references good
Bob Johnson: Stage 1 score 85, interview rating 10/10, references excellent

Who should I hire?"

Claude runs Stage 2 for all three:
- Jane: (88×0.25) + (90×0.50) + (95×0.25) = 90.75 → STRONG HIRE
- John: (92×0.25) + (70×0.50) + (85×0.25) = 79.25 → MARGINAL
- Bob: (85×0.25) + (100×0.50) + (95×0.25) = 95.0 → STRONG HIRE

Recommendation: Bob Johnson (highest final score, exceptional interview)
Analysis: Bob's interview performance outweighed John's stronger resume
```

---

## Installation

### Requirements

**For Claude Code:**
- Python 3.x (built-in to macOS)
- SQLite (built into Python - no install needed)
- openpyxl (optional, for Excel exports): `pip install openpyxl`

**For Claude.ai:**
- No requirements - works in browser/desktop app

### Setup

1. **Copy to skills directory**:
   ```bash
   cp -r recruiting-tracker ~/.claude/skills/
   ```

2. **Test the database** (optional):
   ```bash
   cd ~/.claude/skills/recruiting-tracker
   python3 test_database.py
   ```

3. **Start using**:
   ```bash
   mkdir ~/recruiting/test-job
   cd ~/recruiting/test-job
   claude-code
   # Say: "Evaluate resumes in this folder"
   ```

See [INSTALLATION.md](INSTALLATION.md) for detailed setup instructions.

---

## Common Commands

### Evaluation

```bash
# Single candidate
"Evaluate this resume and cover letter"

# Bulk evaluation
"Evaluate all resumes in this folder"

# Add new candidates
"Check for new resumes and evaluate them"
```

### Querying

```bash
"Show me all candidates with 85+ scores"
"Show me candidates who haven't been interviewed yet"
"Show me candidates in phone screen stage"
"Get evaluation history for Jane Smith"
"Show me summary statistics"
```

### Stage Management

```bash
"Move Jane Smith to phone screen stage"
"Move John Doe to interview stage"
"Add these candidates to interview shortlist: Jane, John, Bob"
```

### Notes & Feedback

```bash
"Add phone screen note for Jane Smith: [feedback]"
"Add interview note for John Doe: [observations]"
"Add reference check for Bob Johnson: [reference feedback]"
"Get all notes for Jane Smith"
```

### Stage 2 Decisions

```bash
"Run Stage 2 evaluation for Jane Smith with interview score 9/10 and excellent references"
"Compare finalists Jane Smith, John Doe, and Bob Johnson"
"Generate final hiring recommendation"
```

### Exports

```bash
"Export all candidates to Excel"
"Export phone screen candidates to Excel"
"Export interview candidates to Excel"
"Generate comparison report for finalists"
```

---

## Key Features Explained

### Cover Letter Analysis

Cover letters are automatically evaluated as part of Application Quality (25% of Risk Flags component).

**What's evaluated:**
- Customization level (generic vs. personalized)
- Research depth (knowledge of organization)
- Writing quality (grammar, structure, professionalism)
- Fit articulation (why this role, why this organization)
- Gap addressing (proactive explanation of concerns)

**Scoring:**
- 90-100: Exceptional (adds ~1 point to overall)
- 80-89: Strong (adds ~0.3 points)
- 75-79: Adequate (neutral impact)
- 60-74: Weak (subtracts ~0.5 points)
- Below 60: Concerning (subtracts ~1 point)

### Verification Questions

For each candidate, Claude generates 3-5 specific questions to ask during phone screens:

**Example:**
- "Can you walk me through your specific contributions to the distributed systems project?"
- "You mentioned a 6-month gap between roles - what were you working on during that time?"
- "I see you transitioned from data science to engineering - how did you build up your backend skills?"

These questions maximize the value of limited phone screen time.

### Persistent Tracking

The SQLite database stores:
- All candidate information (name, resume, contact)
- All evaluations (with timestamps and scores)
- All notes (phone screens, interviews, references)
- All stage transitions (who moved where and when)
- All shortlist decisions

**Benefits:**
- Add candidates incrementally over weeks
- Never lose track of who you've evaluated
- Full audit trail for compliance
- Query historical data anytime

---

## Output Formats

### Screen and Rank Report (Default for Bulk)

Clean, executive-ready format with:
- Summary rankings table
- Individual candidate tables (stars, scores, strengths, concerns)
- Proposed actions
- Brief methodology explanation

See [SCREEN_AND_RANK_EXAMPLE.md](SCREEN_AND_RANK_EXAMPLE.md) for complete example.

### Detailed Evaluation (Single Candidate)

Comprehensive breakdown with:
- Q/E/R score components
- Risk Flags sub-components table
- Application Quality analysis with cover letter evidence
- Verification questions
- Detailed strengths and concerns

### Stage 2 Final Decision Report

Synthesis of all hiring data:
- Resume/Interview/Reference score breakdown
- Where interview contradicted or confirmed resume
- Reference check highlights
- Final recommendation (STRONG HIRE / HIRE / DO NOT HIRE)
- Confidence level and detailed rationale

### Comparison Reports

Side-by-side finalist analysis:
- Score comparison table
- Strengths/weaknesses of each
- How rankings changed from Stage 1 to Stage 2
- Final recommendation on who to hire

---

## Best Practices

### For Cover Letter Evaluation
- If no cover letter provided and not required → score at 75 (neutral)
- If cover letter provided → score based on quality
- If required but missing → score at 60 or below
- Look for specific evidence of research and customization

### For Stage 1 Screening
- Always infer reasonable requirements if JD is vague
- Evaluate all provided materials (resume + cover letter)
- Generate verification questions for every candidate
- Be specific in strengths and concerns

### For Stage 2 Decisions
- Trust interview performance (50% weight)
- Look for contradictions between resume and interview
- Synthesize patterns across multiple references
- Make clear HIRE / DO NOT HIRE recommendations

### For Database Management
- Update stages promptly as candidates progress
- Add notes after every interaction
- Use tags for easy filtering ([technical_strong], [culture_fit])
- Query before making decisions to ensure you're considering all strong candidates
- Export to Excel for stakeholder reviews

---

## Troubleshooting

**"Claude isn't finding my cover letters"**
- Name them clearly: `candidate_name_cover_letter.pdf`
- Put them in the same `resumes/` folder
- Supported formats: .pdf, .docx, .doc

**"Scores seem off"**
- Review job_description.txt - are requirements clear?
- Check years of experience range
- Verify must-haves vs. preferreds
- Ask: "Explain the score for [Candidate Name]"

**"Cover letter not being evaluated"**
- Ensure cover letter file is in resumes/ folder
- Check file naming (should include "cover" or "letter")
- Ask: "Did you evaluate the cover letter for [Candidate]?"

**"Database isn't updating"**
- Verify recruiting.db exists in current folder
- Try: "Check database status"
- If corrupted: Delete recruiting.db and re-evaluate (WARNING: loses data)

---

## Additional Resources

- **Full Methodology**: See [EVALUATION_METHODOLOGY.md](EVALUATION_METHODOLOGY.md)
- **Example Output**: See [SCREEN_AND_RANK_EXAMPLE.md](SCREEN_AND_RANK_EXAMPLE.md)
- **Database Architecture**: See [SQLITE_ARCHITECTURE.md](SQLITE_ARCHITECTURE.md)
- **Installation Guide**: See [INSTALLATION.md](INSTALLATION.md)
- **What's New**: See [STATUS.md](STATUS.md)

---

## Version History

- **v3.0** (2025-11-04): Unified recruiting-tracker skill
  - Merged recruiting-evaluation and recruiting-evaluation-skill ver2
  - Two-stage framework (resume + post-interview)
  - Cover letter analysis in Application Quality
  - Candidate-specific verification questions
  - SQLite database for persistent tracking
  - Auto folder initialization
  - Excel exports and historical tracking
  - Supports 1 to 100+ candidates

---

## Support

This skill is based on:
- Schmidt & Hunter (1998) meta-analysis on selection validity
- EEOC Uniform Guidelines on Employee Selection Procedures
- Society for Industrial and Organizational Psychology (SIOP) principles

For questions or improvements, modify the SKILL.md file directly.

---

## License

This skill is provided as-is for internal recruiting use. The methodology is based on established research and best practices in industrial-organizational psychology.
