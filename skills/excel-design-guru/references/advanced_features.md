# Advanced Excel Features

## Conditional Formatting

### Color Scales
```python
from openpyxl.formatting.rule import ColorScaleRule

# Three-color scale (red-yellow-green)
rule = ColorScaleRule(
    start_type='min', start_color='F8696B',
    mid_type='percentile', mid_value=50, mid_color='FFEB84',
    end_type='max', end_color='63BE7B'
)
ws.conditional_formatting.add('B2:B100', rule)
```

### Data Bars
```python
from openpyxl.formatting.rule import DataBarRule

# Add data bars to a range
rule = DataBarRule(
    start_type='min', start_value=0,
    end_type='max', end_value=100,
    color='4472C4'
)
ws.conditional_formatting.add('C2:C100', rule)
```

### Icon Sets
```python
from openpyxl.formatting.rule import IconSetRule

# Traffic lights
rule = IconSetRule('3TrafficLights1', 'percentile', [0, 33, 67])
ws.conditional_formatting.add('D2:D100', rule)
```

## Pivot Tables

```python
from openpyxl.pivot.table import TableDefinition, PivotTable
from openpyxl.pivot.fields import RowFields, ColumnFields, DataFields

# Create table from data range
tab = TableDefinition(ref='A1:E100', displayName='DataTable')

# Add pivot table
pivot = PivotTable()
pivot.addRowField('Category')
pivot.addDataField('Sales', 'Sum')

ws_pivot = wb.create_sheet('Pivot')
ws_pivot.add_pivot_table(pivot, 'A3')
```

## Data Validation

### Dropdown Lists
```python
from openpyxl.worksheet.datavalidation import DataValidation

# Create dropdown
dv = DataValidation(type="list", formula1='"Option 1,Option 2,Option 3"')
dv.add('B2:B100')
ws.add_data_validation(dv)
```

### Number Validation
```python
# Whole numbers between 1-100
dv = DataValidation(type="whole", operator="between", formula1=1, formula2=100)
dv.error = 'Enter a number between 1 and 100'
dv.add('C2:C100')
ws.add_data_validation(dv)
```

## Freeze Panes

```python
# Freeze first row
ws.freeze_panes = 'A2'

# Freeze first column
ws.freeze_panes = 'B1'

# Freeze first row and column
ws.freeze_panes = 'B2'
```

## Cell Protection

```python
from openpyxl.styles import Protection

# Protect worksheet but allow certain cells to be edited
ws.protection.sheet = True
ws.protection.password = 'secret'

# Unlock specific cells
for row in ws['B2:B100']:
    for cell in row:
        cell.protection = Protection(locked=False)
```

## Merged Cells

```python
# Merge cells
ws.merge_cells('A1:D1')

# Unmerge cells
ws.unmerge_cells('A1:D1')

# Center text in merged cell
ws['A1'].alignment = Alignment(horizontal='center', vertical='center')
```

## Hyperlinks

```python
# Add hyperlink
ws['A1'].hyperlink = 'https://example.com'
ws['A1'].value = 'Click Here'
ws['A1'].style = 'Hyperlink'

# Internal link
ws['B1'].hyperlink = '#Sheet2!A1'
ws['B1'].value = 'Go to Sheet 2'
```

## Images

```python
from openpyxl.drawing.image import Image

# Add image
img = Image('logo.png')
img.width = 200
img.height = 100
ws.add_image(img, 'A1')
```

## Named Ranges

```python
from openpyxl.workbook.defined_name import DefinedName

# Create named range
new_range = DefinedName('SalesData', attr_text='Sheet1!$A$1:$C$100')
wb.defined_names.append(new_range)

# Use in formula
ws['D1'] = '=SUM(SalesData)'
```

## Custom Number Formats

```python
# Custom formats
ws['A1'].number_format = '$#,##0.00_);[Red]($#,##0.00)'  # Currency with negative in red
ws['B1'].number_format = '0.00%'  # Percentage
ws['C1'].number_format = '#,##0'  # Thousands separator
ws['D1'].number_format = 'mm/dd/yyyy'  # Date
ws['E1'].number_format = '[h]:mm:ss'  # Time duration
```

## Cell Comments

```python
from openpyxl.comments import Comment

# Add comment
comment = Comment('This is a note', 'Author Name')
ws['A1'].comment = comment
```

## Page Setup

```python
# Set print settings
ws.page_setup.orientation = ws.ORIENTATION_LANDSCAPE
ws.page_setup.paperSize = ws.PAPERSIZE_LETTER
ws.page_setup.fitToPage = True
ws.page_setup.fitToHeight = 1
ws.page_setup.fitToWidth = 1

# Print area
ws.print_area = 'A1:G50'

# Print titles (repeat headers)
ws.print_title_rows = '1:1'
ws.print_title_cols = 'A:A'
```
