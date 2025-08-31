import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    if match := re.findall(r"\bum\b",s.lower()):
        return len(match)


...


if __name__ == "__main__":
    main()