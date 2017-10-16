from cipher import Cipher


class Atbash(Cipher):
    def encryption(self, text, *args, **kwargs):
        """This method takes a string of text and returns the uppercased
        result from the encryption in the form of a single string."""
        temp_output = []
        text = text.upper()
        text = self.character_encryptor(text)
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
        temp_output = self.character_seperator(temp_output)

        return ''.join(temp_output)

    def decryption(self, text, *args, **kwargs):
        """This method takes a string of text and returns the uppercased
        result from the decryption in the form of a single string."""
        temp_output = []
        text = text.upper()
        text = self.character_decryptor(text)
        for character in text:
            if character not in self.letters:
                temp_output.append(character)
            else:
                counter = 25
                while counter >= 0:
                    if character == self.letters[counter]:
                        temp_output.append(self.letters_reversed[counter])
                    counter -= 1
        return ''.join(temp_output)
