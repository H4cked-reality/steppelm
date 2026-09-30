import unittest

from src.text_cleaner import clean_text


class TestCleanText(unittest.TestCase):
    def test_removes_empty_lines(self):
        text = "Birinji setir\n\n   \nIkinji setir"
        self.assertEqual(clean_text(text), "Birinji setir\nIkinji setir")

    def test_normalizes_spaces(self):
        text = "Salam,     dünýä!"
        self.assertEqual(clean_text(text), "Salam, dünýä!")

    def test_preserves_turkmen_characters(self):
        text = "ä ç ň ö ş ü ý ž"
        self.assertEqual(clean_text(text), text)


if __name__ == "__main__":
    unittest.main()
