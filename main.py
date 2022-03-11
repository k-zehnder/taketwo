from fastapi import FastAPI
from routers import router


app = FastAPI(
    title="MyTakeHomeTest",
    description="A simple API Service built with FastAPI",
    version="0.1"
)

app.include_router(router)

