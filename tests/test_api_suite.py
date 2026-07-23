import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health_check_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "HEALTHY"

def test_get_summary_endpoint():
    response = client.get("/api/summary")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "metrics" in data
    assert data["metrics"]["total_tests"] > 0

def test_run_tests_endpoint():
    response = client.post("/api/run-tests")
    assert response.status_code == 200
    data = response.json()
    assert "summary" in data

def test_report_generation_endpoint():
    response = client.get("/api/report/html")
    assert response.status_code == 200
    assert "Executive QA Audit Report" in response.text
