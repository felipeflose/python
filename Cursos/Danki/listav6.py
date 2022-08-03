lista = ["carro","barco","aviao"]
lista.extend(["navio","jato"]) # assim add na lista normal - ele extende a lista
print(lista)

lista.pop() # o pop vazio remove a ultima posição da lista
lista.pop(1)  # vc escolhe qual indice quer remover
lista.remove("carro") #remove o valor que vc quer
print(lista)
del lista[0] #escolho o que remover
print(lista)
del lista #remove toda a lista

print(30*"-")
lista2 = ["prod1","prod2","prod0"]
lista3 = [9,6,8]
lista2.sort()
lista2.sort(key = str.lower) # arruma as strings pra minusculo para fazer o sort
lista3.sort(reverse=True) #reverte a ordenação
lista3.reverse #reverte a ordenação
#print(lista2)
#lista2.clear() # ele limpa a lista
print(lista2)
print(lista3)