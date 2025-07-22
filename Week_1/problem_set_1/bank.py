# Steps:
# 1. prompt the user for a greeting
# 2. if greeting starts with "hello" output $0
# 3. if greeting starts with "h" output $20
# 4. otherwise output $100 (ignore any leading whitespace) (treat user's greeting as case-insensitive)

# Strip leading/trailing whitespace and convert to lowercase
greeting = input("Enter your greeting: ").strip().lower()

match greeting:
    case g if g.startswith("hello"):
        print("$0")
    case g if g.startswith("h"):
        print("$20")
    case _:
        print("$100")  # Default case for any other greeting
