import sys
from printing import printing_menu, cls, highscore_show
from game_option import game_start


def menu(hint):
    cls()
    option = "0"
    while option != "3":
        printing_menu("1")
        option = input("Choose option: ")
        if (option == '1'):
            cls()
            print("\n\nYou are playing Hangman. You will be guessing capitals of countries. \n\n")
            nick = input("Your nick:  ")
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
    return True if len(sys.argv) > 1 and "-test" == sys.argv[1] else False


if __name__ == '__main__':
    cls()
    menu(arg_from_terminal())
