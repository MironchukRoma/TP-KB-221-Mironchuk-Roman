
import os

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def save_to_file(file_name, data):
    with open(file_name, 'w', encoding='utf-8') as file:
        for item in data:
            file.write(f"name: {item.name}, age: {item.age}\n")

def main():
    students = [
        Student("Іван", 19),
        Student("Марія", 21),
        Student("Петро", 20),
        Student("Анна", 18)
    ]

    print("Список студентів:")
    for student in students:
        print(f"name: {student.name}, age: {student.age}")

    sort_choice = input("Яке сортування ви виберете за 'name' чи за 'age'? ").lower()

    if sort_choice not in ['name', 'age']:
        print("Неправильний вибір сортування.")
        return

    students = sorted(students, key=lambda x: getattr(x, sort_choice))

    current_directory = os.path.dirname(os.path.abspath(__file__))
    while True:
        file_name = input(f"Введіть назву файлу для збереження у теку {current_directory}: ") + ".txt"
        file_path = os.path.join(current_directory, file_name)

        if os.path.exists(file_path):
            print(f"Файл з іменем {file_name} вже існує. Будь ласка, виберіть інше ім'я файлу.")
        else:
            break

    try:
        save_to_file(file_path, students)
        print(f"Файл {file_name} успішно збережено.")
    except Exception as e:
        print(f"Помилка при збереженні файлу: {e}")

if __name__ == "__main__":
    main()
