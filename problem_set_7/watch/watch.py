import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if match := re.search(r"https?://(?:www\.)?youtube\.com/embed/(?P<url>[a-zA-Z0-9]+)\"",s):
        return f"https://youtu.be/{match.group("url")}"
    

if __name__ == "__main__":
    main()
