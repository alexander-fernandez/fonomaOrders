from starlette.testclient import TestClient
from main import app
import json

client = TestClient(app)


def test_hello():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_solution_all():
    json_body = {"orders":[{"id":1,"item":"Laptop","quantity":1,"price":999.99,"status":"completed"},{"id":2,"item":"Smartphone","quantity":2,"price":499.95,"status":"pending"},{"id":3,"item":"Headphones","quantity":3,"price":99.9,"status":"completed"},{"id":4,"item":"Mouse","quantity":4,"price":24.99,"status":"canceled"}],"criterion":"all"}
    response = client.post("/solution", json=json_body)
    assert response.status_code == 200
    assert response.json() == "2399.55"


def test_solution_completed():
    json_body = {"orders":[{"id":1,"item":"Laptop","quantity":1,"price":999.99,"status":"completed"},{"id":2,"item":"Smartphone","quantity":2,"price":499.95,"status":"pending"},{"id":3,"item":"Headphones","quantity":3,"price":99.9,"status":"completed"},{"id":4,"item":"Mouse","quantity":4,"price":24.99,"status":"canceled"}],"criterion":"completed"}
    response = client.post("/solution", json=json_body)
    assert response.status_code == 200
    assert response.json() == "1299.69"


def test_solution_pending():
    json_body = {"orders":[{"id":1,"item":"Laptop","quantity":1,"price":999.99,"status":"completed"},{"id":2,"item":"Smartphone","quantity":2,"price":499.95,"status":"pending"},{"id":3,"item":"Headphones","quantity":3,"price":99.9,"status":"completed"},{"id":4,"item":"Mouse","quantity":4,"price":24.99,"status":"canceled"}],"criterion":"pending"}
    response = client.post("/solution", json=json_body)
    assert response.status_code == 200
    assert response.json() == "999.9"


def test_solution_failed():
    json_body = {"orders":[{"id":"a","item":"Laptop","quantity":1,"price":999.99,"status":"completed"},{"id":2,"item":"Smartphone","quantity":2,"price":499.95,"status":"pending"},{"id":3,"item":"Headphones","quantity":3,"price":99.9,"status":"completed"},{"id":4,"item":"Mouse","quantity":4,"price":24.99,"status":"canceled"}],"criterion":"completed"}
    response = client.post("/solution", json=json_body)
    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"] == "value is not a valid integer"
