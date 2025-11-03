# Job Description Formatter

Transform raw job descriptions, HR documents, and informal drafts into polished, template-compliant job postings for Creighton University and affiliated Jesuit organizations.

## What This Skill Does

This skill reformats job descriptions into standardized posting templates by:
- Extracting information from various input formats (Word/PDF, screenshots, informal notes)
- Applying organization-specific templates and tone
- Ensuring compliance with inclusive language standards
- Organizing content into clear, compelling sections
- Generating professional, ready-to-post job descriptions

## When to Use This Skill

Use this skill when you need to:
- Convert HR job descriptions into public-facing postings
- Reformat job descriptions from other organizations
- Transform informal job notes into professional postings
- Standardize job posting format across your organization
- Create multiple job postings from raw documentation

## Available Templates

### 1. Creighton University Standard (DEFAULT)
- **Use for:** Most Creighton University positions
- **Format:** Comprehensive, professional structure
- **Includes:** Mission statement, extensive qualifications, institutional context
- **Best for:** Leadership roles, faculty positions, strategic hires

### 2. Jesuit Ministry
- **Use for:** Jesuit retreat centers, communities, ministries
- **Format:** Concise, mission-focused
- **Includes:** Explicit Catholic identity requirements, Ignatian Spirituality emphasis
- **Best for:** Ministry positions, retreat center staff, spiritual roles

### 3. Simplified/Internal
- **Use for:** Internal postings, quick announcements
- **Format:** Streamlined, direct
- **Includes:** Essential information only
- **Best for:** Department-specific roles, temporary positions, internal transfers

## Quick Start

1. **Provide your source material:**
   - Upload a job description document (Word, PDF, image)
   - Paste text directly
   - Describe the role informally

2. **Specify the template** (optional):
   - "Use Creighton Standard format"
   - "Format this for a Jesuit ministry position"
   - If you don't specify, the skill will choose based on context

3. **Review the output:**
   - Complete reformatted posting in markdown
   - Ready to copy/paste into your job board
   - Editable if you need adjustments

## Input Requirements

**Minimum information needed:**
- Position title
- Department/organization
- Core responsibilities (at least 3-5)
- Required qualifications
- Location

**Helpful additional information:**
- Reporting relationship
- Salary range
- Preferred qualifications
- Work schedule details
- Application deadline

**Accepted formats:**
- Microsoft Word (.doc, .docx)
- PDF files
- Screenshots/images
- Plain text
- Informal notes or bullet points

## Examples

### Example 1: Formal HR Document → Creighton Standard Posting

**Input:** HR job description with 15 pages of detailed responsibilities, FLSA classifications, and physical requirements

**Output:** 2-page professional posting with:
- Compelling opening paragraph
- 7 key responsibilities (simplified from 30+ HR duties)
- Clear required vs. preferred qualifications
- Creighton mission context
- Application instructions

### Example 2: Informal Notes → Jesuit Ministry Posting

**Input:** Email notes: "Need retreat coordinator, must be Catholic, handle 100+ retreatants/month, plan logistics, $40K-$45K"

**Output:** Professional 1-page posting with:
- Mission-aligned opening
- Organized responsibilities
- Catholic identity requirements
- Ignatian Spirituality emphasis
- Application process

## Batch Processing

Have multiple job descriptions? You can process them all at once:

1. Provide all source files
2. Specify if they all use the same template or need different templates
3. Choose output format:
   - Separate files (one per position)
   - Combined document (all positions together)

## Compliance & Quality

This skill automatically checks for:
- ✅ Inclusive, gender-neutral language
- ✅ ADA-compliant physical requirement descriptions
- ✅ Non-discriminatory qualification statements
- ✅ Appropriate EEO language (if applicable)
- ✅ Clear, bias-free terminology

## Customization

You can request:
- Different tone (more formal, more casual)
- Emphasis on specific aspects (mission, technical skills, leadership)
- Additional sections (benefits, team structure, success metrics)
- Modifications to standard templates

## Tips for Best Results

**Do:**
- Provide as much detail as possible from your source material
- Specify reporting relationships if known
- Include salary range if you want it in the posting
- Mention any special requirements (travel, schedule, certifications)

**Don't worry about:**
- Perfect formatting in your input
- HR jargon or overly formal language
- Missing some details (the skill will ask for critical info)
- Mixed information from multiple sources

## File Locations

**Input files:** Place in `data/inputs/job-description-formatter/`
**Output files:** Generated in `data/outputs/job-description-formatter/`

## Need Help?

Common questions:

**Q: Can I modify the templates?**
A: Yes! Templates are in `references/`. Edit them to match your organization's needs.

**Q: What if critical information is missing?**
A: The skill will flag missing information with `[INSERT: description]` placeholders and ask you for clarification.

**Q: Can I use this for non-Creighton/Jesuit positions?**
A: Yes! The Simplified template works for any organization. You can also customize the standard templates.

**Q: How do I handle multiple positions?**
A: Provide all source materials and specify whether to use the same template for all or different templates per position.

## Version History

- **v1.0** - Initial release with three templates and compliance checking
