import unittest
from Soundex import generate_soundex

class TestSoundex(unittest.TestCase):
    # Empty string
    def test_empty_string(self):
        self.assertEqual(generate_soundex(""), "")                                          
    # Single vowel
    def test_single_character(self):
        self.assertEqual(generate_soundex("A"), "A000")
    # Normal word     
    def test_normal_word(self):
        self.assertEqual(generate_soundex("Robert"), "R163")
    # Word with first and second characters sharing the same number     
    def test_same_group(self):
        self.assertEqual(generate_soundex("Pfister"), "P236")
    # Word which would result in encoded length being greater than 4
    def test_wordlength_out_of_range(self):
        self.assertEqual(generate_soundex("INNOCENT"), "I525")
    # All vowels together
    def test_all_vowels_together(self):
        self.assertEqual(generate_soundex("aeiou"), "A000")
    # Word with ending characters separated by a vowel
    def test_word_separated_by_vowel(self):
        self.assertEqual(generate_soundex("Tymczak"), "T520")
    # Word with ending a mix of vowel and consonants
    def test_consonant_vowel_mix(self):
        self.assertEqual(generate_soundex("AebeF"), "A100")
    # Input is a not a word
    def test_digits(self):
        self.assertEqual(generate_soundex("0"), "0000")
    # Word starts with a special character
    def test_starts_special_char(self):
        self.assertEqual(generate_soundex("!hello"), "!400")
    # Word ends with a special character
    def test_ends_special_char(self):
        self.assertEqual(generate_soundex("hel!o"), "H400")
    
if __name__ == '__main__':
    unittest.main()
