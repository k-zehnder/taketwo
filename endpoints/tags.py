from typing import List
from fastapi import FastAPI
from helpers import Tag, get_all_tags, get_session, create_tag, get_current, update_tag, get_tag_by_name
import uvicorn
from fastapi import APIRouter
from starlette.responses import RedirectResponse

session = get_session()
router = APIRouter()

@router.get("/", name="Home Page", description="API Documentation Page.")
async def main():
    """API Documentation Page."""
    return "home"

@router.post("/increment", status_code=200,response_model=Tag)
def increment(tag: Tag):
    tags = get_tag_by_name(session, tag)
    if tags:
        current_value = get_current(tags)
        return update_tag(session, tag, current_value)
    print(f"[INFO] {tag.name} does not exist...adding..")
    return create_tag(session, tag)

@router.get("/get_tags", status_code=200,response_model=List[Tag])
def get_tags():
    return get_all_tags(session)




