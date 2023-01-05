import unittest

from translator import english_to_french, french_to_english

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertRaises(Exception, french_to_english, None) # test when None is given as input, the function raises an exception.


    def test2(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # test when Bonjour is given as input, the output is Hello

        

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertRaises(Exception, english_to_french, None) # test when None is given as input, the function raises an exception.

    def test2(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour') # test when Hello is given as input, the output is Bonjour

        
unittest.main()