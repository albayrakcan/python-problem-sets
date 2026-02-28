fruit_dict = {
    "apple":130,
    "avocado":50,
    "banana":110,
    "cantaloupe":50,
    "grapefruit":60,
    "grapes":90,
    "honeydew melon":50,
    "kiwifruit":90,
    "lemon":15,
    "lime":20,
    "nectarine":60,
    "orange":80,
    "peach":60,
    "pear":100,
    "pineapple":50,
    "plums":70,
    "strawberries":50,
    "sweet cherries":100,
    "tangerine":50,
    "watermelon":80,
}

fruit_list = [
    {"fruit":"apple","calorie":130},
    {"fruit":"avocado","calorie":50},
    {"fruit":"banana","calorie":110},
    {"fruit":"cantaloupe","calorie":50},
    {"fruit":"grapefruit","calorie":60},
    {"fruit":"grapes","calorie":90},
    {"fruit":"honeydew melon","calorie":50},
    {"fruit":"kiwifruit","calorie":90},
    {"fruit":"lemon","calorie":15},
    {"fruit":"lime","calorie":20},
    {"fruit":"nectarine","calorie":60},
    {"fruit":"orange","calorie":80},
    {"fruit":"peach","calorie":60},
    {"fruit":"pear","calorie":100},
    {"fruit":"pineapple","calorie":50},
    {"fruit":"plums","calorie":70},
    {"fruit":"strawberries","calorie":50},
    {"fruit":"sweet cherries","calorie":100},
    {"fruit":"tangerine","calorie":50},
    {"fruit":"watermelon","calorie":80},
]

def main():
    fruit = input("Item: ").lower()
    nutrition(fruit)
    # nutrition_list(fruit)

def nutrition(fruit):
    print(f"Calories: {fruit_dict[fruit]}") if fruit in fruit_dict.keys() else print("", end='')
        
"""
def nutrition_list(fruit_name):
    for fruit in fruit_list:
        if fruit_name == fruit["fruit"]:
            print(f"Calories: {fruit["calorie"]}")
"""

main()