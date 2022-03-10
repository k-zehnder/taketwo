from firebase_admin import credentials, firestore, initialize_app
from schemas import Tag


def update_tag(session, tag, current_value):
    session.collection(u'tagdb').document(tag.name).update({
                'value': tag.value + current_value
            })
    return tag

def get_all_tags(session):
    collection = session.collection(u'tagdb').stream()
    return [Tag(name=c.get("name"), value=c.get("value")) for c in collection]

def sum_all_tags(session):
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

def get_current_value(tags):
    return tags[0].get("value")

def log_tag_sum(logger, tag_sum):
    logger.log(f"[TAG_TOTAL] {tag_sum}", resource={"type":"global", 
        "labels":{"total" : "update"}})

"""
Example of total tag count payload stored in Google Cloud Platform.
{
    insertId: "1l5w75vfh4rv49"
    logName: "projects/project3-343609/logs/post_count"
    receiveTimestamp: "2022-03-10T06:38:49.656625022Z"
    resource: {
    labels: {
        project_id: "project3-343609"
    }
        type: "global"
    }
    textPayload: "[TAG_TOTAL] 1"
    timestamp: "2022-03-10T06:38:49.656625022Z"
}
"""