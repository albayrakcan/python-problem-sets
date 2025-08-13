import sys


def get_input():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].rsplit(".", 1)[1] == "py":
        sys.exit("Not a Python file")


def count_lines(file_name):
    line_count = 0

    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")

    for line in lines:
        if line.startswith("#"):
            continue
        elif line.strip() == "":
            continue

        line_count += 1
    
    return line_count


if __name__ == "__main__":
    get_input()
    print(count_lines(sys.argv[1]))
