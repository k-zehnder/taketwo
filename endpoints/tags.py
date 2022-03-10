from typing import List
from fastapi import FastAPI
from helpers import Tag, get_all_tags, get_session, create_tag, get_current_value, update_tag, get_tag_by_name, sum_all_tags
from fastapi import APIRouter
from starlette.responses import RedirectResponse
from typing import Set
import google.cloud.logging

session = get_session()
router = APIRouter()

client = google.cloud.logging.Client()
logger = client.logger()

logger.warning("Hello World!")
logger.log(
    "an entry with fields set",
    severity="ERROR",
    insert_id="0123",
    labels={"my-label": "my-value"},
)  # API call


@router.get("/", name="Home Page", description="API Documentation Page.")
async def main():
    """API Documentation Page."""
    return RedirectResponse(url="/docs/")

@router.post("/increment", status_code=200, response_model=Tag)
def increment(tag: Tag):
    tags = get_tag_by_name(session, tag)
    if tags:
        current_value = get_current_value(tags)
        return update_tag(session, tag, current_value)
    print(f"[INFO] {tag.name} does not exist...adding..")
    return create_tag(session, tag)

@router.get("/get_tags", status_code=200, response_model=List[Tag])
def get_tags():
    tag_sum = sum_all_tags(session)
    print(f'[INFO] sum: {tag_sum}')
    # logger.log(f"Total request count: {tag_sum}"
    return get_all_tags(session)

