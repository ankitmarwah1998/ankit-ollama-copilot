#!/bin/bash
analysis=$(jq -r '.analysis' response.json)
echo "$analysis" > comment.md
gh pr comment "$PR_NUMBER" --body-file comment.md

