import unittest
import sys

sys.path.append('../')
import day_13

class TestDay13(unittest.TestCase):
		
	def test_answer_part_1(self):
		res = day_13.main()
		self.assertEqual(res, 398)
		
	def test_answer_part_2(self):
		res = day_13.play(day_13.program, True, False)
		self.assertEqual(res, 19447)
		
if __name__ == '__main__':
	unittest.main()
