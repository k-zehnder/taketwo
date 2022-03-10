from fastapi import FastAPI
from firebase_admin import credentials, firestore, initialize_app
from starlette.testclient import TestClient
from helpers import Tag, get_all_tags, get_session, create_tag, get_current_value, update_tag, get_tag_by_name
from main import app

# USAGE python -m pytest

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
    assert response.status_code == 200
    assert response.json() == {
            "name": "init_foo",
            "value": 0
        }

def test_read_tag():
    response = client.get("/get_tags")
    assert response.status_code == 200
    assert response.json() == [{
            "name": "init_foo",
            "value": 0
        }]

def test_increment_tag():
    response = client.post(
        "/increment",
        json={"name": "init_foo", "value": 1},
    )
    assert response.status_code == 200
    assert response.json() == {
            "name": "init_foo",
            "value": 1
        }

# def test_read_item_bad_count():
#     response = client.get("/items/foo", headers={"X-Token": "hailhydra"})
#     assert response.status_code == 400
#     assert response.json() == {"detail": "Invalid X-Token header"}


# def test_read_item_bad_token():
#     response = client.get("/items/foo", headers={"X-Token": "hailhydra"})
#     assert response.status_code == 400
#     assert response.json() == {"detail": "Invalid X-Token header"}


# def test_read_inexistent_item():
#     response = client.get("/items/baz", headers={"X-Token": "coneofsilence"})
#     assert response.status_code == 404
#     assert response.json() == {"detail": "Item not found"}



# def test_create_item_bad_token():
#     response = client.post(
#         "/items/",
#         headers={"X-Token": "hailhydra"},
#         json={"id": "bazz", "title": "Bazz", "description": "Drop the bazz"},
#     )
#     assert response.status_code == 400
#     assert response.json() == {"detail": "Invalid X-Token header"}


# def test_create_existing_item():
#     response = client.post(
#         "/items/",
#         headers={"X-Token": "coneofsilence"},
#         json={
#             "id": "foo",
#             "title": "The Foo ID Stealers",
#             "description": "There goes my stealer",
#         },
#     )
#     assert response.status_code == 400
#     assert response.json() == {"detail": "Item already exists"}
