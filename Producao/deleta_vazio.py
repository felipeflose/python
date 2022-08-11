import os
import csv
import time
import speedtest
from datetime import datetime
from time import sleep
import uuid


def qual_caminho():
      import socket
      name = socket.gethostname()
      if name == 'LGNTVIVO71':
                #caminho = "C:\\Users\\fflose\\Lab\\\Pessoal\\python\\csv\\teste_internet\\"
                caminho =  "\\\\desktop-73e3j72\\teste_internet\\"         
      else:
                caminho =  "\\\\desktop-73e3j72\\teste_internet\\"     
      return(caminho)

def lista_arquivos():
        
        path = qual_caminho()
        ListaArquivos = os.listdir(path)
        dt = datetime.now().strftime('%d-%m-%Y')
        l = []
        for x in ListaArquivos:
             if x[15:25] == dt:
               # print(x)
                l.append(x)
        return l

def deleta_vazio():
        for x in lista_arquivos():
                path = qual_caminho()
                arq1 = open(path+x)
                arq1Lendo = csv.reader(arq1,delimiter=',',quoting=csv.QUOTE_NONE)
                arqLista = list(arq1Lendo)
                if len(arqLista) != 2:
                    arq1.close()
                    os.remove(path+x)        
                return print('arquivo '+ x +'  deletado!')

def qtd_pasta():
    path = qual_caminho()
    ListaArquivos = os.listdir(path)
    return len(ListaArquivos)

deleta_vazio()

