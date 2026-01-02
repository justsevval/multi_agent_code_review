import pytest
from fastapi.testclient import TestClient
from app.main import app

pytestmark = pytest.mark.integration

client = TestClient(app)

def test_review_endpoint_returns_issues():
    code = "eval('2+2')"
    response = client.post("/review", json={"code": code})
    assert response.status_code == 200

    data = response.json()
    assert "issues" in data
    assert isinstance(data["issues"], list)

def test_review_endpoint_handles_empty_code():
    response = client.post("/review", json={"code": ""})
    assert response.status_code == 200
    assert "issues" in response.json()
