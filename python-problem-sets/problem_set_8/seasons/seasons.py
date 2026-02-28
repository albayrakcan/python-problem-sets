from datetime import date
import re
import sys
import inflect


def main():
    print_delta_minutes(date.today(), get_birthday_date())


def get_birthday_date():
    date_of_birth = input("Date of Birth: ")
    if match := re.fullmatch(
        r"(?P<year>[0-2][0-9]{3})-(?P<month>0[1-9]|1[0-2])-(?P<day>0[1-9]|[1-2][0-9]|3[0-1])",
        date_of_birth,
    ):
        return date(
            int(match.group("year")), int(match.group("month")), int(match.group("day"))
        )
    else:
        sys.exit("Invalid Date")


def print_delta_minutes(day1, day2):
    p = inflect.engine()
    value = str(
        p.number_to_words((day1 - day2).days * 24 * 60, andword="")
    ).capitalize()
    unit = str(p.plural_noun("minute", (day1 - day2).days * 24 * 60))
    print(value, unit)


if __name__ == "__main__":
    main()
