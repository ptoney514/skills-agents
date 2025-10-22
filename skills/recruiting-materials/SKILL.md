---
name: recruiting-materials
description: Generate interview guides, evaluation forms, and reference check templates for recruiting. Use when hiring managers need interview preparation materials, structured evaluation forms, or reference check scripts. Creates customized guides based on job descriptions and role requirements.
---

# Recruiting Materials Generator

Generate professional interview guides, evaluation forms, and reference check templates customized for specific roles and hiring needs.

## Overview

This skill provides ready-to-use recruiting materials:
- **Interview Guides**: Customized 60-90 minute interview structures with role-specific questions
- **Interview Rating Forms**: Structured evaluation forms for interviewers to complete
- **Reference Check Guides**: Scripts and forms for conducting professional reference checks

All materials are designed to work seamlessly with the `recruiting-evaluation` skill's two-stage framework.

---

## When to Use This Skill

Trigger this skill when user requests:
- "Generate interview guide for [job title]"
- "I need an interview rating form"
- "Create reference check template"
- "Help me prepare for interviewing candidates"
- "What questions should I ask in the interview?"

---

## Material Types

### 1. Interview Guide

**Purpose:** Provide structured interview framework with customized questions based on job requirements.

**When to generate:**
- After candidate passes Stage 1 resume screening (85+ score)
- Before conducting phone screens or in-person interviews
- When preparing panel interviews

**Customization based on:**
- Job description and key responsibilities
- Required competencies and skills
- Industry/population specifics
- Organizational culture/values
- Resume concerns that need exploration

**Output:** See `assets/interview-guide-template.md` for full template structure.

### 2. Interview Rating Form

**Purpose:** Standardized evaluation form for interviewers to complete during/after interviews.

**When to generate:**
- Alongside interview guide preparation
- For all interviewers on panel interviews
- Before conducting phone screens

**Key sections:**
- Core competency ratings (1-10 scale)
- Situational response assessments
- Red flag checklist
- Overall hiring recommendation
- Comparison to resume expectations

**Output:** See `assets/interview-rating-form.md` for complete form.

### 3. Reference Check Guide

**Purpose:** Professional script and structure for conducting reference checks.

**When to generate:**
- After strong interview performance
- Before making final hiring decision
- When proceeding to Stage 2 evaluation

**Key sections:**
- Opening script and context setting
- Performance and competency questions
- Interpersonal and cultural fit questions
- Critical assessment questions
- Reference rating and notes

**Output:** See `assets/reference-check-guide.md` for full template.

---

## How to Generate Customized Materials

### Interview Guide Generation

When user requests an interview guide, follow this process:

**1. Gather Information**

Ask for or extract from provided materials:
- Job title and department
- Key responsibilities (3-5 main duties)
- Required competencies (technical, soft skills, leadership)
- Must-have vs. preferred qualifications
- Organizational values/culture keywords
- Industry or population specifics
- Any resume concerns from Stage 1 screening

**2. Customize Questions**

Using the template from `assets/interview-guide-template.md`:

**Behavioral Questions:**
- Map required competencies to STAR method questions
- Create 4-5 behavioral questions tied to success factors
- Include follow-up probes for depth

Example:
```
Required Competency: Project Management
→ Behavioral Q: "Tell me about a time you managed a complex project with competing priorities. Walk me through your approach."
→ Follow-up: "What would you do differently if you faced that situation today?"
```

**Situational Scenarios:**
- Create 2-3 realistic scenarios the person will face in role
- Base scenarios on actual job challenges
- Include ethical/values-based scenario

Example:
```
Role: Campus Minister to Graduate Students
→ Scenario: "A doctoral student comes to you in crisis three weeks before their dissertation defense. They're questioning their faith and career path. You have 15 minutes before your next commitment. What do you do?"
```

**Technical/Role-Specific:**
- Include 3-4 questions testing required knowledge or skills
- Match complexity to role level (entry vs. senior)
- Allow candidate to demonstrate expertise

**Red Flag Probes (if applicable):**
- Address any concerns from Stage 1 resume screening
- Employment gaps, job hopping, skill currency, etc.
- Frame professionally, give candidate chance to explain

**3. Format for Use**

- Use clear timing structure (0:00-0:05 Welcome, etc.)
- Include space for interviewer notes
- Provide rating scale (1-10) for each question
- Add post-interview reflection section

**4. Pair with Rating Form**

Always provide the interview rating form alongside the guide so interviewer can complete evaluation.

### Interview Rating Form Generation

Use the template from `assets/interview-rating-form.md` as-is, or customize:

**Customization options:**
- Add role-specific competencies to Part 1
- Tailor scenario questions in Part 2
- Adjust red flags checklist for role context
- Keep standard structure for Stage 2 compatibility

**Important:** Form must produce:
- Overall interview rating (1-10)
- Hiring recommendation category
- Specific observations and notes

These feed directly into Stage 2 evaluation (50% weight).

### Reference Check Guide Generation

Use the template from `assets/reference-check-guide.md` with minor customization:

**Customize Section 2: Performance Questions**
- Add 1-2 role-specific questions
- Ask about key competencies from job description

Example:
```
Standard Q: "What were their greatest strengths?"
+ Role-Specific Q: "This role requires strong data analysis skills. How did [Candidate] demonstrate analytical thinking?"
```

**Keep standardized:**
- Opening script and rapport building
- Would-rehire question
- Red flag probes section
- Rating structure (1-10)

References produce 1-10 ratings that convert to 0-100 scale for Stage 2 (25% weight).

---

## Output Format

When generating materials, provide:

### For Interview Guide Requests:

```
INTERVIEW GUIDE
Position: [Job Title]
Department: [Department]
Prepared for: [Interviewer Name]

[Full customized interview guide using template structure]

═══════════════════════════════════════════════════
PAIRED INTERVIEW RATING FORM
═══════════════════════════════════════════════════

[Include the interview rating form so interviewer has both documents]
```

### For Interview Rating Form Requests:

```
[Provide complete interview rating form from assets/interview-rating-form.md]

This form should be completed during or immediately after the interview and will be used in Stage 2 final evaluation (weighted at 50%).
```

### For Reference Check Guide Requests:

```
[Provide complete reference check guide from assets/reference-check-guide.md with any role-specific customizations]

Conduct 2-3 reference checks per finalist candidate. Average the ratings for Stage 2 evaluation (weighted at 25%).
```

---

## Integration with recruiting-evaluation Skill

These materials support the two-stage evaluation framework:

**Stage 1 → Materials Generation:**
```
User: [Runs Stage 1 resume screening]
recruiting-evaluation: "Candidate scored 88 - ADVANCE TO INTERVIEW"
User: "Generate interview guide for this role"
recruiting-materials: [Creates customized guide + rating form]
```

**Interview → Stage 2:**
```
User: [Conducts interview using guide, completes rating form]
User: [Conducts reference checks using guide]
User: "Evaluate final hiring decision with interview rating of 9/10 and references averaging 8.5/10"
recruiting-evaluation: [Performs Stage 2 evaluation with Resume 25% + Interview 50% + References 25%]
```

---

## Material Templates

All full templates are stored in the `assets/` directory:

- `assets/interview-guide-template.md` - Complete interview guide structure
- `assets/interview-rating-form.md` - Standardized evaluation form
- `assets/reference-check-guide.md` - Reference check script and form

These templates are:
- Copy-paste ready for users
- Formatted for printing or digital use
- Compatible with Stage 2 evaluation scoring
- Customizable while maintaining structure

---

## Best Practices

### Interview Guide Design
- ✓ Match questions to actual job demands, not generic skills
- ✓ Include mix of behavioral, situational, and technical questions
- ✓ Provide realistic time allocations
- ✓ Leave space for candidate questions (reveals priorities)
- ✓ Include immediate post-interview reflection section

### Interview Rating Form Usage
- ✓ Complete within 15 minutes of interview ending
- ✓ Use specific examples to justify ratings
- ✓ Be honest about red flags (they matter for Stage 2)
- ✓ Compare to resume expectations explicitly
- ✓ Trust your observations (50% of final decision)

### Reference Check Conduct
- ✓ Conduct at least 2-3 references per finalist
- ✓ Ask for specific examples, not just opinions
- ✓ Listen for what's NOT said (lukewarm = concerning)
- ✓ Probe on interview concerns if applicable
- ✓ Document immediately while fresh

---

## Usage Examples

### Example 1: Generating Interview Guide

**User:** "Generate an interview guide for a Senior Campus Minister position working with graduate students. The job requires pastoral skills, program development, Ignatian spirituality knowledge, and interfaith competence."

**Response:**
```
INTERVIEW GUIDE
Position: Senior Campus Minister (Graduate Students)
Department: Campus Ministry
Interview Duration: 75 minutes

[Provides fully customized guide including:]

PART 3: BEHAVIORAL QUESTIONS (30 minutes)

[Pastoral Skills]
Q: "Describe a time when you had to provide spiritual support to someone in crisis while balancing multiple commitments. What was your approach?"
Follow-up: "How do you practice self-care to sustain your ministry?"
RATING: ___/10  NOTES:

[Program Development]
Q: "Tell me about a program or initiative you developed from scratch. What was the need, your approach, and the outcome?"
Follow-up: "How did you measure success?"
RATING: ___/10  NOTES:

[Ignatian Spirituality - if mentioned in resume]
Q: "How have you incorporated Ignatian practices like discernment or the Examen into your ministry?"
Follow-up: "Give an example of guiding someone through an Ignatian discernment process."
RATING: ___/10  NOTES:

OR

[Ignatian Spirituality - if NOT mentioned]
Q: "Tell me about your experience with contemplative spiritual practices. Which traditions or approaches have you found most effective with young adults?"
Follow-up: "How do you adapt spiritual practices for people at different stages of faith development?"
NOTE TO INTERVIEWER: Assess openness to learning Ignatian tradition
RATING: ___/10  NOTES:

[Interfaith Competence]
Q: "Describe a situation where you navigated religious diversity or interfaith dialogue. What was challenging and what did you learn?"
Follow-up: "How do you maintain your own faith identity while honoring others' traditions?"
RATING: ___/10  NOTES:

PART 4: SITUATIONAL SCENARIOS (15 minutes)

[SCENARIO 1: Pastoral Crisis]
"A doctoral student comes to you three weeks before their dissertation defense. They're experiencing a faith crisis and questioning their entire career path. You have your next appointment in 15 minutes. Walk me through how you'd handle this."

Look for:
• Triage and prioritization
• Presence and empathy
• Appropriate boundaries
• Follow-up planning
RATING: ___/10  NOTES:

[SCENARIO 2: Values Conflict]
"A graduate student leader wants to host an event that conflicts with university Catholic identity guidelines, but they're passionate about the cause and it's for social justice. How do you navigate this?"

Look for:
• Ignatian discernment approach
• Balancing pastoral care and institutional policy
• Creative problem-solving
• Accompaniment skills
RATING: ___/10  NOTES:

[... continues with full guide ...]

═══════════════════════════════════════════════════
PAIRED INTERVIEW RATING FORM
═══════════════════════════════════════════════════

[Includes complete rating form]
```

### Example 2: Interview Rating Form Only

**User:** "I need the standard interview rating form"

**Response:**
```
[Provides complete interview rating form from assets]

CANDIDATE INTERVIEW EVALUATION FORM
Role: _______________________
Candidate: ___________________
Interviewer: _________________
Date: _______  Time: _______
Interview Type: ☐ Phone Screen ☐ In-Person ☐ Panel

[Full form with all sections...]

This form should be completed immediately after the interview. Your ratings will be weighted at 50% in the final hiring decision (Stage 2 evaluation).
```

### Example 3: Reference Check Guide

**User:** "Create a reference check template for the campus minister role"

**Response:**
```
REFERENCE CHECK FORM
Candidate: ___________________
Position: Senior Campus Minister (Graduate Students)
Reference Name: _______________
Reference Title/Relationship: ______________
Dates Working Together: _______
Checked By: _________  Date: _________

[Standard opening script and rapport building]

SECTION 2: PERFORMANCE & COMPETENCIES (Customized)

[Standard questions...]

4. [ROLE-SPECIFIC QUESTION]
"This role requires strong pastoral presence with graduate students going through transition and crisis. How did [Candidate] demonstrate pastoral care skills in your experience together?"

5. [ROLE-SPECIFIC QUESTION]
"The position involves developing and growing ministry programs. Can you give an example of how [Candidate] built or improved a program or initiative?"

[Continues with full reference check guide...]
```

---

## Tips for Effective Materials

### Interview Guides
- Questions should feel conversational, not interrogative
- Mix of challenging and relationship-building questions
- Allow space for candidate personality to emerge
- Include "culture add" not just "culture fit" questions

### Rating Forms
- Use 1-10 scale (don't use 1-5, less granular)
- Require written notes, not just numbers
- Include "would you want to work with this person?" question
- Force comparison to resume expectations

### Reference Checks
- Warm, professional tone in script
- Listen for enthusiasm level (or lack thereof)
- "Would rehire?" is the most telling question
- Code words matter: "adequate" = not great, "tries hard" = struggled

---

## When NOT to Use This Skill

**Don't use this skill for:**
- Actual candidate evaluation (use recruiting-evaluation skill)
- Resume screening decisions
- Final hiring recommendations
- Interview coaching or training

**Use recruiting-evaluation skill instead when:**
- Evaluating candidate resumes
- Making interview/no-interview decisions
- Synthesizing interview results into hiring decision
- Comparing multiple candidates

These two skills work together: recruiting-materials creates the tools, recruiting-evaluation uses them to make decisions.
