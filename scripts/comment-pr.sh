#!/bin/bash

# Extract PR number from event payload
PR_NUMBER=$(jq --raw-output .number "$GITHUB_EVENT_PATH")

# Extract analysis from response.json
analysis=$(jq -r '.analysis' response.json)

# Save to a markdown file
echo "$analysis" > comment.md

# Post comment to PR
gh pr comment "$PR_NUMBER" --body-file comment.md

