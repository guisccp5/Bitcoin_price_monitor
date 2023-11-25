# Bitcoin and Ethereum Price Monitor
 
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/imguisilva/Bitcoin_price_monitor/blob/main/LICENSE) 

# Sobre o projeto

Bitcoin and Ethereum Price Monitor é um chatbot desenvolvido em python que envia mensagens no whatsapp.

A aplicação consiste em realizar uma requisição em uma API de criptomoedas (mercado bitcoin), onde é coletado último valor do bitcoin e do ethereum, e depois o valor e enviado para um número de whatsapp e atualizado a cada cinco segundos até que a execução do mesmo seja interrompida.

## Representação
![Requisição via Wpp](https://github.com/imguisilva/Bitcoin_price_monitor/blob/main/captura-twilio.PNG?raw=true)

# Tecnologias utilizadas
### Linguagem
- Python
### Implantação em produção
- API Whatsapp: Twilio
- API Criptomoedas: Mercado Bitcoin

# Como executar o projeto

Pré-requisitos: Python 3.9 ou superior

```bash
# clonar repositório
git clone https://github.com/imguisilva/Bitcoin_price_monitor

# instalar dependências
pip install -r requirements.txt

# armazenar as credenciais do twilio em uma variável
account_sid = 'account_sid'
auth_token = 'auth_token'
to_number = 'seu telefone'

As variáveis também podem ser definidas nas variáveis de ambiente do computador, em: Edit Configurations > Environment variables (Pycharm)

```

# Autor

Guilherme Pereira

https://www.linkedin.com/in/imguilhermesilva/
 
