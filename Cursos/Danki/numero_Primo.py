print(30 * "-")
numero = int(input("Insira um numero: "))
if numero > 1:
    for x in range(2,numero):
        if(numero % x) == 0:
            print("Esse não é primo")
            break
    else:
            print("É primo")
else:
    print("esse não é primo, menor ou igual a 1")
print(30 * "-")

