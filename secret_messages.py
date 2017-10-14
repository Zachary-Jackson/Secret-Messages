import os

from atbash import Atbash
from rail_fence import RailFence
from keyword_cipher import KeywordCipher

# This function calls on the proper class for the requested cipher


def clear():
    """This function clears the screen for easier reading and use"""
    os.system('cls' if os.name == 'nt' else 'clear')


def welcome():
    """This function welcomes the user to the program"""
    clear()
    print("""      Welcome to the secret messages application!
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
    """This function gets the users choice of chiper and returns a
    variable as the class of the the aformentioned chiper"""
    else_true = True
    while True:
        if else_true:
            clear()
        cipher_viewer(cipher_list)
        cipher = input("""Which cipher do you want to use?
        Enter r to return to the main menu.  """).lower()
        # This section creates the chiper class to return
        if cipher == 'atbash' or cipher =='a':
            cipher = Atbash()
            break
        elif cipher == 'railfence' or cipher == 'rail fence':
            cipher = RailFence()
            break
        elif cipher == 'keyword' or cipher =='k':
            cipher = KeywordCipher()
            break
        elif cipher == 'return' or cipher == 'r' or cipher == 'q':
            return False
        else:
            clear()
            print("That is not a valid option.\n")
            else_true = False
    return(cipher)


def encryption(cipher, pad_lock):
    """ This function takes a cipher class and returns a properly formated
    encrypted string using the class's encryption and get_input function """
    message, keyword = cipher.get_input()
    output = cipher.encryption(message, keyword)
    if pad_lock:
        pad = input("What one time key do you want to use?")
        print(cipher.one_time_key_encryption(output, pad))
    else:
        print(cipher.encryption(message, keyword))
    continue_prompt = input("""This message will be destroyed.
Press enter to return to the main menu.""")
    # Normally the following would be left off, but is included so no
    # PEP8 problems get presented
    if continue_prompt:
        return None


def decryption(cipher, pad_lock):
    """ This function takes a chiper class and returns a properly formated
    encrypted string using the class's encryption and get_input function """
    message, keyword = cipher.get_input(encrypt=False)
    print(cipher.decryption(message, keyword))
    continue_prompt = input("""This message will be destroyed.
Press enter to return to the main menu.""")
    # Normally the following would be left off, but is included so no
    # PEP8 problems get presented
    if continue_prompt:
        return None


def main(clear_screen=True):
    """Main() is the primary menu for secret_messages.py
    It prompts the user to select a cipher and to encrypt or decrypt.
    The user is also allowed to quit and end the script."""

    cipher_list = ['Atbash', 'Keyword', 'Rail Fence']
    one_time_pad = True

    while True:
        # This clears the screen on every instance of the loop
        # Except for when the welcome screen is shown
        if clear_screen:
            clear()
        else:
            clear_screen = True

        # Prints out a menu prompting the user to select a cipher or quit
        # Asks the user if the cipher is going to encrypt or decrypt
        print("""    Would you like to encrypt 'e' or decrypt 'd' a message?
 Enter 'view' or 'v' to see the ciphers this program has.
 Enter 'pad lock' or 'p' to turn on or off the one time key encryption.""")
        if one_time_pad == True:
            print(" The one time pad is activated.")
        else:
            print(" You currently have the one time pad disabled")
        menu_selector = input("\n Enter 'quit' or 'q' to end the "
                         " program.  ").lower()


        # Sends the user to an encryption or decryption function
        if menu_selector == 'encrypt' or menu_selector == 'e':
            encryption(cipher_selector(cipher_list), one_time_pad)
        elif menu_selector == 'decrypt' or menu_selector == 'd':
            decryption(cipher_selector(cipher_list), one_time_pad)
        elif menu_selector == 'view' or menu_selector == 'v':
            clear()
            cipher_viewer(cipher_list)
            clear_screen = False
        elif menu_selector == 'pad lock' or menu_selector == 'p':
            if one_time_pad == True:
                one_time_pad = False
            else:
                one_time_pad = True
        elif(menu_selector) == 'quit' or menu_selector == 'q':
            break


if __name__ == "__main__":
    # Makes sure that the script does not run if imported
    welcome()
