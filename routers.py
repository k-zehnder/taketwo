from fastapi import APIRouter
from endpoints import home_page, tags

router = APIRouter()

router.include_router(home_page.router, tags=["Home"])
router.include_router(tags.router, tags=["Tags"])
