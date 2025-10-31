---
name: excel-design-guru
description: Expert Excel file designer specializing in converting CSV/raw data into professionally formatted, styled Excel workbooks with tables, charts, pivot tables, conditional formatting, and custom styling. Use when you need to transform CSV files into styled Excel reports, apply professional formatting and color schemes to spreadsheets, create tables with filtering and sorting capabilities, generate charts (pie, bar, line, etc.) from data, build pivot tables for analysis, apply conditional formatting rules, create multi-sheet workbooks with formatted data, or implement custom color schemes and styling preferences for reports. This skill can be called by other agents or used directly for Excel design tasks.
---

# Excel Design Guru

This skill specializes in transforming raw data into professionally designed Excel files with comprehensive formatting, styling, and visualization capabilities.

## Core Capabilities

### 1. Data Transformation
- Convert CSV/TSV files to formatted Excel workbooks
- Apply Excel table formatting with filtering and sorting
- Create multi-sheet workbooks with organized data
- Preserve data types and handle special characters

### 2. Professional Styling
- Apply custom color schemes to tables and headers
- Implement row banding (alternating colors) for readability
- Format headers with bold text and background colors
- Apply cell borders and alignment
- Set appropriate column widths and row heights

### 3. Charts and Visualizations
- Pie charts for proportional data
- Bar/column charts for comparisons
- Line charts for trends over time
- Combination charts for multi-series data
- Position charts appropriately on sheets
- Apply colors matching the overall theme

### 4. Advanced Features
- Create pivot tables for data analysis
- Apply conditional formatting (color scales, data bars, icon sets)
- Add formulas for calculations
- Implement data validation rules
- Freeze panes for easier navigation
- Create summary sheets with key metrics

### 5. HR/University-Specific Formatting
- Professional report layouts for workforce analytics
- Clean, accessible designs for university leadership
- Branded color schemes (when specified)
- Executive-friendly summary dashboards

## Default Style Preferences

Unless otherwise specified, apply these professional defaults:

### Colors
- **Headers**: Navy blue background (#1F4E78) with white text
- **Alternating rows**: Light gray (#F2F2F2) and white
- **Accent color**: Medium blue (#4472C4)
- **Data emphasis**: Dark blue text (#1F4E78)

### Tables
- Convert ranges to Excel tables with filter buttons
- Apply "Table Style Medium 2" or similar professional style
- Bold header row
- Auto-fit columns to content

### Numbers
- Currency: `$#,##0.00`
- Percentages: `0.0%`
- Dates: `MM/DD/YYYY`
- Large numbers: `#,##0` with thousand separators

### Charts
- Clean, minimal design
- Descriptive titles
- Labeled axes
- Legend when needed
- Match table color scheme

## Workflow

1. **Understand Requirements**
   - Identify data source (CSV, existing Excel, etc.)
   - Clarify desired styling, charts, and special formatting
   - Determine if multiple sheets are needed

2. **Data Preparation**
   - Read source data using pandas
   - Clean and transform as needed
   - Prepare data for tables and charts

3. **Create Excel File**
   - Use openpyxl for full control over formatting
   - Build structure (sheets, tables, headers)
   - Apply all styling and formatting

4. **Add Visualizations**
   - Create requested charts
   - Position appropriately
   - Style to match theme

5. **Advanced Features**
   - Add pivot tables if requested
   - Apply conditional formatting
   - Add formulas and calculations

6. **Finalize**
   - Save workbook
   - If formulas used, run recalc.py to calculate values
   - Verify output meets requirements

## Example Usage Patterns

### Pattern 1: CSV to Formatted Table
```python
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils.dataframe import dataframe_to_rows

# Read CSV
df = pd.read_csv('data.csv')

# Create workbook
wb = Workbook()
ws = wb.active
ws.title = 'Report'

# Write data
for row in dataframe_to_rows(df, index=False, header=True):
    ws.append(row)

# Style header
header_fill = PatternFill(start_color='1F4E78', end_color='1F4E78', fill_type='solid')
header_font = Font(bold=True, color='FFFFFF')

for cell in ws[1]:
    cell.fill = header_fill
    cell.font = header_font
    cell.alignment = Alignment(horizontal='center')

# Auto-fit columns
for column in ws.columns:
    max_length = max(len(str(cell.value)) for cell in column)
    ws.column_dimensions[column[0].column_letter].width = max_length + 2

wb.save('output.xlsx')
```

### Pattern 2: Adding Charts
```python
from openpyxl.chart import PieChart, Reference

# Create chart
chart = PieChart()
chart.title = 'Distribution'
chart.style = 10

# Data reference
data = Reference(ws, min_col=2, min_row=1, max_row=ws.max_row)
labels = Reference(ws, min_col=1, min_row=2, max_row=ws.max_row)

chart.add_data(data, titles_from_data=True)
chart.set_categories(labels)

# Position chart
ws.add_chart(chart, 'E2')
```

### Pattern 3: Alternating Row Colors
```python
from openpyxl.styles import PatternFill

# Light gray for alternating rows
light_gray = PatternFill(start_color='F2F2F2', end_color='F2F2F2', fill_type='solid')

for row_idx, row in enumerate(ws.iter_rows(min_row=2, max_row=ws.max_row), start=2):
    if row_idx % 2 == 0:
        for cell in row:
            cell.fill = light_gray
```

## Important Notes

- **Always use openpyxl** for full formatting control (not pandas alone)
- **Preserve formulas**: Use formulas instead of hardcoded calculations
- **Run recalc.py**: After creating files with formulas to calculate values
- **Test output**: Verify formatting appears as expected
- **Column width**: Auto-fit or set explicit widths for readability
- **Freeze panes**: Consider freezing header rows for long tables

## Integration with Other Skills

This skill works well with:
- **xlsx skill**: For complex formula requirements and financial modeling
- **HR program manager skills**: For formatting workforce reports
- **Data analysis workflows**: For presenting analysis results professionally

## References

- For advanced Excel functionality, see `references/advanced_features.md`
- For chart styling options, see `references/chart_guide.md`
- For HR-specific templates, see `references/hr_templates.md`
