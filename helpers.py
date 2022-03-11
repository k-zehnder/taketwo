import google.cloud.logging
from firebase_admin import credentials, firestore, initialize_app
from schemas import Tag
import re


def update_tag(session, tag, current_value):
    session.collection(u'tagdb').document(tag.name).update({
                'value': tag.value + current_value
            })
    return tag

def get_all_tags(session):
    collection = session.collection(u'tagdb').stream()
    return [Tag(name=c.get("name"), value=c.get("value")) for c in collection]

def get_tag_sum(session):
    return sum(t.value for t in get_all_tags(session))

def get_tags_by_name(session, tag):
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

def get_current_value(tag):
    return tag[0].get("value")

def log_tag_sum(logger, tag_sum):
    logger.log(f"[TAG_TOTAL] {tag_sum}", resource={"type":"global", 
        "labels":{"total" : "update"}})

def log_new_tag(logger, tag):
    print(f"[INFO] {tag.name} does not exist...adding..")
    logger.log(f"[NEW_TAG] {tag.name}", resource={"type":"global", 
        "labels":{"tag" : "create"}})

def get_logger(name):
    client = google.cloud.logging.Client()
    logger = client.logger(name) # name="post_count"
    return logger
