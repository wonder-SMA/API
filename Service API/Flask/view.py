import os
from flask import render_template
import pymysql
from dotenv import load_dotenv
from app import app

load_dotenv()


def database():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        db='my_db',
        charset='utf8mb4',
        password=str(os.getenv("PASSWORD")),
        cursorclass=pymysql.cursors.DictCursor
    )
    sql = "SELECT * FROM coin ORDER BY date_time DESC"
    cursor = connection.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    connection.close()
    return data


@app.route('/history')
def history():
    data = database()
    l = []
    for part in data:
        l.append({1: f"Дата и время:  {str(part['date_time'])}"})
        l.append({2: f"Валюта:  {str(part['name'])}"})
        l.append({3: f"Цена:  {str(part['price'])}"})
        l.append({4: f"Количество монет в обороте:  {str(part['circulating_supply'])}"})
        l.append('-----')
    return render_template('history.html', data=l)


@app.route('/last')
def last():
    data = database()
    l = []
    for part in data[:1]:
        l.append({1: f"Дата и время:  {str(part['date_time'])}"})
        l.append({2: f"Валюта:  {str(part['name'])}"})
        l.append({3: f"Цена:  {str(part['price'])}"})
        l.append({4: f"Количество монет в обороте:  {str(part['circulating_supply'])}"})
    return render_template('last.html', data=l)
