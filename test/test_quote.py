import unittest
from app.requests import get_blogQuotes

class TestQuote(unittest.TestCase):
    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.random_quote = get_blogQuotes("Sam Martin", "Hello World")

    def test_instance(self):
        self.assertTrue(isinstance(self.random_quote, get_blogQuotes))

    def test_init(self):
        self.assertEqual(self.random_quote.author, "Sam Martin")
        self.assertEqual(self.random_quote.quote,"Hello World")