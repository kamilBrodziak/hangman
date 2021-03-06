import os
import sys
import time
from termcolor import colored, cprint
from leaderboard import loading_highscore_file_into_list


def cls():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def printing_hangman(lifes, letters):
    print("Your lifes: ", end="")
    if lifes < 0:
        lifes = 0
    cprint((chr(9829) + " ") * lifes, 'red', attrs=['bold'])
    print("------------------------------------------------------\n")
    with open(str(lifes) + '.txt', 'r') as file:
        if lifes > 4:
            cprint(file.read(), 'green', attrs=['bold'])
        elif lifes > 2 and lifes < 5:
            cprint(file.read(), 'yellow', attrs=['bold'])
        elif (lifes < 3 and lifes > 1) or lifes < 1:
            cprint(file.read(), 'red', attrs=['bold'])
        elif lifes == 1:
            cprint(file.read(), 'red', attrs=['bold', 'blink'])
    print("Used letters: ", letters)


def display_hint(country):
    print("Capital of " + country)


def display_test_hint(capital):
    print("Debug mode,  capital: " + capital)


def printing_menu(option):
    cls()
    with open('logo.txt', 'r') as logo:
        cprint(logo.read(), 'yellow', attrs=['bold'])
    with open('option' + option + '.txt', 'r') as option:
        print(option.read())


def back_to_menu():
    question = 20 * " " + "Do you want to back to menu? (yes/no): "
    print("\n")
    answer = input(question)
    while answer.lower() != "yes" and answer.lower() != "no":
        sys.stdout.write("\033[F")
        answer = input(question)
    return True if answer.lower() == "yes" else False


def highscore_show():
    with open('trophy.txt', 'r') as trophy:
        cprint(trophy.read(), 'yellow', attrs=['bold', 'dark'])
    print("---PLACE-----NICK-------------TIME-------DATE--------------------------WORD-----\n")
    sorted_highscores = loading_highscore_file_into_list()
    place_nr = 1
    for result in sorted_highscores:
        print(3 * " " + str(place_nr) + "." + (7 - len(str(place_nr))) * " " + result[0] +
              (19 - len(result[0])) * " " + str(round(float(result[1]), 3)) +
              (11 - len(str(round(float(result[1]), 3)))) * " " + str(result[2]) +
              (30 - len(result[2])) * " " + result[3])
        place_nr += 1
    print(" " + 79 * "_")
    return back_to_menu()


def win_defeat(status, nick, score):
    if status == "lost":
        time.sleep(2)
        cls()
        with open('lost.txt', 'r') as lost:
            cprint(lost.read(), 'red', attrs=['bold'], end="")
            cprint(
                "|" + 38 * " " + "You lost." +
                38 * " " + "|", 'red', attrs=['bold'])
            cprint("|" + 85 * "_" + "|", 'red', attrs=['bold'])
    if status == "won":
        cls()
        with open('won.txt', 'r') as won:
            cprint(won.read(), 'green', attrs=['bold'], end="")
            string = nick + ", you won with score: " + str(round(score, 3))
            cprint("|" + int((78 - len(string)) / 2) * " " +
                   string + int((76 - len(string)) / 2) * " " + "|", 'green', attrs=['bold'])
            cprint("|" + 77 * "_" + "|", 'green', attrs=['bold'])
    return back_to_menu()


def used_letter_before():
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[F")
    print("You used that letter before, give me another one!")


def printing_hint_and_capital(capital_display_on_screen, cou_cap, life, hint):
    if life == 1:
        display_hint(cou_cap[0])
        if hint:
            display_test_hint(cou_cap[1])
    print("".join(capital_display_on_screen))
    print("------------------------------------------------------\n")
