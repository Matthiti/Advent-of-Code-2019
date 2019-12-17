import unittest
import sys

sys.path.append('../')
import day_14

class TestDay14(unittest.TestCase):
	
	def test_example_1(self):
		input = """10 ORE => 10 A
1 ORE => 1 B
7 A, 1 B => 1 C
7 A, 1 C => 1 D
7 A, 1 D => 1 E
7 A, 1 E => 1 FUEL"""
		res = day_14.main(input)
		self.assertEqual(res, 31)
		
	def test_example_2(self):
		input = """9 ORE => 2 A
8 ORE => 3 B
7 ORE => 5 C
3 A, 4 B => 1 AB
5 B, 7 C => 1 BC
4 C, 1 A => 1 CA
2 AB, 3 BC, 4 CA => 1 FUEL"""
		res = day_14.main(input)
		self.assertEqual(res, 165)
		
if __name__ == '__main__':
	unittest.main()
