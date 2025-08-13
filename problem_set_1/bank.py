def main():
    greeting=input("Greeting: ").strip().lower()
    bank(greeting)

def bank(greeting):
    first_word=greeting.split()[0]
    
    if first_word == "hello":
        print("$0")
    elif greeting[0] == "h":
        print("$20")
    else:
        print("$100")

main()