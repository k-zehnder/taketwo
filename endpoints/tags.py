from typing import List
from fastapi import FastAPI
from helpers import Tag, get_all_tags, get_session, create_tag, get_current_value, update_tag, get_tag_by_name, sum_all_tags
from fastapi import APIRouter
from starlette.responses import RedirectResponse
from typing import Set


session = get_session()
router = APIRouter()


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
    # all_tags = get_all_tags(session)
    # logger.log(f"Total request count: {len(all_tags)}")
    summ = sum_all_tags(session)
    print(f'[INFO] sum: {summ}')
    return get_all_tags(session)




