import boto3
from datetime import datetime
import requests


def downloadHTML():
    try:
        s3 = boto3.resource('s3')
        bucket = s3.Bucket('landing-casas-3003')
        now = datetime.now()
        obj = bucket.Object('' + str(now.year) + '-' + str(now.month) + '-' + str(now.day) + '.html')
        obj.get()['Body'].read()
        return True
    except ValueError:
        return False


def isntnullHTML():
    try:
        s3 = boto3.resource('s3')
        bucket = s3.Bucket('landing-casas-3003')
        now = datetime.now()
        obj = bucket.Object('' + str(now.year) + '-' + str(now.month) + '-' + str(now.day) + '.html')
        body = obj.get()['Body'].read()
        if body is None:
            return False
        else:
            return True
    except ValueError:
        return False


def rqt_Mitula(url, header, json):
    rpta = requests.post(url, headers=header, json=json)
    return rpta
