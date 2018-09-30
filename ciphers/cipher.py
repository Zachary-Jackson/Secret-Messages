import os
import string


class Cipher:
    """This is a base template class for a cipher"""

    @classmethod
    def clear(cls):
        """This method clears the screen for easier reading and use"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def encryption(self, *args, **kwargs):
        raise NotImplementedError()

    def decryption(self, *args, **kwargs):
        raise NotImplementedError()

    def get_user_message(self):
        """
        Gets the user's encryption/decryption message
        Ensures that no punctuation or digits are in the message

        :return: a message string
        """
        digits_and_punctuation = string.digits + string.punctuation
        while True:
            message = input('Please enter a message to encrypt\n\n')

            # check if a digit or number is in message
            invalid_characters = False
            for char in digits_and_punctuation:
                if char in message:
                    invalid_characters = True
                    break

            if not invalid_characters:
                return message

            # Prepare the user for another message
            self.clear()
            print('Digits and Punctuation (234 (*&) are not allowed')
