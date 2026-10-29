# 07 — Service DNS / connectivity failure

**Symptoms:** gateway cannot reach a service by name; timeouts or name-resolution errors.

```bash
kubectl get svc,endpoints -n nexaai
kubectl exec -n nexaai deploy/nexaai-gateway -- sh -c 'cat /etc/resolv.conf; getent hosts nexaai-inference || true'
kubectl get pods -n kube-system
kubectl logs -n kube-system -l k8s-app=kube-dns --tail=100
```

**Layer-by-layer:** check DNS name/namespace, Service selector, endpoints, targetPort/containerPort, NetworkPolicy, CNI, and application listener. Test from the same namespace/network context.

**Practice:** change a Service selector to a label that no pod has.

**Recovery:** restore selector/labels or correct port mapping, then verify Endpoints populate and a request succeeds. Do not assume every timeout is DNS.
