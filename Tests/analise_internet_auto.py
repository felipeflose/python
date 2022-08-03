
import numpy as np
import pandas as pd
import os
import csv
import time
import glob
from imblearn.over_sampling import SMOTE 


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
    df = pd.DataFrame(combined_csv)
    return df
def lista_arquivos():
        path = "C:\\Users\\fflose\\Lab\\Pessoal\\python\csv\\teste_internet\\"
        ListaArquivos = os.listdir(path)
        return list(ListaArquivos)

def deleta_vazio():
    for x in lista_arquivos():
        path = "C:\\Users\\fflose\\Lab\\Pessoal\\python\csv\\teste_internet\\"
        arq1 = open(path+x)
        arq1Lendo = csv.reader(arq1,delimiter=',',quoting=csv.QUOTE_NONE)
        arqLista = list(arq1Lendo)
        if len(arqLista) == 1:
            arq1.close()
            os.remove(path+x)        
            return print('arquivo '+ x +'  deletado!') 


#df[df.columns[0]].count()
#qtdLinhas
#print(df['idExec'].nunique())
#df[['dt_teste']].nunique()
#max = df['dt_teste'].max()
#max1 = df['hora_fechada'].max()
#df = df.loc[df['dt_teste'] == max]
#df = df.loc[df['hora_fechada'] == max1]
#df[['idExec','dt_teste','hora_teste','down','chegou','up','hora_fechada']]        


def resultado():
#qtd de teste de download por hora
    df = pd.DataFrame(lendo_arquivo())
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
    print(dffinal4[['data','hora', 'qtdteste','media', 'min','max','qtdchegou']])

def clear_console():
    os.system('cls')

def esperar():
     time.sleep(15)


while 1 == 1:
    #try:
       # deleta_vazio()
    #finally:
        resultado()
        esperar()
        clear_console()