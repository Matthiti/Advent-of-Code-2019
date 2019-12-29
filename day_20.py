from enum import Enum

## PART 1 ##

input = """
         A           
         A           
  #######.#########  
  #######.........#  
  #######.#######.#  
  #######.#######.#  
  #######.#######.#  
  #####  B    ###.#  
BC...##  C    ###.#  
  ##.##       ###.#  
  ##...DE  F  ###.#  
  #####    G  ###.#  
  #########.#####.#  
DE..#######...###.#  
  #.#########.###.#  
FG..#########.....#  
  ###########.#####  
             Z       
             Z   
"""


class MapObjectType(Enum):
	WALL = 0
	OPEN_PASSAGE = 1
	PORTAL = 2


class MapObject(object):
	def __init__(self, type: MapObjectType, value: str=None):
		self.type = type
		self.value = value
		
	def __str__(self) -> str:
		if self.type == MapObjectType.WALL:
			return '#'
		elif self.type == MapObjectType.OPEN_PASSAGE:
			return '.'
		else:
			return self.value[0] # Return only first value, since there will be a problem with printing otherwise.
		
	@staticmethod
	def parse(string: str) -> 'MapObject':
		if string == '#':
			return MapObject(MapObjectType.WALL)
		elif string == '.':
			return MapObject(MapObjectType.OPEN_PASSAGE)
		else:
			return MapObject(MapObjectType.PORTAL, string)


def parse_input(input: str) -> {(int, int): MapObject}:
	input_split = input.split('\n')
	res = {}
	for y in range(len(input_split)):
		line = input_split[y]
		for x in range(len(line)):
			val = line[x]
			if x == ' ': continue  # continue if the field is empty
			if x.isalpha():
				# If this is part of a portal, check if there is also on to the right or down.
				# check to the right:
					if len(line) < x + 1 and line[x+1].isalpha():
						o = MapObject.parse(val + line[x+1])
						res[(x, y)] = o
						res[(x+1, y)] = o
					
					if len(input_split) < y + 1 and input_split[y+1][x].isalpha():
						o = MapObject.parse(val + input_split[y+1][x])
						res[(x, y)] = o
						res[(x, y+1)] = o
			else:
				res[(x, y)] = MapObject.parse(val)
	return res
				

def main(input: str = input) -> int:
	
