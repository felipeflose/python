
from ctypes.wintypes import INT
import os
import csv
path = "C:\\Users\\fflose\\Lab\\csv\\teste\\"
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