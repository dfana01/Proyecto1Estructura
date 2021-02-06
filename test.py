import unittest
from main import read_file, clean, calculate_similarity, levenshtein_distance, equal, read_folder_meta


class Test(unittest.TestCase):
    def test_read_file(self):
        self.assertEqual(read_file('db/test/test.py'), r"Hello world")

    def test_clean_str(self):
        self.assertEqual(clean("Hello world"), "Helloworld")

    def test_calculate_similarity(self):
        self.assertEqual(calculate_similarity("estructura de datos", "estructura de ", 5), 73.68)

    def test_levenshtein_distance(self):
        self.assertEqual(levenshtein_distance("estructura de datos", "estructura de "), 5)

    def test_equal_true(self):
        self.assertTrue(equal("estructura de datos", "estructura de datos"))

    def test_equal_false(self):
        self.assertTrue(not equal("estructura de datos", "estructura de "))

    def test_read_folder_meta(self):
        self.assertTrue("test.py" in [e.name for e in read_folder_meta('db/test')])

if __name__ == '__main__':
    unittest.main()
