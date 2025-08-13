import re

def main():
    greeting = input("Greeting: ")
    print(f"${value(greeting)}")


def value(greeting):
    greeting_no_spaces = greeting.strip()
    greeting_lower = greeting_no_spaces.lower()
    greeting_split = re.split(r"[ \t,;.!?]+", greeting_lower)
    first_word = greeting_split[0]

    if first_word == "hello":
        return 0
    elif first_word[0] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
