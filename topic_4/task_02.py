def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("Помилка: ділення на нуль")
    return a / b

while True:
    print("Оберіть операцію:")
    print("1. Додавання")
    print("2. Віднімання")
    print("3. Множення")
    print("4. Ділення")
    print("5. Вихід")

    operation = input("Введіть номер операції (1/2/3/4/5): ")

    if operation == '5':
        print("Сессія завершена")
        break

    if operation not in ('1', '2', '3', '4'):
        print("Некоректний вибір операції")
        continue

    try:
        number1 = float(input("Введіть перше число: "))
        number2 = float(input("Введіть друге число: "))

        if operation == '1':
            result = addition(number1, number2)
        elif operation == '2':
            result = subtraction(number1, number2)
        elif operation == '3':
            result = multiplication(number1, number2)
        elif operation == '4':
            try:
                result = division(number1, number2)
            except ValueError as e:
                print(f"Помилка: {e}")
                continue

        print("Результат:", result)
    except ValueError:
        print("Некоректне введення чисел")
