# Recruiting Evaluation Skill

**Version**: 2.2
**Updated**: November 4, 2025
**For**: Claude (claude.ai) and Claude Code

---

## What This Skill Does

This skill evaluates job candidates using a rigorous, evidence-based methodology that produces **Screen and Rank Reports** - clean, executive-ready evaluations with:
- ⭐ Star ratings (5-star system)
- 📊 Objective Evala scores (0-100)
- ✅ Specific strengths tied to job requirements
- ⚠️ Specific concerns or clarifications needed
- 🎯 Clear recommendations: Strong Candidate, Good Candidate, Potential Fit, Not a Match

**Key Benefits:**
- ✅ **Objective** - Mathematical scoring eliminates bias
- ✅ **Repeatable** - Same criteria applied to every candidate
- ✅ **Legally Defensible** - EEOC-compliant, job-related criteria only
- ✅ **Executive-Ready** - Clean format without complex calculations
- ✅ **Research-Based** - Founded on industrial-organizational psychology

---

## Quick Start

### Using with Claude.ai (Web/Desktop)

1. **Create ZIP file**:
   ```bash
   cd /Users/pernelltoney/Documents
   zip -r recruiting-evaluation-skill.zip recruiting-evaluation-skill/
   ```

2. **Upload to Claude.ai**:
   - Go to Settings > Features > Custom Skills
   - Upload the ZIP file
   - Available on Pro, Max, Team, and Enterprise plans
   
3. **Use it**:
   ```
   "Evaluate these 5 candidates for Senior Software Engineer.
   Here's the JD: [paste]
   Resumes attached: [upload files]"
   ```

Claude will automatically produce a Screen and Rank Report.

---

### Using with Claude Code

1. **Copy to skills directory**:
   ```bash
   # Create skills directory if needed
   mkdir -p ~/.claude/skills

   # Copy the skill
   cp -r /Users/pernelltoney/Documents/recruiting-evaluation-skill ~/.claude/skills/
   ```

2. **Create a new job folder** (automatic initialization):
   ```bash
   mkdir ~/recruiting/software-developer
   cd ~/recruiting/software-developer
   claude-code
   # Say: "Evaluate resumes in this folder"

   # Claude will prompt: "This folder hasn't been set up yet. Initialize it?"
   # Reply: "yes"

   # Claude creates:
   # - job_description.txt (template)
   # - resumes/ folder
   # - recruiting.db (database)
   # - HOW_TO_USE.md (guide)
   ```

3. **Fill in job details and add resumes**:
   - Edit `job_description.txt` with job requirements
   - Drop resumes (and cover letters) into `resumes/` folder

4. **Run evaluation**:
   ```bash
   claude-code
   # Say: "Evaluate all resumes"
   ```

---

## What's Included

```
recruiting-evaluation-skill/
├── SKILL.md                          ✅ Main skill file (Claude reads this)
├── SCREEN_AND_RANK_EXAMPLE.md        ✅ Example output showing exact format
├── EVALUATION_METHODOLOGY.md         ✅ Complete mathematical framework
├── SQLITE_ARCHITECTURE.md            ✅ Database schema and implementation
├── recruiting_database.py            🐍 SQLite database wrapper class
├── excel_exporter.py                 🐍 Excel export functions
├── test_database.py                  🧪 Database validation script
├── templates/                        📁 Templates for new job folders
│   ├── job_description_template.txt  ✅ Job description template
│   └── HOW_TO_USE_template.md       ✅ Job-specific guide template
├── CACHING_INSTRUCTIONS.md           📋 Legacy caching docs (reference only)
├── CANDIDATE_EVALUATION_TEMPLATE.MD  📋 Legacy template (reference only)
├── INSTALLATION.md                   📖 Setup instructions
├── README.md                         📖 This file
├── STATUS.md                         📖 What's ready and what changed
└── create-zip.sh                     🛠️ Helper script for creating ZIP
```

---

## Default Output: Screen and Rank Report

Your reports will look like this:

### Summary Rankings Table (Top of Report)
Quick comparison view of all candidates with stars, scores, and recommendations.

### Detailed Candidate Tables
Individual analysis for each candidate with:
- **✅ Key Strengths**: 3-5 specific bullet points tied to job requirements
- **⚠️ Key Concerns**: 1-3 specific issues or clarifications needed
- **Stars**: ⭐⭐⭐⭐⭐ (auto-calculated from score)
- **Recommendation**: Strong Candidate / Good Candidate / Potential Fit / Not a Match

### Proposed Actions
Who to interview, candidate-specific actions needed

### Evaluation Methodology
Brief explanation of scoring system

**What's NOT included:** Detailed calculations, AI reasoning paragraphs, interview questions (unless requested)

See `SCREEN_AND_RANK_EXAMPLE.md` for complete example output.

---

## SQLite Database System (Persistent Tracking!)

**For Claude Code users:** The skill uses SQLite for persistent candidate tracking across multiple evaluation rounds and hiring stages.

### How It Works:

1. **First run**: Evaluates all candidates, creates `recruiting.db` + exports `candidate_scores.xlsx`
2. **Add new candidates**: Only processes NEW resumes, updates database and Excel
3. **Stage management**: Move candidates through phone screen → interview → final round → offer
4. **Add notes**: Track interview feedback, reference checks, hiring manager comments
5. **Query database**: "Show me 85+ candidates not yet interviewed"
6. **Historical tracking**: See evaluation history and how scores changed over time

### Your Folder Structure:

```
job-folder/
├── job_description.txt
├── resumes/
│   ├── candidate1.pdf
│   ├── candidate2.pdf
│   └── candidate3.pdf           ← Drop new resumes here
├── recruiting.db                 ← SQLite database (source of truth)
├── candidate_scores.xlsx         ← Generated on demand
└── Screen_and_Rank_Report.md    ← Generated on demand
```

### Benefits:

- ✅ **Persistent tracking**: Keep data across weeks/months of recruiting
- ✅ **Stage management**: Track candidates through hiring funnel
- ✅ **Interview notes**: Add feedback from phone screens, interviews, references
- ✅ **Query capabilities**: Filter by score, stage, date evaluated
- ✅ **Historical data**: Full audit trail of evaluations and decisions
- ✅ **Excel exports**: Generate reports anytime from database
- ✅ **No re-evaluation**: Add new candidates without re-processing existing ones

### Common Commands:

```bash
# Initial evaluation
"Evaluate all resumes in this folder"

# Add new candidates weeks later
"Check for new resumes and evaluate them"

# Query candidates
"Show me all candidates with 85+ scores who haven't been interviewed yet"

# Stage management
"Move Jane Smith to phone screen stage"

# Add notes
"Add interview note for John Doe: Great cultural fit, strong technical skills"

# Export reports
"Export all candidates to Excel"
"Generate comparison report for top 3 finalists"
```

See [SQLITE_ARCHITECTURE.md](SQLITE_ARCHITECTURE.md) for complete database schema and API documentation.

---

## The Scoring System

### Formula
```
Evala Overall Score = (Q × 0.40) + (E × 0.40) + (R × 0.20)

Where:
  Q = Qualifications (must-haves, preferreds, education, certs)
  E = Experience (years, progression, industry, complexity)
  R = Risk Flags (job hopping, gaps, overqualification, etc.)
```

### Star Ratings
```
90-100  → ⭐⭐⭐⭐⭐ → "Strong Candidate"
85-89   → ⭐⭐⭐⭐   → "Good Candidate"
70-84   → ⭐⭐⭐     → "Potential Fit"
60-69   → ⭐⭐       → "Not a Match"
0-59    → ⭐         → "Not a Match"
```

These are **candidate-quality** recommendations, not workflow steps (no "phone screen", "decline", etc.)

---

## Example Usage

### Scenario: Hiring Executive Director of Internal Audit

**You provide:**
- Job description
- 19 candidate resumes

**Claude delivers:**

```markdown
# Candidate Screening Report

## Summary Rankings Table
| Rank | Candidate | Last Position | Stars | Score | Recommendation |
|------|-----------|---------------|-------|-------|----------------|
| #1 | Cris Riddle | VP - Fiserv | ⭐⭐⭐⭐⭐ | 92.5 | Strong Candidate |
| #2 | Matthew Meyer | Sr Mgr - BCBS | ⭐⭐⭐⭐⭐ | 92.0 | Strong Candidate |
...

## Detailed Candidate Analysis

### Candidate #1 - Cris Riddle
✅ Strengths: 25 years audit, CIA + CRMA certs, Fortune 500 VP...
⚠️ Concerns: Financial services background, relocation needed...

[Continues for each candidate]

## Proposed Actions
Schedule Interviews: Cris Riddle (92.5), Matthew Meyer (92.0)...
```

Clean, scannable, actionable.

---

## Customization

### Adjust Score Thresholds

Edit `SKILL.md` to change what qualifies as "Strong Candidate":

```markdown
# Current:
90-100 → Strong Candidate

# Change to:
92-100 → Strong Candidate
85-91  → Good Candidate
```

### Adjust Formula Weights

If your organization prioritizes experience over qualifications:

```markdown
# Current:
Evala Score = (Q × 0.40) + (E × 0.40) + (R × 0.20)

# Change to:
Evala Score = (Q × 0.30) + (E × 0.50) + (R × 0.20)
```

Always update both `SKILL.md` and `EVALUATION_METHODOLOGY.md` to keep them in sync.

---

## Best Practices

### ✅ Do This:
- Provide complete job descriptions (not just titles)
- Upload clean, readable resumes (avoid scanned images)
- Use for initial screening, not sole hiring factor
- Apply consistently across all candidates for same role

### ❌ Avoid This:
- Don't override scores without documentation
- Don't apply different standards to different candidates
- Don't use as the only hiring criterion
- Don't include protected characteristics in evaluation

---

## Compliance & Legal

This methodology is designed to be:
- **EEOC Compliant**: Job-related criteria only
- **Defensible**: Documented, consistent process
- **Unbiased**: Mathematical scoring reduces unconscious bias
- **Auditable**: Clear trail from resume to decision

**Important**: This is a decision support tool. Always have qualified humans make final hiring decisions.

---

## Troubleshooting

### "Claude isn't using the skill"
- Check that the skill is uploaded/copied correctly
- Mention "recruiting" or "candidates" in your request
- Try: "Use the recruiting-evaluation skill to..."

### "Output doesn't match the format"
- Check `SCREEN_AND_RANK_EXAMPLE.md` for correct format
- Ensure SKILL.md has proper YAML frontmatter
- Re-upload/re-copy the skill files

### "Scores seem off"
- Review job requirements extraction
- Verify candidate experience calculation
- Check for explained gaps (shouldn't be penalized)
- See `EVALUATION_METHODOLOGY.md` for scoring details

---

## Additional Resources

- **Full Methodology**: See [EVALUATION_METHODOLOGY.md](EVALUATION_METHODOLOGY.md)
- **Example Output**: See [SCREEN_AND_RANK_EXAMPLE.md](SCREEN_AND_RANK_EXAMPLE.md)
- **Database Architecture**: See [SQLITE_ARCHITECTURE.md](SQLITE_ARCHITECTURE.md)
- **What's Changed**: See [STATUS.md](STATUS.md)
- **Installation Help**: See [INSTALLATION.md](INSTALLATION.md)

---

## Version History

- **v2.2** (2025-11-04): Added automatic folder initialization with job description template and job-specific guide
- **v2.1** (2025-11-04): Added SQLite database for persistent tracking, stage management, notes, and historical data
- **v2.0** (2025-11-04): Screen and Rank format, star ratings, simplified recommendations
- **v1.0** (2025-11-04): Initial release with detailed methodology

---

## Support

This skill is based on:
- Schmidt & Hunter (1998) meta-analysis on selection validity
- EEOC Uniform Guidelines on Employee Selection Procedures
- Society for Industrial and Organizational Psychology (SIOP) principles

For questions or improvements, modify the `SKILL.md` file directly.

---

## License

This skill is provided as-is for internal recruiting use. The methodology is based on established research and best practices in industrial-organizational psychology.
