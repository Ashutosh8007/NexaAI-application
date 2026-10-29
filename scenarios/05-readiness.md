# 05 — Readiness probe fails while process is running

**Symptoms:** pod is Running but not Ready; Service has no endpoints.

```bash
kubectl get pods,svc,endpoints -n nexaai
kubectl describe pod <pod> -n nexaai
kubectl exec -n nexaai <pod> -- sh -c 'wget -qO- http://127.0.0.1:8080/health || true'
```

**Practice:** set readiness probe port/path to a wrong value.

**Key distinction:** liveness asks whether the process should be restarted; readiness asks whether it should receive traffic. A readiness failure normally removes the pod from Service endpoints without restarting it.

**Recovery:** correct the path/port and ensure startup timing matches real initialization. Avoid making liveness depend on every external dependency, which can create restart cascades.
