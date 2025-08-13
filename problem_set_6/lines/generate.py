import random
"""
import random

coin = random.choice(["heads", "tails"])
print(coin)


from random import choice

coin = choice(["heads", "tails"])
print(coin)

# random integer between and including 1 and 10
number = random.randint(1,10)
print(number)
"""

cards=["king","queen","jack"]
random.shuffle(cards)
for card in cards:
    print(card)
