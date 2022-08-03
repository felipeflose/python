
from ast import Break
from random import choice

jogador_vitorias = 0
maq_vitorias = 0

def opcao_jogador():
    esc_jogador = input("Escolha entre, pedra, papel ou tesoura: ")
    esc_jogador.lower()
    if esc_jogador == "pedra":
        return esc_jogador
    elif esc_jogador == "papel":
        return esc_jogador
    elif esc_jogador == "tesoura":
        return esc_jogador
    else:
        print("opção invalida.. tente novamente")
        opcao_jogador()

def opcao_maquina():
    esc_maquina = choice(["pedra", "papel", "tesoura"])
    return esc_maquina


while True:

    print("-"*30)
    esc_jogador = opcao_jogador()
    esc_maquina = opcao_maquina()
    print("-"*30)

    if(esc_jogador == "pedra" ) and (esc_maquina == "tesoura") \
        or (esc_jogador == "papel") and (esc_maquina == "pedra")  \
        or (esc_jogador == "tesoura") and (esc_maquina == "papel"):
            #jogador ganha
            print(f"o jogador escolheu {esc_jogador} e a maquina escolheu {esc_maquina} - você ganhou!")
            jogador_vitorias +=1
    elif esc_jogador == esc_maquina:
        print("empate")
    else:
            print(f"o jogador escolheu {esc_jogador} e a maquina escolheu {esc_maquina} - você perdeu!")
            maq_vitorias +=1

    print("-"*30)
    print(f"vitórias jogador: {jogador_vitorias}")
    print(f"vitórias jogador: {maq_vitorias}")
    print("-"*30)
    
    esc_jogador = input("vc quer jogar novamente? ")
    if esc_jogador in ["Sim","s","S","sim"]:
        pass
    elif esc_jogador in ["NAO","não","Não","S","s"]:
        break
    else:
        break