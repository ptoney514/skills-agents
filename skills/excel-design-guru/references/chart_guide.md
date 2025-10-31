# Chart Styling Guide

## Chart Types and Use Cases

### Pie Chart
**Best for:** Showing proportions of a whole
```python
from openpyxl.chart import PieChart, Reference

chart = PieChart()
chart.title = 'Market Share by Category'
chart.style = 10

# Data
data = Reference(ws, min_col=2, min_row=1, max_row=6)
labels = Reference(ws, min_col=1, min_row=2, max_row=6)

chart.add_data(data, titles_from_data=True)
chart.set_categories(labels)

ws.add_chart(chart, 'E2')
```

### Bar Chart (Horizontal)
**Best for:** Comparing items across categories
```python
from openpyxl.chart import BarChart, Reference

chart = BarChart()
chart.type = 'bar'
chart.title = 'Sales by Region'
chart.x_axis.title = 'Sales ($)'
chart.y_axis.title = 'Region'

data = Reference(ws, min_col=2, min_row=1, max_row=6)
categories = Reference(ws, min_col=1, min_row=2, max_row=6)

chart.add_data(data, titles_from_data=True)
chart.set_categories(categories)

ws.add_chart(chart, 'E2')
```

### Column Chart (Vertical)
**Best for:** Comparing values over time or categories
```python
from openpyxl.chart import BarChart, Reference

chart = BarChart()
chart.type = 'col'  # Column chart
chart.title = 'Quarterly Revenue'
chart.x_axis.title = 'Quarter'
chart.y_axis.title = 'Revenue ($M)'

data = Reference(ws, min_col=2, min_row=1, max_row=5, max_col=3)
categories = Reference(ws, min_col=1, min_row=2, max_row=5)

chart.add_data(data, titles_from_data=True)
chart.set_categories(categories)

ws.add_chart(chart, 'E2')
```

### Line Chart
**Best for:** Showing trends over time
```python
from openpyxl.chart import LineChart, Reference

chart = LineChart()
chart.title = 'Monthly Website Traffic'
chart.x_axis.title = 'Month'
chart.y_axis.title = 'Visitors'
chart.style = 10

data = Reference(ws, min_col=2, min_row=1, max_row=13)
dates = Reference(ws, min_col=1, min_row=2, max_row=13)

chart.add_data(data, titles_from_data=True)
chart.set_categories(dates)

ws.add_chart(chart, 'E2')
```

### Stacked Bar/Column
**Best for:** Showing composition and comparison
```python
from openpyxl.chart import BarChart, Reference

chart = BarChart()
chart.type = 'col'
chart.grouping = 'stacked'
chart.title = 'Sales by Product and Region'

data = Reference(ws, min_col=2, min_row=1, max_row=6, max_col=4)
categories = Reference(ws, min_col=1, min_row=2, max_row=6)

chart.add_data(data, titles_from_data=True)
chart.set_categories(categories)

ws.add_chart(chart, 'E2')
```

### Scatter Plot
**Best for:** Showing correlation between variables
```python
from openpyxl.chart import ScatterChart, Reference, Series

chart = ScatterChart()
chart.title = 'Price vs. Sales Volume'
chart.x_axis.title = 'Price ($)'
chart.y_axis.title = 'Units Sold'

x_values = Reference(ws, min_col=2, min_row=2, max_row=10)
y_values = Reference(ws, min_col=3, min_row=2, max_row=10)

series = Series(y_values, x_values)
chart.series.append(series)

ws.add_chart(chart, 'E2')
```

### Area Chart
**Best for:** Showing cumulative totals over time
```python
from openpyxl.chart import AreaChart, Reference

chart = AreaChart()
chart.title = 'Cumulative Revenue'
chart.x_axis.title = 'Month'
chart.y_axis.title = 'Revenue ($)'

data = Reference(ws, min_col=2, min_row=1, max_row=13, max_col=3)
dates = Reference(ws, min_col=1, min_row=2, max_row=13)

chart.add_data(data, titles_from_data=True)
chart.set_categories(dates)

ws.add_chart(chart, 'E2')
```

## Chart Styling

### Colors
```python
from openpyxl.chart.series import DataPoint
from openpyxl.drawing.fill import SolidColorFillProperties, ColorChoice

# Set custom colors for pie slices
s = chart.series[0]
s.dPt = [
    DataPoint(idx=0, spPr=SolidColorFillProperties(solidFill=ColorChoice(srgbClr='4472C4'))),
    DataPoint(idx=1, spPr=SolidColorFillProperties(solidFill=ColorChoice(srgbClr='ED7D31'))),
    DataPoint(idx=2, spPr=SolidColorFillProperties(solidFill=ColorChoice(srgbClr='A5A5A5'))),
]
```

### Professional Color Palettes

**Default Blue Theme:**
- Primary: #4472C4
- Secondary: #ED7D31
- Tertiary: #A5A5A5
- Accent 1: #FFC000
- Accent 2: #5B9BD5

**University/Corporate:**
- Navy: #1F4E78
- Light Blue: #7BA0C0
- Gray: #767676
- Accent: #C55A11

**Traffic Light:**
- Green: #70AD47
- Yellow: #FFC000
- Red: #E74C3C

### Chart Size and Position
```python
# Standard chart size
chart.width = 15  # cm
chart.height = 7.5  # cm

# Position (cell reference)
ws.add_chart(chart, 'E2')  # Top-left at E2

# Multiple charts in a row
ws.add_chart(chart1, 'A15')
ws.add_chart(chart2, 'H15')
ws.add_chart(chart3, 'O15')
```

### Legend Positioning
```python
# Legend positions: 'r' (right), 'l' (left), 't' (top), 'b' (bottom)
chart.legend.position = 'r'

# Hide legend
chart.legend = None
```

### Data Labels
```python
# Show values on data points
chart.dataLabels = DataLabel()
chart.dataLabels.showVal = True
chart.dataLabels.showPercent = True  # For pie charts
```

### Gridlines
```python
# Major gridlines
chart.y_axis.majorGridlines = None  # Remove gridlines

# Custom gridlines
from openpyxl.chart.axis import ChartLines
chart.y_axis.majorGridlines = ChartLines()
```

## Chart Layout Examples

### Dashboard Layout (Multiple Charts)
```python
# Top row: Two column charts
ws.add_chart(column_chart_1, 'A2')
ws.add_chart(column_chart_2, 'H2')

# Middle row: Line chart spanning full width
line_chart.width = 22
ws.add_chart(line_chart, 'A17')

# Bottom row: Three pie charts
ws.add_chart(pie_chart_1, 'A32')
ws.add_chart(pie_chart_2, 'G32')
ws.add_chart(pie_chart_3, 'M32')
```

### Report Layout (Chart + Data Table)
```python
# Data table: A1:E15
# Chart positioned to the right
chart.width = 12
chart.height = 8
ws.add_chart(chart, 'G2')
```

## Best Practices

1. **Choose appropriate chart type** for the data story
2. **Limit colors** to 3-5 for clarity
3. **Use consistent styling** across all charts in a workbook
4. **Add descriptive titles** and axis labels
5. **Remove chart junk** (unnecessary gridlines, borders)
6. **Size appropriately** - not too large or small
7. **Position strategically** - near related data
8. **Consider colorblind accessibility** - use patterns or sufficient contrast
