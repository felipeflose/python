lista = ["a","b","c"]
lista2 = [1,5,7]

#jeito 1 - concat listas
lista = lista + lista2
print(lista)
 
#jeito 2 concat listas
lista.extend(lista2)
print(lista)

#jeito 3 concat listas
for x in lista2:
    lista.append(x)

print(lista)

#copiar lista jeito 1
lista = lista2
print(lista)

#copiar lista lista jeito 2
lista = lista2.copy
print(lista)

