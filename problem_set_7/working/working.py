import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if match := re.search(r"(?P<h1>[0-9]|1[0-2])(?P<m1>:[0-5][0-9])? (?P<t1>A|P)M to (?P<h2>1[0-2]|[0-9])(?P<m2>:[0-5][0-9])? (?P<t2>A|P)M",s):

        h1, m1, t1 = int(match.group("h1")), match.group("m1"), match.group("t1")
        h2, m2, t2 = int(match.group("h2")), match.group("m2"), match.group("t2")

        print(h1)

        hours = [h1, h2]
        minutes = [m1, m2]
        times = [t1, t2]

        for i in range(2):
            if minutes[i] == None:
                minutes[i] = ":00"

        for i in range(2):
            if times[i] == "A" and hours[i] == 12:
                hours[i] = 0
            elif times[i] == "P" and hours[i] < 12:
                hours[i] = hours[i] + 12

        return f"{hours[0]:02}{minutes[0]} to {hours[1]:02}{minutes[1]}"


    else:
        raise ValueError


if __name__ == "__main__":
    main()
