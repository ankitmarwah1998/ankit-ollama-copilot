#!/bin/bash

# Load response safely
RESPONSE=$(cat response.json)

# Escape newlines
ESCAPED=$(echo "$RESPONSE" | sed ':a;N;$!ba;s/\n/\\n/g')

# Add comment to PR
gh pr comment "$PR_URL" --body "$ESCAPED"
