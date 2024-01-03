def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def main():
    print("Welcome to the Simple Calculator!")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("Choose the operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        result = add(num1, num2)
        operation = "+"
    elif choice == 2:
        result = subtract(num1, num2)
        operation = "-"
    elif choice == 3:
        result = multiply(num1, num2)
        operation = "*"
    elif choice == 4:
        result = divide(num1, num2)
        operation = "/"
    else:
        print("Invalid choice. Please try again.")
        return

    print(f"{num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    main()