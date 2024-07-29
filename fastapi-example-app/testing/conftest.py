from fastapi.testclient import TestClient
from pytest import fixture
from main import app


@fixture
def client():
    return TestClient(app)
