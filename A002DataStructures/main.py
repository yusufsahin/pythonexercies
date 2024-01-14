#List
fruits = ['apple','banana','cheery']
print(fruits[0])

fruits.append("orange")
fruits.remove("banana")

for fruit in fruits:
    print(fruit)

squared_numbers=[x**2 for x in range(10)]
print(squared_numbers)

#Tuple

coordinates = (10,20)
print(coordinates[0])
for coordinate in coordinates:
    print(coordinate)

#Dictionary

person = {"name": "Alice", "age": 30}
print(person["name"])

person["city"] = "New York"

for key, value in person.items():
    print(f"{key}: {value}")

del person["age"]

for key, value in person.items():
    print(f"{key}: {value}")

#Set

numbers = {1, 2, 3, 4}
print(numbers)

numbers.add(5)
numbers.remove(2)
for number in numbers:
    print(number)

a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))