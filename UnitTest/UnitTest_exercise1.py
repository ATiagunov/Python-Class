import unittest
import numpy as np


def positive(x):
	return x > 0


def array(x):
	return np.arange(x)


def random(x, y):
	return np.random.randint(x, size=y)


def subtract(a, b):
	c = a - b
	return c


class TestNumberMethods(unittest.TestCase):
	def tests(self):
		self.assertTrue(positive(2))
		self.assertFalse(positive(-2))
		self.assertIn(5, array(10))
		self.assertNotIn(10, array(10))
		self.assertGreater(subtract(8, 2), 4)
		self.assertLess(subtract(8, 2), 10)
		self.assertCountEqual(random(3, 3), [1, 2, 3])


if __name__ == '__main__':
	unittest.main()
