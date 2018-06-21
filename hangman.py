import sys
from printing import printing_menu, cls, highscore_show
from game_option import game_start

def menu(hint):
    cls()
    option = "0"
    while option != "3":
        printing_menu("1")
        option=input("Choose option: ")
        if (option == '1'):
            cls()
            nick = input ("Your nick:  ")
            cls()
            if game_start(nick, hint):
                continue
            else:
                exit()
        elif (option == '2'):
            cls()
            if highscore_show():
                continue
            else:
                exit()
    exit()

def arg_from_terminal():
    hint = False
    if len(sys.argv) > 1:
        if "-test" == sys.argv[1]:
            hint = True
    return hint

cls()
menu(arg_from_terminal())
