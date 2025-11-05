# SQLite Architecture for Recruiting Evaluation Skill

## Overview

This document proposes a SQLite-based architecture for persistent candidate tracking across multiple evaluation rounds, shortlisting stages, and iterative refinement.

## Database Schema

### Table: `jobs`

Tracks job requisitions being recruited for.

```sql
CREATE TABLE jobs (
    job_id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_title TEXT NOT NULL,
    job_description_file TEXT,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status TEXT DEFAULT 'active',  -- active, filled, cancelled
    notes TEXT
);
```

### Table: `candidates`

Stores candidate information and resume metadata.

```sql
CREATE TABLE candidates (
    candidate_id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_id INTEGER NOT NULL,
    full_name TEXT NOT NULL,
    resume_filename TEXT NOT NULL,
    resume_file_path TEXT,
    file_hash TEXT,  -- To detect file changes
    first_seen_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    current_stage TEXT DEFAULT 'new',  -- new, screened, phone_screen, interview, final_round, offer, rejected, withdrawn
    FOREIGN KEY (job_id) REFERENCES jobs(job_id),
    UNIQUE(job_id, resume_filename)
);
```

### Table: `evaluations`

Tracks all evaluation scores (allows re-evaluation history).

```sql
CREATE TABLE evaluations (
    evaluation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    candidate_id INTEGER NOT NULL,
    evaluation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    evaluation_type TEXT DEFAULT 'initial',  -- initial, re-screen, post-interview

    -- Scores
    q_score REAL,
    e_score REAL,
    r_score REAL,
    overall_score REAL,

    -- Derived fields
    stars INTEGER,
    recommendation TEXT,
    last_position TEXT,

    -- Context
    job_description_hash TEXT,  -- Track if JD changed

    FOREIGN KEY (candidate_id) REFERENCES candidates(candidate_id)
);
```

### Table: `evaluation_details`

Stores strengths, concerns, and detailed breakdown.

```sql
CREATE TABLE evaluation_details (
    detail_id INTEGER PRIMARY KEY AUTOINCREMENT,
    evaluation_id INTEGER NOT NULL,
    strengths TEXT,  -- JSON array
    concerns TEXT,   -- JSON array
    score_breakdown TEXT,  -- JSON with Q/E/R components
    FOREIGN KEY (evaluation_id) REFERENCES evaluations(evaluation_id)
);
```

### Table: `notes`

Tracks notes from interviews, phone screens, reference checks.

```sql
CREATE TABLE notes (
    note_id INTEGER PRIMARY KEY AUTOINCREMENT,
    candidate_id INTEGER NOT NULL,
    note_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    note_type TEXT,  -- phone_screen, interview, reference_check, internal, hiring_manager
    author TEXT,     -- Who wrote the note
    content TEXT NOT NULL,
    tags TEXT,       -- JSON array for filtering
    FOREIGN KEY (candidate_id) REFERENCES candidates(candidate_id)
);
```

### Table: `shortlists`

Tracks shortlist decisions and stage transitions.

```sql
CREATE TABLE shortlists (
    shortlist_id INTEGER PRIMARY KEY AUTOINCREMENT,
    candidate_id INTEGER NOT NULL,
    stage TEXT NOT NULL,  -- phone_screen, interview, final_round, offer
    added_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    added_by TEXT,
    decision_rationale TEXT,
    FOREIGN KEY (candidate_id) REFERENCES candidates(candidate_id)
);
```

### Table: `comparisons`

Tracks side-by-side comparisons for final decisions.

```sql
CREATE TABLE comparisons (
    comparison_id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_id INTEGER NOT NULL,
    comparison_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    candidate_ids TEXT,  -- JSON array of candidate IDs
    notes TEXT,
    final_decision TEXT,
    FOREIGN KEY (job_id) REFERENCES jobs(job_id)
);
```

---

## Query Examples

### Get current top candidates for a job

```sql
SELECT
    c.full_name,
    c.current_stage,
    e.overall_score,
    e.stars,
    e.recommendation,
    e.evaluation_date
FROM candidates c
JOIN evaluations e ON c.candidate_id = e.candidate_id
WHERE c.job_id = 1
  AND e.evaluation_id = (
      SELECT evaluation_id
      FROM evaluations
      WHERE candidate_id = c.candidate_id
      ORDER BY evaluation_date DESC
      LIMIT 1
  )
ORDER BY e.overall_score DESC;
```

### Get candidates ready for interview (85+ score, screened stage)

```sql
SELECT
    c.full_name,
    e.overall_score,
    e.stars,
    c.current_stage
FROM candidates c
JOIN evaluations e ON c.candidate_id = e.candidate_id
WHERE c.job_id = 1
  AND e.overall_score >= 85
  AND c.current_stage = 'screened'
  AND e.evaluation_id = (
      SELECT evaluation_id
      FROM evaluations
      WHERE candidate_id = c.candidate_id
      ORDER BY evaluation_date DESC
      LIMIT 1
  );
```

### Show evaluation history for a candidate

```sql
SELECT
    e.evaluation_date,
    e.evaluation_type,
    e.overall_score,
    e.stars,
    e.recommendation
FROM evaluations e
WHERE e.candidate_id = 5
ORDER BY e.evaluation_date ASC;
```

### Get all notes for a candidate

```sql
SELECT
    n.note_date,
    n.note_type,
    n.author,
    n.content
FROM notes n
WHERE n.candidate_id = 5
ORDER BY n.note_date DESC;
```

### Compare shortlisted candidates

```sql
SELECT
    c.full_name,
    c.current_stage,
    e.overall_score,
    e.stars,
    COUNT(n.note_id) as note_count,
    MAX(n.note_date) as last_note_date
FROM candidates c
JOIN evaluations e ON c.candidate_id = e.candidate_id
LEFT JOIN notes n ON c.candidate_id = n.candidate_id
WHERE c.job_id = 1
  AND c.current_stage IN ('interview', 'final_round')
  AND e.evaluation_id = (
      SELECT evaluation_id
      FROM evaluations
      WHERE candidate_id = c.candidate_id
      ORDER BY evaluation_date DESC
      LIMIT 1
  )
GROUP BY c.candidate_id
ORDER BY e.overall_score DESC;
```

---

## Workflow Integration

### 1. Initial Evaluation (First Run)

```python
# Create database if not exists
db = Database('recruiting.db')

# Create job record
job_id = db.create_job(
    title="Executive Director of Internal Audit",
    jd_file="job_description.txt"
)

# Scan resumes folder
for resume_file in resume_files:
    # Check if candidate exists
    candidate = db.get_candidate_by_filename(job_id, resume_file.name)

    if not candidate:
        # New candidate - evaluate
        scores = evaluate_candidate(resume_file, job_description)

        # Insert candidate
        candidate_id = db.insert_candidate(
            job_id=job_id,
            name=scores['name'],
            resume_filename=resume_file.name,
            resume_path=str(resume_file),
            file_hash=hash_file(resume_file)
        )

        # Insert evaluation
        db.insert_evaluation(candidate_id, scores)

# Export to Excel
db.export_to_excel(job_id, 'candidate_scores.xlsx')

# Generate report
db.generate_screen_and_rank_report(job_id)
```

### 2. Adding New Candidates (Incremental)

```python
# Open existing database
db = Database('recruiting.db')

# Get job
job_id = db.get_active_job()

# Find new resumes
new_resumes = db.find_new_resumes(job_id, resume_folder)

if new_resumes:
    print(f"Found {len(new_resumes)} new candidates to evaluate")

    for resume_file in new_resumes:
        scores = evaluate_candidate(resume_file, job_description)
        candidate_id = db.insert_candidate(job_id, ...)
        db.insert_evaluation(candidate_id, scores)

    # Export updated list
    db.export_to_excel(job_id, 'candidate_scores.xlsx')
else:
    print("No new candidates found")
```

### 3. Shortlisting Workflow

```python
# Show top candidates
top_candidates = db.get_candidates_by_score(job_id, min_score=85)

# User reviews and selects candidates for phone screen
selected_candidates = [1, 5, 8, 12]  # candidate IDs

# Move to phone screen stage
for candidate_id in selected_candidates:
    db.update_candidate_stage(candidate_id, 'phone_screen')
    db.add_to_shortlist(candidate_id, 'phone_screen',
                       'Score 85+, strong qualifications')

# Export phone screen list
db.export_shortlist_to_excel(job_id, 'phone_screen',
                            'phone_screen_candidates.xlsx')
```

### 4. Adding Interview Notes

```python
# After phone screen with candidate #5
db.add_note(
    candidate_id=5,
    note_type='phone_screen',
    author='Pernell Toney',
    content="""
    Great communication skills. Addressed concerns about job-hopping
    (family relocation x2). Strong technical knowledge of audit frameworks.
    Interested in mission-driven work. Available for in-person interview
    next week.
    """,
    tags=['communication', 'technical_strong', 'mission_fit']
)

# Update stage
db.update_candidate_stage(5, 'interview')
```

### 5. Generating Reports

```python
# Export all candidates with latest scores
db.export_to_excel(job_id, 'all_candidates.xlsx')

# Export shortlist for hiring committee
db.export_shortlist_to_excel(job_id, 'interview', 'interview_candidates.xlsx')

# Generate comparison report (top 3 finalists)
db.generate_comparison_report(job_id, candidate_ids=[5, 8, 12])
```

---

## Benefits Over JSON/Excel

| Feature | JSON + Excel | SQLite + Excel |
|---------|--------------|----------------|
| **Query candidates by score/stage** | Manual filtering | SQL queries |
| **Track evaluation history** | No | Yes (all evaluations stored) |
| **Add notes from interviews** | Manual Excel edits | Structured notes table |
| **Shortlisting workflow** | Manual columns | Dedicated shortlists table |
| **Audit trail** | No | Full history with timestamps |
| **Cross-job comparisons** | Separate files | Single database |
| **Incremental updates** | Merge logic | INSERT if not exists |
| **Generate multiple reports** | Manual | SQL + export functions |

---

## CLI Commands

With SQLite backend, you could support commands like:

```bash
# Initial evaluation
claude "Evaluate all resumes in this folder"

# Add new candidates
claude "Check for new resumes and evaluate them"

# Query candidates
claude "Show me all candidates with 85+ scores who haven't been interviewed yet"

# Shortlist
claude "Move candidates #1, #3, and #5 to phone screen stage"

# Add notes
claude "Add interview note for Jane Smith: [note content]"

# Generate reports
claude "Export top 10 candidates to Excel"
claude "Generate comparison report for finalists"
claude "Show me evaluation history for John Doe"

# Stage management
claude "Show all candidates in interview stage"
claude "Move Sarah Johnson to final round"
```

---

## File Structure

```
job-folder/
├── job_description.txt
├── resumes/
│   ├── candidate1.pdf
│   ├── candidate2.pdf
│   └── candidate3.pdf
├── recruiting.db              ← SQLite database (source of truth)
├── exports/
│   ├── candidate_scores.xlsx
│   ├── phone_screen_list.xlsx
│   └── final_round_comparison.xlsx
└── reports/
    ├── Screen_and_Rank_Report.md
    └── Final_Round_Analysis.md
```

---

## Migration Strategy

To migrate from JSON caching to SQLite:

1. **Parallel approach**: Support both systems initially
2. **Import existing data**: Convert `.evaluation_cache.json` to SQLite
3. **Gradual transition**: Use SQLite for new jobs
4. **Maintain Excel exports**: Keep familiar output format

---

## Implementation Notes

### Dependencies

```python
import sqlite3  # Built into Python - no installation needed
import json
import hashlib
from pathlib import Path
from datetime import datetime
```

### Database Class Example

```python
class RecruitingDatabase:
    def __init__(self, db_path='recruiting.db'):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self.create_tables()

    def create_tables(self):
        """Create all tables if they don't exist."""
        # Execute CREATE TABLE statements
        pass

    def insert_candidate(self, job_id, name, resume_filename, ...):
        """Insert new candidate."""
        pass

    def get_latest_evaluation(self, candidate_id):
        """Get most recent evaluation for candidate."""
        pass

    def export_to_excel(self, job_id, output_file):
        """Export all candidates to Excel."""
        # Use openpyxl or pandas
        pass
```

---

## Next Steps

1. **Create database schema** - Implement all tables
2. **Build database wrapper class** - CRUD operations
3. **Update skill to use SQLite** - Replace JSON caching
4. **Add CLI commands** - Support shortlisting, notes, queries
5. **Test with real data** - Migrate existing evaluations
6. **Document workflow** - Update user guides

---

## Conclusion

SQLite provides a **professional, scalable solution** for managing recruiting workflows over time. It enables:

- **Persistent tracking** across multiple rounds
- **Historical data** and audit trails
- **Flexible querying** for decision-making
- **Structured notes** and stage management
- **Easy reporting** with Excel exports

The overhead is minimal (SQLite ships with Python), and the benefits are substantial for your iterative, multi-stage recruiting process.
