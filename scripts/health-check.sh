#!/usr/bin/env bash
set -uo pipefail
BASE_URL="${1:-http://localhost:8080}"
ENDPOINTS=("/health" "/ready")
failed=0
for endpoint in "${ENDPOINTS[@]}"; do
  code="$(curl -sS -o /tmp/nexaai-health-body -w '%{http_code}' --max-time 4 "${BASE_URL}${endpoint}" || true)"
  printf '%-10s %-12s %s\n' "$code" "$endpoint" "$(cat /tmp/nexaai-health-body 2>/dev/null || true)"
  [[ "$code" == "200" ]] || failed=1
done
exit "$failed"
