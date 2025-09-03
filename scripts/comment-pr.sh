#!/bin/bash
set -e

PR_NUMBER="${PR_NUMBER:-${GITHUB_EVENT_PULL_REQUEST_NUMBER}}"
if [ -z "$PR_NUMBER" ]; then
  echo "PR number not found. Exiting."
  exit 1
fi

if [ ! -f comment.md ]; then
  echo "comment.md not found. Skipping PR comment."
  exit 0
fi

echo "Posting AI analysis to PR #$PR_NUMBER..."
gh pr comment "$PR_NUMBER" --body-file comment.md

