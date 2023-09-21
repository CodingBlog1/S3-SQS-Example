import boto3

AWS_REGION = "Enter-your-region"
AWS_ACCESS_KEY_ID = "enter-your-access-key-id"
AWS_SECRET_ACCESS_KEY = "enter-your-secret-access-key"

BUCKET_NAME = "Enter-your-bucket-name"

file_name = "Enter the file name what you want to upload on the s3 bucket"

session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION,
)

s3 = session.resource("s3")
s3.meta.client.upload_file(Filename=file_name, Bucket=BUCKET_NAME, Key=file_name)
