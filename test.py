import unittest
from main import read_file, clean, calculate_similarity, levenshtein_distance, equal, read_folder_meta\
    , plagiarism_checker, equalize_functions_n_vars


class UnitTest(unittest.TestCase):
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

    def test_equalize_functions_and_vars(self):
        code1 = """
        def oianfoasfpoasiodfjaoisdopasfdas(*args):
            try:
                iajfiadjfiaofdasdf = float(int(args[0], 2))
                for idx in range(1, len(args)):
                    if idx % 2 != 0:
                        oajfkoadfpoasiofas = args[idx]
                        faoisjfoasfoadsf = float(int(args[idx + 1], 2))
                        oiajfafomasf = operators[op](acu, n)
                return acu
            except Exception:
                raise ValueError(r/"/""
                    Malformed exception please check if your input complies the format 
                    Format: calculator <binary-number> <+ | - | * | / | and | or> <binary-number> [<+ | - | * | / | and | or> <binary-number>]
                /"/"")
        """
        code2 = """
        def oajdfoiajsoifjasdiofjaosdnfoandpgapdsofja(*args):
            try:
                okasfoafoasofmasdf = float(int(args[0], 2))
                for idx in range(1, len(args)):
                    if idx % 2 != 0:
                        ioanfoasfoijasdopfnasdonvojasdnv = args[idx]
                        ojkmfaokdsfmoasfas = float(int(args[idx + 1], 2))
                        afasjfoasjfipoajsdiofjas = operators[op](acu, n)
                return acu
            except Exception:
                raise ValueError(r/"/""
                    Malformed exception please check if your input complies the format 
                    Format: calculator <binary-number> <+ | - | * | / | and | or> <binary-number> [<+ | - | * | / | and | or> <binary-number>]
                /"/"")
        """
        code1_equalize = equalize_functions_n_vars(code1)
        code2_equalize = equalize_functions_n_vars(code2)
        self.assertEqual(code2_equalize, code1_equalize)


class IntegrationTest(unittest.TestCase):
    def test_equal_file(self):
        self.assertTrue("files are equal" in plagiarism_checker("db/tarea0"))

    def test_file_hidden_plagiarism_with_tabs_and_space(self):
        self.assertTrue("is possible that the user try to hide plagiarism with taps and spaces" in plagiarism_checker("db/tarea0"))

    def test_file_hidden_plagiarism_with_new_name_function(self):
        self.assertTrue("renaming function and/or variables" in plagiarism_checker("db/tarea0"))


if __name__ == '__main__':
    unittest.main()
