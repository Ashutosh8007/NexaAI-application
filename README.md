# NexaAI — DevOps Scenario-Based Interview Lab

A deliberately small but production-shaped AI microservices platform for practicing **DevOps troubleshooting**, not application feature development.

> Terraform is intentionally excluded. Infrastructure provisioning with Terraform can be practiced separately.

## What you will operate

- **API Gateway** — public entry point and request routing
- **Auth Service** — validates a demo API token
- **Inference Service** — simulates an AI model endpoint and can be made slow/unhealthy
- **Document Service** — simulates document ingestion/status
- **Redis** — cache/queue dependency
- **Worker** — background document processing simulation
- **Docker Compose** for local incidents
- **Kubernetes manifests** for cluster incidents
- **GitHub Actions** for tests, image build, security scanning, and manifest checks
- **Shell scripts** for health checks, log analysis, resource checks, and controlled fault injection

The application is intentionally lightweight. It does **not** download or run a large language model; the inference endpoint simulates an AI backend so you can focus on deployment, networking, reliability, observability, and incident response.

## Quick start

Requirements: Git, Docker Desktop/Engine with Compose, Python 3.11+ (optional for local tests), and `kubectl` plus kind or minikube for Kubernetes labs.

```bash
docker compose up --build -d
docker compose ps
curl -i http://localhost:8080/health
curl -i http://localhost:8080/api/ask -H 'Content-Type: application/json' \
  -d '{"question":"How do I troubleshoot a failed deployment?"}'
curl -i http://localhost:8080/api/documents
docker compose logs --tail=100
```

Stop the stack:

```bash
docker compose down
```

## Suggested practice loop

1. Start from a healthy baseline.
2. Read a scenario in [`scenarios/`](scenarios/).
3. Inject only the specified fault.
4. Do **not** read the resolution immediately. Collect evidence first.
5. Write a short incident update: impact, scope, evidence, mitigation, root cause, prevention.
6. Fix the issue and verify recovery with health checks, logs, and a repeat request.
7. Explain your decision-making aloud as if the interviewer were the incident commander.

## Repository map

```text
.
├── .github/workflows/ci.yml
├── app/
│   ├── gateway/       # Public API gateway
│   ├── auth/          # Demo auth service
│   ├── inference/     # Simulated AI inference service
│   ├── documents/     # Document API
│   └── worker/        # Background worker
├── deploy/
│   └── k8s/           # Kubernetes Deployment, Service, ConfigMap, probes, resources
├── scripts/           # Operational shell tools and fault injectors
├── scenarios/         # Interview incident playbooks
├── tests/             # Basic smoke/unit tests
├── Dockerfile
└── compose.yaml
```

## GitHub setup

This package is ready to push to a repository you create in your GitHub account:

```bash
git init
git add .
git commit -m "Initial NexaAI DevOps scenario lab"
git branch -M main
git remote add origin https://github.com/<YOUR_USERNAME>/nexaai-devops-scenario-lab.git
git push -u origin main
```

Create an empty GitHub repository named `nexaai-devops-scenario-lab` first. Do not add a README/license from GitHub if you are pushing this existing initial commit.

## GitHub Actions

The workflow in `.github/workflows/ci.yml` runs on pull requests and pushes:
- Python syntax and unit tests
- Docker image build
- Trivy filesystem scan (findings are reported; the initial lab does not fail on every finding)
- Kubernetes YAML validation with `kubeconform`

The workflow does not publish images or deploy to a real cluster by default. Add publishing/deployment only after you understand the workflow and configure repository secrets/environments safely.

## Kubernetes practice

For kind, build and load the image:

```bash
docker build -t nexaai-lab:dev .
kind create cluster --name nexaai
kind load docker-image nexaai-lab:dev --name nexaai
kubectl apply -f deploy/k8s/
kubectl get pods,svc
kubectl port-forward svc/nexaai-gateway 8080:80
```

The base manifests use `imagePullPolicy: IfNotPresent`. If your cluster is not kind, update the image strategy to match your registry.

## Safety rules for fault injection

- Use only your local lab or a disposable practice cluster.
- Never run chaos commands against a work, shared, or production cluster.
- Read every script before running it.
- Some scenarios intentionally create broken configurations. Keep a clean Git commit so you can reset with `git checkout -- .`.
- Avoid putting credentials, tokens, kubeconfigs, or cloud keys in source control.

## Scenario catalogue

| ID | Incident | Main skills |
|---|---|---|
| 01 | Container exits immediately | Docker entrypoint, logs, exit codes |
| 02 | Gateway returns 502 | service DNS, port mapping, dependencies |
| 03 | Kubernetes CrashLoopBackOff | events, logs, probes, config |
| 04 | Pods stuck Pending | requests/limits, scheduling, events |
| 05 | Readiness probe fails | probes, app port, endpoints |
| 06 | ImagePullBackOff | tags, registry auth, imagePullPolicy |
| 07 | DNS/network connectivity issue | CoreDNS, Services, NetworkPolicy concepts |
| 08 | High latency / timeout | dependency latency, timeout budgets, concurrency |
| 09 | Redis unavailable | dependency failure, graceful degradation |
| 10 | Disk pressure / log growth | Linux disk tools, container logs |
| 11 | CPU/memory pressure | top, ps, kubectl top, limits/OOMKilled |
| 12 | CI pipeline fails | GitHub Actions logs, exit codes, caching |
| 13 | Security scan blocks release | Trivy findings, triage, risk-based remediation |
| 14 | Bad rollout / rollback | rollout status/history/undo |
| 15 | Secret/config drift | environment variables, Kubernetes Secret hygiene |
| 16 | Background queue backlog | worker health, throughput, retries |
| 17 | Certificate / TLS failure | expiry, chain, hostname, trust store |
| 18 | 100 services / noisy logs | structured logs, correlation IDs, aggregation |

See each scenario file for **symptoms, first 5 minutes, commands, fault injection, success criteria, and interview answer structure**.
