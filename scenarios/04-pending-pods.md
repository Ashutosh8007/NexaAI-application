# 04 — Pods stuck Pending

**Symptoms:** deployment desired replicas exceed available replicas; pod never schedules.

```bash
kubectl get pods -n nexaai -o wide
kubectl describe pod <pod> -n nexaai
kubectl get nodes
kubectl describe nodes
kubectl top nodes
```

**Practice:** in a disposable manifest, set a CPU request larger than node capacity or add a required node selector that no node satisfies.

**Expected evidence:** scheduler events such as insufficient CPU/memory, unmatched node selector, taint/toleration mismatch, or unbound PVC.

**Recovery:** right-size requests based on observed demand, correct placement rules, or scale capacity through the approved platform process. Do not remove resource requests indiscriminately.
