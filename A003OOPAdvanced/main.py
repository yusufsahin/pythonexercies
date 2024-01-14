#Abstract Classes and Methods
from abc import ABC, abstractmethod

class AbstractShape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(AbstractShape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
square = Square(5)
print(square.area())

#Multiple Inheritance

class A:
    def method(self):
        print("A method")

class B(A):
    def method(self):
        print("B method")

class C(A):
    def method(self):
        print("C method")

class D(B, C):
    pass

d = D()
d.method()  # Output depends on the method resolution order

#Method Overloading
class Math:
    def add(self, *args):
        return sum(args)

math = Math()
print(math.add(10, 20))        # Two arguments
print(math.add(10, 20, 30))    # Three arguments

#Class Methods and Static Methods
class MyClass:
    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        print("Called static_method.")

MyClass.class_method()
MyClass.static_method()

#Property Decorators
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

person = Person("Alice")
print(person.name)  # Access like an attribute
person.name = "Bob" # Set like an attribute

#Mixins
class JsonMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

class MyClass(JsonMixin):
    def __init__(self, name):
        self.name = name

obj = MyClass("Test")
print(obj.to_json())  # Outputs a JSON string of the object

#Duck Typing
class Duck:
    def quack(self):
        print("Quack, quack!")

class Person:
    def quack(self):
        print("I'm Quacking Like a Duck!")

def in_the_forest(obj):
    obj.quack()

duck = Duck()
person = Person()
in_the_forest(duck)   # Quack, quack!
in_the_forest(person) # I'm Quacking Like a Duck!

#Operator Overloading
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

v1 = Vector(2,2)
v2 = Vector(1, 3)
v3 = v1 + v2
print(f"Vector Addition: ({v3.x}, {v3.y})")

#Magic Methods
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __len__(self):
        return len(self.title)

book = Book("Python 101", "John Doe")
print(book)  # Output: 'Python 101' by John Doe
print(len(book))  # Output: Length of the title

#Descriptors
class Descriptor:
    def __init__(self, initial_value=None):
        self.value = initial_value

    def __get__(self, obj, objtype):
        return self.value

    def __set__(self, obj, value):
        self.value = value

class MyClass:
    attribute = Descriptor()

my_instance = MyClass()
my_instance.attribute = 10
print(my_instance.attribute)  # Output: 10
