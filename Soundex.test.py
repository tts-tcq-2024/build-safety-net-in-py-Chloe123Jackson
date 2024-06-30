import unittest
from Soundex import generate_soundex

class TestSoundex(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(generate_soundex(""), "")

    def test_single_character(self):
        self.assertEqual(generate_soundex("A"), "A000")
        
    def test_single_character(self):
        self.assertEqual(generate_soundex("Robert"), "R163")
        
    def test_single_character(self):
        self.assertEqual(generate_soundex("Pfister"), "P236")
    
    def test_single_character(self):
        self.assertEqual(generate_soundex("INNOCENT"), "I152")
    
    def test_single_character(self):
        self.assertEqual(generate_soundex("aeiou"), "A000")
    
    def test_single_character(self):
        self.assertEqual(generate_soundex("Tymczak"), "T522")

    def test_single_character(self):
        self.assertEqual(generate_soundex("AebeF"), "A100")
    
    def test_single_character(self):
        self.assertEqual(generate_soundex("0"), "000")
    
    def test_single_character(self):
        self.assertEqual(generate_soundex("!hello"), "H400")
    
if __name__ == '__main__':
    unittest.main()
