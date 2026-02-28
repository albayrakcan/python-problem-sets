def main():
    coke()

def coke():
    amount_due=50
    while amount_due>0:
        print(f"Amount Due: {amount_due}")
        try:
            coins=int(input("Insert Coin:"))
        except ValueError:
            print(f"Amount Due: {amount_due}")
            coins=int(input("Insert Coin:"))

        if (coins == 25 or coins == 10 or coins == 5):
            amount_due=amount_due-coins
    print(f"Change Owed: {abs(amount_due)}")

main()