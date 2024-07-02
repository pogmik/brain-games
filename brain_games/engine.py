
ATTEMPTS = 3


def play(game):
    print('Welcome to the Brain Games!')
    name = input("May I have your name? ")
    while name == '':
        if name == '':
            name = input("May I have your name? ")
    else:
        print("Hello, " + name + "!")
    print(game.RULE)
    for _ in range(ATTEMPTS):
        question, right_answer = game.generate_data()
        print(f"Question: {question}")
        answer = input(('Your answer: '))
        if right_answer == answer:
            print('Correct!')
        else:
            print(
                f'\"{answer}\" is wrong answer ;(.'
                f' Correct answer was "{right_answer}".')
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')