# Skills & Agents Catalog

A comprehensive reference of all skills and agents available in this repository.

**Last Updated:** 2025-11-14

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
| **Create pixel-perfect design systems** | [Pixel-Perfect Designer](#pixel-perfect-designer) |
| **Extract CSS into style guides** | [CSS Style Extractor](#css-style-extractor) |
| **Run A/B tests and analytics** | [Product Operations](#product-operations) |
| **Fast MVP planning (0→1)** | [Product & Growth Lead 0→1](#product--growth-lead-01) |
| **Full-stack BI solution** | [Data Analytics Engineer](#data-analytics-engineer) |
| **Review React code** | [React Stack Reviewer](#react-stack-reviewer) |
| **Audit UX design** | [UX Site Reviewer](#ux-site-reviewer) |
| **Write how-to guides** | [How-to Guide Writer](#how-to-guide-writer) |
| **Create quick-reference job aids** | [Job Aid Writer](#job-aid-writer) |
| **Optimize AI prompts for HR** | [Lyra Prompt Optimizer](#lyra-prompt-optimizer) |
| **Track recruiting pipelines** | [Recruiting Tracker](#recruiting-tracker) |
| **Manage HR sprint tracking** | [HR Project Manager](#hr-project-manager) |

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
- **GitHub Issues & Projects integration** (work tracking, user stories, roadmaps, sprints)

**When to Use:**
- Writing comprehensive PRDs for complex features
- Prioritizing backlog using frameworks (RICE, Value vs. Effort)
- Creating quarterly or annual product roadmaps
- Conducting user research and defining personas
- Managing stakeholder alignment
- Defining product strategy and vision

**GitHub Projects Support:**
Agent proactively recommends GitHub Issues and Projects for tracking work. Provides:
- Issue templates for user stories (acceptance criteria, labels, priorities)
- Project board configurations (Backlog, Sprint, Roadmap, Release views)
- Milestone tracking for releases
- Custom fields (Priority, RICE score, Effort, Quarter)
- Alternative markdown format for Jira/Linear/Asana teams

**How to Use:**
```
Launch the Product Manager agent from:
agents/product-manager/AGENT.md

Help me create a PRD and roadmap for [feature name]
```

The agent will ask:
> "How would you like to track this work? I recommend using GitHub Issues and Projects if your team is already on GitHub..."

**Choose GitHub:** Get issue templates, project setup, automation workflows
**Choose another tool:** Get markdown format for Jira/Linear/Asana

**Related:** Product Operations, Technical Architect, Pixel-Perfect Designer

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

### Pixel-Perfect Designer

**Location:** `agents/pixel-perfect-designer/`

**Purpose:** Expert in Flow Engineering methodology for creating pixel-perfect, personalized design systems. Achieves high-fidelity UI design through structured, iterative workflows that move beyond generic AI output to truly on-brand, professional results.

**Key Capabilities:**
- **Flow Engineering Methodology** (4-step process: Layout → Scene → Animation → Scaling)
- **Lo-Fi Mode:** ASCII wireframes for rapid layout iteration
- **Hi-Fi Mode:** Complete design systems with comprehensive style guides
- CSS extraction and style analysis from reference websites
- Design system documentation (color, typography, spacing, shadows, animations)
- Component scaling and consistency enforcement
- Framework-agnostic output (React, iOS, print wireframes, static sites)
- Animation/micro-interaction specifications
- Production-ready component generation

**When to Use:**
- Building new design systems from scratch
- Replicating existing website aesthetics (100% fidelity)
- Creating comprehensive style guides
- Ensuring design consistency across large projects
- Rapid wireframe iteration
- Extracting and systematizing design patterns
- Need pixel-perfect replication (not generic AI UI)

**Workflow Modes:**
1. **Lo-Fi Wireframe:** Quick ASCII layouts for alignment and iteration
2. **Hi-Fi from Reference:** Extract CSS from existing site → Generate style guide → Apply to new project
3. **Custom Design System:** Build unique brand system from scratch with guided iteration

**What Makes It Different:**
- Achieves 100% fidelity (vs. typical 60-70% from screenshots)
- Systematic co-creation process ensures quality before scaling
- Generates reusable templates (style guides, animation specs, component manifests)
- Works with companion `css-style-extractor` skill for high-fidelity input

**Related:** Product Manager, Product & Growth Lead 0→1, UX Site Reviewer, CSS Style Extractor (skill)

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
- **GitHub Issues & Projects integration** (launch tracking, experiment management, analytics coordination)

**When to Use:**
- Designing A/B tests to improve metrics
- Creating event tracking plans for new features
- Defining KPI dashboards
- Analyzing funnels to identify drop-off points
- Planning feature launches (GTM plan, channels, messaging)
- Writing release notes and onboarding emails
- Analyzing experiment results

**GitHub Projects Support:**
Agent proactively recommends GitHub Issues and Projects for tracking launches and experiments. Provides:
- Launch task issues (Pre-launch, Day-of, Post-launch phases)
- Experiment tracking issues (hypothesis, ICE score, results)
- Launch Coordination Board (Timeline, Kanban, Checklist views)
- Growth Experiments Board (Active, Backlog, Results Archive)
- Integration with analytics dashboards (PostHog, Mixpanel links)
- Alternative markdown checklists for Jira/Linear/Asana teams

**How to Use:**
```
Launch the Product Operations agent from:
agents/product-operations/AGENT.md

Help me plan the launch for [feature name] and set up experiment tracking
```

The agent will ask:
> "How would you like to track this launch/experiment? I recommend using GitHub Issues and Projects if your team is on GitHub..."

**Choose GitHub:** Get launch checklists, experiment issues, project boards, analytics integration
**Choose another tool:** Get markdown checklists and experiment tracker format

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
- **GitHub Issues & Projects integration** (weekly ship plans, MVP tracking, velocity monitoring)

**When to Use:**
- Weeks 1-12 (0→1 MVP stage)
- Tiny teams (<5 people) shipping weekly
- Fast MVP execution with lo-fi artifacts
- Need to ship quickly and learn fast

**When NOT to Use:**
- Deep technical architecture (use Technical Architect)
- Polished visual design (use Pixel-Perfect Designer)
- Mature products or large teams

**GitHub Projects Support:**
Agent proactively recommends GitHub Issues and Projects for weekly ship plans. Provides:
- Weekly task issues (5-7 tasks/week format)
- Simple project board ("This Week" Kanban + Velocity Tracker)
- Milestone tracking for MVP launch
- Weekly rituals integration (Mon planning, Fri retro)
- Emphasis on minimal overhead (ship > process)
- Alternative markdown ship plans for lightweight tracking

**How to Use:**
```
Launch the Product & Growth Lead 0→1 agent from:
agents/product-growth-lead-0to1/AGENT.md

Help me plan Week [N] ship plan for [MVP feature]
```

The agent will ask:
> "How would you like to track this week's ship plan? I recommend using GitHub Issues and Projects for fast-moving 0→1 work..."

**Choose GitHub:** Get 5-7 weekly task issues, "This Week" board, velocity tracking
**Choose markdown:** Get lightweight ship plan checklist for Notion/Google Docs

**Related:** Product Manager, Product Operations, Technical Architect, Pixel-Perfect Designer

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

### HR Project Manager

**Location:** `skills/hr-project-manager/`

**Purpose:** Automate HR Operations sprint tracking through Excel spreadsheet manipulation and Linear issue synchronization. Maintains Excel as single source of truth while providing enhanced project management through Linear integration.

**What It Does:**
- Excel tracker manipulation (read, update, save dated copies)
- Linear issue creation and sync (Excel → Linear)
- Sprint report generation (summaries, emails, metrics)
- Data validation (integrity checks, dependency parsing)
- Task breakdown suggestions (weekly chunks for large projects)

**When to Use:**
- Managing weekly HR Operations sprints
- Tracking projects in Excel with Linear integration
- Generating sprint confirmation emails
- Breaking down large tasks into weekly deliverables
- Validating tracker data integrity
- Automating sprint workflow (meeting updates, Linear sync, reporting)

**Key Features:**
- **Excel as Source of Truth:** All updates happen in Excel first
- **Weekly Sprint Cadence:** Thursday meetings with 7-day lookahead
- **Linear Integration:** Optional sync for enhanced visibility
- **Sprint Reports:** Automated summaries with completion rates
- **Blocker Detection:** Identifies dependencies and blocked items

**Workflow:**
1. **Wednesday:** Review sprint items for tomorrow's meeting
2. **Thursday (Meeting):** Update status, % done, notes in Excel
3. **Thursday (Post-Meeting):** Sync to Linear, generate sprint email
4. **Friday:** Progress check on in-progress items

**Related:** Recruiting Tracker (similar tracking pattern), Excel Design Guru, Product Operations (sprint management)

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

### CSS Style Extractor

**Location:** `skills/css-style-extractor/`

**Purpose:** Extract and parse CSS stylesheets into standardized, comprehensive style guide documentation. Transforms raw CSS from websites or design systems into structured markdown guides with color palettes, typography, spacing, shadows, and component styles.

**What It Does:**
- Extract CSS variables and hard-coded values from stylesheets
- Categorize colors into primary, secondary, neutrals, semantic (success/error/warning)
- Document typography systems (fonts, sizes, weights, line heights)
- Identify spacing scales and patterns
- Extract shadow/elevation systems and border radius scales
- Parse component styles (buttons, inputs, cards, navigation)
- Document animations and transitions
- Generate standardized style guide markdown

**When to Use:**
- Extracting design systems from reference website CSS
- Converting raw stylesheets into design documentation
- Creating style guides from existing codebases
- Documenting design tokens from CSS variables
- Preparing high-fidelity context for pixel-perfect-designer agent
- Batch processing multiple CSS files for comparison
- Analyzing competitor design patterns

**Workflow:**
1. Extract CSS from website (Inspect → Copy styles)
2. Save to `data/inputs/css-extraction/[source]__[date].css`
3. Run processing script: `python extract_css_styles.py [input_file]`
4. Review generated style guide in `data/outputs/css-extraction/`
5. Use with pixel-perfect-designer agent for high-fidelity replication

**Output:**
- Comprehensive markdown style guide with organized sections
- All CSS variables documented
- Color palette organized by category
- Typography system (fonts, scale, weights, line heights)
- Spacing, shadows, border radius scales
- Component style examples with code snippets

**Integration:**
- **Companion to pixel-perfect-designer agent**
- Provides high-fidelity CSS input (vs. 60-70% accuracy from screenshots)
- Enables 100% fidelity design replication
- Systematic extraction ensures no details are lost

**Related:** Pixel-Perfect Designer (agent), Brand Guidelines

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
| **Post-MVP** | Pixel-Perfect Designer | Design systems, pixel-perfect UI, Flow Engineering |
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

- **2025-11-18:** Added HR Project Manager skill (Excel tracker manipulation, Linear sync, sprint management)
- **2025-11-14:** Added GitHub Issues & Projects integration to Product Manager, Product Operations, and Product & Growth Lead 0→1 agents
- **2025-11-14:** Added "How to Use" invocation examples to all product management agents
- **2025-11-14:** Added Pixel-Perfect Designer agent (replaces UX/UI Designer and Canvas Design)
- **2025-11-14:** Added CSS Style Extractor skill (companion to Pixel-Perfect Designer)
- **2025-11-14:** Archived UX/UI Designer agent and Canvas Design skill
- **2025-11-05:** Added Product Manager, Technical Architect, UX/UI Designer, Product Operations agents
- **2025-11-05:** Added Data Analytics Engineer agent
- **2025-10:** Initial catalog with Product & Growth Lead 0→1, React Stack Reviewer, Position Review Skill

---

**Questions?**
- See individual agent/skill README files for detailed documentation
- See [CLAUDE.md](./CLAUDE.md) for repository structure and workflow
- See [agents/README.md](./agents/README.md) for agent usage guidance
