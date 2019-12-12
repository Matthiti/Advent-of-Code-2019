import copy

input = [[-1, -4, 0], [4, 7, -1], [-14, -10, 9], [1, 2, 17]]

#input = [[-1, 0, 2], [2, -10, -7], [4, -8, 8], [3, 5, -1]]

#input = [[-8, -10, 0], [5, 5, 10], [2, -7, 3], [9, -8, -3]]

AXIS = 3


def apply_gravity(positions: [[int, int, int]], velocities: [[int, int, int]]) -> [[int, int, int]]:
	for i in range(len(positions)):
		for j in range(i, len(positions)):
			for axis in range(AXIS):
				if positions[i][axis] > positions[j][axis]:
					velocities[i][axis] -= 1
					velocities[j][axis] += 1
				elif positions[i][axis] < positions[j][axis]:
					velocities[i][axis] += 1
					velocities[j][axis] -= 1
	return velocities
	

def apply_velocity(positions: [[int, int, int]], velocities: [[int, int, int]]) -> [[int, int, int]]:
	for i in range(len(positions)):
		for axis in range(AXIS):
			positions[i][axis] += velocities[i][axis]
	return positions
			

def energy(p: [int, int, int]) -> int:
	result = 0
	for axis in range(AXIS):
			result += abs(p[axis])
	return result
	
def total_energy(positions: [[int, int, int]], velocities: [[int, int, int]]) -> int:
	result = 0
	for i in range(len(positions)):
		potential_energy = energy(positions[i])
		kinetic_energy = energy(velocities[i])
		
		total = potential_energy * kinetic_energy
		result += total
	return result


def main(input = input) -> int:
	positions = copy.deepcopy(input)
	velocities = [[0, 0, 0] for _ in positions]
	
	for i in range(1000):
		apply_gravity(positions, velocities)
		apply_velocity(positions, velocities)
	
	return total_energy(positions, velocities)
	
## PART 2 ##

def find_steps_of_axis_before_repeat(positions: [int], velocities: [int]) -> int:
	original_pos = positions.copy()
	original_vel = velocities.copy()
	
	apply_gravity_to_axis(positions, velocities)
	apply_velocity_to_axis(positions, velocities)
	
	count = 1
	while positions != original_pos or velocities != original_vel:
		apply_gravity_to_axis(positions, velocities)
		apply_velocity_to_axis(positions, velocities)
		count += 1 
		
	return count

def apply_gravity_to_axis(positions: [int], velocities: [int]) -> [int]:
	for i in range(len(positions)):
		for j in range(i, len(positions)):
			if positions[i] > positions[j]:
				velocities[i] -= 1
				velocities[j] += 1
			elif positions[i] < positions[j]:
				velocities[i] += 1
				velocities[j] -= 1
	return velocities


def apply_velocity_to_axis(positions: [int], velocities: [int]) -> [int]:
	for i in range(len(positions)):
		positions[i] += velocities[i]
	return positions


def main_2(input = input) -> int:
	positions = copy.deepcopy(input)
	velocities = [[0, 0, 0] for _ in positions]
	
	counts = []
	for a in range(AXIS):
		res = find_steps_of_axis_before_repeat(([p[a] for p in positions]), ([v[a] for v in velocities]))
		counts.append(res)
	res = counts[0]
	for i in range(1, len(counts)):
		res = lcm(counts[i], res)
	
	return res
	

def gcd(a: int, b: int) -> int:
	if b == 0: return a
	return gcd(b, a % b)
	
	
def lcm(a: int, b: int) -> int:
	return a * b // gcd(a, b)
	
