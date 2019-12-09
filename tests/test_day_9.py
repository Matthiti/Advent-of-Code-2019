import unittest
import sys

sys.path.append('../')
import intcode
import day_9

class TestDay9(unittest.TestCase):
	
	def test_example_1(self):
		program = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
		machine = intcode.Machine(program.copy())
		res = machine.run()
		self.assertEqual(res, program, "It should output a copy of the program")
		
	def test_example_2(self):
		program = [1102,34915192,34915192,7,4,7,99,0]
		machine = intcode.Machine(program.copy())
		res = machine.run()
		self.assertEqual(len(str(res[0])), 16, "It should output a 16-digit number")
		
	def test_example_3(self):
		program = [104,1125899906842624,99]
		machine = intcode.Machine(program.copy())
		res = machine.run()
		self.assertEqual(res[0], program[1], "It should output the middle number")
		
	def test_answer_part_1(self):
		self.assertEqual(day_9.main(), 4006117640)
		
	def test_answer_part_2(self):
		self.assertEqual(day_9.main_2(), 88231)
		
if __name__ == '__main__':
	unittest.main()
