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
    def whitespace_remover(cls, text):
        """This method takes a string and removes the whitespaces and
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
            for item in alphabet_list:
                if letter == item:
                    numbers_from_pad.append(alphabet_list.index(item))
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
            if number > 26:
                combined_numbers[index_counter] = number - 26
                index_counter += 1
            else:
                index_counter += 1


                index_counter += 1
        # This restructures combined_numbers into a string to return
        import pdb; pdb.set_trace()
        output = []
        for number in combined_numbers:
            output.append(alphabet_list[number])
        return ''.join(output)

zach = Cipher
print(zach.one_time_key_encryption('sadf', 'fds'))
