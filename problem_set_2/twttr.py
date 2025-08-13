def main():
    name = input("Input: ")
    print(f"Output: {twttr(name)}")

def twttr(name):
    vowels=["a","e","i","o","u"]
    twttr_name=""
    new_name=[char for char in name if not char in vowels]
    for char in new_name:
        twttr_name=twttr_name+char
    return twttr_name

main()