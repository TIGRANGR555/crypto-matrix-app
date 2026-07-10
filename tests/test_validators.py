"""
Unit tests for validators module
"""

import unittest
from utils.validators import is_valid_email, is_valid_hex, is_non_empty


class TestValidators(unittest.TestCase):
    """Test validator functions"""
    
    def test_is_valid_email(self):
        """Test email validation"""
        self.assertTrue(is_valid_email("user@example.com"))
        self.assertTrue(is_valid_email("test.name@domain.co.uk"))
        self.assertFalse(is_valid_email("invalid@"))
        self.assertFalse(is_valid_email("invalid"))
    
    def test_is_valid_hex(self):
        """Test hex validation"""
        self.assertTrue(is_valid_hex("FF"))
        self.assertTrue(is_valid_hex("1A2B3C"))
        self.assertFalse(is_valid_hex("GGGG"))
        self.assertFalse(is_valid_hex(""))
    
    def test_is_non_empty(self):
        """Test non-empty validation"""
        self.assertTrue(is_non_empty("text"))
        self.assertFalse(is_non_empty(""))
        self.assertFalse(is_non_empty("   "))


if __name__ == "__main__":
    unittest.main()
