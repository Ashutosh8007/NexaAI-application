# 11 — CPU throttling or OOMKilled

**Symptoms:** slow requests, restarts, `OOMKilled`, or CPU throttling.

```bash
kubectl top pods -n nexaai
kubectl describe pod <pod> -n nexaai
kubectl get pod <pod> -n nexaai -o jsonpath='{.status.containerStatuses[*].lastState}'
docker stats
free -h
ps -eo pid,%cpu,%mem,rss,cmd --sort=-%mem | head
```

**Reasoning:** compare requests/limits with actual usage; check memory leak versus traffic spike, node pressure, CPU throttling, and recent deployment changes.

**Mitigation:** scale/rollback where justified and safe; adjust limits based on evidence and load tests. More memory is not a root-cause analysis.

**Prevention:** resource dashboards, realistic requests, autoscaling signals, load tests, and capacity alerts.
