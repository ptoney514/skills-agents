# Product Operations

Expert in growth experiments, A/B testing, analytics (event tracking, KPIs, funnels), launch execution (GTM plans, release notes), metrics dashboards, and data-driven product optimization.

## Overview

This agent provides **Product Operations expertise** focused on growth experiments, analytics, and launch execution. While Product Managers define strategy and features, Product Operations focuses on **execution and measurement**: running experiments, tracking metrics, optimizing funnels, and launching features successfully.

## Core Capabilities

### Growth Experiments & A/B Testing
- **ICE Framework:** Impact × Confidence × Ease for prioritizing experiments
- **Experiment design:** Hypothesis, metrics, variants, success criteria, rollback plan
- **A/B test best practices:** One variable at a time, sufficient sample size, statistical significance (95%), segment results
- **Common experiments:** Signup flow, onboarding, pricing, feature adoption, retention

### Analytics & Event Tracking
- **Event tracking plans:** Event name, trigger, properties, owner
- **Event naming:** `snake_case`, past tense verbs, specific and descriptive
- **Analytics tools:** PostHog, Mixpanel, Amplitude, Google Analytics 4, Segment
- **Implementation:** Work with engineering to instrument events, validate accuracy

### KPIs & Metrics Dashboards
- **AARRR (Pirate Metrics):** Acquisition, Activation, Retention, Revenue, Referral
- **SaaS KPIs:** Signups, D7/D30 retention, MRR, ARR, ARPU, LTV:CAC, churn rate
- **E-Commerce:** Visits, conversions, AOV, repeat purchase rate, GMV
- **Consumer App:** Installs, DAU/MAU, retention cohorts, ARPU, viral coefficient
- **North Star Metric:** One metric that captures core product value

### Funnel Analysis
- Map user journey (Landing → Signup → Activation → Retention)
- Identify drop-off points (where users leave)
- Hypothesize why users drop off
- Design experiments to optimize bottlenecks
- Measure impact and iterate

### Launch Execution & GTM Planning
- **GTM plan:** Goals, audience, value prop, channels, messaging, timeline
- **Launch channels:** Email, in-app, blog, social, Product Hunt, press
- **Release notes:** New features, improvements, bug fixes, coming soon
- **Onboarding emails:** Welcome (Day 0), activation nudge (Day 3), value reinforcement (Day 7)

### Cohort Analysis & Retention
- Retention cohort tables (D1/D7/D14/D30)
- Segment by acquisition source, user type, onboarding path, geography
- Track trends over time (improving, flat, declining)

## When to Use This Agent

✅ **Use this agent when:**
- Designing A/B tests to improve metrics (signup conversion, retention, revenue)
- Creating event tracking plans for new features
- Defining KPI dashboards (acquisition → activation → retention → revenue)
- Analyzing funnels to identify drop-off points
- Planning feature launches (GTM plan, channels, messaging)
- Writing release notes and onboarding emails
- Analyzing experiment results and recommending next steps
- Setting up cohort analysis and retention tracking

❌ **Don't use this agent for:**
- Product strategy and roadmaps (use **Product Manager**)
- Technical architecture (use **Technical Architect**)
- Visual design (use **UX/UI Designer**)
- 0→1 MVP planning (use **Product & Growth Lead 0→1** which combines PM + Ops)

## Example Use Cases

### 1. Design A/B Test for Signup Conversion

**Task:** "Our signup conversion is 12%. Design an experiment to improve it."

**Output includes:**
- **Hypothesis:** Reducing form fields from 8 to 4 will increase signup completion because users abandon long forms
- **Metric:** Signup completion rate (baseline: 12%, target: 15%, +3pp)
- **Variants:** Control (8 fields), Variant (4 fields: email, password, name, company)
- **ICE Score:** Impact 8/10, Confidence 80%, Ease 8/10 → Score 5.12 (high priority)
- **Success criteria:** 95% confidence, 2-week duration, 1000+ users per variant
- **Implementation:** Feature flag `experiment_simplified_signup`, 50/50 split
- **Analysis plan:** Segment by source (organic vs. paid), device (mobile vs. desktop), watch for novelty effects
- **Rollback plan:** Toggle flag to 0% if completion rate drops
- **Timeline:** Design (Week 1), Dev (Week 2), Launch (Week 3), Results (Week 5)

### 2. Create Event Tracking Plan for Team Dashboards

**Task:** "We're launching Team Dashboards. Create an event tracking plan."

**Output includes:**

| Event Name | Trigger | Properties | Owner |
|------------|---------|------------|-------|
| `dashboard_viewed` | User opens Team Dashboard | `user_id`, `team_id`, `timestamp`, `screen_size` | Product |
| `dashboard_filtered` | User applies filters | `user_id`, `filter_type` (date/member), `filter_value` | Product |
| `activity_drilled_down` | User clicks activity for details | `user_id`, `activity_id`, `activity_type` | Product |
| `dashboard_shared` | User shares dashboard link | `user_id`, `recipient_email`, `share_method` (email/link) | Growth |
| `dashboard_exported` | User exports dashboard data | `user_id`, `export_format` (CSV/PDF), `date_range` | Product |

**Implementation notes:**
- Use PostHog for event tracking
- Add events to codebase (work with engineering)
- Validate events firing correctly in PostHog debugger
- Create dashboard in PostHog: Total views, unique users, filters applied, shares sent

### 3. GTM Plan for iOS App Launch

**Task:** "We're launching our iOS app in Q2. Create a GTM plan."

**Output includes:**
- **Launch goals:** 5K downloads in first month, 40% D7 retention, 4.5★ App Store rating
- **Target audience:**
  - Primary: Existing web users (10K) who requested mobile app
  - Secondary: New mobile-first users discovering via App Store
- **Value proposition:** "Access [Product] on the go. Sync seamlessly with web. Never miss an update."
- **Launch channels:**
  - Email: Announce to 10K existing users (Monday 9am)
  - In-App (Web): Banner "Now available on iOS" (Monday 9am)
  - Blog: "Introducing [Product] for iOS" with video demo (Monday 12pm)
  - Social: Twitter, LinkedIn posts with App Store link (Monday 1pm)
  - Product Hunt: Submit Wednesday for max visibility
  - Press: Pitch to TechCrunch, The Verge (if newsworthy milestone)
- **Messaging:**
  - Email subject: "Introducing [Product] for iOS 📱"
  - Social: "We just launched [Product] for iOS! Download now and take your workflow mobile. [Link] [Video Demo]"
  - App Store description: [Optimized for ASO]
- **Timeline:**
  - T-4 weeks: Beta via TestFlight (100 early adopters)
  - T-2 weeks: Gather feedback, fix critical bugs
  - T-1 week: Submit to App Store for review
  - T-0 (Launch): Announce via all channels
  - T+1 week: Analyze metrics, iterate based on feedback
- **Success metrics:**
  - Downloads: 5K in first month
  - Activation: 3K users create account (60% activation rate)
  - Retention: 40% D7 retention (return to app within 7 days)
  - Rating: 4.5★ average on App Store
- **Rollback plan:** Feature flags for new iOS-only features, can disable remotely if critical bugs

## ICE Framework Example

```
Experiment: Add Apple Sign-In

Impact: 8/10 (significantly reduces signup friction, industry standard)
Confidence: 70% (proven pattern, but uncertain for our specific audience)
Ease: 6/10 (requires Apple developer setup, OAuth integration, ~2 weeks)

ICE Score: (8 × 0.7 × 6) / 10 = 3.36

Interpretation: Medium-high priority. Good impact and ease, moderate confidence.
```

## AARRR (Pirate Metrics) Framework

```
Acquisition: How users find you
- Metrics: Website visits, signups, app installs
- Channels: Organic, paid, referral, direct

Activation: First valuable experience
- Metrics: Onboarding completion, first project created, "aha moment"
- Goal: Get users to experience core value quickly

Retention: Users come back
- Metrics: DAU, WAU, MAU, D1/D7/D30 retention cohorts
- Goal: Build habit, deliver ongoing value

Revenue: Monetization
- Metrics: MRR, ARR, ARPU, LTV, conversion to paid
- Goal: Sustainable business model

Referral: Users bring others
- Metrics: Viral coefficient, NPS, invites sent, share rate
- Goal: Organic growth engine
```

## Retention Cohort Table Example

```
Cohort      Day 1   Day 7   Day 14  Day 30
Jan 1       100%     45%     32%     25%
Jan 8       100%     48%     35%     28%
Jan 15      100%     52%     38%     30%
Jan 22      100%     55%     40%     32%

Trend: Improving! D7 retention up from 45% → 55% over 3 weeks.
Likely due to new onboarding flow launched Jan 10.
```

## Best Practices

### Data-Driven Decision Making
- Always define success metrics before starting work
- Use quantitative (analytics) and qualitative (user feedback) data
- Wait for statistical significance (95% confidence)
- Segment data to find patterns (new vs. returning, mobile vs. desktop)

### Experiment Discipline
- Run one experiment at a time (isolate variables)
- Calculate required sample size before launching
- Don't peek early (wait for significance)
- Document all experiments (even failures teach us)
- Kill experiments that hurt metrics quickly

### Launch Execution
- Plan launches like campaigns (GTM plan, timeline, channels)
- Monitor metrics in real-time on launch day
- Respond quickly to feedback and bugs
- Iterate based on learnings (1-week post-launch review)

### Communication
- Share metrics dashboards with whole team (transparency)
- Celebrate wins (retention improved!) and learn from failures
- Translate data into stories ("Users drop off at signup because...")
- Involve team in experiment ideas (not just top-down)

## How to Invoke

**In Claude Code:**
```
I need to design an A/B test to improve our signup conversion rate.

Launch a Product Operations agent using the prompt from:
agents/product-operations/AGENT.md
```

**Direct reference:**
```
Please read agents/product-operations/AGENT.md and create an event
tracking plan for our new dashboard feature.
```

## Configuration

- **Model:** Sonnet (recommended for balanced speed/quality)
  - Use Opus for complex experiment designs or multi-variate tests
  - Use Haiku for simple event tracking plans or release notes
- **Thoroughness:** Comprehensive (default), or specify "lean" for quick experiments
- **Output:** Markdown tables (event plans), experiment briefs, GTM timelines

## Related Agents

**Use together with:**
- **Product Manager** - Defines product strategy and features to launch
- **Product & Growth Lead 0→1** - Combines PM + Ops for MVP speed (0→1 stage)
- **Data Analytics Engineer** - For data pipeline and BI infrastructure
- **UX/UI Designer** - For designing experiment variants (UI changes)

**Product Operations role:**
- Receives features from Product Manager → Designs launch plan → Tracks success metrics
- Designs experiments → Measures impact → Informs Product Manager roadmap

## Tips for Best Results

1. **Provide context:** Current metrics, baseline performance, business goals
2. **Share constraints:** Timeline, engineering resources, technical limitations
3. **Define success:** What does "good" look like? (Target metrics)
4. **Include data:** User feedback, analytics, past experiment results
5. **Iterate:** Start with simple experiments, compound learnings

## Key Concepts

- **ICE Framework:** Impact × Confidence × Ease (prioritize experiments)
- **AARRR:** Acquisition, Activation, Retention, Revenue, Referral (Pirate Metrics)
- **North Star Metric:** One metric that captures core product value
- **Statistical Significance:** 95% confidence (p < 0.05)
- **Cohort Analysis:** Group users by signup date, track retention over time
- **Funnel Optimization:** Identify drop-offs, hypothesize, experiment, measure

## Version History

- **1.0.0** (2025-11-05) - Initial version with experiments, analytics, launch execution

---

**Questions?**
- See [AGENT.md](./AGENT.md) for complete agent instructions
- See [agents/README.md](../README.md) for general agent guidance
