import csv
import sys

def scourgify(before, after):
    try:
        with open(before, "r", encoding="utf-8") as csvfile_before, open(after, "w", newline="", encoding="utf-8") as csvfile_after:
            reader = csv.DictReader(csvfile_before)
            writer = csv.DictWriter(csvfile_after, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for row in reader:
                last, first = row["name"].split(", ")
                writer.writerow({"first":first, "last":last, "house":row["house"]})
    except FileNotFoundError:
        sys.exit(f"Could not read {before}")


def get_input():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        scourgify(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    get_input()
