import unittest
import time
from prime import is_prime

class TestPrimeFunction(unittest.TestCase):

	def test_zero_to_ten(self):
		numbers = is_prime(10)
		self.assertEqual(numbers, [2,3,5,7])

if __name__ == '__main__':
	unittest.main()
