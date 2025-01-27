from os import getenv
from boto3 import client
from sys import stderr

def lambda_handler(event, context) -> None:
    try:
        message = event.get('message')

        if message:
            sns = client('sns')
            publich_message = sns.publish(
                TopicArn=getenv('TOPIC_ARN'),
                Message=message
            )

    except Exception as e:
        stderr.write(str(e))

    finally:
        return None
