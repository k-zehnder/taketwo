from fastapi import APIRouter
from endpoints import tags, index
from schemas import Tags


router = APIRouter()


router.include_router(index.router, tags=Tags.index)
router.include_router(tags.router, tags=Tags.tags)


