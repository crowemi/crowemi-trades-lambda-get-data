import os
import json
from datetime import datetime, timedelta

from crowemi_helps.aws.aws_s3 import AwsS3
from crowemi_trades.utilities.get_daily_data import get_daily_data

CLIENT = AwsS3()
BUCKET = os.getenv("BUCKET")
MANIFEST_NAME = "manifest.json"


def handler(manifest_path: str = None):
    # pull extract instructions from S3
    if not manifest_path:
        manifest = CLIENT.get_object(BUCKET, MANIFEST_NAME)
    else:
        with open(manifest_path) as f:
            manifest = json.loads(f.read())

    list(map(get_data, manifest))
    CLIENT.write_s3(MANIFEST_NAME, BUCKET, json.dumps(manifest))


def get_data(record):
    ticker = record.get("ticket", None)
    timespan = record.get("timespan", None)
    interval = record.get("interval", None)
    bucket = record.get("bucket", None)
    # process last_modified
    last_modified = record.get("last_modified", None)
    today = datetime.utcnow()
    start_date = datetime(
        year=int(last_modified[0:4]),
        month=int(last_modified[4:6]),
        day=int(last_modified[6:8]),
    ) + timedelta(days=1)
    end_date = today + timedelta(days=-1)

    if start_date < end_date:
        ret = get_daily_data(
            ticker,
            timespan,
            interval,
            start_date,
            end_date,
            bucket,
        )
        # TODO: confirm ret was successful

    # update manifest last modified date
    record["last_modified"] = f"{end_date.year}{end_date.month:02}{end_date.day:02}"


if __name__ == "__main__":
    handler("manifest.json")