"""espoco de variaveis"""

# as var global -- acessivel em qualquer parte do programa
# as var local --  são declaradas apenas naquela função e só existe enquanto tiver a função em exec

x = 5

def fun():
    x = 3
    print ("var global", x)

fun()
print("var local", x)


#usar nomes amigáveis
