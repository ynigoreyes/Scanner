import unittest
from Scanner import Scanner
from BadTokenExpection import BadTokenExpection

class TestScannerFunctionality(unittest.TestCase):
    def test_for_error_on_bad_assignment(self):
        with open('./test_cases/BadAssignment.txt') as f:
            fileContents = f.read()
            with self.assertRaises(BadTokenExpection):
                Scanner.scan(fileContents)
            
if __name__ == '__main__':
    unittest.main()