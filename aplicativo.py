# Instalar biblioteca
# pip install keyboard pywhatkit

# importando bibliotecas
import pywhatkit
import keyboard
import time
from datetime import datetime

# Definir quais contatos enviar mensagem
contatos = ['+5511', '+5521']
mensagem = 'Digite a sua mensagem'


# Definir intervalo de envio
while len(contatos) >= 1:
    # enviar mensagem
    pywhatkit.sendwhatmsg(
        contatos[0], mensagem, datetime.now().hour, datetime.now().minute + 1)
    # Deleta contato inicial para não repetir envio
    del contatos[0]
    # Tempo de espera
    time.sleep(6)
    # Fecha a aba
    keyboard.press_and_release('ctrl + w')
