import os
import csv
import time
import speedtest
from datetime import datetime
from time import sleep
import uuid

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
   
def cria_lista():       
        lista = []
        try:        
                data_atual, hora_atual, velocidade_download, velocidade_upload = teste_internet()
                lista.append(uuid.uuid1())
                lista.append(data_atual)
                lista.append(hora_atual)
                lista.append(datetime.now().strftime('%H')) 
                lista.append(velocidade_download)
                if velocidade_download >= 200:
                        lista.append(1)
                else:   lista.append(0)
                lista.append(velocidade_upload)
                lista.append(datetime.now().strftime('%d-%m-%Y'))
                lista.append(datetime.now().strftime('%H-%M-%S')) 
        
        except:
                print('deu erro, esperando 2 segundos')
                time.sleep(2)


        return lista

def qual_caminho():
      import socket
      name = socket.gethostname()
      if name == 'LGNTVIVO71':
                caminho = "C:\\Users\\fflose\\Lab\\\Pessoal\\python\\csv\\teste_internet\\"
      else:
                caminho =  "D:\\Felipe Flose\\csv\\teste_internet\\"     
      return(caminho)


def cria_arquivo():
       
        dt = datetime.now().strftime('%d-%m-%Y')
        hr = datetime.now().strftime('%H-%M-%S')     
        c = qual_caminho()
        caminho = c+"teste_internet-"+str(dt)+"-"+str(hr)+".csv"
        cab = ['idExec','dt_teste','hora_teste','hora_fechada','down','chegou','up','dtProcesso','hrProcesso','caminho']
        f = open(caminho,'w',encoding= 'utf-8',newline='')
        w = csv.DictWriter(f,delimiter=',', fieldnames=cab)
        w.writeheader()
        f = open(caminho,'a',encoding= 'utf-8',newline='')
        w = csv.writer(f,delimiter=',')
        lista_grava = cria_lista()
        lista_grava.append(caminho)
        w.writerow(lista_grava)
        
        #w.writerow(cab)
        #f.close()
        #f = open(caminho,'w',newline='',encoding= 'utf-8')
        #w = csv.writer(f,delimiter=',')        
        #lista_grava = cria_lista()
        #lista_grava.append(caminho)
        #w.writerow(lista_grava)
        
        

def qtd_arquivos():
        path = qual_caminho()
        ListaArquivos = os.listdir(path)
        return len(ListaArquivos)

def lista_arquivos():
        
        path = qual_caminho()
        ListaArquivos = os.listdir(path)
        return list(ListaArquivos)

def deleta_vazio():
        for x in lista_arquivos():
                path = qual_caminho()
                arq1 = open(path+x)
                arq1Lendo = csv.reader(arq1,delimiter=',',quoting=csv.QUOTE_NONE)
                arqLista = list(arq1Lendo)
                if len(arqLista) == 1:
                    arq1.close()
                    os.remove(arq1)        
                return print('arquivo '+ x +'  deletado!')

def cria_versao_final():
        path = qual_caminho()
        c1 = 0
        caminho = "C:\\Users\\fflose\\Lab\\csv\\annual-enterprise-survey_python.csv"
        f = open(caminho,'w',newline='',encoding= 'utf-8')
        ListaArquivos = os.listdir(path)
        for c in ListaArquivos:
                nomeArquivo = ListaArquivos[c1]
                caminho1 = path+nomeArquivo
                arq1 = open(caminho1)
                arq1Lendo = csv.reader(arq1,delimiter=';',quoting=csv.QUOTE_NONE)   
                arqLista = list(arq1Lendo)
                w = csv.writer(f)
                w.writerow(arqLista)
                c1 = c1+1
                os.remove(caminho1)



#\\desktop-73E3J72\teste_internet\

while 1 == 1 :
   # deleta_vazio()
    qual_caminho()
    cria_arquivo()
    print(qtd_arquivos())
    time.sleep(1)


