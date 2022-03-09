from fastapi import FastAPI
from firebase_admin import credentials, firestore, initialize_app
from fastapi import FastAPI
from typing import Set
from pydantic import BaseModel, validator
import string
import re


VALID_NAME_CHARACTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' 
VALID_NAME_RANGE = [str(i) for i in range(3, 16)]


def is_valid_digits(query):
    matched = re.findall('\d+', query)
    return all(m in VALID_NAME_RANGE for m in matched)

def is_valid_chars(query):
    return any(char not in VALID_NAME_CHARACTERS for char in query if char.isalpha())

class Tag(BaseModel):
    name: str
    value: int

    @validator("name")
    def is_valid_name(cls, name):
        print(is_valid_digits(name))
        valid_name = is_valid_digits(name)
        if not valid_name:
             raise ValueError("Bad name, digits are {3, 15}.") 
        valid_chars = is_valid_chars(name)      
        if valid_chars:
            raise ValueError("Bad name, must be character.")
        return name

    @validator("value")
    def is_valid_value(cls, value):
        """Validator to check whether value is valid"""
        if not 0 <= value < 10:
            raise ValueError("Bad value, must be integer and 0 <= integer < 10")
        return value

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