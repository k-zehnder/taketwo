# set up the Google Cloud Logging python client library
from google.cloud.logging import DESCENDING
import google.cloud.logging
import logging
import json

import google.cloud.logging
from datetime import datetime, timedelta, timezone
import os

client = google.cloud.logging.Client()
client.setup_logging()# use Python’s standard logging library to send logs to GCP



yesterday = datetime.now(timezone.utc) - timedelta(minutes=10)
# Cloud Logging expects a timestamp in RFC3339 UTC "Zulu" format
# https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry
time_format = "%Y-%m-%dT%H:%M:%S.%f%z"
# build a filter that returns activity in the past 24 hours
# https://cloud.google.com/kubernetes-engine/docs/how-to/audit-logging
filter_str = (
    f'timestamp>="{yesterday.strftime(time_format)}"'
)
# query and print all matching logs
client = google.cloud.logging.Client()
for entry in client.list_entries(filter_=filter_str):
    print(entry)
    print()
    print()