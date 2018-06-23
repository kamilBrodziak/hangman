import time


def loading_highscore_file_into_list():
    highscore_list = []
    with open('highscores.txt', 'r') as highscores:
        for line in highscores:
            one_score = line.split(" ", )
            if line != "" and line != '\n' and line != " ":
                highscore_list.append(one_score)
    return highscore_list


def highscore_add_to_highscore_list(nick, time_score, guessed_word):
    highscore_list = loading_highscore_file_into_list()
    time_clock = time.asctime()
    time_clock = time_clock.split(" ",)
    guessed_word = guessed_word.split(" ")
    guessed_word = "_".join(guessed_word)
    highscore_list.append(
        (nick, str(time_score), "_".join(time_clock), guessed_word))
    sorted_highscore_list = sorted(highscore_list, key=lambda x: float(x[1]))
    if len(sorted_highscore_list) > 10:
        sorted_highscore_list = sorted_highscore_list[:-1]
    return sorted_highscore_list


def add_highscore_to_file(nick, time_score, guessed_word):
    sorted_highscore_list = highscore_add_to_highscore_list(
        nick, time_score, guessed_word)
    with open('highscores.txt', 'w') as highscores:
        for i in sorted_highscore_list:
            line = i[0] + " " + str(i[1]) + " " + str(i[2]) + " " + i[3]
            highscores.write(line + '\n')
