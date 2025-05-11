from view import *

import time


on=True
while on == True:
    clear()
    print("Ola, seja bem vindo(a)!")
    user = credential_check("user.txt")
    if( user == True):
        opt=input(""" 
Parece que ja ha um usuario existente! 
Deseja continuar com ele?
[1]-Sim
[2]-Nao

[Option]: """)
        match opt:
            case ("1"):
                print("Logando com um usuario existente!")
            case ("2"):
                print("Continuando com outro usuario!")
            case _:
                print("Opcao invalida!")