from fastapi import FastAPI
from firebase_admin import credentials, firestore, initialize_app
from fastapi import FastAPI
from pydantic import BaseModel


class Tag(BaseModel):
    #TODO: set validators for constraints in the problem definition
    name: str
    value: int

    class Config:
        orm_mode = True


def update_tag(session, tag, current_value):
    session.collection(u'tagdb').document(tag.name).update({
                'value': tag.value + current_value
            })
    return tag

def get_all_tags(session):
    collection = session.collection(u'tagdb').stream()
    return [Tag(name=c.get("name"), value=c.get("value")) for c in collection]

def get_tag_by_name(session, tag):
    return list(session.collection(u'tagdb').where(u'name', u'==', tag.name).stream())

def create_tag(session, tag):
    new_doc = session.collection(u'tagdb').document(tag.name)
    new_doc.set(tag.dict())  
    return tag

def get_session():
    #Initialize Firestore DB
    cred = credentials.Certificate("./project3-343609-3de9eceebaa1.json")
    default_app = initialize_app(cred)
    session = firestore.client()
    return session

def get_current_value(tags):
    return tags[0].get("value")