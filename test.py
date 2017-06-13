import unittest
from prime import is_prime

class TestPrimeFunction(unittest.TestCase):

	def test_zero_to_ten(self):
		#To check for the prime numbers between one and ten.
		numbers = is_prime(10)
		self.assertEqual(numbers, [2,3,5,7])

	def test_n_is_zero(self):


		with self.assertRaises(ValueError) as context:
			is_prime(0)

		self.assertTrue("There is no prime number less that 2", context.exception)

	def test_n_is_2(self):
		self.assertEqual(is_prime(2), [2])

	def test_n_is_not_integer(self):		

		with self.assertRaises(ValueError) as context:
			is_prime("number")

		self.assertTrue("Input should be a number", context.exception)

	def test_is_one(self):
		with self.assertRaises(ValueError) as context:
			is_prime(1)

		self.assertTrue("There is no prime number less that 2", context.exception)

		


if __name__ == '__main__':
	unittest.main()
