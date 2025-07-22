""" PEDAC:

P: Problem 
implement a program that prompts the user for the name of a file and 
then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:

.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip


Input: A file name (string)
Output: The media type of the file based on its suffix

Clarifying Questions:
1. What should the program do if the file name does not match any of the specified suffixes?
   - The program should output "application/octet-stream" for any file name that does not
   
2. How will I store the media types?
   - I will use a dictionary to map file suffixes to their corresponding media types.
   

E: Examples
input: "image.jpg"
output: "image/jpeg"

input: "document.pdf"
output: "application/pdf"

input: "archive.zip"
output: "application/zip"



D: Data Structures
Dictionary to map file suffixes to media types


A: Algorithm
- Create a dictionary to map file suffixes to media types
- Prompt the user for a file name
- Extract the file suffix from the file name
- Convert the suffix to lowercase
- Check if the suffix exists in the dictionary
- If it exists, print the corresponding media type
- If it does not exist, print "application/octet-stream"
- Handle any exceptions that may arise from invalid input or file names
- Ensure the program is case-insensitive when checking suffixes
- Use a match statement to handle different cases for suffixes



C: Code
    """


# Dictionary to map file suffixes to media types

media_types = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip"
}

# Prompt the user for a file name
# Remove leading/trailing whitespace
file_name = input("Enter the file name: ").strip()

# Extract the file suffix
# Get the last part after the last dot, or an empty string if no dot is present
suffix = file_name.lower().split('.')[-1] if '.' in file_name else ''

# Check if the suffix exists in the dictionary
if suffix in media_types:
    # Print the corresponding media type (value from the dictionary)
    print(media_types[suffix])
else:
    # Default case for any other file suffix not in the dictionary
    print("application/octet-stream")
