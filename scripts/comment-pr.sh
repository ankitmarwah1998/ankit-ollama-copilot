#!/bin/bash

set -e

# Check if response.json exists
if [ ! -f response.json ]; then
  echo "❌ response.json not found"
  exit 1
fi

# Escape newlines for GitHub comment
ESCAPED=$(cat response.json | sed ':a;N;$!ba;s/\n/\\n/g')

# Ensure PR_URL is set
if [ -z "$PR_URL" ]; then
  echo "❌ PR_URL not set"
  exit 1
fi

# Extract repo and PR number
REPO=$(echo "$PR_URL" | awk -F '/' '{print $(NF-3) "/" $(NF-2)}')
PR_NUMBER=$(echo "$PR_URL" | awk -F '/' '{print $NF}')

# Add comment to PR
gh pr comment "$PR_NUMBER" --repo "$REPO" --body "$ESCAPED"

