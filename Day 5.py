## PART 1 & 2 ##
from enum import Enum

program = [
	3, 225, 1, 225, 6, 6, 1100, 1, 238, 225, 104, 0, 1102, 88, 66, 225, 101, 8,
	125, 224, 101, -88, 224, 224, 4, 224, 1002, 223, 8, 223, 101, 2, 224, 224, 1,
	224, 223, 223, 1101, 87, 23, 225, 1102, 17, 10, 224, 101, -170, 224, 224, 4,
	224, 102, 8, 223, 223, 101, 3, 224, 224, 1, 223, 224, 223, 1101, 9, 65, 225,
	1101, 57, 74, 225, 1101, 66, 73, 225, 1101, 22, 37, 224, 101, -59, 224, 224,
	4, 224, 102, 8, 223, 223, 1001, 224, 1, 224, 1, 223, 224, 223, 1102, 79, 64,
	225, 1001, 130, 82, 224, 101, -113, 224, 224, 4, 224, 102, 8, 223, 223, 1001,
	224, 7, 224, 1, 223, 224, 223, 1102, 80, 17, 225, 1101, 32, 31, 225, 1, 65,
	40, 224, 1001, 224, -32, 224, 4, 224, 102, 8, 223, 223, 1001, 224, 4, 224, 1,
	224, 223, 223, 2, 99, 69, 224, 1001, 224, -4503, 224, 4, 224, 102, 8, 223,
	223, 101, 6, 224, 224, 1, 223, 224, 223, 1002, 14, 92, 224, 1001, 224, -6072,
	224, 4, 224, 102, 8, 223, 223, 101, 5, 224, 224, 1, 223, 224, 223, 102, 33,
	74, 224, 1001, 224, -2409, 224, 4, 224, 1002, 223, 8, 223, 101, 7, 224, 224,
	1, 223, 224, 223, 4, 223, 99, 0, 0, 0, 677, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
	1105, 0, 99999, 1105, 227, 247, 1105, 1, 99999, 1005, 227, 99999, 1005, 0,
	256, 1105, 1, 99999, 1106, 227, 99999, 1106, 0, 265, 1105, 1, 99999, 1006, 0,
	99999, 1006, 227, 274, 1105, 1, 99999, 1105, 1, 280, 1105, 1, 99999, 1, 225,
	225, 225, 1101, 294, 0, 0, 105, 1, 0, 1105, 1, 99999, 1106, 0, 300, 1105, 1,
	99999, 1, 225, 225, 225, 1101, 314, 0, 0, 106, 0, 0, 1105, 1, 99999, 107, 677,
	677, 224, 1002, 223, 2, 223, 1006, 224, 329, 101, 1, 223, 223, 108, 677, 677,
	224, 1002, 223, 2, 223, 1005, 224, 344, 101, 1, 223, 223, 1007, 677, 677, 224,
	1002, 223, 2, 223, 1006, 224, 359, 101, 1, 223, 223, 1107, 226, 677, 224,
	1002, 223, 2, 223, 1006, 224, 374, 1001, 223, 1, 223, 8, 677, 226, 224, 1002,
	223, 2, 223, 1006, 224, 389, 101, 1, 223, 223, 1108, 677, 677, 224, 1002, 223,
	2, 223, 1005, 224, 404, 1001, 223, 1, 223, 7, 226, 226, 224, 1002, 223, 2,
	223, 1006, 224, 419, 101, 1, 223, 223, 1107, 677, 677, 224, 1002, 223, 2, 223,
	1005, 224, 434, 101, 1, 223, 223, 107, 226, 226, 224, 102, 2, 223, 223, 1005,
	224, 449, 101, 1, 223, 223, 107, 677, 226, 224, 1002, 223, 2, 223, 1006, 224,
	464, 1001, 223, 1, 223, 8, 226, 677, 224, 102, 2, 223, 223, 1006, 224, 479,
	1001, 223, 1, 223, 108, 677, 226, 224, 102, 2, 223, 223, 1005, 224, 494, 1001,
	223, 1, 223, 1108, 677, 226, 224, 1002, 223, 2, 223, 1005, 224, 509, 1001,
	223, 1, 223, 1107, 677, 226, 224, 1002, 223, 2, 223, 1005, 224, 524, 101, 1,
	223, 223, 1008, 226, 226, 224, 1002, 223, 2, 223, 1006, 224, 539, 101, 1, 223,
	223, 1008, 226, 677, 224, 1002, 223, 2, 223, 1005, 224, 554, 1001, 223, 1,
	223, 7, 226, 677, 224, 1002, 223, 2, 223, 1005, 224, 569, 101, 1, 223, 223,
	1007, 677, 226, 224, 1002, 223, 2, 223, 1006, 224, 584, 1001, 223, 1, 223, 7,
	677, 226, 224, 102, 2, 223, 223, 1006, 224, 599, 101, 1, 223, 223, 1007, 226,
	226, 224, 102, 2, 223, 223, 1006, 224, 614, 101, 1, 223, 223, 1008, 677, 677,
	224, 1002, 223, 2, 223, 1006, 224, 629, 101, 1, 223, 223, 108, 226, 226, 224,
	102, 2, 223, 223, 1006, 224, 644, 101, 1, 223, 223, 1108, 226, 677, 224, 1002,
	223, 2, 223, 1005, 224, 659, 101, 1, 223, 223, 8, 226, 226, 224, 1002, 223, 2,
	223, 1005, 224, 674, 101, 1, 223, 223, 4, 223, 99, 226
]


class Opcode(Enum):
	ADD = 1
	MULTIPLY = 2
	INPUT = 3
	OUTPUT = 4
	JUMP_IF_TRUE = 5
	JUMP_IF_FALSE = 6
	LESS_THAN = 7
	EQUALS = 8
	HALT = 99


class ParameterMode(Enum):
	POSITION = 0
	IMMEDIATE = 1


class Instruction(object):
	def __init__(self, opcode: Opcode, parameter_modes: [ParameterMode]):
		self.opcode = opcode
		self.parameter_modes = parameter_modes

	@staticmethod
	def fromInt(number: int):
		opcode = Opcode(number % 100)
		string = str(number)
		modes = [int(d) for d in str(number // 100)][::-1]
		parameter_modes = []
		for i in range(0, len(modes)):
			parameter_modes.append(ParameterMode(modes[i]))
		return Instruction(opcode, parameter_modes)

	def get_parameter_mode(self, index: int) -> ParameterMode:
		if index >= len(self.parameter_modes):
			return ParameterMode.POSITION
		return self.parameter_modes[index]


def get_value(index: int, mode: ParameterMode) -> int:
	if mode == ParameterMode.POSITION:
		return program[index]
	elif mode == ParameterMode.IMMEDIATE:
		return index
	else:
		raise ValueError('Unknown parameter mode: ' + str(mode))


# returns (true, instruction_pointer) when the program is finished; (false, instruction_pointer) otherwise #
# amount_of_values is the amount of values it consumed and the caller has to jump #
def execute_instruction(index: int) -> (int, bool):
	instruction = Instruction.fromInt(program[index])
	if instruction.opcode == Opcode.ADD or instruction.opcode == Opcode.MULTIPLY:
		first_value = get_value(program[index + 1],
																										instruction.get_parameter_mode(0))
		second_value = get_value(program[index + 2],
																											instruction.get_parameter_mode(1))

		target_index = program[index + 3]
		if instruction.opcode == Opcode.ADD:
			program[target_index] = first_value + second_value
		else:
			program[target_index] = first_value * second_value
		return index + 4, False
	elif instruction.opcode == Opcode.HALT:
		return index + 1, True
	elif instruction.opcode == Opcode.INPUT:
		value = int(input("INPUT: "))
		program[program[index + 1]] = value
		return index + 2, False
	elif instruction.opcode == Opcode.OUTPUT:
		value = get_value(program[index + 1], instruction.get_parameter_mode(0))
		print("OUTPUT: " + str(value))
		return index + 2, False
	elif instruction.opcode == Opcode.JUMP_IF_TRUE or instruction.opcode == Opcode.JUMP_IF_FALSE:
		function = (
			lambda x: x != 0) if instruction.opcode == Opcode.JUMP_IF_TRUE else (
				lambda x: x == 0)
		val = get_value(program[index + 1], instruction.get_parameter_mode(0))
		if function(val):
			return get_value(program[index + 2],
																				instruction.get_parameter_mode(1)), False
		return index + 3, False
	elif instruction.opcode == Opcode.LESS_THAN or instruction.opcode == Opcode.EQUALS:
		function = (
			lambda x, y: x < y) if instruction.opcode == Opcode.LESS_THAN else (
				lambda x, y: x == y)
		val1 = get_value(program[index + 1], instruction.get_parameter_mode(0))
		val2 = get_value(program[index + 2], instruction.get_parameter_mode(1))

		if function(val1, val2):
			program[program[index + 3]] = 1
		else:
			program[program[index + 3]] = 0
		return index + 4, False
	else:
		raise ValueError('Unknown opcode: ' + str(opcode))


def run_program():
	i = 0
	done = False
	while i < len(program) and not done:
		i, done = execute_instruction(i)


if __name__ == '__main__':
	run_program()

