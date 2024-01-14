#Classes and Objects
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # Grade from 0 to 100

    def get_grade(self):
        return self.grade

    def display_student(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

# Example usage
student1 = Student("Alice", 20, 85)
print(student1.display_student())


#Inheritance

class Animal:
    def __init__(self,name):
        self.name = name
    def speak(self):
        raise  NotImplementedError("Subclass must implement abstract method")
class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.name = name
        self.age = age
    def speak(self):
        return "Woof!"

my_dog = Dog("Buddy" ,3)
print(my_dog.name)
print(my_dog.speak())
class Cat(Animal):
    def speak(self):
        return "Meow"

my_cat = Cat("Whiskers")
print(my_cat.speak())

for animal in [Dog("Buddy",3), Cat("Whiskers")]:
    print(animal.speak())

#Encapsulation
class BankAccount:
    def __init__(self, account_number, name, balance):
        self.__account_number = account_number  # Private attribute
        self.__name = name                      # Private attribute
        self.__balance = balance                # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposit successful. New balance: {self.__balance}"
        else:
            return "Invalid deposit amount"

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrawal successful. New balance: {self.__balance}"
        else:
            return "Invalid withdrawal amount or insufficient funds"

    def get_account_details(self):
        return f"Account Number: {self.__account_number}, Name: {self.__name}, Balance: {self.__balance}"

# Example usage
account = BankAccount("123456789", "Alice", 1000)
print(account.deposit(500))  # Deposit money
print(account.withdraw(200)) # Withdraw money
print(account.get_account_details())  # Display account details


#Polymorphism
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Polymorphism in action
shapes = [Circle(5), Rectangle(10, 5)]

for shape in shapes:
    print(shape.area())
