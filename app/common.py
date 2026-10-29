from datetime import datetime, timezone
import json
import os
import sys

def log(event: str, **fields):
    record = {"timestamp": datetime.now(timezone.utc).isoformat(), "event": event, **fields}
    print(json.dumps(record, separators=(",", ":")), file=sys.stdout, flush=True)

def env(name: str, default: str = "") -> str:
    return os.getenv(name, default)
