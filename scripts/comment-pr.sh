#!/bin/bash

set -e

PR_NUMBER=$(jq --raw-output .pull_request.number "$GITHUB_EVENT_PATH")
REPO_URL=$(jq --raw-output .repository.full_name "$GITHUB_EVENT_PATH")

ANALYSIS=$(cat response.json | jq -r '.analysis')

gh pr comment "$PR_NUMBER" --repo "$REPO_URL" --body "$ANALYSIS"
