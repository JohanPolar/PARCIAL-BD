import json
import boto3
from datetime import datetime
from bs4 import BeautifulSoup


def lambdaProc(event, context):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('landing-casas-3003')
    now = datetime.now()
    obj = bucket.Object('' + str(now.year) + '-' + str(now.month) + '-' + str(now.day) + '.html')
    body = obj.get()['Body'].read()
    soup = BeautifulSoup(body, 'html.parser')
    data_casas = soup.find_all('div', class_='listing listing-card')
    data_barrio = soup.find_all('div', class_='listing-card__location')
    data_precio = soup.find_all('div', class_='price')

    print(format)

    csv = "FechaDescarga, Barrio, Valor, NumHabitaciones, NumBanos, mts2\n"

    for i in range(len(data_casas)):
        download_date = now.strftime('%d-%m-%Y')
        barrio = (data_barrio[i].text)
        newBarrio = ""
        for j in barrio:
            newBarrio += j
        barrio = newBarrio.replace(',', '.')
        price = (data_precio[i].text)
        num_rooms = (f"{data_casas[i]['data-rooms']}")
        num_BRooms = (f"{data_casas[i].find_all('div', class_='listing-card__properties')[0].find_all('span')[1].text[:1]}")
        mts = (f"{data_casas[i].find_all('div', class_='listing-card__properties')[0].find_all('span')[2].text}")
        csv += f"{download_date}, {barrio}, {price}, {num_rooms}, {num_BRooms}, {mts}\n"

    client = boto3.client("s3")
    client.put_object(Body=csv, Bucket="casas-final-3003", Key='' + str(now.year) + '-' + str(now.month) + '-' + str(now.day) + '.csv')
    return {
        'statusCode': 202,
        'body': json.dumps('Hello from Lambda!')
    }
