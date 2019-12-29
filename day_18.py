from enum import Enum
import copy

## PART 1 ##

input = """#########
#b.A.@.a#
#########"""


class ObjectType(Enum):
	POSITION = 0
	OPEN_PASSAGE = 1
	STONE_WALL = 2
	KEY = 3
	DOOR = 4


class Object(object):
	
	def __init__(self, type: ObjectType, value: str = ''):
		self.type = type
		self.value = value
	
	def __str__(self) -> str:
		if self.type == ObjectType.POSITION:
			return '@'
		elif self.type == ObjectType.OPEN_PASSAGE:
			return '.'
		elif self.type == ObjectType.STONE_WALL:
			return '#'
		else:
			return self.value
			
	def __repr__(self) -> str:
		return str(self)
		
	def __eq__(self, other) -> bool:
		return self.type == other.type and self.value == other.value
		
	@staticmethod
	def parse(string) -> 'Object':
		if string == '@':
			return Object(ObjectType.POSITION)
		elif string == '.':
			return Object(ObjectType.OPEN_PASSAGE)
		elif string == '#':
			return Object(ObjectType.STONE_WALL)
		elif string.islower():
			return Object(ObjectType.KEY, string)
		elif string.isupper():
			return Object(ObjectType.DOOR, string)
		else:
			raise ValueError("Unknown object: %s" % string)
	

def get_field(input: str) -> [[Object]]:
	input_split = input.split('\n')
	res = []
	for i in input_split:
		res.append([])
		for j in i:
			res[-1].append(Object.parse(j))
	return res


def get_fields_around(pos: (x, y), field: [[Object]]) -> [(x, y)]:
	return [field[y][x-1], field[y][x+1], field[y-1][x], field[y+1][x]]	
	

def get_accessible_keys(pos: (x, y), field: [[Object]]) -> [(x, y)]:
	res = []
	for (x, y) in get_fields_around(pos, field):
		o = field[y][x]
		if o.type == ObjectType.KEY:
			res.append(o)
		elif o.type == ObjectType.OPEN_PASSAGE:
			res += get_accessible_keys((x, y), field)
	return res
	

def get_current_position(field: [[Object]]) -> 
	
def main(input: str = input) -> int:
	
