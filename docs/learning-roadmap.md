# 4-week hands-on roadmap

## Week 1 — Linux + Docker
- Day 1: start/stop stack, inspect images, containers, networks and volumes.
- Day 2: container exits, entrypoint, ports, environment variables, non-root user.
- Day 3: disk/inodes, memory/CPU, process signals, logs and exit codes.
- Day 4: shell scripts, exit status, `set -euo pipefail`, quoting, grep/awk/sort.
- Day 5: repeat scenarios 01, 02, 10, 11 without looking at solutions.

## Week 2 — GitHub Actions + supply chain
- Understand triggers, jobs, steps, `needs`, artifacts, caching, permissions and secrets.
- Break and fix the test/build/security jobs.
- Add a PR check and require it before merge in GitHub branch protection.
- Explain why the workflow builds but does not deploy to production by default.

## Week 3 — Kubernetes
- Apply manifests; inspect pods, Deployments, ReplicaSets, Services, endpoints, events.
- Practice probes, resource requests/limits, image pulls, DNS and rollback.
- Use `kubectl describe`, current logs, previous logs, and rollout history deliberately.

## Week 4 — incident simulation
- Pick two random scenarios daily.
- Time-box diagnosis to 10 minutes.
- Write a short incident report and a 90-second spoken interview answer.
- Re-run after a clean reset to prove the fix is repeatable.

## Exit criteria
You can explain the command before running it, distinguish symptom from root cause, show objective recovery evidence, and state a preventive action.
