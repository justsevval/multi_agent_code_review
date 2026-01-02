import pytest
from fastapi.testclient import TestClient
from app.main import app

pytestmark = pytest.mark.system

def test_end_to_end_review_flow():
    client = TestClient(app)
    code = "eval('2+2')\n" + ("x" * 120)

    response = client.post("/review", json={"code": code})
    assert response.status_code == 200

    data = response.json()
    assert "issues" in data
    assert len(data["issues"]) > 0
