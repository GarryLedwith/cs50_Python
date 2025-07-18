def area(length, width): 
    print(f"{str(length * width)} square feet")  # Calculate and print the area 
    return length * width  # Return the area value
    
def main(): # Main function to prompt user for input
    length = float(input("Enter the length: "))  # Prompt user for length
    width = float(input("Enter the width: "))  # Prompt user for width
    area(length, width)  # Call area function with user inputs
    
main()  # Execute main function