---
name: recruiting-evaluation
description: Evaluate job candidates using evidence-based scoring methodology. Use when screening resumes, ranking applicants against job descriptions, or creating hiring reports. Applies mathematical Q(40%)+E(40%)+R(20%) formula for objective, EEOC-compliant candidate assessment. Default output is Screen and Rank format with summary table, strengths/concerns, and recommendations.
---

# Recruiting Evaluation Skill

## Overview

This skill enables Claude to evaluate job candidates using an evidence-based, mathematically rigorous methodology. The default output is a **Screen and Rank Report** - a clean, executive-ready format without detailed calculations or AI explanations.

## When to Use This Skill

Use this skill when you need to:
- Screen and rank job candidates against a job description
- Produce hiring recommendations with numerical justification
- Create executive-ready evaluation reports for hiring managers
- Apply consistent, bias-free evaluation criteria across all candidates

---

## Folder Initialization (For Claude Code Users)

**IMPORTANT**: When a user asks you to "evaluate resumes" or "review resumes" in a folder, FIRST check if the folder is initialized for recruiting.

### Detection Logic

**Check for these files:**
1. Does `recruiting.db` exist in current directory?
2. Does `job_description.txt` exist in current directory?

**If BOTH are missing**, the folder is uninitialized.

### Initialization Prompt

When folder is uninitialized, **STOP** and ask the user:

```
This folder hasn't been set up for recruiting yet. Would you like me to initialize it?

I can create:
- job_description.txt (template with instructions)
- resumes/ folder (for resumes and cover letters)
- recruiting.db (SQLite database)
- HOW_TO_USE.md (job-specific guide)

Reply 'yes' to initialize, or 'no' to cancel.
```

**Wait for user confirmation before proceeding.**

### Initialization Steps

If user confirms with "yes":

1. **Copy templates from skill directory:**
   - Copy `templates/job_description_template.txt` → `job_description.txt`
   - Copy `templates/HOW_TO_USE_template.md` → `HOW_TO_USE.md`

2. **Customize HOW_TO_USE.md:**
   - Replace `{JOB_TITLE}` with "New Position" (or extract from user's message if mentioned)
   - Replace `{FOLDER_PATH}` with current working directory path
   - Replace `{FOLDER_NAME}` with current directory name
   - Replace `{DATE}` with current date

3. **Create directory structure:**
   ```bash
   mkdir -p resumes/
   ```

4. **Create empty SQLite database:**
   ```python
   from recruiting_database import RecruitingDatabase
   db = RecruitingDatabase('recruiting.db')
   db.close()
   ```
   *Do NOT create a job record yet - wait until job_description.txt is filled in.*

5. **Inform user:**
   ```
   ✅ Folder initialized successfully!

   Next steps:
   1. Fill in job_description.txt with job details (fields marked with * are required)
   2. Add candidate resumes and cover letters to resumes/ folder
   3. Ask me to "evaluate resumes" when ready

   See HOW_TO_USE.md for complete instructions.
   ```

### After Initialization

- User fills in `job_description.txt`
- User adds resumes to `resumes/` folder
- When user asks to "evaluate resumes" next time:
  - Folder will be detected as initialized (recruiting.db exists)
  - Read job_description.txt to extract requirements
  - Create job record in database
  - Process resumes
  - Generate reports

### If User Declines Initialization

If user says "no" to initialization:

```
No problem. To use this skill, you'll need:
- job_description.txt with job requirements
- resumes/ folder with candidate resumes
- I can help set this up manually - just let me know!
```

---

## Default Output: Screen and Rank Report

**This is your standard deliverable.** Always produce this format unless explicitly asked otherwise.

### What to Include:

1. **Summary Rankings Table** (at the TOP)
   - Quick comparison view of all candidates
   - Columns: Rank | Candidate | Last Position | Stars | Evala Score | Recommendation

2. **Detailed Candidate Tables** (one per candidate)
   - Columns: RANK | CANDIDATE | LAST POSITION | STARS | MY NOTES | STRENGTHS | CONCERNS | EVALA OVERALL SCORE | RECOMMENDATION
   - ✅ Key Strengths: Up to 5 specific bullet points
   - ⚠️ Key Concerns: Up to 5 specific bullet points

3. **Proposed Actions**
   - Who should be interviewed
   - Any candidate-specific actions needed

4. **Evaluation Methodology**
   - Brief explanation of scoring system (1 paragraph)

### What to EXCLUDE:

❌ **NEVER include these in Screen and Rank reports:**
- AI Reasoning paragraphs (no explanatory essays)
- Suggested Interview Questions
- Detailed Score Breakdowns (Q/E/R calculations like "Q = (95×0.60)+(85×0.25)...")
- Formula explanations for each candidate
- Your internal working notes

The hiring manager only needs: rankings, scores, strengths, concerns, and next steps.

---

## Star Rating & Recommendation System

**Auto-calculate stars from Evala Overall Score:**

```
90-100  → ⭐⭐⭐⭐⭐ → "Strong Candidate"
85-89   → ⭐⭐⭐⭐   → "Good Candidate"
70-84   → ⭐⭐⭐     → "Potential Fit"
60-69   → ⭐⭐       → "Not a Match"
0-59    → ⭐         → "Not a Match"
```

These recommendations are **candidate-quality focused**, not workflow-focused (no "phone screen", "decline", etc.)

---

## Core Scoring Methodology

### Overall Score Formula:
```
Evala Overall Score = (Q × 0.40) + (E × 0.40) + (R × 0.20)

Where:
  Q = Qualifications Score (0-100)
  E = Experience Score (0-100)  
  R = Risk Flags Score (0-100)
```

### Qualifications Score (Q) — Weight: 40%
```
Q = (M × 0.60) + (P × 0.25) + (Ed × 0.10) + (C × 0.05)

Where:
  M = Must-have requirements match (0-100)
  P = Preferred requirements match (0-100)
  Ed = Education alignment (0-100)
  C = Certifications value (0-100)
```

### Experience Score (E) — Weight: 40%
```
E = (Y × 0.40) + (Rp × 0.30) + (I × 0.20) + (Pc × 0.10)

Where:
  Y = Years of experience match (0-100)
  Rp = Role progression/seniority (0-100)
  I = Industry relevance (0-100)
  Pc = Project complexity (0-100)
```

**Years Match Scoring Logic:**
```
If candidate_years < required_minimum:
  Y = (candidate_years / required_minimum) × 70

If required_minimum ≤ candidate_years ≤ required_maximum:
  Y = 100

If candidate_years > required_maximum:
  Y = 100 - ((candidate_years - required_maximum) × 5)
  Y = max(Y, 70)  # Floor at 70 for overqualified candidates
```

### Risk Flags Score (R) — Weight: 20%

Start at 100 and deduct points for:
- **Frequent Job Changes** (-15): 3+ jobs in last 2 years without explanation
- **Employment Gaps** (-10): Unexplained gaps > 6 months
- **Geographic Mismatch** (-10): Requires relocation without stated willingness
- **Overqualification** (-10): 5+ years beyond max required experience
- **Skills Currency** (-15): Most recent relevant work > 3 years ago
- **Lateral Moves** (-5): No progression in 5+ year career
- **Industry Misalignment** (-15): No transferable experience

```
R = 100 - Σ(risk_deductions)
R = max(R, 0)  # Floor at 0
```

**IMPORTANT:** If a gap or concern has a reasonable explanation in the resume/cover letter, DO NOT deduct points. Just note it in the concerns section if relevant.

---

## Evaluation Workflow

### Step 1: Extract Job Requirements

From the job description, identify:
- **Must-Have Requirements**: Skills, experience, education, certifications required
- **Preferred Requirements**: Nice-to-have qualifications
- **Experience Range**: Minimum and maximum years (infer if not stated)
- **Key Criteria**: Leadership needs, industry background, technical skills

If requirements aren't explicit, infer them logically:
- "Senior Engineer" → likely 5-8 years experience
- "Python development" → Python is a must-have
- "Startup environment" → adaptability matters

### Step 2: Score Each Candidate

For each candidate:
1. Calculate Q (Qualifications) score using the formula
2. Calculate E (Experience) score using the formula
3. Calculate R (Risk Flags) score using deductions
4. Calculate Overall Score: (Q × 0.40) + (E × 0.40) + (R × 0.20)
5. Assign star rating based on Overall Score
6. Assign recommendation based on Overall Score

### Step 3: Create Screen and Rank Report

Generate the report using the **exact format** specified in the Output Template below.

---

## Output Template: Screen and Rank Report

Use this EXACT structure for all Screen and Rank reports:

```markdown
# Candidate Screening Report
**Position**: [Job Title]  
**Evaluation Date**: [Date]  
**Number of Candidates Reviewed**: [X]  
**Report Type**: Screen and Rank

---

## Summary Rankings Table

| **Rank** | **Candidate** | **Last Position** | **Stars** | **Evala Score** | **Recommendation** |
|----------|---------------|-------------------|-----------|-----------------|-------------------|
| #1 | [Name] | [Title - Company] | ⭐⭐⭐⭐⭐ | XX.X | **Strong Candidate** |
| #2 | [Name] | [Title - Company] | ⭐⭐⭐⭐ | XX.X | **Good Candidate** |
| #3 | [Name] | [Title - Company] | ⭐⭐⭐ | XX.X | **Potential Fit** |

*Evala scores combine qualifications (40%), experience (40%), and risk factors (20%). Higher scores indicate better fit.*

---

## Detailed Candidate Analysis

---

### Candidate #1 - [Full Name]

| **RANK** | **CANDIDATE** | **LAST POSITION** | **STARS** | **MY NOTES** | **EVALA OVERALL SCORE** | **RECOMMENDATION** |
|----------|---------------|-------------------|-----------|--------------|------------------------|-------------------|
| #1 | **[Name]** | [Title - Company] | ⭐⭐⭐⭐⭐ | [Leave blank or add notes] | **XX.X** | **Strong Candidate** |

#### ✅ Key Strengths
- [Specific strength 1 - tied to job requirements]
- [Specific strength 2 - notable achievement]
- [Specific strength 3 - relevant credential or experience]
- [Optional strength 4]
- [Optional strength 5]

#### ⚠️ Key Concerns
- [Specific concern 1 - gap or clarification needed]
- [Specific concern 2 - risk factor if applicable]
- [Optional concern 3]

---

### Candidate #2 - [Full Name]

[Repeat same table and strengths/concerns format]

---

## Proposed Actions

**Schedule Interviews** ([X] candidates with 85+ scores)
- **[Candidate Name]** - Score: XX.X/100
- **[Candidate Name]** - Score: XX.X/100

**Consider for Phone Screen** ([X] candidates with 70-84 scores, if applicable)
- **[Candidate Name]** - Score: XX.X/100
  - Focus areas: [Specific concern 1], [Specific concern 2]

**Candidate-Specific Actions** (if needed):
- **[Candidate Name]**: [Specific action like "Verify degree completion" or "Discuss relocation plans"]

---

## Evaluation Methodology

This evaluation used the **Evidence-Based Candidate Assessment Framework**:

**Formula**: Evala Overall Score = (Q × 0.40) + (E × 0.40) + (R × 0.20)

- **Qualifications (Q)**: Must-haves (60%), Preferreds (25%), Education (10%), Certifications (5%)
- **Experience (E)**: Years (40%), Progression (30%), Industry Relevance (20%), Complexity (10%)
- **Risk Flags (R)**: Deductive scoring from 100 baseline

**Star Rating System:**
- ⭐⭐⭐⭐⭐ (90-100) = Strong Candidate
- ⭐⭐⭐⭐ (85-89) = Good Candidate
- ⭐⭐⭐ (70-84) = Potential Fit
- ⭐⭐ (60-69) = Not a Match
- ⭐ (0-59) = Not a Match

All scores are objective, repeatable, and legally defensible per EEOC guidelines.

---

**Report Generated**: [Date and Time]
```

---

## Writing Effective Strengths & Concerns

### ✅ GOOD Examples (Specific and Actionable):

**Strengths:**
- "15 years audit experience with CIA and CRMA certifications (both preferred credentials)"
- "Led $2M+ projects at Fortune 500 company with demonstrated P&L ownership"
- "Master's degree from accredited institution with relevant thesis work"
- "Healthcare industry background directly matches organization's sector"
- "Omaha-based candidate (no relocation required)"

**Concerns:**
- "Management experience limited to 5 years vs. 7-10 year requirement"
- "Four job changes in last 3 years without explanation (stability concern)"
- "Financial services background may require orientation to higher education environment"
- "15 years beyond maximum experience requirement (overqualification risk)"
- "Most recent Python work was 4 years ago (skills currency question)"

### ❌ BAD Examples (Generic and Vague):

**Strengths:**
- "Strong background" ← Too vague, what specifically?
- "Good experience" ← Doesn't tell the hiring manager anything
- "Impressive resume" ← Generic and unhelpful

**Concerns:**
- "Some gaps" ← How long? Where?
- "Career progression concern" ← What's the specific issue?
- "May not be a fit" ← Why? Be specific.

---

## Best Practices

### 1. Always Infer Reasonable Requirements
If the JD doesn't explicitly state requirements, infer them logically:
- "Senior Engineer" → likely 5-8 years experience
- "Python development" → Python is a must-have
- "Startup environment" → adaptability and ambiguity tolerance matter
- "Director" role → likely needs 7-10 years total, 3-5 in management

### 2. Handle Explained Gaps Gracefully
If a resume explains a gap (grad school, caregiving, sabbatical, relocation), DO NOT penalize. Just note it if relevant to the role.

### 3. Be Specific in Strengths/Concerns
Every bullet point should be actionable and tied to job requirements. Avoid generic praise or vague concerns.

### 4. Maintain Objectivity
- Use the formulas consistently
- Don't let one impressive credential override systematic scoring
- Apply same standards to all candidates for the same role

### 5. Focus on Hiring Manager Needs
The report is for a busy hiring manager who needs to make decisions quickly. Give them:
- Clear rankings
- Specific reasons to interview or not interview
- Actionable next steps

---

## Example Scoring Scenario

**Job**: Senior Software Engineer  
**Requirements**: 5-7 years Python, CS degree preferred, distributed systems experience

**Candidate**: 6 years Python, BS Computer Science, led 2 distributed systems projects, 4-month gap (explained: relocation), steady progression Jr → Mid → Senior

**Scoring:**

**Q (Qualifications):** M=100 (all must-haves met), P=100 (CS degree), Ed=90, C=0  
→ Q = (100×0.60)+(100×0.25)+(90×0.10)+(0×0.05) = **94.0**

**E (Experience):** Y=100 (6 years in 5-7 range), Rp=85, I=100, Pc=90  
→ E = (100×0.40)+(85×0.30)+(100×0.20)+(90×0.10) = **94.5**

**R (Risk Flags):** Starting 100, Gap=0 (explained), Job changes=0  
→ R = **100**

**Overall:** (94×0.40)+(94.5×0.40)+(100×0.20) = **95.4**  
**Stars:** ⭐⭐⭐⭐⭐  
**Recommendation:** Strong Candidate

---

## When NOT to Use Default Format

If the user specifically requests:
- "Show me the detailed calculations" → Include Q/E/R breakdowns
- "Give me interview questions" → Add suggested questions section
- "Explain your reasoning" → Include AI reasoning paragraphs
- "Just evaluate this one candidate" → Use same format but single candidate

Otherwise, always use the clean Screen and Rank format.

---

## Integration with Other Tools

This skill works seamlessly with:
- **File reading**: Parse resumes (PDF, DOCX, TXT)
- **Spreadsheet creation**: Export rankings to XLSX
- **Document generation**: Create formatted reports in DOCX

When using with Claude Code, the skill can:
1. Read a batch of resume files from a directory
2. Process them programmatically
3. Generate Screen and Rank report
4. Export to hiring manager-ready formats

---

## SQLite Database System (Persistent Candidate Tracking)

**This skill uses SQLite for persistent candidate tracking** across multiple evaluation rounds, shortlisting stages, and iterative refinement.

### How It Works:

1. **First Evaluation:**
   - Claude creates `recruiting.db` in your job folder
   - Processes all resumes and stores evaluations in database
   - Exports `candidate_scores.xlsx` for review
   - Generates Screen and Rank Report

2. **Adding New Candidates:**
   - User drops new resumes into the folder
   - Claude checks database for existing candidates
   - **Only evaluates NEW resumes** (saves time!)
   - Updates database and Excel export
   - Regenerates report with ALL candidates (old + new)

3. **Stage Management:**
   - Move candidates through stages: new → screened → phone_screen → interview → final_round → offer
   - Track who moved to each stage and when
   - Add notes from interviews, phone screens, reference checks
   - Query candidates by stage or score

4. **Historical Tracking:**
   - All evaluations stored with timestamps
   - View evaluation history for any candidate
   - Track notes and decisions over time
   - Full audit trail of recruiting process

### File Structure:

```
job-folder/
├── job_description.txt
├── resumes/
│   ├── candidate1.pdf
│   ├── candidate2.pdf
│   └── candidate3.pdf           ← Add new ones here
├── recruiting.db                 ← SQLite database (source of truth)
├── candidate_scores.xlsx         ← Generated on demand
└── Screen_and_Rank_Report.md    ← Generated on demand
```

### Database Tables:

- **jobs** - Job requisitions being recruited for
- **candidates** - Candidate information and resume metadata
- **evaluations** - All evaluation scores (supports re-evaluation history)
- **evaluation_details** - Strengths, concerns, score breakdowns
- **notes** - Interview notes, phone screen feedback, etc.
- **shortlists** - Stage transitions and shortlist decisions

### Common Commands:

**Initial evaluation:**
```
"Evaluate all resumes in this folder"
```

**Add new candidates:**
```
"Check for new resumes and evaluate them"
```

**Query candidates:**
```
"Show me all candidates with 85+ scores who haven't been interviewed yet"
"Show me candidates in the phone screen stage"
```

**Stage management:**
```
"Move Jane Smith to phone screen stage"
"Add these candidates to interview shortlist: [names]"
```

**Add notes:**
```
"Add interview note for John Doe: Great cultural fit, strong technical skills"
```

**Export reports:**
```
"Export all candidates to Excel"
"Generate comparison report for top 3 finalists"
"Show me evaluation history for Jane Smith"
```

### Database Behavior:

**Check for existing database:**
- Look for `recruiting.db` in current directory
- If found, load existing job and candidate data
- If not found, create new database

**Identify new candidates:**
- Query database for existing resume filenames
- Only process files not in database
- Store new evaluations with timestamps

**Update database:**
- All changes immediately saved to SQLite
- Export Excel files on demand
- Generate reports from current database state

**Inform user:**
```
✅ Found existing recruiting database
📊 Already evaluated: 15 candidates
🆕 New candidates to evaluate: 4

Processing new candidates only...
```

### When to Re-evaluate:

Re-evaluation should occur when:
- Job description file is modified (different requirements)
- User explicitly says "re-evaluate all candidates"
- Resume file has been significantly updated

### Excel Export Files:

Generated on demand from database:
- **candidate_scores.xlsx** - All candidates with scores, strengths, concerns
- **phone_screen_list.xlsx** - Candidates in phone screen stage
- **interview_candidates.xlsx** - Candidates in interview stage
- **finalist_comparison.xlsx** - Side-by-side comparison of finalists

All exports include filters, formatting, and timestamps.

For complete database schema and API details, see [SQLITE_ARCHITECTURE.md](SQLITE_ARCHITECTURE.md).

---

## Compliance & Legal Considerations

This methodology is designed for:
- ✅ EEOC compliance (job-related criteria only)
- ✅ Consistent application across all candidates
- ✅ Documented decision-making process
- ✅ Adverse impact monitoring

**Remember:**
- Apply same standards to every candidate for the same role
- Don't use protected characteristics (age, race, gender) in scoring
- Keep audit trail of all scores and decisions
- Review for disparate impact regularly

---

## Support Files

This skill references:
- `EVALUATION_METHODOLOGY.md` - Full mathematical framework and research foundation
- `SCREEN_AND_RANK_EXAMPLE.md` - Sample output showing exact format expected
- `SQLITE_ARCHITECTURE.md` - Complete database schema and implementation details
- `recruiting_database.py` - SQLite database wrapper class
- `excel_exporter.py` - Excel export functions
- `templates/job_description_template.txt` - Template for new job folders
- `templates/HOW_TO_USE_template.md` - Job-specific guide template

For detailed methodology documentation, see [EVALUATION_METHODOLOGY.md](EVALUATION_METHODOLOGY.md).

For database schema and API, see [SQLITE_ARCHITECTURE.md](SQLITE_ARCHITECTURE.md).

---

## Version History

- **v2.2** (2025-11-04): Added automatic folder initialization with templates and job-specific guide
- **v2.1** (2025-11-04): Added SQLite database support for persistent candidate tracking, stage management, and historical data
- **v2.0** (2025-11-04): Updated with Screen and Rank format, star ratings, simplified recommendations
- **v1.0** (2025-11-04): Initial skill creation with detailed methodology
