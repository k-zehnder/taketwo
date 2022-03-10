from typing import List
from fastapi import FastAPI
from helpers import Tag, get_all_tags, get_session, create_tag, get_current_value, update_tag, get_tag_by_name, sum_all_tags
from fastapi import APIRouter
from starlette.responses import RedirectResponse

import google.cloud.logging
import logging
from datetime import datetime, timedelta, timezone
import os

session = get_session()
router = APIRouter()

client = google.cloud.logging.Client()
client.setup_logging()# use Python’s standard logging library to send logs to GCP

@router.get("/", name="Home Page", description="API Documentation Page.")
async def main():
    """API Documentation Page."""
    return RedirectResponse(url="/docs/")

@router.post("/increment", status_code=200, response_model=Tag)
def increment(tag: Tag):
    tags = get_tag_by_name(session, tag)
    if tags:
        current_value = get_current_value(tags)
        return update_tag(session, tag, current_value)
    print(f"[INFO] {tag.name} does not exist...adding..")
    return create_tag(session, tag)

@router.get("/get_tags", status_code=200, response_model=List[Tag])
def get_tags():
    tag_sum = sum_all_tags(session)
    print(f'[INFO] sum: {tag_sum}')
    logging.info("logging sum", extra={
        "labels": {"type": "app_health"},
        "trace": "01234" # + uuid
    })
    return get_all_tags(session)




