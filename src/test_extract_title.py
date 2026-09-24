import unittest
from main import extract_title
class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        extracted_title = extract_title("# this is my header\nthis shouldnt be part of the header.")
        self.assertEqual(extracted_title,"this is my header")
        extracted_title2 = extract_title("this is not my header\n## neither is this #or this\n# this will be my header.")
        self.assertEqual(extracted_title2,"this will be my header.")

if __name__ == '__main__':
    unittest.main()