# Instalar biblioteca
# pip install pyodbc
# pip install keyboard pywhatkit

# importando bibliotecas
import pyodbc
import pywhatkit
import keyboard
import time
from datetime import datetime


# Conexão com o banco de dados


def conexao_bd():
    server = 'server'
    database = 'database'
    username = 'username'
    password = 'password'
    driver = 'SQL Server'

    cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server +
                          ';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+password)

    return cnxn


conexao = conexao_bd()
cursor = conexao.cursor()
query_contato = cursor.execute('SELECT telefone  FROM [dbo].[contatos]')

mensagem = """Olá,

  Teste da automação.

  Atenciosamente.

  """

contatos = []
for linha in cursor.fetchall():
    contatos.append(list(linha))

    for contato in contatos:
        while len(contato) >= 1:
            # enviar mensagem
            pywhatkit.sendwhatmsg(
                contato[0], mensagem, datetime.now().hour, datetime.now().minute + 1)
            # Deleta contato inicial para não repetir envio
            del contato[0]
            # Tempo de espera
            time.sleep(6)
            # Fecha a aba
            keyboard.press_and_release('ctrl + w')

        contato


conexao.commit()
conexao.close()
