---
name: recruiting-tracker
description: Complete recruiting management system with two-stage evaluation framework. Screen resumes with cover letter analysis (Stage 1), synthesize interview feedback for final hiring decisions (Stage 2), and track candidates through hiring funnel with SQLite database. Supports single candidate or bulk evaluation with persistent tracking across weeks/months.
---

# Recruiting Tracker - Complete Recruiting Management System

## Overview

This skill provides a complete end-to-end recruiting solution that combines rigorous candidate evaluation with professional candidate management. It supports both quick one-off evaluations and complex multi-month recruiting campaigns.

**Key Capabilities:**
- **Stage 1: Resume Screening** - Evaluate resumes and cover letters using Q/E/R methodology
- **Stage 2: Post-Interview Decisions** - Synthesize resume + interview + references for final hiring decisions
- **Candidate Management** - Track candidates through hiring funnel with SQLite database
- **Flexible Scale** - Works for 1 candidate or 100+ candidates
- **Persistent Tracking** - Maintain data across weeks/months of recruiting

---

## Two-Stage Evaluation Framework

This skill uses a two-stage process to evaluate candidates:

### Stage 1: Resume Screening (Initial Filter)
- **Purpose:** Identify which candidates to phone screen/interview
- **Input:** Resume, cover letter, application materials
- **Scoring:** Qualifications (40%) + Experience (40%) + Risk Flags (20%)
  - **Risk Flags include:** Employment Gaps + Job Hopping + Skill Currency + **Cover Letter Quality**
- **Output:** 0-100 score + Star rating + Strengths/Concerns + Verification questions
- **Decision Thresholds:**
  - **90-100 (⭐⭐⭐⭐⭐):** Strong Candidate - Interview ASAP
  - **85-89 (⭐⭐⭐⭐):** Good Candidate - Definitely interview
  - **70-84 (⭐⭐⭐):** Potential Fit - Consider for phone screen
  - **Below 70:** Not a Match - Decline

### Stage 2: Post-Interview Evaluation (Final Decision)
- **Purpose:** Determine who receives the job offer
- **Input:** Resume score + Interview ratings + Reference checks
- **Scoring:** Resume (25%) + Interview (50%) + References (25%)
- **Output:** Final hire/no-hire recommendation with detailed comparison
- **Key Feature:** Human interviewer feedback weighted at 50% - the most important factor

**Critical Philosophy:** A strong resume gets you to the interview. Your performance in the interview determines if you get the job. Manager/interviewer observations override resume credentials.

---

## When to Use This Skill

Use this skill when you need to:
- Screen and rank job candidates against a job description
- Evaluate cover letters as part of candidate assessment
- Track candidates through multiple hiring stages over time
- Synthesize interview feedback for final hiring decisions
- Manage recruiting campaigns for weeks/months
- Generate executive-ready evaluation reports
- Apply consistent, bias-free evaluation criteria

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
- User adds resumes and cover letters to `resumes/` folder
- When user asks to "evaluate resumes" next time:
  - Folder will be detected as initialized (recruiting.db exists)
  - Read job_description.txt to extract requirements
  - Create job record in database
  - Process resumes and cover letters
  - Generate reports

### If User Declines Initialization

If user says "no" to initialization:

```
No problem. To use this skill, you'll need:
- job_description.txt with job requirements
- resumes/ folder with candidate resumes and cover letters
- I can help set this up manually - just let me know!
```

---

## Stage 1: Resume Screening

### Core Scoring Methodology

**Overall Score Formula:**
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

**Risk Flags has 4 sub-components, each weighted at 25%:**

**R = (Employment Gaps × 0.25) + (Job Hopping × 0.25) + (Skill Currency × 0.25) + (Application Quality × 0.25)**

#### 1. Employment Gaps (25% of Risk Flags)
- Evaluate context before penalizing
- Valid reasons: caregiving, education, health, layoffs, entrepreneurship
- Focus on skills currency and ability to ramp up
- **Scoring:** 100 = no gaps, 90 = explained gaps, 70 = moderate concerns, <60 = significant unexplained gaps

#### 2. Job Hopping Patterns (25% of Risk Flags)
- Frequent changes without clear progression
- Look for explanations, patterns of growth, or valid reasons
- Consider industry norms (tech vs. other sectors)
- **Scoring:** 100 = stable progression, 90 = logical moves, 70 = some concerns, <60 = concerning pattern

#### 3. Skill Currency (25% of Risk Flags)
- Outdated technical or professional skills
- Continuous learning indicators
- Relevance of recent experience
- **Scoring:** 100 = current skills, 90 = mostly current, 70 = some outdated, <60 = significantly outdated

#### 4. Application Quality (25% of Risk Flags) — **INCLUDES COVER LETTER EVALUATION**
- Cover letter customization and personalization
- Understanding of organization/mission
- Professional writing quality and attention to detail
- Articulation of fit for this specific role
- Addresses resume gaps or career transitions

**Application Quality Scoring:**
- **90-100:** Exceptional cover letter - Highly customized, demonstrates deep research, compelling narrative, excellent writing, addresses gaps proactively
- **80-89:** Strong cover letter - Personalized, clear articulation of fit, professional writing, shows understanding of role
- **75-79:** Adequate cover letter - Generic but acceptable, basic customization, OR no cover letter when not required
- **60-74:** Weak - Template letter with minimal customization, poor writing, or missing when expected
- **Below 60:** Major concerns - Unprofessional, significant errors, missing when required, raises communication concerns

**Note:** Cover letters can differentiate candidates with similar qualifications. A strong cover letter can add 3-5 points to overall score; a weak one can subtract 2-4 points.

**IMPORTANT:** If a gap or concern has a reasonable explanation in the resume/cover letter, DO NOT deduct points. Just note it in the concerns section if relevant.

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

## Stage 1 Output Formats

### Default: Screen and Rank Report (For Multiple Candidates)

**This is your standard deliverable for batch evaluations.** Always produce this format unless explicitly asked otherwise.

#### What to Include:

1. **Summary Rankings Table** (at the TOP)
   - Quick comparison view of all candidates
   - Columns: Rank | Candidate | Last Position | Stars | Evala Score | Recommendation

2. **Detailed Candidate Tables** (one per candidate)
   - Columns: RANK | CANDIDATE | LAST POSITION | STARS | MY NOTES | EVALA OVERALL SCORE | RECOMMENDATION
   - ✅ Key Strengths: Up to 5 specific bullet points
   - ⚠️ Key Concerns: Up to 5 specific bullet points
   - **Candidate-Specific Verification Questions** (3-5 questions to ask in phone screen)

3. **Proposed Actions**
   - Who should be interviewed
   - Any candidate-specific actions needed

4. **Evaluation Methodology**
   - Brief explanation of scoring system (1 paragraph)

#### What to EXCLUDE from Screen and Rank Reports:

❌ **NEVER include these in Screen and Rank reports:**
- AI Reasoning paragraphs (no explanatory essays)
- Suggested Interview Questions (unless explicitly requested)
- Detailed Score Breakdowns (Q/E/R calculations like "Q = (95×0.60)+(85×0.25)...")
- Formula explanations for each candidate
- Your internal working notes

The hiring manager only needs: rankings, scores, strengths, concerns, and next steps.

### Detailed Format (For Single Candidate or When Requested)

When evaluating a single candidate or when user requests detailed analysis:

**STAGE 1: RESUME SCREENING RESULTS**

**Candidate:** [Full Name]
**Score:** [0-100] out of 100
**Recommendation:** [⭐⭐⭐⭐⭐ Strong Candidate / ⭐⭐⭐⭐ Good Candidate / etc.]

**Main Components:**

| Component | Score | Weight | Weighted Score | Notes |
|-----------|-------|--------|----------------|-------|
| Qualifications | [0-100] | 40% | [calc] | [Brief assessment] |
| Experience | [0-100] | 40% | [calc] | [Brief assessment] |
| Risk Flags | [0-100] | 20% | [calc] | See detailed breakdown below |
| **TOTAL** | | | **[Final Score]** | |

**Risk Flags Detailed Breakdown (20% of total):**

| Risk Factor | Score | Weight (of Risk Flags) | Contribution | Notes |
|-------------|-------|------------------------|--------------|-------|
| Employment Gaps | [0-100] | 25% | [calc] | [Gap assessment] |
| Job Hopping | [0-100] | 25% | [calc] | [Pattern assessment] |
| Skill Currency | [0-100] | 25% | [calc] | [Currency assessment] |
| Application Quality | [0-100] | 25% | [calc] | Cover letter evaluation |
| **Risk Flags Total** | **[0-100]** | **100%** | | |

**Application Quality Analysis:**
- **Cover Letter Quality:** [Exceptional/Strong/Adequate/Weak/Missing]
- **Application Quality Score:** [0-100]
- **Impact on Overall Score:** This candidate's application quality [added/subtracted/had neutral effect on] their total score by approximately [X] points compared to a baseline adequate application (score 75).
- **Evidence:**
  - [Specific example 1 from cover letter]
  - [Specific example 2]
  - [Specific example 3]

**Key Strengths:**
• [Strength 1 with specific evidence]
• [Strength 2 with specific evidence]
• [Strength 3 with specific evidence]

**Key Concerns:**
• [Concern 1 requiring interview attention]
• [Concern 2 requiring verification]
• [Concern 3 or "None significant"]

**CANDIDATE-SPECIFIC VERIFICATION QUESTIONS:**
*(Ask these during phone screen to address concerns/gaps identified)*

1. [Question about gap/concern, if applicable]
2. [Question about specific experience validation]
3. [Question about role-critical skill demonstration]

---

## Stage 2: Post-Interview Evaluation

After interviews are conducted, synthesize all information to make final hiring decision.

### Scoring Formula

**Final Score = (Resume Score × 0.25) + (Interview Rating × 0.50) + (Reference Checks × 0.25)**

**Interview performance is weighted at 50% - the most important factor in final decisions.**

### Required Inputs

To perform Stage 2 evaluation, provide:

1. **Resume Score** (from Stage 1) - 25% weight
2. **Interview Rating** (completed by interviewer) - 50% weight
   - Overall interview performance score (1-10, converted to 0-100 scale)
   - Core competency ratings
   - Situational responses
   - Red flags observed
   - Hiring recommendation
3. **Reference Check Notes** (at least 2-3 references) - 25% weight
   - Overall reference ratings (1-10, converted to 0-100 scale)
   - Would rehire assessment
   - Key themes from references

**Note:** Interview rating forms and reference check guides can be generated using the `recruiting-materials` skill.

### Stage 2 Output Format

When user provides interview form(s) and reference notes:

**STAGE 2: FINAL HIRING EVALUATION**

**Candidate:** [Full Name]

| Evaluation Component | Raw Score | Weight | Weighted Score | Notes |
|---------------------|-----------|--------|----------------|-------|
| Resume (Stage 1) | [0-100] | 25% | [calc] | [Stage 1 summary] |
| Interview Performance | [0-100] | 50% | [calc] | [Interview highlights] |
| Reference Checks | [0-100] | 25% | [calc] | [Reference themes] |
| **FINAL SCORE** | | | **[Total]** | |

**Score Interpretation:**
- **90-100:** STRONG HIRE (Excellent across all dimensions)
- **80-89:** HIRE (Solid candidate, recommend offer)
- **70-79:** MARGINAL (Proceed with caution, has reservations)
- **60-69:** DO NOT HIRE (Significant concerns)
- **0-59:** DO NOT HIRE (Not suitable for role)

**KEY INSIGHTS:**

*Where Interview Contradicted Resume:*
• [Example: Resume showed X, but interview revealed Y]
• [Pattern observed during interview]
• [Discrepancy between credentials and demonstrated capability]

*Where Interview Confirmed Resume:*
• [Strength evident in both resume and interview]
• [Verified capability through specific examples]
• [Consistency between written and in-person presentation]

*Reference Check Highlights:*
• [Theme from multiple references]
• [Validation or concern raised]
• [Would rehire assessment and context]

**RECOMMENDATION: [STRONG HIRE / HIRE / DO NOT HIRE / KEEP SEARCHING]**

**Confidence Level:** [High / Medium / Low]

**Rationale:**
[2-3 paragraph explanation of decision, including:
- How interview performance aligned or contradicted resume
- Weight given to interviewer observations vs. credentials
- Reference check validations or concerns
- Why this candidate is/isn't the right fit
- Specific evidence supporting the recommendation]

### Multiple Candidate Comparison (Stage 2)

**If Multiple Candidates Were Interviewed:**

| Rank | Candidate | Final Score | Resume | Interview | References | Recommendation |
|------|-----------|-------------|--------|-----------|------------|----------------|
| 1 | [Name] | [Score] | [Score] | [Score] | [Score] | [Decision] |
| 2 | [Name] | [Score] | [Score] | [Score] | [Score] | [Decision] |
| 3 | [Name] | [Score] | [Score] | [Score] | [Score] | [Decision] |

**Comparative Analysis:**

[Explain:
- Why top candidate stands out
- Key differentiators between candidates
- How interview performance changed initial rankings from Stage 1
- Specific examples where candidates diverged
- Final recommendation on who should receive offer]

---

## SQLite Database System (Persistent Candidate Tracking)

**This skill uses SQLite for persistent candidate tracking** across multiple evaluation rounds, shortlisting stages, and iterative refinement.

### How It Works:

1. **First Evaluation:**
   - Claude creates `recruiting.db` in your job folder
   - Processes all resumes and cover letters, stores evaluations in database
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

5. **Stage 2 Integration:**
   - Store interview ratings in notes table
   - Store reference check feedback in notes table
   - Run Stage 2 evaluation using database data
   - Track final hiring decisions

### File Structure:

```
job-folder/
├── job_description.txt
├── resumes/
│   ├── candidate1.pdf
│   ├── candidate1_cover_letter.pdf
│   ├── candidate2.pdf
│   └── candidate2_cover_letter.docx
├── recruiting.db                 ← SQLite database (source of truth)
├── candidate_scores.xlsx         ← Generated on demand
└── Screen_and_Rank_Report.md    ← Generated on demand
```

### Database Tables:

- **jobs** - Job requisitions being recruited for
- **candidates** - Candidate information and resume metadata
- **evaluations** - All evaluation scores (supports re-evaluation history)
- **evaluation_details** - Strengths, concerns, score breakdowns
- **notes** - Interview notes, phone screen feedback, reference checks
- **shortlists** - Stage transitions and shortlist decisions

### Common Commands:

**Initial evaluation:**
```
"Evaluate all resumes in this folder"
"Evaluate this one candidate with resume and cover letter"
```

**Add new candidates:**
```
"Check for new resumes and evaluate them"
```

**Query candidates:**
```
"Show me all candidates with 85+ scores who haven't been interviewed yet"
"Show me candidates in the phone screen stage"
"Show me top 10 candidates sorted by score"
```

**Stage management:**
```
"Move Jane Smith to phone screen stage"
"Move John Doe to interview stage"
"Add these candidates to interview shortlist: [names]"
```

**Add notes:**
```
"Add phone screen note for John Doe: Strong technical skills, interested in mission"
"Add interview note for Jane Smith: Excellent cultural fit, some concern about timeline"
"Add reference check for Bob Johnson: Former manager gave glowing review, would rehire"
```

**Stage 2 evaluation:**
```
"Run Stage 2 evaluation for Jane Smith using her interview ratings and reference checks"
"Compare final candidates John Doe, Jane Smith, and Bob Johnson with interview data"
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

## Best Practices

### For Stage 1 (Resume Screening):

1. **Always Infer Reasonable Requirements**
   If the JD doesn't explicitly state requirements, infer them logically:
   - "Senior Engineer" → likely 5-8 years experience
   - "Director" role → likely needs 7-10 years total, 3-5 in management
   - "Python development" → Python is a must-have

2. **Evaluate Cover Letters Fairly**
   - Not all roles require cover letters
   - If no cover letter provided and not required → score Application Quality at 75 (neutral)
   - If cover letter provided → score based on quality
   - If cover letter required but missing → penalize accordingly

3. **Handle Explained Gaps Gracefully**
   If a resume or cover letter explains a gap (grad school, caregiving, sabbatical), DO NOT penalize. Just note it if relevant to the role.

4. **Generate Verification Questions**
   For each candidate, create 3-5 specific questions to ask during phone screen that address:
   - Gaps or concerns from resume
   - Verification of key skills
   - Clarification of role transitions

### For Stage 2 (Post-Interview):

1. **Trust Interview Performance**
   Interview ratings are weighted at 50% - the most important factor. If someone interviews poorly despite a strong resume, that should dominate the final decision.

2. **Look for Contradictions**
   Explicitly note where interview revealed something different from resume (better or worse).

3. **Synthesize Reference Checks**
   Look for patterns across multiple references, not just one person's opinion.

4. **Make Clear Recommendations**
   Use STRONG HIRE, HIRE, or DO NOT HIRE. Avoid wishy-washy language.

### For Candidate Management:

1. **Update Stages Promptly**
   Move candidates through stages as decisions are made.

2. **Add Notes After Every Interaction**
   Phone screens, interviews, reference checks - document everything.

3. **Use Tags for Notes**
   Tag notes with keywords for easy filtering: [technical_strong], [culture_fit], [relocation_concern]

4. **Query Before Decisions**
   Use database queries to ensure you're considering all strong candidates.

---

## Evaluation Workflow

### Single Candidate Evaluation

```
User: "Evaluate this resume and cover letter for Senior Software Engineer"
[Provides JD, resume, cover letter]

Claude:
1. Extract requirements from JD
2. Evaluate resume using Q/E/R formula
3. Analyze cover letter (Application Quality component)
4. Calculate overall score
5. Generate verification questions
6. Provide detailed output with score breakdown
```

### Bulk Candidate Evaluation

```
User: "Evaluate all resumes in this folder"

Claude:
1. Check if folder initialized (if not, prompt to initialize)
2. Check for existing recruiting.db
3. Find new resume files
4. For each new candidate:
   - Evaluate resume + cover letter
   - Store in database
5. Generate Screen and Rank Report (all candidates)
6. Export to Excel
```

### Post-Interview Decision

```
User: "Run Stage 2 evaluation for Jane Smith. Her interview score was 9/10,
references were excellent (would rehire), and her Stage 1 score was 88."

Claude:
1. Retrieve Stage 1 score from database (or use provided score)
2. Convert interview rating to 0-100 scale (9/10 = 90)
3. Get reference rating (provided or extract from notes)
4. Calculate: (88 × 0.25) + (90 × 0.50) + (reference × 0.25)
5. Generate Stage 2 report with recommendation
6. Store decision in database
```

---

## Integration with Other Tools

This skill works seamlessly with:
- **File reading**: Parse resumes and cover letters (PDF, DOCX, TXT)
- **Spreadsheet creation**: Export rankings to XLSX
- **recruiting-materials skill**: Generate phone screen scripts and interview guides
- **Document generation**: Create formatted reports in DOCX

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

**Important:** This is a decision support tool. Always have qualified humans make final hiring decisions.

---

## Support Files

This skill references:
- `EVALUATION_METHODOLOGY.md` - Full mathematical framework and research foundation
- `SCREEN_AND_RANK_EXAMPLE.md` - Sample output showing exact format expected
- `SQLITE_ARCHITECTURE.md` - Complete database schema and implementation details
- `recruiting_database.py` - SQLite database wrapper class
- `excel_exporter.py` - Excel export functions
- `test_database.py` - Database validation script
- `templates/job_description_template.txt` - Template for new job folders
- `templates/HOW_TO_USE_template.md` - Job-specific guide template

For detailed methodology documentation, see [EVALUATION_METHODOLOGY.md](EVALUATION_METHODOLOGY.md).

For database schema and API, see [SQLITE_ARCHITECTURE.md](SQLITE_ARCHITECTURE.md).

---

## Version History

- **v3.0** (2025-11-04): Unified recruiting-tracker skill combining evaluation + management
  - Merged recruiting-evaluation and recruiting-evaluation-skill ver2
  - Two-stage framework (resume screening + post-interview decisions)
  - Cover letter analysis in Application Quality component
  - Candidate-specific verification questions
  - SQLite database for persistent tracking
  - Folder initialization with templates
  - Stage management and notes system
  - Excel exports and historical tracking
  - Renamed to "recruiting-tracker" for clarity
