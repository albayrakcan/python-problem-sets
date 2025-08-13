def main():
    name = input("Input: ")
    print(f"Output: {shorten(name)}")

def shorten(word):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    twttr_name=""
    new_name=[char for char in word if not char in vowels]
    for char in new_name:
        twttr_name = twttr_name + char
    return twttr_name

if __name__ == "__main__":
    main()