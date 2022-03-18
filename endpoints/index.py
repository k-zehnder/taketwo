from fastapi import APIRouter, status
from starlette.responses import RedirectResponse
from schemas import TagEnum

router = APIRouter()


@router.get(
    "/", 
    name="Home Page", 
    status_code=status.HTTP_200_OK, 
    description="API Documentation Page",
    summary="Index", 
    tags=[TagEnum.index]

)
async def main():
    return RedirectResponse(url="/docs/")