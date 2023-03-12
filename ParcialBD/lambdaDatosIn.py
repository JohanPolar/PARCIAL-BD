import json
import boto3
from urllib.request import urlopen
from datetime import datetime


def lambdaDatos(event, context):
    # TODO implement
    url = 'https://casas.mitula.com.co/searchRE/nivel1-Cundinamarca/nivel2-Bogot%C3%A1/nivel3-Chapinero/orden-0/op-1/m2_min-1/m2_max-200/hab_min-1/ban_min-1/q-bogot%C3%A1?req_sgmt=REVTS1RPUDtVU0VSX1NFQVJDSDtTRVJQOw=='
    now = datetime.now()
    with urlopen(url) as response:
        body = response.read()
    client = boto3.client("s3")
    client.put_object(Body=body, Bucket="landing-casas-3003", Key="" + str(now.year) + "-" + str(now.month) + "-" + str(now.day) + ".html")
    return {
        'statusCode': 202,
        'body': json.dumps('Hello from Lambda!')
    }
