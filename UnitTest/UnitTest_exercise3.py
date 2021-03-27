import unittest
import os,shutil


def new_directory(path):
	try:
		os.makedirs(path)
	except FileExistsError:
		pass
	os.chdir(path)
	with open("sonnet.txt", "w") as file:
		file.write("From fairest creatures we desire increase")


class SimpleWidgetTestCase(unittest.TestCase):
	def setUp(self):
		self.widget = new_directory('/home/alexander/Desktop/test_folder')
	def tests(self):
		self.assertTrue(os.path.getsize('/home/alexander/Desktop/test_folder') != 0)
		self.assertFalse(os.path.getsize('/home/alexander/Desktop/test_folder') == 0)
		with open("sonnet.txt") as f:
			self.assertSequenceEqual(f.read(), "From fairest creatures we desire increase")
	def tearDown(self):
		shutil.rmtree('/home/alexander/Desktop/test_folder')

if __name__ == '__main__':
	unittest.main()

