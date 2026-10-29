# Scenario interview answer framework

Use this sequence rather than guessing a fix immediately:

1. **Clarify impact:** What is failing? All users or a subset? Since when? Production or non-production?
2. **Establish signals:** error rate, latency, traffic, saturation, alerts, recent deployments, logs, traces.
3. **Localize the layer:** application → container → Kubernetes workload → Service/DNS/network → dependency → node/platform.
4. **Form one hypothesis at a time:** state the evidence that would confirm or reject it.
5. **Mitigate safely:** rollback, shift traffic, scale within guardrails, restart only if justified, or disable a noncritical feature.
6. **Validate:** smoke tests, ready endpoints, normal error rate/latency, no new restarts, customer confirmation.
7. **Prevent:** alerting, tests, capacity, runbooks, safer rollout, retry/timeout budgets, ownership.

A strong junior-level answer says what you would check and why, acknowledges uncertainty, and avoids claiming access or authority you do not have.
