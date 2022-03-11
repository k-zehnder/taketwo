from firebase_admin import credentials, firestore
from starlette.testclient import TestClient
from schemas import Tag
from main import app
import pytest 


client = TestClient(app)


def test_app_init():
    response = client.get("/")
    assert response.status_code == 200

def test_db_init():
    session = firestore.client()
    cred = credentials.Certificate("./project3-343609-3de9eceebaa1.json")
    assert cred != None
    assert session != None

def test_create_tag():
    response = client.post(
        "/increment",
        json={"name": "init_foo", "value": 0},
    )
    assert response.status_code == 201
    assert response.json() == {
            "name": "init_foo",
            "value": 0
        }

def test_read_tag():
    response = client.get("/tags")
    assert response.status_code == 200
    assert response.json() == {
            "data": [{"name": "init_foo", "value": 0}]
        }

def test_increment_tag():
    response = client.post(
        "/increment",
        json={"name": "init_foo", "value": 1}
    )
    assert response.status_code == 201
    assert response.json() == {
            "name": "init_foo",
            "value": 1
        }

@pytest.mark.parametrize(
    "tag, exp", [
        [Tag(name="tim", value=1), True], 
        [Tag(name="joe", value=2), True]
    ]
)
def test_foo(tag, exp):
    assert isinstance(tag, Tag) == exp