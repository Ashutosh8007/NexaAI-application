#!/usr/bin/env bash
set -euo pipefail
ns="${1:-nexaai}"
echo "== Pods =="
kubectl get pods -n "$ns" -o wide
echo "== Deployments =="
kubectl get deploy -n "$ns"
echo "== Services and endpoints =="
kubectl get svc,endpoints -n "$ns"
echo "== Recent events =="
kubectl get events -n "$ns" --sort-by=.lastTimestamp | tail -30
echo "== Restarting / unhealthy pod details =="
for pod in $(kubectl get pods -n "$ns" --no-headers | awk '$3!="Running" || $4+0>0 {print $1}'); do
  echo "--- $pod ---"
  kubectl describe pod "$pod" -n "$ns" || true
  kubectl logs "$pod" -n "$ns" --all-containers --previous 2>/dev/null || true
done
