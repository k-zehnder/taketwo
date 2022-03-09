from fastapi import APIRouter
from api_functions import ResponseModel, ErrorResponseModel
import geocoder

router = APIRouter()

# forward geocoding
@router.get("/hello", name="Hello", description="Testing if I work")
async def hello():
    return "success"
