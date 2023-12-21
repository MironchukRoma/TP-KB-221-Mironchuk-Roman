# 1) Написати програму калькулятор з постійними запитами на введення нових даних та операцій.

while(True):
    print(
        "1 - Addition\n"
        "2 - Subtraction\n"
        "3 - Multiplication\n"
        "4 - Division\n"
        )
    op = int(input("Operation: "))
    a = int(input("Enter num1: "))
    b = int(input("Enter num2: "))


    def sum(a,b):
        return a + b
    def minus(a,b):
        return a - b
    def multiply(a,b):
        return a * b
    def divide(a,b):
        return a / b

    if op == 1:
        result = sum(a,b)
        print ("\nresult", result, "\n")
    elif op == 2:
        result = minus(a,b)
        print ("\nresult", result, "\n")
    elif op == 3:
        result = multiply(a,b)
        print ("\nresult", result, "\n")
    elif op == 4:
        result = divide(a,b)
        print ("\nresult", result, "\n")