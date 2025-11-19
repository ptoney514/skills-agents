---
name: hr-project-manager
description: Automate HR Operations sprint tracking through Excel spreadsheet manipulation and Linear issue synchronization. Maintains Excel as single source of truth while providing enhanced project management through Linear integration. Generates sprint reports, validates data, and manages weekly sprint workflows.
---

# HR Project Manager Skill
**Excel Manipulation & Linear Sync Automation**

---

## 🎯 Skill Overview

**Skill Name:** `hr-project-manager`

**Purpose:** Automate HR Operations sprint tracking through Excel spreadsheet manipulation and Linear issue synchronization. Maintains Excel as the single source of truth while providing enhanced project management through Linear integration.

**Core Capabilities:**
1. Read and parse HR Projects Excel tracker
2. Update Excel cells, formulas, and formatting programmatically
3. Create/update Linear issues in bulk from Excel data
4. Sync status between Excel and Linear
5. Generate sprint reports and communications
6. Validate data integrity and dependencies

---

## 📋 Skill Specification

### **Installation Command**
```bash
claude code skill add hr-project-manager
```

### **Skill Metadata**

**Name:** HR Project Manager  
**Version:** 1.0.0  
**Category:** Project Management  
**Language:** Python 3.11+  
**Dependencies:**
- `openpyxl>=3.1.2` (Excel manipulation)
- `pandas>=2.1.0` (data processing)
- `python-dateutil>=2.8.2` (date handling)
- `requests>=2.31.0` (Linear API calls)

---

## 🛠️ Required Python Libraries

```python
# requirements.txt for skill
openpyxl>=3.1.2
pandas>=2.1.0
python-dateutil>=2.8.2
requests>=2.31.0
```

---

## 📊 Excel Tracker Schema

The skill must understand this Excel structure:

### **Column Definitions**
```python
EXCEL_SCHEMA = {
    'A': 'ID',                    # Sequential number
    'B': 'Project/Task',          # Task description
    'C': 'Owner',                 # Person responsible
    'D': 'Due Date',              # MM/DD/YYYY format
    'E': 'Days Until Due',        # Auto-calculated formula
    'F': 'Status',                # In Progress/Not Started/Complete
    'G': '% Done',                # 0-100
    'H': 'Category',              # Project category
    'I': 'Priority',              # Urgent/High/Medium/Low
    'J': 'Notes',                 # Meeting updates, blockers
    'K': 'Linear ID',             # HR-XX format
    'L': 'HR Labels',             # Comma-separated tags
}

# Excel file configuration
HEADER_ROW = 2  # Row 3 in Excel (0-indexed as 2)
DATA_START_ROW = 3  # Row 4 in Excel (0-indexed as 3)
```

### **Color Coding Rules**
```python
# Priority colors (Column I)
PRIORITY_COLORS = {
    'Urgent': 'FF0000',    # Red background
    'High': 'FFA500',      # Orange background
    'Medium': 'FFFF00',    # Yellow background
    'Low': '00FF00',       # Green background
}

# Days Until Due colors (Column E)
def get_days_color(days):
    if days < 0:
        return {'bg': 'FF0000', 'font': 'FF0000', 'bold': True}  # Overdue
    elif days <= 7:
        return {'bg': None, 'font': '00FF00', 'bold': True}      # This sprint
    else:
        return {'bg': None, 'font': '000000', 'bold': False}     # Future
```

---

## 🔧 Core Functions Required

### **1. Excel Reading & Parsing**

```python
def read_hr_tracker(filepath: str) -> pd.DataFrame:
    """
    Read Excel tracker and return structured DataFrame.
    
    Args:
        filepath: Path to Excel file
        
    Returns:
        DataFrame with parsed tracker data
        
    Important:
        - Use header=2 to correctly identify columns
        - Parse dates as datetime objects
        - Handle None/NaN values in Notes column
        - Preserve formatting information
    """
    pass

def get_sprint_items(df: pd.DataFrame, days_threshold: int = 7) -> pd.DataFrame:
    """
    Filter items for current sprint (due within days_threshold).
    
    Args:
        df: Full tracker DataFrame
        days_threshold: Days until due (default 7 for weekly sprint)
        
    Returns:
        Filtered DataFrame with sprint focus items
    """
    pass
```

### **2. Excel Writing & Updating**

```python
def update_excel_cell(filepath: str, row: int, column: str, value: any) -> bool:
    """
    Update a single cell in Excel tracker.
    
    Args:
        filepath: Path to Excel file
        row: Row number (1-indexed)
        column: Column letter (A-L)
        value: New value to write
        
    Returns:
        Success boolean
        
    Important:
        - Preserve existing formulas in other cells
        - Maintain conditional formatting
        - Use openpyxl to preserve Excel features
    """
    pass

def update_sprint_status(filepath: str, updates: List[Dict]) -> bool:
    """
    Batch update multiple status fields after sprint meeting.
    
    Args:
        filepath: Path to Excel file
        updates: List of dicts with keys: id, status, percent_done, notes
        
    Returns:
        Success boolean
        
    Example:
        updates = [
            {'id': 48, 'status': 'Complete', 'percent_done': 100, 'notes': 'All three issues resolved'},
            {'id': 49, 'status': 'In Progress', 'percent_done': 80, 'notes': 'Submitting today'}
        ]
    """
    pass

def save_tracker_with_date(filepath: str, output_dir: str) -> str:
    """
    Save dated copy of tracker for sprint history.
    
    Args:
        filepath: Source Excel file
        output_dir: Directory for dated copies
        
    Returns:
        Path to saved file (HR_Projects_MM_DD_YYYY.xlsx)
    """
    pass
```

### **3. Linear Integration**

```python
def create_linear_issues(df: pd.DataFrame, team_id: str, api_key: str) -> List[Dict]:
    """
    Create Linear issues from Excel tracker rows.
    
    Args:
        df: DataFrame with tracker data
        team_id: Linear team ID
        api_key: Linear API key
        
    Returns:
        List of created issues with Linear IDs
        
    Important:
        - Use HR-XX format for Linear IDs
        - Map Priority to Linear priority (0-4 scale)
        - Parse HR Labels into Linear labels
        - Set due dates from Excel
        - Assign to owner if email matches Linear user
    """
    pass

def sync_excel_to_linear(filepath: str, team_id: str, api_key: str) -> Dict:
    """
    Sync Excel tracker status to Linear issues.
    
    Args:
        filepath: Path to Excel file
        team_id: Linear team ID
        api_key: Linear API key
        
    Returns:
        Dict with sync results: {'updated': N, 'errors': [...]}
        
    Logic:
        - Read Excel tracker
        - For each row with Linear ID:
            - Check if Linear issue exists
            - Update Linear status from Excel Status column
            - Update Linear progress from Excel % Done
            - Add Excel Notes as Linear comment (if new)
        - Excel is authoritative source
    """
    pass

def get_linear_updates(team_id: str, api_key: str, since: str) -> List[Dict]:
    """
    Check for Linear updates to sync back to Excel.
    
    Args:
        team_id: Linear team ID
        api_key: Linear API key
        since: ISO datetime string for filtering
        
    Returns:
        List of Linear issues updated since timestamp
        
    Note: Use sparingly - Excel is source of truth
    """
    pass
```

### **4. Sprint Report Generation**

```python
def generate_sprint_summary(filepath: str, sprint_date: str) -> Dict:
    """
    Generate sprint summary data for communications.
    
    Args:
        filepath: Path to Excel file
        sprint_date: Date string (YYYY-MM-DD) for sprint start
        
    Returns:
        Dict with sprint data:
        {
            'sprint_items': List[Dict],  # Items for this sprint
            'completed': List[Dict],      # Completed items
            'in_progress': List[Dict],    # In progress items
            'blocked': List[Dict],        # Items with blockers in Notes
            'next_sprint_preview': List[Dict],  # Items due in 7-14 days
            'overdue': List[Dict],        # Overdue items
            'metrics': {
                'completion_rate': float,
                'total_items': int,
                'avg_days_until_due': float
            }
        }
    """
    pass

def create_sprint_email(summary: Dict, facilitator: str = "Pernell") -> str:
    """
    Generate formatted sprint confirmation email.
    
    Args:
        summary: Output from generate_sprint_summary()
        facilitator: Name of sprint facilitator
        
    Returns:
        Formatted email text ready to send
        
    Template:
        Subject: Sprint Focus [Date] - [Date]
        
        Team - This sprint's focus (Thu [date] - Thu [date]):
        
        1. [Item] - [Owner] - Due [date]
        2. [Item] - [Owner] - Due [date]
        ...
        
        Blockers I'm working on:
        - [Blocker 1]
        - [Blocker 2]
        
        New urgent requests? Send to me for triage.
        
        Next sprint meeting: Thursday [date] at [time]
    """
    pass
```

### **5. Data Validation**

```python
def validate_tracker_data(filepath: str) -> Dict:
    """
    Validate Excel tracker data integrity.
    
    Args:
        filepath: Path to Excel file
        
    Returns:
        Dict with validation results:
        {
            'valid': bool,
            'errors': List[str],
            'warnings': List[str]
        }
        
    Checks:
        - All required columns present
        - Due dates are valid dates
        - Status values are valid (In Progress/Not Started/Complete)
        - Priority values are valid (Urgent/High/Medium/Low)
        - Linear IDs follow HR-XX format if present
        - No duplicate IDs
        - Owner names are not empty
        - Days Until Due formula is correct
    """
    pass

def check_dependencies(filepath: str) -> List[Dict]:
    """
    Parse Notes column for dependency indicators.
    
    Args:
        filepath: Path to Excel file
        
    Returns:
        List of identified dependencies:
        [
            {
                'item_id': 51,
                'depends_on': 48,
                'note': 'Dependent on HR-48 completion'
            }
        ]
        
    Pattern matching:
        - Look for "depends on", "blocked by", "waiting on" in Notes
        - Extract HR-XX or item numbers
    """
    pass
```

### **6. Task Breakdown Assistance**

```python
def suggest_task_breakdown(task_description: str, due_date: str) -> Dict:
    """
    Analyze a large task and suggest weekly chunks.
    
    Args:
        task_description: Full task description
        due_date: Final due date (YYYY-MM-DD)
        
    Returns:
        Dict with breakdown suggestions:
        {
            'original_task': str,
            'estimated_weeks': int,
            'suggested_chunks': List[Dict[str, str]],  # week, deliverable
            'breakdown_rationale': str
        }
        
    Logic:
        - Calculate weeks until due date
        - Suggest 3-5 phases
        - Generate weekly deliverables
        - Format as: "[Project] - Week X: [Deliverable]"
    """
    pass
```

---

## 🎮 Usage Examples

### **Example 1: Read Sprint Items**
```bash
# From command line
claude code "Show me items for this sprint"

# Skill executes:
df = read_hr_tracker('/path/to/HR_Projects.xlsx')
sprint_items = get_sprint_items(df, days_threshold=7)
print(sprint_items[['ID', 'Project/Task', 'Owner', 'Due Date', 'Status']])
```

### **Example 2: Update After Sprint Meeting**
```bash
claude code "Update sprint status: HR-48 Complete 100%, HR-49 In Progress 80% with note 'Submitting today', HR-50 Complete 100%"

# Skill executes:
updates = [
    {'id': 48, 'status': 'Complete', 'percent_done': 100},
    {'id': 49, 'status': 'In Progress', 'percent_done': 80, 'notes': 'Submitting today'},
    {'id': 50, 'status': 'Complete', 'percent_done': 100}
]
update_sprint_status('/path/to/HR_Projects.xlsx', updates)
save_tracker_with_date('/path/to/HR_Projects.xlsx', '/path/to/archive/')
```

### **Example 3: Sync to Linear**
```bash
claude code "Sync Excel tracker to Linear"

# Skill executes:
result = sync_excel_to_linear(
    filepath='/path/to/HR_Projects.xlsx',
    team_id='TEAM_ID',
    api_key='LINEAR_API_KEY'
)
print(f"Updated {result['updated']} issues")
```

### **Example 4: Generate Sprint Email**
```bash
claude code "Generate sprint summary email for this Thursday"

# Skill executes:
summary = generate_sprint_summary('/path/to/HR_Projects.xlsx', '2025-11-14')
email = create_sprint_email(summary)
print(email)
```

### **Example 5: Break Down Large Task**
```bash
claude code "Help me break down 'Complete Year-End Tax Process' due Jan 9"

# Skill executes:
breakdown = suggest_task_breakdown(
    'Complete Year-End Tax Process',
    '2026-01-09'
)
for chunk in breakdown['suggested_chunks']:
    print(f"Week {chunk['week']}: {chunk['deliverable']}")
```

---

## ⚙️ Configuration

### **Environment Variables**
```bash
# Required
export HR_TRACKER_PATH="/path/to/HR_Projects.xlsx"
export LINEAR_API_KEY="lin_api_xxxxxxxxxxxxxxxx"
export LINEAR_TEAM_ID="team_xxxxxxxxxxxxxxxx"

# Optional
export HR_ARCHIVE_DIR="/path/to/archive/"
export SPRINT_DAY="Thursday"  # Day of week for sprints
export SPRINT_TIME="10:00 AM"  # Meeting time
```

### **Config File (optional): hr_project_config.json**
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

---

## 🔐 Security Considerations

1. **API Keys**: Store Linear API key in environment variable, not code
2. **File Permissions**: Excel tracker should be read/write for skill
3. **Backup Strategy**: Always save dated copies before modifications
4. **Error Handling**: Gracefully handle missing files, API failures
5. **Data Validation**: Validate all inputs before writing to Excel

---

## 🐛 Error Handling

```python
class HRTrackerError(Exception):
    """Base exception for HR tracker operations"""
    pass

class ExcelReadError(HRTrackerError):
    """Failed to read Excel file"""
    pass

class LinearSyncError(HRTrackerError):
    """Failed to sync with Linear"""
    pass

class ValidationError(HRTrackerError):
    """Data validation failed"""
    pass

# All functions should raise appropriate exceptions
# Claude Code will catch and display errors to user
```

---

## 📚 Advanced Features (Future)

### **Phase 2 Enhancements**
1. **Automated Sprint Emails**: Send emails directly from skill
2. **Slack Integration**: Post sprint summaries to Slack channel
3. **Capacity Planning**: Track team member hours/capacity
4. **Burndown Charts**: Generate sprint progress visualizations
5. **Historical Analytics**: Analyze trends over multiple sprints
6. **Smart Scheduling**: Suggest optimal sprint items based on capacity

### **Phase 3 Enhancements**
1. **Meeting Minutes Parsing**: Extract updates from meeting notes
2. **Blocker Detection**: NLP to identify blockers in Notes column
3. **Dependency Graphs**: Visualize task dependencies
4. **Predictive Analytics**: Forecast completion dates
5. **Auto-breakdown**: AI-powered large task decomposition

---

## 🧪 Testing Requirements

### **Unit Tests**
```python
def test_read_hr_tracker():
    """Test reading Excel with correct header row"""
    df = read_hr_tracker('test_data/sample_tracker.xlsx')
    assert len(df.columns) == 12
    assert 'Project/Task' in df.columns

def test_get_sprint_items():
    """Test filtering items by days threshold"""
    df = load_test_data()
    sprint = get_sprint_items(df, days_threshold=7)
    assert all(sprint['Days Until Due'] <= 7)

def test_update_excel_cell():
    """Test updating cell preserves formulas"""
    # Create test file with formula
    # Update adjacent cell
    # Verify formula still works
    pass

def test_linear_sync():
    """Test Linear API integration (mocked)"""
    # Mock Linear API responses
    # Test create_linear_issues()
    # Verify correct data mapping
    pass
```

### **Integration Tests**
1. End-to-end: Read → Update → Save → Verify
2. Linear sync: Excel → Linear → Status update
3. Sprint workflow: Generate summary → Create email → Validate output

---

## 📖 Documentation

Each function must include:
- **Docstring**: Clear description with Args/Returns
- **Type hints**: For all parameters and returns
- **Examples**: Usage example in docstring
- **Edge cases**: How function handles errors

Example:
```python
def read_hr_tracker(filepath: str, header_row: int = 2) -> pd.DataFrame:
    """
    Read HR Projects tracker Excel file into structured DataFrame.
    
    Args:
        filepath: Path to Excel file (e.g., '/path/to/HR_Projects.xlsx')
        header_row: Row number for column headers (default: 2 for row 3)
        
    Returns:
        DataFrame with columns: ID, Project/Task, Owner, Due Date, etc.
        
    Raises:
        ExcelReadError: If file not found or cannot be parsed
        ValidationError: If required columns missing
        
    Example:
        >>> df = read_hr_tracker('/path/to/HR_Projects.xlsx')
        >>> print(df.columns)
        Index(['ID', 'Project/Task', 'Owner', ...])
        
    Note:
        - Due Date is parsed as datetime object
        - Days Until Due is calculated integer
        - Empty Notes cells are converted to empty string
    """
    try:
        df = pd.read_excel(filepath, header=header_row)
        # ... implementation
        return df
    except FileNotFoundError:
        raise ExcelReadError(f"Tracker file not found: {filepath}")
```

---

## 🚀 Skill Installation Steps

### **Step 1: Create Skill Directory**
```bash
mkdir -p ~/.claude/skills/hr-project-manager
cd ~/.claude/skills/hr-project-manager
```

### **Step 2: Create Skill Files**
```
hr-project-manager/
├── skill.json           # Skill metadata
├── requirements.txt     # Python dependencies
├── hr_tracker.py        # Main Excel functions
├── linear_sync.py       # Linear integration
├── sprint_reports.py    # Report generation
├── validators.py        # Data validation
├── utils.py            # Helper functions
└── tests/              # Unit tests
    ├── test_tracker.py
    └── test_linear.py
```

### **Step 3: skill.json Configuration**
```json
{
  "name": "hr-project-manager",
  "version": "1.0.0",
  "description": "Excel tracker manipulation and Linear sync for HR sprint planning",
  "author": "Pernell",
  "language": "python",
  "entry_point": "hr_tracker.py",
  "dependencies": [
    "openpyxl>=3.1.2",
    "pandas>=2.1.0",
    "python-dateutil>=2.8.2",
    "requests>=2.31.0"
  ],
  "commands": {
    "read": "Read Excel tracker and display sprint items",
    "update": "Update tracker with sprint status",
    "sync": "Sync Excel to Linear",
    "report": "Generate sprint summary report",
    "email": "Create sprint confirmation email",
    "validate": "Validate tracker data integrity",
    "breakdown": "Suggest task breakdown for large items"
  },
  "config": {
    "tracker_path": "${HR_TRACKER_PATH}",
    "linear_api_key": "${LINEAR_API_KEY}",
    "linear_team_id": "${LINEAR_TEAM_ID}"
  }
}
```

### **Step 4: Install Dependencies**
```bash
pip install -r requirements.txt
```

### **Step 5: Add to Claude Code**
```bash
claude code skill add hr-project-manager
```

---

## 💡 Usage Patterns for Pernell

### **Weekly Sprint Workflow**

**Wednesday COB - Prep for Tomorrow**
```bash
claude code "Show me sprint items for tomorrow's meeting"
claude code "Validate tracker data"
```

**Thursday - After Sprint Meeting**
```bash
claude code "Update sprint: HR-48 complete, HR-49 80% in progress with note 'submitting EOD', HR-50 complete"
claude code "Save tracker with today's date"
claude code "Generate sprint email for team"
```

**Thursday - Sync to Linear**
```bash
claude code "Sync Excel tracker to Linear"
```

**Friday - Progress Check**
```bash
claude code "Show items marked 'In Progress' with blockers"
```

### **Monthly Maintenance**

```bash
claude code "Generate sprint velocity report for November"
claude code "Show most common blockers this month"
claude code "List all items pushed to next sprint"
```

---

## 🎯 Success Criteria

The skill is successful if:

1. ✅ **Excel Integrity**: Never corrupts Excel formulas or formatting
2. ✅ **Data Accuracy**: Reads and writes data correctly 100% of time
3. ✅ **Linear Sync**: Successfully syncs status without conflicts
4. ✅ **Performance**: Operations complete in <5 seconds
5. ✅ **Error Handling**: Graceful failures with helpful error messages
6. ✅ **Documentation**: All functions clearly documented
7. ✅ **Testing**: >90% code coverage with unit tests

---

## 📞 Support & Maintenance

**Skill Owner:** Pernell  
**Update Frequency:** As needed based on process evolution  
**Issue Tracking:** Note bugs/enhancements in Sprint Evolution Tracker  

**Common Issues:**
- Excel file locked: Close Excel before running skill
- Linear API rate limits: Add backoff/retry logic
- Date parsing errors: Ensure consistent MM/DD/YYYY format
- Missing dependencies: Re-run `pip install -r requirements.txt`

---

## 🎓 Learning Resources

**Excel with Python:**
- openpyxl documentation: https://openpyxl.readthedocs.io/
- pandas Excel I/O: https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html

**Linear API:**
- Linear GraphQL API: https://developers.linear.app/docs/graphql/working-with-the-graphql-api
- Python requests library: https://requests.readthedocs.io/

**Claude Code Skills:**
- Skill development guide: https://docs.anthropic.com/claude/docs/claude-code-skills

---

## 🔄 Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0.0 | Nov 18, 2025 | Initial skill specification | Pernell + Claude |

---

*End of HR Project Manager Skill Instructions*

**Next Steps:**
1. Review this specification
2. Set up skill directory structure
3. Implement core functions (start with read/update)
4. Test with sample tracker
5. Add Linear integration
6. Deploy to production
7. Train team on usage

**Questions or issues? Update this document and upload to Project Knowledge.**
