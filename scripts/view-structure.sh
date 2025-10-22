#!/bin/bash
# View Structure Script
# Displays the skills-agents folder structure

# Get the script's directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
WORKSPACE_DIR="$(dirname "$SCRIPT_DIR")"

echo "📁 Skills-Agents Workspace Structure"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Check if tree command is available
if command -v tree &> /dev/null; then
    # Use tree command with nice formatting
    tree -L 3 -a --dirsfirst "$WORKSPACE_DIR"
else
    # Fallback to find command
    echo "Location: $WORKSPACE_DIR"
    echo ""
    find "$WORKSPACE_DIR" -maxdepth 3 -not -path '*/\.*' | \
        sed "s|$WORKSPACE_DIR|.|" | \
        sort | \
        sed 's|[^/]*/ |  |g'
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "🔗 Claude Code Skills (symlinks):"
ls -la ~/.claude/skills/ 2>/dev/null | grep '^l' | awk '{print "   " $9 " -> " $11}' || echo "   (none)"
echo ""
