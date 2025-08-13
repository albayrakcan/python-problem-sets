def main():
    expression=input("Expression: ").strip()
    print(interpreter(expression))

def interpreter(expression):
    x, y, z = expression.split()
    x = int(x)
    z = int(z)
    match y:
        case "+":
            return round(float(x + z), 1)
        case "-":
            return round(float(x - z), 1)
        case "*":
            return round(float(x * z), 1)
        case "/":
            return round(float(x / z), 1)
        
main()
