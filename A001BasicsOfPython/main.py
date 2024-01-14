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

