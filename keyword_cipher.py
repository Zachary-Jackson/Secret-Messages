import copy

from cipher import Cipher


class KeywordCipher(Cipher):
    def get_input(self, encrypt=True, *args, **kwargs):
        """This gets an input from the users and returns a text
        and keyword file."""
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

    def new_alphabet_from_keyword(self, keyword):
        """This method takes a keyword and creates a "new" alphabet
        using the parameters of the Keyword cipher. This returns a
        string of the alphabet"""
        copy_alphabet = copy.copy((self.letters_list))
        keyword_list = [letter.upper() for letter in keyword]
        for letter in keyword_list:
            for item in copy_alphabet:
                if letter == item:
                    copy_alphabet.remove(item)
        return ''.join(keyword_list + copy_alphabet)

    def encryption(self, text, keyword, *args, **kwargs):
        """This method returns the uppercased result from the encryption"""
        # letters_list is renamed alphabet_list for easier readability
        alphabet_list = self.letters_list
        text = self.whitespace_remover(text).upper()
        output = []

        new_alphabet_list = self.new_alphabet_from_keyword(keyword)
        new_alphabet_list = [letter for letter in new_alphabet_list]

        # This compares the text in keyword to new_alphabet_list
        # and makes a new string based on the comparison
        for letter in text:
            for item in alphabet_list:
                if letter == item:
                    output.append(new_alphabet_list[
                     # This is the index value in text corresponding to letter
                     alphabet_list.index(item)])

        return output

    def decryption(self, text, keyword, *args, **kwargs):
        """This method returns the uppercased result from the decryption"""
        alphabet_list = self.letters_list
        text = self.whitespace_remover(text).upper()
        output = []

        new_alphabet_list = self.new_alphabet_from_keyword(keyword)
        new_alphabet_list = [letter for letter in new_alphabet_list]

        # This compares the text in new_alphabet_list to keyword
        # and makes a new string based on the comparison
        for letter in text:
            for item in new_alphabet_list:
                if letter == item:
                    output.append(alphabet_list[
                     # This is the index value in text corresponding to letter
                     new_alphabet_list.index(item)])

        return output


zach = KeywordCipher()
print(zach.decryption('dghvenpstbmihvtl', 'kryptos'))
