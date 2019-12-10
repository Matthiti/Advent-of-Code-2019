## PART 1 ##

input = """.#..#..#..#...#..#...###....##.#....
.#.........#.#....#...........####.#
#..##.##.#....#...#.#....#..........
......###..#.#...............#.....#
......#......#....#..##....##.......
....................#..............#
..#....##...#.....#..#..........#..#
..#.#.....#..#..#..#.#....#.###.##.#
.........##.#..#.......#.........#..
.##..#..##....#.#...#.#.####.....#..
.##....#.#....#.......#......##....#
..#...#.#...##......#####..#......#.
##..#...#.....#...###..#..........#.
......##..#.##..#.....#.......##..#.
#..##..#..#.....#.#.####........#.#.
#......#..........###...#..#....##..
.......#...#....#.##.#..##......#...
.............##.......#.#.#..#...##.
..#..##...#...............#..#......
##....#...#.#....#..#.....##..##....
.#...##...........#..#..............
.............#....###...#.##....#.#.
#..#.#..#...#....#.....#............
....#.###....##....##...............
....#..........#..#..#.......#.#....
#..#....##.....#............#..#....
...##.............#...#.....#..###..
...#.......#........###.##..#..##.##
.#.##.#...##..#.#........#.....#....
#......#....#......#....###.#.....#.
......#.##......#...#.#.##.##...#...
..#...#.#........#....#...........#.
......#.##..#..#.....#......##..#...
..##.........#......#..##.#.#.......
.#....#..#....###..#....##..........
..............#....##...#.####...##."""

'''
input = """.##.#
.....
#####
....#
#.###"""
'''

def get_asteroids(input: str) -> [(int, int)]:
	map = input.split("\n")
	asteroids = []
	for y in range(len(map)):
		for x in range(len(map[y])):
			if map[y][x] == '#':
				asteroids.append((x, y))
	return asteroids


def get_detected_asteroids(asteroid: (int, int), asteroids: [(int,
																																																														int)]) -> int:
	result = 0
	for other in asteroids:
		if other == asteroid:
			continue
		if is_asteroid_detectable(asteroid, other, asteroids): result += 1
	return result


def is_asteroid_detectable(fromAsteroid: (int, int),
																											toAsteroid: (int, int),
																											otherAsteroids: [(int, int)]) -> bool:
	diff_x = toAsteroid[0] - fromAsteroid[0]
	diff_y = toAsteroid[1] - fromAsteroid[1]

	res = abs(gcd(diff_x, diff_y))
	if res == 1:
		return True

	def is_in_pattern(asteroid: (int, int)) -> bool:
		x, y = (fromAsteroid[0], fromAsteroid[1])
		x_step = diff_x // res
		y_step = diff_y // res
		
		while True:
			x += x_step
			y += y_step

			if asteroid == (x, y):
				return True
			elif toAsteroid == (x, y):
				return False

	for o in otherAsteroids:
		if o == fromAsteroid or o == toAsteroid: continue

		if is_in_pattern(o):
			return False

	return True


def gcd(a: int, b: int) -> int:
	if b == 0: return a
	return gcd(b, a % b)


def get_maximum_detected_asteroids(input) -> ((int, int), int):
	asteroids = get_asteroids(input)
	max_val = 0
	best_asteroid = None
	
	for a in asteroids:
		res = get_detected_asteroids(a, asteroids)
		if res > max_val:
			max_val = res
			best_asteroid = a
	return (best_asteroid, max_val)


#if __name__ == '__main__':
	#res = is_asteroid_detectable((4, 2), (5, 2), get_asteroids(input))
	#print(res)
	#print(get_maximum_detected_asteroids(input))

## PART 2 ##
import math
import functools
import collections

LASER_LOCATION = (17, 22) # Calculated
#LASER_LOCATION = (2, 2)
#LASER_LOCATION = (11, 13)

def vaporize(input) -> (int, int):
	a = get_asteroids(input)
	m = map_to_angles(a)
	s = sort_asteroids_by_angle(m)
	c = combine_asteroids(s)
	
	def vaporize_next(astroids):
		res = []
		for j in astroids:
			if j != LASER_LOCATION and is_asteroid_detectable(LASER_LOCATION, j, a):
				return j
	
	i = 0
	j = 0
	while i < 199:
		j = j % len(c)
		
		to_vaporize = vaporize_next(c[j])
		i += 1
		a.remove(to_vaporize)
		c[j].remove(to_vaporize)
		if len(c[j]) == 0:
			del c[j]
			j -= 1
				
		j += 1
	print("DONE")
	return vaporize_next(c[j])

def map_to_angles(asteroids: [(int, int)]) -> [((int, int), float)] :
	if len(asteroids) == 0:
		return None
	res = []
	for a in asteroids:
		delta_x = LASER_LOCATION[0] - a[0]
		delta_y = LASER_LOCATION[1] - a[1]
		res.append((a, math.atan2(delta_x, delta_y)))
	return res
	
def sort_asteroids_by_angle(asteroids: [((int, int), float)]) -> [((int, int), float)]:
	def compare(a, b):
		if a[1] <= 0 and b[1] <= 0: return b[1] - a[1]
		if a[1] <= 0: return -1
		if b[1] <= 0: return 1
		else: return b[1] - a[1]
			
	return sorted(asteroids, key=functools.cmp_to_key(compare))
	
def combine_asteroids(asteroids):
	res = collections.OrderedDict()
	for a in asteroids:
		if a[1] not in res:
			res[a[1]] = [a[0]]
		else:
			res[a[1]].append(a[0])
	return list(res.values())
	
		
