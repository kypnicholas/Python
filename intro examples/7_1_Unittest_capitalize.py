
import unittest
# import 7_Capitalize                               # THROWS AN ERROR AS IT CANNOT IMPORT  A FILE THAT STARTS WITH A NUMBER           
Capitalize = __import__ ('7_Capitalize')            # USE THIS AS A WORKAROUND

class TestCap(unittest.TestCase):
    
    def test_one_word(self):
        text = 'python'
        result = Capitalize.cap_text(text)
        self.assertEqual(result, 'Python')
        
    def test_multiple_words(self):
        text = 'monty python'
        result = Capitalize.cap_text(text)
        self.assertEqual(result, 'Monty Python')
        
        
if __name__ == '__main__':
    unittest.main()