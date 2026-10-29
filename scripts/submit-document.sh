#!/usr/bin/env bash
set -euo pipefail
base="${1:-http://localhost:8080}"
token="${DEMO_API_TOKEN:-local-demo-token}"
curl -sS -i --max-time 5 "$base/api/documents" \
  -H "Content-Type: application/json" \
  -H "x-api-token: $token" \
  -d '{"name":"sample-policy.pdf"}'
echo
