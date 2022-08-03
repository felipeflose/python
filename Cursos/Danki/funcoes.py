#paragidma imperativo
#linguagem c, fortran, bobol, basic, pascal

#atribuições
#sequenciais
#variaveis

# variaveis locais e globais;
#função pode ser chamada a qualquer momento;

#chamamos de def
#-------------------# 

nome = "felipe"
    #bloco externo

def funcao():
    #bloco interno de um função é conhecido como corpo da função é a alma dela, onde se faz as tarefas;
    nome = "feliped"
    print(nome)

print(nome) #aqui foi a variavel global
funcao() #aqui chama a função (def)


#----------------------------------------------------------#

def par_impar():
    numero = 4
    if(numero % 2 ) == 0:
        return "par"
    return "impar"
#o return sai da função
print(par_impar())


