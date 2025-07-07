#!/bin/bash

set -e

PR_NUMBER=$(jq -r .pull_request.number "$GITHUB_EVENT_PATH")
AI_ANALYSIS=$(jq -r '.analysis' diff_response.json)
COST_ESTIMATION=$(jq -r '.analysis' infra_response.json)

# Create comment markdown
{
  echo "### 🤖 AI Code Review Suggestion:"
  echo "$AI_ANALYSIS"
  echo ""
  echo "### 💰 Estimated Infra Cost Impact:"
  echo "$COST_ESTIMATION"
} > comment.md

# Post comment on PR
gh pr comment "$PR_NUMBER" --body-file comment.md

