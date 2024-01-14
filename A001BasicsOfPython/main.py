#Variables and Data Types
age=30
height=5.9
name="Alice"
is_student=True
print(age,height,name,is_student)
print("--------------------------")
#Operators
# Arithmetic Operators
a=10
b=3
print("Addition:",a+b)
print("Subtraction:",a-b)
print("Multiplication:",a*b)
print("Division:",a/b)

print("Equal:",a==b)
print("Not Equal:",a!=b)

print("AND:",a>5 and b<5)
print("OR:",a>5 or b>5)
print("--------------------------")

#Basic String Operations
str1="Hello"
str2="World"
concatenated=str1+" "+str2
print("Concatenated String:",concatenated)
print("Lenght of String:",len(concatenated))
print("First Character:",concatenated[0])

#String Formatting
name="Alice"
age="25"
formatted_string=f"My name is {name} is and I am {age} years old."
print("Using f-string:",formatted_string)

#Slicing and Substrings
text="Python Programming"
slice1=text[0:6]
slice2=text[:]
print("Slice 1:",slice1)
print("Slice 2:",slice2)

example="hello world"
print("Upper Case:",example.upper())
print("Lower Case:",example.lower())
print("Title Case:",example.title())
print("Swap Case:",example.swapcase())


#Stripping Whitespace
spaced_string = "  Hello, World!  "
print("Stripped:",spaced_string.strip())
print("LStrip:",spaced_string.lstrip())
print("RStrip:",spaced_string.rstrip())

#Searching and Replacing
sentence = "The quick brown fox jumps over the lazy dog"
print("Find 'fox':",sentence.find("fox"))
print("Replace 'dog' with 'cat':",sentence.replace("dog","cat"))
print("'quick' in sentence:","quick" in sentence)

#Splitting and Joining
data = "apple,banana,cherry"
words = data.split(",")  # Split into a list
print("Split List:", words)
joined = " - ".join(words)  # Join list into a string
print("Joined String:", joined)

#String Testing Methods
num_str = "12345"
alpha_str = "abcde"
print("Is digit:", num_str.isdigit())
print("Is alpha:", alpha_str.isalpha())
print("Is alphanumeric:", alpha_str.isalnum())
#Iterating Over Strings
for char in "Hello":
    print(char)
#Advanced String Techniques

import re

pattern = r"\d+"
text = "There are 123 apples and 45 bananas."
matches = re.findall(pattern, text)
print("Numbers in text:", matches)

#more assigment operators
x = 10  # Assigns 10 to x

#Addition Assignment Operator (+=)
x = 5
x += 3  # Equivalent to x = x + 3
print("After += 3:", x)  # x is now 8
#Subtraction Assignment Operator (-=)
x = 10
x -= 4  # Equivalent to x = x - 4
print("After -= 4:", x)  # x is now 6
#Multiplication Assignment Operator (*=)
x = 6
x *= 3  # Equivalent to x = x * 3
print("After *= 3:", x)  # x is now 18

#Division Assignment Operator (/=)
x = 20
x /= 4  # Equivalent to x = x / 4
print("After /= 4:", x)  # x is now 5.0

#Modulus Assignment Operator (%=)
x = 10
x %= 3  # Equivalent to x = x % 3
print("After %= 3:", x)  # x is now 1
#Exponentiation Assignment Operator (**=)
x = 5
x **= 2  # Equivalent to x = x ** 2
print("After **= 2:", x)  # x is now 25

#Floor Division Assignment Operator (//=)
x = 15
x //= 4  # Equivalent to x = x // 4
print("After //= 4:", x)  # x is now 3
#Bitwise OR Assignment Operator (|=)
x = 4  # Binary: 100
x |= 3  # Binary: 011
print("After |= 3:", x)  # x is now 7 (Binary: 111)
# Bitwise XOR Assignment Operator (^=)
x = 5  # Binary: 101
x ^= 3  # Binary: 011
print("After ^= 3:", x)  # x is now 6 (Binary: 110)

#Bitwise Left Shift Assignment Operator (<<=)
x = 2  # Binary: 10
x <<= 2  # Shift left by 2 bits
print("After <<= 2:", x)  # x is now 8 (Binary: 1000)

#Bitwise Right Shift Assignment Operator (>>=)
x = 8  # Binary: 1000
x >>= 2  # Shift right by 2 bits
print("After >>= 2:", x)  # x is now 2 (Binary: 10)


#Control Structures

number = 5
#if-else
if number > 0:
    print("Positive number")
else:
    print("Negative number")
#for loop
for i in range(5):
    print(i)
#while loop
count=0
while count < 5:
    print(count)
    count += 1

#Functions and Modules

# Defining a function
def greet(name):
    return f"Hello {name}!"

# Using the function
print(greet("Alice"))

#Exception Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")

#File Handling

def write_to_file(filename, data):
    try:
        with open(filename, "w") as file:
            file.write(data)
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")
    else:
        print(f"Data successfully written to {filename}")

def read_from_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except IOError as e:
        print(f"An error occurred while reading the file: {e}")
        return None

def main():
    filename = "example.txt"
    user_input = input("Enter some text to write to the file: ")
    write_to_file(filename, user_input)

    print("\nReading from the file...")
    content = read_from_file(filename)
    if content is not None:
        print("Content of the file:")
        print(content)

if __name__ == "__main__":
    main()



