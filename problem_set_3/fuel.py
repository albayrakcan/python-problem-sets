def main():
    print(fuel())

def fuel():
    while True:
        fraction=input("Fraction: ")
        if "-" in fraction:
            continue
        try:
            X, Y = int(fraction.split("/")[0]), int(fraction.split("/")[1])
            percent = round(100*(X/Y))
        except ZeroDivisionError:
            pass
        except ValueError:
            pass
        else:
            if percent <= 1:
                return "E"
            elif 100 >= percent >= 99:
                return "F"
            elif 100 >= percent:
                return f"{percent}%"

main()