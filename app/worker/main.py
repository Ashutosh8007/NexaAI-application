import os
import time
from redis import Redis
from redis.exceptions import RedisError
from app.common import log

def main():
    url = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    interval = float(os.getenv("WORKER_INTERVAL_SECONDS", "2"))
    redis = Redis.from_url(url, decode_responses=True, socket_connect_timeout=2)
    log("worker_started", interval=interval)
    while True:
        try:
            item = redis.brpop("nexaai:documents", timeout=2)
            if item:
                _, name = item
                log("document_processed", name=name)
        except RedisError as exc:
            log("worker_dependency_error", error=str(exc))
            time.sleep(interval)

if __name__ == "__main__":
    main()
