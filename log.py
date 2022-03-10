from google.cloud.logging import DESCENDING
import google.cloud.logging
from datetime import datetime, timedelta, timezone


# query and print all matching log
def get_logs(logger, filter_str):
    for entry in logger.list_entries(filter_=filter_str):
        print(entry)
        print()
        print()


if __name__ == "__main__":
    client = google.cloud.logging.Client()
    logger = client.logger(name="post_count")

    yesterday = datetime.now(timezone.utc) - timedelta(minutes=100)
    # Cloud Logging expects a timestamp in RFC3339 UTC "Zulu" format
    # https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry
    time_format = "%Y-%m-%dT%H:%M:%S.%f%z"
    # build a filter that returns activity in the past 24 hours
    # https://cloud.google.com/kubernetes-engine/docs/how-to/audit-logging
    filter_str = (
        f'timestamp>="{yesterday.strftime(time_format)}"'
    )
    
    get_logs(logger, filter_str)

    