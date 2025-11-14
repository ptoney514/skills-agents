# Position Review Meeting Processor - User Guide

## Overview

This custom Claude agent skill automates the tedious parts of preparing your weekly position review meeting documents. It processes Oracle Cloud Recruiting exports and formats them into your standard meeting document.

## What Gets Automated

✅ **Filtering** - Automatically selects only positions needing approval (blank Approved Date) AND excludes cancelled requisitions (those with "_ORA_DELETED" in ReqID)  
✅ **Column Mapping** - Converts Oracle Cloud format to your meeting format  
✅ **Person Parsing** - Extracts "Person Being Replaced" from requisition comments  
✅ **Status Defaults** - Sets all positions to "Ready for Review"  
✅ **Excel Generation** - Creates properly formatted output file  

## What Still Needs Your Attention

⚠️ **Placeholder Fields** - Recruiter, Hiring Manager, Campus (awaiting second CSV integration)  
⚠️ **Quality Review** - Check flagged items with missing/unclear data  
⚠️ **Meeting Updates** - During the meeting, update Review Status column  

## Quick Start

### Using in Claude.ai

1. **Upload this skill:**
   - Zip the `position-review-skill` folder
   - Go to claude.ai Settings → Features → Skills
   - Upload the zip file

2. **Use it:**
   - Upload your Oracle Cloud requisitions file to a conversation
   - Say: "Process this file for the position review meeting"
   - Claude automatically uses this skill

3. **Download result:**
   - Claude generates the Excel file
   - Download and review before meeting

### Using via API

See the main documentation at: https://docs.claude.com/en/api/skills-guide

## Understanding the Output

### Output Filename
`Position_Review_Meetings_MM-DD-YYYY.xlsx`

### Column Descriptions

| Column | Source | Notes |
|--------|--------|-------|
| ReqID | Job Requisition Number | Direct mapping |
| Req. Title | Job Requisition Title | Direct mapping |
| School/Org | Hiring Manager Department Name | Direct mapping |
| Recruiter | (Placeholder) | **Fill manually or await second CSV** |
| Review Status | Default: "Ready for Review" | **Update during meeting** |
| Person Being Replaced | Parsed from comments | Blank for new positions |
| Hiring Manager | (Placeholder) | **Fill manually or await second CSV** |
| Anticipated Salary | Anticipated Salary | Direct mapping |
| Justification | Business Justification | "Replacement" or "New Position" |
| Campus | (Placeholder) | **Fill manually or await second CSV** |
| Grant Funded? | Grant Funded | "Yes" or "No" |
| Justification and Impacts | Requisition Comments | Full text |

### Data Quality Flags

The skill reports:
- Positions without "Person Being Replaced" identified
- Positions with unclear justification types
- Positions missing salary information

Review these before the meeting to gather additional context.

## How "Person Being Replaced" Parsing Works

The script looks for these patterns in Requisition Comments:

**Pattern 1:**
```
Person Being Replaced
John Smith
```

**Pattern 2:**
```
Back fill for Jane Doe
```

**Pattern 3:**
```
Replacement for Bob Johnson
```

If none found → Left blank (normal for new positions)

## Troubleshooting

### "No positions found that need approval"
- All requisitions in your file have Approved Dates filled in
- Check if you're using the right export file
- Verify filter criteria matches your workflow

### Parser doesn't find person's name
- Check if the comment uses a different format
- You can manually fill in the cell
- Let me know the pattern and we can update the parser

### Missing fields
- Recruiter, Hiring Manager, Campus are intentionally blank
- These will be filled when second CSV integration is added
- You can manually fill them for now if needed

## Next Enhancements

When you provide the second CSV with recruiter/hiring manager/campus data:
1. We'll add automatic merging logic
2. All placeholder fields will populate automatically
3. You'll have a fully automated workflow

## Example Workflow

**Monday morning before the meeting:**
1. Export requisitions from Oracle Cloud
2. Upload to Claude: "Process for this week's position review meeting"
3. Download generated Excel file
4. Quick review of flagged items
5. Ready for meeting! ✓

**During the meeting:**
- Update "Review Status" column as decisions are made
- Save and distribute to attendees

## Questions or Issues?

This skill is designed to evolve with your workflow. As you use it:
- Note any patterns it misses
- Identify fields that could be auto-populated
- Share feedback to improve the automation

We can continuously refine the skill to save you more time!
