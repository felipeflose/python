
from lib2to3.pgen2.token import NEWLINE
import os
import csv
import time
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
from imblearn.over_sampling import SMOTE 

class internet():
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

    def cria_arquivo():
        dt = datetime.now().strftime('%d-%m-%Y')
        hr = datetime.now().strftime('%H-%M-%S')     
        caminho = "C:\\Users\\fflose\\Lab\\\Pessoal\\python\\csv\\teste_internet\\"+"teste_internet-"+str(dt)+"-"+str(hr)+".csv"
        cab = ['idExec','dt_teste','hora_teste','hora_fechada','down','chegou','up','dtProcesso','hrProcesso','caminho']
        f = open(caminho,'w',encoding= 'utf-8',newline='')
        w = csv.DictWriter(f,delimiter=',', fieldnames=cab)
        w.writeheader()
        f = open(caminho,'a',encoding= 'utf-8',newline='')
        w = csv.writer(f,delimiter=',')
        lista_grava = internet.cria_lista()
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
            path = "C:\\Users\\fflose\\Lab\\Pessoal\\python\csv\\teste_internet\\"
            ListaArquivos = os.listdir(path)
            return len(ListaArquivos)

    def exec():
            #while 1 ==1 :
                internet.cria_arquivo()
                print(internet.qtd_arquivos())
                time.sleep(1)
                
            
    def caminho():
        path = "C:\\Users\\fflose\\Lab\\Pessoal\\python\\csv\\teste_internet\\"
        return path

    def lendo_arquivo():
        l = []
        #path = caminho()
        os.chdir("C:\\Users\\fflose\\Lab\\Pessoal\\python\\csv\\teste_internet\\")
        extension = 'csv'
        all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
    #combinar todos os arquivos da lista
        combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
    #exportar para csv
    #combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')
        df = pd.DataFrame(combined_csv).reset_index()
        #df[df.columns[0]].count()
        #qtdLinhas
        #print(df['idExec'].nunique())
        #df[['dt_teste']].nunique()
        #max = df['dt_teste'].max()
        #max1 = df['hora_fechada'].max()
        #df = df.loc[df['dt_teste'] == max]
        #df = df.loc[df['hora_fechada'] == max1]
        #df[['idExec','dt_teste','hora_teste','down','chegou','up','hora_fechada']]        
       
        return df
    



    def resultado():
#qtd de teste de download por hora
        df = pd.DataFrame(internet.lendo_arquivo())
        dfqtdTeste =  df.groupby(['dt_teste','hora_fechada']) ['down'].count().reset_index()
        dfqtdTeste.rename(columns={'dt_teste':'data', 'hora_fechada':'hora' ,'down':'qtdteste'}, inplace = True)
        dfqtdTeste = pd.pivot_table(dfqtdTeste, values = 'qtdteste', index=['data','hora','qtdteste'], columns = 'hora').reset_index()
#max de download por hora
        dfqmedia =  df.groupby(['dt_teste','hora_fechada']) ['down'].mean().reset_index()
        dfqmedia.rename(columns={'dt_teste':'data', 'hora_fechada':'hora' ,'down':'media'}, inplace = True)
        dfqmedia = pd.pivot_table(dfqmedia, values = 'media', index=['data','hora','media'], columns = 'hora').reset_index()
#min de download por hora
        dfqtdmin =  df.groupby(['dt_teste','hora_fechada']) ['down'].min().reset_index()
        dfqtdmin.rename(columns={'dt_teste':'data', 'hora_fechada':'hora' ,'down':'min'}, inplace = True)
        dfqtdmin = pd.pivot_table(dfqtdmin, values = 'min', index=['data','hora','min'], columns = 'hora').reset_index()
#max de download por hora
        dfqtdmax =  df.groupby(['dt_teste','hora_fechada']) ['down'].max().reset_index()
        dfqtdmax.rename(columns={'dt_teste':'data', 'hora_fechada':'hora' ,'down':'max'}, inplace = True)
        dfqtdmax = pd.pivot_table(dfqtdmax, values = 'max', index=['data','hora','max'], columns = 'hora').reset_index()
#qtd chegou de download por hora
        dfqtdchegou =  df.groupby(['dt_teste','hora_fechada']) ['chegou'].sum().reset_index()
        dfqtdchegou.rename(columns={'dt_teste':'data', 'hora_fechada':'hora' ,'chegou':'qtdchegou'}, inplace = True)
        dfqtdchegou = pd.pivot_table(dfqtdchegou, values = 'qtdchegou', index=['data','hora','qtdchegou'], columns = 'hora').reset_index()

    #dffinal = pd.concat([dfqtdTeste, dfqmedia, dfqtdmin, dfqtdmax]).reset_index()
        dffinal1 = pd.merge(dfqtdTeste, dfqmedia, how = 'inner', on = ['hora','data'] ).reset_index()
        dffinal2 = pd.merge(dfqtdmin, dfqtdmax, how = 'inner', on = ['hora','data'] ).reset_index()
        dffinal3 = pd.merge(dffinal1, dffinal2, how = 'inner', on = ['hora','data'] ).reset_index()
        dffinal4 = pd.merge(dfqtdchegou, dffinal3, how = 'inner', on = ['hora','data'] ).reset_index() 
        df = pd.DataFrame(dffinal4)
        print(df)

    def clear_console():
        os.system('cls')

    def esperar():
         time.sleep(60)

    def exec_monitorado():
        while 1 == 1:
            internet.exec()
            internet.clear_console()
            internet.resultado()
            internet.esperar()
            internet.clear_console()



x = internet.exec_monitorado()

