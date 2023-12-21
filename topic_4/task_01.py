import operator


OPER_MAP = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}


def calculator():
    s = input("Знак (+,-,*,/): ")
    if s not in OPER_MAP:
        raise ValueError()
    x = float(input("x="))
    y = float(input("y="))
    if s == '/' and y < 0:
        raise ZeroDivisionError
    operation = OPER_MAP[s]
    print(operation(x, y))


while True:
    try:
        calculator()
    except ValueError:
        print("Такої арифметичної операції немає,спробуйте ще раз")
    except ZeroDivisionError:
        print("Ділити на нуль не можна, спробуйте спочатку")
