
import os
import csv
import time
import speedtest
from datetime import datetime
from time import sleep


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
   
quantidade_testes = 1000
intervalo_minutos = 1
segundos = 0
contador = 0
# Loop para execução dos testes

while contador <= quantidade_testes:
    for q in range(quantidade_testes):
        data_atual, hora_atual, velocidade_download, velocidade_upload = teste_internet()
    #print('Teste {}/{} Data: {} Hora: {} Download: {} Upload: {}'.format(q+1, quantidade_testes, data_atual, hora_atual, velocidade_download, velocidade_upload))    
        cab = ['id','dt_teste','hora_teste','down','up']
        lista = []
        lista.append(id(q))
        lista.append(data_atual)
        lista.append(hora_atual)
        lista.append(velocidade_download)
        lista.append(velocidade_upload)
   # print (lista)
        dt = datetime.now().strftime('%d-%m-%Y')
        hr = datetime.now().strftime('%H-%M-%S') 
        caminho = "C:\\Users\\fflose\\Lab\\\Pessoal\\python\\csv\\teste_internet\\"+"teste_internet-"+str(dt)+"-"+str(hr)+".csv"
        f = open(caminho,'w',newline='',encoding= 'utf-8')
        w = csv.writer(f)
        w.writerow(cab)
        w.writerow(lista)
        contador  = contador + 1
        #print(contador)
        path = "C:\\Users\\fflose\\Lab\\Pessoal\\python\csv\\teste_internet\\"
        ListaArquivos = os.listdir(path)
        dicio = dict.fromkeys(ListaArquivos)
        for x in dicio.keys():
                arq = open(path+x)
                d = arq
                linhas = csv.reader(arq,delimiter=';',quoting=csv.QUOTE_NONE)
                linhasLista = list(linhas)
                dicio[x] = linhasLista       
                #for i in dicio.items():  
        time.sleep(10)
        print(quantidade_testes - contador )
    






   

  
  
    



    
    
    
        

       
        
        
        









     
