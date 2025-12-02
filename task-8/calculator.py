from typing import Union

def add(x: float, y: float) -> float:
    """Adds two numbers."""
    return x + y

def subtract(x: float, y: float) -> float:
    """Subtracts two numbers."""
    return x - y

def multiply(x: float, y: float) -> float:
    """Multiplies two numbers."""
    return x * y

def divide(x: float, y: float) -> Union[float, str]:
    """Divides two numbers, with a check for division by zero."""
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def main():
    """Main function to run the calculator CLI."""
    
    operations = {
        '1': (add, '+'),
        '2': (subtract, '-'),
        '3': (multiply, '*'),
        '4': (divide, '/'),
    }

    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice(1/2/3/4/5): ")

        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in operations:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            operation_func, symbol = operations[choice]
            result = operation_func(num1, num2)
            print(f"{num1} {symbol} {num2} = {result}")

        else:
            print("Invalid choice. Please select a valid operation (1-5).")

if __name__ == "__main__":
    main()