# -*- coding: utf-8 -*-

banco_dados = {"reginaldo":1234, "nikael":4321, "guilherme": 6789, \
               "marcos":9876, "alisson":112233}

#Prompt com o usuário
nome = input("Digite seu nome de usuário: ")
senha = int(input("Digite sua senha: "))

#Bloco lógico
if nome in list(banco_dados.keys()):
    if senha in list(banco_dados.values()):
        print(f"Seja bem vindo {nome}!")
    else:
        print(f"{nome.title()} gostaria de recuperar sua senha?")

elif nome.title() in list(banco_dados.keys()):
    if senha == banco_dados[nome.lower()]:
        print(f"Seja bem vindo {nome}!")
    else:
        print(f"{nome.title()} gostaria de recuperar sua senha?")

elif nome.upper() in list(banco_dados.keys()):
    if senha == banco_dados[nome.lower()]:
        print(f"Seja bem vindo {nome}!")
    else:
        print(f"{nome.title()} gostaria de recuperar sua senha?")

elif nome.lower() in list(banco_dados.keys()):
    if senha == banco_dados[nome.lower()]:
        print(f"Seja bem vindo {nome}!")
    else:
        print(f"{nome.title()} gostaria de recuperar sua senha?")

else:
    print("Usuário não encontrado!")