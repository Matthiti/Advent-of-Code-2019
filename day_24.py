from enum import Enum

## PART 1 ##
field = """.#..#
.#.#.
#..##
.#.##
##..#"""


class FieldObject(Enum):
	BUG = '#'
	OPEN_SPACE = '.'

	def __str__(self):
		return self.value

	def __repr__(self):
		return str(self)


def parse_field(field: str) -> {(int, int): FieldObject}:
	result = {}
	rows = field.split('\n')
	for y in range(len(rows)):
		for x in range(len(rows[y])):
			result[(x, y)] = FieldObject(rows[y][x])
	return result


def get_adjacent_bugs(pos: (int, int), field: {(int, int):
																																															FieldObject}) -> int:
	result = 0
	x, y = pos
	positions = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
	for p in positions:
		if p in field and field[p] == FieldObject.BUG: result += 1
	return result


def update_bugs(field: {(int, int): FieldObject}) -> {(int, int): FieldObject}:
	new_field = {}
	for pos, o in field.items():
		adjacent_bugs = get_adjacent_bugs(pos, field)
		if o == FieldObject.OPEN_SPACE and (adjacent_bugs == 1 or
																																						adjacent_bugs == 2):
			new_field[(pos)] = FieldObject.BUG
		elif o == FieldObject.BUG and adjacent_bugs == 1:
			new_field[(pos)] = FieldObject.BUG
		else:
			new_field[(pos)] = FieldObject.OPEN_SPACE
	return new_field


def biodiversity_rating(field: {(int, int): FieldObject}) -> int:
	result = 0
	for pos, o in field.items():
		if o == FieldObject.BUG:
			x, y = pos
			result += 2**(y * 5 + x)
	return result


def main(field_str: str) -> int:
	field = parse_field(field_str)
	fields = []

	while field not in fields:
		fields.append(field.copy())
		field = update_bugs(field)

	return biodiversity_rating(field)


if __name__ == '__main__':
	print(main(field))

