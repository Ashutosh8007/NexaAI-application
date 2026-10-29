from fastapi.testclient import TestClient
from app.gateway.main import app

client = TestClient(app)

def test_gateway_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_ask_requires_token():
    response = client.post("/api/ask", json={"question": "hello"})
    assert response.status_code == 401

def test_ask_validates_payload():
    response = client.post("/api/ask", json={})
    assert response.status_code == 422
