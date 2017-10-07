#This is a temporary file to get the Atbash cipher working before
# the cipher is transfered to a class
#This is also just for me to play around a bit.

import string

#Creates a dictionary with letters and there corisponding opposites
# could just use letters and letters_reversed as shown in encryption()
letters = string.ascii_lowercase
letters_reversed = letters[::-1]
alphabet = {}
#The counter represents the alphabet, but is reduced by one to allow for indexes
counter = 25
while counter >= 0:
    alphabet[letters[counter]] = {letters_reversed[counter]}
    counter -=1


def encryption():
    #gathers a string from the user to convert
    thing_to_encrypt = input("What do you want to encrypt? ").lower()
    thing_to_return = []
    # This changes the letters in thing_to_encrypt to there corisponding
    # values in the Atbash chripter
    for letter in thing_to_encrypt:
        for key, value in alphabet.items():
            if letter == key:
                for thing in value:
                    thing_to_return.append(thing)
    print(''.join(thing_to_return))




def decryption():
    #the encryption/decryption could be done with a counter and indexes
    # instead of a created dictionary, but the dictionary could
    # be helpful latter on.
    thing_to_encrypt = input("What are you decrypting? ").lower()
    thing_to_return = []
    # Starts a loop and counter for each letter to be encrypted
    # and changes them based on the indexes of letters and letters_reversed.
    for letter in thing_to_encrypt:
        counter = 25
        while counter >= 0:
            if letter == letters_reversed[counter]:
                thing_to_return.append(letters[counter])
            counter -=1
    print(''.join(thing_to_return))


def main():
    #ask the user if they want to encrypt or decrypt and do the following
    while True:
        conversion = input("""Do you want to encrypt or decrypt a message?
        Enter q to quit  """).lower()

        if conversion == 'e' or conversion == 'encrypt':
            encryption()
        elif conversion =='d' or conversion == 'decrypt':
            decryption()
        elif conversion == 'q':
            print("Thanks for using this program!")
            break

main()
