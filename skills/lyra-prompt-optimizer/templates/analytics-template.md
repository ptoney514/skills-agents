# Prompt Template: Workforce Analytics & Data Analysis

Use this template when you need to analyze HR data, calculate metrics, or generate insights from workforce data.

## Template Structure

```
You are a [ANALYST ROLE] analyzing [DATA TYPE] for [ORGANIZATION]'s HR department.

CONTEXT:
- Organization: [Company name], [industry], [size] employees
- Analysis Period: [Time range - e.g., "January - October 2024"]
- Business Objective: [What decision or action will this inform?]
- Audience: [Who will receive this analysis - CHRO, leadership, HR team]
- Current Situation: [Why is this analysis needed now?]

DATA STRUCTURE:
My [Excel/CSV/database] contains the following columns:
- [Column 1]: [Description]
- [Column 2]: [Description]
- [Column 3]: [Description]
- [Column 4]: [Description]
[List all relevant columns]

Note: [Any data quality issues, missing values, or limitations]

ANALYSIS FRAMEWORK:

1. DESCRIPTIVE METRICS (Calculate and Display):
   - [Metric 1 - e.g., "Overall turnover rate"]
   - [Metric 2 - e.g., "Average time to fill"]
   - [Metric 3 - e.g., "Cost per hire"]
   - [Metric 4]
   - [Metric 5]

2. SEGMENTATION ANALYSIS (Break down by):
   - [Dimension 1 - e.g., "Department"]
   - [Dimension 2 - e.g., "Job level"]
   - [Dimension 3 - e.g., "Location"]
   - [Dimension 4 - e.g., "Manager"]
   - [Dimension 5 - e.g., "Tenure band"]

3. TREND ANALYSIS:
   - [Time-based pattern 1 - e.g., "Month-over-month changes"]
   - [Time-based pattern 2 - e.g., "Year-over-year comparison"]
   - [Seasonal patterns if applicable]

4. COMPARATIVE ANALYSIS:
   - Compare to [benchmark 1 - e.g., "industry standards"]
   - Compare to [benchmark 2 - e.g., "prior year"]
   - Compare to [benchmark 3 - e.g., "company goals"]

5. PATTERN IDENTIFICATION:
   - Which [segments] are above/below [threshold]?
   - Are there [correlations] between [variable 1] and [variable 2]?
   - Do patterns suggest [hypothesis to test]?
   - What anomalies or outliers exist?

6. ROOT CAUSE HYPOTHESES:
   Based on data patterns, hypothesize potential causes:
   - [Potential cause 1]
   - [Potential cause 2]
   - [Potential cause 3]

7. ACTIONABLE RECOMMENDATIONS:
   Provide [3-5] specific, prioritized recommendations:
   - Each recommendation should be specific and actionable
   - Include estimated impact (high/medium/low)
   - Include implementation difficulty (quick win vs. long-term)
   - Suggest ownership (who should act)

OUTPUT FORMAT:

**Section 1: Executive Summary**
- [2-3] key findings (most critical insights)
- Overall [primary metric] vs. [benchmark]
- Top [3] recommendations

**Section 2: Detailed Metrics Dashboard**
- Summary table of all calculated metrics
- [Visualization type - e.g., "Time trend chart"]

**Section 3: Segmentation Analysis**
- Tables/charts showing [metrics] by each dimension
- Highlight segments that are outliers or concerning

**Section 4: Pattern & Trend Analysis**
- Narrative explaining what the data reveals
- Statistical observations (correlations, distributions, outliers)

**Section 5: Recommendations & Action Plan**
- Prioritized list of [specific actions]
- Impact vs. effort matrix
- Suggested timeline and owners

**Section 6: Data Quality & Limitations**
- Any data issues encountered
- Caveats about the analysis
- Recommendations for improving future data collection

ADDITIONAL REQUESTS:
- Flag any data quality issues or missing values
- Suggest [2-3] additional data points to collect for deeper analysis
- Propose a [frequency] monitoring dashboard structure
- Compare findings to [industry] benchmarks (if available)

TONE: [Analytical / Objective / Action-oriented]
Balance statistical rigor with practical business insights.
Assume audience has [basic / intermediate / advanced] analytics knowledge.
```

## Customization Guide

### Fill in these fields:

**[ANALYST ROLE]:**
- Workforce analytics specialist
- HR data analyst
- People analytics consultant
- HR metrics analyst
- Compensation analyst
- Talent analytics specialist

**[DATA TYPE]:**
- Employee turnover data
- Recruiting funnel data
- Compensation data
- Performance review data
- Engagement survey results
- Time-to-fill metrics
- Diversity & inclusion metrics
- Training completion data
- Headcount and workforce planning data

**[ORGANIZATION]:**
- Company name + industry + size
- Example: "Creighton University, higher education, 5,000 employees"

**[AUDIENCE OPTIONS]:**
- CHRO and executive leadership (high-level insights)
- HR leadership team (tactical recommendations)
- Department heads (operational focus)
- Board of Directors (strategic overview)

## Example Use Cases

### Example 1: Turnover Analysis
```
You are a workforce analytics specialist analyzing employee turnover data 
for ABC Corp's HR department.

CONTEXT:
- Organization: ABC Corp, technology, 1,200 employees
- Analysis Period: January 2024 - October 2024
- Business Objective: Identify turnover trends and develop retention 
  strategies for 2025 planning
- Audience: CHRO and HR leadership team

DATA STRUCTURE:
My Excel file contains:
- Employee ID
- Hire Date
- Termination Date (if applicable)
- Department
- Job Title
[... continue with template ...]
```

### Example 2: Diversity & Inclusion Metrics
```
You are a people analytics consultant analyzing workforce diversity data 
for XYZ Company.

CONTEXT:
- Organization: XYZ Company, financial services, 3,500 employees
- Analysis Period: Current headcount as of October 2024
- Business Objective: Assess diversity across levels and identify gaps 
  for DEI strategy planning
- Audience: Executive leadership and Board DEI committee

DATA STRUCTURE:
My database contains:
- Employee demographics (gender, race/ethnicity, veteran status)
- Job level (entry, professional, manager, director, VP, SVP, C-suite)
- Department
- Hire date
- Promotion history
[... continue with template ...]
```

### Example 3: Recruiting Efficiency
```
You are an HR metrics analyst analyzing recruiting performance data 
for Acme Inc.

CONTEXT:
- Organization: Acme Inc., manufacturing, 850 employees
- Analysis Period: Q1-Q3 2024
- Business Objective: Identify bottlenecks and improve time-to-fill for 
  critical roles in Q4 hiring push
- Audience: Talent acquisition team and hiring managers

DATA STRUCTURE:
My Excel file contains:
- Requisition ID
- Job title and level
- Posting date
- Days to fill
- Source of hire
- Number of applicants
- Number of interviews
- Offer acceptance rate
[... continue with template ...]
```

## Tips for Best Results

✅ **Define clear data structure**
- List every relevant column in your dataset
- Note data types (dates, numbers, categories)
- Mention any calculated fields

✅ **Specify business context**
- Why is this analysis needed NOW?
- What decision will it inform?
- What's the urgency level?

✅ **Request specific visualizations**
- Bar charts for comparisons
- Line charts for trends
- Scatter plots for correlations
- Heat maps for multi-dimensional data

✅ **Ask for benchmarks**
- Industry standards
- Historical company performance
- Peer company comparisons
- Goal attainment

✅ **Define actionability**
- Request specific recommendations, not just observations
- Ask for prioritization (impact vs. effort)
- Request ownership suggestions

## Common Additions

### For Predictive Analytics:
Add to ANALYSIS FRAMEWORK:
```
8. PREDICTIVE INSIGHTS:
   - Based on historical patterns, predict [future metric]
   - Identify leading indicators for [outcome]
   - Suggest early warning triggers for [risk]
```

### For Financial Impact:
Add to DESCRIPTIVE METRICS:
```
- Cost of [issue] - Calculate financial impact
- ROI of [intervention] - Estimate return on investment
- Budget implications - Project costs for recommendations
```

### For Comparative Analysis:
Add to OUTPUT FORMAT:
```
**Section 7: Competitive Benchmark Analysis**
- Compare our performance to industry standards
- Identify where we lead and where we lag
- Suggest strategies to close gaps
```

### For Dashboard Creation:
Add to ADDITIONAL REQUESTS:
```
- Design a quarterly monitoring dashboard structure
- Suggest KPIs for ongoing tracking
- Propose alert thresholds for intervention triggers
- Create a one-page visual executive summary
```

## Metrics by Analysis Type

### Turnover Analysis:
- Overall turnover rate
- Voluntary vs. involuntary split
- Regrettable vs. non-regrettable turnover
- Turnover by tenure bands
- Average tenure of departing employees
- Cost of turnover

### Recruiting Analysis:
- Time to fill
- Time to hire
- Source effectiveness
- Applicant-to-interview ratio
- Interview-to-offer ratio
- Offer acceptance rate
- Cost per hire
- Quality of hire (performance + retention)

### Compensation Analysis:
- Compa-ratio (pay vs. market)
- Pay equity analysis
- Compression issues
- Pay range penetration
- Merit increase distribution
- Total compensation cost

### DEI Analysis:
- Representation by level and department
- Hiring diversity metrics
- Promotion rate parity
- Retention rate parity
- Pay equity analysis
- Leadership pipeline diversity

---

**Save this template and customize it for your specific analytics needs!**
