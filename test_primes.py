import unittest
from unittest.mock import patch
from primes import is_prime, next_prime

class PrimesTestCase(unittest.TestCase):
    """tests for primes.py"""
    def test_is_five_prime(self):
        self.assertTrue(is_prime(5))

    def test_is_four_prime(self):
        self.assertFalse(is_prime(4))

    def test_three_primes(self):
        numbers = [3,5,7]
        for number in numbers:
            self.assertTrue(is_prime(number))

    def test_is_zero_not_prime(self):
        self.assertFalse(is_prime(0), msg='Zero is not prime.')

    def test_are_negatives_not_prime(self):
        for index in range(-1, -10, -1):
            self.assertFalse(is_prime(index), msg='{} should not be prime'.format(index))

    @patch('primes.is_prime', return_value = 5)
    def test_next_prime(self, is_prime):
        number = 5
        next_prime(5)
        is_prime.assert_called_once_with(number)

if __name__ == '__main__':
    unittest.main()
