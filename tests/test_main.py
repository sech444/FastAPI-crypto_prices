from starlette.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_ping():
    response = client.get("/index")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong!"}
