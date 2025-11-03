---
name: job-description-formatter
description: Reformat job descriptions into standardized posting templates for Creighton University and affiliated Jesuit organizations. Use when users need to convert raw job descriptions, HR documents, or informal drafts into polished job postings using specific organizational templates. Supports multiple template formats including Creighton University Standard, Jesuit Ministry, and Simplified/Internal formats.
---

# Job Description Formatter

Transform raw job descriptions into polished, template-compliant postings for Creighton University and Jesuit organizations.

## Quick Start

When the user provides a job description and requests reformatting:

1. **Read the appropriate template** from `references/` based on user request or infer from context:
   - `template_creighton_standard.md` - For Creighton University positions (DEFAULT)
   - `template_jesuit_ministry.md` - For Jesuit retreat centers, communities, ministries
   - `template_simplified.md` - For internal postings or quick announcements

2. **Extract information** using guidelines in `references/extraction_guidelines.md`

3. **Review compliance** using `references/compliance_guidelines.md` to ensure inclusive language and legal compliance

4. **Apply the template** structure and tone to create the reformatted posting

5. **Present the result** and offer to make adjustments

## Template Selection Guide

**Use Creighton Standard when:**
- Position is a Creighton University employee role
- User doesn't specify format
- Professional, comprehensive posting needed
- Position has leadership or strategic importance

**Use Jesuit Ministry when:**
- Position is at a Jesuit retreat center, community, or ministry
- User references Jesuit organizations outside Creighton
- Posting needs mission/spirituality emphasis
- More concise format appropriate

**Use Simplified when:**
- Internal posting requested
- Quick turnaround needed
- Less formal context
- User explicitly requests streamlined format

## Special Handling

### Multiple Input Formats
- **Word/PDF documents**: Extract all text, identify sections
- **Images/Screenshots**: Carefully transcribe visible content
- **Informal notes**: Organize and structure missing elements
- **Partial information**: Note gaps and ask clarifying questions

### Additional Details Not in Original
When user provides additional responsibilities or details not in the source document:
- Integrate naturally into appropriate sections
- Maintain consistent tone and style
- Prioritize by importance

### Ambiguous Information
If critical information is unclear or missing:
- Note the gap in brackets: `[INSERT DEPARTMENT]`
- Ask user for clarification before finalizing
- Suggest reasonable defaults when appropriate

### Batch Processing
When user provides multiple job descriptions:

1. **Confirm template strategy:**
   - Ask if all positions use the same template
   - Or allow different templates per position based on context

2. **Process systematically:**
   - Handle one position at a time
   - Maintain consistent quality across all postings
   - Track which positions have been completed

3. **Output format options:**
   - Separate markdown files (one per position)
   - Combined document with clear section breaks
   - Ask user preference if not specified

4. **Efficiency tips:**
   - If all use same template, confirm once and apply to all
   - Flag common issues across multiple postings
   - Summarize batch completion at end

### Job Requirements Definition
When user needs help defining job requirements before drafting the posting:

- Use `references/job-requirements-template.md` to help structure and capture requirements
- This template helps identify must-have vs. nice-to-have qualifications
- Creates clear knockout criteria and evaluation framework
- Can be completed first, then used as input for formatting the final posting

## Output Format

Always provide:
1. Complete reformatted posting in markdown
2. Brief note identifying which template was used
3. Offer to adjust or use different template if needed

Do not include:
- Meta-commentary about the reformatting process
- Detailed explanations unless requested
- Multiple template versions unless asked

## Quality Standards

Ensure every posting includes:
- Clear, specific position title
- Compelling opening that positions the role
- Well-organized responsibilities
- Distinct required vs. preferred qualifications
- Clear application instructions
- Appropriate organizational context

Maintain:
- Professional, engaging tone
- Active voice
- Inclusive language
- Consistent formatting
- Appropriate level of detail for template type

## Compliance & Inclusive Language

**ALWAYS review postings against `references/compliance_guidelines.md` for:**

### Legal Compliance
- Include EEO statement if required
- Use ADA-compliant language for physical requirements ("with or without reasonable accommodation")
- Avoid age-discriminatory terms (e.g., "recent graduate," "digital native")
- Check religious organization exemptions are appropriately applied

### Inclusive Language
- Use gender-neutral language throughout (avoid he/she, use "they" or "the candidate")
- Avoid gender-coded terms (e.g., "aggressive" → "results-driven")
- Ensure requirements are truly essential (e.g., "native English speaker" → "strong English communication skills")
- Check for ableist language and physical requirement assumptions

### Red Flags to Fix
- "Culture fit" → "Values alignment with [specific values]"
- Unnecessary degree requirements → Add "or equivalent experience"
- "Rockstar," "ninja," "guru" → Use professional, specific descriptions
- Masculine or feminine-coded language clusters → Balance or use neutral terms

### Quality Check Before Finalizing
- [ ] Gender-neutral language throughout
- [ ] Physical requirements include accommodation language
- [ ] No age-coded terms
- [ ] Required vs. preferred qualifications are truly essential vs. nice-to-have
- [ ] EEO statement included if applicable
- [ ] Religious requirements justified (ministry positions only)
- [ ] Reviewed for unconscious bias

**See `references/compliance_guidelines.md` for detailed guidance and examples.**
