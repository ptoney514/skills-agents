# HR Project Manager Skill

Automate HR Operations sprint tracking through Excel spreadsheet manipulation and Linear issue synchronization.

## Overview

This skill maintains an Excel-based HR projects tracker as the single source of truth while providing enhanced project management capabilities through Linear integration. It handles:

- **Excel Manipulation:** Read, update, and maintain HR Projects tracker spreadsheet
- **Linear Sync:** Create and update Linear issues from Excel data
- **Sprint Management:** Generate sprint summaries, reports, and confirmation emails
- **Data Validation:** Ensure tracker integrity and identify dependencies
- **Task Breakdown:** Suggest weekly chunks for large projects

## Quick Start

### Prerequisites

1. **Excel Tracker:** HR Projects spreadsheet (see schema in SKILL.md)
2. **Linear Account:** Team ID and API key (optional, for sync features)
3. **Python Dependencies:** Install via `pip install -r requirements.txt`

### Environment Variables

```bash
export HR_TRACKER_PATH="/path/to/HR_Projects.xlsx"
export LINEAR_API_KEY="lin_api_xxxxxxxxxxxxxxxx"  # Optional
export LINEAR_TEAM_ID="team_xxxxxxxxxxxxxxxx"     # Optional
export HR_ARCHIVE_DIR="/path/to/archive/"          # Optional
```

### Installation

```bash
# From repository root
./scripts/sync-skills.sh
```

The skill will be symlinked to `~/.claude/skills/hr-project-manager/` and auto-loaded by Claude Code.

## Usage Examples

### Read Sprint Items

```bash
# Place your HR_Projects.xlsx in data/inputs/hr-tracker/
# Then ask Claude:
"Show me items for this sprint"
```

### Update After Sprint Meeting

```bash
"Update sprint status: HR-48 Complete 100%, HR-49 In Progress 80% with note 'Submitting today', HR-50 Complete 100%"
```

### Generate Sprint Email

```bash
"Generate sprint summary email for this Thursday"
```

### Sync to Linear

```bash
"Sync Excel tracker to Linear"
```

### Break Down Large Task

```bash
"Help me break down 'Complete Year-End Tax Process' due Jan 9"
```

## Workflow

### Weekly Sprint Cadence

**Wednesday EOB - Prep**
- Review sprint items for tomorrow's meeting
- Validate tracker data integrity

**Thursday - Sprint Meeting**
- Update status, % done, and notes for all sprint items
- Save dated copy of tracker
- Generate and send sprint confirmation email

**Thursday - Post-Meeting**
- Sync Excel tracker to Linear (if using Linear)
- Create any new issues identified in meeting

**Friday - Progress Check**
- Review items marked "In Progress"
- Identify blockers and dependencies

## Excel Tracker Schema

### Columns

| Column | Name | Description |
|--------|------|-------------|
| A | ID | Sequential number |
| B | Project/Task | Task description |
| C | Owner | Person responsible |
| D | Due Date | MM/DD/YYYY format |
| E | Days Until Due | Auto-calculated formula |
| F | Status | In Progress / Not Started / Complete |
| G | % Done | 0-100 |
| H | Category | Project category |
| I | Priority | Urgent / High / Medium / Low |
| J | Notes | Meeting updates, blockers |
| K | Linear ID | HR-XX format (optional) |
| L | HR Labels | Comma-separated tags (optional) |

### Sprint Selection

**Items for current sprint:** Due within 7 days (Days Until Due ≤ 7)

**Next sprint preview:** Due in 7-14 days

**Overdue:** Days Until Due < 0 (highlighted in red)

## Features

### Excel Operations
- ✅ Read tracker with proper column parsing
- ✅ Update cells while preserving formulas
- ✅ Batch status updates after sprint meetings
- ✅ Save dated copies for sprint history
- ✅ Maintain color coding and formatting

### Linear Integration
- ✅ Create Linear issues from Excel rows
- ✅ Sync Excel status → Linear status
- ✅ Update Linear progress from Excel % Done
- ✅ Add Excel notes as Linear comments
- ✅ Map Excel Priority → Linear priority

### Sprint Reporting
- ✅ Generate sprint summary with metrics
- ✅ Create formatted confirmation emails
- ✅ Identify blocked items
- ✅ Calculate completion rates
- ✅ Preview next sprint items

### Data Validation
- ✅ Validate column structure
- ✅ Check date formats and status values
- ✅ Identify duplicate IDs
- ✅ Verify formula integrity
- ✅ Parse dependencies from Notes

### Task Management
- ✅ Suggest weekly breakdowns for large tasks
- ✅ Estimate weeks until due date
- ✅ Generate phase deliverables
- ✅ Format as sprint-ready chunks

## Data Flow

```
Excel Tracker (Source of Truth)
       ↓
   Read/Parse
       ↓
Filter Sprint Items (Due ≤ 7 days)
       ↓
Sprint Meeting Updates
       ↓
Update Excel + Save Dated Copy
       ↓
Sync to Linear (Optional)
       ↓
Generate Sprint Email
```

## File Structure

```
skills/hr-project-manager/
├── SKILL.md              # Full specification and implementation details
├── README.md             # This file (user guide)
├── requirements.txt      # Python dependencies
├── hr_tracker.py         # Excel read/write functions
├── linear_sync.py        # Linear API integration
├── sprint_reports.py     # Report and email generation
├── validators.py         # Data validation
└── utils.py             # Helper functions

data/inputs/hr-tracker/   # Place Excel tracker here
data/outputs/hr-tracker/  # Dated copies and reports
```

## Configuration

### Config File (Optional)

Create `hr_project_config.json`:

```json
{
  "tracker": {
    "filepath": "/path/to/HR_Projects.xlsx",
    "archive_dir": "/path/to/archive/",
    "header_row": 2,
    "data_start_row": 3
  },
  "sprint": {
    "cadence": "weekly",
    "day": "Thursday",
    "time": "10:00 AM",
    "duration_minutes": 10,
    "items_per_sprint": 5
  },
  "linear": {
    "enabled": true,
    "team_id": "team_xxxxxxxxxxxxxxxx",
    "api_key": "lin_api_xxxxxxxxxxxxxxxx",
    "sync_direction": "excel_to_linear"
  },
  "team": {
    "facilitator": "Pernell",
    "director": "Tom",
    "team_members": ["Tom", "Judi", "Jen"]
  }
}
```

## Troubleshooting

### Excel file locked
**Issue:** Can't write to Excel
**Solution:** Close Excel before running skill operations

### Linear API rate limits
**Issue:** Sync fails with rate limit error
**Solution:** Reduce sync frequency or add backoff/retry logic

### Date parsing errors
**Issue:** Due dates not recognized
**Solution:** Ensure consistent MM/DD/YYYY format in Excel

### Missing dependencies
**Issue:** Import errors
**Solution:** Re-run `pip install -r requirements.txt`

## Best Practices

1. **Always save dated copies** before making bulk changes
2. **Validate data** before syncing to Linear
3. **Keep Excel as source of truth** - never manually edit Linear issues
4. **Use consistent date formats** (MM/DD/YYYY)
5. **Document blockers** in Notes column during sprint meetings
6. **Review dependencies** weekly to catch blocked items early

## Limitations

- Excel must be closed during skill operations (file lock)
- Linear sync is one-way (Excel → Linear)
- Formula preservation requires using openpyxl (not pandas write)
- Large trackers (>500 rows) may have performance impact

## Future Enhancements

**Phase 2:**
- Automated sprint email sending
- Slack integration for summaries
- Capacity planning and burndown charts

**Phase 3:**
- Meeting minutes parsing
- NLP blocker detection
- Dependency graph visualization
- Predictive analytics for completion dates

## Support

**Skill Owner:** Pernell
**Documentation:** See SKILL.md for full specification
**Issues:** Note bugs/enhancements in Sprint Evolution Tracker

## Version History

- **v1.0.0** (Nov 18, 2025) - Initial skill specification and structure

## Related Skills

- **recruiting-tracker** - Similar tracking pattern for recruiting pipelines
- **excel-design-guru** - Excel formatting and styling
- **data-analytics-engineer** - Advanced Excel reporting

---

**Questions or issues? See SKILL.md for detailed implementation guidance.**
