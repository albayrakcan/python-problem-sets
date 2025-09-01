from validator_collection import validators, checkers, errors


def validate(s):
    try:
        if result := validators.email(s):
            return "Valid"
    except errors.InvalidEmailError:
        return "Invalid"


def main():
    print(validate(input("What's your email address? ")))


if __name__ == "__main__":
    main()
