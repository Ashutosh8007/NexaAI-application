# 16 — Background queue backlog grows

**Symptoms:** documents are accepted but not processed quickly; queue depth rises.

**Investigate:** queue depth and age of oldest message, worker replicas/health, processing duration, dependency errors, poison messages, retries, and available CPU/memory.

**Practice:** stop the worker with `docker compose stop worker`, submit documents, then inspect queue depth. Restore it with `docker compose start worker`.

**Mitigation:** restore worker capacity, scale consumers carefully, quarantine poison messages, and preserve ordering/idempotency requirements. More workers help only if the bottleneck is parallelizable and dependencies can handle the extra load.

**Prevention:** backlog/age alerts, retry limits, dead-letter queues, idempotent handlers, and throughput-based autoscaling.
