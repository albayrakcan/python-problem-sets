def main():
    ...


def convert(fraction):
    try:
        X, Y = int(fraction.split("/")[0]), int(fraction.split("/")[1])
    except ValueError:
        raise ValueError
    
    if Y == 0:
        raise ZeroDivisionError
    
    if X > Y:
        raise ValueError

    return int(100*(X/Y))
    


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    elif 99 > percentage > 1:
        return f"{percentage}%"



if __name__ == "__main__":
    main()