import unittest
import stats as s

class TestStatsMethods(unittest.TestCase):

	def test_compute_avg(self):
		expected = 2.5
		test = s.compute_avg([1,2,3,4])
		self.assertEqual(test, expected)

	def test_compute_min(self):
		expected = 1
		test = s.compute_min([1,2,3,4])
		self.assertEqual(test, expected)

	def test_compute_max(self):
		expected = 4
		test = s.compute_max([1,2,3,4])
		self.assertEqual(test, expected)

if __name__ == '__main__':
	unittest.main()

unittest.main()