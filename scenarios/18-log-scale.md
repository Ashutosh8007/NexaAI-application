# 18 — Investigating failures across 100 services

**Scenario:** a user reports intermittent failures across a large microservices estate.

**Do not** open every service log manually first. Establish the time window, affected user/tenant, request ID, region/cluster, and recent deployments. Correlate gateway access logs with traces and dependency metrics.

**Useful pattern:** centralize structured JSON logs; standard fields include timestamp, service, environment, severity, trace/request ID, route, status code, duration, and dependency. Aggregate error rates and latency by service/version, then drill into the first failing hop.

**Questions:** Is the issue broad or one tenant? Did it start after a release? Is there a common dependency? Are retries multiplying traffic? Is the problem latency, saturation, or errors?

**Deliverable:** timeline, impact, evidence, root cause, mitigation, recovery proof, and preventive actions.
