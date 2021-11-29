## Kate Pollock
## November 28, 2021
## Foundations of Programming: Python
## Password Creation – Assignment07  

### Introduction
In Module 7, we learned about exception handling and pickling, both through review of the module and our own web research. Unlike other modules we made our own scripts to demonstrate understanding of these concepts. I chose to create a script in which a user enters or changes a password, demonstrating both of these concepts.

### Research
I found the following websites to be helpful regarding exception handling:

[W3 Schools Exception Handling](https://www.w3schools.in/python-tutorial/exception-handling/)

[Programiz Exception Handling](https://www.programiz.com/python-programming/exception-handling)

•	W3 Schools provided a good overview of exceptions in Python including types of statements, why and when they are used as well as examples of different exceptions.

•	Programwhiz provided a good overview as well as videos describing built in exceptions, how to handle exceptions and user defined/custom exceptions.

I found the following website to be helpful regarding pickling:

[Real Python Pickle Module](https://realpython.com/python-pickle-module/)

•	I felt that the above site had a good explanation of the serialization process. It also provided a description of the different modules for serialization in Python. 
### Planning my “Password Creation ” Script 
In planning my password creation script, I tried to utilize mostly functions in my code as many of the tasks were repetitive. Additionally, I created two custom exceptions to check the validity of the password entered and whether the passwords match when creating a new password. It was necessary to import pickle as I would be saving the passwords in a binary format (Figure 1).
``` 
# ---------------------------------------------------------------------------- #
# Title: Assignment 07 - Password Generator
# Description: Working with exceptions and pickling on a password
#              program, when program starts, import pickle,
#              create functions to read and save to file,
#              check password validity, then call functions,
#              use exceptions when no file to read and password
#              valid or doesn't agree.
# ChangeLog (Who,When,What):
# KPollock, 11.28.2021
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables, exception classes

import pickle


class PasswordDoesNotMeetCriteriaException(Exception):
    pass


class PasswordMismatch(Exception):
    pass


strFileName = 'PassData.dat'
```

_Figure 1: Script Heading, Declare Classes and Variable_


### Main Body of Password Script
The following are some of the main features of my script (See Figure 2):

•	Function enforce_password_validity checks for each requirement or rule for password generation. If any of the criteria are not meant, the custom exception PasswordDoesNotMeetCriteria is raised.

•	Function save_data_to_file saves the password in binary format to the file. I used write in order to write over the previous password with the new one. 

•	Function read_data_from_file loads the password back into memory.

•	Function main is the function that will be called in the output section of the script. It uses a try-except block to catch FileNotFound error which indicates a new user. In this case, the function set password is called. It additionally offers the user a choice of menu options.

•	Functions set_password, change_password and authenticate are utilized for menu options 2 and 3). The custom exceptions are raised when a user does not enter a password that meets the criterion or they do not replicate their initial password entry in the case of setting a new password or changing a password (PasswordMismatch).
```
# Processing  --------------------------------------------------------------- #
# Rules for password generation
# Password must be 8 characters or more
# Password must contain both letters (upper and lower)
# numbers and special characters, 1 of each


def enforce_password_validity(password):
    """ Check that password agrees with "rules"
    :param password: (string) user password
    """
    count_upper = 0
    count_lower = 0
    count_digit = 0
    count_special = 0
    for ch in password:
        if ch.isupper():
            count_upper += 1
        elif ch.islower():
            count_lower += 1
        elif ch.isdigit():
            count_digit += 1
        else:
            count_special += 1

    if not (count_upper > 0 and count_lower > 0 and count_digit > 0 and count_special > 0 and len(password) >= 8):
        raise PasswordDoesNotMeetCriteriaException


def save_data_to_file(file_name, password):
    """ Saves password to file using pickle
    :param file_name: (string) with name of file
    :param password: (string) user password
    """
    file = open(file_name, "wb")
    pickle.dump(password, file)
    file.close()


def read_data_from_file(file_name):
    """ Reads data from a file into a variable (string)
    :param file_name: (string) with name of file
    :return: password: (string) user password
    """
    file = open(file_name, "rb")
    password = pickle.load(file)
    file.close()
    return password


def print_menu_choices():
    """  Display a menu of choices to the user
    :return: choice: (string) user choice
    """
    print("""
    Please select from menu options:
    1) Authenticate user 
    2) Change password
    3) Exit
    
    """)
    choice = input('Enter menu choice: ')
    return choice


def main():
    """ calls menu choice and proceeds based on choice
    """
    try:
        read_data_from_file(strFileName)
    except FileNotFoundError:
        print('Welcome new user. No password is on file. Please enter your initial password.')
        set_password()

    while True:

        strMenuChoice = print_menu_choices()

        if strMenuChoice == '1':
            authenticate()
        elif strMenuChoice == '2':
            change_password()
        elif strMenuChoice == '3':
            print('Goodbye!')
            break
        else:
            print('Please enter [1 to 3]')


def change_password():
    """ calls authenticate and if True, calls set_password
    """
    if authenticate():
        set_password()

def set_password():
    """ user inputs password and functions password_validity
    is checked and password is reentered to see if it matches.
    If not, mismatch exception is passed.
    """
    while True:
        try:
            password = input('Enter new password: ')
            enforce_password_validity(password)
            if password != input('Re-Enter new password: '):
                raise PasswordMismatch
            print('New password accepted')
            save_data_to_file(strFileName, password)
            return
        except PasswordDoesNotMeetCriteriaException:
            print('Password does not meet requirements.')
        except PasswordMismatch:
            print('Passwords did not match.')

def authenticate():
    """  Checks if password in file and
    if it is the same, if not passes PasswordMismatch
    :return: true or false (bool)
    """
    try:
        password_exist = input('Please enter your current password: ')
        if password_exist != read_data_from_file(strFileName):
            raise PasswordMismatch
        print('Password accepted')
        return True
    except PasswordMismatch:
        print('Passwords did not match.')
        return False

#Presentation I/O code
main()
```

_Figure 2: Processing and Output code_
### Results of Script

I ran the code in the command prompt and the results were as expected (Figure 3). 

![These are the results](https://github.com/katepollock/IntroToProg-Python-Mod07/blob/main/docs/password_command_output.jpg)

 

_Figure 3: Output in Command Prompt_

### Summary
I have written the Python program above by utilizing the new concepts learned in Module 7 of this course. These concepts include opening and writing data from and to a file in binary format (pickling) and using try-except error handling. I’m looking forward to learning about classes next week. 

