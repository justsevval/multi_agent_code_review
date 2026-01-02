from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_review_endpoint_returns_issues_list():
    code = "eval('2+2')\n"
    resp = client.post("/review", json={"code": code})
    assert resp.status_code == 200

    data = resp.json()
    assert "issues" in data
    assert isinstance(data["issues"], list)

def test_review_endpoint_empty_code_still_returns_schema():
    resp = client.post("/review", json={"code": ""})
    assert resp.status_code == 200
    data = resp.json()
    assert "issues" in data

def test_review_endpoint_bad_payload():
    resp = client.post("/review", json={})
    assert resp.status_code in (422, 400)
