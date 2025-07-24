"""
   Suppose that you’re in a country where it’s customary to eat breakfast between 7:00 and 8:00, 
   lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00. 
   Wouldn’t it be nice if you had a program that could tell you what to eat when?

In meal.py, implement a program that prompts the user for a time and outputs 
whether it’s breakfast time, lunch time, or dinner time. If it’s not time for a meal, don’t output anything at all. 
Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##. And assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.

Structure your program per the below, wherein convert is a function (that can be called by main) that converts time, 
a str in 24-hour format, to the corresponding number of hours as a float. 
For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).


PEDAC: 
P: Problem
Requirements: 
- eat breakfast between 7:00 and 8:00, 
   lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00. 
- Prompt the user for a time in 24-hour format
- Output the meal type based on the time
- If the time does not fall within any meal time, do not output anything
- Use a function to convert time from string to float

Clarifying Questions:
1. What format should the time be in?
   - The time should be in 24-hour format as #:## or ##:##.
2. What should the program do if the time does not match any meal time?
   - The program should not output anything if the time does not match any meal time.   
   
3. How should the program handle edge cases like 7:00 or 8:00?
   - The program should include these times as valid for breakfast, lunch, and dinner.
   
   
E: Examples
Input: "7:30"
Output: "breakfast"

Input: "12:00"
Output: "lunch"

D: Data Structures
- String to represent the time input
- Float to represent the converted time in hours    

A: Algorithm
1. Define a function `convert` that takes a string time in 24-hour format and
   converts it to a float representing hours.
2. Prompt the user for a time input.
3. Call the `convert` function to convert the input time to float.
4. Check the converted time against the meal times:
   - If the time is between 7.0 and 8.0 (inclusive), output "breakfast".
   - If the time is between 12.0 and 13.0 (inclusive), output "lunch".
   - If the time is between 18.0 and 19.0 (inclusive), output "dinner".
5. If the time does not match any meal time, do not output anything.    
    """
    
def convert(time_str): 
    hours, minutes = time_str.split(':')  # Split the input string into hours and minutes
    hours = int(hours)  # Convert hours to integer
    minutes = int(minutes)  # Convert minutes to integer
    return hours + minutes / 60.0  # Convert to float representing hours

def main():
    time_input = input("Enter the time in 24-hour format (e.g., 7:30): ").strip() # Prompt user for time input
    time_float = convert(time_input) # Convert the input time to float
    
    if 7.0 <= time_float <= 8.0: # Check if it's breakfast time
        print("breakfast")
    elif 12.0 <= time_float <= 13.0: # Check if it's lunch time
        print("lunch")
    elif 18.0 <= time_float <= 19.0: # Check if it's dinner time
        print("dinner")
    # If the time does not match any meal time, do not output anything
    
if __name__ == "__main__":
    main()  # Call the main function to run the program
    
