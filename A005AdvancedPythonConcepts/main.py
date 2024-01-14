#List Comprehensions

squares = [x**2 for x in range(10)]
print(squares)

#Lambda Functions
multiply = lambda x, y: x * y
print(multiply(2,3))

#Map filter Reduce

from functools import reduce

numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, numbers)
even = filter(lambda x: x % 2 == 0, numbers)
sum_all = reduce(lambda x, y: x + y, numbers)
print(sum_all)

#Decorators

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

#Generators

def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

counter = count_up_to(5)
for num in counter:
    print(num)

#Context Managers

with open('example.txt', 'w') as file:
    file.write('Hello, world!')

#Regular Expressions

import re
pattern = re.compile(r'\d{3}-\d{2}-\d{4}')
result = pattern.search('My number is 123-45-6789.')
print(result.group())  # Output: 123-45-6789

#Comprehensions for Other Data Types
square_set = {x**2 for x in range(10)}  # Set comprehension
count_map = {x: str(x) for x in range(5)}  # Dictionary comprehension

print(count_map)

#Iterators and Iterables
class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

for x in Counter(3, 8):
    print(x)

#Advanced Functional Programming

from functools import partial

def multiply(x, y):
    return x * y

double = partial(multiply, 2)
print(double(5))  # Output: 10
