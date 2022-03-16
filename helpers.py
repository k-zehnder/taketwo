from typing import List
import google.cloud.logging
from firebase_admin import credentials, firestore, initialize_app
from schemas import Tag, TagRead, TagCreate
from config import TAG_DB, CREDS


def update_tag(session, tag: Tag) -> Tag:
    tag_ref = session.collection(TAG_DB).document(tag.name)
    tag_ref.update({"value": firestore.Increment(tag.value)})

# def update_tag(session, tag: Tag) -> Tag:
#     tag_ref = session.collection(TAG_DB)
#     tag_ref = tag_ref.where("name", "==", tag.name)
#     tag_ref.update({"value": firestore.Increment(tag.value)})
#     return tag

def get_all_tags(session) -> List[Tag]:
    all_tags = session.collection(TAG_DB).stream()
    return [Tag(name=c.get("name"), value=c.get("value")) for c in all_tags]

def get_tag_sum(session) -> int:
    return sum(t.value for t in get_all_tags(session))

def get_tags_by_name(session, tag: Tag):
    tag_ref = session.collection(TAG_DB).document(tag.name)
    tag = tag_ref.get()
    return tag

def create_tag(session, tag: TagCreate) -> Tag:
    new_doc = session.collection(TAG_DB).document(tag.name)
    new_doc.set(tag.dict())  
    return tag

# def create_tag(session, tag: TagCreate) -> Tag:
#     new_doc = session.collection(TAG_DB).set(tag.dict())
#     return tag

def get_session():
    cred = credentials.Certificate(CREDS)
    default_app = initialize_app(cred)
    session = firestore.client()
    return session

def get_logger(name: str):
    client = google.cloud.logging.Client()
    logger = client.logger(name)
    return logger

def log_tag_sum(logger, tag_sum: int):
    logger.log(f"[TAG_TOTAL] {tag_sum}", 
        resource={"type":"global", 
        "labels":{
            "total" : "update"}
        })

def log_new_tag(logger, tag: TagCreate):
    print(f"[INFO] {tag.name} does not exist...adding..")
    logger.log(f"[NEW_TAG] {tag.name}", 
        resource={"type":"global", 
        "labels":{
            "tag" : "create"}
        })