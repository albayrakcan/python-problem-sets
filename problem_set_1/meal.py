def main():
    time=input("What time is it? ").strip()
    convert(time)

def convert(time):
    hours, minutes=time.split(':')
    hours = float(hours)
    minutes = float(minutes)
    hours = hours + minutes/60

    if 7 <= hours <= 8:
        print("breakfast time")
    elif 12 <= hours <= 13:
        print("lunch time")
    elif 18 <= hours <= 19:
        print("dinner time")

main()