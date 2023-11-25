import requests
from credentials import *
from twilio.rest import Client
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

def send_whatsapp_msg(msg='hello world'):
    account_sid = sid
    auth_token = twilio_auth_token
    to_number = telefone

    client = Client(account_sid, auth_token)
    message = client.messages.create(body=msg, from_='whatsapp:+14155238886', to=to_number) # cria uma mensagem para o cliente com base nas informações passadas
    return message.sid

@sched.scheduled_job('interval', seconds=5) # determina qual intervalo que a requisição será solicitada e enviada
def get_last_coin_price(target_btc=190000.00, target_eth=15000.00): # enviará a mensagem sempre que o bitcoin estiver abaixo do valor declarado em target
    res_btc = requests.get('https://www.mercadobitcoin.net/api/BTC/ticker/') # api do bitcoin
    res_eth = requests.get('https://www.mercadobitcoin.net/api/ETH/ticker/') # api do ethereum
    last_price_btc = float(res_btc.json().get('ticker').get('last')) # retorna o último preco do bitcoin em json
    last_price_eth = float(res_eth.json().get('ticker').get('last'))  # retorna o último preco do etherium em json
    if last_price_btc <= target_btc or last_price_eth <= target_eth:
        return send_whatsapp_msg(f'Recebemos a solicitação! \nO preço do bitcoin agora é de: *R${round(last_price_btc, 2)}*. \nO preço do Ethereum é de: *R${round(last_price_eth, 2)}*. \nA diferença de preço entre as duas criptomoedas é de: *R${round(last_price_btc-last_price_eth, 2)}*') #chama a função 'send_whatsapp_msg' e retorna essa mensagem.

sched.start()