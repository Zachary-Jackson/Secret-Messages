import os
import string

# This class is the parent class for all ciphers in that it automatically
# creates the required encrypt and decrypt functions for ciphers.


class Cipher:
    def __init__(self):
        """This method initalizes Atbash"""
        self.letters = string.ascii_uppercase
        self.letters_reversed = self.letters[::-1]
        self.letters_list = [letter for letter in self.letters]
        self.letters_reversed_list = ([letter for letter
                                      in self.letters_reversed])

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
        keyword = None
        return message, keyword

    @classmethod
    def character_encryptor(cls, text):
        """This method takes a string and converts the non letter portions
        of the string into other encrypted characters. """
        letters = string.ascii_letters
        new_text = []
        for letter in text:
            if letter in letters:
                new_text.append(letter)
            elif letter == ' ':
                new_text.append('&')
            elif letter == '.':
                new_text.append('*')
            elif letter == '!':
                new_text.append('%')
            elif letter == '?':
                new_text.append('#')
            elif letter == "'":
                new_text.append('=')
            elif letter == ',':
                new_text.append('@')
        return ''.join(new_text)

    @classmethod
    def character_decryptor(cls, text):
        """This method takes a string and unconverts the non letter portions
        of the string into turns them into unincrypted characters."""
        letters = string.ascii_letters
        new_text = []
        for letter in text:
            if letter in letters:
                new_text.append(letter)
            elif letter == '&':
                new_text.append(' ')
            elif letter == '*':
                new_text.append('.')
            elif letter == '%':
                new_text.append('!')
            elif letter == '#':
                new_text.append('?')
            elif letter == '=':
                new_text.append("'")
            elif letter == '@':
                new_text.append(',')
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
        # This section adds junk to the end of the the parsed_output if
        # parsed_output is not five characters long.
        counter = 0
        while len(parsed_output) < 5:
            if counter == 0:
                parsed_output.append('~')
                counter += 1
            elif counter == 1:
                parsed_output.append('>')
                counter += 1
            elif counter == 2:
                parsed_output.append('+')
        output.append(''.join(parsed_output))

        return ' '.join(output)

    @classmethod
    def one_time_key_encryption(cls, text, pad_key, *args, **kwargs):
        """This takes a single string and a pad_key and
        returns an encrypted message using the one time key
        encryption method."""
        alphabet_list = [letter for letter in string.ascii_uppercase]
        text = cls.whitespace_remover(text).upper()
        pad_key = cls.whitespace_remover(pad_key).upper()

        # This portion creates a list of numbers based on the index
        # values for each letter in text and then pad_key.
        numbers_from_text = []
        for letter in text:
            for item in alphabet_list:
                if letter == item:
                    numbers_from_text.append(alphabet_list.index(item))
        numbers_from_pad = []
        for letter in pad_key:
            try_continue = True
            for item in alphabet_list:
                if letter == item:
                    numbers_from_pad.append(alphabet_list.index(item))
                else:
                    if try_continue is True:
                        try:
                            temp_letter = int(letter)
                        except ValueError:
                            pass
                        else:
                            numbers_from_pad.append(temp_letter)
                            try_continue = False
        # This combines both of the numbers from text and the pad key
        combined_numbers = []
        length = len(text)
        index_counter = 0
        while index_counter < length:
            try:
                combined_numbers.append(numbers_from_text[index_counter] +
                                        numbers_from_pad[index_counter])
            except IndexError:
                combined_numbers.append(numbers_from_text[index_counter])
                index_counter += 1
            else:
                index_counter += 1
        # This section insures no number is above 26 and if it is
        # it gets rolled back by 26 numbers
        index_counter = 0
        for number in combined_numbers:
            if number > 25:
                combined_numbers[index_counter] = number - 26
                index_counter += 1
            else:
                index_counter += 1

        # This restructures combined_numbers into a string to return
        output = []
        for number in combined_numbers:
            output.append(alphabet_list[number])
        return cls.character_seperator(output)

    @classmethod
    def one_time_key_decryption(cls, text, pad_key, *args, **kwargs):
        """This takes a single string and a pad_key and
        returns an encrypted message using the one time key
        decryption method."""
        alphabet_list = [letter for letter in string.ascii_uppercase]
        text = cls.whitespace_remover(text).upper()
        pad_key = cls.whitespace_remover(pad_key).upper()

        # This portion creates a list of numbers based on the index
        # values for each letter in text and then pad_key.
        numbers_from_text = []
        for letter in text:
            for item in alphabet_list:
                if letter == item:
                    numbers_from_text.append(alphabet_list.index(item))
        numbers_from_pad = []
        for letter in pad_key:
            try_continue = True
            for item in alphabet_list:
                if letter == item:
                    numbers_from_pad.append(alphabet_list.index(item))
                else:
                    if try_continue is True:
                        try:
                            temp_letter = int(letter)
                        except ValueError:
                            pass
                        else:
                            numbers_from_pad.append(temp_letter)
                            try_continue = False
        # This combines both of the numbers from text and the pad key
        combined_numbers = []
        length = len(text)
        index_counter = 0
        while index_counter < length:
            try:
                combined_numbers.append(numbers_from_text[index_counter] -
                                        numbers_from_pad[index_counter])
            except IndexError:
                combined_numbers.append(numbers_from_text[index_counter])
                index_counter += 1
            else:
                index_counter += 1
        # This section insures no number is above 26 and if it is
        # it gets rolled back by 26 numbers
        index_counter = 0
        for number in combined_numbers:
            if number < 0:
                combined_numbers[index_counter] = number + 26
                index_counter += 1
            else:
                index_counter += 1

        # This restructures combined_numbers into a string to return
        output = []
        for number in combined_numbers:
            output.append(alphabet_list[number])
        return cls.character_seperator(output)
