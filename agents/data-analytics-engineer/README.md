# Data Analytics Engineer - Full-Stack BI Specialist

A comprehensive AI agent for building end-to-end Business Intelligence solutions, from raw data ingestion through API development to interactive dashboards with executive insights.

## Overview

This agent combines expertise across multiple domains to function as a complete BI development team:

- **Data Engineering**: ETL/ELT pipelines, data quality validation, PII compliance
- **Backend Development**: RESTful APIs, data aggregation, caching strategies
- **Frontend Development**: Interactive dashboards, data visualization, responsive UX
- **HR Analytics**: Workforce metrics, KPIs, executive reporting
- **Domain Knowledge**: HR terminology, compliance, stakeholder communication

## Quick Start

### Invoke the Agent

**In Claude Code:**
```
I need to build a workforce analytics dashboard showing headcount trends and turnover metrics.

Launch a Data Analytics Engineer agent using the prompt from
agents/data-analytics-engineer/AGENT.md
```

**The agent will guide you through:**
1. Understanding business requirements
2. Designing data pipelines and schemas
3. Building backend APIs for data retrieval
4. Creating interactive visualizations
5. Testing and deploying the solution

## What This Agent Can Do

### Data Pipeline Engineering
- Design and implement ETL/ELT workflows
- Clean, transform, and validate data from multiple sources (CSV, Excel, databases)
- Build data quality checks and audit trails
- Handle PII data with GDPR/privacy compliance
- Create data freshness indicators

### Backend API Development
- Build RESTful APIs using Flask, FastAPI, or Node.js
- Implement filtering, sorting, pagination, and aggregation endpoints
- Add caching for performance optimization (Redis, in-memory)
- Create comprehensive API documentation (OpenAPI/Swagger)
- Write unit and integration tests

### Frontend & Visualization
- Create executive-friendly interactive dashboards
- Build KPI cards, trend charts, and comparative visualizations
- Use Chart.js, D3.js, Plotly, or other modern charting libraries
- Implement filtering controls (date ranges, departments, drill-downs)
- Design responsive, accessible UIs for non-technical users

### HR & Workforce Analytics
- Calculate headcount, FTE, turnover, retention, and tenure metrics
- Analyze departmental structures and organizational hierarchies
- Track requisition pipelines and time-to-fill
- Generate YoY, QoQ, MoM trend comparisons
- Create executive summary reports with actionable insights

### Report Generation
- Generate formatted Excel reports with multiple sheets
- Create CSV/PDF exports with filters applied
- Build automated email delivery for scheduled reports
- Include metadata (export date, data freshness, filters)

## Example Use Cases

### 1. Executive Workforce Dashboard
**Goal:** Real-time dashboard showing headcount, turnover, tenure, and hiring pipeline

**Agent provides:**
- Data pipeline from HR system exports
- API endpoints for KPI calculations
- Interactive dashboard with date range filtering
- YoY trend visualizations
- Excel export functionality

### 2. Position Requisition Tracker
**Goal:** Track job requisitions from submission to approval with bottleneck identification

**Agent provides:**
- Database schema for requisition lifecycle
- Status update APIs
- Timeline visualizations (Gantt-style)
- Time-to-fill metrics
- Weekly stakeholder reports

### 3. Compensation Analysis Tool
**Goal:** Analyze salary distributions by department/job family with privacy protection

**Agent provides:**
- Secure data handling for sensitive compensation data
- Privacy-preserving aggregation APIs
- Salary distribution visualizations
- Market positioning metrics (percentiles, ranges)
- Executive compensation summaries

### 4. Diversity & Inclusion Reporting
**Goal:** Track D&I metrics across hiring, retention, and promotion

**Agent provides:**
- Demographic data pipeline with privacy controls
- D&I metric calculations (representation, hiring rates, promotion rates)
- Trend analysis dashboards
- Compliance reporting exports

## Technology Stack

**Data Processing:**
- Python (pandas, NumPy) or SQL for data transformations
- ETL frameworks (Airflow, Prefect) when needed

**Backend:**
- Flask, FastAPI (Python)
- Express (Node.js/TypeScript)
- PostgreSQL, MySQL, or cloud data warehouses

**Frontend:**
- HTML5, CSS3, JavaScript (ES6+)
- React, Vue.js, or vanilla JS
- Chart.js, D3.js, Plotly, Recharts
- Tailwind CSS, Bootstrap

**Testing:**
- pytest, Jest, Selenium
- API testing with Postman/Insomnia

**Infrastructure:**
- Docker for containerization
- AWS (S3, Lambda, RDS) or other cloud providers
- CI/CD pipelines

## When to Use This Agent

✅ **Use this agent when:**
- Building complete BI solutions from scratch
- Creating data pipelines for analytics workflows
- Developing backend APIs for data retrieval
- Building interactive dashboards for executives
- Processing HR/workforce data with complex metrics
- Handling sensitive data with compliance requirements
- Translating business requirements into technical solutions

❌ **Don't use this agent for:**
- Machine learning model development (use ML specialist)
- Database administration or infrastructure setup (use DevOps/DBA)
- Advanced statistical modeling
- Mobile app development (unless consuming BI APIs)
- Non-data-related web development

## Best Practices

### Data Quality First
- Always validate data at ingestion
- Implement comprehensive error handling
- Create data quality reports
- Test with production-scale data early

### API Design
- Follow REST conventions
- Version your APIs
- Provide clear error messages
- Document with examples
- Implement proper authentication

### Dashboard UX
- Design for non-technical users
- Show loading states and errors gracefully
- Make visualizations interactive (tooltips, drill-downs)
- Ensure mobile responsiveness
- Follow accessibility standards (WCAG 2.1)

### HR Analytics
- Understand data nuances (terminations, transfers, LOAs)
- Validate calculations against HR systems
- Handle organizational changes over time
- Respect confidentiality of employee data

### Security & Compliance
- Never expose PII in logs or errors
- Use environment variables for credentials
- Implement role-based access control
- Audit data access for compliance
- Keep dependencies updated

## Agent Configuration

**Recommended Model:** `sonnet` (balanced performance and cost)

**Other Options:**
- `opus` - For complex architecture decisions or optimization challenges
- `haiku` - For quick prototypes or simple report generation

**Thoroughness Levels:**
- `quick` - Fast prototypes and exploratory analysis
- `medium` - Standard development with testing (default)
- `very thorough` - Production-ready with comprehensive testing and documentation

## Workflow Approach

The agent follows a structured methodology:

### Phase 1: Requirements & Discovery
- Understand business problem and stakeholders
- Identify data sources and update frequency
- Define KPIs and visualizations
- Document compliance requirements

### Phase 2: Data Pipeline Development
- Design schema and transformation logic
- Build ETL with validation
- Implement data quality checks
- Create audit trails

### Phase 3: Backend API Development
- Design endpoints and data models
- Implement data retrieval with filtering
- Add caching and optimization
- Write tests and documentation

### Phase 4: Frontend Dashboard Development
- Design layout and visualization strategy
- Implement interactive charts and KPIs
- Add filtering and drill-down features
- Ensure responsive design

### Phase 5: Testing & Deployment
- End-to-end testing
- Validate data accuracy
- Load test performance
- Document deployment procedures
- Train stakeholders

## Tips for Best Results

1. **Start with clear requirements** - Document business goals and success metrics upfront
2. **Provide sample data** - Representative data helps the agent understand context
3. **Iterate frequently** - Get stakeholder feedback early and often
4. **Clarify constraints** - Share infrastructure, timeline, and compliance requirements
5. **Test with real data** - Use production-scale data for performance testing

## Common Pitfalls to Avoid

- Over-engineering early - start simple, iterate
- Skipping data validation - causes downstream issues
- Ignoring performance - test at scale early
- Missing stakeholder input - validate assumptions frequently
- Neglecting documentation - future you will thank present you

## Related Resources

**In this repository:**
- `skills/position-review-skill` - Automated Oracle HCM requisition processing
- `agents/react-stack-reviewer` - For reviewing React dashboard code
- `agents/supabase-dev-admin` - For real-time database integration
- `agents/product-growth-lead-0to1` - For defining analytics product strategy

**External Documentation:**
- [Claude Agent SDK](https://docs.claude.com/en/docs/claude-code/sdk/overview)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Chart.js Documentation](https://www.chartjs.org/)
- [pandas Documentation](https://pandas.pydata.org/)

## Version History

- **1.0.0** (2025-11-05) - Initial release
  - Full-stack BI specialist with data engineering, API, visualization, and HR analytics expertise
  - Comprehensive workflow from raw data to dashboards
  - Focus on data quality, privacy compliance, and executive communication

## Contributing

This agent is maintained in version control. To improve it:

1. Test changes in a real BI project
2. Update version number in AGENT.md
3. Document changes in version history
4. Commit with descriptive message
5. Push to GitHub for access across all projects

## License

This agent definition is part of the skills-agents repository and follows the repository's license.

---

**Questions or Issues?**
- Check the [AGENT.md](./AGENT.md) file for complete agent instructions
- Review the [agents/README.md](../README.md) for general agent usage guidance
- Refer to the repository [CLAUDE.md](../../CLAUDE.md) for repository structure
