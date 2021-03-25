import pytest

from app import main

@pytest.fixture
def flask_app():
    yield main.app

@pytest.fixture
def client(flask_app):
    return flask_app.test_client()

def test_index(flask_app, client):
    res = client.get('/')
    assert res.status_code == 200
