#This class is the parent class for all ciphers in that it automatically
#creates the required encrypt and decrypt functions for ciphers.

class Cipher:
    def encryption(self):
        """This creates an encryption method for all ciphers"""
        raise NotImplementedError()


    def decryption(self):
        """This creates a decryption method for all ciphers"""
        raise NotImplementedError()


    def character_seperator(self, text):
        """This method takes a list of letters or a single string with no
        whitespaces and convertes it into a string where every fith
        item is seperated by a space"""

        #The following is redundancy to allow the use of a single string
        #or a list of letters
        text = ''.join(text)
        text = text.upper()
        temp_text = []
        for letter in text:
            temp_text.append(letter)

        #This section seperates the temp_output file by items of fives
        parsed_output = []
        output = []
        max_count = len(temp_text) - 1
        main_counter = 0
        sub_counter = 1
        #This while loop gets all groups of letters except the last group
        #if the last group does not round until five
        while max_count >= main_counter:
            parsed_output.append(temp_text[main_counter])
            main_counter += 1
            if sub_counter == 5:
                output.append(''.join(parsed_output))
                parsed_output = []
                sub_counter = 0
            sub_counter += 1
        if parsed_output:
            output.append(''.join(parsed_output))

        return output
