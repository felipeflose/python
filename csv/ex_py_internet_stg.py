
import os
count = 0 
path = "C:\\Users\\fflose\\Lab\\csv\\teste_internet\\"
ListaArquivos = os.listdir(path)


for i in ListaArquivos:
    print(i)
    ListaArquivos = os.listdir(path)
