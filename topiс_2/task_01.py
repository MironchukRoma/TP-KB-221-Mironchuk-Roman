import math

def findD(a, b, c):
    D = b**2 - 4 * a * c
    return D

def findRoots(a, b, c):
    D = findD(a, b, c)
    if D == 0:
        x1 = x2 = -b / (2 * a)
        return x1
    elif D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        return x1, x2
    else:
        return None  # No real roots for D < 0

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

roots = findRoots(a, b, c)
if roots is not None:
    print("Roots:", roots)
else:
    print("No real roots.")

