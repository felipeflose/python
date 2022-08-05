
import numpy as np
import pandas as pd
import os
import csv
import time
import glob
from datetime import datetime


path = "C:\\Users\\fflose\\Lab\\\Pessoal\\python\\csv\\teste_internet\\"
l = []
ListaArquivos = os.listdir(path)
l = ListaArquivos
dt = datetime.now().strftime('%d-%m-%Y')

for x in l:
    #print(x[15:25])
    if x[15:25] == dt:
        print(x)