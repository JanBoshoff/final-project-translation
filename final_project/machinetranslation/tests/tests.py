import unittest

from translator import english_to_french, french_to_english


class TestFrenchToEnglish(unittest.TestCase):

    def test1(self):
        # test when None is given as input, the function raises an exception.
        self.assertRaises(Exception, french_to_english, None)

    def test2(self):
        # test when Bonjour is given as input, the output is Hello
        self.assertEqual(french_to_english('Bonjour'), 'Hello')


class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        # test when None is given as input, the function raises an exception.
        self.assertRaises(Exception, english_to_french, None)

    def test2(self):
        # test when Hello is given as input, the output is Bonjour
        self.assertEqual(english_to_french('Hello'), 'Bonjour')


unittest.main()
