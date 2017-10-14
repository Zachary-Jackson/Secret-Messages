from cipher import Cipher


class RailFence(Cipher):
    def empty_list_creator(self, length):
        """ This returns an empty list that is the size of length.
        length needs to be a whole number. """
        returned_list = []
        while length:
            returned_list.append('')
            length -= 1
        return returned_list

    def rail_sorter(self, rail_1, rail_2, rail_3):
        """ This method sorts three rails of a rail fence and returns
        one string with them all sorted properly based on the rail fence
        parameters. """
        output = []
        # This stage goes through rail_1, rail_2 then rail_3 and looks for
        # letters and if it finds them it appends it to output.
        for letter in rail_1:
            if letter != '':
                output.append(letter)
        for letter in rail_2:
            if letter != '':
                output.append(letter)
        for letter in rail_3:
            if letter != '':
                output.append(letter)
        return ''.join(output)

    def encryption(self, text_data, *args, **kwargs):
        """This method takes a string of text and returns the uppercased
        result from the encryption in the form of a single string."""
        # Creates a list format of text
        text_data = self.whitespace_remover(text_data)
        text = []
        for letter in text_data:
            text.append(letter)

        # Figures out the length of the text and creates an additional
        # two lists to start the encryption proccess
        length = len(text)
        # text_2 & 3 are empty lists to be filled latter with letters
        text_2 = self.empty_list_creator(length)
        text_3 = self.empty_list_creator(length)

        # This section fills the text_2 and replaces some letters in text
        # main_counter controls the index variable for the append
        main_counter = 0
        # sub_counter controls if a letter will be transported
        sub_counter = 0
        for letter in text:
            if sub_counter == 0:
                sub_counter += 1
                main_counter += 1
                continue
            else:
                text_2[main_counter] = text[main_counter]
                text[main_counter] = ''
                sub_counter = 0
                main_counter += 1

        # This section fills the text_3 and replaces some letters in text
        main_counter = 0
        sub_counter = 1
        for letter in text:
            if sub_counter == 3:
                sub_counter = 0
                text_3[main_counter] = text[main_counter]
                text[main_counter] = ''
                main_counter += 1
            else:
                sub_counter += 1
                main_counter += 1
        output = self.rail_sorter(text, text_2, text_3)
        output = self.character_seperator(output)
        return output

    def decryption(self, text_data, *args, **kwargs):
        """This method takes a string of text and returns the uppercased
        result from the decryption in the form of a single string."""
        text_data = self.whitespace_remover(text_data)
        length = len(text_data)
        temp_text = []

        # This step takes the text_data string and turns it into a list
        for letter in text_data:
            temp_text.append(letter)

        # The text variables are used as the "rails" to the Rail Fence cipher
        # and will be used to store letters in
        text, text_2, text_3 = [], [], []

        # The len_texts are used to figure out how long the
        # text variables are going to be
        len_text_2 = int(length/2)
        len_text_3 = (int((length - len_text_2) / 2))
        len_text = ((length - len_text_2) - len_text_3)

        # This section allocates the proper letters to the text files.
        while len_text:
            text.append(temp_text.pop(0))
            len_text -= 1
        while len_text_2:
            text_2.append(temp_text.pop(0))
            len_text_2 -= 1
        while len_text_3:
            text_3.append(temp_text.pop(0))
            len_text_3 -= 1

        # This section reverts text 1, 2, and 3 into the pre cipher stage
        #
        # For help on how this works all three of the rails are
        # compared at the same time going through the number of letters
        # (counter) one by one and finding the letter on the proper rail in
        # a zig-zag pattern.
        #
        # 1) W . . . E . . . C . . . R . . . L . . . T . . . E
        # 2) . E . R . D . S . O . E . E . F . E . A . O . C .
        # 3) . . A . . . I . . . V . . . D . . . E . . . N . .
        #
        # This becomes WE ARE DISCOVERED FLEE AT ONCE without the spaces
        #
        # Note that text, text_2 and text_3 do not have spaces or '.'s
        # in them the above example is just to help with understanding
        # what is happening.

        output = []
        counter = 0
        sub_counter = 0
        # The reverse_sub_counter switches the direction of sub_counter
        # 0 means the sub_counter goes down a rail.  i.e 1) to 2)
        # 1 means the sub_counter goes up a rail.  i.e 3) to 2)
        reverse_sub_counter = 0
        while counter < length:
            if sub_counter == 0:
                output.append(text.pop(0))
                counter += 1
                sub_counter += 1
                reverse_sub_counter = 0
            elif sub_counter == 1:
                output.append(text_2.pop(0))
                counter += 1
                if reverse_sub_counter == 0:
                    sub_counter += 1
                else:
                    sub_counter -= 1
            else:
                output.append(text_3.pop(0))
                counter += 1
                reverse_sub_counter = 1
                sub_counter -= 1

        return self.character_seperator(output)
