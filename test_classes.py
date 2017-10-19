import unittest

from atbash import Atbash
from cipher import Cipher
from keyword_cipher import KeywordCipher
from rail_fence import RailFence


class AtbashTestCase(unittest.TestCase):
    """ Tests the encryption/decryption for Atbash. """

    def test_encryption(self):
        """ Does the encryption work? """
        atbash = Atbash()
        test_1 = atbash.encryption('Merry had a little lamb')
        self.assertEqual(test_1, 'NVIIB &SZW& Z&ORG GOV&O ZNY~>')

        test_2 = atbash.encryption('Hello lama')
        self.assertEqual(test_2, 'SVOOL &OZNZ ')

        test_3 = atbash.encryption('They are close')
        self.assertEqual(test_3, 'GSVB& ZIV&X OLHV~')

    def test_decryption(self):
        """ Does the decryption work? """
        atbash = Atbash()
        test_1 = atbash.decryption('NVIIB &SZW& Z&ORG GOV&O ZNY~>')
        self.assertEqual(test_1, 'MERRY HAD A LITTLE LAMB')

        test_2 = atbash.decryption('svool &oznz')
        self.assertEqual(test_2, 'HELLO LAMA')

        test_3 = atbash.decryption('GSVB& ZIV&X OLHV~')
        self.assertEqual(test_3, 'THEY ARE CLOSE')


class KeywordCipherTestCase(unittest.TestCase):
    """ Tests the encryption/decryption for KeywordCipher. """

    def test_encryption(self):
        """ Does the encryption work? """
        keyword = KeywordCipher()
        test_1 = keyword.encryption('knowledge is power', 'kryptos')
        self.assertEqual(test_1, 'DGHVE TPST& BM&IH VTL~>')

        test_2 = keyword.encryption('They are close', 'tree')
        self.assertEqual(test_2, 'SFBY& TPB&E JMQB~')

    def test_decryption(self):
        """ Does the decryption work? """
        keyword_test = KeywordCipher()
        test_1 = keyword_test.decryption('DGHVE TPST& BM&IH VTL~>',
                                         'kryptos')
        self.assertEqual(test_1, 'KNOWLEDGE IS POWER')

        test_2 = keyword_test.decryption('SFBY& TPB&E JMQB~', 'tree')
        self.assertEqual(test_2, 'THEY ARE CLOSE')


class RailFenceTestCase(unittest.TestCase):
    """ Tests the encryption/decryption for RailFence. """

    def test_encryption(self):
        """ Does the encryption work? """
        railfence = RailFence()
        test_1 = railfence.encryption('wearediscoveredfleeatonce')
        self.assertEqual(test_1, 'WECRL TEERD SOEEF EAOCA IVDEN ')

        test_2 = railfence.encryption('We are discovered. Flee at once')
        self.assertEqual(test_2, 'WRIVD LANEA EDSOE E*FE& TOC&& CR&E& E~>++')

        test_3 = railfence.encryption('They are close')
        self.assertEqual(test_3, 'T&&SH YAECO EERL~')

    def test_decryption(self):
        """ Does the decryption work? """
        railfence = RailFence()
        test_1 = railfence.decryption('WECRL TEERD SOEEF EAOCA IVDEN')
        self.assertEqual(test_1, 'WEAREDISCOVEREDFLEEATONCE')

        test_2 = railfence.decryption('WRIVD LANEA EDSOE E*FE&' +
                                      ' TOC&& CR&E& E~>++')
        self.assertEqual(test_2, 'WE ARE DISCOVERED. FLEE AT ONCE')

        test_3 = railfence.decryption('T&&SH YAECO EERL~')
        self.assertEqual(test_3, 'THEY ARE CLOSE')


class OneTimePadTestCase(unittest.TestCase):
    """ Tests the encryption/decryption for the one time pad. """

    def test_encryption(self):
        """ Does the encryption work? """
        cipher = Cipher()
        test_1 = cipher.one_time_key_encryption('Hello', 'xmckl')
        self.assertEqual(test_1, 'EQNVZ ')

    def test_decryption(self):
        """ Does the decryption work? """
        cipher = Cipher()
        test_1 = cipher.one_time_key_decryption('eqnvz', 'xmckl')
        self.assertEqual(test_1, 'HELLO')


unittest.main()
