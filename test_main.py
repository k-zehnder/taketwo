from fastapi import status
from firebase_admin import credentials, firestore
from starlette.testclient import TestClient
from schemas import Tag
from main import app
import pytest 
from config import CREDS


client = TestClient(app)


def test_app_init():
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK

def test_db_init():
    session = firestore.client()
    cred = credentials.Certificate(CREDS)
    assert cred != None
    assert session != None

def test_create_tag():
    response = client.post(
        "/increment",
        json={"name": "init_foo", "value": 0},
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {
            "name": "init_foo",
            "value": 0
        }

def test_read_tag():
    response = client.get("/tags")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
            "data": [{"name": "init_foo", "value": 0}]
        }

def test_increment_tag():
    response = client.post(
        "/increment",
        json={"name": "init_foo", "value": 1}
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {
            "name": "init_foo",
            "value": 1
        }

@pytest.mark.parametrize(
    "tag, expected", [
        [Tag(name="alice", value=0), True], 
        [Tag(name="bob"), True]
    ]
)
def test_default_value(tag, expected):
    assert isinstance(tag, Tag) == expected
    assert tag.value == 0