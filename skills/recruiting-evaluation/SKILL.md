---
name: recruiting-evaluation
description: Evaluate job candidates using a two-stage framework - Stage 1 (Resume Screening) determines who to interview, Stage 2 (Post-Interview Evaluation) determines who gets the job offer. Use when screening resumes, making interview decisions, or conducting final hiring evaluations with interview feedback weighted at 50%.
---

# Recruiting Evaluation Skill

A comprehensive two-stage evaluation framework that separates initial resume screening from post-interview assessment, with heavy emphasis on human interviewer feedback.

## Two-Stage Evaluation Framework

This skill uses a two-stage process to evaluate candidates:

### Stage 1: Resume Screening (Initial Filter)
- **Purpose:** Quickly identify which candidates to interview
- **Input:** Resume, cover letter, application materials
- **Scoring:** Qualifications (40%) + Experience (40%) + Risk Flags (20%)
- **Output:** 0-100 score + Text recommendation + Interview questions
- **Decision Thresholds:**
  - **85-100: ADVANCE TO INTERVIEW** - Schedule in-person interview
  - **70-84: PHONE SCREEN FIRST** - Conduct 30-min phone screen, then reassess
  - **0-69: DECLINE** - Send professional decline communication

### Stage 2: Post-Interview Evaluation (Final Decision)
- **Purpose:** Determine who receives the job offer
- **Input:** Resume score + Interview ratings + Reference checks + Manager observations
- **Scoring:** Resume (25%) + Interview (50%) + References (25%)
- **Output:** Final hire/no-hire recommendation with detailed comparison
- **Key Feature:** Human interviewer feedback is weighted at 50% - the most important factor

**Critical Philosophy:** A strong resume gets you to the interview. Your performance in the interview determines if you get the job. Manager/interviewer observations override resume credentials.

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

Assess potential concerns (score inversely - higher is better):

- Employment gaps (evaluate context before penalizing)
- Job hopping patterns without clear progression
- Relocation requirements (if role requires it)
- Skill currency concerns (outdated technical skills)
- Internal vs. external candidate considerations
- Cultural/mission fit concerns based on application materials

**Scoring Guide:**
- **90-100:** No risk flags, ideal scenario
- **80-89:** Minor concerns, easily manageable
- **70-79:** Moderate risk, needs discussion in interview
- **60-69:** Notable concerns, requires careful evaluation
- **Below 60:** High risk factors, significant concerns

### Stage 1 Output Format

Present results as:

**STAGE 1: RESUME SCREENING RESULTS**

**Candidate:** [Full Name]
**Score:** [0-100] out of 100
**Recommendation:** [ADVANCE TO INTERVIEW / PHONE SCREEN FIRST / DECLINE]

| Component | Score | Weight | Weighted Score | Notes |
|-----------|-------|--------|----------------|-------|
| Qualifications | [0-100] | 40% | [calc] | [Brief assessment] |
| Experience | [0-100] | 40% | [calc] | [Brief assessment] |
| Risk Flags | [0-100] | 20% | [calc] | [Brief assessment] |
| **TOTAL** | | | **[Final Score]** | |

**Score Interpretation:**
- **90-100:** ADVANCE TO INTERVIEW (Exceptional candidate)
- **85-89:** ADVANCE TO INTERVIEW (Strong candidate)
- **70-84:** PHONE SCREEN FIRST (Promising, needs verification)
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

**Decision: [ADVANCE TO INTERVIEW / PHONE SCREEN FIRST / DECLINE]**

**Key Questions for Interview:**
1. [Question about gap/concern, if applicable]
2. [Question about specific experience validation]
3. [Question about role-critical skill demonstration]

**Next Steps:**
- **If 85+:** Schedule in-person interview and prepare interview guide (see recruiting-materials skill)
- **If 70-84:** Conduct 30-minute phone screen to verify concerns, then reassess
- **If <70:** Send professional decline communication

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

### Stage 1 Batch Format

| Candidate | Score | Recommendation | Top Strength | Top Concern |
|-----------|-------|----------------|--------------|-------------|
| [Name 1] | [0-100] | [ADVANCE/PHONE/DECLINE] | [Brief] | [Brief] |
| [Name 2] | [0-100] | [ADVANCE/PHONE/DECLINE] | [Brief] | [Brief] |
| [Name 3] | [0-100] | [ADVANCE/PHONE/DECLINE] | [Brief] | [Brief] |

Follow with detailed individual evaluations for each candidate who scored 70+.

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

For interview guides, evaluation forms, and reference check templates:

**Use the `recruiting-materials` skill to:**
- Generate customized interview guides based on job description
- Get interview rating forms (copy-paste ready)
- Get reference check guides and scripts
- Create role-specific evaluation rubrics

Example: "Generate an interview guide for [job title]" or "I need an interview rating form"

---

## Usage Examples

### Example 1: Stage 1 Resume Screening

**User:** "Evaluate this candidate for our Senior Campus Minister role. [attaches resume and job description]"

**Response:**
```
STAGE 1: RESUME SCREENING RESULTS

Candidate: Maria Rodriguez
Score: 88 out of 100
Recommendation: ADVANCE TO INTERVIEW

[Full scoring breakdown table]

Decision: ADVANCE TO INTERVIEW

Key Strengths:
• 8 years progressive campus ministry experience at similar institutions
• Masters in Divinity with focus on young adult spirituality
• Demonstrated success with graduate student populations (grew program 40%)

Key Concerns:
• Limited explicit mention of Ignatian spirituality in materials
• No direct experience with international student ministry
• Need to verify approach to interfaith dialogue

Key Questions for Interview:
1. How have you incorporated contemplative practices into campus ministry?
2. Describe your experience working with diverse faith traditions
3. Tell me about your largest challenge ministering to graduate students

Next Steps: Schedule in-person interview and use recruiting-materials skill to generate interview guide
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
- ✓ High scores earn an interview, not the job
- ✓ Don't let a great resume blind you to potential interview red flags
- ✓ Borderline candidates (70-84) deserve a phone screen opportunity

### Stage 2 (Final Evaluation)
- ✓ **Interview performance is 50% of the decision** - trust what you observed
- ✓ References often reveal patterns that interviews miss
- ✓ If your gut says "no," explore why before overriding it
- ✓ A candidate can have a perfect resume and still be wrong for the role
- ✓ Compare all interviewed candidates side-by-side, not in isolation
- ✓ Document specific examples, not just feelings

### General Principles
- ⚠ Resume shows potential; interview shows reality
- ⚠ Skills can be taught; values and work ethic cannot
- ⚠ Hiring the wrong person is expensive; taking time to find the right one is worth it
- ⚠ When in doubt, keep looking

---

## When to Use This Skill

**Trigger Stage 1 when user provides:**
- Resumes with job description
- "Screen these candidates"
- "Evaluate this applicant"
- "Should I interview this person?"

**Trigger Stage 2 when user provides:**
- Completed interview forms
- Post-interview assessment request
- "Help me decide between candidates"
- "Final evaluation for [candidate]"

**Direct to recruiting-materials skill when user asks for:**
- "Create interview guide"
- "I need evaluation forms"
- "Reference check template"

---

## References

For detailed methodology and supporting materials:
- **Scoring Rubrics**: See `references/scoring-rubrics.md` for detailed component scoring
- **Red Flags Guide**: See `references/red-flags.md` for warning signs
- **Green Flags Guide**: See `references/green-flags.md` for positive indicators
- **Interview Materials**: Use `recruiting-materials` skill for guides and forms
