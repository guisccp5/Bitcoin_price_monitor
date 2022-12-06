# Bitcoin Price Monitor
 
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/imguisilva/Bitcoin_price_monitor/blob/main/LICENSE) 

# Sobre o projeto

Bitcoin Price Monitor é um chatbot desenvolvido em python que realiza o deploy no heroku.

A aplicação consiste em realizar uma requisição em uma API de criptomoedas, onde é coletado último valor de bitcoin, e depois o valor e enviado para um número de whatsapp e atualizado a cada dez segundos até que o deploy no heroku seja interrompido.

## Representação
![Requisição via Wpp](https://github.com/imguisilva/Bitcoin_price_monitor/blob/main/atualizacao-bitcoin.png)

# Tecnologias utilizadas
## Back end
- Python
## Implantação em produção
- Back end: Heroku
- API Whatsapp: Twilio
- API Bitcoin: Mercado Bitcoin

# Como executar o projeto

## Back end
Pré-requisitos: Python 3.9 ou superior

```bash
# clonar repositório
git clone https://github.com/imguisilva/Bitcoin_price_monitor

# instalar dependências
pip install -r requirements.txt

# definir as variáveis de ambiente
heroku config:set AUTH_TOKEN='auth_token' (sem as aspas)
heroku config:set ACCOUNT_SID='account_sid'
heroku config:set TELEPHONE_NUMBER='to_number'

As variáveis devem ser definidas também em: Edit Configurations > Environment variables (Pycharm)

# logar no heroku
heroku login

# executar o bot digitando: 
heroku ps:scale clock=1 (on)
heroku ps:scale clock=0 (off) 

```

# Autor

Guilherme Pereira

https://www.linkedin.com/in/imguilhermesilva/
 
