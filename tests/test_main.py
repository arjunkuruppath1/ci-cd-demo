
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_home_endpoint():
    response = client.get("/")

    assert response.status_code == 200

    assert response.json() == {
        "message": "Welcome to CI/CD Demo API"
    }


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200

    assert response.json() == {
        "status": "healthy"
    }


def test_get_user_endpoint():
    response = client.get("/users/101")

    assert response.status_code == 200

    assert response.json() == {
        "user_id": 101,
        "name": "Arjun"
    }


def test_invalid_user_id():
    response = client.get("/users/abc")

    assert response.status_code == 422
