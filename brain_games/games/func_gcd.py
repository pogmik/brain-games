import random
import sys
import math


def game_gcd():
    global right_answer
    name = input("May I have your name? ")
    while name == '':
        if name == '':
            name = input("May I have your name? ")
    else:
        print("Hello, " + name + "!")
    i = 0
    while i < 3:
        count_one = random.randint(1, 50)
        count_two = random.randint(1, 50)
        print("Find the greatest common divisor of given numbers.")
        print("Question:", count_one, count_two)
        right_answer = math.gcd(count_one, count_two)
        player = int(input("Your answer: "))
        if player == right_answer:
            print("Correct!")
        elif player != right_answer:
            sys.exit(f"'{player}' is wrong answer ;(. Correct answer was '{right_answer}'.\nLet's try again, '{name}'")
        i += 1
        if i == 3:
            sys.exit(f"Congratulations, {name}!")


if __name__ == "__main__":
    game_gcd()

