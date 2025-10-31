# HR Report Templates

## Workforce Analytics Dashboard

Standard layout for university HR reports:

### Sheet 1: Executive Summary
```python
# Header section (A1:F3)
- Report Title: Bold, 18pt, Navy (#1F4E78)
- Date Range
- Key Metrics in highlight boxes

# KPI Cards (Row 5-8)
- Total Headcount
- New Hires
- Turnover Rate
- Average Tenure

# Charts (Row 10+)
- Headcount by Department (Column chart)
- Turnover Trend (Line chart)
- Demographics Breakdown (Pie chart)
```

### Sheet 2: Detailed Data
```python
# Formatted table with:
- Employee ID
- Name
- Department
- Position
- Hire Date
- Status
- FTE
- Salary Band

# Styling:
- Freeze first row
- Filter buttons enabled
- Alternating row colors
- Currency formatting for salary
- Date formatting for dates
```

## Position Review Report

### Layout
```python
# Columns:
A: Position Number
B: Position Title
C: Department
D: Budget Code
E: FTE
F: Incumbent
G: Hire Date
H: Status
I: Notes

# Formatting:
- Header: Navy background, white bold text
- Conditional formatting: Vacant positions in yellow
- Row banding: Light gray alternating
- Auto-filter enabled
- Freeze panes at row 2
```

## Recruiting Pipeline Report

### Structure
```python
# Sheet 1: Pipeline Overview
- Funnel chart showing applicant stages
- Time-to-fill metrics
- Source effectiveness

# Sheet 2: Active Requisitions
Table with:
- Req Number
- Position Title
- Department
- Hiring Manager
- Posted Date
- Days Open
- Applicants
- Status

# Conditional formatting:
- Green: <30 days
- Yellow: 30-60 days
- Red: >60 days
```

## Student Employment Report

### Data Sheet
```python
# Columns:
- Student Name
- Student ID
- Position
- Department
- Supervisor
- Start Date
- End Date
- Hours/Week
- Hourly Rate

# Summary metrics:
- Total student employees
- Total hours/week
- Total budget impact
- By department breakdown
```

## Turnover Analysis

### Monthly Trend Sheet
```python
# Line chart:
- X-axis: Months (last 12)
- Y-axis: Turnover rate (%)
- Multiple series by employee category

# Table below:
- Month
- Voluntary separations
- Involuntary separations
- Total headcount
- Turnover rate
```

### Department Comparison
```python
# Bar chart:
- Departments ranked by turnover
- Color coding by severity
- Target line at acceptable rate

# Supporting table:
- Department name
- Headcount
- Separations
- Turnover rate
- YTD trend
```

## Compensation Analysis

### Salary Distribution
```python
# Histogram showing:
- Salary ranges (bins)
- Employee count per range
- Department overlay

# Summary stats:
- Mean
- Median
- 25th percentile
- 75th percentile
- Min/Max
```

### Market Comparison
```python
# Scatter plot:
- Internal salary vs. market rate
- Color by department
- Trend line

# Gap analysis table:
- Position
- Internal avg
- Market rate
- Variance
- Priority level
```

## Compliance Tracking

### Required Reports Layout
```python
# I-9 Compliance
- Employee count
- Verification status
- Expiring documents
- Action items

# Certification Status
- Professional licenses
- Training requirements
- Completion rates
- Upcoming deadlines
```

## Standard Color Schemes

### Creighton University Theme
```python
navy = '1F4E78'      # Primary
blue = '4472C4'      # Secondary
gray = 'A5A5A5'      # Neutral
light_gray = 'F2F2F2'  # Alternating rows
white = 'FFFFFF'      # Background
```

### Status Colors
```python
green = '70AD47'     # Complete/Good
yellow = 'FFC000'    # Warning/Pending
red = 'C55A11'       # Alert/Overdue
```

## Professional Report Best Practices

1. **Consistent Branding**: Use university colors and style throughout
2. **Clean Layout**: White space is good, don't overcrowd
3. **Clear Hierarchy**: Size and color indicate importance
4. **Accessible Design**: High contrast, readable fonts
5. **Action-Oriented**: Highlight what needs attention
6. **Data Sources**: Note data pull date and system source
7. **Print-Friendly**: Consider printed format even if digital

## Header Template
```python
# Row 1: Title
ws['A1'] = 'WORKFORCE ANALYTICS REPORT'
ws['A1'].font = Font(size=18, bold=True, color='1F4E78')

# Row 2: Date range
ws['A2'] = f'Report Period: {start_date} - {end_date}'
ws['A2'].font = Font(size=11, color='767676')

# Row 3: Run date
ws['A3'] = f'Generated: {datetime.now().strftime("%m/%d/%Y")}'
ws['A3'].font = Font(size=9, color='A5A5A5')
```

## KPI Card Template
```python
def create_kpi_card(ws, cell, label, value, format_type='number'):
    # Label
    ws[cell].font = Font(size=10, color='767676')
    ws[cell].value = label

    # Value cell (one row below)
    value_cell = cell[0] + str(int(cell[1:]) + 1)
    ws[value_cell].font = Font(size=20, bold=True, color='1F4E78')

    if format_type == 'currency':
        ws[value_cell].number_format = '$#,##0'
    elif format_type == 'percent':
        ws[value_cell].number_format = '0.0%'
    else:
        ws[value_cell].number_format = '#,##0'

    ws[value_cell].value = value
```
