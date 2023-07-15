import os  # Module needed to check if file exists


def get_input_option() -> str:
    """
    Ask user enter correct input option (file/console).
    If input option is incorrect user should put this one again.
    """
    choises = ['file', 'console']  # Possible choises

    choise = input('Enter input option (file/console): ').lower()  # Try to enter choise

    while choise not in choises:  # If choise is incorrect enter the loop until choise won't be correct
        print('This option is not available, please enter again!')  # Write message what we should do next
        choise = input('Enter input option (file/console): ')  # Enter choise again

    return choise  # Return correct value


def get_file_name():
    """
    Ask user to enter file name or path which exists.
    If file name or path doesn't exist user should put this one again.
    """
    file_name = input('Enter file name or path to file: ')  # Try to enter file name or path
    while not os.path.isfile(file_name):  # If file name or path doesn't exist invoke the loop until we enter file name or path will exists
        print('File like this doesn\'t exists. Try to input again')  # Write message what we should do next
        file_name = input('Enter file name or path to file: ')  # Enter file name or path again
    return file_name  # Return file name or path


def get_number():
    """
    Ask user to enter number.
    If input is incorrect user should enter number again.
    """
    number = ''  # Variable contains this value until user enters a number
    while number == '':  # Loop gets us possibility to put something until this won't a number
        try:
            number = float(input())  # Try to enter a number
        except ValueError:  # Catch error
            print('Incorrect value')  # Print message means that user entered incorrect value
    return number
