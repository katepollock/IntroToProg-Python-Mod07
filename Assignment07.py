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

