## LAST CHANGE: DAY 9 ##
## Has been adapted to support mock input and returns the output ##
from enum import Enum
from queue import Queue


class Opcode(Enum):
	ADD = 1
	MULTIPLY = 2
	INPUT = 3
	OUTPUT = 4
	JUMP_IF_TRUE = 5
	JUMP_IF_FALSE = 6
	LESS_THAN = 7
	EQUALS = 8
	ADJUST_RELATIVE_BASE = 9
	HALT = 99


class ParameterMode(Enum):
	POSITION = 0
	IMMEDIATE = 1
	RELATIVE = 2


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


class Machine(object):
	def __init__(self, program: [int], user_input: [int] = [], q_in: Queue = None, q_out: Queue = None):
		self.program = program
		self.user_input = user_input
		self.q_in = q_in
		self.q_out = q_out
		self.relative_base = 0

	def get_value(self, index: int, mode: ParameterMode) -> int:
		if mode == ParameterMode.POSITION:
			return self.program[index] if index < len(self.program) else 0
		elif mode == ParameterMode.IMMEDIATE:
			return index
		elif mode == ParameterMode.RELATIVE:
			return self.program[self.relative_base + index] if (self.relative_base + index) < len(self.program) else 0
		else:
			raise ValueError('Unknown parameter mode: ' + str(mode))
			
	def set_value(self, index, value, mode: ParameterMode):
		if mode == ParameterMode.IMMEDIATE:
			raise ValueError('Immediate mode not supported for writing')
		elif mode == ParameterMode.RELATIVE:
			index += self.relative_base
		
		while index > len(self.program) - 1:
			self.program.append(0)
		
		self.program[index] = value
			
	def _in(self) -> int:
		if len(self.user_input) > 0:
			res = self.user_input[0]
			del self.user_input[0]
			return res
		
		if self.q_in is not None:
			return self.q_in.get()
			
		return int(input("INPUT: "))
	
	def _out(self, output: int):
		if self.q_out is not None:
			self.q_out.put(output)
		else:
			print("OUTPUT: " + str(output))
		

	# returns (res, true, instruction_pointer) when the program is finished; (res, false, instruction_pointer)  otherwise 
	# amount_of_values is the amount of values it consumed and the caller has to jump #
	# res is the print result, which can be None #
	def execute_instruction(self, index: int) -> (int, int, bool):
		instruction = Instruction.fromInt(self.program[index])
		if instruction.opcode == Opcode.ADD or instruction.opcode == Opcode.MULTIPLY:
			first_value = self.get_value(self.program[index + 1],
																											instruction.get_parameter_mode(0))
			second_value = self.get_value(self.program[index + 2],
																												instruction.get_parameter_mode(1))

			target_index = self.program[index + 3]
			if instruction.opcode == Opcode.ADD:
				self.set_value(target_index, first_value + second_value, instruction.get_parameter_mode(2))
			else:
				self.set_value(target_index, first_value * second_value, instruction.get_parameter_mode(2))
			return None, index + 4, False
		elif instruction.opcode == Opcode.HALT:
			return None, index + 1, True
		elif instruction.opcode == Opcode.INPUT:
			self.set_value(self.program[index + 1], self._in(), instruction.get_parameter_mode(0))
			return None, index + 2, False
		elif instruction.opcode == Opcode.OUTPUT:
			value = self.get_value(self.program[index + 1], instruction.get_parameter_mode(0))
			self._out(value)
			return value, index + 2, False
		elif instruction.opcode == Opcode.JUMP_IF_TRUE or instruction.opcode == Opcode.JUMP_IF_FALSE:
			function = (
				lambda x: x != 0) if instruction.opcode == Opcode.JUMP_IF_TRUE else (
					lambda x: x == 0)
			val = self.get_value(self.program[index + 1], instruction.get_parameter_mode(0))
			if function(val):
				return None, self.get_value(self.program[index + 2],
																											instruction.get_parameter_mode(1)), False
			return None, index + 3, False
		elif instruction.opcode == Opcode.LESS_THAN or instruction.opcode == Opcode.EQUALS:
			function = (
				lambda x, y: x < y) if instruction.opcode == Opcode.LESS_THAN else (
					lambda x, y: x == y)
			val1 = self.get_value(self.program[index + 1], instruction.get_parameter_mode(0))
			val2 = self.get_value(self.program[index + 2], instruction.get_parameter_mode(1))

			if function(val1, val2):
				self.set_value(self.program[index + 3], 1, instruction.get_parameter_mode(2))
			else:
				self.set_value(self.program[index + 3], 0, instruction.get_parameter_mode(2))
			return None, index + 4, False
		elif instruction.opcode == Opcode.ADJUST_RELATIVE_BASE:
			value = self.get_value(self.program[index + 1], instruction.get_parameter_mode(0))
			self.relative_base += value
			return None, index + 2, False
		else:
			raise ValueError('Unknown opcode: ' + str(opcode))

	def run(self):
		i = 0
		done = False
		res = []
		while i < len(self.program) and not done:
			r, i, done = self.execute_instruction(i)
			if r is not None: res.append(r)
		return res

