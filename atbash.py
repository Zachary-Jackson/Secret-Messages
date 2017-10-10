import string

from cipher import Cipher



class Atbash(Cipher):


    def __init__(self):
        """This method initalizes Atbash"""
        self.letters = string.ascii_uppercase
        self.letters_reversed = letters[::-1]

    def encryption(self, text):
        """This method returns the uppercased result from the encryption"""
        output = []
        text = text.upper()
        letters = string.ascii_uppercase
        letters_reversed = letters[::-1]
        for character in text:
            counter = 25
            while counter >=0:
                if character == letters[counter]:
                    output.append(letters_reversed[counter])
                counter -=1
        return ''.join(output)

    def decryption(self, text):
        """This method returns the uppercased result from the decryption"""
        output = []
        text = text.upper()
        letters = string.ascii_uppercase
        letters_reversed = letters[::-1]
        for character in text:
            counter = 25
            while counter >=0:
                if character == letters_reversed[counter]:
                    output.append(letters[counter])
                counter -=1
        return ''.join(output)
