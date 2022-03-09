from fastapi import APIRouter
from endpoints import tags

router = APIRouter()

router.include_router(tags.router, tags=["Tags"])
