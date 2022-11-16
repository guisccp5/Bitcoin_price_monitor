import requests
from twilio.rest import Client
import os
from infos import *
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

account_sid = os.environ.get('TWILIO_ACCOUNT_SID') #declaração da variável de ambiente (deve ser declarada nas configurações também)
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
to_number = os.environ.get('TELEPHONE_NUMBER')

def send_whatsapp_msg(msg='hello world'):
    client = Client(account_sid, auth_token)
    message = client.messages.create(body=msg, from_='whatsapp:+14155238886', to=to_number) #cria uma mensagem para o cliente com base nas informações passadas
    return message.sid

@sched.scheduled_job('interval', seconds=10) #determina o intervalo que a requisição será solicitada e enviada
def get_last_bitcoin_price(target=100000): #enviará a mensagem sempre que o bitcoin estiver abaixo de R$100.000,00
    res = requests.get('https://www.mercadobitcoin.net/api/BTC/ticker/') #api do bitcoin
    last_price = float(res.json().get('ticker').get('last')) #retorna o último preco do bitcoin em json
    if last_price <= target:
        return send_whatsapp_msg(f'Recebemos a solicitação. O preço do bitcoin agora é de: R${last_price}') #chama a função 'send_whatsapp_msg' e retorna essa mensagem.

sched.start()