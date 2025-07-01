#!/bin/bash

set -e

if [ ! -f response.json ]; then
  echo "❌ response.json not found"
  exit 1
fi

# Escape content
ESCAPED=$(cat response.json | sed ':a;N;$!ba;s/"/\\"/g; s/\n/\\n/g')

# Check PR URL
if [ -z "$PR_URL" ]; then
  echo "❌ PR_URL not set"
  exit 1
fi

# Extract PR info
REPO=$(echo "$PR_URL" | awk -F '/' '{print $(NF-3) "/" $(NF-2)}')
PR_NUMBER=$(echo "$PR_URL" | awk -F '/' '{print $NF}')

# Post comment
gh api repos/$REPO/issues/$PR_NUMBER/comments \
  --method POST \
  --header "Accept: application/vnd.github+json" \
  -f body="$ESCAPED"
#end
