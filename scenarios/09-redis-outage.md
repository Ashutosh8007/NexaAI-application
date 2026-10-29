# 09 — Redis unavailable / queue API fails

**Symptoms:** document requests return 503; worker logs connection errors.

```bash
docker compose stop redis
docker compose logs --since=3m documents worker
curl -i http://localhost:8080/api/documents -H 'x-api-token: local-demo-token'
docker compose start redis
```

**Reasoning:** distinguish Redis process failure, wrong URL, DNS, port, authentication, and resource exhaustion. Check whether writes were accepted and whether retries can duplicate work.

**Recovery:** restore Redis connectivity, verify queue depth and worker processing, and check for stuck/dead-letter jobs. In production, discuss persistence, backup/restore, HA, bounded retries, idempotency, and alerting.
