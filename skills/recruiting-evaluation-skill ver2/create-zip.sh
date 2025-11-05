#!/bin/bash

# Recruiting Evaluation Skill - ZIP Creation Script
# This creates a properly formatted ZIP file for upload to Claude.ai

echo "Creating recruiting-evaluation-skill.zip..."

# Navigate to the parent directory
cd /Users/pernelltoney/Documents

# Create the ZIP file
zip -r recruiting-evaluation-skill.zip recruiting-evaluation-skill/ \
    -x "*.DS_Store" \
    -x "recruiting-evaluation-skill/.git/*" \
    -x "recruiting-evaluation-skill/create-zip.sh"

echo "✅ ZIP file created: /Users/pernelltoney/Documents/recruiting-evaluation-skill.zip"
echo ""
echo "📤 Next steps:"
echo "1. Go to Claude.ai Settings > Features"
echo "2. Upload recruiting-evaluation-skill.zip"
echo "3. Start using it in conversations!"
echo ""
echo "🧪 Test command:"
echo "   'Evaluate 3 candidates for Senior Developer role...'"
