# Skills & Agents Catalog

A comprehensive reference of all skills and agents available in this repository.

**Last Updated:** 2025-11-05

---

## Table of Contents

- [Quick Reference](#quick-reference)
- [Product & Growth Agents](#product--growth-agents)
- [Development Agents](#development-agents)
- [Design & UX Agents](#design--ux-agents)
- [Data & Analytics Agents](#data--analytics-agents)
- [Automation Skills](#automation-skills)
- [Writing & Documentation Skills](#writing--documentation-skills)
- [HR & Recruiting Skills](#hr--recruiting-skills)
- [Design & Brand Skills](#design--brand-skills)

---

## Quick Reference

### When to Use What?

| Need | Use This Agent/Skill |
|------|---------------------|
| **Write a comprehensive PRD** | [Product Manager](#product-manager-core) |
| **Design system architecture** | [Technical Architect](#technical-architect) |
| **Create polished UI mockups** | [UX/UI Designer](#uxui-designer) |
| **Run A/B tests and analytics** | [Product Operations](#product-operations) |
| **Fast MVP planning (0→1)** | [Product & Growth Lead 0→1](#product--growth-lead-01) |
| **Full-stack BI solution** | [Data Analytics Engineer](#data-analytics-engineer) |
| **Review React code** | [React Stack Reviewer](#react-stack-reviewer) |
| **Audit UX design** | [UX Site Reviewer](#ux-site-reviewer) |
| **Write how-to guides** | [How-to Guide Writer](#how-to-guide-writer) |
| **Create quick-reference job aids** | [Job Aid Writer](#job-aid-writer) |
| **Optimize AI prompts for HR** | [Lyra Prompt Optimizer](#lyra-prompt-optimizer) |
| **Track recruiting pipelines** | [Recruiting Tracker](#recruiting-tracker) |

---

## Product & Growth Agents

### Product Manager (Core)

**Location:** `agents/product-manager/`

**Purpose:** Expert Product Manager for PRDs, roadmaps, user stories, prioritization frameworks, stakeholder management, and user research across all product stages.

**Key Capabilities:**
- Product discovery & user research (personas, JTBD, customer interviews)
- Comprehensive PRD creation with acceptance criteria
- Prioritization frameworks (RICE, Value vs. Effort, MoSCoW, Kano)
- Product roadmapping (Now/Next/Later, quarterly timelines)
- Stakeholder management and communication
- Product strategy & vision (North Star Metric)
- Competitive analysis and market research
- Product metrics & analytics

**When to Use:**
- Writing comprehensive PRDs for complex features
- Prioritizing backlog using frameworks (RICE, Value vs. Effort)
- Creating quarterly or annual product roadmaps
- Conducting user research and defining personas
- Managing stakeholder alignment
- Defining product strategy and vision

**Related:** Product Operations, Technical Architect, UX/UI Designer

---

### Technical Architect

**Location:** `agents/technical-architect/`

**Purpose:** Expert in deep system design, scalability, architecture patterns, technology selection, API design, microservices, cloud infrastructure, and technical decision-making.

**Key Capabilities:**
- System architecture & design patterns (Monolithic, Microservices, Event-Driven, Serverless)
- Scalability & performance optimization (load balancing, caching, sharding)
- API design & contracts (RESTful, GraphQL, gRPC)
- Data modeling & database design (SQL vs. NoSQL, schema design)
- Microservices architecture (bounded contexts, service communication)
- Cloud architecture (AWS/GCP/Azure: compute, storage, databases, networking)
- Security architecture (OAuth 2.0, JWT, RBAC, encryption)
- Architecture Decision Records (ADRs)
- Migration planning (monolith to microservices, legacy modernization)

**When to Use:**
- Designing system architecture from scratch
- Scaling from 10K to 10M users
- Choosing between technologies (SQL vs. NoSQL, monolith vs. microservices)
- Designing REST/GraphQL API contracts
- Planning database schema and data models
- Architecting for performance (<100ms p95 latency)
- Designing cloud infrastructure
- Writing Architecture Decision Records

**Related:** Product Manager, Data Analytics Engineer

---

### UX/UI Designer

**Location:** `agents/ux-ui-designer/`

**Purpose:** Expert in polished visual design, design systems, component libraries, user experience patterns, accessibility (WCAG), responsive design, and high-fidelity mockups.

**Key Capabilities:**
- User experience (UX) design (user research, journey maps, information architecture)
- Visual design (UI) (visual hierarchy, typography, color theory, spacing)
- Design systems & component libraries (buttons, forms, cards, modals, navigation)
- Responsive design (mobile, tablet, desktop breakpoints)
- Accessibility (WCAG 2.1 AA compliance, contrast, keyboard nav, alt text)
- Design tools & deliverables (Figma, high-fidelity mockups, interactive prototypes)
- Design process & workflow (discovery → ideation → high-fidelity → developer handoff)

**When to Use:**
- Creating high-fidelity, production-ready mockups
- Building design systems with component libraries
- Designing reusable UI components
- Ensuring accessibility compliance (WCAG 2.1 AA)
- Designing responsive layouts
- Improving visual hierarchy, spacing, and typography
- Conducting design critiques

**Related:** Product Manager, Product & Growth Lead 0→1, UX Site Reviewer

---

### Product Operations

**Location:** `agents/product-operations/`

**Purpose:** Expert in growth experiments, A/B testing, analytics, launch execution, metrics dashboards, and data-driven product optimization.

**Key Capabilities:**
- Growth experiments & A/B testing (ICE framework, hypothesis design, statistical significance)
- Analytics & event tracking (event tracking plans, analytics tools: PostHog, Mixpanel)
- KPIs & metrics dashboards (AARRR/Pirate Metrics, SaaS/E-Commerce/Consumer App KPIs)
- Funnel analysis (identify drop-offs, optimize bottlenecks)
- Launch execution & GTM planning (go-to-market plans, release notes, onboarding emails)
- Cohort analysis & retention (retention cohorts, segmentation)
- North Star Metric definition

**When to Use:**
- Designing A/B tests to improve metrics
- Creating event tracking plans for new features
- Defining KPI dashboards
- Analyzing funnels to identify drop-off points
- Planning feature launches (GTM plan, channels, messaging)
- Writing release notes and onboarding emails
- Analyzing experiment results

**Related:** Product Manager, Product & Growth Lead 0→1, Data Analytics Engineer

---

### Product & Growth Lead 0→1

**Location:** `agents/product-growth-lead-0to1/`

**Purpose:** Founding Product & Growth Lead combining PM, Ops, and Growth to prioritize MVPs, plan weekly releases, set up analytics, run experiments, and create PRDs, Tech Specs, wireframes, user flows.

**Key Capabilities:**
- MVP planning and prioritization (smallest shippable work)
- Weekly ship plans and rapid iteration
- Analytics setup (activation, retention, revenue metrics)
- Growth experiments (ICE framework)
- Visual artifacts (lo-fi wireframes, user flows, sitemaps, Mermaid diagrams)
- Launch/GTM assets and release notes
- One metric that matters (focus and clarity)

**When to Use:**
- Weeks 1-12 (0→1 MVP stage)
- Tiny teams (<5 people) shipping weekly
- Fast MVP execution with lo-fi artifacts
- Need to ship quickly and learn fast

**When NOT to Use:**
- Deep technical architecture (use Technical Architect)
- Polished visual design (use UX/UI Designer)
- Mature products or large teams

**Related:** Product Manager, Product Operations, Technical Architect, UX/UI Designer

---

## Development Agents

### React Stack Reviewer

**Location:** `agents/react-stack-reviewer/`

**Purpose:** Expert in React, TypeScript, Next.js, Tailwind CSS code review and best practices.

**When to Use:**
- Reviewing React component code
- Ensuring TypeScript type safety
- Optimizing performance (React.memo, useMemo, useCallback)
- Reviewing Next.js routing and data fetching
- Tailwind CSS best practices

---

### iOS Swift Developer

**Location:** `agents/ios-swift-developer/`

**Purpose:** Expert iOS developer with Swift, SwiftUI, UIKit expertise.

**When to Use:**
- Building iOS applications
- SwiftUI/UIKit development
- iOS best practices and design patterns
- App Store submission guidance

---

### Swift Code Reviewer

**Location:** `agents/swift-code-reviewer/`

**Purpose:** Expert in Swift code review, best practices, and optimization.

**When to Use:**
- Reviewing Swift code for quality and best practices
- Identifying performance improvements
- Ensuring Swift idioms and conventions

---

### Code Reviewer

**Location:** `agents/code-reviewer/`

**Purpose:** General-purpose code reviewer for multiple languages.

**When to Use:**
- Reviewing code in languages not covered by specialized reviewers
- General code quality and best practices

---

### Test Generator

**Location:** `agents/test-generator/`

**Purpose:** Generates unit tests, integration tests, and E2E tests.

**When to Use:**
- Creating comprehensive test suites
- Writing unit tests for new features
- Generating integration and E2E tests

---

### Debug Assistant

**Location:** `agents/debug-assistant/`

**Purpose:** Helps debug errors, analyze stack traces, and find root causes.

**When to Use:**
- Debugging errors and exceptions
- Analyzing stack traces
- Finding root causes of bugs

---

### PR Prep

**Location:** `agents/pr-prep/`

**Purpose:** Prepares pull requests with descriptions, summaries, and checklists.

**When to Use:**
- Creating pull request descriptions
- Generating PR summaries for reviewers
- Ensuring PR best practices

---

## Design & UX Agents

### UX Site Reviewer

**Location:** `agents/ux-site-reviewer/`

**Purpose:** Audits websites for UX, accessibility, and usability issues using Playwright.

**When to Use:**
- Conducting UX audits of existing websites
- Identifying accessibility issues
- Improving user experience

---

### Design Review Specialist

**Location:** `agents/design-review-specialist/`

**Purpose:** Reviews design work for quality, consistency, and best practices.

**When to Use:**
- Reviewing design mockups
- Ensuring design consistency
- Providing design feedback

---

## Data & Analytics Agents

### Data Analytics Engineer

**Location:** `agents/data-analytics-engineer/`

**Purpose:** Full-stack BI specialist for data engineering, web development, visualization, and HR analytics. Goes from raw data → API → interactive dashboard → actionable insights.

**Key Capabilities:**
- Data pipeline engineering (ETL/ELT, data quality, PII compliance)
- Backend API development (Flask, FastAPI, Node.js)
- Data visualization & frontend (Chart.js, D3.js, Plotly, responsive dashboards)
- Analytics & business intelligence (HR metrics: headcount, turnover, tenure)
- Report generation & export (Excel, CSV, PDF)

**When to Use:**
- Building end-to-end BI solutions
- Creating data pipelines for analytics
- Developing backend APIs for data retrieval
- Building interactive dashboards for executives
- Processing HR/workforce data with complex metrics

**Related:** Technical Architect, Product Operations

---

### Supabase Dev Admin

**Location:** `agents/supabase-dev-admin/`

**Purpose:** Expert in Supabase for backend development and database management.

**When to Use:**
- Building with Supabase
- PostgreSQL database design
- Real-time features and authentication

---

## Automation Skills

### Recruiting Tracker

**Location:** `skills/recruiting-tracker/`

**Purpose:** Unified recruiting management system for tracking candidates, positions, and hiring pipelines.

**When to Use:**
- Tracking recruiting pipelines
- Managing candidate information
- Reporting on hiring metrics

---

## Writing & Documentation Skills

### How-to Guide Writer

**Location:** `skills/how-to-guide-writer.skill/`

**Purpose:** Creates clear, step-by-step how-to guides for end users.

**When to Use:**
- Writing user documentation
- Creating tutorials and guides
- Explaining complex processes simply

---

### Job Aid Writer

**Location:** `skills/job-aid-writer/`

**Purpose:** Creates quick-reference job aids, checklists, flowcharts, decision trees, and visual reference materials for point-of-need performance support.

**What It Does:**
- Quick reference guides and cheat sheets
- Process flowcharts and workflow diagrams
- Decision trees and decision support tools
- Checklists for task completion
- Comparison tables and reference cards
- One-page desktop references

**When to Use:**
- Employees need just-in-time guidance while performing tasks
- Creating visual, scannable one-page references
- Building decision support tools (which leave type to use, which form to complete)
- Providing quick lookup guides for complex processes

**How It Differs:**
- **Job Aids:** Quick reference at point of need (1-2 pages, visual, scannable)
- **SOPs:** Formal compliance documentation (3-10 pages, comprehensive)
- **How-To Guides:** Educational training materials (5-20 pages, detailed)

---

### SOP Writer

**Location:** `skills/sop-writer/`

**Purpose:** Writes Standard Operating Procedures for internal processes.

**When to Use:**
- Documenting internal processes
- Creating operational procedures
- Standardizing workflows

---

### Recruiting Materials

**Location:** `skills/recruiting-materials/`

**Purpose:** Creates recruiting materials like job descriptions, offer letters, and email templates.

**When to Use:**
- Writing job descriptions
- Creating offer letters
- Generating recruiting email templates

---

### Job Description Formatter

**Location:** `skills/job-description-formatter/`

**Purpose:** Formats job descriptions with templates and compliance guidelines.

**When to Use:**
- Formatting job postings
- Ensuring compliance with employment laws
- Standardizing job description format

---

## HR & Recruiting Skills

### Oracle HCM Solution Architect

**Location:** `skills/oracle-hcm-solution-architect/`

**Purpose:** Expert in Oracle HCM Cloud configuration and integration.

**When to Use:**
- Configuring Oracle HCM Cloud
- Integrating with Oracle systems
- Troubleshooting Oracle HCM issues

---

## Design & Brand Skills

### Brand Guidelines

**Location:** `skills/brand-guidelines/`

**Purpose:** Creates and maintains brand guidelines (colors, typography, logo usage).

**When to Use:**
- Establishing brand identity
- Documenting visual standards
- Ensuring brand consistency

---

### Canvas Design

**Location:** `skills/canvas-design/`

**Purpose:** Creates visual designs and graphics.

**When to Use:**
- Generating visual assets
- Creating graphics and illustrations
- Designing marketing materials

---

### Excel Design Guru

**Location:** `skills/excel-design-guru/`

**Purpose:** Creates professionally formatted Excel reports and templates.

**When to Use:**
- Designing Excel templates
- Formatting complex spreadsheets
- Creating dashboard-style reports in Excel

---

## Utility Skills

### Lyra Prompt Optimizer

**Location:** `skills/lyra-prompt-optimizer/`

**Purpose:** Transform vague AI requests into precision-engineered prompts that deliver professional-grade HR results on the first try using the 4-D methodology (Deconstruct → Diagnose → Develop → Deliver).

**What It Does:**
- Optimizes prompts for SOPs, job descriptions, and HR documents
- Uses 4-D methodology: Deconstruct → Diagnose → Develop → Deliver
- Eliminates trial-and-error by engineering prompts with precision from the start
- Specializes in compliance-ready HR documentation
- Provides two optimization modes: BASIC (quick fix) and DETAIL (comprehensive)

**When to Use:**
- Creating Standard Operating Procedures and policy documents
- Drafting job descriptions and recruitment materials
- Generating workforce analytics reports
- Writing employee communications
- Building training materials and user guides
- Developing performance review templates
- Creating compliance audit checklists
- You're not getting good results from AI and need to improve your prompt

**Key Features:**
- **BASIC Mode:** Quick prompt fix (2-3 minutes) - adds missing context, clarifies ambiguity
- **DETAIL Mode:** Comprehensive optimization (5-7 minutes) - includes examples, edge cases, validation criteria
- Built specifically for HR professionals with understanding of compliance and operational realities
- Get usable, compliance-ready output on attempt #1 instead of attempt #5

---

### Skill Creator

**Location:** `skills/skill-creator/`

**Purpose:** Helps create new skills for the repository.

**When to Use:**
- Building new automation skills
- Understanding skill structure
- Following skill development best practices

---

### Shipping Coach

**Location:** `skills/shipping-coach/`

**Purpose:** Helps teams ship features faster and more reliably.

**When to Use:**
- Improving shipping velocity
- Establishing release processes
- Reducing deployment friction

---

## How to Use This Catalog

### For Agents

**Invoke via Task Tool:**
```
I need help with [task description].

Launch a [Agent Name] agent using the prompt from:
agents/[agent-name]/AGENT.md
```

**Direct Reference:**
```
Please read and use the [Agent Name] agent from:
agents/[agent-name]/AGENT.md

Help me with [specific task].
```

### For Skills

Skills are symlinked to `~/.claude/skills/` and auto-loaded by Claude Desktop and Claude Code.

**To sync skills:**
```bash
./scripts/sync-skills.sh
```

**To invoke a skill:**
Simply place relevant files in `data/inputs/[skill-name]/` and ask Claude to process them using the skill.

---

## Repository Structure

```
skills-agents/
├── agents/              # Reusable AI agents (manual invoke)
│   ├── product-manager/
│   ├── technical-architect/
│   ├── ux-ui-designer/
│   ├── product-operations/
│   ├── product-growth-lead-0to1/
│   ├── data-analytics-engineer/
│   └── [other agents]/
│
├── skills/              # Automation workflows (auto-loaded)
│   ├── recruiting-tracker/
│   ├── how-to-guide-writer.skill/
│   └── [other skills]/
│
├── data/
│   ├── inputs/          # Input files for skills
│   └── outputs/         # Generated reports
│
└── scripts/
    └── sync-skills.sh   # Sync skills to ~/.claude/skills/
```

---

## Product Agent Suite (New!)

The following agents form a **complete product team** for different stages and specializations:

| Stage | Agent | Focus |
|-------|-------|-------|
| **0→1 MVP** | Product & Growth Lead 0→1 | Fast, lo-fi, weekly shipping |
| **Post-MVP** | Product Manager | Core PM: PRDs, roadmaps, prioritization |
| **Post-MVP** | Technical Architect | System design, scalability, architecture |
| **Post-MVP** | UX/UI Designer | Polished design, design systems, accessibility |
| **Ongoing** | Product Operations | Experiments, analytics, launch execution |
| **Ongoing** | Data Analytics Engineer | Full-stack BI, data → API → dashboard |

---

## Contributing

To add a new agent or skill:

1. **Create agent:** `mkdir agents/[agent-name]`, add `AGENT.md` and `README.md`
2. **Create skill:** `mkdir skills/[skill-name]`, add `SKILL.md`, processing scripts, `README.md`
3. **Sync skills:** `./scripts/sync-skills.sh`
4. **Update this catalog:** Add entry to appropriate section
5. **Commit and push:** Version control your changes

---

## Version History

- **2025-11-05:** Added Product Manager, Technical Architect, UX/UI Designer, Product Operations agents
- **2025-11-05:** Added Data Analytics Engineer agent
- **2025-10:** Initial catalog with Product & Growth Lead 0→1, React Stack Reviewer, Position Review Skill

---

**Questions?**
- See individual agent/skill README files for detailed documentation
- See [CLAUDE.md](./CLAUDE.md) for repository structure and workflow
- See [agents/README.md](./agents/README.md) for agent usage guidance
