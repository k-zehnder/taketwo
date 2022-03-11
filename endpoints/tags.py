from typing import List
from helpers import get_all_tags, get_session, get_logger, create_tag, get_current_value, update_tag, get_tags_by_name, get_tag_sum, log_tag_sum, log_new_tag
from fastapi import APIRouter, status
from schemas import Tag
import google.cloud.logging


router = APIRouter()

logger = get_logger("post_count")
session = get_session()


@router.get("/get_tags", status_code=status.HTTP_200_OK, response_model=List[Tag], description="Get all Tags.", tags=["Tags"])
async def get_tags():
    tag_sum = get_tag_sum(session)
    log_tag_sum(logger, tag_sum)
    return get_all_tags(session)

@router.post("/increment_tag", description="Alter Tag state.", status_code=status.HTTP_201_CREATED, response_model=Tag, tags=["Tags"])
async def increment_tag(tag: Tag):
    existing_tag = get_tags_by_name(session, tag)
    if existing_tag:
        current_value = get_current_value(existing_tag)
        return update_tag(session, tag, current_value)
    log_new_tag(logger, tag)
    return create_tag(session, tag)




