# 14 — Bad Kubernetes rollout

**Symptoms:** new version is deployed but error rate rises or rollout stalls.

```bash
kubectl rollout status deployment/nexaai-gateway -n nexaai --timeout=60s
kubectl rollout history deployment/nexaai-gateway -n nexaai
kubectl describe deployment nexaai-gateway -n nexaai
kubectl get rs,pods -n nexaai
```

**Practice:** deploy an intentionally invalid image or broken probe in a disposable cluster.

**Mitigation:** stop promotion and rollback only after confirming the previous revision is viable:
```bash
kubectl rollout undo deployment/nexaai-gateway -n nexaai
kubectl rollout status deployment/nexaai-gateway -n nexaai
```

**Validate:** healthy replicas, ready endpoints, successful smoke test, and normalized error/latency metrics. Then preserve evidence and fix forward in a new change.
