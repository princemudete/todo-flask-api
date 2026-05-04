import pytest

from app import create_app
from app.models import db, Todo


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.drop_all()


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json() == {"message": "Flask TODO API running"}


def test_get_todos_empty(client):
    response = client.get("/todos")
    assert response.status_code == 200
    assert response.get_json() == []


def test_create_todo(client):
    data = {"title": "Test Todo", "description": "Test description"}
    response = client.post("/todos", json=data)
    assert response.status_code == 201
    todo = response.get_json()
    assert todo["title"] == "Test Todo"
    assert todo["description"] == "Test description"
    assert todo["completed"] is False


def test_get_todo(client):
    data = {"title": "Test Todo"}
    response = client.post("/todos", json=data)
    todo_id = response.get_json()["id"]

    response = client.get(f"/todos/{todo_id}")
    assert response.status_code == 200
    todo = response.get_json()
    assert todo["title"] == "Test Todo"


def test_update_todo(client):
    data = {"title": "Test Todo"}
    response = client.post("/todos", json=data)
    todo_id = response.get_json()["id"]

    update_data = {"title": "Updated Todo", "completed": True}
    response = client.put(f"/todos/{todo_id}", json=update_data)
    assert response.status_code == 200
    todo = response.get_json()
    assert todo["title"] == "Updated Todo"
    assert todo["completed"] is True


def test_delete_todo(client):
    data = {"title": "Test Todo"}
    response = client.post("/todos", json=data)
    todo_id = response.get_json()["id"]

    response = client.delete(f"/todos/{todo_id}")
    assert response.status_code == 204

    response = client.get(f"/todos/{todo_id}")
    assert response.status_code == 404
