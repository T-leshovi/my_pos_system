import pytest
from backend.app import app

@pytest.fixture
def client():
    # La función test_client() nos permite probar la app sin levantar el servidor real
    with app.test_client() as client:
        yield client

def test_health_endpoint(client):
    # Hacemos una petición GET a /health
    response = client.get("/health")
    assert response.status_code == 200
    assert response.data == b"OK"
