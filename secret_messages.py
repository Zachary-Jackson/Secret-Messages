import os


# This function calls on the proper class for the requested cipher

def clear():
    """This function clears the screen for easier reading and use"""
    os.system('cls' if os.name == 'nt' else 'clear')


def welcome():
    """This function welcomes the user to the program"""
    clear()
    print("""Welcome to the secret messages application!
The encryption and decryption of messages in this application may not
be entirely secure and could be found out by others.
Use the program at your own risk
""")
    main(clear_screen=False)


def cipher_viewer(cipher_list):
    """This function shows the user all of the ciphers the secret_messages
    application contains"""
    print("Here is a list of all the ciphers that can be used.\n" +
          "{}\n".format(cipher_list))


def cipher_selector(cipher_list):
    """This function gets the users choice of chiper and returns the
    choice of the user as a string"""
    clear()
    cipher_viewer(cipher_list)
    cipher = input("""Which cipher do you want to use?
    Enter q to quit.  """).lower()
    return(cipher)


def encryption(cipher):
    clear()
    temp = input("""This message will be destroyed.
Press enter to return to the main menu.""")


def decryption(cipher):
    clear()
    temp = input("""This message will be destroyed.
Press enter to return to the main menu.""")


def main(clear_screen=True):
    """Main() is the primary menu for secret_messages.py
    It prompts the user to select a cipher and to encrypt or decrypt.
    The user is also allowed to quit and end the script."""

    cipher_list = ['ADFGVX', 'Atbash', 'Bifid']

    while True:
        # This clears the screen on every instance of the loop
        # Except for when the welcome screen is shown
        if clear_screen:
            clear()
        else:
            clear_screen = True

        # Prints out a menu prompting the user to select a cipher or quit
        # Asks the user if the cipher is going to encrypt or decrypt
        menu_selector = input(
         """Would you like to encrypt or decrypt a message?flkasjlsjadjsfhdakjlfshad
Enter view to see the ciphers this program has.
Enter quit or q to end the program. """).lower()

        # Sends the user to an encryption or decryption function
        if menu_selector == 'encrypt' or menu_selector == 'e':
            encryption(cipher_selector(cipher_list))
        elif menu_selector == 'decrypt' or menu_selector == 'd':
            decryption(cipher_selector(cipher_list))
        elif menu_selector == 'view' or menu_selector == 'v':
            clear()
            cipher_viewer(cipher_list)
            clear_screen = False
        elif(menu_selector) == 'quit' or menu_selector == 'q':
            break


if __name__ == "__main__":
    # Makes sure that the script does not run if imported
    welcome()
