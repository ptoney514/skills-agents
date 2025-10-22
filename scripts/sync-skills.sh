#!/bin/bash
# Sync Skills Script
# Creates symlinks from ~/.claude/skills/ to skills in this workspace

set -e

# Get the script's directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
WORKSPACE_DIR="$(dirname "$SCRIPT_DIR")"
SKILLS_DIR="$WORKSPACE_DIR/skills"
CLAUDE_SKILLS_DIR="$HOME/.claude/skills"

echo "🔄 Syncing skills to Claude Code..."
echo "   Source: $SKILLS_DIR"
echo "   Target: $CLAUDE_SKILLS_DIR"
echo ""

# Create ~/.claude/skills if it doesn't exist
mkdir -p "$CLAUDE_SKILLS_DIR"

# Find all skill directories (those containing SKILL.md)
SKILLS_FOUND=0

for skill_path in "$SKILLS_DIR"/*; do
    if [ -d "$skill_path" ] && [ -f "$skill_path/SKILL.md" ]; then
        skill_name=$(basename "$skill_path")
        link_path="$CLAUDE_SKILLS_DIR/$skill_name"

        # Remove existing symlink or directory
        if [ -L "$link_path" ]; then
            echo "   🔗 Updating symlink: $skill_name"
            rm "$link_path"
        elif [ -e "$link_path" ]; then
            echo "   ⚠️  Warning: $skill_name exists but is not a symlink"
            echo "      Please manually remove: $link_path"
            continue
        else
            echo "   ➕ Creating symlink: $skill_name"
        fi

        # Create symlink
        ln -s "$skill_path" "$link_path"
        SKILLS_FOUND=$((SKILLS_FOUND + 1))
    fi
done

echo ""
if [ $SKILLS_FOUND -eq 0 ]; then
    echo "⚠️  No skills found in $SKILLS_DIR"
    echo "   Skills must contain a SKILL.md file"
else
    echo "✅ Synced $SKILLS_FOUND skill(s)"
fi

echo ""
echo "📋 Current skills in Claude Code:"
ls -la "$CLAUDE_SKILLS_DIR" | grep '^l' || echo "   (none)"
echo ""
