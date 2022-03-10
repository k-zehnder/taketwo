from typing import List
from helpers import get_all_tags, get_session, create_tag, get_current_value, update_tag, get_tags_by_name, sum_all_tags, log_tag_sum
from fastapi import APIRouter
from schemas import Tag
from starlette.responses import RedirectResponse
import google.cloud.logging


session = get_session()
router = APIRouter()

client = google.cloud.logging.Client()
logger = client.logger(name="post_count")


@router.get("/", name="Home Page", status_code=200, description="API Documentation Page.")
async def main():
    return RedirectResponse(url="/docs/")

@router.post("/increment", status_code=200, response_model=Tag)
async def increment(tag: Tag):
    existing_tag = get_tags_by_name(session, tag)
    if existing_tag:
        return update_tag(session, tag)
    print(f"[INFO] {tag.name} does not exist...adding..")
    return create_tag(session, tag)

@router.get("/get_tags", status_code=200, response_model=List[Tag])
async def get_tags():
    tag_sum = sum_all_tags(session)
    log_tag_sum(logger, tag_sum)
    return get_all_tags(session)

