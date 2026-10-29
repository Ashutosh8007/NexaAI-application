# 06 — ImagePullBackOff

**Symptoms:** Kubernetes cannot start the requested container image.

```bash
kubectl describe pod <pod> -n nexaai
kubectl get pod <pod> -n nexaai -o jsonpath='{.spec.containers[*].image}'
docker images
```

**Check:** typo/missing tag, private registry credentials, image architecture, rate limits, and whether the image exists in the registry. `IfNotPresent` only uses a local image if it is available on that node.

**Practice:** change the image tag to a nonexistent tag.

**Recovery:** publish/use the correct immutable tag and configure least-privilege `imagePullSecrets` where needed. For kind, load the image into the cluster explicitly.
