import re


def extract_standard_phone_number(text):
    """
    Extracts a standard phone number (in the format XXX-XXX-XXXX) from the given text.
    
    Parameters:
        text (str): The text containing the phone number.
    
    Returns:
        tuple: A tuple containing the area code and the main number.
               Returns None if no phone number is found.
    
    Example:
        >>> extract_standard_phone_number("My number is 415-555-4242")
        ('415', '555-4242')
    """
    phone_num_regex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
    match_obj = phone_num_regex.search(text)
    
    if match_obj:
        area_code, main_number = match_obj.groups()
        print("Standard Phone Number Found:")
        print("Area code:", area_code)
        print("Main number:", main_number)
        return area_code, main_number
    else:
        print("No standard phone number found.")
        return None

def extract_parenthesized_phone_number(text):
    """
    Extracts a phone number with a parenthesized area code (format (XXX)-XXX-XXXX) from the given text.
    
    Parameters:
        text (str): The text containing the phone number.
    
    Returns:
        tuple: A tuple containing the area code and the main number.
               Returns None if no phone number is found.
    
    Example:
        >>> extract_parenthesized_phone_number("My number is (415)-555-4242")
        ('(415)', '555-4242')
    """
    phone_num_regex = re.compile(r'(\(\d{3}\))-(\d{3}-\d{4})')
    match_obj = phone_num_regex.search(text)
    
    if match_obj:
        area_code, main_number = match_obj.groups()
        print("Parenthesized Phone Number Found:")
        print("Area code:", area_code)
        print("Main number:", main_number)
        return area_code, main_number
    else:
        print("No parenthesized phone number found.")
        return None

# Test the functions with example phone numbers
text1 = "My number is 415-555-4242"
text2 = "My number is (415)-555-4242"

# Extract standard phone number
extract_standard_phone_number(text1)

# Extract parenthesized phone number
extract_parenthesized_phone_number(text2)
