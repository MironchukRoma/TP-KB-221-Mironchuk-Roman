list = [
    {"name":"Oliver", "phone":"0635555555", "age": "20", "city" : "Chernihiv"},
    {"name":"Jack", "phone":"0633333333", "age": "23", "city" : "Chernihiv"},
    {"name":"Harry",  "phone":"0634444444", "age": "24", "city" : "Chernihiv"},
    {"name":"Jacob",  "phone":"0636666666", "age": "18", "city" : "Chernihiv"}
]

def printAllList():
    for elem in list:
        strForPrint = "Student name is " + elem["name"] + ",  Phone is " + elem["phone"] + ", age is " + elem["age"] + ", city is " + elem["city"]
        print(strForPrint)
    return

def addNewElement():
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    age = input("Please enter student age: ")
    city = input("Please enter student city: ")

    newItem = {"name": name, "phone": phone, "age" : age, "city" : city}
    # find insert position
    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return
    
def deleteElement():
    name = input("Please enter name to be delated: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Dele position " + str(deletePosition))
        # list.pop(deletePosition)
        del list[deletePosition]
    return

def updateElement():
    name_to_update = input("Enter student name to update: ")
    for student in list:
        if student["name"] == name_to_update:
            new_phone = input("Enter new phone number: ")
            student["phone"] = new_phone
            age = input("Enter new age: ")
            student["age"] = age
            city = input("Enter new city: ")
            student["city"] = city
            print("Student updated successfully!")
            return
    print("Student not found.")

def main():
    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
                updateElement()
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                print("Exit()")
                break
            case _:
                print("Wrong chouse")
main()