def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return True if word_limit(s, 2, 6) and word_start(s, 2) and word_check(s) and number_check(s, 2) else False

def word_limit(word, lower, upper):
    lower, upper = int(lower), int(upper)
    return True if lower <= len(word) <= upper else False

def word_start(word, lower):
    lower = int(lower)
    return word[:lower].isalpha()

def word_check(word):
    return word.isalnum()

def number_check(word, limit):
    limit = int(limit)
    word = word[limit:]
    if len(word) == 0:
        return True
    if word.isalpha():
        return True
    for i in range(len(word)):
        if word[i].isdigit():
            word = word[i:]
            break
    return False if word[0] == "0" else word.isdigit()


if __name__ == "__main__":
    main()