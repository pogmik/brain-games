import random
import sys
count = random.randint(1, 100)


def game_calc():
    print('Welcome to the Brain Games!')
    global right_answer
    name = input("May I have your name? ")
    while name == '':
        if name == '':
            name = input("May I have your name? ")
    else:
        print("Hello, " + name + "!")
    i = 0
    print('What is the result of the expression?')
    while i < 3:
        operators = ['-', '+', '*']
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(operators)
        print("Question:", num1, operator, num2)
        player = input("Your answer: ")
        if operator == '-':
            right_answer = num1 - num2
        elif operator == '*':
            right_answer = num1 * num2
        elif operator == '+':
            right_answer = num1 + num2
        if int(player) == right_answer:
            print("Correct!")
        if int(player) != right_answer :
            sys.exit(f"'{player}' is wrong answer ;(. Correct answer was '{right_answer}' .\nLet's try again, '{name}'")
        i += 1
        if i == 3 :
            sys.exit(f"Congratulations, {name}!")








if __name__ == "__main__":
    game_calc()
