import unittest
import sys

sys.path.append('../')
import day_16

class TestDay16(unittest.TestCase):
	
	def test_example_1(self):
		input = "80871224585914546619083218645595"
		res = day_16.main(input)
		self.assertEqual(res, 24176176)
		
	def test_example_2(self):
		input = "19617804207202209144916044189917"
		res = day_16.main(input)
		self.assertEqual(res, 73745418)
	
	def test_example_3(self):
		input = "69317163492948606335995924319873"
		res = day_16.main(input)
		self.assertEqual(res, 52432133)
		
	def test_answer_part_1(self):
		res = day_16.main()
		self.assertEqual(res, 19944447)
		
if __name__ == '__main__':
	unittest.main()
