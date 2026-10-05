import os
import boto3
from botocore.client import Config

FILE_NAME = "volchek_egor.html"

AWS_REGION_NAME = "EEUR"
AWS_ENDPOINT_URL = "https://8721af4803f2c3c631a90d8b64d397b7.r2.cloudflarestorage.com"
AWS_ACCESS_KEY = "fc1229e80fb7eed545fe6b9b9532bb6d"
AWS_SECRET_KEY = "86386672bf8536575c4f55d36420f300ddc43efe22c266bbf0c0e88fcb6e1b99"
AWS_PUBLIC_BASE_URL = "https://pub-d6d331676b6f46f0a66072646e49ac3c.r2.dev"
AWS_BUCKET_NAME = "group25082026"

def run():
    if not os.path.exists(FILE_NAME):
        print(f"Error: {FILE_NAME} not found!")
        return

    s3 = boto3.client(
        "s3",
        endpoint_url=AWS_ENDPOINT_URL,
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
        config=Config(signature_version="s3v4"),
        region_name="auto"
    )

    try:
        s3.upload_file(
            Filename=FILE_NAME,
            Bucket=AWS_BUCKET_NAME,
            Key=FILE_NAME,
            ExtraArgs={"ContentType": "text/html"}
        )
        print(f"{AWS_PUBLIC_BASE_URL}/{FILE_NAME}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run()
