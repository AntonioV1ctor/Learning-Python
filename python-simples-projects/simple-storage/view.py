import platform
import os

def verify_if_exist(user_txt):
    f = open("{}".format(user_txt))
    for i in f:
        if(i):
            return True
    return False

def pass_check(user_txt):
    return open("{}".format(user_txt))
    
def user_check(pass_txt):
    return open("{}".format(pass_txt))

def get_os():
    return platform.system()

def clear():
    match get_os():
        case ("Windows"):
            os.system("cls")
        case ("Linux"):
            os.system("clear")
            
def store():
    while True:
        print("Seja muito bem vindo(a) {}".format())

def user_create(user_txt,pass_txt):
    UserName,UserPass = input("[UserName and UserPass]:").split()
    u = open(user_txt,"w")
    u.write("{}".format(UserName))
    p = open(pass_txt,"w")
    p.write("{}".format(UserPass))
    clear()
    return print("Usuario criado com sucesso!")

def store (store_txt):
    product_list = []
    u = open(store_txt)
    # u.write("{}".format())
    if(verify_if_exist(store_txt)):
        for i in store_txt:
            product_list.append(i)
        return product_list
    else:
        return "Nem um produto no estoque!"

def store_stand(product):
    r = len(product)
    print(r)
    print("-"*(r+2))
    print("|{}|".format(product))
    print("-"*(r+2))
    opt = input("[Option]: ")