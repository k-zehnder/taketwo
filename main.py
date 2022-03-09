from fastapi import FastAPI
from routers import router

# fastapi app
app = FastAPI(
    title="MyTakeHomeTest",
    description="A simple API Service built with FastAPI",
    version="0.1"
)

app.include_router(router)


# uvicorn main:app --reload