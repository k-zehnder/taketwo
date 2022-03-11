from typing import List
import google.cloud.logging
from firebase_admin import credentials, firestore, initialize_app
from schemas import Tag, TagRead, TagCreate
from config import TAG_DB


def update_tag(session, tag: Tag, current_value: int) -> Tag:
    session.collection(TAG_DB).document(tag.name).update({
                'value': tag.value + current_value
            })
    return tag

def get_all_tags(session) -> List[Tag]:
    collection = session.collection(TAG_DB).stream()
    return [Tag(name=c.get("name"), value=c.get("value")) for c in collection]

def get_tag_sum(session) -> int:
    return sum(t.value for t in get_all_tags(session))

def get_tags_by_name(session, tag: Tag) -> list:
    return list(session.collection(TAG_DB).where(u'name', u'==', tag.name).stream())

def create_tag(session, tag: TagCreate) -> Tag:
    new_doc = session.collection(TAG_DB).document(tag.name)
    new_doc.set(tag.dict())  
    return tag

def get_current_value(tag: Tag) -> int:
    return tag[0].get("value")

def get_session():
    #Initialize Firestore DB
    cred = credentials.Certificate("./project3-343609-3de9eceebaa1.json")
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