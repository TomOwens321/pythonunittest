import unittest
from primes import is_prime

class PrimesTestCase(unittest.TestCase):
    """tests for primes.py"""
    def test_is_five_prime(self):
        self.assertTrue(is_prime(5))

    def test_is_four_prime(self):
        self.assertFalse(is_prime(4))

if __name__ == '__main__':
    unittest.main()
