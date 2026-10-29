# 08 — AI inference latency and 504s

**Symptoms:** users report slow answers; gateway emits 504 after upstream timeout.

**Practice with Compose:** `./scripts/inject-delay-compose.sh 8`, then send a request:
```bash
time curl -i --max-time 8 http://localhost:8080/api/ask -H 'Content-Type: application/json' -H 'x-api-token: local-demo-token' -d '{"question":"summarize this document"}'
docker compose logs --since=2m gateway inference
./scripts/inject-delay-compose.sh 0
```

**Investigate:** p50/p95/p99 latency, timeout budgets at each hop, CPU/memory, connection pools, request concurrency, dependency latency, queue depth, and recent changes.

**Mitigation:** rollback a bad release, shed noncritical load, reduce concurrency or route traffic safely. Do not blindly increase all timeouts: that can amplify resource exhaustion.

**Prevention:** SLO-based alerts, tracing/correlation IDs, load tests, bounded retries with jitter, and capacity planning.
