# Failing to Set Authenticate on Unsubscribe to true
import boto3
import logging

def authenticate_on_subscribe(event) -> None:
    subscriptions_failed = 0
    for record in event['Records']:
        message = record['Message']
        if message['Type'] == 'SubscriptionConfirmation':
            try:
                topic_arn = message['TopicArn']
                Token = message['Token']
                sns_client = boto3.client(
                    'sns', region_name=topic_arn.split(':')[3])
                sns_client.confirm_subscription(
                    TopicArn=topic_arn, Token=Token)
            except Exception:
                subscriptions_failed += 1
                logging.error("Failed to confirm subscription")
                logging.error(Exception)