import inflect

p = inflect.engine()


def main():
    names = []
    while True:
        try:
            name = input("Name: ")
        except EOFError:
            print(f"Adieu, adieu, to {p.join(names)}")
            break
        else:
            names.append(name)


main()
