import platform
import os

def credential_check(user_txt):
    f = open("{}".format(user_txt))
    if(f.read() == "antonio"):
        return True
    else:
        return False

def get_os():
    return platform.system()

def clear():
    match get_os():
        case ("Windows"):
            os.system("cls")
        case ("Linux"):
            os.system("clear")