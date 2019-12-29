import unittest
import sys

sys.path.append('../')
import day_24

class TestDay24(unittest.TestCase):

  def test_biodiversity_rating(self):
    field = day_24.parse_field(""".....
.....
.....
#....
.#...""")

    self.assertEqual(day_24.biodiversity_rating(field), 2129920)
		
if __name__ == '__main__':
	unittest.main()