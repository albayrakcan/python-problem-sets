def main():
    greeting=input("Greeting: ").strip().lower()
    bank(greeting)


def bank(greeting):
    if greeting.find("hello") == 0:
        print("$0")
    elif greeting[0] == "h":
        print("$20")
    else:
        print("$100")


main()
