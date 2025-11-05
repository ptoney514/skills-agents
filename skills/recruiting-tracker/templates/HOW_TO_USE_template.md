# Recruiting Folder Guide - {JOB_TITLE}

**Job Folder**: `{FOLDER_PATH}`
**Created**: {DATE}
**Status**: Active

---

## Folder Structure

```
{FOLDER_NAME}/
├── job_description.txt       ← Your job requirements (FILL THIS IN FIRST!)
├── resumes/                  ← Drop candidate resumes and cover letters here
│   ├── candidate1.pdf
│   ├── candidate1_cover_letter.pdf
│   ├── candidate2.docx
│   └── ...
├── recruiting.db             ← SQLite database (managed by Claude)
├── candidate_scores.xlsx     ← Excel report (generated on demand)
├── Screen_and_Rank_Report.md ← Evaluation report (generated on demand)
└── HOW_TO_USE.md            ← This file
```

---

## Quick Start Guide

### Step 1: Fill in Job Description
1. Open `job_description.txt`
2. Fill in the required fields (marked with *)
3. Add as much detail as possible for accurate candidate evaluation
4. Save the file

### Step 2: Add Candidate Resumes
1. Drop PDF or DOCX resumes into the `resumes/` folder
2. Cover letters can also be added to the same folder
3. Name files clearly (e.g., `john_doe_resume.pdf`, `jane_smith_cover_letter.pdf`)

### Step 3: Run Initial Evaluation
```bash
cd {FOLDER_PATH}
claude-code
# Say: "Evaluate all resumes in this folder"
```

Claude will:
- Create recruiting database
- Evaluate all candidates using Q/E/R methodology
- Generate candidate scores Excel file
- Produce Screen and Rank Report

---

## Common Commands for This Job

### Evaluate Candidates

**First-time evaluation:**
```
"Evaluate all resumes in this folder"
```

**Add new candidates later:**
```
"Check for new resumes and evaluate them"
```
*Only new resumes will be processed - existing candidates are cached!*

---

### Query & Filter Candidates

**Find top candidates:**
```
"Show me all candidates with 85+ scores"
"Show me candidates with 90+ scores who haven't been interviewed"
```

**Filter by stage:**
```
"Show me candidates in phone screen stage"
"Show me candidates in interview stage"
```

**View candidate details:**
```
"Show me evaluation history for [Candidate Name]"
"Get all notes for [Candidate Name]"
```

---

### Stage Management

**Move candidates through hiring funnel:**
```
"Move [Candidate Name] to phone screen stage"
"Move [Candidate Name] to interview stage"
"Move [Candidate Name] to final round stage"
"Move [Candidate Name] to offer stage"
```

**Add multiple to shortlist:**
```
"Add these candidates to phone screen shortlist: [Name1], [Name2], [Name3]"
```

---

### Add Notes & Feedback

**After phone screen:**
```
"Add phone screen note for [Candidate Name]:
Great technical knowledge, interested in mission-driven work,
available for on-site interview next week"
```

**After interview:**
```
"Add interview note for [Candidate Name]:
Excellent cultural fit, strong leadership examples,
some concern about relocation timeline - needs follow-up"
```

**Internal notes:**
```
"Add internal note for [Candidate Name]:
Hiring manager very interested, fast-track to final round"
```

---

### Generate Reports

**Export all candidates:**
```
"Export all candidates to Excel"
```

**Generate shortlist:**
```
"Export phone screen candidates to Excel"
"Export interview candidates to Excel"
```

**Compare finalists:**
```
"Generate comparison report for [Name1], [Name2], and [Name3]"
```

**Regenerate Screen and Rank report:**
```
"Generate Screen and Rank Report for all candidates"
```

---

## Hiring Stages

Candidates move through these stages:

1. **new** - Just added, not yet evaluated
2. **screened** - Resume evaluated, scores assigned
3. **phone_screen** - Passed initial screening, scheduled for phone call
4. **interview** - Passed phone screen, invited for in-person/video interview
5. **final_round** - Top candidates, final decision pending
6. **offer** - Offer extended
7. **rejected** - Not moving forward
8. **withdrawn** - Candidate withdrew

Use stage management commands to track progress!

---

## Understanding the Scores

### Evala Score Formula
```
Overall Score = (Q × 40%) + (E × 40%) + (R × 20%)

Q = Qualifications (must-haves, preferreds, education, certs)
E = Experience (years, progression, industry, complexity)
R = Risk Flags (job hopping, gaps, overqualification, etc.)
```

### Star Ratings
- ⭐⭐⭐⭐⭐ (90-100) = **Strong Candidate** - Interview ASAP
- ⭐⭐⭐⭐ (85-89) = **Good Candidate** - Definitely interview
- ⭐⭐⭐ (70-84) = **Potential Fit** - Consider for phone screen
- ⭐⭐ (60-69) = **Not a Match** - Pass
- ⭐ (0-59) = **Not a Match** - Pass

---

## Database & Files

### recruiting.db
- SQLite database storing all candidate data
- Managed automatically by Claude
- Contains: candidates, evaluations, notes, shortlists
- **Do not delete** - this is your source of truth!

### candidate_scores.xlsx
- Excel export of all candidates with scores
- Generated on demand
- Includes filters, conditional formatting
- Safe to delete (can be regenerated anytime)

### Screen_and_Rank_Report.md
- Executive-ready candidate report
- Shows rankings, strengths, concerns, recommendations
- Generated on demand
- Safe to delete (can be regenerated anytime)

---

## Tips & Best Practices

### Before Evaluating
- Fill in job_description.txt completely
- Include years of experience range
- List must-have vs. preferred requirements clearly
- Specify any industry experience needed

### During Evaluation
- Add new resumes to resumes/ folder anytime
- Claude only processes NEW files (no re-processing!)
- Cover letters help - include them if available
- Use consistent file naming

### After Evaluation
- Review candidate_scores.xlsx in Excel (easy sorting/filtering)
- Read Screen and Rank Report for detailed analysis
- Add notes after every phone screen / interview
- Update stages as candidates progress
- Export shortlists before scheduling interviews

### Managing the Process
- Check database regularly: "Show me summary statistics"
- Track progress: "How many candidates in each stage?"
- Keep notes organized: Add tags like [technical_strong], [culture_fit]
- Re-evaluate if JD changes: "Re-evaluate all candidates with updated JD"

---

## Troubleshooting

**"Claude isn't finding my resumes"**
- Ensure resumes are in `resumes/` folder (not subfolders)
- Use .pdf or .docx format
- Check file permissions (readable)

**"Scores seem off"**
- Review job_description.txt - are requirements clear?
- Check years of experience range
- Verify must-haves vs. preferreds
- Ask Claude: "Explain the score for [Candidate Name]"

**"Database isn't updating"**
- Make sure recruiting.db exists in this folder
- Try: "Check database status"
- If corrupted: Delete recruiting.db and start fresh (WARNING: loses all data!)

**"Want to start over"**
- Delete recruiting.db
- Keep job_description.txt and resumes/
- Ask Claude to "Evaluate all resumes" again

---

## Need Help?

### Quick Reference
- Full documentation: See skill README.md in `~/.claude/skills/recruiting-evaluation-skill/`
- Methodology details: See EVALUATION_METHODOLOGY.md
- Database schema: See SQLITE_ARCHITECTURE.md
- Example output: See SCREEN_AND_RANK_EXAMPLE.md

### Common Questions

**Q: Can I edit candidate scores?**
A: Scores are auto-generated from the methodology. If they seem wrong, adjust the job description or ask Claude to explain the reasoning.

**Q: How do I delete a candidate?**
A: Currently not supported via commands. You can manually edit the SQLite database or just ignore low-scoring candidates.

**Q: Can I use this for multiple jobs?**
A: Yes! Each job folder has its own database. Keep folders separate.

**Q: What if the JD changes mid-search?**
A: Update job_description.txt and ask Claude to "re-evaluate all candidates with updated job description"

**Q: Can I export to my ATS (Applicant Tracking System)?**
A: Excel exports can be imported to most ATS systems. Check your ATS documentation for CSV/Excel import instructions.

---

## Next Steps

1. ✅ Folder initialized
2. ⬜ Fill in `job_description.txt`
3. ⬜ Add resumes to `resumes/` folder
4. ⬜ Ask Claude to "evaluate resumes"
5. ⬜ Review `candidate_scores.xlsx`
6. ⬜ Read `Screen_and_Rank_Report.md`
7. ⬜ Schedule interviews with top candidates
8. ⬜ Add notes after each interview
9. ⬜ Move candidates through stages
10. ⬜ Make hiring decision!

---

**Good luck with your search!** 🎯
