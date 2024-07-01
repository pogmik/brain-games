import random

import string
import sys
count = random.randint(1, 100)


from brain_games.cli  import *


def game_even():
    print('Welcome to the Brain Games!')
    name = input("May I have your name? ")
    while name == '':
        if name == '':
            name = input("May I have your name? ")
    else:
        print("Hello, " + name + "!")
    i = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while i < 3:
        count = random.randint(1, 100)
        print("Question:", count)
        player = input("Your answer: ")
        if player != "yes" and player != "no":
            sys.exit("'" + player + "'" + " is wrong answer;(.Correct answer was 'yes' or 'no'.\nLet's try again," + name + "!")
        elif player == "yes" and count % 2 == 0:
            print("Correct!")
        elif player == "no" and count % 2 != 0:
            print("Correct!")
        i += 1
        if i == 3:
            sys.exit("Congratulations, " + name + "!")
        if player == "yes" and count % 2 != 0:
            sys.exit("'yes' is wrong answer;(.Correct answer was 'no'.\nLet's try again," + name + "!")
        elif player == "no" and count % 2 == 0:
            sys.exit("'no' is wrong answer;(.Correct answer was 'yes'.\nLet's try again," + name + "!")


if __name__ == "__main__":
    game_even()



