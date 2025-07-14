import sys # Import the sys module

name = input("What's your name? ")  # prompt for user input

objects = ["Welcome", "to", "Python"]  # Define objects to print
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)  # print objects with specified parameters

# remove whitespace from the beginning and end of a string and capitalize the first letter of each word
name = name.strip().title()  # method chaining 

# split method splits a string into a list where each word is a list item
first, last = name.split(" ")  # split the name into words
print
# f-strings (formatted string literals) are used to embed expressions inside string literals, using curly braces `{}`.
print(f"Hello, {name}!")  # greet the user with their name
print(f"Hello, {first}")  # greet the user with their first and last name
print(f"Hello, {last}")  # greet the user with their last name

#########################
# type conversions 

# convert a string to an integer
age = input("How old are you? ")  # prompt for user input
age = int(age)  # convert the string to an integer

print(f"You are {age} years old.")  # print the age
print(f"You are {age + 1} years old next year.")  # print the age next year


# floating point numbers
height = input("How tall are you in meters? ")  # prompt for user input
height = round(float(height), 2)  # convert the string to a float and round to 2 decimal places
print(f"You are {height} meters tall.")  # print the height

# functions 
def greet(name):
    print(f"Hello, {name}!") # greet the user with their name
    
greet(name)  # call the function with the name variable