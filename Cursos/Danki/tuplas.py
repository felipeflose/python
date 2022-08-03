
"""
tupla = ("item1","item3","item3")
print(type(tupla))
print
print(tupla[2])
#elas tbm tem index
# A tupla não é imutavel (não muda os itens dela)e tem menos opção para trabalhar
#tupla não aceita alterar usando o index, porém, posso redefinir ela.

print(tupla.count("item1"))

print("-"*90)


uf = ("SP","DF","GO")
print(uf)

tupla = ("item1",) #força uma tupla de um item


tupla = "item1", "item2" #não precisa da () é definida pela ,
print(tupla)
lista = list(tupla)
print(lista)
lista.append("item3")
print(lista)
tupla = tuple(lista)
print(tupla)

"""

tupla = ("item1",) 
tupla2 = ("a","b" )
tupla3 = tupla + tupla2
print(tupla3)

for x in tupla3:
    print(x)

for x in range(len(tupla3)): #imprime o index
    print(x)

for x in range(len(tupla3)): #imprime o endereço com o id do index
    print(x, tupla3[x])

#impacotada
tupla = ("item1","item2","item3","item4", "item5")    

#desenpacotada simples
"""
(x,y) = tupla
print(x)
print(y)
"""
#desenpacotada composto

(x,*y,z) = tupla
print(x)
print(y)
print(z)

#na y ele jogou o resto da tupla com lista

 6^6