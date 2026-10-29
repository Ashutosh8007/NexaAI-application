# 02 — Gateway returns 502

**Symptoms:** `/api/ask` returns 502 or `/ready` returns 503.

**Practice:** stop a dependency with `docker compose stop inference`.

```bash
curl -i http://localhost:8080/ready
curl -i http://localhost:8080/api/ask -H 'Content-Type: application/json' -H 'x-api-token: local-demo-token' -d '{"question":"hello"}'
docker compose logs --since=5m gateway inference
docker compose ps
docker network ls
docker compose exec gateway python -c "import socket; print(socket.getaddrinfo('inference', 8082))"
```

**Expected diagnosis:** upstream service unavailable or unhealthy. In Compose, service DNS uses the service name (`inference`), not `localhost`; `localhost` inside a container means that same container.

**Recovery:** restore the dependency, verify it is listening on the expected port, then retest through the gateway. In Kubernetes inspect Service selectors and Endpoints.

**Prevention:** dependency timeouts, bounded retries with backoff, clear metrics/logs, and carefully designed readiness checks.
