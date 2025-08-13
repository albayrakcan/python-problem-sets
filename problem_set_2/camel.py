def main():
    camelCase=input("camelCase: ")
    snake = camel(camelCase)
    print(f"snake_case: {snake}")

def camel(camelCase):
    snake=""
    for char in camelCase:
        if char.isupper():
            snake = snake + "_" + char.lower()
        else:
            snake = snake + char
    
    return snake
        
main()