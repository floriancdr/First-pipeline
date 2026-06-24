from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    # Mise à jour ici pour inclure le champ environment attendu par défaut ('development')
    assert response.json() == {
        "status": "healthy",
        "version": "1.0.0",
        "environment": "development",
    }


def test_read_item():
    response = client.get("/items/42?q=test")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "query": "test"}