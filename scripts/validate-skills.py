#!/usr/bin/env python3

"""
Skill Validation Script
Validates all SKILL.md files against Anthropic requirements
"""

import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple

# ANSI color codes
class Colors:
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[0;34m'
    NC = '\033[0m'  # No Color

class SkillValidator:
    def __init__(self):
        self.total_skills = 0
        self.passed_skills = 0
        self.failed_skills = 0
        self.warning_skills = 0
        self.report = []

    def validate_skill(self, skill_path: Path) -> Tuple[int, List[str]]:
        """
        Validate a single skill file.
        Returns: (status, issues) where status is 0=passed, 1=warnings, 2=failed
        """
        skill_name = skill_path.parent.name
        issues = []
        errors = 0
        warnings = 0

        print(f"Checking: {skill_name}")

        try:
            content = skill_path.read_text()
            lines = content.split('\n')

            # Check if file starts with ---
            if not lines[0].strip() == '---':
                issues.append("❌ YAML frontmatter must start on line 1 with '---'")
                errors += 1
            else:
                print(f"{Colors.GREEN}  ✓ Frontmatter starts correctly{Colors.NC}")

            # Extract frontmatter
            frontmatter_lines = []
            in_frontmatter = False
            frontmatter_end = -1

            for i, line in enumerate(lines):
                if i == 0 and line.strip() == '---':
                    in_frontmatter = True
                    continue
                elif in_frontmatter and line.strip() == '---':
                    frontmatter_end = i
                    break
                elif in_frontmatter:
                    frontmatter_lines.append(line)

            if frontmatter_end == -1:
                issues.append("❌ YAML frontmatter not properly closed with '---'")
                errors += 1

            # Parse frontmatter fields
            frontmatter_text = '\n'.join(frontmatter_lines)

            # Extract name field
            name_match = re.search(r'^name:\s*(.+)$', frontmatter_text, re.MULTILINE)
            if not name_match:
                issues.append("❌ Missing required 'name' field")
                errors += 1
            else:
                name_value = name_match.group(1).strip().strip('"').strip("'")

                # Check name length
                if len(name_value) > 64:
                    issues.append(f"❌ Name exceeds 64 characters ({len(name_value)})")
                    errors += 1
                else:
                    print(f"{Colors.GREEN}  ✓ Name length OK ({len(name_value)} chars){Colors.NC}")

                # Check name format (lowercase letters, numbers, hyphens only)
                if not re.match(r'^[a-z0-9-]+$', name_value):
                    issues.append(f"❌ Name contains invalid characters (must be lowercase letters, numbers, hyphens only)")
                    issues.append(f"  Current: '{name_value}'")
                    errors += 1
                else:
                    print(f"{Colors.GREEN}  ✓ Name format valid: '{name_value}'{Colors.NC}")

                # Check for reserved words
                if re.search(r'\b(anthropic|claude)\b', name_value, re.IGNORECASE):
                    issues.append("❌ Name contains reserved word (anthropic/claude)")
                    errors += 1

            # Extract description field
            desc_match = re.search(r'^description:\s*(.+?)(?=^\w+:|\Z)', frontmatter_text, re.MULTILINE | re.DOTALL)
            if not desc_match:
                issues.append("❌ Missing required 'description' field")
                errors += 1
            else:
                desc_value = desc_match.group(1).strip().strip('"').strip("'")

                # Check description length
                if len(desc_value) > 1024:
                    issues.append(f"❌ Description exceeds 1024 characters ({len(desc_value)})")
                    errors += 1
                else:
                    print(f"{Colors.GREEN}  ✓ Description length OK ({len(desc_value)} chars){Colors.NC}")

                # Check for XML tags
                if re.search(r'<[^>]+>', desc_value):
                    issues.append("❌ Description contains XML tags")
                    errors += 1

                # Check for reserved words (warning only)
                if re.search(r'\b(anthropic|claude)\b', desc_value, re.IGNORECASE):
                    issues.append("⚠️ Description contains 'anthropic' or 'claude' - verify intentional")
                    warnings += 1

                # Check description quality (heuristics)
                if re.match(r'^(helps with|works with|assists)', desc_value, re.IGNORECASE):
                    issues.append("⚠️ Description starts with generic phrase (consider being more specific)")
                    warnings += 1

                if len(desc_value) < 50:
                    issues.append(f"⚠️ Description is short ({len(desc_value)} chars) - consider adding trigger context")
                    warnings += 1

            # Check for tabs in file (should use spaces only)
            if '\t' in content:
                issues.append("⚠️ File contains tabs (YAML should use spaces only)")
                warnings += 1

        except Exception as e:
            issues.append(f"❌ Error reading file: {str(e)}")
            errors += 1

        # Determine status
        if errors > 0:
            return 2, issues  # Failed
        elif warnings > 0:
            return 1, issues  # Warnings
        else:
            return 0, issues  # Passed

    def run_validation(self, skills_dir: Path) -> int:
        """Run validation on all skills in the directory."""
        print(f"{Colors.BLUE}=== Skill Validation ==={Colors.NC}\n")

        # Find all SKILL.md files
        skill_files = sorted(skills_dir.glob('*/SKILL.md'))

        self.report.append("# Skill Validation Report")
        self.report.append(f"Date: {Path.cwd()}")
        self.report.append("")

        for skill_file in skill_files:
            self.total_skills += 1
            skill_name = skill_file.parent.name

            status, issues = self.validate_skill(skill_file)

            # Add to report
            self.report.append(f"## {skill_name}")
            self.report.append("")
            if issues:
                for issue in issues:
                    self.report.append(f"- {issue}")
            else:
                self.report.append("- ✅ All checks passed")
            self.report.append("")

            # Print status
            if status == 0:
                print(f"{Colors.GREEN}  ✓ PASSED{Colors.NC}\n")
                self.passed_skills += 1
            elif status == 1:
                print(f"{Colors.YELLOW}  ⚠ PASSED (with warnings){Colors.NC}\n")
                self.warning_skills += 1
            else:
                print(f"{Colors.RED}  ✗ FAILED{Colors.NC}\n")
                self.failed_skills += 1

        # Summary
        print(f"{Colors.BLUE}=== Validation Summary ==={Colors.NC}")
        print(f"Total Skills: {self.total_skills}")
        print(f"{Colors.GREEN}Passed: {self.passed_skills}{Colors.NC}")
        print(f"{Colors.YELLOW}Warnings: {self.warning_skills}{Colors.NC}")
        print(f"{Colors.RED}Failed: {self.failed_skills}{Colors.NC}")

        # Add summary to report
        self.report.append("## Summary")
        self.report.append("")
        self.report.append(f"- **Total Skills**: {self.total_skills}")
        self.report.append(f"- **Passed**: {self.passed_skills}")
        self.report.append(f"- **Warnings**: {self.warning_skills}")
        self.report.append(f"- **Failed**: {self.failed_skills}")

        # Save report
        report_file = Path('validation-report.md')
        report_file.write_text('\n'.join(self.report))
        print(f"\nFull report saved to: {report_file}")

        # Return exit code
        if self.failed_skills > 0:
            print(f"{Colors.RED}Some skills failed validation. Please review the report.{Colors.NC}")
            return 1
        elif self.warning_skills > 0:
            print(f"{Colors.YELLOW}All skills passed but some have warnings. Consider reviewing.{Colors.NC}")
            return 0
        else:
            print(f"{Colors.GREEN}All skills passed validation!{Colors.NC}")
            return 0

def main():
    skills_dir = Path('skills')
    if not skills_dir.exists():
        print(f"{Colors.RED}Error: 'skills' directory not found{Colors.NC}")
        return 1

    validator = SkillValidator()
    return validator.run_validation(skills_dir)

if __name__ == '__main__':
    sys.exit(main())
