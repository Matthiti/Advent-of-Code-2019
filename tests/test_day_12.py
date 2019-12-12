import unittest
import sys

sys.path.append('../')
import day_12

class TestDay12(unittest.TestCase):
		
	def test_answer_part_1(self):
		res = day_12.main()
		self.assertEqual(res, 7988)
		
	def test_example_1_part_2(self):
		input = [[-1, 0, 2], [2, -10, -7], [4, -8, 8], [3, 5, -1]]
		res = day_12.main_2(input)
		self.assertEqual(res, 2772)
	
	def test_example_2_part_2(self):
		input = [[-8, -10, 0], [5, 5, 10], [2, -7, 3], [9, -8, -3]]
		res = day_12.main_2(input)
		self.assertEqual(res, 4686774924)
		
	def test_answer_part_2(self):
		res = day_12.main_2()
		self.assertEqual(res, 337721412394184)
		
if __name__ == '__main__':
	unittest.main()
