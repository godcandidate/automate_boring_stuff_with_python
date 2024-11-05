import pyinputplus as pyip


def display(name, email, age, date_of_birth, salary):
    print(f"Name         : {name}")
    print(f"Email        : {email}")
    print(f"Age          : {age}")
    print(f"Date of Birth: {date_of_birth}")
    print(f"Salary       : GHc{salary}")



fullname = pyip.inputStr('Enter your name: ')
email = pyip.inputEmail('Enter a valid email address: ')
age = pyip.inputInt('Enter your age(18 years and above): ', greaterThan=17)
date_of_birth = pyip.inputStr('Enter your date of birth: ', allowRegexes=[r'^\d{1,2}/\d{1,2}/\d{4}$'])
salary = pyip.inputInt('Enter the amount of salary: ')


display(fullname, email, age, date_of_birth, salary)