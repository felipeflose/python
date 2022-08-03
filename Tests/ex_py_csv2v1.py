#imports"
from fileinput import close
import os
import csv
import datetime

nomeArquivox = 'teste_internet'

# Passo 1, separar o csv em vários csv's

#arq = open("C:\\Users\\fflose\\Lab\\csv\\"+nomeArquivox+".csv")
#linhas = csv.reader(arq,delimiter=';',quoting=csv.QUOTE_NONE)
#linhasLista = list(linhas)
##c = 0
#for i in linhasLista:                  
 #       caminho = "C:\\Users\\fflose\\Lab\\csv\\teste\\annual-enterprise-survey-2021"+str(c)+".csv"
 #       f = open(caminho,'w',newline='',encoding= 'utf-8')
 #       dataAtual = str(datetime.datetime.today()).split()[0]
 #       lista = list(i)
 ##       if c == 0:
 #           lista.append("Id")
 #           lista.append("dataProcesso")
 #           lista.append("caminho")
 #       else:
 ##           lista.append(id(i))
 #           lista.append(dataAtual)
 #           lista.append(caminho)
 #       w = csv.writer(f)
 #       w.writerow(lista)
 #       c = c + int(1)
 #       f.close()
#        print ("arquivo "+caminho+" criado!")
  
# Passo 2, juntar todos os csv's e limpar a pasta
path = "C:\\Users\\fflose\\Lab\\csv\\teste_internet\\"
c1 = 0
arquivoFinal = "C:\\Users\\fflose\\Lab\\csv\\"+nomeArquivox+"_python.csv"
f1 = open(arquivoFinal,'w',newline='',encoding= 'utf-8')
ListaArquivos = os.listdir(path)
for i2 in ListaArquivos:
    nomeArq = ListaArquivos[c1]
    nomeCompleto = path+nomeArq
    arq1Abrindo = open(nomeCompleto)
    arq1Lendo = csv.reader(arq1Abrindo,delimiter=';',quoting=csv.QUOTE_NONE)
    arqLista = list(arq1Lendo)
    arq1Lendo = csv.writer(f1)
    arq1Lendo.writerow(arqLista)
    c1 = c1 + int(1)
    arq1Abrindo.close()
    #os.remove(nomeCompleto)
    print("nomeCompleto"+" deletado")
    

    
    