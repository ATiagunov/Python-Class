import unittest
import os


class MorphologyTests(unittest.TestCase):
	def tests(self):
		self.assertTrue(os.path.exists('/home/alexander/PycharmProjects/python_practice/XML/annot.opcorpora.no_ambig.xml'))


if __name__ == '__main__':
	unittest.main()
