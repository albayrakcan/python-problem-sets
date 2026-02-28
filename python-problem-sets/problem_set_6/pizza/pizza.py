from tabulate import tabulate
import sys
import csv


def tabulate_menu(menu):
    menu_list = []

    try:
        with open(menu, "r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            print(tabulate(reader, tablefmt="grid",headers="keys"))
    except:
        sys.exit("File does not exist")


def get_input():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].split(".")[1] != "csv":
        sys.exit("Not a CSV file")
    else:
        tabulate_menu(sys.argv[1])


if __name__ == "__main__":
    get_input()
