import csv
from sys import argv

class StudentManagementSystem:
    def init(self, filename):
        self.filename = filename
        self.students_list = self.loadFromCSV()

    def loadFromCSV(self):
        students_list = []
        with open(self.filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                students_list.append(row)
        return students_list

    def saveToCSV(self):
        with open(self.filename, mode='w', newline='') as file:
            fieldnames = ["name", "phone", "age", "city"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.students_list)
        print("Data saved successfully to CSV.")

    def printAllList(self):
        for elem in self.students_list:
            strForPrint = (
                "Student name is " + elem["name"] + ", Phone is " + elem["phone"] + ", age is " + elem["age"] + ", city is " + elem["city"]
            )
            print(strForPrint)

    def addNewElement(self):
        name = input("Please enter student name: ")
        phone = input("Please enter student phone: ")
        age = input("Please enter student age: ")
        city = input("Please enter student city: ")

        newItem = {"name": name, "phone": phone, "age": age, "city": city}
        insertPosition = 0
        for item in self.students_list:
            if name > item["name"]:
                insertPosition += 1
            else:
                break
        self.students_list.insert(insertPosition, newItem)
        print("New element has been added")

    def deleteElement(self):
        name = input("Please enter name to be deleted: ")
        deletePosition = -1
        for item in self.students_list:
            if name == item["name"]:
                deletePosition = self.students_list.index(item)
                break
        if deletePosition == -1:
            print("Element was not found")
        else:
            print("Delete position " + str(deletePosition))
            del self.students_list[deletePosition]

    def updateElement(self):
        name = input("Please enter name to be updated: ")
        userPosition = -1

        for i, item in enumerate(self.students_list):
            if name == item["name"]:
                userPosition = i
                break

        if userPosition == -1:
            print("Student not found")
        else:
            print(f"Student found: {self.students_list[userPosition]}")
            updated_fields = {
                "name": input("Enter the new name: "),
                "phone": input("Enter the new phone: "),
                "age": input("Enter the new age: "),
                "city": input("Enter the new city: "),
            }
            del self.students_list[userPosition]
            insertPosition = 0
            for i, elem in enumerate(self.students_list):
                if updated_fields["name"] > elem["name"]:
                    insertPosition += 1
                else:
                    break

            self.students_list.insert(insertPosition, updated_fields)
            print("Student information updated")

def main(self):
        while True:
            choice = input("Please specify the action [C create, U update, D delete, P print, S save, X exit]: ")
            if choice.upper() == "C":
                print("New element will be created:")
                self.addNewElement()
                self.printAllList()
            elif choice.upper() == "U":
                print("Existing element will be updated")
                self.updateElement()
            elif choice.upper() == "D":
                print("Element will be deleted")
                self.deleteElement()
            elif choice.upper() == "P":
                print("List will be printed")
                self.printAllList()
            elif choice.upper() == "S":
                self.saveToCSV()
            elif choice.upper() == "X":
                print("Exit()")
                break
            else:
                print("Wrong choice")

if __name__ == '__main__':
    filename = argv[1]
    student_system = StudentManagementSystem(filename)
    student_system.main()