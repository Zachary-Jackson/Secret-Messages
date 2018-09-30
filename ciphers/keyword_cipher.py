import copy
import string

from .cipher import Cipher


class KeywordCipher(Cipher):
    def __init__(self):
        """This method initializes a letter list"""
        self.letters = string.ascii_uppercase
        self.letters_reversed = self.letters[::-1]
        self.letters_list = [letter for letter in self.letters]
        self.letters_reversed_list = ([letter for letter
                                      in self.letters_reversed])

    @staticmethod
    def get_keyword():
        """ This gets an input from the user and returns the keyword for
        the keyword cipher. It presumes that the message has been gotten
        elsewhere."""
        print("\n You are using the Keyword cipher.")
        keyword = input(" What keyword do you want to use?  ")
        return keyword

    def new_alphabet_from_keyword(self, keyword):
        """This method takes a keyword and creates a "new" alphabet
        using the parameters of the Keyword cipher. This returns a
        string of the alphabet"""
        copy_alphabet = copy.copy(self.letters_list)
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

    def encryption(self, text, keyword=None, *args, **kwargs):
        """This method takes a string of text and returns the uppercase
        result from the encryption in the form of a single string."""
        if not keyword:
            keyword = self.get_keyword()

        # letters_list is renamed alphabet_list for easier readability
        alphabet_list = self.letters_list
        output = []

        #uppercase all text letters
        text = text.upper()

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

        return ''.join(output)

    def decryption(self, text, keyword=None, *args, **kwargs):
        """This method takes a string of text and returns the uppercase
        result from the decryption in the form of a single string."""
        if not keyword:
            keyword = self.get_keyword()

        alphabet_list = self.letters_list
        output = []

        #uppercase all text letters
        text = text.upper()

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
