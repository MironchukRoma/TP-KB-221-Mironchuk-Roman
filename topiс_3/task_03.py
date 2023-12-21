# 3) Написати програму тестування функцій словників

# update()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.update({"color": "White"})
print(car)

# del
class MyClass:
  name = "John"
del MyClass
print(MyClass)

# clear
fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear()

# keys()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.keys()
print(x)

# values()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.values()
print(x)

# items()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.items()
print(x)