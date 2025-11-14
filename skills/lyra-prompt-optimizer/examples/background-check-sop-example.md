# Example: Background Check SOP Optimization

This example demonstrates how Lyra optimizes a vague prompt into a precision-engineered request.

## Original Request (Vague)
```
Help me write a new hire background check SOP
```

## Lyra's Analysis

### DECONSTRUCT
- **Core Intent:** Create a Standard Operating Procedure for conducting background checks
- **Key Entities:** Background checks, new hires, SOP format
- **Missing Context:** 
  - Organization type/name
  - Compliance requirements (FCRA, state laws)
  - Background check vendor
  - Target audience (HR team? Hiring managers?)
  - Scope (all positions? specific roles?)

### DIAGNOSE
- **Clarity Issues:** Too generic - "background check" could mean many things
- **Specificity Gaps:** No compliance framework, no vendor info, no process scope
- **Complexity Level:** DETAIL mode required (compliance-heavy, multi-stakeholder process)
- **Compliance Needs:** FCRA critical, state-specific laws, ban-the-box considerations

### DEVELOP
**Techniques to Apply:**
- Role Assignment (HR compliance specialist)
- Context Layering (organization, regulations, vendor)
- Constraint Optimization (SOP structure, sections)
- Output Specification (templates, decision trees)
- Compliance Integration (FCRA requirements embedded)
- Audience Calibration (HR team with operational focus)

## Optimized Prompt

```
You are an HR compliance specialist creating a Standard Operating Procedure 
for Creighton University's new hire background check process.

CONTEXT:
- Organization: Higher education institution (Creighton University)
- Compliance requirements: FCRA, Nebraska state law, Catholic institution values
- Background check vendor: [Specify vendor, e.g., HireRight, Sterling]
- Applicable positions: All full-time staff and faculty positions
- Current process: Post-offer, pre-employment

REQUIRED SOP SECTIONS:
1. Purpose & Scope
2. Roles & Responsibilities (HR, hiring manager, candidate)
3. Process Steps:
   - When background check is initiated (conditional offer stage)
   - Required candidate authorizations and disclosures (FCRA compliance)
   - Types of checks conducted (criminal, education, employment verification)
   - Timeline expectations (standard: 5-7 business days)
   - Adverse action procedures (pre-adverse, final adverse letters)
4. Special Considerations:
   - Ban-the-box compliance
   - Position-specific requirements (working with minors, financial roles)
   - International candidates
5. Documentation & Record Retention
6. Exception Handling (delayed results, concerns flagged)
7. Related Policies (drug testing, reference checks)

OUTPUT FORMAT:
- Professional SOP format with numbered sections
- Include decision trees for adverse action scenarios
- Add compliance callout boxes for legal requirements
- Provide email templates for candidate communication
- Maximum 4-5 pages, scannable with clear headers
- Include version control footer and approval signature block

TONE: Professional, compliance-focused, operationally clear
Assume audience has basic HR knowledge but needs step-by-step guidance.
```

## Key Improvements Made

✅ **Added Organization Context**
- Specified Creighton University (higher education)
- Noted Catholic institution values (relevant for culture/mission fit)

✅ **Embedded Compliance Frameworks**
- FCRA requirements explicitly mentioned
- Nebraska state law included
- Ban-the-box considerations added

✅ **Defined SOP Structure**
- 7 required sections clearly outlined
- Each section has specific sub-components
- Operational clarity with concrete elements

✅ **Added Practical Components**
- Decision trees for adverse actions
- Email templates for communication
- Timeline expectations (5-7 days)

✅ **Specified Output Format**
- Length constraint (4-5 pages)
- Visual elements (callout boxes, decision trees)
- Version control and approval sections
- Professional formatting expectations

✅ **Calibrated for Audience**
- Tone: Professional, compliance-focused
- Assumption: Basic HR knowledge
- Focus: Step-by-step operational guidance

## Techniques Applied

1. **Role Assignment:** "HR compliance specialist"
2. **Context Layering:** Organization type, compliance requirements, vendor specifics
3. **Constraint-Based Precision:** Exact SOP sections, length limits, format requirements
4. **Output Specification:** Decision trees, templates, callout boxes
5. **Compliance Integration:** FCRA, state laws, ban-the-box embedded
6. **Audience Calibration:** Professional tone for HR audience

## Expected Results

### What You'll Get:
A comprehensive, compliance-ready SOP that includes:
- Clear purpose statement and scope definition
- Detailed role assignments (HR, hiring manager, candidate)
- Step-by-step process workflow with decision points
- FCRA-compliant adverse action procedures with template letters
- Position-specific requirements (e.g., working with minors)
- International candidate considerations
- Record retention guidelines
- Exception handling procedures
- Professional formatting ready for immediate use

### Time Saved:
- **Original (vague prompt):** 30-40 minutes of back-and-forth + 3-5 iterations
- **Optimized:** 5-10 minutes to customize and get final output on first try

### Quality Improvement:
- **Before:** Generic SOP template requiring heavy customization
- **After:** Organization-specific, compliance-ready, immediately implementable

## Pro Tips for Further Refinement

🎯 **If you have more context:**
- Specify your actual background check vendor for vendor-specific instructions
- Include your organization's standard timeline (if different from 5-7 days)
- Add state-specific requirements if you operate in multiple states
- Include links to your existing related policies

🎯 **For additional sections:**
- Request a separate "FAQs for Hiring Managers" section
- Add a "Quick Reference Flowchart" for visual learners
- Include a "Common Mistakes to Avoid" section

🎯 **For variations:**
- Create separate SOPs for faculty vs. staff if processes differ
- Add appendices for state-specific compliance requirements
- Include a "What's Changed" section if updating an existing SOP

## Use This Pattern For:
- Onboarding SOPs
- Performance management procedures
- Leave administration processes
- Accommodation request procedures
- Any compliance-heavy HR process requiring step-by-step clarity

---

*This example demonstrates the power of moving from vague to precise. The optimized prompt delivers usable, compliant output on the first attempt.*
