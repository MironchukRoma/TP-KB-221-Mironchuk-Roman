
import math
from calculator_functions import sum, minus, multiply, divide

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

main()
