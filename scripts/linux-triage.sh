#!/usr/bin/env bash
# Read-only first-pass Linux triage. Run locally or inside a disposable lab VM.
set -u
echo "===== time / host ====="
date -Is
hostname
uptime
echo "===== disk ====="
df -hT
echo "===== inode usage ====="
df -ih
echo "===== memory ====="
free -h
echo "===== top processes ====="
ps -eo pid,ppid,%cpu,%mem,rss,etime,cmd --sort=-%mem | head -15
echo "===== failed systemd units (if systemd is available) ====="
systemctl --failed --no-pager 2>/dev/null || true
echo "===== recent kernel warnings (permissions may limit output) ====="
dmesg --ctime 2>/dev/null | tail -30 || true
