import os
import httpx
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from app.common import log

app = FastAPI(title="NexaAI API Gateway", version="1.0.0")
AUTH_URL = os.getenv("AUTH_URL", "http://localhost:8081")
INFERENCE_URL = os.getenv("INFERENCE_URL", "http://localhost:8082")
DOCUMENTS_URL = os.getenv("DOCUMENTS_URL", "http://localhost:8083")
DEMO_API_TOKEN = os.getenv("DEMO_API_TOKEN", "local-demo-token")

class AskRequest(BaseModel):
    question: str

@app.get("/health")
async def health():
    return {"status": "ok", "service": "gateway"}

@app.get("/ready")
async def ready():
    # Liveness is local; readiness checks dependencies used by this gateway.
    try:
        async with httpx.AsyncClient(timeout=2.0) as client:
            for url in (AUTH_URL + "/health", INFERENCE_URL + "/health", DOCUMENTS_URL + "/health"):
                response = await client.get(url)
                response.raise_for_status()
        return {"status": "ready"}
    except Exception as exc:
        log("readiness_failed", error=str(exc))
        raise HTTPException(status_code=503, detail="dependency not ready")

@app.post("/api/ask")
async def ask(payload: AskRequest, x_api_token: str = Header(default="")):
    if x_api_token != DEMO_API_TOKEN:
        raise HTTPException(status_code=401, detail="invalid demo token")
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            auth = await client.get(AUTH_URL + "/validate", headers={"x-api-token": x_api_token})
            auth.raise_for_status()
            response = await client.post(INFERENCE_URL + "/infer", json={"question": payload.question})
            response.raise_for_status()
            result = response.json()
        log("inference_request", status="success")
        return result
    except httpx.TimeoutException:
        log("inference_request", status="timeout")
        raise HTTPException(status_code=504, detail="upstream timeout")
    except httpx.HTTPError as exc:
        log("upstream_error", error=str(exc))
        raise HTTPException(status_code=502, detail="upstream service unavailable")

@app.get("/api/documents")
async def documents(x_api_token: str = Header(default="")):
    if x_api_token != DEMO_API_TOKEN:
        raise HTTPException(status_code=401, detail="invalid demo token")
    try:
        async with httpx.AsyncClient(timeout=3.0) as client:
            response = await client.get(DOCUMENTS_URL + "/documents")
            response.raise_for_status()
            return response.json()
    except httpx.HTTPError as exc:
        log("documents_error", error=str(exc))
        raise HTTPException(status_code=502, detail="document service unavailable")
