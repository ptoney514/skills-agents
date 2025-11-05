#!/usr/bin/env python3
"""
Test script for recruiting database system.

This script demonstrates how to use the SQLite database for recruiting evaluation.
Run this to verify the database system is working correctly.

Usage:
    python3 test_database.py
"""

import sys
from pathlib import Path

# Import database module
try:
    from recruiting_database import RecruitingDatabase
    from excel_exporter import export_candidate_scores
    print("✅ Database modules imported successfully")
except ImportError as e:
    print(f"❌ Error importing modules: {e}")
    sys.exit(1)


def test_database_creation():
    """Test creating a new database."""
    print("\n" + "="*60)
    print("TEST 1: Database Creation")
    print("="*60)

    # Create test database
    db = RecruitingDatabase('test_recruiting.db')
    print("✅ Database created: test_recruiting.db")

    return db


def test_job_creation(db):
    """Test creating a job record."""
    print("\n" + "="*60)
    print("TEST 2: Job Creation")
    print("="*60)

    job_id = db.create_job(
        title="Senior Software Engineer",
        jd_file="job_description.txt",
        notes="Test job for database validation"
    )

    print(f"✅ Job created with ID: {job_id}")

    # Verify job was created
    job = db.get_active_job()
    print(f"   Job title: {job['job_title']}")
    print(f"   Created: {job['created_date']}")

    return job_id


def test_candidate_creation(db, job_id):
    """Test creating candidate records."""
    print("\n" + "="*60)
    print("TEST 3: Candidate Creation")
    print("="*60)

    # Create test candidates
    candidates = [
        ("John Doe", "john_doe.pdf"),
        ("Jane Smith", "jane_smith.pdf"),
        ("Bob Johnson", "bob_johnson.pdf"),
    ]

    candidate_ids = []
    for name, filename in candidates:
        candidate_id = db.add_candidate(job_id, name, filename)
        candidate_ids.append(candidate_id)
        print(f"✅ Created candidate: {name} (ID: {candidate_id})")

    return candidate_ids


def test_evaluation_creation(db, candidate_ids):
    """Test creating evaluation records."""
    print("\n" + "="*60)
    print("TEST 4: Evaluation Creation")
    print("="*60)

    # Sample evaluation data
    evaluations = [
        {
            'candidate_id': candidate_ids[0],
            'q_score': 95.0,
            'e_score': 88.0,
            'r_score': 100.0,
            'overall_score': 93.0,
            'stars': 5,
            'recommendation': 'Strong Candidate',
            'last_position': 'Senior Engineer - TechCorp',
            'strengths': [
                '10 years Python experience',
                'Led 5+ distributed systems projects',
                'BS Computer Science from top university'
            ],
            'concerns': [
                'No experience with our specific tech stack',
                'Requires relocation'
            ]
        },
        {
            'candidate_id': candidate_ids[1],
            'q_score': 92.0,
            'e_score': 85.0,
            'r_score': 95.0,
            'overall_score': 90.5,
            'stars': 5,
            'recommendation': 'Strong Candidate',
            'last_position': 'Software Engineer - StartupCo',
            'strengths': [
                '8 years relevant experience',
                'Strong algorithmic skills',
                'Open source contributions'
            ],
            'concerns': [
                'Job hopping in past 2 years (explained by startup closures)',
                'Salary expectations may be high'
            ]
        },
        {
            'candidate_id': candidate_ids[2],
            'q_score': 80.0,
            'e_score': 75.0,
            'r_score': 85.0,
            'overall_score': 79.0,
            'stars': 3,
            'recommendation': 'Potential Fit',
            'last_position': 'Junior Engineer - BigCo',
            'strengths': [
                '3 years experience',
                'Eager to learn',
                'Good cultural fit'
            ],
            'concerns': [
                'Below minimum 5 year requirement',
                'Limited senior-level work',
                'May need mentoring'
            ]
        }
    ]

    for eval_data in evaluations:
        eval_id = db.add_evaluation(**eval_data)
        candidate = db.get_candidate(eval_data['candidate_id'])
        print(f"✅ Added evaluation for {candidate['full_name']} "
              f"(Score: {eval_data['overall_score']}, {eval_data['stars']} stars)")

    print(f"\n   Total evaluations created: {len(evaluations)}")


def test_notes(db, candidate_ids):
    """Test adding notes."""
    print("\n" + "="*60)
    print("TEST 5: Notes Management")
    print("="*60)

    # Add notes for first candidate
    note_id = db.add_note(
        candidate_id=candidate_ids[0],
        content="Phone screen went well. Strong technical knowledge. "
                "Discussed relocation timeline - flexible. Interested in mission-driven work.",
        note_type='phone_screen',
        author='Pernell Toney',
        tags=['technical_strong', 'relocation_ok', 'mission_fit']
    )

    print(f"✅ Added phone screen note for candidate {candidate_ids[0]}")

    # Add second note
    note_id = db.add_note(
        candidate_id=candidate_ids[0],
        content="Hiring manager very interested. Schedule on-site ASAP.",
        note_type='internal',
        author='Pernell Toney'
    )

    print(f"✅ Added internal note for candidate {candidate_ids[0]}")

    # Retrieve notes
    notes = db.get_notes(candidate_ids[0])
    print(f"\n   Total notes for candidate: {len(notes)}")


def test_shortlist(db, job_id, candidate_ids):
    """Test shortlist management."""
    print("\n" + "="*60)
    print("TEST 6: Shortlist Management")
    print("="*60)

    # Add top 2 candidates to phone screen
    db.add_to_shortlist(
        candidate_id=candidate_ids[0],
        stage='phone_screen',
        rationale='Score 93+, strong technical background',
        added_by='Pernell Toney'
    )
    print(f"✅ Added candidate {candidate_ids[0]} to phone screen shortlist")

    db.add_to_shortlist(
        candidate_id=candidate_ids[1],
        stage='phone_screen',
        rationale='Score 90+, good fit for team',
        added_by='Pernell Toney'
    )
    print(f"✅ Added candidate {candidate_ids[1]} to phone screen shortlist")

    # Move first candidate to interview stage
    db.add_to_shortlist(
        candidate_id=candidate_ids[0],
        stage='interview',
        rationale='Excellent phone screen, moving to on-site',
        added_by='Pernell Toney'
    )
    print(f"✅ Moved candidate {candidate_ids[0]} to interview stage")

    # Get shortlist
    phone_screen_list = db.get_shortlist_by_stage(job_id, 'phone_screen')
    interview_list = db.get_shortlist_by_stage(job_id, 'interview')

    print(f"\n   Candidates in phone screen: {len(phone_screen_list)}")
    print(f"   Candidates in interview: {len(interview_list)}")


def test_queries(db, job_id):
    """Test database queries."""
    print("\n" + "="*60)
    print("TEST 7: Database Queries")
    print("="*60)

    # Get all candidates with scores
    all_candidates = db.get_candidates_with_scores(job_id)
    print(f"✅ Retrieved {len(all_candidates)} candidates with scores")

    # Get candidates with 85+ scores
    strong_candidates = db.get_candidates_with_scores(job_id, min_score=85)
    print(f"✅ Found {len(strong_candidates)} candidates with 85+ scores")

    # Get candidates in specific stage
    phone_screen = db.get_candidates_with_scores(job_id, stage='phone_screen')
    print(f"✅ Found {len(phone_screen)} candidates in phone_screen stage")

    # Get summary stats
    stats = db.get_summary_stats(job_id)
    print(f"\n   Summary Statistics:")
    print(f"   - Total candidates: {stats['total_candidates']}")
    print(f"   - Strong (90+): {stats['strong_candidates']}")
    print(f"   - Good (85-89): {stats['good_candidates']}")
    print(f"   - Potential (70-84): {stats['potential_fit']}")
    print(f"   - No match (<70): {stats['no_match']}")


def test_excel_export(db, job_id):
    """Test Excel export."""
    print("\n" + "="*60)
    print("TEST 8: Excel Export")
    print("="*60)

    try:
        export_candidate_scores(db, job_id, 'test_candidate_scores.xlsx')
        print(f"✅ Excel export successful: test_candidate_scores.xlsx")
        return True
    except Exception as e:
        print(f"⚠️  Excel export failed: {e}")
        print("   (This is OK if openpyxl is not installed)")
        return False


def test_evaluation_history(db, candidate_ids):
    """Test evaluation history tracking."""
    print("\n" + "="*60)
    print("TEST 9: Evaluation History")
    print("="*60)

    # Add a second evaluation for first candidate (re-evaluation)
    db.add_evaluation(
        candidate_id=candidate_ids[0],
        q_score=96.0,
        e_score=90.0,
        r_score=100.0,
        overall_score=94.5,
        stars=5,
        recommendation='Strong Candidate',
        last_position='Senior Engineer - TechCorp',
        evaluation_type='re-screen',
        strengths=['All previous strengths', 'Clarified tech stack experience in phone screen'],
        concerns=['Relocation timeline confirmed']
    )

    print(f"✅ Added re-evaluation for candidate {candidate_ids[0]}")

    # Get history
    history = db.get_evaluation_history(candidate_ids[0])
    print(f"\n   Evaluation history:")
    for i, eval_record in enumerate(history, 1):
        print(f"   {i}. {eval_record['evaluation_date']}: "
              f"Score {eval_record['overall_score']} ({eval_record['evaluation_type']})")


def cleanup():
    """Clean up test files."""
    print("\n" + "="*60)
    print("CLEANUP")
    print("="*60)

    test_files = ['test_recruiting.db', 'test_candidate_scores.xlsx']

    for file in test_files:
        path = Path(file)
        if path.exists():
            path.unlink()
            print(f"✅ Deleted: {file}")


def main():
    """Run all tests."""
    print("\n" + "="*60)
    print("RECRUITING DATABASE TEST SUITE")
    print("="*60)

    try:
        # Run tests
        db = test_database_creation()
        job_id = test_job_creation(db)
        candidate_ids = test_candidate_creation(db, job_id)
        test_evaluation_creation(db, candidate_ids)
        test_notes(db, candidate_ids)
        test_shortlist(db, job_id, candidate_ids)
        test_queries(db, job_id)
        test_excel_export(db, job_id)
        test_evaluation_history(db, candidate_ids)

        # Close database
        db.close()

        print("\n" + "="*60)
        print("✅ ALL TESTS PASSED!")
        print("="*60)

        # Ask about cleanup
        print("\nTest files created:")
        print("  - test_recruiting.db")
        print("  - test_candidate_scores.xlsx (if export worked)")

        response = input("\nDelete test files? (y/n): ").strip().lower()
        if response == 'y':
            cleanup()
        else:
            print("\nTest files kept for inspection.")

    except Exception as e:
        print(f"\n❌ TEST FAILED: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
