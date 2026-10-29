import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from redis import Redis
from redis.exceptions import RedisError
from app.common import log

app = FastAPI(title="NexaAI Document Service")
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

class DocumentRequest(BaseModel):
    name: str

def get_redis():
    return Redis.from_url(REDIS_URL, decode_responses=True, socket_connect_timeout=1)

@app.get("/health")
def health():
    return {"status": "ok", "service": "documents"}

@app.get("/ready")
def ready():
    try:
        get_redis().ping()
        return {"status": "ready"}
    except RedisError as exc:
        raise HTTPException(status_code=503, detail=f"redis unavailable: {exc}")

@app.get("/documents")
def documents():
    try:
        redis = get_redis()
        return {"queued": redis.llen("nexaai:documents"), "service": "documents"}
    except RedisError as exc:
        log("redis_error", error=str(exc))
        raise HTTPException(status_code=503, detail="queue dependency unavailable")

@app.post("/documents")
def create_document(payload: DocumentRequest):
    try:
        job_id = get_redis().lpush("nexaai:documents", payload.name)
        log("document_queued", name=payload.name, queue_depth=job_id)
        return {"accepted": True, "queue_depth": job_id}
    except RedisError as exc:
        log("redis_error", error=str(exc))
        raise HTTPException(status_code=503, detail="queue dependency unavailable")
