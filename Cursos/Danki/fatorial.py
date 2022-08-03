
from socket import NI_NUMERICHOST
from tkinter import E


#4! = 4*3*2*1
#0! = 1
#1! = 1

fatorial = 1

numero = int(input("Insira num para saber o fatorial: "))
if numero < 0:
    print("Não tem pra numero negativo!")
elif numero == 0:
    print(f"{numero}! = 1")
else:
    for x in range(1,numero+1):
        fatorial = fatorial*x
                
    print(f"O {numero}! é: {fatorial}")

