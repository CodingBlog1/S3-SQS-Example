# sqs_app/views.py

from django.http import JsonResponse

# from django.conf import settings
from app.aws import sqs

URLQUEUE = "Enter you queue URL here"

#send the messages
def send_message_to_sqs(request):
    queue_url = URLQUEUE
    message = f"Hello dillu your order has been placed with orderID {1234} and the delevry address is dillu kka ghar "
    sqs.send_message(QueueUrl=queue_url, MessageBody=message)
    return JsonResponse({"status": "Message sent to SQS successfully"})

#get the messages
def retrive_mesage(request):
    queue_url = URLQUEUE

    response = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=1,
        VisibilityTimeout=50,
        WaitTimeSeconds=0,
    )

    messages = response.get("Messages", [])
    if messages:
        message_body = messages[0]["Body"]
        receipt_handle = messages[0]["ReceiptHandle"]
        # delete the msg from the queue
        sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=receipt_handle)

        return JsonResponse(
            {
                "status": "Message retrieved from SQS successfully",
                "message_body": message_body,
            }
        )
    else:
        return JsonResponse({"status": "No messages available in the queue"})
