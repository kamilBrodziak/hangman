import os, time, sys

def cls():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def back_to_menu():
    answer = ""
    while answer.lower != "no":
        answer = input("Would you like to back to menu? (yes/no): ")
        if answer.lower() == "yes":
            return menu()
        else:
            sys.stdout.write("\033[F")
    exit()

def won():
    cls()
    print("You won!")
    back_to_menu()

def defeat():
    time.sleep(2)
    cls()
    print("You loss!")
    back_to_menu()