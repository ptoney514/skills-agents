---
name: recruiting-materials
description: Generate professional hiring documents including phone screen scripts, interview guides, evaluation forms (1-10 rating scale), and reference check guides. Supports both single-candidate and batch generation modes with standardized and candidate-specific questions.
---

# Recruiting Materials Skill

Generate consistent, professional hiring documents for any position. This skill creates standardized interview materials while allowing for candidate-specific customization based on concerns identified during resume screening.

## Overview

This skill generates four types of recruiting documents:

1. **Phone Screen Scripts** - 30-minute structured phone screens
2. **Interview Guides** - Comprehensive in-person interview guides
3. **Interview Evaluation Forms** - Standardized rating forms (1-10 scale)
4. **Reference Check Guides** - Professional reference check scripts

**Key Features:**
- **Standardized Questions** - Same core questions for all candidates (ensures fairness)
- **Candidate-Specific Questions** - Tailored questions to address individual concerns
- **Clear Labeling** - All materials clearly distinguish standard vs. custom questions
- **Batch Support** - Generate materials for one candidate or many at once
- **Stage 2 Compatible** - Evaluation forms align with recruiting-evaluation skill's scoring model

---

## Material Types

### 1. Phone Screen Scripts

**Purpose:** 30-minute structured phone conversations to verify basic qualifications and interest before investing in full interviews.

**When to generate:** After Stage 1 resume evaluation recommends phone screen (70+ score)

**Key sections:**
- Standard assessment questions (same for all candidates)
- Candidate-specific verification questions (from Stage 1 concerns)
- Logistics and practical matters
- Role overview
- Post-call evaluation

### 2. Interview Guides

**Purpose:** Comprehensive guides for in-person/virtual interviews with behavioral and situational questions.

**When to generate:** After successful phone screen, before scheduling interviews

**Key sections:**
- Pre-interview preparation checklist
- Time-structured interview flow
- Standard competency-based questions (ALL candidates)
- Candidate-specific verification questions (THIS candidate only)
- Cultural fit assessment
- Post-interview reminders

### 3. Interview Evaluation Forms

**Purpose:** Standardized 1-10 rating forms that contribute 50% to Stage 2 final decision.

**When to generate:** Before interviews (provide to all interviewers)

**Key sections:**
- Core competency ratings (1-10 scale for each)
- Overall interview performance rating (converts to 0-100 for Stage 2)
- Red flags checklist
- Strengths and concerns
- Hiring recommendation with rationale

### 4. Reference Check Guides

**Purpose:** Professional scripts for checking references to validate candidate qualifications.

**When to generate:** For finalist candidates before final hiring decision

**Key sections:**
- Opening script and relationship verification
- Performance assessment questions
- Competency validation
- "Would rehire?" critical question
- Candidate-specific validation questions
- Post-call evaluation (contributes 25% to Stage 2)

---

## How to Use This Skill

### Single Candidate Mode

**Request format:**
- "Generate [material type] for [candidate name] for [job title]"
- "Create phone screen script for Maria Rodriguez for Senior Campus Minister"
- "I need an interview guide for John Smith for Associate Director position"

**Provide when requesting:**
- Job title and description
- Candidate name
- Candidate-specific verification questions (if from Stage 1 evaluation)
- Key competencies to assess

### Batch Mode

**Request format:**
- "Generate [material type] for all candidates in [list/evaluation]"
- "Create interview guides for these 4 finalists: [names]"
- "I need phone screen scripts for all candidates who scored 70+"

**Output:** Individual materials for each candidate with standardized questions consistent across all, but candidate-specific sections tailored to each person.

---

## Template Structure

All materials follow this consistent structure:

**🔵 STANDARD SECTIONS**
- Same for ALL candidates for this position
- Ensures fair comparison
- Required for legal compliance

**🟡 CANDIDATE-SPECIFIC SECTIONS**
- Unique to THIS candidate
- Addresses Stage 1 concerns/gaps
- Clearly labeled so interviewers know context

---

## Integration with Recruiting-Evaluation Skill

This skill works hand-in-hand with the `recruiting-evaluation` skill:

**Workflow:**
1. User provides resume → `recruiting-evaluation` runs Stage 1
2. Stage 1 outputs candidate-specific verification questions
3. User requests phone screen script → `recruiting-materials` generates it (includes verification questions)
4. After phone screen passes → `recruiting-materials` generates interview guide + evaluation form
5. After interview → interviewer completes evaluation form
6. User provides completed form → `recruiting-evaluation` runs Stage 2
7. Stage 2 uses interview rating (50%), resume score (25%), references (25%)

**Key Connection Points:**
- Stage 1 verification questions → included in phone screen scripts and interview guides
- Evaluation form ratings → feed into Stage 2 scoring (50% weight)
- Reference check ratings → feed into Stage 2 scoring (25% weight)

---

## Usage Examples

### Example 1: Phone Screen Script Generation

**User Request:**
"Generate phone screen script for Maria Rodriguez for Senior Campus Minister. She scored 88 in Stage 1. Verification questions: (1) How have you incorporated contemplative practices? (2) Experience with diverse faith traditions? (3) Largest challenge with graduate students?"

**Generated Output:**
```
PHONE SCREEN SCRIPT

Position: Senior Campus Minister
Candidate: Maria Rodriguez
Duration: 30 minutes

[Opening script with candidate name]

SECTION 1: STANDARD ASSESSMENT QUESTIONS
(These questions are asked of ALL candidates)

1. Walk me through your campus ministry experience...
2. How do you approach spiritual formation with graduate students?
3. Describe your experience building community...
4. Tell me about your approach to interfaith dialogue...
5. What attracts you to Jesuit higher education?

SECTION 2: CANDIDATE-SPECIFIC VERIFICATION QUESTIONS
(These questions are unique to Maria and address Stage 1 concerns)

NOTE: These questions were generated because Maria's application showed limited explicit Ignatian spirituality experience.

1. How have you incorporated contemplative practices into your ministry work?
2. Can you describe your experience working with diverse faith traditions?
3. What has been your largest challenge ministering to graduate students?

[Logistics, role overview, closing, evaluation sections]
```

### Example 2: Batch Interview Guides

**User Request:**
"Create interview guides for 3 finalists: Maria Rodriguez, John Smith, Sarah Johnson. Position is Senior Campus Minister. Key competencies: pastoral care, community building, Ignatian spirituality, program development, interfaith engagement."

**Generated Output:**
```
[THREE SEPARATE GUIDES]

INTERVIEW GUIDE #1: MARIA RODRIGUEZ

[Standard sections same for all three]
🔵 STANDARD ASSESSMENT QUESTIONS (ALL CANDIDATES):
1. Pastoral Care: "Tell me about a time you supported someone through a spiritual crisis..."
2. Community Building: "Describe how you built community in a diverse campus setting..."
3. Ignatian Spirituality: "How do you integrate Ignatian practices into ministry?"
4. Program Development: "Walk me through a program you developed from scratch..."
5. Interfaith Engagement: "Describe your approach to interfaith dialogue..."

🟡 MARIA-SPECIFIC QUESTIONS:
1. [Her verification question about contemplative practices]
2. [Her verification question about graduate students]

---

INTERVIEW GUIDE #2: JOHN SMITH

[Same 5 standard questions as Maria's guide]

🟡 JOHN-SPECIFIC QUESTIONS:
1. [His unique verification questions based on his Stage 1 evaluation]

[And so on for Sarah Johnson...]
```

### Example 3: Evaluation Form

**User Request:**
"Generate interview evaluation form for Senior Campus Minister position."

**Generated Output:**
```
INTERVIEW EVALUATION FORM

Position: Senior Campus Minister
Candidate Name: _____________________

INSTRUCTIONS: Rate each competency 1-10. Your ratings contribute 50% to final hiring decision.

CORE COMPETENCIES (🔵 Same for ALL candidates):

Competency 1: Pastoral Care
Rating: ☐1 ☐2 ☐3 ☐4 ☐5 ☐6 ☐7 ☐8 ☐9 ☐10
Evidence/Notes: ________________

Competency 2: Community Building
Rating: ☐1 ☐2 ☐3 ☐4 ☐5 ☐6 ☐7 ☐8 ☐9 ☐10
Evidence/Notes: ________________

[Continue for all 5 competencies]

OVERALL INTERVIEW RATING: ___/10

This rating × 10 = /100 for Stage 2 (weighted at 50%)

HIRING RECOMMENDATION:
☐ Strong Hire ☐ Hire ☐ Maybe ☐ No Hire

[Red flags checklist, strengths, concerns sections...]
```

### Example 4: Reference Check Guide

**User Request:**
"Generate reference check guide for Maria Rodriguez. We're calling her previous supervisor at University of San Diego to verify her campus ministry experience."

**Generated Output:**
```
REFERENCE CHECK GUIDE

Candidate: Maria Rodriguez
Position: Senior Campus Minister
Reference: [To be filled in]
Relationship: Former Supervisor

[Opening script]

STANDARD QUESTIONS (for all references):
1. Working relationship and dates?
2. Overall performance assessment?
3. Greatest strengths?
4. Areas for development?
5. Example of best work?
6. Working style and cultural fit?
7. How did they handle feedback?
8. Why did they leave?
9. Would rehire? (CRITICAL)

MARIA-SPECIFIC VERIFICATION:
🟡 "Maria mentioned limited experience with Ignatian spirituality in her application. Can you speak to how she approaches contemplative practices and spiritual formation?"

RATING: ___/10

[This rating contributes 25% to Stage 2 final decision]
```

---

## Best Practices

### Fairness & Legal Compliance

✓ **Use identical standardized questions** for all candidates
✓ **Only vary candidate-specific sections** based on resume gaps
✓ **Rate against requirements**, not against other candidates
✓ **Document specific examples** for all ratings
✓ **Avoid protected characteristic questions** (age, religion, family status, etc.)
✓ **Get candidate permission** before checking references

### Quality & Consistency

✓ **Complete evaluation forms immediately** after interviews (while fresh)
✓ **Check minimum 2-3 references** (not just one)
✓ **Use verification questions strategically** (only what you need to verify)
✓ **Keep all materials for 1-2 years** (for compliance/recordkeeping)
✓ **File naming convention**: Position_MaterialType_CandidateName_Date.md

### Effective Usage

✓ **Phone screens first** - even for strong candidates (saves time)
✓ **Print evaluation forms** - easier than typing during interview
✓ **Brief interviewers beforehand** - review standardized questions
✓ **Take notes during interviews** - support your ratings with evidence
✓ **Be consistent** - don't deviate from standardized questions

---

## When to Use This Skill

**Trigger when user requests:**
- "Generate phone screen script"
- "Create interview guide"
- "I need an evaluation form"
- "Reference check template"
- "Interview materials for [position]"
- "Hiring documents for [candidate]"

**Trigger phrase examples:**
- "Make interview materials"
- "Prepare for phone screen with [candidate]"
- "Generate forms for upcoming interviews"
- "Need reference check script"

---

## References & Resources

For detailed templates and question banks:
- `templates/phone-screen-template.md` - Base phone screen structure
- `templates/interview-guide-template.md` - Base interview guide structure
- `templates/evaluation-form-template.md` - Base evaluation form structure
- `templates/reference-check-template.md` - Base reference check structure
- `references/question-banks.md` - Role-specific question library

For candidate evaluation:
- Use `recruiting-evaluation` skill for Stage 1 (resume screening) and Stage 2 (final decision)
- This skill generates the TOOLS for evaluation
- recruiting-evaluation makes the DECISIONS

---

## Customization

All materials can be customized for:

**Your organization:**
- Add mission statement to interview guides
- Include organizational values in assessment
- Customize branding and language
- Add required legal disclosures

**Specific roles:**
- Technical roles: add coding exercises, technical assessments
- Leadership roles: add case studies, strategic thinking questions
- Creative roles: add portfolio reviews
- Remote roles: add virtual work and communication questions

**To customize:**
- Modify templates in `templates/` folder
- Add role-specific questions to `references/question-banks.md`
- Adjust competencies based on job description

