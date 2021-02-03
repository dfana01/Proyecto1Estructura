import unittest
import main
import os

TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'testdata.txt')

class Test(unittest.TestCase):
    def test_readFile(self):
        self.testfile = open(TESTDATA_FILENAME)
        self.testdata = self.testfile.read()

if __name__ == '__main__':
    unittest.main()
