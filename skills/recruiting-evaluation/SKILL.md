---
name: recruiting-evaluation
description: Evaluate job candidates using a two-stage framework - Stage 1 (Resume Screening) determines who to interview, Stage 2 (Post-Interview Evaluation) determines who gets the job offer. Use when screening resumes, making interview decisions, or conducting final hiring evaluations with interview feedback weighted at 50%.
---

# Recruiting Evaluation Skill

A comprehensive two-stage evaluation framework that separates initial resume screening from post-interview assessment, with heavy emphasis on human interviewer feedback.

## Two-Stage Evaluation Framework

This skill uses a two-stage process to evaluate candidates:

### Stage 1: Resume Screening (Initial Filter)
- **Purpose:** Quickly identify which candidates to phone screen
- **Input:** Resume, cover letter, application materials
- **Scoring:** Qualifications (40%) + Experience (40%) + Risk Flags (20%)
- **Output:** 0-100 score + Text recommendation + Candidate-specific verification questions
- **Decision Thresholds:**
  - **70-100: PHONE SCREEN** - Conduct 30-min phone screen (use recruiting-materials skill to generate script)
  - **0-69: DECLINE** - Send professional decline communication

### Stage 2: Post-Interview Evaluation (Final Decision)
- **Purpose:** Determine who receives the job offer
- **Input:** Resume score + Interview ratings + Reference checks + Manager observations
- **Scoring:** Resume (25%) + Interview (50%) + References (25%)
- **Output:** Final hire/no-hire recommendation with detailed comparison
- **Key Feature:** Human interviewer feedback is weighted at 50% - the most important factor

**Critical Philosophy:** A strong resume gets you to the phone screen. Passing the phone screen gets you to the interview. Your performance in the interview determines if you get the job. Manager/interviewer observations override resume credentials.

---

## Stage 1: Resume Screening

When a user provides candidate resume(s) and job description, perform initial screening.

### Scoring Formula

**Total Score = (Qualifications × 0.40) + (Experience × 0.40) + (Risk Flags × 0.20)**

### Evaluation Criteria

#### Qualifications (40% weight)

Score the candidate's educational background and credentials:

- Required degree(s) obtained
- Certifications/licenses current and relevant
- Educational background alignment with role
- Professional credentials and memberships

**Scoring Guide:**
- **90-100:** Exceeds all qualifications, advanced credentials
- **80-89:** Meets all requirements, some exceed expectations
- **70-79:** Meets most requirements, minor gaps exist
- **60-69:** Meets minimum requirements, notable gaps
- **Below 60:** Missing critical qualifications

#### Experience (40% weight)

Evaluate relevant work history and career progression:

- Years in relevant roles (matches requirement range)
- Career progression and growth trajectory
- Direct role alignment (similar responsibilities)
- Population/industry match (e.g., higher ed, healthcare, etc.)
- Recency of experience (currency of skills)

**Scoring Guide:**
- **90-100:** Perfect experience match, proven track record, exceeds requirements
- **80-89:** Strong relevant experience, clear success in similar roles
- **70-79:** Good relevant experience, some gaps or concerns
- **60-69:** Some relevant experience, notable gaps
- **Below 60:** Little to no relevant experience

#### Risk Flags (20% weight)

Assess potential concerns (score inversely - higher is better). This component has **4 sub-components, each weighted at 25%**:

**1. Employment Gaps (25% of Risk Flags)**
- Evaluate context before penalizing
- Valid reasons: caregiving, education, health, layoffs, entrepreneurship
- Focus on skills currency and ability to ramp up
- **Scoring:** 100 = no gaps, 90 = explained gaps, 70 = moderate concerns, <60 = significant unexplained gaps

**2. Job Hopping Patterns (25% of Risk Flags)**
- Frequent changes without clear progression
- Look for explanations, patterns of growth, or valid reasons
- Consider industry norms (tech vs. other sectors)
- **Scoring:** 100 = stable progression, 90 = logical moves, 70 = some concerns, <60 = concerning pattern

**3. Skill Currency (25% of Risk Flags)**
- Outdated technical or professional skills
- Continuous learning indicators
- Relevance of recent experience
- **Scoring:** 100 = current skills, 90 = mostly current, 70 = some outdated, <60 = significantly outdated

**4. Application Quality (25% of Risk Flags)** ← **NEW: Includes Cover Letter Evaluation**
- Cover letter customization and personalization
- Understanding of organization/mission
- Professional writing quality and attention to detail
- Articulation of fit for this specific role
- Addresses resume gaps or career transitions

**Application Quality Scoring:**
- **90-100:** Exceptional cover letter - Highly customized, demonstrates deep research about organization, compelling narrative about fit, excellent writing, addresses any resume gaps proactively
- **80-89:** Strong cover letter - Personalized, clear articulation of fit and interest, professional writing, shows understanding of role/organization
- **70-79:** Adequate cover letter - Generic but acceptable, basic customization, standard professional quality, or no cover letter when not required
- **60-69:** Weak - Template letter with minimal customization, poor writing quality, or missing when expected/requested
- **Below 60:** Major concerns - Unprofessional presentation, significant errors, missing when explicitly required, raises communication concerns

**Overall Risk Flags Scoring Guide:**
- **90-100:** No significant risk flags across all areas
- **80-89:** Minor concerns in 1-2 areas, easily manageable
- **70-79:** Moderate concerns, needs discussion in phone screen/interview
- **60-69:** Notable concerns in multiple areas, careful evaluation needed
- **Below 60:** High risk factors, significant concerns across multiple areas

**Note:** Cover letters can influence all three main components (Qualifications, Experience, Risk Flags) by providing context, but Application Quality provides an explicit, measurable score within Risk Flags.

### Stage 1 Output Format

Present results as:

**STAGE 1: RESUME SCREENING RESULTS**

**Candidate:** [Full Name]
**Score:** [0-100] out of 100
**Recommendation:** [PHONE SCREEN / DECLINE]

**Main Components:**

| Component | Score | Weight | Weighted Score | Notes |
|-----------|-------|--------|----------------|-------|
| Qualifications | [0-100] | 40% | [calc] | [Brief assessment] |
| Experience | [0-100] | 40% | [calc] | [Brief assessment] |
| Risk Flags | [0-100] | 20% | [calc] | See detailed breakdown below |
| **TOTAL** | | | **[Final Score]** | |

**Risk Flags Detailed Breakdown (20% of total):**

| Risk Factor | Score | Weight (of Risk Flags) | Contribution to Risk Flags | Notes |
|-------------|-------|------------------------|---------------------------|-------|
| Employment Gaps | [0-100] | 25% | [calc] | [Gap assessment] |
| Job Hopping | [0-100] | 25% | [calc] | [Pattern assessment] |
| Skill Currency | [0-100] | 25% | [calc] | [Currency assessment] |
| Application Quality | [0-100] | 25% | [calc] | Cover letter evaluation |
| **Risk Flags Total** | **[0-100]** | **100%** | | |

**Application Quality Analysis:**
- **Cover Letter Quality:** [Exceptional/Strong/Adequate/Weak/Missing]
- **Application Quality Score:** [0-100]
- **Impact on Overall Score:** This candidate's application quality [added/subtracted/had neutral effect on] their total score by approximately [X] points compared to a baseline adequate application (score 75).
- **Evidence:**
  - [Specific example 1 from cover letter - e.g., "Demonstrated deep research by referencing our recent program launch"]
  - [Specific example 2 - e.g., "Proactively addressed career gap by explaining sabbatical for professional development"]
  - [Specific example 3 - e.g., "Writing quality excellent with clear, professional communication" OR "Generic template with no personalization"]

**Score Interpretation:**
- **90-100:** PHONE SCREEN (Exceptional candidate)
- **85-89:** PHONE SCREEN (Strong candidate)
- **70-84:** PHONE SCREEN (Promising, needs verification)
- **60-69:** DECLINE (Below threshold)
- **0-59:** DECLINE (Not qualified)

**Key Strengths:**
• [Strength 1 with specific evidence]
• [Strength 2 with specific evidence]
• [Strength 3 with specific evidence]

**Key Concerns:**
• [Concern 1 requiring interview attention]
• [Concern 2 requiring verification]
• [Concern 3 or "None significant"]

**Decision: [PHONE SCREEN / DECLINE]**

**CANDIDATE-SPECIFIC VERIFICATION QUESTIONS:**
*(These questions are unique to this candidate and should be asked during phone screen to address concerns/gaps identified in Stage 1)*

1. [Question about gap/concern, if applicable]
2. [Question about specific experience validation]
3. [Question about role-critical skill demonstration]

**Next Steps:**
- **If 70+:** Use `recruiting-materials` skill to generate phone screen script (includes standard assessment questions + above verification questions)
- **If <70:** Send professional decline communication
- **After successful phone screen:** Use `recruiting-materials` skill to generate interview guide and evaluation form

---

### Cover Letter as Differentiator: Example

**Scenario:** Two candidates with nearly identical qualifications and experience, but different application quality.

**Candidate A: Sarah Johnson**
- Qualifications: 85 (Masters in relevant field, required certifications)
- Experience: 86 (5 years relevant experience, good progression)
- Risk Flags: 78
  - Employment Gaps: 90 (no significant gaps)
  - Job Hopping: 85 (stable progression)
  - Skill Currency: 90 (current skills)
  - Application Quality: **65** (Generic template cover letter, minimal customization)
- **Total Score: 83**
- **Recommendation:** PHONE SCREEN

**Candidate B: Michael Chen**
- Qualifications: 85 (Masters in relevant field, required certifications) *Same as Sarah*
- Experience: 86 (5 years relevant experience, good progression) *Same as Sarah*
- Risk Flags: 91
  - Employment Gaps: 90 (no significant gaps)
  - Job Hopping: 85 (stable progression)
  - Skill Currency: 90 (current skills)
  - Application Quality: **95** (Exceptional - researched organization deeply, referenced specific programs, compelling fit narrative, excellent writing)
- **Total Score: 87**
- **Recommendation:** PHONE SCREEN

**Key Differentiator:** Michael's exceptional cover letter added **4 points** to his overall score compared to Sarah's generic application.

**Evidence from Michael's Cover Letter:**
- Referenced the organization's recent strategic plan by name
- Explained how his previous work at similar institution prepared him for specific challenges
- Addressed potential concern about geographic relocation with clear commitment
- Demonstrated writing ability critical for this role
- Showed genuine interest through depth of research

**Result:** Both candidates get phone screens, but Michael would be prioritized for earlier scheduling and is flagged as higher-priority candidate.

**Transparency Note:** When presenting these scores to hiring managers, explicitly state: "Candidate B's superior application quality (scored 95 vs. Candidate A's 65) contributed to the 4-point score difference, demonstrating stronger communication skills and genuine interest in the organization."

---

## Stage 2: Post-Interview Evaluation

After interviews are conducted, synthesize all information to make final hiring decision.

### Scoring Formula

**Final Score = (Resume Score × 0.25) + (Interview Rating × 0.50) + (Reference Checks × 0.25)**

### Required Inputs

To perform Stage 2 evaluation, provide:

1. **Resume Score** (from Stage 1) - 25% weight
2. **Interview Rating Form** (completed by interviewer) - 50% weight
   - Overall interview performance score (1-10, converted to 0-100 scale)
   - Core competency ratings
   - Situational responses
   - Red flags observed
   - Hiring recommendation
3. **Reference Check Notes** (at least 2-3 references) - 25% weight
   - Overall reference ratings (1-10, converted to 0-100 scale)
   - Would rehire assessment
   - Key themes from references

**Note:** Interview rating forms and reference check guides can be generated using the `recruiting-materials` skill.

### Stage 2 Output Format

When user provides completed interview form(s) and reference notes, generate:

**STAGE 2: FINAL HIRING EVALUATION**

**Candidate:** [Full Name]

| Evaluation Component | Raw Score | Weight | Weighted Score | Notes |
|---------------------|-----------|--------|----------------|-------|
| Resume (Stage 1) | [0-100] | 25% | [calc] | [Stage 1 summary] |
| Interview Performance | [0-100] | 50% | [calc] | [Interview highlights] |
| Reference Checks | [0-100] | 25% | [calc] | [Reference themes] |
| **FINAL SCORE** | | | **[Total]** | |

**Score Interpretation:**
- **90-100:** STRONG HIRE (Excellent across all dimensions)
- **80-89:** HIRE (Solid candidate, recommend offer)
- **70-79:** MARGINAL (Proceed with caution, has reservations)
- **60-69:** DO NOT HIRE (Significant concerns)
- **0-59:** DO NOT HIRE (Not suitable for role)

**KEY INSIGHTS:**

*Where Interview Contradicted Resume:*
• [Example: Resume showed X, but interview revealed Y]
• [Pattern observed during interview]
• [Discrepancy between credentials and demonstrated capability]

*Where Interview Confirmed Resume:*
• [Strength that was evident in both resume and interview]
• [Verified capability through specific examples]
• [Consistency between written and in-person presentation]

*Reference Check Highlights:*
• [Theme from multiple references]
• [Validation or concern raised]
• [Would rehire assessment and context]

**RECOMMENDATION: [STRONG HIRE / HIRE / DO NOT HIRE / KEEP SEARCHING]**

**Confidence Level:** [High / Medium / Low]

**Rationale:**
[2-3 paragraph explanation of decision, including:
- How interview performance aligned or contradicted resume
- Weight given to interviewer observations vs. credentials
- Reference check validations or concerns
- Why this candidate is/isn't the right fit
- Specific evidence supporting the recommendation]

### Multiple Candidate Comparison

**If Multiple Candidates Were Interviewed:**

| Rank | Candidate | Final Score | Resume | Interview | References | Recommendation |
|------|-----------|-------------|--------|-----------|------------|----------------|
| 1 | [Name] | [Score] | [Score] | [Score] | [Score] | [Decision] |
| 2 | [Name] | [Score] | [Score] | [Score] | [Score] | [Decision] |
| 3 | [Name] | [Score] | [Score] | [Score] | [Score] | [Decision] |

**Comparative Analysis:**

[Explain:
- Why top candidate stands out
- Key differentiators between candidates
- How interview performance changed initial rankings from Stage 1
- Specific examples where candidates diverged
- Final recommendation on who should receive offer]

---

## Batch Processing

When evaluating multiple candidates simultaneously:

### Stage 1 Batch Format Options

**Option 1: Quick Summary Table**

| Candidate | Score | Recommendation | Top Strength | Top Concern |
|-----------|-------|----------------|--------------|-------------|
| [Name 1] | [0-100] | [PHONE SCREEN/DECLINE] | [Brief] | [Brief] |
| [Name 2] | [0-100] | [PHONE SCREEN/DECLINE] | [Brief] | [Brief] |
| [Name 3] | [0-100] | [PHONE SCREEN/DECLINE] | [Brief] | [Brief] |

**Option 2: Tiered Summary (Notion-Ready Format)**

Generate comprehensive markdown document organized by tiers:

```markdown
# [Position Title] Candidate Screening Summary

## Overview

[Summary paragraph: number of candidates, evaluation approach]

---

## Candidate Rankings

### 🟢 TIER 1: EXCEPTIONAL CANDIDATES (90-100)

**1. [Candidate Name]** ([Location]) — RECOMMENDED

- **Current Role:** [Title] at [Company] ([Dates])
- **Score:** [Score]/100 (Qualifications: [X] | Experience: [Y] | Risk Flags: [Z])
- **Application Quality:** [Exceptional/Strong/Adequate/Weak] - [Brief note on cover letter]
- **Key Strengths:**
    - [Strength with evidence]
    - [Strength with evidence]
    - [Strength with evidence]
- **Fit:** [Excellent/Very Good/Good]
- **Potential Concern:** [Concern or "None significant"]

### 🟡 TIER 2: STRONG CANDIDATES (85-89)

[Same format as Tier 1]

### 🟠 TIER 3: SOLID CANDIDATES (70-84)

[Same format]

### 🔴 TIER 4: BELOW THRESHOLD (<70)

[Same format - DECLINE recommendations]

---

## Summary Matrix

| Rank | Candidate | Score | Qualifications | Experience | Risk Flags | Cover Letter | Recommendation |
|------|-----------|-------|----------------|------------|------------|--------------|----------------|
| 1 | [Name] | [Score] | [Score] | [Score] | [Score] | Exceptional | ⭐⭐⭐ PHONE SCREEN |
| 2 | [Name] | [Score] | [Score] | [Score] | [Score] | Strong | ⭐⭐⭐ PHONE SCREEN |
| 3 | [Name] | [Score] | [Score] | [Score] | [Score] | Adequate | ⭐⭐ PHONE SCREEN |
| 4 | [Name] | [Score] | [Score] | [Score] | [Score] | Weak | ⭐ CONSIDER |
| ... | ... | ... | ... | ... | ... | ... | ... |

---

## Key Competency Assessment

### Strong in [Competency 1]
- **[Candidate Name]** — [Evidence]
- **[Candidate Name]** — [Evidence]

### Strong in [Competency 2]
- **[Candidate Name]** — [Evidence]

---

## Strategic Recommendations

**IMMEDIATE PHONE SCREENS (Tier 1):**
1. **[Candidate Name]** — [Why]
2. **[Candidate Name]** — [Why]

**SECONDARY PHONE SCREENS (Tier 2):**
1. **[Candidate Name]** — [Why]

**DO NOT ADVANCE:**
- **[Candidate Name]** — [Reason]

---

## Notes for Hiring Manager

[Key insights, standout candidates, special considerations]

---

## How Scores Were Calculated

### Scoring Methodology

**Overall Score Formula:**
- **Qualifications (40%)** - Educational background, certifications, credentials
- **Experience (40%)** - Relevant work history, career progression, role alignment
- **Risk Flags (20%)** - Inverse scoring (higher = fewer concerns)

### Risk Flags Sub-Components (Each 25% of Risk Flags score)

1. **Employment Gaps** - Context-based evaluation of career continuity
2. **Job Hopping** - Pattern analysis of career stability and progression
3. **Skill Currency** - Assessment of how current skills and knowledge are
4. **Application Quality** - Cover letter evaluation and presentation

**Application Quality specifically evaluates:**
- Customization and personalization of cover letter
- Understanding of organization/mission demonstrated
- Professional writing quality and attention to detail
- Clear articulation of fit for this specific role
- Proactive addressing of resume gaps or transitions

### Impact of Cover Letters on Rankings

**Application Quality contributes 25% of Risk Flags score, which is 5% of the total score.**

**What this means:**
- An **exceptional cover letter** (score 95) vs. **adequate** (score 75) adds ~1 point to total
- An **exceptional cover letter** (score 95) vs. **weak/missing** (score 60) adds ~1.75 points to total
- An **exceptional cover letter** (score 95) vs. **poor** (score 40) adds ~2.75 points to total

**For similar candidates (identical Qualifications and Experience):**
Cover letter quality can be the deciding factor between candidates within the same tier or push a candidate into the next tier.

**Example:** Two candidates both score 85 on Qualifications and 88 on Experience:
- Candidate with **exceptional cover letter** → Total: ~87 (Strong Tier)
- Candidate with **generic cover letter** → Total: ~84 (Solid Tier)
- **Differentiator:** 3-point gap from application quality alone

### Transparency Note

All evaluations show the detailed breakdown of scores, including the Application Quality sub-score, so hiring managers can see exactly how cover letters influenced candidate rankings and understand the evidence-based rationale for recommendations.
```

This tiered format creates a markdown file ready to paste into Notion or share with stakeholders.

Follow with detailed individual evaluations for candidates scoring 70+, including candidate-specific verification questions.

### Stage 2 Batch Format

Use the Multiple Candidate Comparison table format shown above.

---

## Special Considerations

### Diversity & Inclusion
- Focus on skills and qualifications only
- Avoid bias based on name, school prestige, or employment gaps
- Value diverse experience paths and non-traditional backgrounds
- Consider how different backgrounds bring unique perspectives
- Use consistent evaluation criteria across all candidates

### Legal Compliance
- Never make recommendations based on protected characteristics
- Focus on job-related qualifications only
- Document objective reasons for all decisions
- Apply the same framework consistently to all candidates
- Interview questions should be role-related, not personal

### Red Flags

Common warning signs in resumes and interviews:
- Frequent job changes without clear progression
- Unexplained gaps (though ask for context before penalizing)
- Inability to provide specific examples in interviews
- Blaming others for past failures
- Defensive responses to questions
- Lack of preparation or research about organization
- Inconsistencies between resume and interview responses

See `references/red-flags.md` for comprehensive list.

### Green Flags

Positive indicators to recognize:
- Progressive career growth and increasing responsibility
- Relevant industry experience and domain knowledge
- Strong alignment with organizational mission/values
- Concrete examples with measurable outcomes
- Thoughtful questions about role and organization
- Self-awareness about strengths and development areas
- References eager to provide strong recommendations

See `references/green-flags.md` for comprehensive list.

---

## Integration with Recruiting Materials

The `recruiting-materials` skill generates all documents needed for the hiring process:

**Use the `recruiting-materials` skill to:**
- **Phone Screen Scripts** - 30-min scripts with standard assessment questions + candidate-specific verification questions
- **Interview Guides** - Comprehensive guides with standardized assessment questions (same for all candidates) + candidate-specific questions
- **Interview Evaluation Forms** - 1-10 rating scale forms aligned with Stage 2 scoring (Interview 50% weight)
- **Reference Check Guides** - Standardized reference check scripts and rating forms

**Usage Examples:**
- "Generate phone screen script for [candidate name] for [job title]" (includes verification questions from Stage 1)
- "Create interview guide for [job title]" (standardized assessment questions)
- "Generate evaluation form for [job title]" (Stage 2 compatible)
- "I need a reference check guide"

**Batch Mode:**
- "Generate phone screen scripts for all candidates in my evaluation report"
- "Create interview materials for top 3 candidates"

---

## Usage Examples

### Example 1: Stage 1 Resume Screening

**User:** "Evaluate this candidate for our Senior Campus Minister role. [attaches resume and job description]"

**Response:**
```
STAGE 1: RESUME SCREENING RESULTS

Candidate: Maria Rodriguez
Score: 88 out of 100
Recommendation: PHONE SCREEN

[Full scoring breakdown table]

Decision: PHONE SCREEN

Key Strengths:
• 8 years progressive campus ministry experience at similar institutions
• Masters in Divinity with focus on young adult spirituality
• Demonstrated success with graduate student populations (grew program 40%)

Key Concerns:
• Limited explicit mention of Ignatian spirituality in materials
• No direct experience with international student ministry
• Need to verify approach to interfaith dialogue

CANDIDATE-SPECIFIC VERIFICATION QUESTIONS:
(Ask during phone screen to address concerns above)

1. How have you incorporated contemplative practices into campus ministry?
2. Describe your experience working with diverse faith traditions
3. Tell me about your largest challenge ministering to graduate students

Next Steps: Use recruiting-materials skill to generate phone screen script (will include standard assessment questions + verification questions above)
```

### Example 2: Stage 2 Post-Interview Evaluation

**User:** "I interviewed Maria Rodriguez. Here's the completed interview form showing overall rating of 9/10 (90), and reference checks averaged 8.5/10 (85). Her Stage 1 score was 88. However, I noticed she seemed uncertain about our Ignatian mission during the interview."

**Response:**
```
STAGE 2: FINAL HIRING EVALUATION

Candidate: Maria Rodriguez

[Full evaluation table showing:]
Resume: 88 × 25% = 22
Interview: 90 × 50% = 45
References: 85 × 25% = 21.25
FINAL SCORE: 88.25

Score Interpretation: HIRE (Solid candidate, recommend offer)

KEY INSIGHTS:

Where Interview Contradicted Resume:
• Resume emphasized "contemplative ministry" but interview revealed limited depth on Ignatian tradition specifically
• Application suggested strong interfaith work, interview showed more Christian-focused approach

Where Interview Confirmed Resume:
• Graduate student ministry expertise validated through specific examples
• Program development skills confirmed (detailed 3-year growth strategy)
• Pastoral presence and empathy evident throughout interview

Reference Check Highlights:
• All 3 references would rehire "without hesitation"
• Described as "deeply spiritual but accessible to questioning students"
• One reference noted: "not Jesuit-trained but quick learner of new traditions"

RECOMMENDATION: HIRE

Confidence Level: High

Rationale:
While Maria's familiarity with Ignatian spirituality is developing rather than deep, her interview performance (90/100, weighted 50%) demonstrates the pastoral skills, graduate student expertise, and adaptive capacity that are most critical for success. Her uncertainty about the Ignatian mission is a training opportunity, not a disqualifier—references consistently praised her ability to learn and integrate new spiritual frameworks. The interview revealed someone who may grow into the Ignatian tradition organically through practice.

Most importantly, your direct observation of her presence, empathy, and student-centered approach (captured in the 9/10 interview rating) outweighs the resume credential gap. References validate this is who she is consistently, not just in an interview setting.

Recommendation: Make offer with onboarding plan that includes Ignatian formation and mentorship.
```

### Example 3: Multiple Candidate Comparison

**User:** "I interviewed three finalists. Here are all the interview forms and references. Help me decide."

**Response:**
```
[Provides comparative analysis table showing all three candidates with scores]

COMPARATIVE ANALYSIS:

While Candidate A had the strongest resume (92), their interview performance (65) revealed concerning gaps in practical ministry skills that appeared impressive on paper. Multiple references used the phrase "better administrator than pastor."

Candidate B, who scored lower in Stage 1 (78), significantly exceeded expectations in the interview (94) with compelling examples of navigating difficult pastoral situations and building inclusive communities. References were unanimous: "best campus minister we've ever had."

Candidate C scored consistently (82/85/80) but didn't distinguish themselves beyond solid competence.

**Recommendation:** Hire Candidate B. The interview and reference checks (weighted 75% combined) reveal the pastoral effectiveness and community-building skills that matter most for daily success, despite the less impressive paper credentials.
```

---

## Critical Reminders for Users

### Stage 1 (Resume Screening)
- ✓ Be objective - score against requirements, not preferences
- ✓ High scores (70+) earn a phone screen, not the job
- ✓ Don't let a great resume blind you to potential red flags
- ✓ All candidates scoring 70+ deserve a phone screen opportunity
- ✓ Generate candidate-specific verification questions for each phone screen

### Stage 2 (Final Evaluation)
- ✓ **Interview performance is 50% of the decision** - trust what you observed
- ✓ References often reveal patterns that interviews miss
- ✓ If your gut says "no," explore why before overriding it
- ✓ A candidate can have a perfect resume and still be wrong for the role
- ✓ Compare all interviewed candidates side-by-side, not in isolation
- ✓ Document specific examples, not just feelings

### General Principles
- ⚠ Resume shows potential; phone screen verifies basics; interview shows reality
- ⚠ Skills can be taught; values and work ethic cannot
- ⚠ Hiring the wrong person is expensive; taking time to find the right one is worth it
- ⚠ When in doubt, keep looking
- ⚠ Use recruiting-materials skill to generate consistent, professional hiring documents

---

## When to Use This Skill

**Trigger Stage 1 when user provides:**
- Resumes with job description
- "Screen these candidates"
- "Evaluate this applicant"
- "Should I phone screen this person?"

**For batch evaluations with tiered Notion-ready format:**
- "Evaluate all candidates and create a tiered summary"
- "Screen these candidates and give me a Notion-ready report"
- "Create a comprehensive candidate screening summary"

**Trigger Stage 2 when user provides:**
- Completed interview forms
- Post-interview assessment request
- "Help me decide between candidates"
- "Final evaluation for [candidate]"

**Direct to recruiting-materials skill when user asks for:**
- "Create phone screen script"
- "Generate interview guide"
- "I need evaluation forms"
- "Reference check template"
- "Generate materials for [candidate]"

---

## References

For detailed methodology and supporting materials:
- **Scoring Rubrics**: See `references/scoring-rubrics.md` for detailed component scoring
- **Red Flags Guide**: See `references/red-flags.md` for warning signs
- **Green Flags Guide**: See `references/green-flags.md` for positive indicators
- **Interview Materials**: Use `recruiting-materials` skill for guides and forms
