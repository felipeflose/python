
#---- for simples
from multiprocessing.sharedctypes import Value



lista = ["F","e","l","i","p","e"]

for item  in lista:
    print (item)

#---- for com numeração de lista

for key, value in enumerate(["F","e","l","i","p","e"]):
    print (key, value)

#---- for com range

for i in range(10):
    c = 0
    c = c + 1
    print (i,c)


    cont = 10

for c in range(cont):

    file = 'screenShot{:05d}.jpg'.format(c)

    print(file)