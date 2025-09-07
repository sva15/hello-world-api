from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_hello_world():
    """Test the root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_hello_name():
    """Test the personalized hello endpoint."""
    response = client.get("/hello/John")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello John"}

def test_hello_name_with_spaces():
    """Test hello endpoint with spaces in name."""
    response = client.get("/hello/John%20Doe")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello John Doe"}
