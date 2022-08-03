

#lista: coleção, mutalvel e que permite valores duplicados
#tuplas: coleção, imutalvel e que permite valores duplicados
#dicionario, não ordenada, mutal e não permite valores duplicados

#dicionario, funciona como chave e valor
#no dicionário, a chave que é o index da lista pq não tem index.

#jeito1
dicio = {"chave1":"Felipe","chave2":1991,"chave3":True}
print(dicio)

#jeito2
dicionario = {
    "nome": "Felipe",
    "idade": 31,
    "nacionalidade": "Brasileira"
}

print(dicionario)

#não pode ter duplicado, se tiver, ele vai pegar o ultimo

#jeito 1 para pegar a chave
print(dicionario["nome"])
#jeito 2 para pegar a chave
print(dicionario.get("idade"))
#no python no terminal declara o dicio e dir(dicio) mostra o q ele faz
print(dicionario.keys()) #todas as chaves do dicionario
print(len(dicionario)) 
print(dicionario.keys())
print(dicionario.values())
print(dicionario.items())

if "idade" in dicionario:
    print("A chave idade existe")


dicionario["nome"] = "Felipoioi"
print(dicionario)
dicionario.update({"nome":"Felipe Flose"})
print(dicionario)
dicionario.update({"estado":"SP"})
print(dicionario)
#dicionario.popitem() #pop item elimia o ultimo item do dicionario a partir da versão 3.7 pra cima, anterior é aleatório
print(dicionario)
#dicionario.pop("nacionalidade")
print(dicionario)
#del dicionario["idade"]
print(dicionario)
#del dicionario #deleta tudo
#dicionario.clear()

for x in dicionario:
    print(dicionario[x])

for x in dicionario.keys():
    print(x)

for x in dicionario.values():
    print(x)

for x, y in dicionario.items(): #são as tuplas dentro do dicio
    print(x, y)

#copia jeito 1
x_dicionario = dicionario.copy()
print(x_dicionario)

#copia jeito 2
y_dicionario = dict(dicionario)
print(y_dicionario)

#fromkyes


tupla = ("item1","item2","item3")
tupla2 = ("item1","item2","item3")
x = 0
dicio = dict.fromkeys(tupla,tupla2)
print(dicio)



dicionario = {
    "dicio1": {
        "nome":"Felipe",
        "idade": 30
    },
    "dicio2": {
        "nome":"Laura",
        "idade": 8,
         "dicio3":{
            "sobrenome":"Flose" 
              }
    }
}

print(dicionario)
