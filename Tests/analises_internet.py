from logging.config import dictConfig
import numpy
import pandas as pd
import os
import csv
import time

def procurando_arquivo_vazio():
    path = "C:\\Users\\fflose\\Lab\\Pessoal\\python\\csv\\teste_internet\\"
    ListaArquivos = os.listdir(path)
    lista = []
    for x in ListaArquivos:
        m = 0
        arq = open(path+x)
        linhas = pandas.read_csv(arq)
        #print("Esse arquivo " + x +" tem "+ str(len(linhas)) + "linhas" )
        if len(linhas) == 0:
            time.sleep(5)
            #print( path + x )
            lista.append(path + x)
    return lista
       
def lendo_arquivo_ok():
    path = "C:\\Users\\fflose\\Lab\\Pessoal\\python\\csv\\teste_internet\\"
    ListaArquivos = os.listdir(path)
    lista = []
    for x in ListaArquivos:
        m = 0
        arq = open(path+x)
        linhas = pd.read_csv(arq)
        #print("Esse arquivo " + x +" tem "+ str(len(linhas)) + "linhas" )
        if len(linhas) == 1:
            time.sleep(5)
            #print( path + x )
            lista.append(path + x)
    return lista


def lendo_arquivos_2():
    l = lendo_arquivo_ok()  
    df = []
    for x in range(len(l)):
        #print(l[x])
        if x == 0:
            data = pd.read_csv(l[0],delimiter=',')
            df.append(data)
            print(data)
        else:
              data1 = pd.read_csv(l[1],delimiter=',',skiprows = 1,header=None)
              df.append(data1)
              print(data1)
        print(df)
        
    
    #print(main_dataframe)

    
lendo_arquivos_2()
    

    
               
   
    