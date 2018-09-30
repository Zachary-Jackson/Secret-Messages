import string


from .cipher import Cipher


class Atbash(Cipher):

    def __init__(self):
        """This method initializes Atbash with an encryption alphabet"""
        self.letters = string.ascii_uppercase
        self.letters_reversed = self.letters[::-1]
        self.letters_list = [letter for letter in self.letters]
        self.letters_reversed_list = ([letter for letter
                                      in self.letters_reversed])

    def encryption(self, text):
        """This method takes a string of text and returns the uppercase
        result from the encryption in the form of a single string."""
        temp_output = []
        text = text.upper()
        for character in text:
            if character not in self.letters:
                temp_output.append(character)
            else:
                counter = 25
                while counter >= 0:
                    if character == self.letters[counter]:
                        temp_output.append(self.letters_reversed[counter])
                        counter = 0
                    counter -= 1

        return ''.join(temp_output)

    def decryption(self, text):
        """This method takes a string of text and returns the uppercase
        result from the decryption in the form of a single string."""
        return self.encryption(text)
