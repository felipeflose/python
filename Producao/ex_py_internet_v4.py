
from lib2to3.pgen2.token import NEWLINE
import os
import csv
from re import X
import time
import turtle
import speedtest
from datetime import datetime
from time import sleep
import uuid
import numpy as np
import pandas as pd
import os
import csv
import time
import glob
import sqlite3


class internet:

    def __init__(self, teste):
        self.teste = teste

    def teste_internet():
        # Instanciando a função de test do Speedtest
        s = speedtest.Speedtest()
        s.get_servers()
        s.get_best_server()
    # Testando velocidades
        velocidade_download = round(s.download(threads=None)*(10**-6))
        velocidade_upload = round(s.upload(threads=None)*(10**-6))
    # Capturando data e hora do teste
        data_atual = datetime.now().strftime('%d/%m/%Y')
        hora_atual = datetime.now().strftime('%H:%M:%S')
        return data_atual, hora_atual, velocidade_download, velocidade_upload

    def cria_item():
        lista = []
        while len(lista) == 0:
            try:
                data_atual, hora_atual, velocidade_download, velocidade_upload = internet.teste_internet()
                #id = uuid.uuid1()
                # lista.append(id)
                #sjkdapksos
                lista.append(data_atual)
                lista.append(hora_atual)
                lista.append(velocidade_download)
                lista.append(velocidade_upload)
                # lista.append(internet.qual_caminho())
            except:
                #id = uuid.uuid1()
                # lista.append(id)
                lista.append(datetime.now().strftime('%d/%m/%Y'))
                lista.append(datetime.now().strftime('%H:%M:%S'))
                lista.append(0)
                lista.append(0)
                # lista.append(internet.qual_caminho())
                #print('deu erro, esperando 2 segundos')
                time.sleep(2)
        return lista

    def qual_caminho():
        import socket
        name = socket.gethostname()
        if name == 'LGNTVIVO71':
            caminho = "C:\\Users\\fflose\\Lab\\\Pessoal\\python\\csv\\teste_internet\\"
        else:
            caminho = "D:\\Felipe Flose\\csv\\teste_internet\\"

        return(caminho)

    def main():
        x = []
        x.append(tuple(internet.cria_item()))
        sql_insert = 'insert into teste ' \
                     '(dt_teste' \
                     ',hora_teste' \
                     ',down' \
                     ',up) values'
        for i in x:
            Sql.cria_tabelas()
            print(sql_insert + str(i))
            con = Sql.conexao()
            cur = Sql.cursor()
            cur.execute(sql_insert + str(i))
            con.commit()
            #con.close()


class Sql():
    def conexao():
        caminhoBD = '\\\\desktop-73e3j72\\bd\\'
        nomeTable = 'internet.db'
        con = sqlite3.connect(caminhoBD+nomeTable)
        return con

    def cria_tabelas():
        sql_create_teste = 'CREATE TABLE IF NOT EXISTS teste '\
            '(idExec INTEGER primary key AUTOINCREMENT, '\
            'dt_teste date, '\
            'hora_teste time, '\
            'down int, '\
            'up int) '
        # os.remove(caminhoBD+nomeTable) if os.path.exists(caminhoBD+nomeTable) else
        Sql.exec(sql_create_teste)

    def cursor():
        cur = Sql.conexao().cursor()
        return cur

    def exec(x):
        cur = Sql.conexao().cursor().execute(x)
        return cur

if __name__ == "__main__":
    internet.main()
