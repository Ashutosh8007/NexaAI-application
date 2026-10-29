# 03 — Kubernetes CrashLoopBackOff

**Symptoms:** pod restarts repeatedly.

```bash
kubectl get pods -n nexaai
kubectl describe pod <pod> -n nexaai
kubectl logs <pod> -n nexaai --previous
kubectl get events -n nexaai --sort-by=.lastTimestamp
kubectl get deploy <deployment> -n nexaai -o yaml
```

**Practice options:** change a container command to a bad module, remove a required env var, or configure an invalid port in a disposable branch.

**Reasoning:** `CrashLoopBackOff` is a restart/backoff state, not a root cause. Inspect previous-container logs, exit code, events, command/args, ConfigMaps/Secrets, and probe behavior.

**Recovery:** fix the root cause, apply the change, watch rollout, and confirm restarts stop. Avoid deleting pods repeatedly without addressing the cause.
