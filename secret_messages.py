import os

from atbash import Atbash
from rail_fence import RailFence
from keyword_cipher import KeywordCipher
from output_to_text import OutputToText

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
    application contains."""
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
        if cipher == 'atbash':
            cipher = Atbash()
            break
        elif cipher == 'railfence' or cipher == 'rail fence':
            cipher = RailFence()
            break
        elif cipher == 'keyword':
            cipher = KeywordCipher()
            break
        elif cipher == 'return' or cipher == 'r' or cipher == 'q':
            cipher = False
            return cipher
        else:
            clear()
            print("That is not a valid option.\n")
            else_true = False
    return(cipher)


def encryption(cipher, pad_lock, output_to_file):
    """ This function takes a cipher class and returns a properly formated
    encrypted string using the class's encryption and get_input function """
    if cipher:
        message, keyword = cipher.get_input()
        if pad_lock:
            pad = input("\n What one time key do you want to use?\n"
                        " The pad can include letters and numbers.   ")
            output = cipher.encryption(message, keyword)
            output = cipher.one_time_key_encryption(output, pad)
            print('\n ' + str())
        else:
            output = cipher.encryption(message, keyword)
            print('\n' + str(output))
        if output_to_file:
            text_output = OutputToText()
            text_output.write(output)
            print(" This message will be saved in temp_text.txt")
            continue_prompt = input('Press enter to return to the '
                                    'main menu.')
        else:
            continue_prompt = input(""" This message will be destroyed.
        Press enter to return to the main menu.""")
        # Normally the following would be left off, but is included so no
        # PEP8 problems get presented
        if continue_prompt:
            return None


def decryption(cipher, pad_lock, output_to_file):
    """ This function takes a chiper class and returns a properly formated
    encrypted string using the class's decryption and get_input function """
    if cipher:
        if output_to_file:
            text_output = OutputToText()
            message = text_output.get()
            if message:
                print("\n We have gotten your encrypted message from"
                      "'temp_text.txt'")
                try:
                    keyword = cipher.get_keyword()
                except AttributeError:
                    keyword = False
            else:
                message, keyword = cipher.get_input(encrypt=False)
        else:
            message, keyword = cipher.get_input(encrypt=False)
        if pad_lock:
            pad = input("\n What one time key do you want to use?\n"
                        " The pad can include letters and numbers.   ")
            output = cipher.one_time_key_decryption(message, pad)
            print('\n ' + str(cipher.decryption(output, keyword)))
        else:
            print('\n' + str(cipher.decryption(message, keyword)))
        continue_prompt = input("""\n This message will be destroyed.
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
    output_to_file = True

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
        if one_time_pad is True:
            print(" The one time pad is activated.")
        else:
            print(" You currently have the one time pad disabled")
        if output_to_file:
            print('\n You are currently outputing the encryption/decryption'
                  ' to a file.')
        else:
            print('\n The encryption/decryption output to file'
                  ' had been disabled.')
        print(" Enter 'output' or 'o' to turn on or off the output to file.")
        menu_selector = input("\n Enter 'quit' or 'q' to end the "
                              " program.  ").lower()

        # Sends the user to an encryption or decryption function
        if menu_selector == 'encrypt' or menu_selector == 'e':
            encryption(cipher_selector(cipher_list), one_time_pad,
                       output_to_file)
        elif menu_selector == 'decrypt' or menu_selector == 'd':
            decryption(cipher_selector(cipher_list), one_time_pad,
                       output_to_file)
        elif menu_selector == 'view' or menu_selector == 'v':
            clear()
            cipher_viewer(cipher_list)
            clear_screen = False
        elif menu_selector == 'pad lock' or menu_selector == 'p':
            if one_time_pad is True:
                one_time_pad = False
            else:
                one_time_pad = True
        elif menu_selector == 'output' or menu_selector == 'o':
            if output_to_file:
                output_to_file = False
            else:
                output_to_file = True
        elif(menu_selector) == 'quit' or menu_selector == 'q':
            break


if __name__ == "__main__":
    # Makes sure that the script does not run if imported
    welcome()
