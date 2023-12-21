# 2) Написати програму тестування функцій списків
# extend()
prime_numbers = [2, 3, 5]
numbers = [1, 4]
numbers.extend(prime_numbers)
print('List after extend():', numbers)


# append()
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)

# insert(id, val)
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)

# remove(val)
val = [2, 3, 5, 7, 9, 11]
val.remove(9)
print('Updated List: ', val)

# clear()
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)

# sort()
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)

# reverse()
prime_numbers = [2, 3, 5, 7]
prime_numbers.reverse()
print('Reversed List:', prime_numbers)

# copy()
prime_numbers = [2, 3, 5]
numbers = prime_numbers.copy()
print('Copied List:', numbers)