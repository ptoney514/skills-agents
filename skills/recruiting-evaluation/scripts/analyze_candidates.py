#!/usr/bin/env python3
"""
Candidate Batch Analyzer

This script processes candidate data from CSV or Excel files exported from
Oracle Recruiting or other ATS systems and prepares structured data for evaluation.
"""

import sys
import csv
import json
from pathlib import Path

def load_candidates_from_csv(file_path):
    """
    Load candidate data from a CSV file.
    
    Expected columns (flexible, will auto-detect):
    - Name/Candidate Name
    - Email
    - Phone
    - Current Title/Title
    - Company/Current Company
    - Years of Experience/Experience
    - Education
    - Skills
    - Location
    - Application Date
    - Resume/Summary
    """
    candidates = []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        # Auto-detect column names (case-insensitive, flexible)
        headers = reader.fieldnames
        
        for row in reader:
            candidate = {}
            
            # Extract data with flexible column matching
            for key, value in row.items():
                normalized_key = key.lower().strip()
                
                # Map common variations to standard fields
                if any(x in normalized_key for x in ['name', 'candidate']):
                    if 'first' in normalized_key:
                        candidate['first_name'] = value.strip()
                    elif 'last' in normalized_key:
                        candidate['last_name'] = value.strip()
                    else:
                        candidate['name'] = value.strip()
                
                elif 'email' in normalized_key:
                    candidate['email'] = value.strip()
                
                elif 'phone' in normalized_key:
                    candidate['phone'] = value.strip()
                
                elif 'title' in normalized_key and 'current' not in normalized_key:
                    candidate['current_title'] = value.strip()
                
                elif 'company' in normalized_key:
                    candidate['current_company'] = value.strip()
                
                elif 'experience' in normalized_key or 'years' in normalized_key:
                    candidate['years_experience'] = value.strip()
                
                elif 'education' in normalized_key or 'degree' in normalized_key:
                    candidate['education'] = value.strip()
                
                elif 'skill' in normalized_key:
                    candidate['skills'] = value.strip()
                
                elif 'location' in normalized_key:
                    candidate['location'] = value.strip()
                
                elif 'date' in normalized_key and 'application' in normalized_key:
                    candidate['application_date'] = value.strip()
                
                elif 'resume' in normalized_key or 'summary' in normalized_key:
                    candidate['resume_text'] = value.strip()
                
                elif 'salary' in normalized_key or 'compensation' in normalized_key:
                    candidate['salary_expectations'] = value.strip()
                
                else:
                    # Keep other fields as-is
                    candidate[key] = value.strip()
            
            candidates.append(candidate)
    
    return candidates

def print_candidate_summary(candidates):
    """Print a summary of loaded candidates."""
    print(f"\n{'='*60}")
    print(f"LOADED {len(candidates)} CANDIDATES")
    print(f"{'='*60}\n")
    
    for i, candidate in enumerate(candidates, 1):
        name = candidate.get('name', 
                            f"{candidate.get('first_name', '')} {candidate.get('last_name', '')}").strip()
        title = candidate.get('current_title', 'N/A')
        company = candidate.get('current_company', 'N/A')
        
        print(f"{i}. {name}")
        print(f"   Title: {title}")
        print(f"   Company: {company}")
        print(f"   Email: {candidate.get('email', 'N/A')}")
        print()

def export_for_analysis(candidates, output_file='candidates_for_analysis.json'):
    """Export candidates in JSON format for easy analysis."""
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(candidates, f, indent=2)
    
    print(f"\n✓ Exported {len(candidates)} candidates to {output_file}")
    return output_file

def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python analyze_candidates.py <csv_file> [output_json]")
        print("\nExample: python analyze_candidates.py candidates.csv")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else 'candidates_for_analysis.json'
    
    if not Path(input_file).exists():
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    
    print(f"Loading candidates from: {input_file}")
    
    try:
        candidates = load_candidates_from_csv(input_file)
        print_candidate_summary(candidates)
        export_for_analysis(candidates, output_file)
        
        print("\n" + "="*60)
        print("NEXT STEPS:")
        print("="*60)
        print(f"1. Review the loaded candidates above")
        print(f"2. Provide job requirements for the role")
        print(f"3. Run evaluation against requirements")
        print()
        
    except Exception as e:
        print(f"Error processing file: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
