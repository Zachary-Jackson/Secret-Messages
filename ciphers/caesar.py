import string

from .cipher import Cipher


class Caesar(Cipher):
    FORWARD = string.ascii_uppercase * 3

    def __init__(self, offset=3):
        """This method initializes Caesar with an encryption alphabet"""
        self.offset = offset
        self.FORWARD = string.ascii_uppercase + string.ascii_uppercase[:self.offset+1]
        self.BACKWARD = string.ascii_uppercase[:self.offset+1] + string.ascii_uppercase

    def encryption(self, text, *args, **kwargs):
        """
        Uses a given text message and encrypts it using the caesar cipher

        :param text: The message to be encrypted
        :return: The encrypted message
        """
        output = []
        text = text.upper()
        for char in text:
            try:
                index = self.FORWARD.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self.FORWARD[index+self.offset])
        return ''.join(output)

    def decryption(self, text, *args, **kwargs):
        """
        Uses a given text message and decrypts it using the caesar cipher

        :param text: The message to be decrypted
        :return: The decrypted message
        """
        output = []
        text = text.upper()
        for char in text:
            try:
                index = self.BACKWARD.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self.BACKWARD[index-self.offset])
        return ''.join(output)
