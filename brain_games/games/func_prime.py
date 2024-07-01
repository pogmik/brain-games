import sys
import random


def game_prime():
    print('Welcome to the Brain Games!')
    name = input("May I have your name? ")
    while name == '':
        if name == '':
            name = input("May I have your name? ")
    else:
        print("Hello, " + name + "!")
        print('Answer "yes" if given number is prime. Otherwise answer "no".')
        i = 0
        while i < 3:
            count = random.randint(2, 50)
            print("Question:", count)
            player = input("Your answer: ")
            d = 2
            while count % d != 0:
                d += 1
            if d == count and player == 'no':
                sys.exit("'no' is wrong answer;(.Correct answer was 'yes'.\nLet's try again, " + name + "!")
            elif count != d and player == 'yes':
                sys.exit("'yes' is wrong answer;(.Correct answer was 'yes'.\nLet's try again, " + name + "!")
            elif count == d and player == 'yes':
                print('Correct!')
            elif count != d and player == 'no':
                print('Correct!')

            i += 1
            if i == 3:
                sys.exit(f"Congratulations, {name}!")

if __name__ == "__main__":
    game_prime()
