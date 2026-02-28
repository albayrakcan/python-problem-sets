def main():
    grocery()

def grocery():
    items=[]
    while True:
        try:
            item=input("").upper()
        except EOFError:
            break
        else:
            items.append(item)
        items = sorted(items)
    count(items)

def count(items):
    count_dict = {}
    for item in items:
        if item not in count_dict:
            count_dict[item] = items.count(item)
    print_dict(count_dict)

def print_dict(dict):
    for item in dict:
        print(f"{dict[item]} {item}")

main()
