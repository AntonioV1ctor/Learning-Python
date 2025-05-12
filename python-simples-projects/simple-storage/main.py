from view import *
import time


on=True
while on == True:
    clear()
    print("Ola, seja bem vindo(a)!")
    user = verify_if_exist("user.txt")
    if( user == True):
        opt=input(""" 
Parece que ja ha um usuario existente! 
Deseja continuar com ele?
[1]-Sim
[2]-Nao

[Option]: """)
        match opt:
            case ("1"):
                passwd = input("[Pass]: ")
            case ("2"):
                print("Continuando com outro usuario!")
            case _:
                print("Opcao invalida!")
    else:
        print("Nem um usuario encontrado!")
        time.sleep(1.5)
        clear()
        user_create("user.txt","pass.txt")
        store_stand(store("products.txt"))
        break