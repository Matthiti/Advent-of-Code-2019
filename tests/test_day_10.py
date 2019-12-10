import unittest
import sys

sys.path.append('../')
import intcode
import day_10

class TestDay10(unittest.TestCase):
	
	def test_example_1(self):
		input = ".#..#\n.....\n#####\n....#\n...##"
		asteroid, amount = day_10.get_maximum_detected_asteroids(input)
		self.assertEqual(asteroid, (3, 4))
		self.assertEqual(amount, 8)
		
	def test_example_2(self):
		input = """......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####"""
	
		asteroid, amount = day_10.get_maximum_detected_asteroids(input)
		self.assertEqual(asteroid, (5, 8))
		self.assertEqual(amount, 33)
		
	def test_example_3(self):
		input = """#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###."""

		asteroid, amount = day_10.get_maximum_detected_asteroids(input)
		self.assertEqual(asteroid, (1, 2))
		self.assertEqual(amount, 35)
		
	def test_example_4(self):
		input = """.#..#..###
####.###.#
....###.#.
..###.##.#
##.##.#.#.
....###..#
..#.#..#.#
#..#.#.###
.##...##.#
.....#.#.."""
		
		asteroid, amount = day_10.get_maximum_detected_asteroids(input)
		self.assertEqual(asteroid, (6, 3))
		self.assertEqual(amount, 41)
		
	def test_example_5(self):
		input = """.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##"""

		asteroid, amount = day_10.get_maximum_detected_asteroids(input)
		self.assertEqual(asteroid, (11, 13))
		self.assertEqual(amount, 210)
		
	def test_answer_part_1(self):
		asteroid, amount = day_10.get_maximum_detected_asteroids(day_10.input)
		self.assertEqual(asteroid, (day_10.LASER_LOCATION))
		self.assertEqual(amount, 276)
		
if __name__ == '__main__':
	unittest.main()
