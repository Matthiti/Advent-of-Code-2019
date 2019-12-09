## PART 1 ##
masses = [
	99603, 121503, 86996, 72052, 112039, 106616, 123581, 123171, 52480, 68686,
	66395, 102661, 110250, 73289, 105725, 123802, 75488, 79426, 98634, 76095,
	50852, 141405, 112388, 72180, 103300, 124602, 104531, 94751, 63270, 139027,
	145939, 62275, 91812, 74751, 144010, 60221, 62821, 51080, 149802, 53067,
	102574, 131339, 78942, 88430, 105314, 72764, 55214, 79095, 97458, 68699,
	106974, 141492, 57673, 141866, 139355, 134222, 52145, 83293, 144322, 70741,
	107873, 123638, 141011, 133249, 99065, 120480, 100767, 136550, 147323, 146988,
	65583, 141287, 53097, 50662, 121124, 94886, 59344, 93981, 112492, 149136,
	56647, 96430, 63968, 117987, 138475, 125958, 74967, 64480, 104644, 70273,
	50671, 147116, 147101, 89096, 94697, 83282, 74533, 68418, 145578, 59032
]


def get_fuel_of_module(mass: int) -> int:
	return int(mass / 3) - 2


def get_total_fuel(masses: [int]) -> int:
	sum = 0
	for mass in masses:
		sum += get_fuel_of_module(mass)
	return sum


#if __name__ == '__main__':
#print(get_total_fuel(masses))


## PART 2 ##
def get_total_fuel_with_mass_of_fuel(masses: [int]) -> int:
	sum = 0
	for mass in masses:
		fuel = mass
		while fuel > 0:
			fuel = get_fuel_of_module(fuel)
			if fuel > 0: sum += fuel
	return sum


if __name__ == '__main__':
	print(get_total_fuel_with_mass_of_fuel(masses))

