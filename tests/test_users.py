from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_create_user():
    headers = {"Authorization": "Bearer valid-token"}
    res = client.post("/users/", json={"name": "Alice", "email": "alice@example.com"}, headers=headers)
    assert res.status_code == 200
    assert res.json()["name"] == "Alice"


def test_list_users():
    headers = {"Authorization": "Bearer valid-token"}
    res = client.get("/users/", headers=headers)
    assert res.status_code == 200
    assert isinstance(res.json(), list)
