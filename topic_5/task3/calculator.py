import math

a = int(input("Enter a: "))
b = int(input("Enter b: "))
print( "1 - Addition\n"
       "2 - Subtraction\n"
       "3 - Multiplication\n"
       "4 - Division\n"
    )
op = int(input("Operation: "))

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
elif op == 2:
    result = minus(a,b)
elif op == 3:
    result = multiply(a,b)
elif op == 4:
   result = divide(a,b)

print (result)


