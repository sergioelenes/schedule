from flask import Flask, render_template
from flask_apscheduler import APScheduler
from datetime import datetime, timedelta
from apscheduler.triggers.interval import IntervalTrigger
import requests
import os
from dotenv import load_dotenv

load_dotenv('dt.env')

bt = '5133345908:AAHWId08dwpEafQoo0Kv3NtfpSyLrT6pM4Y'
cid = '-918593451'

app = Flask(__name__)
scheduler = APScheduler()

# Configuración de la programación en segundo plano
def send_telegram_message():
    now=datetime.now()
    bot_token = bt
    chat_id = cid
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    message = f'Hola, esto es una prueba de mensaje en Telegram | {now}'
    data = {'chat_id': chat_id, 'text': message}
    response = requests.post(url, data=data)
    print(response.json())

#scheduler.add_job(id='send_telegram_message', func=send_telegram_message, trigger='interval', days=3, start_date=datetime.now()+timedelta(seconds=1), timezone='America/Mazatlan')
scheduler.add_job(id='send_telegram_message', func=send_telegram_message, trigger=IntervalTrigger(minutes=10), start_date=datetime.now()+timedelta(seconds=1))
# Inicialización de la programación en segundo plano
scheduler.init_app(app)
scheduler.start()

# Rutas de la aplicación Flask
@app.route("/", methods=['GET','POST'])
def inicio():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
