def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero."

def calculator():
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    try:
        choice = int(input("Enter operation choice (1-4): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if choice not in range(1, 5):
        print("Invalid choice. Please enter a number between 1 and 4.")
        return

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return

    if choice == 1:
        result = add(num1, num2)
        print(f"Result: {num1} + {num2} = {result}")
    elif choice == 2:
        result = subtract(num1, num2)
        print(f"Result: {num1} - {num2} = {result}")
    elif choice == 3:
        result = multiply(num1, num2)
        print(f"Result: {num1} * {num2} = {result}")
    elif choice == 4:
        result = divide(num1, num2)
        print(f"Result: {num1} / {num2} = {result}")

if __name__ == "__main__":
    calculator()