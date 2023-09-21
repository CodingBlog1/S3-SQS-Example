import boto3

AWS_REGION = "Enter-your-region"
AWS_ACCESS_KEY_ID = "enter-your-access-key-id"
AWS_SECRET_ACCESS_KEY = "enter-your-secret-access-key"

session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION,
)

sqs = session.client("sqs")
print(sqs)
