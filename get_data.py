import boto3
import os

from crowemi_trades.processes.process_get_data import ProcessGetData
from crowemi_trades.storage.s3_storage import S3Storage


def handler(event, context):
    role_info = {
        "RoleArn": "arn:aws:iam::926488920335:role/crowemi-trades-lambda-get-data",
        "RoleSessionName": "crowemi-trades-lambda-get-data",
    }

    client = boto3.client("sts")
    credentials = client.assume_role(**role_info)

    session = boto3.session.Session(
        aws_access_key_id=credentials["Credentials"]["AccessKeyId"],
        aws_secret_access_key=credentials["Credentials"]["SecretAccessKey"],
        aws_session_token=credentials["Credentials"]["SessionToken"],
    )
    process = ProcessGetData().run(
        storage=S3Storage(session=session),
        bucket=os.getenv("BUCKET", None),
        manifest_key="manifest.json",
    )
    assert process == True


if __name__ == "__main__":
    handler(None, None)
