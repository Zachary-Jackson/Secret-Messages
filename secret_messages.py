"""
Just a reminder that this is a new and improved menu working with old cipher
classes. The ciphers are liable to be inefficient and unorganized.
"""

from collections import OrderedDict
import datetime
import os
import sys
import time

from ciphers import *


CIPHERS = OrderedDict([
    ('Atbash', Atbash),
    ('Caesar', Caesar),
    ('Keyword', KeywordCipher),
    ('Railfence', RailFence)
])


def clear():
    """Clears the screen for easier reading and use"""
    os.system('cls' if os.name == 'nt' else 'clear')


def decrypt():
    """
    Allows the user to choose a cipher and decrypts a message
    This message is then shown to the user

    """
    cipher = get_cipher()

    message = cipher.get_user_message()
    decrypted_message = cipher.decryption(message)

    print(f'Your decrypted message is: {decrypted_message}')

    input('Enter anything to continue')


def encrypt():
    """
    Allows the user to choose a cipher and encrypts a message
    This message is then shown to the user

    """
    cipher = get_cipher()

    message = cipher.get_user_message()
    encrypted_message = cipher.encryption(message)
    print(f'Your encrypted message is: {encrypted_message}')

    input('Enter anything to continue')


def encrypt_decrypt_or_exit():
    """
    Determines if the user wants to encrypt, or decrypt a cipher
    They can also choose to exit the program

    :return: String saying 'encrypt', 'decrypt', or 'exit'
    """
    while True:
        request = input(
            "Would you like to use a cipher to encrypt or decrypt a message?\n"
            "Enter [E]ncrypt or [D]ecrypt\n\n"
            "Or type 'exit' to end the program\n"
        ).lower()

        # Determine if the user typed in a proper request
        if request in ['e', 'encrypt']:
            return 'encrypt'
        elif request in ['d', 'decrypt']:
            return 'decrypt'
        elif request in ['exit', 'exit()']:
            return 'exit'
        else:
            clear()


def get_cipher():
    """
    Asks the user what cipher they want to use

    :return: A cipher class object
    """
    all_ciphers_list = [cipher for cipher in CIPHERS]
    all_ciphers_string = ', '.join(all_ciphers_list)

    while True:
        cipher = input(
            'Please choose a cipher from the following:\n'
            f' {all_ciphers_string}.\n'
        ).title()

        if cipher in CIPHERS:
            return CIPHERS[cipher]()

        clear()


def get_time_welcome_message():
    """
    Determines the time of the day, and creates a welcome message based on that

    :return: String that welcomes the user
    """
    current_time = datetime.datetime.now()
    hour = current_time.hour

    if 6 < hour < 12:
        return 'May the sun rise and show you the way.'
    elif 12 <= hour < 15:
        return 'Beware of the bright sun, the enemy can your your path!'
    elif 15 <= hour < 18:
        return 'Be careful of the waning light!'
    else:
        return 'Use the darkness to conceal your movements.'


def welcome():
    """
    Welcomes the user to the cipher program
    The program is paused for 2.5 seconds for the user
    """
    clear()
    time_message = get_time_welcome_message()

    # creates the message template
    message = f"""  {time_message}
    
Use the ciphers that follows to your advantage!
    """
    print(message)

    time.sleep(2.5)
    return True


def main_program_loop():
    """
    The main program which answers the user's cipher requests until they
    exit the program
    """
    while True:
        clear()
        user_request = encrypt_decrypt_or_exit()

        # calls the encryption/decryption functions or ends the program

        if user_request == 'exit':
            print('May your adventures go well.')
            sys.exit()
        elif user_request == 'encrypt':
            encrypt()
        elif user_request == 'decrypt':
            decrypt()


if __name__ == "__main__":
    # Makes sure that the script does not run if imported
    welcome()
    main_program_loop()