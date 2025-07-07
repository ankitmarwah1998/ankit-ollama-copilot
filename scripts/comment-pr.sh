#!/bin/bash

# Extract PR number
PR_NUMBER=$(jq --raw-output .number "$GITHUB_EVENT_PATH")

# Validate PR_NUMBER
if [[ -z "$PR_NUMBER" || "$PR_NUMBER" == "null" ]]; then
  echo "❌ Could not extract PR number"
  exit 1
fi

# Extract AI response
if ! analysis=$(jq -r '.analysis' response.json); then
  echo "❌ Failed to parse response.json"
  cat response.json
  exit 1
fi

# Validate analysis
if [[ -z "$analysis" || "$analysis" == "null" ]]; then
  echo "❌ AI analysis is empty. Not posting comment."
  exit 1
fi

# Save analysis and comment
echo "$analysis" > comment.md
gh pr comment "$PR_NUMBER" --body-file comment.md
#!/bin/bash
