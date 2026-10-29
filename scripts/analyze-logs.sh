#!/usr/bin/env bash
# Usage: ./scripts/analyze-logs.sh [logfile]
set -euo pipefail
file="${1:-}"
if [[ -z "$file" ]]; then
  echo "Usage: $0 <logfile>" >&2
  exit 2
fi
if [[ ! -r "$file" ]]; then
  echo "Cannot read log file: $file" >&2
  exit 2
fi
echo "== Top event types =="
grep -o '"event":"[^"]*"' "$file" | sort | uniq -c | sort -nr | head -10 || true
echo
echo "== Error/timeout indicators =="
grep -Ei 'error|exception|timeout|failed|unavailable|503|502|504|oom' "$file" | tail -50 || true
echo
echo "== Approximate 5xx/status counts =="
grep -Eo 'status.?[:=].?(5[0-9]{2})' "$file" | sort | uniq -c || true
