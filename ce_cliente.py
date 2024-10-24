import requests
import time
from random import randint

SERVER_URL = 'http://10.0.2.15:5000/data'

def send_data(data):
    try:
        response = requests.post(SERVER_URL, json=data)
        if response.status_code == 200:
            print("O dado foi enviado com sucesso uhuu!")
        else:
            print(f"falhou ao enviar os dados: {response.status_code} - {response.json()}")
    except Exception as e:
        print(f"Putz... deu erro ao conectar no servidor, foi esse aqui >>>: {e}")

if __name__ == '__main__':
    print("Cliente foi conectado, enviando dados...")

    while True:
        mensagem = randint(1, 20)  # Vai escolher um número aleatório de 1 até 20.
        dados = {"message": mensagem}

        send_data(dados)
        time.sleep(2)  # Vai enviar o número escolhido a cada 2 segundos.
