from fastapi import APIRouter
from endpoints import tags, index


router = APIRouter()


router.include_router(index.router, tags=["Index"])
router.include_router(tags.router, tags=["Tags"])


