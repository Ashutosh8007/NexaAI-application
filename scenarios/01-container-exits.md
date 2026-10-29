# 01 — Container exits immediately

**Symptoms:** container repeatedly exits; Compose shows `Exited (1)`.

**Practice:** temporarily change the gateway command in `compose.yaml` to a nonexistent module, then run `docker compose up -d --force-recreate gateway`.

**First 5 minutes**
```bash
docker compose ps -a
docker compose logs --tail=100 gateway
docker inspect "$(docker compose ps -aq gateway)" --format '{{.State.ExitCode}} {{.State.Error}}'
docker image inspect nexaai-devops-scenario-lab-gateway 2>/dev/null || true
```

**Expected diagnosis:** process/entrypoint/import/configuration failure, not a port-forwarding issue. Read the first traceback and compare the command, working directory, copied files, and runtime dependencies.

**Recovery:** restore the command, rebuild, recreate, and verify `/health`. Do not blindly restart a deterministic failing process.

**Interview answer:** explain the evidence you used to distinguish startup failure from a health-check failure, and how you would prevent it with image smoke tests.
