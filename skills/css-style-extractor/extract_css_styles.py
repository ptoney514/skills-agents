#!/usr/bin/env python3
"""
CSS Style Extractor
Parses CSS files and generates comprehensive style guide documentation.

Usage:
    python extract_css_styles.py <input_css_file> [output_directory]

Example:
    python extract_css_styles.py data/inputs/css-extraction/motherduck__2025-11-14.css
"""

import re
import sys
import os
from datetime import datetime
from pathlib import Path
from collections import defaultdict


class CSSStyleExtractor:
    """Extract and organize CSS styles into structured documentation"""

    def __init__(self, css_content, source_name="Unknown Source"):
        self.css_content = css_content
        self.source_name = source_name
        self.colors = defaultdict(list)
        self.typography = {}
        self.spacing = {}
        self.shadows = {}
        self.border_radius = {}
        self.animations = {}
        self.components = defaultdict(dict)
        self.css_variables = {}

    def extract_all(self):
        """Run all extraction methods"""
        self.extract_css_variables()
        self.extract_colors()
        self.extract_typography()
        self.extract_spacing()
        self.extract_shadows()
        self.extract_border_radius()
        self.extract_animations()
        self.extract_components()

    def extract_css_variables(self):
        """Extract CSS custom properties (variables) from :root"""
        # Match :root { ... } block
        root_pattern = r':root\s*\{([^}]*)\}'
        root_match = re.search(root_pattern, self.css_content, re.DOTALL)

        if root_match:
            root_content = root_match.group(1)
            # Extract all --variable: value pairs
            var_pattern = r'(--[\w-]+)\s*:\s*([^;]+);'
            matches = re.findall(var_pattern, root_content)

            for var_name, var_value in matches:
                self.css_variables[var_name] = var_value.strip()

    def extract_colors(self):
        """Extract color values and organize by category"""
        # Color patterns
        hex_pattern = r'#(?:[0-9a-fA-F]{3}){1,2}\b'
        rgb_pattern = r'rgba?\([^)]+\)'
        hsl_pattern = r'hsla?\([^)]+\)'

        # Extract from CSS variables first
        for var_name, var_value in self.css_variables.items():
            if any(keyword in var_name.lower() for keyword in ['color', 'bg', 'background', 'text', 'border']):
                category = self._categorize_color(var_name)
                self.colors[category].append({
                    'name': var_name,
                    'value': var_value,
                    'source': 'css-variable'
                })

        # Extract hard-coded colors
        all_colors = (
            re.findall(hex_pattern, self.css_content) +
            re.findall(rgb_pattern, self.css_content) +
            re.findall(hsl_pattern, self.css_content)
        )

        # Count frequency to identify recurring colors
        color_freq = defaultdict(int)
        for color in all_colors:
            color_freq[color.lower()] += 1

        # Only include colors that appear multiple times (likely part of system)
        for color, freq in color_freq.items():
            if freq >= 2:  # Appears at least twice
                self.colors['recurring'].append({
                    'value': color,
                    'frequency': freq,
                    'source': 'hard-coded'
                })

    def _categorize_color(self, var_name):
        """Categorize color variable by name"""
        var_lower = var_name.lower()
        if 'primary' in var_lower:
            return 'primary'
        elif 'secondary' in var_lower:
            return 'secondary'
        elif 'accent' in var_lower:
            return 'accent'
        elif any(keyword in var_lower for keyword in ['gray', 'grey', 'neutral']):
            return 'neutrals'
        elif 'success' in var_lower or 'green' in var_lower:
            return 'semantic-success'
        elif 'error' in var_lower or 'danger' in var_lower or 'red' in var_lower:
            return 'semantic-error'
        elif 'warning' in var_lower or 'yellow' in var_lower or 'orange' in var_lower:
            return 'semantic-warning'
        elif 'info' in var_lower or 'blue' in var_lower:
            return 'semantic-info'
        elif 'bg' in var_lower or 'background' in var_lower:
            return 'backgrounds'
        else:
            return 'other'

    def extract_typography(self):
        """Extract font families, sizes, weights, line heights"""
        # Font families
        font_family_pattern = r'font-family\s*:\s*([^;]+);'
        font_families = re.findall(font_family_pattern, self.css_content, re.IGNORECASE)
        if font_families:
            self.typography['families'] = list(set([f.strip() for f in font_families]))

        # Extract from CSS variables
        for var_name, var_value in self.css_variables.items():
            var_lower = var_name.lower()
            if 'font' in var_lower:
                if 'family' in var_lower:
                    self.typography.setdefault('family_vars', {})[var_name] = var_value
                elif 'weight' in var_lower:
                    self.typography.setdefault('weight_vars', {})[var_name] = var_value
                elif 'size' in var_lower or 'text' in var_name:
                    self.typography.setdefault('size_vars', {})[var_name] = var_value
            elif 'leading' in var_lower or 'line-height' in var_lower:
                self.typography.setdefault('line_height_vars', {})[var_name] = var_value

    def extract_spacing(self):
        """Extract spacing values and patterns"""
        for var_name, var_value in self.css_variables.items():
            var_lower = var_name.lower()
            if any(keyword in var_lower for keyword in ['space', 'spacing', 'gap', 'margin', 'padding']):
                self.spacing[var_name] = var_value

    def extract_shadows(self):
        """Extract box-shadow values"""
        # From CSS variables
        for var_name, var_value in self.css_variables.items():
            if 'shadow' in var_name.lower():
                self.shadows[var_name] = var_value

        # Direct box-shadow declarations
        shadow_pattern = r'box-shadow\s*:\s*([^;]+);'
        shadows = re.findall(shadow_pattern, self.css_content, re.IGNORECASE)
        unique_shadows = list(set([s.strip() for s in shadows]))
        if unique_shadows:
            self.shadows['_direct'] = unique_shadows

    def extract_border_radius(self):
        """Extract border-radius values"""
        for var_name, var_value in self.css_variables.items():
            if 'radius' in var_name.lower() or 'rounded' in var_name.lower():
                self.border_radius[var_name] = var_value

    def extract_animations(self):
        """Extract transition and animation properties"""
        for var_name, var_value in self.css_variables.items():
            var_lower = var_name.lower()
            if any(keyword in var_lower for keyword in ['transition', 'duration', 'ease', 'timing']):
                self.animations[var_name] = var_value

    def extract_components(self):
        """Extract component-specific styles (buttons, inputs, cards, etc.)"""
        component_patterns = {
            'button': r'\.(btn|button)[^\{]*\{([^}]+)\}',
            'input': r'\.(input|form-control|field)[^\{]*\{([^}]+)\}',
            'card': r'\.(card|panel)[^\{]*\{([^}]+)\}',
            'nav': r'\.(nav|navigation|menu)[^\{]*\{([^}]+)\}',
        }

        for component_type, pattern in component_patterns.items():
            matches = re.findall(pattern, self.css_content, re.IGNORECASE)
            if matches:
                self.components[component_type] = [
                    {'selector': match[0], 'rules': match[1].strip()}
                    for match in matches[:3]  # Limit to first 3 examples
                ]

    def generate_style_guide(self):
        """Generate markdown style guide"""
        today = datetime.now().strftime("%Y-%m-%d")
        guide = []

        # Header
        guide.append(f"# {self.source_name} Design System Style Guide\n")
        guide.append(f"**Version:** 1.0\n")
        guide.append(f"**Extracted:** {today}\n")
        guide.append(f"**Source:** {self.source_name}\n")
        guide.append(f"**Generated By:** CSS Style Extractor Skill\n")
        guide.append("\n---\n\n")

        # Overview
        guide.append("## Overview\n\n")
        guide.append(f"This style guide was automatically extracted from CSS source files on {today}. ")
        guide.append("It documents the design tokens, color palette, typography, spacing, and component styles ")
        guide.append("found in the source CSS.\n\n")

        # CSS Variables Summary
        if self.css_variables:
            guide.append(f"**Total CSS Variables Detected:** {len(self.css_variables)}\n\n")

        guide.append("---\n\n")

        # Color Palette
        guide.append("## Color Palette\n\n")

        if self.colors:
            color_sections = {
                'primary': 'Primary Colors',
                'secondary': 'Secondary Colors',
                'accent': 'Accent Colors',
                'neutrals': 'Neutrals / Grays',
                'semantic-success': 'Semantic: Success',
                'semantic-error': 'Semantic: Error',
                'semantic-warning': 'Semantic: Warning',
                'semantic-info': 'Semantic: Info',
                'backgrounds': 'Background Colors',
                'recurring': 'Recurring Hard-Coded Colors',
                'other': 'Other Colors'
            }

            for category, title in color_sections.items():
                if category in self.colors and self.colors[category]:
                    guide.append(f"### {title}\n\n")
                    guide.append("```css\n")
                    for color in self.colors[category]:
                        if 'name' in color:
                            guide.append(f"{color['name']}: {color['value']};\n")
                        else:
                            freq_note = f" /* Used {color.get('frequency', '?')}x */" if 'frequency' in color else ""
                            guide.append(f"{color['value']};{freq_note}\n")
                    guide.append("```\n\n")
        else:
            guide.append("_No color system detected in CSS._\n\n")

        guide.append("---\n\n")

        # Typography
        guide.append("## Typography\n\n")

        if self.typography:
            if 'family_vars' in self.typography:
                guide.append("### Font Families\n\n```css\n")
                for var, value in self.typography['family_vars'].items():
                    guide.append(f"{var}: {value};\n")
                guide.append("```\n\n")

            if 'size_vars' in self.typography:
                guide.append("### Font Sizes / Type Scale\n\n```css\n")
                for var, value in sorted(self.typography['size_vars'].items()):
                    guide.append(f"{var}: {value};\n")
                guide.append("```\n\n")

            if 'weight_vars' in self.typography:
                guide.append("### Font Weights\n\n```css\n")
                for var, value in self.typography['weight_vars'].items():
                    guide.append(f"{var}: {value};\n")
                guide.append("```\n\n")

            if 'line_height_vars' in self.typography:
                guide.append("### Line Heights\n\n```css\n")
                for var, value in self.typography['line_height_vars'].items():
                    guide.append(f"{var}: {value};\n")
                guide.append("```\n\n")
        else:
            guide.append("_No typography system detected in CSS._\n\n")

        guide.append("---\n\n")

        # Spacing
        guide.append("## Spacing System\n\n")

        if self.spacing:
            guide.append("```css\n")
            for var, value in sorted(self.spacing.items()):
                guide.append(f"{var}: {value};\n")
            guide.append("```\n\n")
        else:
            guide.append("_No spacing system detected in CSS._\n\n")

        guide.append("---\n\n")

        # Shadows
        guide.append("## Shadows (Elevation System)\n\n")

        if self.shadows:
            guide.append("```css\n")
            for var, value in self.shadows.items():
                if var == '_direct':
                    guide.append("\n/* Direct box-shadow declarations (no variables) */\n")
                    for shadow in value:
                        guide.append(f"box-shadow: {shadow};\n")
                else:
                    guide.append(f"{var}: {value};\n")
            guide.append("```\n\n")
        else:
            guide.append("_No shadow system detected in CSS._\n\n")

        guide.append("---\n\n")

        # Border Radius
        guide.append("## Border Radius\n\n")

        if self.border_radius:
            guide.append("```css\n")
            for var, value in sorted(self.border_radius.items()):
                guide.append(f"{var}: {value};\n")
            guide.append("```\n\n")
        else:
            guide.append("_No border radius system detected in CSS._\n\n")

        guide.append("---\n\n")

        # Animations
        guide.append("## Animations & Transitions\n\n")

        if self.animations:
            guide.append("```css\n")
            for var, value in self.animations.items():
                guide.append(f"{var}: {value};\n")
            guide.append("```\n\n")
        else:
            guide.append("_No animation/transition system detected in CSS._\n\n")

        guide.append("---\n\n")

        # Component Styles
        guide.append("## Component Styles\n\n")

        if self.components:
            for component_type, examples in self.components.items():
                guide.append(f"### {component_type.title()}\n\n")
                for example in examples:
                    guide.append(f"**Selector:** `.{example['selector']}`\n\n```css\n")
                    guide.append(f"{example['rules']}\n```\n\n")
        else:
            guide.append("_No component styles detected._\n\n")

        guide.append("---\n\n")

        # Footer / Notes
        guide.append("## Notes\n\n")
        guide.append("- This style guide was automatically generated from CSS source files.\n")
        guide.append("- Review for accuracy and add usage guidelines as needed.\n")
        guide.append("- CSS variables indicate an intentional design system.\n")
        guide.append("- Hard-coded recurring values may indicate patterns worth systematizing.\n\n")

        guide.append("---\n\n")
        guide.append("**Integration:** This style guide can be used with the `pixel-perfect-designer` agent ")
        guide.append("to generate new UI components that match this design system.\n")

        return "".join(guide)


def main():
    """Main execution function"""
    if len(sys.argv) < 2:
        print("Usage: python extract_css_styles.py <input_css_file> [output_directory]")
        print("\nExample:")
        print("  python extract_css_styles.py data/inputs/css-extraction/motherduck.css")
        sys.exit(1)

    input_file = Path(sys.argv[1])

    if not input_file.exists():
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)

    # Determine output directory
    if len(sys.argv) >= 3:
        output_dir = Path(sys.argv[2])
    else:
        # Default output directory
        output_dir = Path("data/outputs/css-extraction")

    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)

    # Read CSS content
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            css_content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    # Determine source name from filename
    source_name = input_file.stem.split('__')[0].replace('-', ' ').replace('_', ' ').title()

    # Extract styles
    print(f"Extracting styles from: {input_file.name}")
    print(f"Source: {source_name}")

    extractor = CSSStyleExtractor(css_content, source_name)
    extractor.extract_all()

    # Generate style guide
    style_guide = extractor.generate_style_guide()

    # Output filename
    today = datetime.now().strftime("%Y-%m-%d")
    output_filename = f"{source_name.replace(' ', '-')}-Style-Guide__{today}.md"
    output_path = output_dir / output_filename

    # Write output
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(style_guide)
        print(f"\n✅ Style guide generated: {output_path}")
        print(f"\n📊 Summary:")
        print(f"   - CSS Variables: {len(extractor.css_variables)}")
        print(f"   - Color Categories: {len(extractor.colors)}")
        print(f"   - Typography Entries: {len(extractor.typography)}")
        print(f"   - Spacing Entries: {len(extractor.spacing)}")
        print(f"   - Shadows: {len(extractor.shadows)}")
        print(f"   - Components: {len(extractor.components)}")
        print(f"\nNext step: Use this style guide with the pixel-perfect-designer agent!")
    except Exception as e:
        print(f"Error writing output file: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
