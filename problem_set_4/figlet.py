from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
font_list = figlet.getFonts()


def main():
    if len(sys.argv) == 1:
        text = get_input()
        random_font(text)
    elif (
        len(sys.argv) == 3
        and sys.argv[1] == "-f"
        or sys.argv[1] == "--font"
        and sys.argv[2] in font_list
    ):
        text = get_input()
        fixed_font(text, sys.argv[2])
    else:
        sys.exit("Invalid usage")


def random_font(text):
    figlet.setFont(font=font_list[random.randint(0, len(font_list) - 1)])
    print(figlet.renderText(text))


def fixed_font(text, font):
    figlet.setFont(font=font)
    print(figlet.renderText(text))


def get_input():
    text = input("Input: ")
    print("Output: ")
    return text


main()
