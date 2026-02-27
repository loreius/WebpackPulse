# test_webpackpulse.py
"""
Tests for WebpackPulse module.
"""

import unittest
from webpackpulse import WebpackPulse

class TestWebpackPulse(unittest.TestCase):
    """Test cases for WebpackPulse class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = WebpackPulse()
        self.assertIsInstance(instance, WebpackPulse)
        
    def test_run_method(self):
        """Test the run method."""
        instance = WebpackPulse()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
