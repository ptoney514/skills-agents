"""
SQLite Database Manager for Recruiting Evaluation Skill

This module provides a complete database wrapper for managing candidates,
evaluations, notes, and shortlists throughout the recruiting process.

Usage:
    from recruiting_database import RecruitingDatabase

    db = RecruitingDatabase('recruiting.db')
    job_id = db.create_job('Senior Software Engineer', 'job_description.txt')
    candidate_id = db.add_candidate(job_id, 'John Doe', 'john_doe.pdf')
    db.add_evaluation(candidate_id, q_score=95, e_score=88, r_score=100)
"""

import sqlite3
import json
import hashlib
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, List, Any, Tuple


class RecruitingDatabase:
    """Manages recruiting data in SQLite database."""

    def __init__(self, db_path: str = 'recruiting.db'):
        """
        Initialize database connection and create tables if needed.

        Args:
            db_path: Path to SQLite database file (default: recruiting.db in current directory)
        """
        self.db_path = Path(db_path)
        self.conn = sqlite3.connect(str(self.db_path))
        self.conn.row_factory = sqlite3.Row  # Access columns by name
        self.create_tables()

    def create_tables(self):
        """Create all required tables if they don't exist."""
        cursor = self.conn.cursor()

        # Jobs table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS jobs (
                job_id INTEGER PRIMARY KEY AUTOINCREMENT,
                job_title TEXT NOT NULL,
                job_description_file TEXT,
                job_description_hash TEXT,
                created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                status TEXT DEFAULT 'active',
                notes TEXT
            )
        ''')

        # Candidates table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS candidates (
                candidate_id INTEGER PRIMARY KEY AUTOINCREMENT,
                job_id INTEGER NOT NULL,
                full_name TEXT NOT NULL,
                resume_filename TEXT NOT NULL,
                resume_file_path TEXT,
                file_hash TEXT,
                first_seen_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                current_stage TEXT DEFAULT 'new',
                FOREIGN KEY (job_id) REFERENCES jobs(job_id),
                UNIQUE(job_id, resume_filename)
            )
        ''')

        # Evaluations table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS evaluations (
                evaluation_id INTEGER PRIMARY KEY AUTOINCREMENT,
                candidate_id INTEGER NOT NULL,
                evaluation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                evaluation_type TEXT DEFAULT 'initial',

                q_score REAL,
                e_score REAL,
                r_score REAL,
                overall_score REAL,

                stars INTEGER,
                recommendation TEXT,
                last_position TEXT,

                job_description_hash TEXT,

                FOREIGN KEY (candidate_id) REFERENCES candidates(candidate_id)
            )
        ''')

        # Evaluation details table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS evaluation_details (
                detail_id INTEGER PRIMARY KEY AUTOINCREMENT,
                evaluation_id INTEGER NOT NULL,
                strengths TEXT,
                concerns TEXT,
                score_breakdown TEXT,
                FOREIGN KEY (evaluation_id) REFERENCES evaluations(evaluation_id)
            )
        ''')

        # Notes table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS notes (
                note_id INTEGER PRIMARY KEY AUTOINCREMENT,
                candidate_id INTEGER NOT NULL,
                note_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                note_type TEXT,
                author TEXT,
                content TEXT NOT NULL,
                tags TEXT,
                FOREIGN KEY (candidate_id) REFERENCES candidates(candidate_id)
            )
        ''')

        # Shortlists table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS shortlists (
                shortlist_id INTEGER PRIMARY KEY AUTOINCREMENT,
                candidate_id INTEGER NOT NULL,
                stage TEXT NOT NULL,
                added_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                added_by TEXT,
                decision_rationale TEXT,
                FOREIGN KEY (candidate_id) REFERENCES candidates(candidate_id)
            )
        ''')

        # Create indexes for common queries
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_candidates_job ON candidates(job_id)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_evaluations_candidate ON evaluations(candidate_id)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_notes_candidate ON notes(candidate_id)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_shortlists_candidate ON shortlists(candidate_id)')

        self.conn.commit()

    def _hash_file(self, file_path: Path) -> str:
        """Generate SHA256 hash of file for change detection."""
        sha256 = hashlib.sha256()
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                sha256.update(chunk)
        return sha256.hexdigest()

    # ==================== JOB MANAGEMENT ====================

    def create_job(self, title: str, jd_file: Optional[str] = None, notes: Optional[str] = None) -> int:
        """
        Create a new job record.

        Args:
            title: Job title
            jd_file: Path to job description file
            notes: Optional notes about the job

        Returns:
            job_id of created job
        """
        cursor = self.conn.cursor()

        jd_hash = None
        if jd_file and Path(jd_file).exists():
            jd_hash = self._hash_file(Path(jd_file))

        cursor.execute('''
            INSERT INTO jobs (job_title, job_description_file, job_description_hash, notes)
            VALUES (?, ?, ?, ?)
        ''', (title, jd_file, jd_hash, notes))

        self.conn.commit()
        return cursor.lastrowid

    def get_active_job(self) -> Optional[Dict[str, Any]]:
        """Get the active job (most recent active job)."""
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT * FROM jobs
            WHERE status = 'active'
            ORDER BY created_date DESC
            LIMIT 1
        ''')
        row = cursor.fetchone()
        return dict(row) if row else None

    def get_or_create_job(self, title: str, jd_file: Optional[str] = None) -> int:
        """Get active job or create new one if it doesn't exist."""
        job = self.get_active_job()
        if job:
            return job['job_id']
        return self.create_job(title, jd_file)

    # ==================== CANDIDATE MANAGEMENT ====================

    def add_candidate(self, job_id: int, name: str, resume_filename: str,
                      resume_path: Optional[str] = None) -> int:
        """
        Add a new candidate or return existing candidate_id.

        Args:
            job_id: Job ID
            name: Candidate full name
            resume_filename: Resume file name
            resume_path: Full path to resume file

        Returns:
            candidate_id
        """
        cursor = self.conn.cursor()

        file_hash = None
        if resume_path and Path(resume_path).exists():
            file_hash = self._hash_file(Path(resume_path))

        try:
            cursor.execute('''
                INSERT INTO candidates (job_id, full_name, resume_filename, resume_file_path, file_hash)
                VALUES (?, ?, ?, ?, ?)
            ''', (job_id, name, resume_filename, resume_path, file_hash))
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError:
            # Candidate already exists, return existing ID
            cursor.execute('''
                SELECT candidate_id FROM candidates
                WHERE job_id = ? AND resume_filename = ?
            ''', (job_id, resume_filename))
            row = cursor.fetchone()
            return row['candidate_id'] if row else None

    def get_candidate(self, candidate_id: int) -> Optional[Dict[str, Any]]:
        """Get candidate by ID."""
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM candidates WHERE candidate_id = ?', (candidate_id,))
        row = cursor.fetchone()
        return dict(row) if row else None

    def get_candidate_by_filename(self, job_id: int, filename: str) -> Optional[Dict[str, Any]]:
        """Get candidate by resume filename."""
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT * FROM candidates
            WHERE job_id = ? AND resume_filename = ?
        ''', (job_id, filename))
        row = cursor.fetchone()
        return dict(row) if row else None

    def update_candidate_stage(self, candidate_id: int, stage: str):
        """Update candidate's current stage."""
        cursor = self.conn.cursor()
        cursor.execute('''
            UPDATE candidates
            SET current_stage = ?, last_updated = CURRENT_TIMESTAMP
            WHERE candidate_id = ?
        ''', (stage, candidate_id))
        self.conn.commit()

    def get_candidates_by_job(self, job_id: int) -> List[Dict[str, Any]]:
        """Get all candidates for a job."""
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM candidates WHERE job_id = ? ORDER BY last_updated DESC', (job_id,))
        return [dict(row) for row in cursor.fetchall()]

    def find_new_resumes(self, job_id: int, resume_folder: Path) -> List[Path]:
        """
        Find resume files not yet in database.

        Args:
            job_id: Job ID
            resume_folder: Path to folder containing resumes

        Returns:
            List of Path objects for new resume files
        """
        # Get existing resume filenames
        cursor = self.conn.cursor()
        cursor.execute('SELECT resume_filename FROM candidates WHERE job_id = ?', (job_id,))
        existing_files = {row['resume_filename'] for row in cursor.fetchall()}

        # Find all resume files
        all_resumes = list(resume_folder.glob('*.pdf')) + \
                      list(resume_folder.glob('*.docx')) + \
                      list(resume_folder.glob('*.doc'))

        # Return only new files
        return [r for r in all_resumes if r.name not in existing_files]

    # ==================== EVALUATION MANAGEMENT ====================

    def add_evaluation(self, candidate_id: int, q_score: float, e_score: float, r_score: float,
                       overall_score: float, stars: int, recommendation: str,
                       last_position: Optional[str] = None,
                       strengths: Optional[List[str]] = None,
                       concerns: Optional[List[str]] = None,
                       score_breakdown: Optional[Dict[str, Any]] = None,
                       evaluation_type: str = 'initial',
                       jd_hash: Optional[str] = None) -> int:
        """
        Add an evaluation for a candidate.

        Args:
            candidate_id: Candidate ID
            q_score: Qualifications score
            e_score: Experience score
            r_score: Risk flags score
            overall_score: Overall Evala score
            stars: Star rating (1-5)
            recommendation: Recommendation text
            last_position: Candidate's last position
            strengths: List of strengths
            concerns: List of concerns
            score_breakdown: Detailed score breakdown dictionary
            evaluation_type: Type of evaluation (initial, re-screen, post-interview)
            jd_hash: Hash of job description used

        Returns:
            evaluation_id
        """
        cursor = self.conn.cursor()

        # Insert evaluation
        cursor.execute('''
            INSERT INTO evaluations (
                candidate_id, evaluation_type, q_score, e_score, r_score,
                overall_score, stars, recommendation, last_position, job_description_hash
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (candidate_id, evaluation_type, q_score, e_score, r_score,
              overall_score, stars, recommendation, last_position, jd_hash))

        evaluation_id = cursor.lastrowid

        # Insert evaluation details
        cursor.execute('''
            INSERT INTO evaluation_details (evaluation_id, strengths, concerns, score_breakdown)
            VALUES (?, ?, ?, ?)
        ''', (evaluation_id,
              json.dumps(strengths) if strengths else None,
              json.dumps(concerns) if concerns else None,
              json.dumps(score_breakdown) if score_breakdown else None))

        # Update candidate last_updated
        cursor.execute('''
            UPDATE candidates SET last_updated = CURRENT_TIMESTAMP
            WHERE candidate_id = ?
        ''', (candidate_id,))

        self.conn.commit()
        return evaluation_id

    def get_latest_evaluation(self, candidate_id: int) -> Optional[Dict[str, Any]]:
        """Get most recent evaluation for a candidate."""
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT e.*, ed.strengths, ed.concerns, ed.score_breakdown
            FROM evaluations e
            LEFT JOIN evaluation_details ed ON e.evaluation_id = ed.evaluation_id
            WHERE e.candidate_id = ?
            ORDER BY e.evaluation_date DESC
            LIMIT 1
        ''', (candidate_id,))
        row = cursor.fetchone()
        if not row:
            return None

        result = dict(row)
        # Parse JSON fields
        if result.get('strengths'):
            result['strengths'] = json.loads(result['strengths'])
        if result.get('concerns'):
            result['concerns'] = json.loads(result['concerns'])
        if result.get('score_breakdown'):
            result['score_breakdown'] = json.loads(result['score_breakdown'])

        return result

    def get_evaluation_history(self, candidate_id: int) -> List[Dict[str, Any]]:
        """Get all evaluations for a candidate."""
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT e.*, ed.strengths, ed.concerns, ed.score_breakdown
            FROM evaluations e
            LEFT JOIN evaluation_details ed ON e.evaluation_id = ed.evaluation_id
            WHERE e.candidate_id = ?
            ORDER BY e.evaluation_date ASC
        ''', (candidate_id,))

        results = []
        for row in cursor.fetchall():
            result = dict(row)
            if result.get('strengths'):
                result['strengths'] = json.loads(result['strengths'])
            if result.get('concerns'):
                result['concerns'] = json.loads(result['concerns'])
            if result.get('score_breakdown'):
                result['score_breakdown'] = json.loads(result['score_breakdown'])
            results.append(result)

        return results

    # ==================== NOTES MANAGEMENT ====================

    def add_note(self, candidate_id: int, content: str, note_type: Optional[str] = None,
                 author: Optional[str] = None, tags: Optional[List[str]] = None) -> int:
        """
        Add a note for a candidate.

        Args:
            candidate_id: Candidate ID
            content: Note content
            note_type: Type of note (phone_screen, interview, reference_check, etc.)
            author: Note author
            tags: List of tags for filtering

        Returns:
            note_id
        """
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO notes (candidate_id, content, note_type, author, tags)
            VALUES (?, ?, ?, ?, ?)
        ''', (candidate_id, content, note_type, author,
              json.dumps(tags) if tags else None))

        self.conn.commit()
        return cursor.lastrowid

    def get_notes(self, candidate_id: int) -> List[Dict[str, Any]]:
        """Get all notes for a candidate."""
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT * FROM notes
            WHERE candidate_id = ?
            ORDER BY note_date DESC
        ''', (candidate_id,))

        results = []
        for row in cursor.fetchall():
            result = dict(row)
            if result.get('tags'):
                result['tags'] = json.loads(result['tags'])
            results.append(result)

        return results

    # ==================== SHORTLIST MANAGEMENT ====================

    def add_to_shortlist(self, candidate_id: int, stage: str,
                        rationale: Optional[str] = None, added_by: Optional[str] = None) -> int:
        """
        Add candidate to shortlist for a specific stage.

        Args:
            candidate_id: Candidate ID
            stage: Stage (phone_screen, interview, final_round, offer)
            rationale: Decision rationale
            added_by: Who added to shortlist

        Returns:
            shortlist_id
        """
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO shortlists (candidate_id, stage, decision_rationale, added_by)
            VALUES (?, ?, ?, ?)
        ''', (candidate_id, stage, rationale, added_by))

        # Also update candidate stage
        self.update_candidate_stage(candidate_id, stage)

        self.conn.commit()
        return cursor.lastrowid

    def get_shortlist_by_stage(self, job_id: int, stage: str) -> List[Dict[str, Any]]:
        """Get all candidates in a specific shortlist stage."""
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT c.*, s.added_date, s.decision_rationale, s.added_by
            FROM candidates c
            JOIN shortlists s ON c.candidate_id = s.candidate_id
            WHERE c.job_id = ? AND s.stage = ?
            ORDER BY s.added_date DESC
        ''', (job_id, stage))

        return [dict(row) for row in cursor.fetchall()]

    # ==================== QUERY FUNCTIONS ====================

    def get_candidates_with_scores(self, job_id: int, min_score: Optional[float] = None,
                                   stage: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Get candidates with their latest evaluation scores.

        Args:
            job_id: Job ID
            min_score: Minimum overall score filter
            stage: Current stage filter

        Returns:
            List of candidates with evaluation data
        """
        cursor = self.conn.cursor()

        query = '''
            SELECT
                c.candidate_id,
                c.full_name,
                c.resume_filename,
                c.current_stage,
                c.last_updated,
                e.overall_score,
                e.q_score,
                e.e_score,
                e.r_score,
                e.stars,
                e.recommendation,
                e.last_position,
                e.evaluation_date,
                ed.strengths,
                ed.concerns
            FROM candidates c
            LEFT JOIN (
                SELECT *,
                       ROW_NUMBER() OVER (PARTITION BY candidate_id ORDER BY evaluation_date DESC) as rn
                FROM evaluations
            ) e ON c.candidate_id = e.candidate_id AND e.rn = 1
            LEFT JOIN evaluation_details ed ON e.evaluation_id = ed.evaluation_id
            WHERE c.job_id = ?
        '''

        params = [job_id]

        if min_score is not None:
            query += ' AND e.overall_score >= ?'
            params.append(min_score)

        if stage is not None:
            query += ' AND c.current_stage = ?'
            params.append(stage)

        query += ' ORDER BY e.overall_score DESC'

        cursor.execute(query, params)

        results = []
        for row in cursor.fetchall():
            result = dict(row)
            if result.get('strengths'):
                result['strengths'] = json.loads(result['strengths'])
            if result.get('concerns'):
                result['concerns'] = json.loads(result['concerns'])
            results.append(result)

        return results

    def get_summary_stats(self, job_id: int) -> Dict[str, Any]:
        """Get summary statistics for a job."""
        cursor = self.conn.cursor()

        # Total candidates
        cursor.execute('SELECT COUNT(*) as total FROM candidates WHERE job_id = ?', (job_id,))
        total = cursor.fetchone()['total']

        # Score distribution
        cursor.execute('''
            SELECT
                SUM(CASE WHEN e.overall_score >= 90 THEN 1 ELSE 0 END) as strong,
                SUM(CASE WHEN e.overall_score >= 85 AND e.overall_score < 90 THEN 1 ELSE 0 END) as good,
                SUM(CASE WHEN e.overall_score >= 70 AND e.overall_score < 85 THEN 1 ELSE 0 END) as potential,
                SUM(CASE WHEN e.overall_score < 70 THEN 1 ELSE 0 END) as no_match
            FROM candidates c
            LEFT JOIN (
                SELECT candidate_id, overall_score,
                       ROW_NUMBER() OVER (PARTITION BY candidate_id ORDER BY evaluation_date DESC) as rn
                FROM evaluations
            ) e ON c.candidate_id = e.candidate_id AND e.rn = 1
            WHERE c.job_id = ?
        ''', (job_id,))

        dist = cursor.fetchone()

        # Stage distribution
        cursor.execute('''
            SELECT current_stage, COUNT(*) as count
            FROM candidates
            WHERE job_id = ?
            GROUP BY current_stage
        ''', (job_id,))

        stages = {row['current_stage']: row['count'] for row in cursor.fetchall()}

        return {
            'total_candidates': total,
            'strong_candidates': dist['strong'] or 0,
            'good_candidates': dist['good'] or 0,
            'potential_fit': dist['potential'] or 0,
            'no_match': dist['no_match'] or 0,
            'by_stage': stages
        }

    # ==================== EXPORT FUNCTIONS ====================

    def export_to_dict(self, job_id: int) -> Dict[str, Any]:
        """Export all job data to dictionary (for JSON export or Excel)."""
        job = self.get_active_job()
        candidates = self.get_candidates_with_scores(job_id)
        stats = self.get_summary_stats(job_id)

        return {
            'job': job,
            'candidates': candidates,
            'statistics': stats,
            'exported_date': datetime.now().isoformat()
        }

    def close(self):
        """Close database connection."""
        self.conn.close()

    def __enter__(self):
        """Context manager support."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager support."""
        self.close()


# Convenience function for quick access
def get_database(db_path: str = 'recruiting.db') -> RecruitingDatabase:
    """Get database instance."""
    return RecruitingDatabase(db_path)
