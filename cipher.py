import os
import string

# This class is the parent class for all ciphers in that it automatically
# creates the required encrypt and decrypt functions for ciphers.


class Cipher:
    def __init__(self):
        """This method initalizes Atbash"""
        self.letters = string.ascii_uppercase
        self.letters_reversed = self.letters[::-1]

    @classmethod
    def clear(cls):
        """This method clears the screen for easier reading and use"""
        os.system('cls' if os.name == 'nt' else 'clear')

    @classmethod
    def get_input(cls, encrypt=True, *args, **kwargs):
        """ This gets an input from the user and returns the raw data. """
        cls.clear()
        if encrypt:
            message_word = "encrypt"
        else:
            message_word = "decrypt"
        message = input("Please enter the message you want to {}.\n".format(
                        message_word) +
                        "Use only standard letters and no numbers.  ")
        return message

    @classmethod
    def whitespace_remover(cls, text):
        """ This method takes a string and removes the whitespaces and
        punctuation before rejoining the string without whitespaces or
        punctuation and returning it. """
        punctuation = [' ', '.', '!', '?', ';', '@', ',', '$']
        new_text = []
        for letter in text:
            if letter not in punctuation:
                new_text.append(letter)
        return ''.join(new_text)

    @classmethod
    def character_seperator(cls, text, *args, **kwargs):
        """This method takes a list of letters or a single string with no
        whitespaces and convertes it into a string where every fith
        item is seperated by a space"""

        # The following is redundancy to allow the use of a single string
        # or a list of letters
        text = ''.join(text)
        text = text.upper()
        temp_text = []
        for letter in text:
            temp_text.append(letter)

        # This section seperates the temp_output file by items of fives
        parsed_output = []
        output = []
        max_count = len(temp_text) - 1
        main_counter = 0
        sub_counter = 1
        # This while loop gets all groups of letters except the last group
        # if the last group does not round until five
        while max_count >= main_counter:
            parsed_output.append(temp_text[main_counter])
            main_counter += 1
            if sub_counter == 5:
                output.append(''.join(parsed_output))
                parsed_output = []
                sub_counter = 0
            sub_counter += 1
        if parsed_output:
            output.append(''.join(parsed_output))

        return output
