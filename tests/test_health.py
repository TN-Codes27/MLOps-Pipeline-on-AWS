from fastapi import testclient
from services.api.app.main import app 

client = testclient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"
