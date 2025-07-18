# implement a function called convert that accepts a string 
# and returns the same inputwith any :) converted to a smiley face emoji
# and convert any :( to a sad face emoji
# then implement a main function that prompts the user for input and calls convert 
# and prints the result


def convert(text):
    slightly_smiley_face =  "🙂"
    slightly_frowning_face = "🙁"
    
    if ":)" in text:
        text = text.replace(":)", slightly_smiley_face)
    if ":(" in text:
        text = text.replace(":(", slightly_frowning_face)
    return text

def main():
    user_input = input("Enter some text: ")  # Prompt user for input
    result = convert(user_input)  # Call convert function with user input
    print(result)  # Print the converted text
    
main()  # Execute main function
# Summary:
# The `convert` function replaces ":)" with a smiley face emoji and ":(" with a sad face emoji in the input text.
# The `main` function prompts the user for input, calls the `convert` function with that input, and prints the result.
# This program demonstrates basic string manipulation and user input handling in Python.

    
    
    
    
    
