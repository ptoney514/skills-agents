# Excel Design Guru

Transform raw CSV data into professionally formatted, styled Excel workbooks with comprehensive charts, tables, and visualizations.

## What It Does

This skill specializes in creating executive-ready Excel reports with:
- **Professional styling** (branded colors, row banding, formatted headers)
- **Excel tables** with filtering and sorting
- **Charts and visualizations** (pie, bar, line, scatter, area)
- **Advanced features** (pivot tables, conditional formatting, data validation)
- **Multi-sheet workbooks** with organized data
- **HR/University-specific templates** for workforce analytics

## When to Use

Use this skill when you need to:
- Convert CSV/TSV files into styled Excel reports
- Apply professional formatting and color schemes to spreadsheets
- Create tables with filtering and sorting capabilities
- Generate charts from data (pie, bar, line, etc.)
- Build pivot tables for data analysis
- Apply conditional formatting rules
- Create multi-sheet workbooks with formatted data
- Implement custom color schemes for reports

## Quick Start

### Example 1: CSV to Formatted Table

```
I have a CSV file at data/sales_report.csv. Please convert it to a
professionally formatted Excel file with:
- Navy blue headers with white text
- Alternating gray row banding
- Auto-filter enabled
- Currency formatting for the Amount column
```

**Output**: Styled Excel file with table formatting applied

### Example 2: Data with Charts

```
Transform data/employee_stats.csv into an Excel report with:
- A formatted data table
- A pie chart showing department distribution
- A bar chart comparing salary ranges
- Professional styling throughout
```

**Output**: Multi-element workbook with data table and visualizations

### Example 3: Multi-Sheet Workbook

```
Create a workforce analytics dashboard from data/hr_data.csv with:
- Sheet 1: Executive summary with KPI cards and charts
- Sheet 2: Detailed employee data table
- Sheet 3: Turnover analysis with trend chart
- Use university navy/blue color scheme
```

**Output**: Comprehensive multi-sheet analytics workbook

## Default Styling

Unless specified otherwise, the skill applies these professional defaults:

**Colors:**
- Headers: Navy blue (#1F4E78) with white text
- Alternating rows: Light gray (#F2F2F2) and white
- Accent: Medium blue (#4472C4)

**Tables:**
- Bold header row
- Auto-filter buttons enabled
- Auto-fit columns to content
- Professional table style

**Numbers:**
- Currency: `$#,##0.00`
- Percentages: `0.0%`
- Dates: `MM/DD/YYYY`
- Large numbers with thousand separators

## Capabilities

### Data Transformation
- CSV/TSV to Excel conversion
- Excel table formatting
- Multi-sheet workbooks
- Data type preservation

### Professional Styling
- Custom color schemes
- Row banding
- Header formatting
- Cell borders and alignment
- Column width optimization

### Charts & Visualizations
- Pie charts (proportions)
- Bar/Column charts (comparisons)
- Line charts (trends)
- Scatter plots (correlations)
- Area charts (cumulative data)
- Stacked charts (composition)

### Advanced Features
- Pivot tables
- Conditional formatting (color scales, data bars, icon sets)
- Data validation (dropdowns, number ranges)
- Freeze panes
- Named ranges
- Cell protection
- Hyperlinks
- Page setup for printing

### HR/University Templates
- Workforce analytics dashboards
- Position review reports
- Recruiting pipeline reports
- Turnover analysis
- Compensation analysis
- Compliance tracking

## Reference Documentation

The skill includes comprehensive reference guides:

- **[advanced_features.md](references/advanced_features.md)** - Conditional formatting, pivot tables, data validation, protection
- **[chart_guide.md](references/chart_guide.md)** - Chart types, styling, color palettes, layout examples
- **[hr_templates.md](references/hr_templates.md)** - HR-specific report templates and best practices

## Requirements

This skill uses:
- **pandas** - For reading and manipulating data
- **openpyxl** - For full control over Excel formatting and features

The skill will request permission to install these packages if not already available.

## Example Outputs

### Before (CSV)
```
Department,Employees,Budget
Engineering,45,250000
Marketing,12,85000
Sales,28,150000
```

### After (Styled Excel)
- Professionally formatted table with navy headers
- Auto-filter buttons on each column
- Number formatting with thousand separators
- Pie chart showing employee distribution
- Bar chart comparing budgets
- All with consistent color scheme

## Tips for Best Results

1. **Be specific about styling**: Mention color preferences, chart types, or special formatting needs
2. **Provide context**: "For university leadership" or "Executive dashboard" helps select appropriate templates
3. **Specify data types**: Mention if columns are currency, percentages, or dates for proper formatting
4. **Request features**: Ask for pivot tables, conditional formatting, or specific chart types if needed
5. **Multi-sheet requests**: Clearly describe what should go on each sheet

## Integration with Other Skills

Works well with:
- **position-review-processor** - Formats position review Excel outputs
- **recruiting-evaluation** - Styles candidate evaluation reports
- **Data analysis workflows** - Presents analysis results professionally

## Common Patterns

### Pattern: CSV to Dashboard
1. Read CSV data
2. Create summary sheet with KPI cards
3. Add visualizations (charts)
4. Create detailed data sheet with formatted table
5. Apply consistent styling throughout

### Pattern: Multi-Source Report
1. Combine data from multiple CSVs
2. Organize into logical sheets
3. Create cross-sheet formulas if needed
4. Add charts and summary views
5. Format for executive presentation

### Pattern: Recurring Report Template
1. Define standard structure and styling
2. Apply to new data each period
3. Maintain consistent formatting
4. Update date ranges and metrics
5. Professional output every time

## Troubleshooting

**Issue**: Columns too narrow/wide
**Solution**: Specify "auto-fit columns" or provide desired widths

**Issue**: Numbers formatted as text
**Solution**: Mention "format as currency/number/percentage"

**Issue**: Chart colors don't match
**Solution**: Specify color scheme (e.g., "use navy and blue theme")

**Issue**: Too much data for one sheet
**Solution**: Request multi-sheet workbook with data organized by category

## Version History

- **1.0.0** (2025-10-31) - Initial skill creation with comprehensive Excel design capabilities

## Related Skills

- [position-review-processor](../position-review-skill/) - Oracle Cloud Recruiting data formatting
- [recruiting-evaluation](../recruiting-evaluation/) - Candidate evaluation reports
- [brand-guidelines](../brand-guidelines/) - For Anthropic brand-specific styling

## Notes

- Always uses `openpyxl` for full formatting control
- Preserves formulas when creating calculated fields
- Optimizes for both screen viewing and printing
- Considers accessibility (color contrast, readable fonts)
- Can adapt to custom brand guidelines when specified
