import random
import sys



def game_progression():
    print('Welcome to the Brain Games!')
    name = input("May I have your name? ")
    while name == '':
        if name == '':
            name = input("May I have your name? ")
    else:
        print("Hello, " + name + "!")
    i = 0
    print('What number is missing in the progression')
    while i < 3:
        stop = random.randint(50, 100)
        step = random.randint(1, 5)
        result = list(range(random.randint(0, 9), stop, step))[: 10]
        random_index = random.randint(0, len(result) - 1)
        right_answer = result[random_index]
        result[random_index] = ".."
        question = " ".join(map(str, (result)))
        print("Question: ", question)
        player = int(input("Your answer: "))
        if player == right_answer:
            print("Correct!")
        elif player != right_answer:
            sys.exit(f"'{player}' is wrong answer ;(. Correct answer was '{right_answer}'.\nLet's try again, '{name}'")
        i += 1
        if i == 3:
            sys.exit(f"Congratulations, {name}!")



if __name__ == "__main__":
    game_progression()