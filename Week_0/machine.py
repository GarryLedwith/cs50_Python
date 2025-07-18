# Side effects: print is a side effect
emoticon = "v.v"  # Define an emoticon

def main():
    global emoticon  # Use the global emoticon variable
    say("Is anyone there?")  # Call the say function with a phrase
    emoticon = ":D"  # Change the emoticon
    say("Oh, hi!")
    
def say(phrase): # side effect: print to terminal
    print(f"{phrase} {emoticon}")  # Print the phrase with an emoticon
    
    
main()  # Call the main function

# Summary: 
# The global variable `emoticon` is defined at the top and use in the `say` function. 
# Within the `main` function, the `emoticon` is mofified before the second call to `say` because it is declared as `global`.
# The `say` function, prints the phrase that is passed into the function as an argument along with the current emoticon. 
# The program demonstrates the use of global variables and side effects in Python.
# Warning: Using global variables can lead to code that is harder to understand and maintain, 
# so it's generally better to pass variables as parameters when possible.