# Simple string
my_str_1 = 'My name is mahad'
print(my_str_1)

# Multi line string
multi_line_str = '''Multi
line
string'''
print(multi_line_str)

# Quotation in string
quote_string = "He said: 'Hi! How are you?'"
print(quote_string)

# Checking if a word or character exists in a string
my_str_2 = "Hello World!"
print("Hello" in my_str_2)
print("World" in my_str_2)
print("!" in my_str_2)
print("test" in my_str_2)

# Checking the length of a string
print(len(my_str_2))

# Indexing in a string
print(my_str_2[0])
print(my_str_2[5])
print(my_str_2[11])

# Negative indexing
print(my_str_2[-1])
print(my_str_2[-12])

# Concatenation
str_1 = "Hello"
str_2 = "World!"
print(str_1 + ' ' + str_2)

# Converting int to string
int_1 = 5
int_1_string = str(5)
print("Number of students in class: " + int_1_string)

# Augmented assignment operator
name_and_age = "Mahad"
name_and_age +=str(21)
print(name_and_age)

# String interpolation
name = "Mahad"
age = 21
name_and_age = f"My name is {name} and I am {age} years old"
print(name_and_age)

# String slicing
print(my_str_2[0:5])
print(my_str_2[:5])
print(my_str_2[-6:])
print(my_str_2[::2])
print(my_str_2[::-1])

# String methods

# upper
print(my_str_2.upper())
print(my_str_2[0:5].upper())

# lower
print(my_str_2.lower())

# strip
my_str_3 = " Hello World! "
print(my_str_3.strip())
print(my_str_3[:6].strip())

# replace
print(my_str_3.replace("Hello", "Hi").strip())

# split
print(my_str_3.split())
my_str_4 = "Hello,World!"
print(my_str_4.split(','))

# join
print(" ".join(my_str_3.split()))

# startswith
print(my_str_3.startswith("He"))
print(my_str_2.startswith("He"))

# endswith
print(my_str_3.endswith("!"))
print(my_str_2.endswith("!"))

# find
print(my_str_2.find("W"))
print(my_str_2.find("p"))

# count
print(my_str_2.count("o"))
print(my_str_2.count("l"))

# isupper
print(my_str_2.isupper())

# islower
my_str_5 = "hello world!"
print(my_str_5.islower())

# title
print(my_str_5.title())