#!/bin/bash

# Lyra Prompt Optimizer Installation Script
# This script installs the lyra-prompt-optimizer skill for Claude Code

set -e

echo "=================================="
echo "Lyra Prompt Optimizer Installer"
echo "=================================="
echo ""

# Determine the skills directory based on OS
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    # Windows
    SKILLS_DIR="$USERPROFILE/.claude/skills"
else
    # macOS and Linux
    SKILLS_DIR="$HOME/.claude/skills"
fi

SKILL_NAME="lyra-prompt-optimizer"
INSTALL_PATH="$SKILLS_DIR/$SKILL_NAME"

echo "Target installation directory:"
echo "$INSTALL_PATH"
echo ""

# Create skills directory if it doesn't exist
if [ ! -d "$SKILLS_DIR" ]; then
    echo "Creating Claude skills directory..."
    mkdir -p "$SKILLS_DIR"
fi

# Check if skill already exists
if [ -d "$INSTALL_PATH" ]; then
    echo "⚠️  Skill already exists at $INSTALL_PATH"
    read -p "Do you want to overwrite it? (y/N): " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Installation cancelled."
        exit 0
    fi
    echo "Removing existing installation..."
    rm -rf "$INSTALL_PATH"
fi

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Copy skill files
echo "Installing skill files..."
mkdir -p "$INSTALL_PATH"
cp -r "$SCRIPT_DIR"/* "$INSTALL_PATH/"

# Remove the install scripts from the installation
rm -f "$INSTALL_PATH/install.sh"
rm -f "$INSTALL_PATH/install.bat"

echo ""
echo "✅ Installation complete!"
echo ""
echo "Skill installed to: $INSTALL_PATH"
echo ""
echo "Verification:"
echo "-------------"
if [ -f "$INSTALL_PATH/SKILL.md" ]; then
    echo "✅ SKILL.md found"
else
    echo "❌ SKILL.md not found"
fi

if [ -f "$INSTALL_PATH/README.md" ]; then
    echo "✅ README.md found"
else
    echo "❌ README.md not found"
fi

if [ -d "$INSTALL_PATH/examples" ]; then
    echo "✅ examples/ directory found"
    EXAMPLE_COUNT=$(ls -1 "$INSTALL_PATH/examples" | wc -l)
    echo "   ($EXAMPLE_COUNT examples installed)"
else
    echo "❌ examples/ directory not found"
fi

if [ -d "$INSTALL_PATH/templates" ]; then
    echo "✅ templates/ directory found"
    TEMPLATE_COUNT=$(ls -1 "$INSTALL_PATH/templates" | wc -l)
    echo "   ($TEMPLATE_COUNT templates installed)"
else
    echo "❌ templates/ directory not found"
fi

echo ""
echo "Next steps:"
echo "1. Restart Claude Code if it's currently running"
echo "2. The skill will be automatically available for use"
echo "3. Try: claude 'Optimize this prompt: Help me write a background check SOP'"
echo ""
echo "For more information, see the README.md file."
echo ""
echo "🎯 Quick Start:"
echo "   - View examples: $INSTALL_PATH/examples/"
echo "   - View templates: $INSTALL_PATH/templates/"
echo "   - Read docs: $INSTALL_PATH/README.md"
echo ""
