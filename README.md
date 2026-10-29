# NexaAI DevOps Scenario Lab

**A practical, scenario-driven DevOps lab for learning real-world troubleshooting and production incident management.**

## About the Project

NexaAI DevOps Scenario Lab is a hands-on learning environment designed to simulate real-world DevOps challenges using an AI-powered microservices application. Instead of focusing on application development, this project emphasizes the operational side of DevOps engineering: diagnosing failures, analyzing logs, troubleshooting infrastructure, managing deployments, and restoring service availability.

The application consists of multiple containerized services, including an API Gateway, authentication service, simulated AI inference service, document service, background worker, and Redis. These components provide a realistic environment for investigating service failures, connectivity issues, latency, resource constraints, and deployment problems.

## Objectives

- Develop practical troubleshooting skills for DevOps Engineer interviews.
- Understand how to investigate incidents using logs, metrics, health checks, and diagnostic commands.
- Practice CI/CD pipeline development and troubleshooting with GitHub Actions.
- Build, run, inspect, and debug Docker containers.
- Deploy and troubleshoot applications on Kubernetes.
- Improve Linux administration and shell scripting skills.
- Learn container security scanning and deployment validation.
- Simulate production incidents and practice safe recovery procedures.

## Technology Stack

- **CI/CD:** GitHub Actions
- **Containers:** Docker, Docker Compose
- **Orchestration:** Kubernetes
- **Programming and scripting:** Python, Bash, YAML
- **Application services:** FastAPI-based microservices
- **Caching and queues:** Redis
- **Security:** Trivy container image scanning
- **Deployment validation:** kubeconform
- **Troubleshooting:** Linux commands, application logs, health checks, Kubernetes diagnostics

## Scenarios Covered

The initial lab includes scenarios such as:

- Docker containers exiting unexpectedly
- API Gateway returning HTTP 502 errors
- Kubernetes CrashLoopBackOff and Pending pods
- Failed readiness probes and image pulls
- Service discovery and DNS connectivity issues
- High latency and request timeouts
- Redis connectivity failures
- CPU, memory, and disk pressure
- GitHub Actions pipeline failures
- Security scan failures
- Failed deployments and rollbacks
- Configuration and secrets mismatches
- Background queue backlogs
- TLS and certificate issues
- Log analysis across multiple services

## How to Practice

1. Start the application using Docker Compose.
2. Verify service health and inspect application logs.
3. Reproduce a scenario using the provided instructions.
4. Diagnose the issue using Linux, Docker, networking, or Kubernetes commands.
5. Identify the root cause using evidence rather than assumptions.
6. Apply the safest fix and validate service recovery.
7. Document the root cause, resolution, and preventive actions.

## Learning Approach

Each scenario is intended to encourage a structured incident-response workflow:

**Understand the symptoms → Gather evidence → Identify the failing component → Find the root cause → Apply a fix → Validate recovery → Prevent recurrence.**

The goal is not simply to memorize commands, but to develop the troubleshooting approach expected of a DevOps Engineer working with real applications and production environments.

## Future Enhancements

- Additional scenario-based incidents
- Prometheus and Grafana monitoring exercises
- More advanced Kubernetes troubleshooting
- CI/CD deployment and rollback simulations
- Automated health checks and incident reports
- AI-assisted log analysis and root-cause investigation
- Interview-style troubleshooting exercises with increasing difficulty

## Intended Audience

- Aspiring DevOps Engineers
- Junior Cloud and Infrastructure Engineers
- Engineers preparing for DevOps interviews
- Developers learning containerization and deployment operations
- Anyone seeking practical experience with incident troubleshooting

**Note:** This is a learning and simulation project. Validate configurations and security settings before adapting them to production environments.
