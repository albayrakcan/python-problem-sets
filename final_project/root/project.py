import argparse
import sys
import csv
import os
import re
from enum import Enum
import calendar
from datetime import datetime

Choices = Enum("Choices", [("week", 5), ("month", 20)])

def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="subparser_name", required=True)

    # required working hours for the basic shift
    work_parser = subparsers.add_parser("required", aliases=["re"])
    work_group = work_parser.add_mutually_exclusive_group(required=True)
    work_group.add_argument("-d", "--daily", type=int, dest="dy", default=0)
    work_group.add_argument("-w", "--weekly", type=int, dest="wy", default=0)
    work_group.add_argument("-m", "--monthly", type=int, dest="my", default=0)
    work_parser.set_defaults(function=required_working_hours)

    # worked hours for the basic shift
    basic_parser = subparsers.add_parser("basic", aliases=["bs"])
    basic_parser.add_argument("-i", "--info", action="count", required=True)
    basic_parser.add_argument("hr", type=str)
    global Choices
    basic_parser.add_argument("request", choices=Choices.__members__)
    basic_parser.set_defaults(function=basic_shift)

    # worked hours for pro shift
    pro_parser = subparsers.add_parser("pro", aliases=["pr"])
    punch_subparser = pro_parser.add_subparsers(dest="subparser_name", required=True)
    punch_parser = punch_subparser.add_parser("punch", aliases=["pn"])
    punch_group = punch_parser.add_mutually_exclusive_group(required=True)
    punch_group.add_argument(
        "-ti", "--tin", action="store_const", dest="timein", const=datetime.now()
    )
    punch_group.add_argument(
        "-to", "--tout", action="store_const", dest="timeout", const=datetime.now()
    )
    punch_group.add_argument("-dh", "--dthr", dest="datehour", type=str)
    punch_group.set_defaults(function=punch_function)

    # add holiday to the pro shift
    holiday_parser = punch_subparser.add_parser("holiday", aliases=["hd"])
    holiday_parser.add_argument("holiday", type=str)
    holiday_parser.set_defaults(function=set_holiday)

    # request remaining working hours
    week_parser = punch_subparser.add_parser("week", aliases=["w"])
    week_parser.add_argument("-i", "--info", action="count", required=True)
    week_parser.add_argument(
        "month",
        type=int,
        choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        nargs="?",
        default=datetime.now().month,
    )
    week_parser.add_argument(
        "year",
        type=int,
        choices=range(2024, 2050),
        nargs="?",
        default=datetime.now().year,
    )
    week_parser.set_defaults(function=weeks_shift)

    month_parser = punch_subparser.add_parser("month", aliases=["m"])
    month_parser.add_argument("-i", "--info", action="count", required=True)
    month_parser.add_argument(
        "month",
        type=int,
        choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        nargs="?",
        default=datetime.now().month,
    )
    month_parser.add_argument(
        "year",
        type=int,
        choices=range(2024, 2050),
        nargs="?",
        default=datetime.now().year,
    )
    month_parser.set_defaults(function=months_shift)

    args = parser.parse_args()
    args.function(args)


# save required working hours to a csv file
def required_working_hours(args):
    lst = [args.dy, args.wy / 5, args.my / 20]

    daily_hour = str(max(set(lst)))
    weekly_hour = str(float(daily_hour) * 5)
    monthly_hour = str(float(daily_hour) * 20)  # assumes a month is 4 weeks

    try:
        os.makedirs("hours")
    except FileExistsError:
        pass

    with open("hours/hours.csv", "w", newline="") as file:
        writer = csv.DictWriter(
            file, fieldnames=["daily_hour", "weekly_hour", "monthly_hour"]
        )
        writer.writeheader()
        writer.writerow(
            {
                "daily_hour": daily_hour,
                "weekly_hour": weekly_hour,
                "monthly_hour": monthly_hour,
            }
        )

    print(f"work is {daily_hour} hours a day with lunch time included")


# get the weekdays of a given year
def get_weekdays(year):
    cal = calendar.Calendar()
    weekdays = []

    for month in range(12):
        days2 = cal.itermonthdays2(
            year, month + 1
        )  # tuple (date (days from next/previous month are zero), weekdays (0-6))
        day_number = 0
        for day in days2:
            if day[0] == 0 or day[1] in (5, 6):
                continue  # eliminate days from next/previous month and weekends
            day_number += 1
            weekdays.append(
                {
                    "date": f"{year}-{format((month+1),"02")}-{format(day[0],"02")}",
                    "day": day_number,  # day shows the number of weekdays in a month
                    "weekday": day[1]
                    + 1,  # weekday shows the day, monday is 1 friday is 5
                }
            )

    return weekdays


# create a csv file that has all the weekdays in a year
def create_yearly_csv(year):
    if not os.path.exists("hours"):
        sys.exit("no file is found! enter required working hours")

    if os.path.isfile(f"hours/{year}.csv"):
        return

    weekdays = get_weekdays(year)

    with open(f"hours/{year}.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["date", "day", "weekday", "hours"])
        writer.writeheader()
        for days in weekdays:
            writer.writerow(
                {"date": days["date"], "day": days["day"], "weekday": days["weekday"]}
            )


# hour regex for hours and minutes, return total hours
def hours_regex(s):
    if match := re.fullmatch(
        r"( *(?P<hour>[0-1]?[0-9]|2[0-3]) *h\D*)?((?P<minute>[0-5]?[0-9]) *m\D*)?",
        s,
        re.IGNORECASE,
    ):
        hours = list(
            map(
                lambda x: 0 if x is None else x,
                [match.group("hour"), match.group("minute")],
            )
        )
        return float(hours[0]) + float(hours[1]) / 60
    else:
        sys.exit("wrong format, try again")


# date regex, return datetime object
def date_regex(s):
    if match := re.fullmatch(
        r" *(?P<day>0?[1-9]|[12][0-9]|3[01]) *[.-/ ] *(?P<month>0?[1-9]|1[0-2]) *[.-/ ] *(?P<year>202[5-9]) *",
        s,
    ):
        return datetime(
            int(match.group("year")), int(match.group("month")), int(match.group("day"))
        )
    else:
        sys.exit("wrong format, try again")


# date hours regex, return a list of dict that has datetime object and hours
def date_hours_regex(s):
    if match := re.fullmatch(
        r" *(?P<day>0?[1-9]|[12][0-9]|3[01]) *[.-/ ] *(?P<month>0?[1-9]|1[0-2]) *[.-/ ] *(?P<year>202[5-9])( *(?P<hour>[0-1]?[0-9]|2[0-3]) *h\D*)?((?P<minute>[0-5]?[0-9]) *m\D*)?",
        s,
        re.IGNORECASE,
    ):
        hours = list(
            map(
                lambda x: 0 if x is None else x,
                [match.group("hour"), match.group("minute")],
            )
        )
        return {
            "date": datetime(
                int(match.group("year")),
                int(match.group("month")),
                int(match.group("day")),
            ),
            "hours": float(hours[0]) + float(hours[1]) / 60,
        }
    else:
        sys.exit("wrong format, try again")


# get the required working hours for a day
def read_hours_csv():
    try:
        with open("hours/hours.csv", "r") as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            return float(rows[0]["daily_hour"])
    except FileNotFoundError:
        sys.exit("no file is found! enter required working hours")


# read the year.csv and get the dictionary
def read_year_csv(year):
    weekdays = []

    with open(f"hours/{year}.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            weekdays.append(row)

    return weekdays


# set the worked hours to required daily hour on a holiday
def set_holiday(args):

    date_worked = []
    dates = list(map(date_regex, args.holiday.split(",")))
    for date in dates:
        date_worked.append({"date": date, "hours": str(read_hours_csv())})

    fill_sheet(date_worked)


# return a list of dictionary with datetime object and worked hours
def punch_function(args):
    if args.timein is not None:  # save the date and the hour to clock in
        try:
            with open(f"hours/daily.csv", "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["timein"])
                writer.writeheader()
                writer.writerow({"timein": args.timein})
        except FileNotFoundError:
            sys.exit("no file is found! enter required working hours")

    if args.timeout is not None:  # subtract the clock in hour from the clock out hour
        try:
            with open(f"hours/daily.csv", "r", newline="") as file:
                reader = csv.DictReader(file)
                row = next(reader)
                timein = datetime.fromisoformat(row["timein"])
        except FileNotFoundError:
            sys.exit("no file is found! enter required working hours")

        if args.timeout.date() != timein.date():
            sys.exit("you have to punch out at the same day!")

        delta = args.timeout - timein
        hours = delta.total_seconds() / 3600
        date_worked = [{"date": args.timeout, "hours": hours}]
        fill_sheet(date_worked)

    if args.datehour is not None:  # get the list of dates and corresponding hours
        date_worked = list(map(date_hours_regex, args.datehour.split(",")))
        fill_sheet(date_worked)


# fill the year.csv if the dates given are weekdays
def fill_sheet(date_worked):
    years = set(map(lambda x: x["date"].year, date_worked))
    for year in years:
        create_yearly_csv(year)

        weekdays = read_year_csv(year)

        for date in date_worked:
            for weekday in weekdays:
                if weekday["date"] == str(date["date"].date()):
                    weekday["hours"] = date["hours"]

        with open(f"hours/{year}.csv", "w", newline="") as file:
            writer = csv.DictWriter(
                file, fieldnames=["date", "day", "weekday", "hours", "holiday"]
            )
            writer.writeheader()
            for weekday in weekdays:
                writer.writerow(weekday)


# return a list of dictionary that has the dates for a specific month
def get_months_shift(year, month):
    worked = []

    weekdays = read_year_csv(year)
    for weekday in weekdays:
        if datetime.fromisoformat(weekday["date"]).month == month:
            worked.append(
                {
                    "day": weekday["day"],
                    "weekday": weekday["weekday"],
                    "hours": weekday["hours"],
                }
            )

    return worked


# check if a months shift has any gaps, if not return a list of dictionary that has the filled days only
def check_months_shift(worked):
    hours_worked_dict = []

    if worked[0]["hours"] == "":
        sys.exit("there are missing days!")

    check = True
    for day in worked:
        if not check and day["hours"] != "":
            sys.exit("there are missing days!")

        if check and day["hours"] == "":
            check = False

        if check:
            hours_worked_dict.append(day)

    return hours_worked_dict


# calculates the required working hours for the remaining days in a week or a month
def basic_shift(args):
    hours_worked = list(map(hours_regex, args.hr.split(",")))
    global Choices
    days_required = Choices[args.request].value

    report_hours(
        hours_worked, len(hours_worked), days_required, args.request, args.info
    )


# calculates the required working hours for the remaining days in a week by checking the csv
def weeks_shift(args):
    worked = get_months_shift(args.year, args.month)

    hours_worked_dict = check_months_shift(worked)

    days_worked = int(hours_worked_dict[-1]["weekday"])

    hours_worked = []
    for day in reversed(hours_worked_dict):
        hours_worked.append(float(day["hours"]))
        if day["weekday"] == "1":
            break

    report_hours(hours_worked, days_worked, 5, "week", args.info)


# calculates the required working hours for the remaining days in a month by checking the csv
def months_shift(args):
    worked = get_months_shift(args.year, args.month)

    hours_worked_dict = check_months_shift(worked)

    days_worked = int(hours_worked_dict[-1]["day"])
    days_required = int(worked[-1]["day"])

    hours_worked = []
    for day in hours_worked_dict:
        hours_worked.append(float(day["hours"]))

    report_hours(hours_worked, days_worked, days_required, "month", args.info)


# reports the remaining hours
def report_hours(hours_worked, days_worked, days_required, request, info):

    hours_required = read_hours_csv()

    if days_worked > days_required:
        sys.exit(
            f"the number of days should be lower than {days_required} for the {request} option "
        )

    time_left = hours_required * days_worked - sum(hours_worked)
    days_left = days_required - days_worked
    hours_left, minutes_left = int(time_left), round(
        (time_left - int(time_left)) * 60, 2
    )

    if days_worked == days_required:
        if time_left <= 0:
            print(
                f"you have completed the {request} with extra {abs(hours_left)} hours and {abs(minutes_left)} minutes"
            )
            return
        else:
            print(
                f"you have completed the {request} with missing {abs(hours_left)} hours and {abs(minutes_left)} minutes"
            )
            return

    time_spread = hours_required + time_left / days_left
    hours_spread, minutes_spread = int(time_spread), round(
        (time_spread - int(time_spread)) * 60, 2
    )

    if info == 1:
        if time_left <= 0:
            print(
                f"you have extra {abs(hours_left)} hours and {abs(minutes_left)} minutes so far"
            )
        else:
            print(f"you are short {hours_left} hours and {minutes_left} minutes so far")
    else:
        print(
            f"you have to work {hours_spread} hours and {minutes_spread} minutes for the remaining {days_left} days to complete {hours_required*days_required} hours this {request}"
        )


if __name__ == "__main__":
    main()
