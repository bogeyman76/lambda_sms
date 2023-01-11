import json
import boto3


def lambda_handler(event, context):
    sns = boto3.client('sns')
    
    sns.publish(PhoneNumber = event['number'], Message=event['msg'])
    
    return {
        'statusCode': 200,
        'body': json.dumps('Message sent successfully.')
    }
