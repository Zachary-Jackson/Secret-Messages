import string

from cipher import Cipher


class Atbash(Cipher):

    def __init__(self):
        """This method initalizes Atbash"""
        self.letters = string.ascii_uppercase
        self.letters_reversed = self.letters[::-1]

    def encryption(self, text):
        """This method returns the uppercased result from the encryption"""
        temp_output = []
        text = text.upper()
        letters = string.ascii_uppercase
        letters_reversed = letters[::-1]
        for character in text:
            counter = 25
            while counter >= 0:
                if character == letters[counter]:
                    temp_output.append(letters_reversed[counter])
                counter -= 1
        output = Cipher
        return output.character_seperator(temp_output)

    def decryption(self, text):
        """This method returns the uppercased result from the decryption"""
        temp_output = []
        text = text.upper()
        letters = string.ascii_uppercase
        letters_reversed = letters[::-1]
        for character in text:
            counter = 25
            while counter >= 0:
                if character == letters_reversed[counter]:
                    temp_output.append(letters[counter])
                counter -= 1
        output = Cipher
        return output.character_seperator(temp_output)
