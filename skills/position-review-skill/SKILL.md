---
name: Position Review Meeting Processor
description: Processes Oracle Cloud Recruiting requisitions and formats them for weekly position review meetings. Filters positions needing approval and creates structured Excel reports.
---

# Position Review Meeting Processor

This skill automates the preparation of position review meeting documents from Oracle Cloud Recruiting data exports.

## When to Use This Skill

Use this skill when you need to:
- Process Oracle Cloud Recruiting requisition exports for weekly position review meetings
- Filter positions that need approval review
- Format requisition data into the standard meeting document format
- Parse and extract key information from requisition comments

## What This Skill Does

### Automated Processing
1. **Reads Oracle Cloud requisitions file** (Excel format)
2. **Filters positions** - Selects only requisitions where:
   - "Approved Date" is blank (positions needing review)
   - ReqID does NOT contain "_ORA_DELETED" (excludes cancelled requisitions)
3. **Maps columns** from Oracle Cloud format to Position Review Meeting format
4. **Parses "Person Being Replaced"** from the Requisition Comments field
5. **Sets default values** - "Ready for Review" status for all positions
6. **Creates formatted Excel output** with proper column structure

### Column Mapping

**From Oracle Cloud → To Meeting Document:**
- Job Requisition Number → ReqID
- Job Requisition Title → Req. Title
- Hiring Manager Department Name → School/Org
- (Placeholder) → Recruiter
- Business Justification → Justification (Replacement/New Position type)
- (Default: "Ready for Review") → Review Status
- (Parsed from comments) → Person Being Replaced
- (Placeholder) → Hiring Manager
- Anticipated Salary → Anticipated Salary
- (Placeholder) → Campus
- Grant Funded → Grant Funded?
- Requisition Comments → Justification and Impacts of Not Filling

### Person Being Replaced Parsing

The skill looks for this pattern in Requisition Comments:
```
Person Being Replaced
[Name]
```

If found, extracts the name. If not found or if it's a new position, leaves blank or marks as "New Position - N/A".

### Data Quality Flags

The skill identifies and reports:
- Positions with missing critical information
- Ambiguous justification types
- Empty or unusual requisition comments
- Any parsing issues

## Output Format

Creates an Excel file named: `Position_Review_Meetings_[DATE].xlsx`

**Columns (in order):**
1. ReqID
2. Req. Title
3. School/Org
4. Recruiter (placeholder for now)
5. Review Status (default: "Ready for Review")
6. Person Being Replaced
7. Hiring Manager (placeholder for now)
8. Anticipated Salary
9. Justification (Replacement/New Position)
10. Campus (placeholder for now)
11. Grant Funded?
12. Justification and Impacts of Not Filling

## Usage Examples

### Basic Usage
```
"Process the Oracle Cloud requisitions file for this week's position review meeting"
```

### With Custom Date
```
"Create the position review meeting document for October 30, 2025"
```

### With Source File Specified
```
"Use the orc-requisitions file to generate the position review meeting doc"
```

## How to Use

1. **Provide the Oracle Cloud requisitions export file** (Excel format)
2. The skill automatically:
   - Filters to positions needing approval (blank Approved Date)
   - Maps and formats the data
   - Parses person being replaced
   - Creates the output Excel file
3. **Review the output** - Check flagged items and verify data
4. **Optional:** Manually fill in placeholder fields (Recruiter, Hiring Manager, Campus) if needed

## Future Enhancements

The skill is designed to incorporate:
- **Second CSV merge** for Recruiter, Hiring Manager, and Campus data
- **Automated recruiter assignment** based on department mappings
- **Campus inference** from department names
- **Additional validation rules** as needed

## Files in This Skill

- `SKILL.md` - This instruction file
- `process_positions.py` - Main processing script
- `README.md` - User guide and setup instructions

## Technical Notes

- Uses pandas for data processing
- Uses openpyxl for Excel file handling
- Handles missing data gracefully
- Preserves all data from source for audit trail
