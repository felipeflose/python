from asyncore import write
import csv
from itertools import count
arq = open('C:\\Users\\fflose\\Lab\\csv\\annual-enterprise-survey.csv')
linhas = csv.reader(arq,delimiter=';',quoting=csv.QUOTE_NONE)
linhasLista = list(linhas)
c = 0
for i in linhasLista:                  
        caminho = "C:\\Users\\fflose\\Lab\\csv\\teste\\teste"+str(c)+".csv"
        f = open(caminho,'w',newline='',encoding= 'utf-8')
        w = csv.writer(f)
        w.writerow(i)
        c = c+1





     




