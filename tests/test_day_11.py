import unittest
import sys

sys.path.append('../')
import day_11

class TestDay11(unittest.TestCase):
	
	def test_input_part_1(self):
		res = day_11.get_painted_panels_amount(day_11.input)
		self.assertEqual(res, 2129)
		
if __name__ == '__main__':
	unittest.main()
