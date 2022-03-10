from fastapi import APIRouter, status
from starlette.responses import RedirectResponse


router = APIRouter()

@router.get("/", name="Home Page", status_code=status.HTTP_200_OK, description="API Documentation Page.")
async def main():
    return RedirectResponse(url="/docs/")