import os
from fastapi import FastAPI, Header, HTTPException

app = FastAPI(title="NexaAI Auth Service")

@app.get("/health")
def health():
    return {"status": "ok", "service": "auth"}

@app.get("/validate")
def validate(x_api_token: str = Header(default="")):
    expected = os.getenv("DEMO_API_TOKEN", "local-demo-token")
    if x_api_token != expected:
        raise HTTPException(status_code=401, detail="token rejected")
    return {"valid": True}
