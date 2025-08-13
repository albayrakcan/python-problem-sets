import random


def main():
    actual_number = guess_number()
    try_number(actual_number)


def guess_number():
    while True:
        try:
            level_n = int(input("Level: "))
        except ValueError:
            continue
        if level_n > 0:
            break
    return random.randint(1, level_n)


def try_number(actual_number):
    while True:
        try:
            guess = int(input("Guess: "))
        except ValueError:
            continue
        if guess <= 0:
            continue
        elif guess < actual_number:
            print("Too small!")
            continue
        elif guess > actual_number:
            print("Too large!")
        elif guess == actual_number:
            return print("Just right!")


main()
