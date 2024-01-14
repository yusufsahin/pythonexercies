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

#Comphersive Example

# List of books in the library (Each book is a dictionary)
books = [
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"title": "1984", "author": "George Orwell", "year": 1949}
]

# Tuple representing a new book to be added
new_book = ("Moby-Dick", "Herman Melville", 1851)

# Adding the new book to the books list
books.append({"title": new_book[0], "author": new_book[1], "year": new_book[2]})

# Dictionary to store the count of books by each author
author_count = {}

# Set to store unique publication years
publication_years = set()

# Processing the books
for book in books:
    # Counting books by each author
    author = book["author"]
    if author in author_count:
        author_count[author] += 1
    else:
        author_count[author] = 1

    # Adding the publication year to the set
    publication_years.add(book["year"])

# Displaying the library information
print("Books in the Library:")
for book in books:
    print(f"- {book['title']} by {book['author']} ({book['year']})")

print("\nNumber of Books by Author:")
for author, count in author_count.items():
    print(f"- {author}: {count} book(s)")

print("\nUnique Publication Years:")
for year in sorted(publication_years):
    print(f"- {year}")

