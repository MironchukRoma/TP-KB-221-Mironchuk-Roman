import math

class Calculator:
    def init(self, a, b):
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