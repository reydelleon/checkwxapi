"""Tests for the CheckWXAPI library"""
from checkwxapi import CheckWXAPI, InvalidApiKeyError
import unittest


class TestCheckWXAPI(unittest.TestCase):
    
    def TestCheckWXAPI(self):
      """Test that we can instantiate the client"""
      with self.assertRaises(InvalidApiKeyError):
          client = CheckWXAPI()
    
    if __name__ == '__main__':
        unittest.main()
