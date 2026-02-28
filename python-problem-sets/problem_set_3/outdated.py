months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    date_converter()


def date_converter():
    while True:
        old_date=input("Date: ").strip()
        if "/" in old_date:
            try:
                month, day, year = number_date_converter(old_date)
            except:
                continue
        elif "," in old_date:
            try:
                month, day, year = string_date_converter(old_date)
            except:
                continue
        else:
            continue
        if day > 31 or day < 1 or month > 12 or month < 1:
            continue
        else:
            return print(f"{year}-{month:02}-{day:02}")
            
        
def number_date_converter(date):
    return int(date.split("/")[0]), int(date.split("/")[1]), date.split("/")[2]


def string_date_converter(date):
    try:
        return months.index(date.replace(",","").split()[0])+1, int(date.replace(",","").split()[1]), date.replace(",","").split()[2]
    except ValueError:
        pass


main()