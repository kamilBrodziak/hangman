import time
import sys
from list_containing_capital_transformations import *
from printing import printing_hangman, cls, display_hint, win_defeat, used_letter_before, display_test_hint, printing_hint_and_capital
from leaderboard import highscore_add_to_highscore_list, add_highscore_to_file


def game_start(nick, hint):
    with open('countries_and_capitals.txt') as countries:
        capitals = countries.readlines()
    cou_cap = change_random_line_into_list(capitals)
    win = ""
    time_score = 0
    life = 6
    used_letters = []
    capital_display_on_screen = [" ___"] * len(cou_cap[1])
    start_time = time.time()
    capital_guessed_template = change_capital_word_into_capital_guessed_template(cou_cap[1])
    delete_spaces_in_capital_display_on_screen(cou_cap[1], capital_display_on_screen)
    cls()
    while life > 0:
        cls()
        printing_hangman(life, used_letters)
        printing_hint_and_capital(capital_display_on_screen, cou_cap, life, hint)
        life, win, time_score = make_guess(
                    life, cou_cap[1], capital_display_on_screen, used_letters, time_score)
        if capital_guessed_template == capital_display_on_screen or win == "won":
            time_score += time.time() - start_time
            add_highscore_to_file(nick, time_score, cou_cap[1])
            break
    cls()
    printing_hangman(life, used_letters)
    win = "lost" if life < 1 else "won"
    return win_defeat(win, nick, time_score)


def make_guess(
        life, capital, capital_display_on_screen, used_letters, time_score):
    while True:
        answer = input("Give me your answer: ").upper()
        if not answer.isalpha() and len(answer) < 2:
            continue
        if answer in capital_display_on_screen or answer in used_letters:
            used_letter_before()
            continue
        if len(answer) > 1:
            if answer == capital:
                return life, "won", time_score - 10
            else:
                return life - 2, "", time_score
        else:
            if answer in capital and answer not in capital_display_on_screen:
                return add_letter_to_capital_display_on_screen(
                    life, time_score, capital_display_on_screen, capital, answer)
            else:
                used_letters.append(answer)
                return life - 1, "", time_score
