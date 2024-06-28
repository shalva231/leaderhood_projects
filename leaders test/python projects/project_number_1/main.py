
from decors import decorations
import random

BALANCE = 0
ACCOUNTS = []
PASSWORDS = []

def create_account():
    global username
    global password
    
    print("\n")
    print(decorations[0], "\n")
    print(" hello, user \n we want to help you create an account \n for this amazing program \n")
    print(decorations[0], "\n")
    
    #get users' username
    username = input("please enter your username: ")
    quit = False
    for i in ACCOUNTS:
        while username == i:
            print("already taken :(")
            username = input("please enter your username: ")
            
    keep_username = input(f"do you want to keep {username} as your username? (Y or N)")

            
    while not quit:
        
        if keep_username.lower() == "y":
            print(f"\nok your username will be {username}")
            quit = True
        elif keep_username.lower() == "n":
            username = input("please enter your username: ")
            keep_username = input(f"do you want to keep {username} as your username? (Y or N)")
        else:
            print("!!INCORRECT!!")
            username = input("please enter your username: ")
            keep_username = input(f"do you want to keep {username} as your username? (Y or N)")
            
    #get users' password      
    password = input("please enter your password (we wont tell anyone ;D): ")
    repeat = input("please repeat your password (we wont tell anyone ;D): ")
    
    while password != repeat:
        password = input("please enter your password (we wont tell anyone ;D): ")
        repeat = input("please repeat your password (we wont tell anyone ;D): ")

    print("your information will be:")
    print(f"{decorations[1]}\n\nusername:\n{username} \n\npassword:\n{len(password) * "*"} \n (i told you we wouldn't tell anyone ;D)\n{decorations[1]}")
    
    ACCOUNTS.append(username)
    PASSWORDS.append(password)
    

def perform_transaction():
    if BALANCE == 0:
        print(decorations[0])
        print("you do not have any money :(")
        print(decorations[0])
        print("\n would you like to deposit?")
        dep = input("(y or n): ")
        if dep.lower == "y":
            deposit = int(input("how much would you like to gift me.. i-i mean deposit?: "))
            BALANCE += deposit

    print("what would you like to do with your money?")
    action = input("tip, transfer, deposit (more actions coming soon): ")
    
    if action.lower() == "tip":
        print("wow you wanna tip me?\n thanks a lot :DDDD")
        tip = int(input("how much would you like to tip me?: "))
        print(f"thanks for {tip}$ <3")
        BaseException -= tip

    elif action.lower() == "transfer":
        print("who would you like to transfer to?")
        receiver = input("enter the account name you wanna transfer to: ")
        money = int(input("how much would you like to transfer?: "))
        if receiver not in ACCOUNTS:
            print("this user does not exist :D \n\n i will keep the money >:D")
            BALANCE -= money
        else:
            print("we have sent the money to the user\n")
            print("because of some issues the transferred money might not arrive :( \n(not my problem(the money will be mine >:D))")
            BALANCE -= money
    elif action.lower() == "deposit":
        deposit = int(input("how much would you like to gift me.. i-i mean deposit?: "))
        if random.randit(2) == 2:
            print("oops the money is lost \n ( not my problem dont complain >:D )")
        else:
            print(f"you have deposited {deposit}$")
            BALANCE += deposit
              
        
    
def update_info():
    print("please confirm that this accounts real owner is you")
    c_username = input("enter your username: ")
    c_password = input("enter your password: ")
    if c_password != password and c_username != username:
        print("this is not your account")
    else:
        new_password = input("what would you line your new password to be?: ")
        PASSWORDS.replace(password, new_password)
        password = new_password
        
        
        new_username = input("what would you line your new username to be?: ")
        ACCOUNTS.replace(username, new_username)
        username = new_username


def delete_acaunt():
    print("please confirm that this accounts real owner is you")
    c_username = input("enter your username: ")
    c_password = input("enter your password: ")
    if c_password != password and c_username != username:
        print("this is not your account")
    else:
        print("confirm account deletion")
        confirm = input("(y) to delete or (n) to keep the account: ")
        if confirm.lower() == "y":
            print("bye bye")
            ACCOUNTS.remove(username)
            PASSWORDS.remove(password)


def search_info(user):
    print(f"{username}'s password is {len(password) * "*"}\n\nwe told you we wouldn't tell anyone about your info :D")


def view_list():
    index = 0
    print("!this is our members list!")
    print(ACCOUNTS)     
    
      
exit = False

def main(exit):
    create_account()
    while not exit:
        print("what would you like to do now?")
        act = input("(create,transfer,update,delete,info,list,quit): ")
        if act.lower() == "create":
            create_account()
        elif act.lower() == "transfer":
            perform_transaction()
        elif act.lower() == "update":
            update_info()
        elif act.lower() == "delete":
            delete_acaunt()
        elif act.lower() == "info":
            search_info(username)
        elif act.lower() == "list":
            view_list() 
        elif act.lower() == "quit":
            print("bye bye")
            exit = True
        
        
main(exit)