
import math

def get_user_input():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    return a, b

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def log_operation(operation, result):
    with open("calculator_log.txt", "a") as file:
        file.write(f"{operation} result: {result}\n")

def main():
    a, b = get_user_input()

    print("1 - Addition\n"
          "2 - Subtraction\n"
          "3 - Multiplication\n"
          "4 - Division\n"
          )
    op = int(input("Operation: "))

    operations = {
        1: add,
        2: subtract,
        3: multiply,
        4: divide
    }

    operation_func = operations.get(op, None)
    if operation_func:
        result = operation_func(a, b)
        print(result)
        log_operation(f"Operation {op}", result)
    else:
        print("Invalid operation")

if __name__ == "__main__":
    main()
