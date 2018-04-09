import string

from cipher import Cipher


class Caesar(Cipher):
    FORWARD = string.ascii_uppercase * 3

    def __init__(self, offset=3):
        self.offset = offset
        self.FORWARD = string.ascii_uppercase + string.ascii_uppercase[:self.offset+1]
        self.BACKWARD = string.ascii_uppercase[:self.offset+1] + string.ascii_uppercase

    def encryption(self, text, *args, **kwargs):
        output = []
        text = text.upper()
        text = self.character_encryptor(text)
        for char in text:
            try:
                index = self.FORWARD.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self.FORWARD[index+self.offset])
        return ''.join(output)

    def decryption(self, text, *args, **kwargs):
        output = []
        text = text.upper()
        text = self.character_decryptor(text)
        for char in text:
            try:
                index = self.BACKWARD.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self.BACKWARD[index-self.offset])
        return ''.join(output)
