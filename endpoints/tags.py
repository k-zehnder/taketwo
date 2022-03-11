from helpers import get_all_tags, get_session, get_logger, create_tag, get_current_value, update_tag, get_tags_by_name, get_tag_sum, log_tag_sum, log_new_tag
from fastapi import APIRouter, status
from schemas import Tag, TagCreate, TagRead


router = APIRouter()

logger = get_logger("post_count")
session = get_session()


@router.get(
    "/get_tags", 
    status_code=status.HTTP_200_OK, 
    response_model=TagRead, 
    summary="Get all tags.", 
    tags=["Tags"]
)
async def get_tags():
    """
    Get all Tag objects from GCP Firestore DB.
    """
    tag_sum = get_tag_sum(session)
    log_tag_sum(logger, tag_sum)
    return TagRead(data=get_all_tags(session))

@router.post(
    "/increment_tag", 
    summary="Increment Tag value.", 
    status_code=status.HTTP_201_CREATED, 
    response_model=Tag, 
    tags=["Tags"]
)
async def increment_tag(tag: TagCreate):
    """
    Create/Update a Tag object with all the information:

    - **name**: each item must have a name [a-z_]{3, 15}
    - **value**: each item must have a value 0 <= value < 10
    """
    existing_tag = get_tags_by_name(session, tag)
    if existing_tag:
        current_value = get_current_value(existing_tag)
        return update_tag(session, tag, current_value)
    log_new_tag(logger, tag)
    return create_tag(session, tag)




