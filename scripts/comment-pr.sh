#!/bin/bash

echo "🔍 diff_response.json:"
cat diff_response.json
echo ""
echo "🔍 infra_response.json:"
cat infra_response.json
echo ""

AI_ANALYSIS=$(jq -r '.analysis' diff_response.json)
COST_ESTIMATION=$(jq -r '.analysis' infra_response.json)

