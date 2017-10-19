import copy

from cipher import Cipher


class KeywordCipher(Cipher):
    # I do not know where this will go on other people's computers as this
    # is a relative path. On my computer it goes to
    # C:\Users\{username}\Documents\Python on Windows
    def get_input(self, encrypt=True, *args, **kwargs):
        """This gets an input from the user and returns a raw text file
        and a keyword file."""
        self.clear()
        if encrypt:
            message_word = "encrypt"
        else:
            message_word = "decrypt"
        message = input("Please enter the message you want to {}.\n".format(
                        message_word) +
                        "Use only standard letters and no numbers.  ")
        keyword = input("What keyword do you want to use?  ")
        return message, keyword

    def get_keyword(self, *args, **kwargs):
        """ This gets an input from the user and returns the keyword for
        the keyword cipher. It presumes that the message has been gotten
        elsewhere."""
        print("\n\t You are using the Keyword cipher.")
        keyword = input(" What keyword do you want to use?  ")
        return keyword

    def new_alphabet_from_keyword(self, keyword):
        """This method takes a keyword and creates a "new" alphabet
        using the parameters of the Keyword cipher. This returns a
        string of the alphabet"""
        copy_alphabet = copy.copy((self.letters_list))
        keyword_list = [letter.upper() for letter in keyword]
        used_letters = []
        for letter in keyword_list:
            if [letter] in used_letters:
                continue
            else:
                for item in copy_alphabet:
                    if letter == item:
                        copy_alphabet.remove(item)
                        used_letters.append(letter)
        return ''.join(used_letters + copy_alphabet)

    def encryption(self, text, keyword, *args, **kwargs):
        """This method takes a string of text and returns the uppercased
        result from the encryption in the form of a single string."""
        # letters_list is renamed alphabet_list for easier readability
        alphabet_list = self.letters_list
        text = self.character_encryptor(text).upper()
        output = []

        new_alphabet_list = self.new_alphabet_from_keyword(keyword)
        new_alphabet_list = [letter for letter in new_alphabet_list]

        # This compares the text in keyword to new_alphabet_list
        # and makes a new string based on the comparison
        for letter in text:
            found = False
            for item in alphabet_list:
                if letter == item:
                    output.append(new_alphabet_list[
                     # This is the index value in text corresponding to letter
                     alphabet_list.index(item)])
                    found = True
            if found is False:
                output.append(letter)

        return self.character_seperator(''.join(output))

    def decryption(self, text, keyword, *args, **kwargs):
        """This method takes a string of text and returns the uppercased
        result from the decryption in the form of a single string."""
        alphabet_list = self.letters_list
        text = self.character_decryptor(text).upper()
        output = []

        new_alphabet_list = self.new_alphabet_from_keyword(keyword)
        new_alphabet_list = [letter for letter in new_alphabet_list]

        # This compares the text in new_alphabet_list to keyword
        # and makes a new string based on the comparison
        for letter in text:
            found = False
            for item in new_alphabet_list:
                if letter == item:
                    output.append(alphabet_list[
                     # This is the index value in text corresponding to letter
                     new_alphabet_list.index(item)])
                    found = True
            if found is False:
                output.append(letter)
        return ''.join(output)
