import unittest
import numpy as np


def random_10(n):
	return np.random.randint(2, size=n)


class TestNumberMethods(unittest.TestCase):
	def tests(self):
		for i in random_10(10):
			with self.subTest(i=i):
				self.assertTrue(i >= 0.5)


if __name__ == '__main__':
	unittest.main()
