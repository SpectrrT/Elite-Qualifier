import unittest
import main

class TestLoad_Words(unittest.TestCase):
  
    def test_load_Words(self):
      self.assertTrue(main.load_words())

class TestSuggest(unittest.TestCase):
  
    def test_suggest(self):
      self.assertTrue(main.suggest)     