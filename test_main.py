from starlette.testclient import TestClient

from main import app

# USAGE python -m pytest

client = TestClient(app)


def test_ping():
    response = client.get("/index")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong!"}
