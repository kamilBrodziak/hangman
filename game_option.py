import time, sys
from list_containing_capital_transformations import *
from printing import printing_hangman, cls, display_hint, win_defeat, used_letter_before, display_test_hint
from leaderboard import highscore_add_to_highscore_list, highscores_add_to_file

def game_start(nick, hint):
    with open('countries_and_capitals.txt') as countries:
        capitals = countries.readlines()
    cou_cap = random_list_element_change_into_list(capitals)
    win = ""
    time_score = 0
    life = 6
    used_letters = []
    capital_hidden = [" ___"] * len(cou_cap[1])
    start_time = time.time()
    capital_hidden_template = change_capital_word_into_capital_hidden_template(cou_cap[1])
    delete_spaces_in_capital_hidden(cou_cap[1], capital_hidden)
    cls()
    while life > 0:
        cls()
        printing_hangman(life, used_letters)
        if life == 1:
            if hint:
                display_hint(cou_cap[0])
                display_test_hint(cou_cap[1])
            else:
                display_hint(cou_cap[0])
        print("".join(capital_hidden))
        print ("------------------------------------------------------\n")
        life, win, time_score = answering_time_and_consequences(life, cou_cap[1], capital_hidden, used_letters, time_score)
        if capital_hidden_template == capital_hidden or win == "won":
            time_score += time.time() - start_time
            highscores_add_to_file(nick, time_score, cou_cap[1])
            win = "won"
            break
    cls()
    if life == 0:
        printing_hangman(life, used_letters)
        win = "lost"
    return win_defeat(win, nick, time_score)
    

def answering_time_and_consequences(life, capital, capital_hidden, used_letters, time_score):
    while True:
        answer = input("Give me your answer: ")
        answer = answer.upper()
        if len(answer) > 1:
            if answer == capital:
                return life, "won", time_score - 10
            else:
                return life-2, "", time_score
        else:
            if answer in capital:
                if answer not in capital_hidden:
                    j = 0
                    for char in capital:
                        if char == answer:
                            capital_hidden[j] = " " + answer + "  "
                        j += 1
                    return life, "", time_score
                elif answer in capital_hidden:
                    used_letter_before()
                    continue
            else:
                if answer in used_letters:
                    used_letter_before()
                    continue
                used_letters.append(answer)
                return life -1, "", time_score