# -*- coding: utf-8 -*-

#prompt
num = int(input("Digite um número inteiro: "))

#bloco lógico
if (num%2==0):
    #Início da verificação aninhada de 
    if (num<20):
        print(f"O número {num} atende a condição estabelecida.")
    else:
        print(f"O número {num} não atende a condição estabelecida.")
else:
    print(f"O número {num} não atende a condição estabelecida.")