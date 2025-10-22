#!/bin/bash
# Skills-Agents Setup Script
# Sets up the folder structure and symlinks for Claude Code skills

set -e

echo "🚀 Setting up skills-agents workspace..."

# Get the script's directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
WORKSPACE_DIR="$(dirname "$SCRIPT_DIR")"

echo "📁 Workspace: $WORKSPACE_DIR"

# Create folder structure
echo "📦 Creating folder structure..."
mkdir -p "$WORKSPACE_DIR/skills"
mkdir -p "$WORKSPACE_DIR/data/inputs/position-review"
mkdir -p "$WORKSPACE_DIR/data/outputs/position-review"
mkdir -p "$WORKSPACE_DIR/scripts"

# Create ~/.claude/skills if it doesn't exist
echo "🔗 Setting up Claude Code skills directory..."
mkdir -p ~/.claude/skills

# Sync skills
echo "🔄 Syncing skills to Claude Code..."
bash "$SCRIPT_DIR/sync-skills.sh"

echo ""
echo "✅ Setup complete!"
echo ""
echo "📊 View your structure:"
echo "   bash $SCRIPT_DIR/view-structure.sh"
echo ""
echo "📚 Next steps:"
echo "   1. Add input files to: $WORKSPACE_DIR/data/inputs/"
echo "   2. Create new skills in: $WORKSPACE_DIR/skills/"
echo "   3. Run sync-skills.sh after adding new skills"
echo ""
