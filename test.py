import unittest
from Scanner import Scanner
from BadTokenExpection import BadTokenExpection

class TestScannerFunctionality(unittest.TestCase):
    def test_for_error_on_bad_assignment(self):
        """
        read
        test assignment
        x := 7
        y = 7
        write
        """
        with open('./test_cases/BadAssignment.txt') as f:
            fileContents = f.read()
            with self.assertRaises(BadTokenExpection):
                Scanner.scan(fileContents)
    def test_for_no_error_on_comments(self):
        """
        read
        /**
        * Here is what a normal doc string looks like
        */
        test for comments
        /**
        * Here is what a normal doc string looks like
        */
        write
        /**
        * Here is a sneaky comment at the end
        */
        """
        with open('./test_cases/WithComments.txt') as f:
            fileContents = f.read()
            correctTokens = ['read', 'id', 'id', 'id', 'write']
            tokens = Scanner.scan(fileContents)
            self.makeSureArraysAreTheSame(tokens, correctTokens)
    def test_for_no_error_on_duplicates(self):
        """
        read write test duplicate another duplicate read write
        """
        with open('./test_cases/WithDuplicates.txt') as f:
            fileContents = f.read()
            correctTokens = ['read', 'write', 'id', 'id', 'id', 'id', 'read', 'write']
            tokens = Scanner.scan(fileContents)
            self.makeSureArraysAreTheSame(tokens, correctTokens)
            
    def test_for_no_error_on_symbols_with_comments(self):
        """
        // Here is a doc filled with all of the symbols
        / + - +()
        """
        with open('./test_cases/WithSymbolsAndComments.txt') as f:
            fileContents = f.read()
            correctTokens = ['/', '+', '-', '+', '(', ')']
            tokens = Scanner.scan(fileContents)
            self.makeSureArraysAreTheSame(tokens, correctTokens)
    def test_for_no_error_on_all_types_of_numbers(self):
        """
        0.99
        0.1
        1
        1.0
        100
        """
        with open('./test_cases/AllTypesOfNumbers.txt') as f:
            fileContents = f.read()
            correctTokens = ['number', 'number', 'number', 'number', 'number']
            tokens = Scanner.scan(fileContents)
            self.makeSureArraysAreTheSame(tokens, correctTokens)
    def test_for_error_on_bad_numbers(self):
        """
        1.1.2
        """
        with open('./test_cases/BadNumber.txt') as f:
            fileContents = f.read()
            with self.assertRaises(BadTokenExpection):
                Scanner.scan(fileContents)
    def test_for_error_on_strings_that_start_with_numbers(self):
        """
        4pple
        """
        with open('./test_cases/StringStartWithNumbers.txt') as f:
            fileContents = f.read()
            with self.assertRaises(BadTokenExpection):
                Scanner.scan(fileContents)
    
    def test_for_no_error_on_strings_that_start_with_letters_but_have_numbers(self):
        """
        f00bar m8
        """
        with open('./test_cases/StringStartWithLetter.txt') as f:
            fileContents = f.read()
            correctTokens = ['id', 'id']
            tokens = Scanner.scan(fileContents)
            self.makeSureArraysAreTheSame(tokens, correctTokens)
    
    def makeSureArraysAreTheSame(self, array1, array2):
        self.assertEqual(len(array1), len(array2), array1)
        for i, j in zip(array1, array2):
            self.assertEqual(i, j)

            
if __name__ == '__main__':
    unittest.main()