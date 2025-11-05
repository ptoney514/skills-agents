# Caching Instructions for Recruiting Evaluation Skill

## Overview

To avoid re-evaluating candidates unnecessarily, this skill uses a **dual-file caching system**:

1. **`.evaluation_cache.json`** - Fast lookup for Claude (programmatic)
2. **`candidate_scores.xlsx`** - Human-readable tracking file (review/export)

Both files live in the same directory as the job description and resumes.

---

## How Caching Works

### Initial Evaluation (First Run)

When evaluating candidates for the first time:

1. **Check for existing cache**
   ```bash
   # Look for .evaluation_cache.json in current directory
   # If not found, this is a new evaluation
   ```

2. **Process all resumes**
   - Score each candidate using Q/E/R formulas
   - Store results in memory

3. **Create cache files**
   ```json
   # Create .evaluation_cache.json
   {
     "job_title": "extracted from JD",
     "job_description_file": "job_description.txt",
     "last_updated": "ISO timestamp",
     "candidates": {
       "filename.pdf": {
         "name": "Candidate Name",
         "last_position": "Title - Company",
         "q_score": 98.2,
         "e_score": 87.2,
         "r_score": 90,
         "overall_score": 92.5,
         "stars": 5,
         "recommendation": "Strong Candidate",
         "evaluated_date": "ISO timestamp",
         "strengths": ["strength 1", "strength 2"],
         "concerns": ["concern 1", "concern 2"]
       }
     }
   }
   ```

4. **Create Excel tracking file**
   - Export to `candidate_scores.xlsx`
   - Include all scores, recommendations, and metadata
   - Format as table with filters enabled

5. **Generate report**
   - Create Screen and Rank Report as normal

### Incremental Evaluation (Adding New Candidates)

When user adds new resumes to the folder:

1. **Load existing cache**
   ```python
   # Read .evaluation_cache.json
   # Get list of already-evaluated filenames
   ```

2. **Identify new candidates**
   ```python
   # Compare resume files in folder vs. cached filenames
   # Only process NEW files
   ```

3. **Evaluate new candidates only**
   - Score new candidates using formulas
   - Add to in-memory results

4. **Merge results**
   ```python
   # Combine cached scores + new scores
   # Sort by overall score (highest to lowest)
   ```

5. **Update cache files**
   - Update `.evaluation_cache.json` with new candidates
   - Update `candidate_scores.xlsx` with complete list
   - Update "last_updated" timestamp

6. **Generate updated report**
   - Include ALL candidates (cached + new)
   - Full Screen and Rank Report

### Re-evaluation (Forcing Fresh Scores)

If user explicitly asks to re-evaluate (e.g., "re-score all candidates" or "ignore cache"):

1. **Delete existing cache** (optional)
2. **Process all resumes fresh**
3. **Overwrite cache files**

---

## Cache File Locations

### Standard Setup:
```
/Users/username/recruiting/job-folder/
├── job_description.txt
├── resumes/
│   ├── candidate1.pdf
│   └── candidate2.pdf
├── .evaluation_cache.json          ← Created by Claude
├── candidate_scores.xlsx            ← Created by Claude
└── Screen_and_Rank_Report.md       ← Final report
```

### Alternative Setup (if resumes are in same folder as JD):
```
/Users/username/recruiting/job-folder/
├── job_description.txt
├── candidate1.pdf
├── candidate2.pdf
├── .evaluation_cache.json
├── candidate_scores.xlsx
└── Screen_and_Rank_Report.md
```

Claude should detect which structure is being used and adapt.

---

## Excel File Format

### Sheet 1: "Candidate Scores"

| Column | Description | Example |
|--------|-------------|---------|
| Rank | Numerical ranking | 1, 2, 3... |
| Candidate Name | Full name | Cris Riddle |
| Resume File | Filename | cris_riddle_resume.pdf |
| Last Position | Most recent job | VP Internal Audit Programs - Fiserv |
| Q Score | Qualifications (0-100) | 98.2 |
| E Score | Experience (0-100) | 87.2 |
| R Score | Risk Flags (0-100) | 90 |
| Overall Score | Final Evala score | 92.5 |
| Stars | Visual rating | ⭐⭐⭐⭐⭐ |
| Recommendation | Assessment | Strong Candidate |
| Evaluated Date | Timestamp | 2025-11-04 10:15 AM |
| Strengths | Key strengths | [List as text] |
| Concerns | Key concerns | [List as text] |

**Formatting:**
- Header row: Bold, background color
- Filter enabled on all columns
- Freeze top row
- Conditional formatting on Overall Score column (90+ = green, 85-89 = light green, 70-84 = yellow, <70 = red)

### Sheet 2: "Evaluation Summary" (optional)

| Field | Value |
|-------|-------|
| Job Title | Executive Director of Internal Audit |
| Total Candidates | 19 |
| Strong Candidates (90+) | 12 |
| Good Candidates (85-89) | 3 |
| Potential Fit (70-84) | 2 |
| Not a Match (<70) | 2 |
| Last Updated | 2025-11-04 10:30 AM |

---

## Cache Invalidation

The cache should be invalidated (deleted/ignored) when:

1. **Job description changes**
   - Hash or timestamp the JD file
   - If JD modified, re-evaluate all candidates

2. **User explicitly requests**
   - "Start fresh"
   - "Re-evaluate everything"
   - "Ignore previous scores"

3. **Resume file modified**
   - Check file modification timestamp
   - If resume changed, re-evaluate that candidate

---

## Implementation in Python (Example)

```python
import json
import os
from datetime import datetime
from pathlib import Path

def load_cache(job_folder):
    """Load existing evaluation cache."""
    cache_file = Path(job_folder) / ".evaluation_cache.json"
    if cache_file.exists():
        with open(cache_file, 'r') as f:
            return json.load(f)
    return None

def get_new_candidates(job_folder, cache):
    """Identify resumes not yet evaluated."""
    resume_folder = Path(job_folder) / "resumes"
    if not resume_folder.exists():
        # Resumes might be in root folder
        resume_folder = Path(job_folder)
    
    all_resumes = list(resume_folder.glob("*.pdf")) + \
                  list(resume_folder.glob("*.docx"))
    
    if cache is None:
        return all_resumes  # All are new
    
    cached_files = set(cache.get("candidates", {}).keys())
    new_files = [r for r in all_resumes if r.name not in cached_files]
    
    return new_files

def save_cache(job_folder, cache_data):
    """Save evaluation cache to JSON."""
    cache_file = Path(job_folder) / ".evaluation_cache.json"
    with open(cache_file, 'w') as f:
        json.dump(cache_data, f, indent=2)

def export_to_excel(job_folder, all_candidates):
    """Export all candidates to Excel tracking file."""
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill
    
    wb = Workbook()
    ws = wb.active
    ws.title = "Candidate Scores"
    
    # Headers
    headers = ["Rank", "Candidate Name", "Resume File", "Last Position",
               "Q Score", "E Score", "R Score", "Overall Score", 
               "Stars", "Recommendation", "Evaluated Date", 
               "Strengths", "Concerns"]
    
    ws.append(headers)
    
    # Format headers
    for cell in ws[1]:
        cell.font = Font(bold=True)
        cell.fill = PatternFill(start_color="4472C4", 
                                end_color="4472C4", 
                                fill_type="solid")
    
    # Add data
    for i, candidate in enumerate(sorted(all_candidates, 
                                         key=lambda x: x['overall_score'], 
                                         reverse=True), 1):
        ws.append([
            i,
            candidate['name'],
            candidate['filename'],
            candidate['last_position'],
            candidate['q_score'],
            candidate['e_score'],
            candidate['r_score'],
            candidate['overall_score'],
            candidate['stars'],
            candidate['recommendation'],
            candidate['evaluated_date'],
            "; ".join(candidate['strengths']),
            "; ".join(candidate['concerns'])
        ])
    
    # Enable filters
    ws.auto_filter.ref = ws.dimensions
    
    # Save
    excel_file = Path(job_folder) / "candidate_scores.xlsx"
    wb.save(excel_file)
```

---

## Workflow Integration

### Step 1: Check for Cache
```python
cache = load_cache(job_folder)
if cache:
    print(f"Found existing evaluation cache from {cache['last_updated']}")
    print(f"Already evaluated: {len(cache['candidates'])} candidates")
```

### Step 2: Identify New Candidates
```python
new_candidates = get_new_candidates(job_folder, cache)
if new_candidates:
    print(f"Found {len(new_candidates)} new candidates to evaluate")
else:
    print("All candidates already evaluated. Using cached scores.")
```

### Step 3: Evaluate New Candidates Only
```python
for resume_file in new_candidates:
    # Read resume
    # Extract requirements from JD
    # Calculate Q, E, R scores
    # Store in results
```

### Step 4: Merge and Export
```python
# Combine cached + new results
all_results = cache['candidates'] if cache else {}
all_results.update(new_results)

# Update cache
save_cache(job_folder, {
    "job_title": job_title,
    "last_updated": datetime.now().isoformat(),
    "candidates": all_results
})

# Export to Excel
export_to_excel(job_folder, all_results)

# Generate report
create_screen_and_rank_report(all_results)
```

---

## User Communication

When using cache, inform the user:

**If using cached scores:**
```
✅ Found evaluation cache from November 4, 2025
📊 Already evaluated: 15 candidates
🆕 New candidates to evaluate: 4

Processing new candidates only...
[Evaluation results]

✅ Updated candidate_scores.xlsx with all 19 candidates
```

**If starting fresh:**
```
🆕 No previous evaluation found. Evaluating all candidates...
📊 Total candidates: 19

[Evaluation results]

✅ Created candidate_scores.xlsx for future reference
```

---

## Benefits

1. **Faster re-runs**: Only process new candidates
2. **Audit trail**: Excel file shows all evaluations with timestamps
3. **Easy comparison**: Add candidates incrementally without re-scoring everyone
4. **User-friendly**: Excel file is readable and exportable
5. **Reliable**: JSON cache prevents data corruption issues

---

## File Management Best Practices

1. **Don't commit cache files to git**
   - Add `.evaluation_cache.json` to `.gitignore`
   - Excel file is fine to commit (user data)

2. **Clean old caches**
   - If JD changes significantly, delete cache
   - Start fresh evaluation

3. **Backup Excel files**
   - Before re-running, copy Excel file
   - Example: `candidate_scores_backup_2025-11-04.xlsx`

---

## Version History

- **v1.0** (2025-11-04): Initial caching system design
