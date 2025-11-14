# Example: Turnover Analysis Optimization

This example shows how Lyra transforms a basic data analysis request into a structured, actionable prompt.

## Original Request (Vague)
```
I have turnover data in Excel. What can AI tell me about it?
```

## Lyra's Analysis

### DECONSTRUCT
- **Core Intent:** Analyze employee turnover data to gain insights
- **Key Entities:** Turnover data, Excel file, analytics
- **Missing Context:**
  - What specific insights are needed?
  - What's in the Excel file (columns, time period)?
  - Who is the audience for the analysis?
  - What decisions will this inform?
  - Organizational context

### DIAGNOSE
- **Clarity Issues:** "What can AI tell me" is too open-ended
- **Specificity Gaps:** No data structure defined, no output format, no business context
- **Complexity Level:** DETAIL mode (requires structured analysis framework)
- **Business Need:** Likely needs actionable recommendations, not just data description

### DEVELOP
**Techniques to Apply:**
- Role Assignment (Workforce analytics specialist)
- Context Layering (Organization, data structure, time period)
- Output Specification (Metrics, visualizations, recommendations)
- Insight Framework (What to calculate, what patterns to find)
- Action Orientation (Recommendations, not just observations)

## Optimized Prompt

```
You are a workforce analytics specialist analyzing employee turnover data 
for Creighton University's HR department.

CONTEXT:
- Organization: Creighton University (higher education, ~5,000 employees)
- Analysis Period: [Specify time range, e.g., "January 2024 - October 2024"]
- Business Objective: Identify turnover trends, root causes, and develop 
  retention strategies for FY2025 planning
- Audience: CHRO and HR leadership team

DATA STRUCTURE:
My Excel file contains the following columns:
- Employee ID
- Hire Date
- Termination Date (if applicable)
- Department
- Job Title / Job Family
- Employment Status (Full-Time, Part-Time)
- Termination Type (Voluntary, Involuntary, Retirement)
- Termination Reason (category)
- Manager Name / Manager ID
- Location (Campus/Building)
- Annual Salary / Compensation Band
- Performance Rating (last available)
- Tenure (years of service)

ANALYSIS FRAMEWORK:

1. DESCRIPTIVE METRICS (Calculate and Display):
   - Overall turnover rate (% of workforce)
   - Voluntary vs. involuntary turnover split
   - Average tenure of departing employees
   - Turnover by month (identify seasonal patterns)
   - Cost of turnover estimate (if compensation data allows)

2. SEGMENTATION ANALYSIS (Break down turnover by):
   - Department / College (identify high-risk areas)
   - Job family / role type (faculty vs. staff vs. admin)
   - Tenure bands (< 1 year, 1-3 years, 3-5 years, 5+ years)
   - Compensation bands (identify if turnover correlates with pay)
   - Performance level (are high performers leaving?)
   - Manager (identify if certain managers have higher turnover)

3. PATTERN IDENTIFICATION:
   - Which departments have turnover >15% (industry benchmark)?
   - Are there tenure "danger zones" (e.g., 1-2 year mark)?
   - Do voluntary terminations cluster around certain times of year?
   - Are there manager-specific patterns?
   - Does turnover correlate with performance ratings?

4. ROOT CAUSE HYPOTHESES:
   Based on the data patterns, hypothesize potential root causes:
   - Compensation competitiveness
   - Management quality
   - Career development opportunities
   - Onboarding effectiveness (if high turnover < 1 year)
   - Work-life balance issues
   - Market competition / poaching

5. ACTIONABLE RECOMMENDATIONS:
   Provide 3-5 specific, prioritized recommendations such as:
   - "Focus retention efforts on [specific department] with [specific tactic]"
   - "Conduct stay interviews with high performers in [segment]"
   - "Review compensation for [job family] against market"
   - "Implement manager training for [managers with high turnover]"

OUTPUT FORMAT:

**Section 1: Executive Summary**
- 2-3 key findings (most critical insights)
- Overall turnover rate vs. higher education benchmark
- Top 3 recommendations

**Section 2: Detailed Metrics Dashboard**
- Summary table of all metrics calculated
- Month-by-month turnover trend

**Section 3: Segmentation Analysis**
- Tables/charts showing turnover by each dimension
- Highlight segments above benchmark

**Section 4: Pattern & Trend Analysis**
- Narrative explaining what the data reveals
- Statistical observations (correlations, outliers)

**Section 5: Recommendations & Action Plan**
- Prioritized list of retention strategies
- Estimated impact (high/medium/low)
- Implementation difficulty (quick win vs. long-term)
- Suggested owners (CHRO, dept heads, managers)

**Section 6: Data Quality Notes**
- Any limitations or gaps in the data
- Recommendations for improving future data collection

ADDITIONAL REQUESTS:
- Flag any data quality issues or missing values
- Suggest 2-3 additional data points to collect for deeper analysis
- Propose a quarterly turnover dashboard structure for ongoing monitoring
- Compare findings to higher education industry benchmarks (if available)

TONE: Analytical, objective, action-oriented
Balance statistical rigor with practical business insights.
```

## Key Improvements Made

✅ **Added Organization Context**
- Specified Creighton University and industry (higher ed)
- Defined employee count (~5,000)
- Clarified audience (CHRO and HR leadership)

✅ **Defined Data Structure**
- Listed all available columns in the Excel file
- Set clear expectations for what data exists
- Enables AI to provide specific, relevant analysis

✅ **Created Analysis Framework**
- 6 structured sections covering metrics, segmentation, patterns, root causes, and recommendations
- Each section has specific deliverables
- Progressive flow from descriptive to prescriptive

✅ **Specified Output Format**
- 6-section report structure
- Tables, charts, and narrative components
- Executive summary for leadership
- Action-oriented recommendations

✅ **Added Business Context**
- Purpose: FY2025 retention planning
- Benchmarks: Higher education standards (>15% threshold)
- Practical focus: actionable recommendations

✅ **Included Quality Controls**
- Data quality assessment requested
- Limitations acknowledgment
- Future data collection suggestions

## Techniques Applied

1. **Role Assignment:** "Workforce analytics specialist"
2. **Context Layering:** Organization size, industry, business objective, audience
3. **Data Structure Definition:** Explicit column listing
4. **Insight Framework:** 6-step analysis progression
5. **Output Specification:** Detailed report structure with sections
6. **Action Orientation:** Recommendations prioritized by impact and difficulty
7. **Benchmarking:** Industry standards embedded (>15% turnover)

## Expected Results

### What You'll Get:
A comprehensive turnover analysis including:
- Executive summary with top 3 insights and recommendations
- Calculated metrics (turnover rate, voluntary/involuntary split, tenure analysis)
- Segmentation analysis by department, job family, tenure, compensation, manager
- Pattern identification (danger zones, seasonal trends, correlations)
- Root cause hypotheses based on data patterns
- Prioritized action plan with 3-5 specific retention strategies
- Data quality assessment and future collection recommendations
- Quarterly dashboard proposal for ongoing monitoring

### Time Saved:
- **Original (vague prompt):** 45-60 minutes explaining, iterating, clarifying
- **Optimized:** 10-15 minutes to review comprehensive analysis on first try

### Quality Improvement:
- **Before:** Generic statistics without business context or actionable recommendations
- **After:** Strategic insights tied to business objectives with clear action plan

## Pro Tips for Further Refinement

🎯 **Add more context if available:**
- Include your organization's historical turnover rate for comparison
- Add industry benchmarks specific to your institution type
- Mention any known factors (reorganization, budget cuts, market conditions)

🎯 **Request specific analyses:**
- "Compare pre-COVID vs. post-COVID turnover patterns"
- "Analyze turnover by diversity dimensions (if data available)"
- "Calculate regrettable vs. non-regrettable turnover"

🎯 **For ongoing monitoring:**
- "Create a Power BI dashboard structure for this analysis"
- "Suggest predictive indicators for at-risk employees"
- "Design an early warning system for retention issues"

🎯 **For presentation:**
- "Format this as an executive PowerPoint presentation"
- "Create a one-page visual dashboard for leadership"
- "Generate talking points for Board presentation"

## Common Variations

### Variation 1: Turnover Cost Analysis
Add to the prompt:
```
Calculate the financial impact of turnover including:
- Replacement costs (recruiting, onboarding, training)
- Productivity loss during vacancy
- Lost institutional knowledge
- Total annual cost of turnover
```

### Variation 2: Predictive Analysis
Add to the prompt:
```
Based on historical patterns, identify:
- Which current employees are at highest risk of leaving
- Predictive indicators (tenure + performance + compensation)
- Proactive retention interventions
```

### Variation 3: Exit Interview Integration
Add to the prompt:
```
I also have exit interview feedback data. Cross-reference:
- Stated reasons for leaving vs. data patterns
- Sentiment analysis of exit interview comments
- Validate/challenge data-driven hypotheses
```

## Use This Pattern For:
- Compensation analysis
- Diversity & inclusion metrics
- Recruitment funnel analysis
- Performance distribution analysis
- Headcount planning
- Engagement survey analysis
- Any HR data analysis requiring structure and insights

---

*This example demonstrates how to transform "What does my data say?" into "Here's what your data reveals, why it matters, and what to do about it."*
