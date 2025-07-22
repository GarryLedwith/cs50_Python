x = int(input("Enter an integer: ")) # Input an integer
y = int(input("Enter another integer: ")) # Input another integer

if x < y: 
    print(f"{x} is less than {y}")
elif x > y:
    print(f"{x} is greater than {y}")
else:
    print(f"{x} is equal to {y}")


def is_even(n): 
    return True if n % 2 == 0 else False # pythonic way to check if a number is even
    