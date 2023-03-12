import json
import boto3
from datetime import datetime

def lambdaProc(event, context):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('landing-casas-3003')
    obj = bucket.Object('' + str(now.year) + '-' + str(now.month) + '-' + str(now.day) + '.html')
    body = obj.get()['Body'].read()
    todo_item = json.loads(body)
    print(todo_item)

    return {
        'statusCode': 202,
        'body': json.dumps('Hello from Lambda!')
    }
