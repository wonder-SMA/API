import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import os
from dotenv import load_dotenv
from datetime import datetime
import pymysql
from time import sleep

load_dotenv()

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {
    'id': '1'}

headers = {
    'X-CMC_PRO_API_KEY': str(os.getenv("API_KEY")),
    'Accepts': 'application/json'}

session = requests.Session()
session.headers.update(headers)


def database(name, price, circulating_supply):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password=str(os.getenv("PASSWORD")),
        charset='utf8mb4'
    )
    create_db = ("""CREATE DATABASE IF NOT EXISTS my_db; USE my_db; CREATE TABLE IF NOT EXISTS coin (
        `date_time` DATETIME,
        `name` VARCHAR(255),
        `price` BIGINT,
        `circulating_supply` BIGINT
    )""")
    for element in create_db.split(';'):
        try:
            connection.cursor().execute(element)
            connection.commit()
        except:
            print('FAIL IN' + str(element))
    sql = "INSERT INTO coin (date_time, name, price, circulating_supply) VALUES (%s, %s, %s, %s)"
    val = (datetime.now(), name, price, circulating_supply)
    cursor = connection.cursor()
    cursor.execute(sql, val)
    connection.commit()
    connection.close()


def main():
    if headers['X-CMC_PRO_API_KEY'] != '':
        try:
            response = session.get(url, params=parameters)
            data = json.loads(response.text)
            name = data['data']['1']['name']
            price = data['data']['1']['quote']['USD']['price']
            circulating_supply = data['data']['1']['circulating_supply']
            database(name, price, circulating_supply)
        except (ConnectionError, Timeout, TooManyRedirects) as exc:
            print(exc)
    else:
        print('Check your API KEY!')


if __name__ == "__main__":
    time = float(os.getenv("TIME_OUT").strip()) * 60
    while True:
        main()
        sleep(time)
