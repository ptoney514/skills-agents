#!/bin/bash

# Skill Validation Script
# Validates all SKILL.md files against Anthropic requirements

# Note: Not using 'set -e' so we can continue validation even if individual checks fail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Counters
TOTAL_SKILLS=0
PASSED_SKILLS=0
FAILED_SKILLS=0
WARNING_SKILLS=0

# Output file
REPORT_FILE="validation-report.md"
echo "# Skill Validation Report" > "$REPORT_FILE"
echo "Date: $(date '+%Y-%m-%d %H:%M:%S')" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

# Function to check YAML frontmatter
check_frontmatter() {
    local file=$1
    local skill_name=$2
    local errors=0
    local warnings=0

    echo "Checking: $skill_name"
    echo "## $skill_name" >> "$REPORT_FILE"
    echo "" >> "$REPORT_FILE"

    # Check if file starts with ---
    first_line=$(head -n 1 "$file")
    if [ "$first_line" != "---" ]; then
        echo -e "${RED}  ✗ YAML frontmatter must start on line 1 with '---'${NC}"
        echo "- ❌ YAML frontmatter must start on line 1 with '---'" >> "$REPORT_FILE"
        ((errors++))
    else
        echo -e "${GREEN}  ✓ Frontmatter starts correctly${NC}"
    fi

    # Extract frontmatter (between first and second ---)
    frontmatter=$(awk '/^---$/{i++}i==1{next}i==2{exit}1' "$file")

    # Check for required fields: name, description
    if ! echo "$frontmatter" | grep -q "^name:"; then
        echo -e "${RED}  ✗ Missing required 'name' field${NC}"
        echo "- ❌ Missing required 'name' field" >> "$REPORT_FILE"
        ((errors++))
    fi

    if ! echo "$frontmatter" | grep -q "^description:"; then
        echo -e "${RED}  ✗ Missing required 'description' field${NC}"
        echo "- ❌ Missing required 'description' field" >> "$REPORT_FILE"
        ((errors++))
    fi

    # Extract name value
    name_value=$(echo "$frontmatter" | grep "^name:" | sed 's/^name: *//' | tr -d '"' | tr -d "'")

    if [ -n "$name_value" ]; then
        # Check name length (max 64 characters)
        name_length=${#name_value}
        if [ $name_length -gt 64 ]; then
            echo -e "${RED}  ✗ Name exceeds 64 characters ($name_length)${NC}"
            echo "- ❌ Name exceeds 64 characters ($name_length)" >> "$REPORT_FILE"
            ((errors++))
        else
            echo -e "${GREEN}  ✓ Name length OK ($name_length chars)${NC}"
        fi

        # Check name format (lowercase letters, numbers, hyphens only)
        if ! echo "$name_value" | grep -qE '^[a-z0-9-]+$'; then
            echo -e "${RED}  ✗ Name must contain only lowercase letters, numbers, and hyphens${NC}"
            echo "- ❌ Name contains invalid characters (must be lowercase letters, numbers, hyphens only)" >> "$REPORT_FILE"
            echo "  Current: '$name_value'" >> "$REPORT_FILE"
            ((errors++))
        else
            echo -e "${GREEN}  ✓ Name format valid${NC}"
        fi

        # Check for reserved words
        if echo "$name_value" | grep -qiE 'anthropic|claude'; then
            echo -e "${RED}  ✗ Name contains reserved word (anthropic/claude)${NC}"
            echo "- ❌ Name contains reserved word (anthropic/claude)" >> "$REPORT_FILE"
            ((errors++))
        fi
    fi

    # Extract description value (handles multi-line)
    description=$(echo "$frontmatter" | awk '/^description:/{flag=1; gsub(/^description: */, ""); print; next} flag && /^[a-z-]+:/{flag=0} flag')

    if [ -n "$description" ]; then
        # Check description length (max 1024 characters)
        desc_length=${#description}
        if [ $desc_length -gt 1024 ]; then
            echo -e "${RED}  ✗ Description exceeds 1024 characters ($desc_length)${NC}"
            echo "- ❌ Description exceeds 1024 characters ($desc_length)" >> "$REPORT_FILE"
            ((errors++))
        else
            echo -e "${GREEN}  ✓ Description length OK ($desc_length chars)${NC}"
        fi

        # Check for XML tags
        if echo "$description" | grep -qE '<[^>]+>'; then
            echo -e "${RED}  ✗ Description contains XML tags${NC}"
            echo "- ❌ Description contains XML tags" >> "$REPORT_FILE"
            ((errors++))
        fi

        # Check for reserved words
        if echo "$description" | grep -qiE 'anthropic|claude'; then
            echo -e "${YELLOW}  ⚠ Description contains 'anthropic' or 'claude' - verify this is intentional${NC}"
            echo "- ⚠️ Description contains 'anthropic' or 'claude' - verify intentional" >> "$REPORT_FILE"
            ((warnings++))
        fi

        # Check description quality (basic heuristics)
        if echo "$description" | grep -qiE '^(helps with|works with|assists)'; then
            echo -e "${YELLOW}  ⚠ Description starts with generic phrase${NC}"
            echo "- ⚠️ Description uses generic opening (consider being more specific)" >> "$REPORT_FILE"
            ((warnings++))
        fi

        # Check if description is too short (less than 50 chars suggests it might be too vague)
        if [ $desc_length -lt 50 ]; then
            echo -e "${YELLOW}  ⚠ Description is quite short ($desc_length chars) - consider adding more detail${NC}"
            echo "- ⚠️ Description is short - consider adding trigger context and specific use cases" >> "$REPORT_FILE"
            ((warnings++))
        fi
    else
        echo -e "${RED}  ✗ Description is empty${NC}"
        echo "- ❌ Description is empty" >> "$REPORT_FILE"
        ((errors++))
    fi

    # Check for tabs in YAML (should use spaces only)
    if grep -qP '\t' "$file" 2>/dev/null || grep -q "$(printf '\t')" "$file"; then
        echo -e "${YELLOW}  ⚠ File contains tabs (YAML should use spaces only)${NC}"
        echo "- ⚠️ File contains tabs (YAML should use spaces only)" >> "$REPORT_FILE"
        ((warnings++))
    fi

    echo "" >> "$REPORT_FILE"

    # Return status
    if [ $errors -gt 0 ]; then
        return 2  # Failed
    elif [ $warnings -gt 0 ]; then
        return 1  # Warnings
    else
        return 0  # Passed
    fi
}

# Main validation loop
echo -e "${BLUE}=== Skill Validation ===${NC}"
echo ""

for skill_file in skills/*/SKILL.md; do
    if [ -f "$skill_file" ]; then
        ((TOTAL_SKILLS++))
        skill_name=$(basename "$(dirname "$skill_file")")

        check_frontmatter "$skill_file" "$skill_name"
        status=$?

        if [ $status -eq 0 ]; then
            echo -e "${GREEN}  ✓ PASSED${NC}"
            ((PASSED_SKILLS++))
        elif [ $status -eq 1 ]; then
            echo -e "${YELLOW}  ⚠ PASSED (with warnings)${NC}"
            ((WARNING_SKILLS++))
        else
            echo -e "${RED}  ✗ FAILED${NC}"
            ((FAILED_SKILLS++))
        fi
        echo ""
    fi
done

# Summary
echo -e "${BLUE}=== Validation Summary ===${NC}"
echo "Total Skills: $TOTAL_SKILLS"
echo -e "${GREEN}Passed: $PASSED_SKILLS${NC}"
echo -e "${YELLOW}Warnings: $WARNING_SKILLS${NC}"
echo -e "${RED}Failed: $FAILED_SKILLS${NC}"
echo ""
echo "Full report saved to: $REPORT_FILE"

# Add summary to report
echo "## Summary" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"
echo "- **Total Skills**: $TOTAL_SKILLS" >> "$REPORT_FILE"
echo "- **Passed**: $PASSED_SKILLS" >> "$REPORT_FILE"
echo "- **Warnings**: $WARNING_SKILLS" >> "$REPORT_FILE"
echo "- **Failed**: $FAILED_SKILLS" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

if [ $FAILED_SKILLS -gt 0 ]; then
    echo -e "${RED}Some skills failed validation. Please review the report.${NC}"
    exit 1
elif [ $WARNING_SKILLS -gt 0 ]; then
    echo -e "${YELLOW}All skills passed but some have warnings. Consider reviewing.${NC}"
    exit 0
else
    echo -e "${GREEN}All skills passed validation!${NC}"
    exit 0
fi
