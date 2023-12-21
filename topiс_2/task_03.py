import math

num1 = int(input("Enter a: "))
num2 = int(input("Enter b: "))
print( "1 - Addition\n"
       "2 - Subtraction\n"
       "3 - Multiplication\n"
       "4 - Division\n"
    )

operation = (input("Operation: "))

match operation:
        case '1':
            result = num1+num2
            print (num1, " + ", num2, " = ", result)
        case '2':
            result = num1-num2
            print (num1, " - ", num2, " = ", result)
        case '3':
            result = num1*num2
            print (num1, " * ", num2, " = ", result)
        case '4':
            result = num1/num2
            print (num1, " / ", num2, " = ", result)