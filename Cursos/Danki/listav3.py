from re import S
from tkinter import E


lista2 = [2,3,9,77]
print(lista2)

lista1 = [2.6,3.8,9.3,7.7]
print(lista1)

lista3 = lista2 + lista1

print(lista3)
print(30*"-")

print(len(lista3))

print(30*"-")

lista4 = ["Nome","Nome"]
#por ter index, não precisa de preocupar com o nome
print(len(lista4))

#funcoes de lista com tipo numérico

print(sum(lista2))
print(max(lista2))

print(sum(lista1))
print(min(lista1))

print(30*"-")

nome = "curso dahora pra caramba"
valor = range(10)

print(nome)
print(valor)

print(30*"-")
lista7 = list(range(10))
print(lista7)

print(30*"-")

lista8 = list(nome)
print(lista8)

e = "s"
if e in lista8:
    print(e)



