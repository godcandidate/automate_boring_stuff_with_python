#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses from a text file and saves the results in another file.

import re
import filepaths as path


# Compile the regex patterns
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?  # area code
    (\s|-|\.)?          # separator
    (\d{3})             # first 3 digits
    (\s|-|\.)           # separator
    (\d{4})             # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
)''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+    # username
    @                     # @ symbol
    [a-zA-Z0-9.-]+       # domain name
    (\.[a-zA-Z]{2,4})    # dot-something
)''', re.VERBOSE)

base_dir = 'automate_boring_stuff_with_python/'
# Function to find matches in a text file and write them to an output file
def find_phone_and_email(input_file, output_file):
    # Read text from the input file
    with open(input_file, 'r') as file:
        text = file.read()

    matches = []

    # Find phone numbers
    for groups in phoneRegex.findall(text):
        phoneNum = '-'.join([groups[1], groups[3], groups[5]])
        if groups[8]:  # Check if extension exists
            phoneNum += ' x' + groups[8]
        matches.append(phoneNum)

    # Find email addresses
    for groups in emailRegex.findall(text):
        matches.append(groups[0])

    # Write results to the output file
    with open(output_file, 'w') as file:
        for match in matches:
            file.write(match + '\n')

    print("")

# Example usage
'/home/edward/Desktop/devops_python/automate_boring_stuff_with_python/projects/mail_number_extractor/random.txt'
input_file_path = path.file1
output_file_path = path.file2
find_phone_and_email(input_file_path, output_file_path)

print(f"Phone numbers and email addresses have been extracted to sucessfully.")
