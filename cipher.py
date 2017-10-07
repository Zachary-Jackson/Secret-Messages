#This class is the parent class for all ciphers in that it automatically
#creates the required encrypt and decrypt functions for ciphers.

class Cipher:
    def encrypt(self):
        raise NotImplementedError()

    def decrypt(self):
        raise NotImplementedError()
