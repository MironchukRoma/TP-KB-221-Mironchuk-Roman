import math

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Error: Division by zero"

def get_operation_choice():
    print("1 - Addition\n"
          "2 - Subtraction\n"
          "3 - Multiplication\n"
          "4 - Division\n"
    )
    return int(input("Operation: "))

def main():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    calculator = Calculator(a, b)
    op = get_operation_choice()

    if op == 1:
        result = calculator.add()
    elif op == 2:
        result = calculator.subtract()
    elif op == 3:
        result = calculator.multiply()
    elif op == 4:
        result = calculator.divide()

    print(result)

if __name__ == "__main__":
    main()
