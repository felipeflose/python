#sets: coleção, não ordernada, imutavel e não permite valores duplicados os sets são chamamos de conjuntos

conjunto = {"item1","item2","item3"}
print(type(conjunto))
print(conjunto)
print(len(conjunto))

tupla = (1,7,8,5)
tupla2 = (2,7,8,1)
conjunto = set(tupla)
conjunto1 = set(tupla2)
print(conjunto)
conjunto.add(6)
print(conjunto)
#conjunto.remove(6)
print(conjunto)
#a função discart não da erro se não tiver no conjunto
#conjunto.pop()
#print(conjunto)
#conjunto3 = conjunto.union(conjunto1)
#print(conjunto3)

conjunto3 = conjunto.intersection(conjunto1) #intercessão o tem tem igual
print(conjunto3)

conjunto.intersection_update(conjunto1) #intercessão
print(conjunto)

conjunto3 = conjunto.symmetric_difference(conjunto1) #intercessão o tem tem igual
print(conjunto3)

conjunto.symmetric_difference_update(conjunto1) #intercessão
print(conjunto)
