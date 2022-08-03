
import os
import csv
import pandas as pd


        
path = "C:\\Users\\fflose\\Lab\\Pessoal\\python\csv\\teste_internet\\"
ListaArquivos = os.listdir(path)
for x in ListaArquivos:
    c = path+x
    arq1 = open(c)
    arq1Lendo = csv.reader(arq1,delimiter=',',quoting=csv.QUOTE_NONE)
    arqLista = list(arq1Lendo)
    if len(arqLista) == 1:
        arq1.close()
        os.remove(path+x)        
        print('arquivo '+ x +'  deletado!')


