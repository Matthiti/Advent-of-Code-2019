## PART 1 ##
from enum import Enum

program = [
	1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 1, 10, 19, 1, 6, 19, 23, 1,
	13, 23, 27, 1, 6, 27, 31, 1, 31, 10, 35, 1, 35, 6, 39, 1, 39, 13, 43, 2, 10,
	43, 47, 1, 47, 6, 51, 2, 6, 51, 55, 1, 5, 55, 59, 2, 13, 59, 63, 2, 63, 9, 67,
	1, 5, 67, 71, 2, 13, 71, 75, 1, 75, 5, 79, 1, 10, 79, 83, 2, 6, 83, 87, 2, 13,
	87, 91, 1, 9, 91, 95, 1, 9, 95, 99, 2, 99, 9, 103, 1, 5, 103, 107, 2, 9, 107,
	111, 1, 5, 111, 115, 1, 115, 2, 119, 1, 9, 119, 0, 99, 2, 0, 14, 0
]


class Opcode(Enum):
	ADD = 1
	MULTIPLY = 2
	HALT = 99


# returns true when the program is finished; false otherwise #
def execute_instruction(index: int) -> bool:
	opcode = Opcode(program[index])
	if opcode == Opcode.ADD or opcode == Opcode.MULTIPLY:
		first_index = program[index + 1]
		first_value = program[first_index]

		second_index = program[index + 2]
		second_value = program[second_index]

		target_index = program[index + 3]
		if opcode == Opcode.ADD:
			program[target_index] = first_value + second_value
		else:
			program[target_index] = first_value * second_value
	elif opcode == Opcode.HALT:
		return True
	else:
		raise ValueError('Unknown opcode: ' + str(opcode))
	return False


def run_program():
	i = 0
	while i < len(program) and not execute_instruction(i):
		i += 4


#if __name__ == '__main__':
#	program[1] = 12
#	program[2] = 2
#	run_program()
# print(program)

## PART 2 ##

# answer is 86 and 9
def run_program_with_input(noun: int, verb: int) -> int:
	global program
	program_copy = program.copy()
	program[1] = noun
	program[2] = verb
	run_program()
	result = program[0]
	program = program_copy
	return result

if __name__ == '__main__':
	print(run_program(86, 9))
