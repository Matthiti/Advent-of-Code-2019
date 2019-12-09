## PART 1 ##
from enum import Enum

wire1_str = """R994, U598, L555, D997, R997, U529, L251, U533, R640, U120, L813, U927, L908,
	U214, L276, U306, L679, U187, R156, D654, L866, D520, R299, U424, R683, U49,
	R965, U531, R303, D4, L210, U425, R99, D892, R564, D671, L294, D908, L89,
	U855, R275, U790, R214, D588, L754, D873, R297, D97, R979, U850, L953, D281,
	L580, D254, L747, U115, L996, U641, R976, U585, L383, U498, L112, U329, R650,
	U772, L952, U325, L861, U831, R71, D853, R696, D812, R389, U456, L710, D116,
	R789, D829, L57, D940, R908, U569, R617, D832, L492, D397, R152, U898, L960,
	D806, L867, U928, L617, D281, L516, D214, R426, U530, R694, U774, L752, U215,
	L930, U305, R463, U774, R234, U786, R425, U470, R90, D383, R692, D626, L160,
	D588, L141, D351, R574, D237, L869, D499, R873, U856, R148, D919, L582, D804,
	L413, U201, L247, U907, L828, D279, L28, D950, L587, U290, R636, U344, L591,
	U118, L614, U203, R381, U634, L301, D197, R594, D373, L459, U504, L703, U852,
	L672, U613, R816, D712, R813, U97, R824, D690, L556, D308, L568, D924, L384,
	U540, R745, D679, R705, D808, L346, U927, R145, U751, L769, D152, L648, D553,
	L738, U456, R864, U486, R894, D923, R76, U211, L78, U145, R977, U297, R93,
	U200, L71, U665, L392, D309, L399, D594, R118, U552, L328, U317, R369, D109,
	L673, D306, R441, U836, L305, D59, L870, U648, L817, D381, R676, U711, R115,
	U344, L815, U286, R194, U526, R844, U106, L547, D312, L116, U783, R786, D390,
	L115, D483, R691, U802, R569, U13, R854, D90, R22, D819, L440, D13, R438,
	D640, L952, D394, R984, D825, R1, D554, R349, U746, L816, U301, L397, D85,
	R437, D746, L698, D75, L964, U155, L268, U612, R838, D338, L188, U38, R830,
	U538, L245, D885, R194, D989, R8, D69, L268, D677, R163, U784, L308, U605,
	L737, U919, R117, U449, R698, U547, L134, D860, L234, U923, R495, D55, R954,
	D531, L212"""

wire2_str = """L1005, D937, L260, D848, R640, U358, R931, U495, R225, U344, R595, U754, L410,
	D5, R52, D852, L839, D509, R755, D983, R160, U522, R795, D465, R590, U558,
	R552, U332, R330, U752, R860, D503, L456, U254, R878, D164, R991, U569, R44,
	U112, L258, U168, L552, U68, R414, U184, R458, D58, R319, U168, R501, D349,
	R204, D586, R241, U575, L981, D819, L171, D811, L960, U495, R192, D725, R718,
	D346, R399, D692, L117, D215, L390, U364, L700, D207, R372, U767, L738, D844,
	L759, D211, R287, U964, R328, D800, R823, U104, L524, D68, R714, D633, R565,
	D373, R883, U327, R222, D318, L58, D451, R555, D687, R807, U638, L717, U298,
	R849, D489, L159, D692, L136, U242, R884, U202, R419, U41, L980, U483, R966,
	D513, L870, D306, R171, D585, R71, D320, R914, U991, R706, U440, R542, D219,
	L969, U9, R481, U164, R919, U17, L750, U775, R173, U515, L191, D548, L515,
	U54, L132, U56, R203, U544, L796, D508, L321, D517, L358, U12, L892, D472,
	L378, U121, L974, U36, R56, D758, L680, D17, L369, D72, L926, D466, L866,
	U850, R300, D597, L848, U17, L890, D739, L275, U560, L640, U602, R238, U919,
	R636, D188, R910, D992, L13, U241, R77, U857, R453, U883, L881, D267, R28,
	U928, R735, U731, L701, D795, R371, U652, R416, D129, R142, D30, R442, U513,
	R827, U455, L429, D804, R966, D565, R326, U398, R621, U324, L684, D235, L467,
	D575, L200, D442, R320, D550, R278, U929, R555, U537, L416, U98, R991, D271,
	L764, U841, L273, D782, R356, D447, R340, U413, R543, U260, L365, D529, R721,
	U542, L648, U366, R494, U243, L872, U201, L440, U232, R171, D608, R282, U484,
	R81, D320, R274, D760, L250, U749, L132, D162, L340, D308, L149, D5, L312,
	U547, R686, D684, R133, D876, L531, U572, R62, D142, L218, U703, L884, U64,
	L889, U887, R228, U534, R624, D524, R522, D452, L550, U959, R981, U139, R35,
	U98, R212"""

wire1 = wire1_str.replace("\n", "").replace("\t", "").replace(" ",
																																																														"").split(",")
wire2 = wire2_str.replace("\n", "").replace("\t", "").replace(" ",
																																																														"").split(",")


class Direction(Enum):
	LEFT = "L"
	RIGHT = "R"
	UP = "U"
	DOWN = "D"


class Instruction(object):
	def __init__(self, direction: Direction, steps: int):
		self.direction = direction
		self.steps = steps

	@staticmethod
	def fromString(instruction: str):
		direction = Direction(instruction[0])
		steps = int(instruction[1:])
		return Instruction(direction, steps)


def get_points_of_wire(wire: [str]) -> [(int, int)]:
	points = []
	pos = (0, 0)
	for instr in wire:
		instruction = Instruction.fromString(instr)
		pos, res = get_points(pos, instruction)
		points += res
	return points


def find_intersections() -> [(int, int)]:
	points_wire_1 = get_points_of_wire(wire1)
	points_wire_2 = get_points_of_wire(wire2)

	intersections = list(set(points_wire_1).intersection(points_wire_2))
	return intersections


def find_closest_intersection() -> int:
	intersections = find_intersections()
	min_dist = manhatten_distance(intersections[0])
	for i in range(1, len(intersections)):
		dist = manhatten_distance(intersections[i])
		if dist < min_dist:
			min_dist = dist
	return min_dist


def get_direction_function(direction: Direction):
	if direction == Direction.LEFT:
		return lambda x: (x[0] - 1, x[1])
	elif direction == Direction.RIGHT:
		return lambda x: (x[0] + 1, x[1])
	elif direction == Direction.UP:
		return lambda x: (x[0], x[1] + 1)
	else:
		return lambda x: (x[0], x[1] - 1)


def get_points(pos: (int, int),
															instruction: Instruction) -> ((int, int), [(int, int)]):
	function = get_direction_function(instruction.direction)
	result = []
	for i in range(instruction.steps):
		pos = function(pos)
		result.append(pos)
	return pos, result


def manhatten_distance(x: (int, int)) -> int:
	return abs(x[0]) + abs(x[1])


#if __name__ == '__main__':
#	print(find_closest_intersection())


## PART 2 ##
def get_steps_until_point(wire: [str], point: (int, int)) -> int:
	points = get_points_of_wire(wire)
	return points.index(point) + 1


def find_least_steps_to_intersection() -> int:
	intersections = find_intersections()
	distances = []
	for intersection in intersections:
		steps_wire_1 = get_steps_until_point(wire1, intersection)
		steps_wire_2 = get_steps_until_point(wire2, intersection)
		distances.append(steps_wire_1 + steps_wire_2)
	return min(distances)


if __name__ == '__main__':
	print(find_least_steps_to_intersection())

