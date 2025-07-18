# Prompt the user for mass as an integer
mass = int(input("Enter mass in kilograms: "))  # Prompt user for mass input
# Calculate energy using the formula E = mc^2
energy = mass * (300000000 ** 2)  # Calculate energy in joules
# Print the calculated energy
print(f"Energy: {energy} joules")  # Output the energy value
# Summary:
# This code prompts the user to input a mass in kilograms, calculates the energy equivalent using Einstein's equation E=mc^2, and prints the result in joules.
# It demonstrates basic arithmetic operations and user input handling in Python.
# Note: The speed of light (c) is approximated as 300,000,000 meters per second for simplicity.
# In a more precise implementation, you might want to use a constant for the speed of light, such as from the `scipy.constants` module.
# This code is a simple demonstration of how to apply a fundamental physics equation in a programming context.50