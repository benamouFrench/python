# Simple Calculator Program

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

def calculator():
    print("Welcome to the Calculator!")
    print("Available operations: add, subtract, multiply, divide")
    
    while True:
        operation = input("Enter operation (or 'exit' to quit): ").strip().lower()
        if operation == 'exit':
            print("Goodbye!")
            break
        
        if operation not in ['add', 'subtract', 'multiply', 'divide']:
            print("Invalid operation. Please try again.")
            continue
        
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue
        
        if operation == 'add':
            print(f"Result: {add(num1, num2)}")
        elif operation == 'subtract':
            print(f"Result: {subtract(num1, num2)}")
        elif operation == 'multiply':
            print(f"Result: {multiply(num1, num2)}")
        elif operation == 'divide':
            print(f"Result: {divide(num1, num2)}")

# Run the calculator
if __name__ == "__main__":
    calculator()