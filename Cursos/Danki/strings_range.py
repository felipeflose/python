#       012345
from unicodedata import name


nome = "Felipe"
# isso tbm é uma lista - carater intexados
print(nome[3])
for x in nome:
    print(x)

print(30 * "-")
for x in nome:
    print(x, end="")

print(30 * "-")
for x in range(len(nome)):
    print(x)

print(30 * "-")
#lista decrescente
for x in range(10,0,-1):
    print(x)

print(30 * "-")
for x in range(len(nome),0,1):
    print(x)

print(30 * "-")

x = 5
y = 0
x,y = y, x
print(x)
print(y)

    