# Recruiting Materials Skill

Generate professional, standardized hiring documents for your recruitment process.

## What This Skill Does

The **recruiting-materials** skill creates customized interview materials that ensure fair, consistent candidate evaluation:

- **Phone Screen Scripts** - 30-minute structured phone conversations
- **Interview Guides** - Comprehensive guides for in-person/virtual interviews
- **Interview Evaluation Forms** - Standardized 1-10 rating forms (50% of final decision)
- **Reference Check Guides** - Professional reference check scripts (25% of final decision)

All materials clearly distinguish between **standardized questions** (same for all candidates) and **candidate-specific questions** (tailored to individual concerns).

## Why Use This Skill

**Consistency:** Same core questions for every candidate ensures fair comparison

**Legal Compliance:** Standardized approach reduces bias and legal risk

**Integration:** Works seamlessly with recruiting-evaluation skill's two-stage process

**Efficiency:** Generate complete interview packages in minutes instead of hours

**Quality:** Professional, well-structured materials improve interview effectiveness

## Quick Start

### Generate Phone Screen Script

```
"Generate phone screen script for Sarah Johnson for Campus Minister position. 
She scored 82 in Stage 1. Verification questions: 
1) Limited Ignatian spirituality experience 
2) No graduate student ministry background"
```

### Generate Interview Guide

```
"Create interview guide for Campus Minister position. 
Key competencies: pastoral care, community building, program development, 
Ignatian spirituality, interfaith engagement."
```

### Generate Evaluation Form

```
"Generate interview evaluation form for Campus Minister position 
with 5 core competencies."
```

### Generate Reference Check Guide

```
"Create reference check guide for Sarah Johnson, checking with 
her previous supervisor at University of Wisconsin."
```

### Batch Mode

```
"Generate interview materials for all 4 finalists: 
Sarah Johnson, Michael Chen, Rebecca Williams, David Martinez"
```

## How It Works

### Single Candidate Mode

Request materials for one candidate at a time:

1. Provide job title and candidate name
2. Include any Stage 1 verification questions (from recruiting-evaluation)
3. Receive customized materials with standard + candidate-specific sections

### Batch Mode

Generate materials for multiple candidates:

1. Provide list of candidate names and role
2. Provide individual verification questions for each (if applicable)
3. Receive complete set for each candidate
4. **All candidates get same standardized questions** - only verification sections differ

## Material Descriptions

### 1. Phone Screen Scripts

**Purpose:** Quick 30-minute filter before investing in full interviews

**Structure:**
- Opening script and rapport building
- 5 standard assessment questions (ALL candidates)
- Candidate-specific verification questions (THIS candidate only)
- Logistics (salary, location, availability)
- Role overview
- Closing and post-call evaluation

**Use case:** After Stage 1 resume screening recommends phone screen (70+ score)

### 2. Interview Guides

**Purpose:** Comprehensive guides for 60-90 minute interviews

**Structure:**
- Pre-interview preparation checklist
- Time-structured agenda (Introduction → Experience → Competencies → Questions)
- 5-7 competency-based questions (ALL candidates)
- Candidate-specific verification questions (THIS candidate only)
- Cultural fit assessment
- Post-interview reminders

**Use case:** After successful phone screen, before scheduling interviews

### 3. Interview Evaluation Forms

**Purpose:** Standardized rating forms that contribute **50% to final hiring decision**

**Structure:**
- 1-10 rating scale for each core competency
- Overall interview performance rating (converts to 0-100 for Stage 2)
- Red flags checklist
- Strengths and concerns documentation
- Hiring recommendation with detailed rationale

**Use case:** Given to interviewers before interviews, completed immediately after

**Critical:** This form feeds directly into recruiting-evaluation skill's Stage 2 scoring

### 4. Reference Check Guides

**Purpose:** Validate qualifications with 2-3 professional references

**Structure:**
- Opening script and relationship verification
- Standard performance questions (ALL references)
- Competency validation questions
- **Critical "would rehire?" question**
- Candidate-specific verification (THIS candidate only)
- Post-call evaluation and rating (1-10)

**Use case:** For finalist candidates before final hiring decision

**Critical:** Reference scores contribute **25% to Stage 2 final decision**

## Key Features

### Clear Labeling

All materials use visual indicators:

**🔵 STANDARD SECTIONS** - Same for ALL candidates (ensures fairness)

**🟡 CANDIDATE-SPECIFIC SECTIONS** - Unique to THIS candidate (addresses concerns)

### Stage 2 Integration

Materials are designed to feed into recruiting-evaluation skill's final decision:

| Input | Weight | Source |
|-------|--------|--------|
| Resume Score | 25% | recruiting-evaluation Stage 1 |
| Interview Rating | **50%** | Evaluation Form (this skill) |
| Reference Checks | 25% | Reference Guide (this skill) |

### Legal Compliance

- Standardized questions reduce bias
- Same core questions for all candidates
- Job-related focus only
- Protected characteristics avoided
- Documentation supports defensible decisions

## Integration with Recruiting-Evaluation Skill

This skill works hand-in-hand with recruiting-evaluation:

**Typical Workflow:**

1. User provides resume → **recruiting-evaluation** runs Stage 1
2. Stage 1 outputs candidate-specific verification questions
3. User requests phone screen → **recruiting-materials** generates script
4. After phone screen passes → **recruiting-materials** generates interview guide + evaluation form
5. After interview → Interviewer completes evaluation form
6. User requests reference check → **recruiting-materials** generates guide
7. User provides completed forms → **recruiting-evaluation** runs Stage 2 with all inputs

## Best Practices

### For Fair Hiring

✓ Use the same standardized questions for all candidates
✓ Only vary candidate-specific sections based on resume gaps
✓ Rate against requirements, not against other candidates
✓ Document specific examples for all ratings
✓ Complete forms immediately while details are fresh

### For Efficiency

✓ Generate all materials after Stage 1 evaluation
✓ Print evaluation forms (easier than typing during interview)
✓ Brief interviewers on standardized questions beforehand
✓ Keep all materials for 1-2 years for compliance

### For Quality

✓ Check 2-3 references minimum (not just one)
✓ Use verification questions strategically (only what you need)
✓ Take detailed notes during interviews and reference calls
✓ Be consistent - don't deviate from standardized questions

## File Naming Convention

When saving generated materials:

```
[Position]_[MaterialType]_[CandidateName]_[Date].md
```

Examples:
- `CampusMinister_PhoneScreen_SarahJohnson_2025-10-30.md`
- `AssocDirector_InterviewGuide_MichaelChen_2025-11-01.md`
- `CampusMinister_EvaluationForm_Template_2025-10-30.md`

## Customization

All templates can be customized for your organization:

**Organizational Branding:**
- Add mission statement to interview guides
- Include organizational values in assessments
- Customize language and tone
- Add required legal disclosures

**Role-Specific Adjustments:**
- Technical roles: add coding exercises
- Leadership roles: add case studies
- Creative roles: add portfolio reviews
- Remote roles: add virtual work questions

**To Customize:**
- Modify templates in `templates/` folder
- Add role-specific questions to `references/question-banks.md`
- Adjust competencies based on job descriptions

## Common Use Cases

### Use Case 1: New Position Opening

**Scenario:** You're hiring for a new Campus Minister position

**Steps:**
1. Run Stage 1 evaluation on all applications (recruiting-evaluation skill)
2. For candidates scoring 70+: "Generate phone screen scripts for [list of names]"
3. After phone screens: "Generate interview guides and evaluation forms for [finalists]"
4. After interviews: "Generate reference check guides for [top 2 candidates]"
5. Run Stage 2 evaluation with completed forms (recruiting-evaluation skill)

### Use Case 2: Comparing Multiple Finalists

**Scenario:** You have 3 strong finalists and need to choose

**Steps:**
1. Generate interview guides for all 3 (ensures same questions)
2. Provide evaluation forms to all interviewers
3. Collect completed forms
4. Generate reference checks for all 3
5. Use recruiting-evaluation Stage 2 to compare with standardized scores

### Use Case 3: Addressing Specific Concerns

**Scenario:** Candidate has strong resume but limited experience in one key area

**Steps:**
1. Stage 1 identifies gap (e.g., "limited Ignatian spirituality experience")
2. Generate phone screen with verification questions about this gap
3. If passes phone screen, generate interview guide with deeper probing on this area
4. Generate reference check guide with specific questions to validate
5. Stage 2 evaluation weighs all inputs (interview 50%, references 25%)

## Skill Files

This skill includes:

- **SKILL.md** - Main instructions for Claude
- **README.md** - This user-facing documentation
- **templates/** - Base templates for all four material types
  - phone-screen-template.md
  - interview-guide-template.md
  - evaluation-form-template.md
  - reference-check-template.md
- **references/** - Supporting resources
  - question-banks.md - Role-specific question library

## Tips & Tricks

**For Phone Screens:**
- Schedule 30 minutes (not more - it's a filter, not an interview)
- Focus on dealbreakers: interest, availability, compensation alignment
- Use to verify top Stage 1 concerns

**For Interviews:**
- 60-90 minutes is ideal
- Use STAR format (Situation, Task, Action, Result)
- Listen 80%, talk 20%
- Take detailed notes for evaluation form

**For Evaluation Forms:**
- Complete within 1 hour while details are fresh
- Use specific examples to support ratings
- Be honest - hiring the wrong person is expensive
- Your gut matters - if something feels off, note it

**For Reference Checks:**
- Call don't email (you learn more from tone and hesitation)
- The "would rehire?" question is the most critical
- Any hesitation is a red flag
- Check 2-3 references minimum (not just one)

## Support & Questions

For issues with this skill:
- Check that job description and competencies are clearly specified
- Ensure candidate-specific questions are provided if needed
- Review examples in SKILL.md for proper request format
- Consult question-banks.md for role-specific question ideas

For questions about the evaluation process:
- See recruiting-evaluation skill for Stage 1 & 2 scoring
- See references/evaluation-framework.md in recruiting-evaluation skill

## Version History

- **v1.0** (2025-10-30) - Initial creation
  - Four material types: phone screen, interview guide, evaluation form, reference check
  - Standardized vs. candidate-specific question labeling
  - Integration with recruiting-evaluation skill Stage 2
  - Comprehensive question banks by role type
