# 12 — GitHub Actions pipeline fails

**Symptoms:** a PR is red while local execution appears successful.

**Approach**
1. Identify the first failing step, not just the final job status.
2. Read the exact command and exit code.
3. Check runner OS, working directory, runtime/tool versions, environment variables, permissions, and cached dependencies.
4. Reproduce the same command locally or in a clean container.
5. Fix the cause, rerun, and verify the workflow on a clean commit.

**Practice:** intentionally break a Python import, YAML indentation, or Docker COPY path.

**Useful commands:** `python -m compileall -q app tests`, `pytest -q`, `docker build --no-cache -t nexaai-lab:debug .`, `git diff --check`.

**Security:** use GitHub OIDC where supported, least-privilege workflow permissions, protected environments, and secrets only in the steps that need them. Never print tokens in logs.
