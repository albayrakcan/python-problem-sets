import random


def main():
    points = 0
    level = get_level()
    for _ in range(10):
        x, y = generate_integer(level), generate_integer(level)
        correct_answer = x + y
        tries = 0
        for _ in range(3):
            try:
                answer = int(input(f"{x} + {y} = "))
            except ValueError:
                tries += 1
                print("EEE")
                if tries == 3:
                    print(f"{x} + {y} = {correct_answer}")
                continue
            if answer == correct_answer:
                points += 1
                break
            else:
                tries += 1
                print("EEE")
                if tries == 3:
                    print(f"{x} + {y} = {correct_answer}")

    print(f"Score: {points}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue
        if level == 1 or level == 2 or level == 3:
            return level


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
