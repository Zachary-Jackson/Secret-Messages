import unittest

from ciphers import *


class AtbashTestCase(unittest.TestCase):
    """ Tests the encryption/decryption for Atbash. """

    def test_encryption(self):
        """ Does the encryption work? """
        atbach_cipher = Atbash()
        test_1 = atbach_cipher.encryption('Merry had a little lamb')
        self.assertEqual(test_1, 'NVIIB SZW Z ORGGOV OZNY')

        test_2 = atbach_cipher.encryption('aaa zzz')
        self.assertEqual(test_2, 'ZZZ AAA')

    def test_decryption(self):
        """
        Does the decryption work?
        Decryption works the same as encryption, so tests are reused
        """
        atbach_cipher = Atbash()
        test_1 = atbach_cipher.decryption('Merry had a little lamb')
        self.assertEqual(test_1, 'NVIIB SZW Z ORGGOV OZNY')

        test_2 = atbach_cipher.decryption('aaa zzz')
        self.assertEqual(test_2, 'ZZZ AAA')


class KeywordCipherTestCase(unittest.TestCase):
    """ Tests the encryption/decryption for KeywordCipher. """

    def test_encryption(self):
        """ Does the encryption work? """
        keyword_test = KeywordCipher()
        test_1 = keyword_test.encryption('knowledge is power', 'kryptos')
        self.assertEqual(test_1, 'DGHVETPST BM IHVTL')

    def test_decryption(self):
        """ Does the decryption work? """
        keyword_test = KeywordCipher()
        test_1 = keyword_test.decryption('DGHVETPST BM IHVTL', 'kryptos')
        self.assertEqual(test_1, 'KNOWLEDGE IS POWER')


class RailFenceTestCase(unittest.TestCase):
    """ Tests the encryption/decryption for RailFence. """

    def test_encryption(self):
        """ Does the encryption work? """
        railfence = RailFence()
        test_1 = railfence.encryption('merry had a little lamb')
        self.assertEqual(test_1, 'mydllaer a  itelmrhat b')

    def test_decryption(self):
        """ Does the decryption work? """
        railfence = RailFence()
        test_1 = railfence.decryption('mydllaer a  itelmrhat b')
        self.assertEqual(test_1, 'merry had a little lamb')


unittest.main()
