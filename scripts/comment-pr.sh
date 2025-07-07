#!/bin/bash

AI_ANALYSIS=$(jq -r '.analysis' diff_response.json)
COST_ESTIMATION=$(jq -r '.analysis' infra_response.json)

echo "### 🤖 AI Code Review Suggestion:" > comment.md
echo "$AI_ANALYSIS" >> comment.md
echo "" >> comment.md
echo "### 💰 Estimated Infra Cost Impact:" >> comment.md
echo "$COST_ESTIMATION" >> comment.md

gh pr comment "${PR_NUMBER}" --body-file comment.md

