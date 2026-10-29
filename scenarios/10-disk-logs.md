# 10 — Disk pressure caused by logs

**Symptoms:** nodes/VMs show disk pressure; container writes fail; workloads become unstable.

```bash
./scripts/linux-triage.sh
df -hT
df -ih
du -xhd1 /var/log 2>/dev/null | sort -h
journalctl --disk-usage 2>/dev/null || true
docker system df
```

**Important:** full filesystem and exhausted inodes are different failure modes. Identify the growing path before deleting anything. Check log rotation and container runtime storage.

**Mitigation:** rotate/compress or safely truncate the specific runaway log only after confirming ownership and operational policy; never blindly delete active database/container files.

**Prevention:** log rotation, retention limits, disk/inode alerts, and centralized logging.
