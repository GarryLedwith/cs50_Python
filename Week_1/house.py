name = input("Enter your name: ")  # Input a name

if name == "Alice" or name == "Bob" or name == "Charlie":
    print(f"Hello, {name}!")
elif name == "David":
    print(f"Hello, {name}!")
else:
    print("Hello, stranger!")
    
    
# match statement example (aka switch-case)
match name: 
    case "Alice":
        print(f"Hello, {name}!")
    case "Bob":
        print(f"Hello, {name}!")
    case "Charlie":
        print(f"Hello, {name}!")
    case "David":
        print(f"Hello, {name}!")
    case _:
        print("Hello, stranger!")  # Default case for any other name 