import emoji

def main():
    emo = input("Input: ")
    print(f"Output: {emoji.emojize(emo,language="alias")}")

main()