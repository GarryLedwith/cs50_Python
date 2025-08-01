"""
implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:

x is an integer
y is +, -, *, or /
z is an integer
For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0.
    """
  
  
x = int(input("Enter a number: "))
y = input("Enter an operator (+, -, *, /): ")
z = int(input("Enter another number: "))

if y == '+':
    result = x + z
elif y == '-':
    result = x - z
elif y == '*':
    result = x * z
elif y == '/':
    result = x / z
else:
    print("Invalid operator")
    result = None
    
if result is not None: 
    print(f"{result:.1f}")  # Output the result formatted to one decimal place
else: 
    print("Calculation could not be performed")