#!/usr/bin/env bash
# Controlled fault injection: slows the simulated inference service.
set -euo pipefail
delay="${1:-8}"
if ! [[ "$delay" =~ ^[0-9]+$ ]] || (( delay > 30 )); then
  echo "Provide an integer delay from 0 to 30 seconds." >&2
  exit 2
fi
INFERENCE_DELAY_SECONDS="$delay" docker compose up -d --force-recreate inference
echo "Inference delay set to ${delay}s. Restore with: ./scripts/inject-delay-compose.sh 0"
