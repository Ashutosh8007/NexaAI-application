# 15 — Secret or configuration drift

**Symptoms:** one replica gets 401/500 while others work, or a deployment fails after a config change.

```bash
kubectl describe pod <pod> -n nexaai
kubectl get configmap nexaai-config -n nexaai -o yaml
kubectl get secret nexaai-demo-secret -n nexaai
kubectl rollout history deployment/nexaai-gateway -n nexaai
```

Do not print or paste Secret values into logs/chat. Compare key names, mounted/env configuration, namespace, rollout timing, and service-account access.

**Practice:** create the demo Secret using `kubectl apply -f deploy/k8s/secret.example.yaml`, then change the demo token locally and observe 401s.

**Prevention:** external secret manager, rotation runbooks, environment separation, audit trails, and avoiding secrets in Git.
