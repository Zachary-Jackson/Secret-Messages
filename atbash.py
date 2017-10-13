from cipher import Cipher


class Atbash(Cipher):
    def encryption(self, text, *args, **kwargs):
        """This method returns the uppercased result from the encryption"""
        temp_output = []
        text = text.upper()
        for character in text:
            counter = 25
            while counter >= 0:
                if character == self.letters[counter]:
                    temp_output.append(self.letters_reversed[counter])
                counter -= 1
        output = Cipher
        return output.character_seperator(temp_output)

    def decryption(self, text, *args, **kwargs):
        """This method returns the uppercased result from the decryption"""
        return self.encryption(text)
