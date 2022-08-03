palpite = 10
numero = palpite 

#while palpite != numero:
#    print("Qual o num? ")
#    palpite = int(input())
    
#print("Acertou")

#while bool(palpite) is True: # com a validação
while True: # vai direto sempre no true
     print("Qual o num? ")
     palpite = int(input())
     if palpite == numero:
        print("Acertou")
        break
     else: print("Errou")

else: print("Erro no código")    
