def welcome_user():
    name = input("May I have your name? ")
    while name == '':
        if name == '':
            name = input("May I have your name? ")
    else:
        print("Hello, " + name + "!")
    print(name)



if __name__ == "__main__":
    welcome_user()
