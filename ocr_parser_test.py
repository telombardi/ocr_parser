import unittest
from ocr_parser import clean_substring

class TestOCRParser(unittest.TestCase):

    def test_clean_substring(self):
        self.assertEqual(clean_substring("@","telombardi@gmail.com"), "telombardi@gmail.com")
        self.assertEqual(clean_substring("@","telombardi @gmail.com"), "telombardi@gmail.com")
        self.assertEqual(clean_substring("@","telombardi@ gmail.com"), "telombardi@gmail.com")
        self.assertEqual(clean_substring("@","telombardi @ gmail.com"), "telombardi@gmail.com")
        self.assertEqual(clean_substring("@","telombardi  @  gmail.com"), "telombardi@gmail.com")
        self.assertEqual(clean_substring("@","telombardi\t@\tgmail.com"), "telombardi@gmail.com")
        self.assertEqual(clean_substring("!","telombardi@ gmail.com"), "telombardi@ gmail.com")
        self.assertEqual(clean_substring("telombardi     @gmail.com","telombardi @gmail.com"), "telombardi @gmail.com")
        self.assertEqual(clean_substring("telombardi @gmail.com","telombardi @gmail.com"), "telombardi @gmail.com")

if __name__ == '__main__':
    unittest.main(verbosity=2)

    
