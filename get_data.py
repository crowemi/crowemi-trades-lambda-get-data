import boto3
import os

from crowemi_trades.processes.process_get_data import ProcessGetData
from crowemi_trades.storage.s3_storage import S3Storage


def handler(event, context):
    client = boto3.client("sts")
    credentials = client.get_session_token()["Credentials"]
    process = ProcessGetData().run(
        storage=S3Storage(
            session=boto3.Session(
                aws_access_key_id=credentials["AccessKeyId"],
                aws_secret_access_key=credentials["SecretAccessKey"],
                aws_session_token=credentials["SessionToken"],
            )
        ),
        bucket=os.getenv("BUCKET", None),
        manifest_key="manifest.json",
    )
    assert process == True


if __name__ == "__main__":
    handler(None, None)
