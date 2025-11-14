#!/usr/bin/env python3
"""
Position Review Meeting Processor
Processes Oracle Cloud Recruiting requisitions for weekly position review meetings.
"""

import pandas as pd
import re
from datetime import datetime
from pathlib import Path
import sys


def parse_person_being_replaced(comment_text):
    """
    Parses the 'Person Being Replaced' from requisition comments.
    
    Looks for pattern:
        Person Being Replaced
        [Name]
    
    Args:
        comment_text: String containing requisition comments
        
    Returns:
        String with person's name, or empty string if not found
    """
    if pd.isna(comment_text) or not comment_text:
        return ""
    
    # Look for "Person Being Replaced" followed by a name on next line
    pattern = r'Person Being Replaced\s*\n\s*(.+?)(?:\n|$)'
    match = re.search(pattern, str(comment_text), re.IGNORECASE)
    
    if match:
        return match.group(1).strip()
    
    # Check if it's a simple "Back fill for [name]" or "Replacement for [name]"
    backfill_pattern = r'(?:Back\s*fill|Replacement)\s+for\s+(.+?)(?:\.|,|\n|$)'
    match = re.search(backfill_pattern, str(comment_text), re.IGNORECASE)
    
    if match:
        return match.group(1).strip()
    
    return ""


def determine_justification_type(business_justification):
    """
    Determines if position is Replacement or New Position.
    
    Args:
        business_justification: String from Business Justification field
        
    Returns:
        "Replacement" or "New Position"
    """
    if pd.isna(business_justification) or not business_justification:
        return "Unknown"
    
    bj = str(business_justification).lower()
    
    if 'replacement' in bj or 'replace' in bj or 'backfill' in bj or 'back fill' in bj:
        return "Replacement"
    elif 'new' in bj:
        return "New Position"
    else:
        return "Unknown"


def process_oracle_requisitions(input_file, output_date=None):
    """
    Main processing function.
    
    Args:
        input_file: Path to Oracle Cloud requisitions Excel file
        output_date: Optional date string for output filename (default: today)
        
    Returns:
        Path to output file
    """
    print(f"Reading Oracle Cloud requisitions from: {input_file}")
    
    # Read the source file
    df = pd.read_excel(input_file)
    
    print(f"Total requisitions in source: {len(df)}")
    
    # Filter 1: Keep only positions where Approved Date is blank (needs approval)
    df_filtered = df[df['Approved Date'].isna()].copy()
    print(f"Positions needing approval (blank Approved Date): {len(df_filtered)}")
    
    # Filter 2: Exclude cancelled requisitions (those with "_ORA_DELETED" in ReqID)
    cancelled_mask = df_filtered['Job Requisition Number'].astype(str).str.contains('_ORA_DELETED', case=False, na=False)
    cancelled_count = cancelled_mask.sum()
    
    if cancelled_count > 0:
        print(f"Excluding {cancelled_count} cancelled requisitions (containing '_ORA_DELETED')")
        df_filtered = df_filtered[~cancelled_mask].copy()
    
    print(f"Final positions for review (after excluding cancelled): {len(df_filtered)}")
    
    if len(df_filtered) == 0:
        print("⚠️  No positions found that need approval!")
        print("All requisitions have an Approved Date filled in.")
        return None
    
    # Parse Person Being Replaced from Requisition Comments
    df_filtered['Person Being Replaced'] = df_filtered['Requisition Comments'].apply(
        parse_person_being_replaced
    )
    
    # Determine Justification type (Replacement vs New Position)
    df_filtered['Justification Type'] = df_filtered['Business Justification'].apply(
        determine_justification_type
    )
    
    # Create output dataframe with proper column mapping
    output_df = pd.DataFrame({
        'ReqID': df_filtered['Job Requisition Number'],
        'Req. Title': df_filtered['Job Requisition Title'],
        'School/Org': df_filtered['Hiring Manager Department Name'],
        'Recruiter': '',  # Placeholder - will come from second CSV
        'Review Status': 'Ready for Review',  # Default for all
        'Person Being Replaced': df_filtered['Person Being Replaced'],
        'Hiring Manager': '',  # Placeholder - will come from second CSV
        'Anticipated Salary': df_filtered['Anticipated Salary'],
        'Justification': df_filtered['Justification Type'],
        'Campus': '',  # Placeholder - will come from second CSV
        'Grant Funded?': df_filtered['Grant Funded'].apply(lambda x: 'Yes' if x == 'Yes' else 'No'),
        'Justification and Impacts of Not Filling': df_filtered['Requisition Comments']
    })
    
    # Generate output filename
    if output_date:
        date_str = output_date
    else:
        date_str = datetime.now().strftime('%m-%d-%Y')
    
    output_filename = f"Position_Review_Meetings_{date_str}.xlsx"
    
    # Write to Excel
    output_df.to_excel(output_filename, index=False, sheet_name='Position Review Meetings')
    
    print(f"\n✓ Output file created: {output_filename}")
    print(f"  Total positions for review: {len(output_df)}")
    
    # Data quality report
    print("\n--- DATA QUALITY REPORT ---")
    
    no_person_replaced = output_df['Person Being Replaced'].isna() | (output_df['Person Being Replaced'] == '')
    print(f"Positions without 'Person Being Replaced': {no_person_replaced.sum()}")
    if no_person_replaced.sum() > 0:
        print("  (This is OK for new positions)")
    
    unknown_justification = output_df['Justification'] == 'Unknown'
    print(f"Positions with unclear justification type: {unknown_justification.sum()}")
    if unknown_justification.sum() > 0:
        print("  ReqIDs:", list(output_df[unknown_justification]['ReqID']))
    
    missing_salary = output_df['Anticipated Salary'].isna()
    print(f"Positions with missing salary: {missing_salary.sum()}")
    if missing_salary.sum() > 0:
        print("  ReqIDs:", list(output_df[missing_salary]['ReqID']))
    
    print("\n--- PLACEHOLDER FIELDS ---")
    print("The following fields are empty and will need to be filled:")
    print("  • Recruiter (awaiting second CSV)")
    print("  • Hiring Manager (awaiting second CSV)")
    print("  • Campus (awaiting second CSV)")
    
    return output_filename


def main():
    """Command line interface"""
    if len(sys.argv) < 2:
        print("Usage: python process_positions.py <oracle_requisitions_file.xlsx> [output_date]")
        print("Example: python process_positions.py orc-requisitions.xlsx")
        print("Example: python process_positions.py orc-requisitions.xlsx 10-30-2025")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_date = sys.argv[2] if len(sys.argv) > 2 else None
    
    if not Path(input_file).exists():
        print(f"Error: File not found: {input_file}")
        sys.exit(1)
    
    result = process_oracle_requisitions(input_file, output_date)
    
    if result:
        print(f"\n✓ Success! Review the output file: {result}")
    else:
        print("\n⚠️  No output generated - see messages above.")


if __name__ == "__main__":
    main()
