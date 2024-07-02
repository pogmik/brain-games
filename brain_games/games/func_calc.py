from random import randint
import random
RULE = 'What is the result of the expression?'


def generate_data():
    operators = ['-', '+', '*']
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    operator = random.choice(operators)
    question = f"{num1} {operator} {num2}"
    if operator == '-':
        right_answer = num1 - num2
    elif operator == '*':
        right_answer = num1 * num2
    elif operator == '+':
        right_answer = num1 + num2
    return question, str(right_answer)