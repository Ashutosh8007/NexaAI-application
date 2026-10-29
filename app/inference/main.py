import asyncio
import os
from fastapi import FastAPI
from pydantic import BaseModel
from app.common import log

app = FastAPI(title="NexaAI Simulated Inference Service")

class InferRequest(BaseModel):
    question: str

@app.get("/health")
def health():
    return {"status": "ok", "service": "inference"}

@app.post("/infer")
async def infer(payload: InferRequest):
    delay = max(0.0, float(os.getenv("INFERENCE_DELAY_SECONDS", "0")))
    if delay:
        await asyncio.sleep(delay)
    log("inference_completed", question_length=len(payload.question), delay_seconds=delay)
    return {
        "answer": f"Simulated AI response for: {payload.question[:160]}",
        "model": "nexaai-demo-model",
        "latency_mode": "delayed" if delay else "normal"
    }
