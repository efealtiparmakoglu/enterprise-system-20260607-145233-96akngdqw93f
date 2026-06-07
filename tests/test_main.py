import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_create_item():
    item = {"name": "Test Item", "description": "Test Description"}
    response = client.post("/api/v1/items", json=item)
    assert response.status_code == 201
    assert response.json()["name"] == "Test Item"

def test_list_items():
    response = client.get("/api/v1/items")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_item_not_found():
    response = client.get("/api/v1/items/99999")
    assert response.status_code == 404
