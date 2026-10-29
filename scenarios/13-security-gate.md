# 13 — Security scan blocks release

**Symptoms:** Trivy or a quality gate reports vulnerabilities/secrets/misconfiguration.

**Interview response:** confirm the scanner, target, severity, exploitability, reachability, fix availability, and whether the finding is a real secret. Prioritize exposed credentials and exploitable critical/high issues; avoid blindly suppressing findings.

**Actions:** upgrade the vulnerable base image/dependency, rebuild with a pinned version, rescan, review SBOM and image provenance where available, and rotate any leaked credential. A secret found in Git history should be treated as compromised even after the file is removed.

**Practice:** add a dummy test-only secret-like string to a disposable branch and inspect the scanner output; never use a real credential.
