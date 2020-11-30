import pytest
import json
from .app import app


@pytest.fixture
def client():
    return app.test_client()


def test_get_list(client):
    req = client.get("/api/list")
    text_contents = req.data.decode()
    assert json.loads(text_contents) == {"scores": []}


def test_put_new(client):

    req = client.put("/api/new", json={"name": "Test", "score": 100, "date": "10:44:38.491000"})

    assert req.status_code == 204

    req = client.get("/api/list")
    assert req.get_json() == {"scores": [{"name": "Test", "score": 100, "date": "10:44:38.491000"}]}

    req = client.put("/api/new", json={"name": "invalid"})
    assert req.status_code == 400

    req = client.put("/api/new")
    assert req.status_code == 400


def test_delete_list(client):


    client.put("/api/new", json={"name": "Test", "score": 100})

    req = client.delete("/api/list", json={"name": "Test"})
    assert req.status_code == 204

    req = client.get("/api/list")
    assert req.get_json() == {"scores": []}

    req = client.delete("/api/list")
    assert req.status_code == 400




