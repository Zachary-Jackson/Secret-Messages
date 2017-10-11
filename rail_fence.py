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

    def encryption(self, text_data):
        """This method returns the uppercased result from the encryption"""
        # Creates a list format of text
        text = []
        for letter in text_data:
            text.append(letter)
        # Figures out the length of the text and creates an additional
        # two lists to start the encryption proccess
        length = len(text)
        # text_2 & 3 are empty lists to be filled latter with letters
        text_2 = self.empty_list_creator(self, length)
        text_3 = self.empty_list_creator(self, length)
        # This section fills the text_2 and replaces some letters in text
        main_counter = 0
        while main_counter < length:
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
        while main_counter < length:
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

        output = self.rail_sorter(self, text, text_2, text_3)
        output = self.character_seperator(output)
        return output

    def decryption(self, text):
        """This method returns the uppercased result from the decryption"""
        output = Cipher
        return output.character_seperator(temp_output)


zach = RailFence
print(zach.encryption(zach, 'wearediscoveredfleeatonce'))
