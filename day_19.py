from intcode import Machine

from enum import Enum
from threading import Thread
from queue import Queue


## PART 1 ##
program = [
	109, 424, 203, 1, 21101, 11, 0, 0, 1106, 0, 282, 21102, 18, 1, 0, 1106, 0,
	259, 2101, 0, 1, 221, 203, 1, 21101, 31, 0, 0, 1106, 0, 282, 21102, 1, 38, 0,
	1106, 0, 259, 21002, 23, 1, 2, 22102, 1, 1, 3, 21102, 1, 1, 1, 21101, 57, 0,
	0, 1106, 0, 303, 2101, 0, 1, 222, 21002, 221, 1, 3, 21001, 221, 0, 2, 21102,
	259, 1, 1, 21102, 80, 1, 0, 1106, 0, 225, 21102, 1, 79, 2, 21101, 0, 91, 0,
	1106, 0, 303, 2102, 1, 1, 223, 21001, 222, 0, 4, 21102, 259, 1, 3, 21101, 225,
	0, 2, 21102, 1, 225, 1, 21101, 0, 118, 0, 1105, 1, 225, 21002, 222, 1, 3,
	21101, 118, 0, 2, 21101, 0, 133, 0, 1106, 0, 303, 21202, 1, -1, 1, 22001, 223,
	1, 1, 21102, 1, 148, 0, 1105, 1, 259, 1202, 1, 1, 223, 20102, 1, 221, 4,
	20101, 0, 222, 3, 21102, 1, 22, 2, 1001, 132, -2, 224, 1002, 224, 2, 224,
	1001, 224, 3, 224, 1002, 132, -1, 132, 1, 224, 132, 224, 21001, 224, 1, 1,
	21102, 1, 195, 0, 105, 1, 109, 20207, 1, 223, 2, 21002, 23, 1, 1, 21101, -1,
	0, 3, 21102, 214, 1, 0, 1106, 0, 303, 22101, 1, 1, 1, 204, 1, 99, 0, 0, 0, 0,
	109, 5, 2101, 0, -4, 249, 22101, 0, -3, 1, 22102, 1, -2, 2, 21201, -1, 0, 3,
	21101, 0, 250, 0, 1105, 1, 225, 22101, 0, 1, -4, 109, -5, 2105, 1, 0, 109, 3,
	22107, 0, -2, -1, 21202, -1, 2, -1, 21201, -1, -1, -1, 22202, -1, -2, -2, 109,
	-3, 2106, 0, 0, 109, 3, 21207, -2, 0, -1, 1206, -1, 294, 104, 0, 99, 22102, 1,
	-2, -2, 109, -3, 2106, 0, 0, 109, 5, 22207, -3, -4, -1, 1206, -1, 346, 22201,
	-4, -3, -4, 21202, -3, -1, -1, 22201, -4, -1, 2, 21202, 2, -1, -1, 22201, -4,
	-1, 1, 22102, 1, -2, 3, 21102, 343, 1, 0, 1106, 0, 303, 1105, 1, 415, 22207,
	-2, -3, -1, 1206, -1, 387, 22201, -3, -2, -3, 21202, -2, -1, -1, 22201, -3,
	-1, 3, 21202, 3, -1, -1, 22201, -3, -1, 2, 21201, -4, 0, 1, 21102, 384, 1, 0,
	1105, 1, 303, 1106, 0, 415, 21202, -4, -1, -4, 22201, -4, -3, -4, 22202, -3,
	-2, -2, 22202, -2, -4, -4, 22202, -3, -2, -3, 21202, -4, -1, -2, 22201, -3,
	-2, 1, 22101, 0, 1, -4, 109, -5, 2106, 0, 0
]

def main(program: [int] = program) -> int:
	count = 0
	for x in range(50):
		for y in range(50):
			machine = Machine(program.copy(), [x, y])
			res = machine.run()
			if res[0] == 1:
				count += 1
	return count
	

## PART 2 ##
class Result(Enum):
	STATIONARY = 0
	PULLED = 1
	
	def __str__(self) -> str:
		return '#' if self == Result.PULLED else '.'
	
	def __repr__(self) -> str:
		return str(self)
		

def main_2(program: [int] = program) -> int:
	pass


def get_field(program: [int] = program) -> [[Result]]:
	field = []
	for y in range(50):
		field.append([])
		for x in range(50):
			machine = Machine(program.copy(), [x, y], no_output=True)
			res = machine.run()
			field[y].append(Result(res[0]))
	return field
	

def print_field(field: [[Result]]):
	res = ""
	for y in field:
		for x in y:
			res += str(x)
		res += '\n'
	print(res)
	
	
def get_pulled_positions(field: [[Result]]) -> [(int, int)]:
	res = []
	for y in range(len(field)):
		for x in range(len(field[y])):
			if field[y][x] == Result.PULLED:
				res.append((x, y))
	return res


def get_y_diff_between_positions(field: [[Result]]) -> [int]:
	positions = get_pulled_positions(field)
	
	min_y = {}
	max_y = {}
	
	for p in positions:
		x, y = p
		if x not in min_y:
			min_y[x] = y
		
		if x not in max_y:
			max_y[x] = y
		
		if y < min_y[x]:
			min_y[x] = y
			
		elif y > max_y[x]:
			max_y[x] = y
			
	assert len(min_y) == len(max_y)
	res = []
	for x in min_y.keys():
		res.append(max_y[x] - min_y[x])
	return res
